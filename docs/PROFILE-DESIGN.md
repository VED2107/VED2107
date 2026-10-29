# GitHub profile — design and maintenance

This repository is the public GitHub profile of VED2107. The source is deliberately
GitHub-native Markdown and first-party vector artwork.

## Visual system
- The SNOWBROS identity: Ink (#111110), Paper (#F2F0EB), Signal (#FF4F1F), the Hex S
  symbol, Archivo for display and Geist for text. Brand kit: `VED2107/snowbros/brand`.
- Each product card keeps its own tone from the studio site (snowbros.me work section),
  with the same line-drawn emblem.
- `scripts/build_art.py` regenerates every `assets/*.svg`; text is outlined from the fonts
  because GitHub's image sandbox cannot load web fonts. Edit the script, not the SVGs.
- Real product screenshots are hosted in `VED2107/snowbros/public/work`.
- Never present research predictions as medical efficacy, or unfinished builds as releases.

## Live signal
`scripts/generate_profile.py` uses `GET /users/VED2107/repos` with pagination
and the workflow's own GITHUB_TOKEN. It counts publicly owned repositories, stars
on those repositories, and repos with a `pushed_at` date in the preceding 30 days.
Language bars count the *primary language* of original (non-fork, non-archived)
public repositories, **not** total code bytes or commit history.

`snake.yml` is the sole owner of the output branch. It validates the Python
generator, regenerates the public metric card and snake in the same `dist/`
directory, and publishes them together every 12 hours and on pushes to main.
Pull requests only run the unit tests: no write permissions are needed for PRs.

Run the unit tests locally:

```sh
python3 -m unittest discover -s tests -v
```

The README's remote `output/profile-signal.svg` link becomes available once the
first successful `main` publication completes. An initial missing graphic means
the publisher has not completed yet; do not fabricate numbers as a placeholder.
If GitHub's REST API fails, the workflow fails rather than publishing guessed
data. Check Actions and the output branch; the previous output is retained.

## Updating projects
Match the project README for features, verify live links, update real screenshots
in the studio gallery, and put technical/scientific limitations near the claims.
The canonical research repository is
`amrdrugrepurposing/amr-drug-repurposing-1`.
