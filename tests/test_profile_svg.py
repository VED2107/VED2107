import datetime as dt
import importlib.util
from pathlib import Path
import unittest
import xml.etree.ElementTree as ET

script = Path(__file__).resolve().parents[1] / "scripts" / "generate_profile.py"
spec = importlib.util.spec_from_file_location("profile_generator", script)
assert spec and spec.loader
profile = importlib.util.module_from_spec(spec)
spec.loader.exec_module(profile)


class ProfileSignalTests(unittest.TestCase):
    def test_counts_are_grounded_in_repository_metadata(self):
        rows = [
            {"language": "Rust", "stargazers_count": 4,
             "pushed_at": "2026-10-20T00:00:00Z"},
            {"language": "Python", "stargazers_count": 1, "fork": True,
             "pushed_at": "2026-10-01T00:00:00Z"},
            {"language": "TypeScript", "stargazers_count": 2, "archived": True,
             "pushed_at": "2026-08-09T00:00:00Z"}
        ]
        data = profile.calculate_signal(rows, dt.date(2026, 10, 29))
        self.assertEqual(data["public_repositories"], 3)
        self.assertEqual(data["total_stars"], 7)
        self.assertEqual(data["recent_pushes"], 2)
        self.assertEqual(data["languages"], [("Rust", 1)])
        root = ET.fromstring(profile.render_svg(data))
        self.assertEqual(root.tag, "{http://www.w3.org/2000/svg}svg")

    def test_escaping_and_empty_data(self):
        data = profile.calculate_signal(
            [{"language": "R&D <script>", "stargazers_count": 0,
              "pushed_at": "not-a-date"}], dt.date(2026, 10, 29))
        svg = profile.render_svg(data)
        ET.fromstring(svg)
        self.assertIn("R&amp;D &lt;script&gt;", svg)
        self.assertNotIn("<script>", svg)
        ET.fromstring(profile.render_svg(
            profile.calculate_signal([], dt.date(2026, 10, 29))))

    def test_future_push_is_not_recent(self):
        rows = [{"pushed_at": "2026-11-12T12:00:00Z"}]
        data = profile.calculate_signal(rows, dt.date(2026, 10, 29))
        self.assertEqual(data["recent_pushes"], 0)


if __name__ == "__main__":
    unittest.main()
