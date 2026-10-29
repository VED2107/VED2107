#!/usr/bin/env python3
"""Generate first-party GitHub profile statistics SVG from public repository data.

The service produces no artificial contribution metrics and reads no private data.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
from pathlib import Path
import urllib.request
from xml.sax.saxutils import escape

USERNAME = "VED2107"
GITHUB_API = "https://api.github.com"


def get_json(url: str, token: str | None = None):
    if not url.startswith(GITHUB_API + "/"):
        raise ValueError("Only GitHub REST API URLs are permitted")
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "SNOWBROS-profile-signal",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = "Bearer " + token
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.load(response)


def public_owned_repos(username: str, token: str | None = None) -> list[dict]:
    """Fetch the full public-owned repository list with a pagination safety bound."""
    repos: list[dict] = []
    for page in range(1, 12):
        url = (f"{GITHUB_API}/users/{username}/repos"
               f"?type=owner&per_page=100&page={page}&sort=updated")
        batch = get_json(url, token)
        if not isinstance(batch, list):
            raise ValueError("GitHub returned a non-list repository response")
        repos.extend(row for row in batch
                     if isinstance(row, dict)
                     and not row.get("private")
                     and row.get("owner", {}).get("login", "").lower()
                     == username.lower())
        if len(batch) < 100:
            return repos
    raise ValueError("Pagination exceeded safety limit of 1100 repositories")


def calculate_signal(repos: list[dict], today: dt.date) -> dict:
    original = [repo for repo in repos if not repo.get("fork") and not repo.get("archived")]
    counts: dict[str, int] = {}
    for repo in original:
        language = repo.get("language")
        if isinstance(language, str) and language.strip():
            counts[language] = counts.get(language, 0) + 1
    recent = 0
    for repo in repos:
        value = str(repo.get("pushed_at") or "")[:10]
        try:
            pushed = dt.date.fromisoformat(value)
        except ValueError:
            continue
        if 0 <= (today - pushed).days < 30:
            recent += 1
    return {
        "public_repositories": len(repos),
        "total_stars": sum(max(0, int(r.get("stargazers_count") or 0)) for r in repos),
        "recent_pushes": recent,
        "languages": sorted(counts.items(), key=lambda item: (-item[1], item[0]))[:5],
        "date": today.isoformat(),
    }


def render_svg(data: dict) -> str:
    """Render static SVG; inputs escape XML and there are no external SVG dependencies."""
    def text(x, y, value, size=15, color="#F2F0EB", weight=400):
        return (f'<text x="{x}" y="{y}" fill="{color}" font-size="{size}"'
                f' font-family="Segoe UI,Helvetica,Arial,sans-serif" font-weight="{weight}">'
                f'{escape(str(value))}</text>')
    markup = [
        '<svg xmlns="http://www.w3.org/2000/svg" width="1160" height="320"'
        ' viewBox="0 0 1160 320" role="img">',
        '<title>VED2107: public GitHub metrics and languages</title>',
        '<desc>Public repository count, total stars, recent pushes, and primary languages from owned original repositories.</desc>',
        '<rect width="1160" height="320" rx="20" fill="#111110"/>',
        '<rect x="18" y="17" width="1124" height="285" rx="16" fill="#1A1918" stroke="#2E2C29"/>',
        '<circle cx="34" cy="43" r="5" fill="#FF4F1F"/>',
        text(51, 48, "PUBLIC SIGNAL / GITHUB API", 15, "#F2F0EB", 700),
        text(903, 48, "UPDATED " + data["date"], 13, "#8C887F"),
        '<path d="M20 66H1140" stroke="#2E2C29"/>'
    ]
    metrics = [
        ("PUBLIC REPOS", data["public_repositories"]),
        ("TOTAL STARS", data["total_stars"]),
        ("PUSHED IN 30D", data["recent_pushes"])
    ]
    for i, (label, number) in enumerate(metrics):
        x = 43 + i * 205
        markup.extend([text(x, 136, number, 52, "#F2F0EB", 800),
                       text(x, 165, label, 13, "#8C887F", 700)])
        if i < 2:
            markup.append(f'<path d="M{x + 182} 94V174" stroke="#2E2C29"/>')
    markup.extend([
        text(43, 218, "LANGUAGE SIGNATURE", 14, "#FF4F1F", 700),
        text(43, 245, "Primary languages of original public repositories", 13, "#C9C5BC"),
        text(43, 276, "Public GitHub metadata only. No private contributions or synthetic scores.", 12, "#8C887F"),
        '<path d="M672 85V284" stroke="#2E2C29"/>'
    ])
    languages = data["languages"]
    top = max((count for _, count in languages), default=1)
    if not languages:
        markup.append(text(704, 142, "No public language data", 16, "#C9C5BC"))
    for index, (language, count) in enumerate(languages):
        y = 96 + index * 37
        markup.extend([
            text(703, y + 14, language[:15], 14, "#F2F0EB"),
            f'<rect x="835" y="{y}" width="228" height="19" rx="2" fill="#2E2C29"/>',
            f'<rect x="835" y="{y}" width="{max(6, round(228 * count / top))}"'
            f' height="19" rx="2" fill="{"#FF4F1F" if index == 0 else "#C9C5BC"}"/>',
            text(1082, y + 15, count, 13, "#F2F0EB", 700),
        ])
    markup.append('<rect x="0" y="315" width="1160" height="5" fill="#FF4F1F"/>')
    markup.append("</svg>")
    return "\n".join(markup) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=Path("dist"))
    parser.add_argument("--fixture", type=Path, default=None,
                        help="Offline JSON list fixture for local tests")
    parser.add_argument("--date", type=dt.date.fromisoformat,
                        default=dt.datetime.now(dt.timezone.utc).date())
    opts = parser.parse_args()
    repos = (json.loads(opts.fixture.read_text(encoding="utf-8")) if opts.fixture
             else public_owned_repos(USERNAME, os.getenv("GITHUB_TOKEN")))
    svg = render_svg(calculate_signal(repos, opts.date))
    opts.output_dir.mkdir(parents=True, exist_ok=True)
    (opts.output_dir / "profile-signal.svg").write_text(svg, encoding="utf-8")
    print(f"Generated first-party profile signal for {len(repos)} public repositories")


if __name__ == "__main__":
    main()
