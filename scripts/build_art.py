#!/usr/bin/env python3
"""Build the README artwork in the SNOWBROS identity.

Text is outlined from Archivo and Geist (SIL OFL) so the SVGs render identically inside
GitHub's <img> sandbox, which cannot load web fonts. Emblems are the same line drawings the
studio site uses (snowbros.me, src/studio/emblems.ts); each product keeps its own tone.

    python3 scripts/build_art.py --fonts <dir with Archivo.ttf and Geist.ttf>

Fonts: https://github.com/google/fonts/tree/main/ofl/archivo and .../ofl/geist
Requires fontTools (pip install fonttools).
"""
from __future__ import annotations

import argparse
import math
import re
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"
S3 = math.sqrt(3)
TAU = math.tau

INK, PAPER, STONE, SIGNAL, MUTE = "#111110", "#F2F0EB", "#C9C5BC", "#FF4F1F", "#8C887F"

# Hex S symbol, 256-unit master (brand/masters/symbol in VED2107/snowbros).
HEX_S = [(66, 20.61), (190, 20.61), (216.71, 66.87), (97.03, 66.87), (75.09, 104.87),
         (238.65, 104.87), (252, 128), (190, 235.39), (66, 235.39), (39.29, 189.13),
         (158.97, 189.13), (180.91, 151.13), (17.35, 151.13), (4, 128)]


def n(v: float) -> str:
    return f"{v:.2f}".rstrip("0").rstrip(".")


class Face:
    def __init__(self, path: Path, axes: dict[str, float]):
        font = instantiateVariableFont(TTFont(path), axes)
        self.glyphs = font.getGlyphSet()
        self.cmap = font.getBestCmap()
        self.cap = font["OS/2"].sCapHeight

    def width(self, txt: str, size: float, track: float = 0) -> float:
        s = size / self.cap
        return sum(self.glyphs[self.cmap[ord(c)]].width * s for c in txt) + track * size * (len(txt) - 1)

    def path(self, txt: str, x: float, baseline: float, size: float, track: float = 0) -> str:
        """`size` is the cap height in px."""
        s = size / self.cap
        out = []
        for ch in txt:
            g = self.glyphs[self.cmap[ord(ch)]]
            pen = SVGPathPen(self.glyphs, ntos=n)
            g.draw(TransformPen(pen, (s, 0, 0, -s, x, baseline)))
            out.append(pen.getCommands())
            x += g.width * s + track * size
        return " ".join(p for p in out if p)


def text(face: Face, txt: str, x: float, baseline: float, size: float, fill: str,
         track: float = 0, anchor: str = "start", max_w: float | None = None) -> str:
    w = face.width(txt, size, track)
    if max_w and w > max_w:
        size *= max_w / w
        w = max_w
    if anchor == "end":
        x -= w
    elif anchor == "middle":
        x -= w / 2
    return f'<path fill="{fill}" d="{face.path(txt, x, baseline, size, track)}"/>'


def hex_s(x: float, y: float, h: float, fill: str) -> str:
    k = h / 214.78
    pts = " ".join(f"{n(x + (px - 4) * k)},{n(y + (py - 20.61) * k)}" for px, py in HEX_S)
    return f'<polygon fill="{fill}" points="{pts}"/>'


def lattice(x0: float, y0: float, w: float, h: float, cell: float, color: str, opacity: float) -> str:
    hh = cell * S3 / 2
    d = []
    y = 0.0
    while y <= h:
        d.append(f"M{n(x0)},{n(y0 + y)}H{n(x0 + w)}")
        y += hh
    span = h / S3
    x = -span
    while x <= w + span:
        d.append(f"M{n(x0 + x)},{n(y0)}L{n(x0 + x + span)},{n(y0 + h)}")
        d.append(f"M{n(x0 + x + span)},{n(y0)}L{n(x0 + x)},{n(y0 + h)}")
        x += cell
    return (f'<path d="{" ".join(d)}" stroke="{color}" stroke-width="1" fill="none"'
            f' opacity="{opacity}"/>')


# ---- emblems, unit space -1..1 (ported from the studio site)
def arc(cx, cy, r, a0, a1, steps=48):
    return [(cx + math.cos(a0 + (a1 - a0) * i / steps) * r, cy + math.sin(a0 + (a1 - a0) * i / steps) * r,
             cx + math.cos(a0 + (a1 - a0) * (i + 1) / steps) * r, cy + math.sin(a0 + (a1 - a0) * (i + 1) / steps) * r)
            for i in range(steps)]


def poly(pts, closed=True):
    m = len(pts) if closed else len(pts) - 1
    return [(*pts[i], *pts[(i + 1) % len(pts)]) for i in range(m)]


def hexagon(cx, cy, r, rot=0.0):
    return poly([(cx + math.cos(rot + i * TAU / 6) * r, cy + math.sin(rot + i * TAU / 6) * r) for i in range(6)])


def emblem(kind: str):
    if kind == "graph":
        nodes = [(-.8, -.7), (-.1, -.85), (.7, -.6), (-.55, -.05), (.2, .05), (.85, .15), (-.75, .7), (0, .8), (.6, .75)]
        edges = [(0, 3), (0, 4), (1, 4), (2, 4), (2, 5), (3, 6), (3, 7), (4, 7), (4, 8), (5, 8), (7, 8), (8, 4)]
        segs = [(*nodes[a], *nodes[b]) for a, b in edges]
        for x, y in nodes:
            segs += arc(x, y, .09, 0, TAU, 14)
        return segs
    if kind == "play":
        return arc(0, 0, .92, 0, TAU, 72) + arc(0, 0, .8, 0, TAU, 64) + poly([(-.28, -.42), (.44, 0), (-.28, .42)]) \
            + poly([(-.2, -.28), (.27, 0), (-.2, .28)])
    if kind == "molecule":
        r = .34
        dx = r * S3
        segs = hexagon(-dx, .1, r, math.pi / 6) + hexagon(0, .1, r, math.pi / 6) + hexagon(dx * .5, -.42, r, math.pi / 6)
        segs += arc(-dx, .1, r * .55, 0, TAU, 20) + arc(dx * .5, -.42, r * .55, 0, TAU, 20)
        segs += [(0, .1 + r, 0, .1 + r + .38), (-dx - r * .86, .1 + r * .5, -dx - r * .86 - .3, .1 + r * .5 + .18)]
        return segs + arc(0, .1 + r + .46, .08, 0, TAU, 12)
    if kind == "transfer":
        segs = poly([(-.95, -.55), (-.55, -.55), (-.55, .55), (-.95, .55)]) + [(-.83, .42, -.67, .42)]
        segs += poly([(.25, -.45), (.95, -.45), (.95, .2), (.25, .2)]) + [(.6, .2, .6, .42), (.42, .42, .78, .42)]
        return segs + arc(-.15, .1, .62, math.pi * 1.12, math.pi * 1.88, 18)[::2]
    if kind == "ledger":
        segs = [(-.9, -.7, .9, -.7), (0, -.7, 0, .62), (-.9, .62, .9, .62), (-.9, .76, .9, .76)]
        for i in range(5):
            y = -.5 + i * .24
            segs += [(-.8, y, -.8 + .3 + ((i * 37) % 5) * .08, y), (.1, y, .1 + .25 + ((i * 53) % 5) * .09, y)]
        return segs
    if kind == "terminal":
        segs = poly([(-.95, -.7), (.95, -.7), (.95, .7), (-.95, .7)]) + [(-.95, -.45, .95, -.45)]
        segs += [(-.6, -.1, -.3, .12), (-.3, .12, -.6, .34), (-.15, .34, .3, .34)]
        for i in range(3):
            segs += arc(-.8 + i * .13, -.58, .04, 0, TAU, 10)
        return segs
    if kind == "wave":
        pts = [(-.95 + i * 1.9 / 60, .42 * math.sin(i / 60 * TAU * 1.5) * (1 - abs(i - 30) / 45)) for i in range(61)]
        segs = [(*pts[i], *pts[i + 1]) for i in range(60)]
        for t in (0, 20, 40, 60):
            segs += arc(pts[t][0], pts[t][1], .06, 0, TAU, 12)
        segs += [(-.95, -.7, .95, -.7), (-.95, .7, .95, .7)]
        return segs
    raise ValueError(kind)


def draw_emblem(kind: str, cx: float, cy: float, r: float, color: str, width: float = 2.4) -> str:
    d = " ".join(f"M{n(cx + a * r)},{n(cy + b * r)}L{n(cx + c * r)},{n(cy + e * r)}" for a, b, c, e in emblem(kind))
    return (f'<path d="{d}" stroke="{color}" stroke-width="{width}" stroke-linecap="round"'
            f' stroke-linejoin="round" fill="none"/>')


def svg(w: int, h: int, label: str, body: str) -> str:
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}"'
            f' role="img" aria-label="{label}"><title>{label}</title>{body}</svg>\n')


# ---- motion: CSS inside the SVG. GitHub serves README images through its proxy and browsers play
# CSS animations in <img> SVGs. Every element's resting state is its final state, so a viewer with
# reduced motion (or a renderer without animation) sees the finished artwork.
EASE_OUT = "cubic-bezier(0.23, 1, 0.32, 1)"
EASE_IN_OUT = "cubic-bezier(0.77, 0, 0.175, 1)"
MOTION = (
    "<style>"
    f".draw{{stroke-dasharray:1;animation:draw 1.5s {EASE_IN_OUT} .2s both,fillin .5s {EASE_OUT} 1.5s both}}"
    "@keyframes draw{from{stroke-dashoffset:1}to{stroke-dashoffset:0}}"
    "@keyframes fillin{from{fill-opacity:0}to{fill-opacity:1}}"
    f".rise{{animation:rise .8s {EASE_OUT} both}}"
    "@keyframes rise{from{opacity:0;transform:translateY(12px)}to{opacity:1;transform:none}}"
    ".pulse{animation:pulse 3.6s ease-in-out 2.4s infinite}"
    "@keyframes pulse{0%,100%{fill-opacity:.12}50%{fill-opacity:.32}}"
    "@media (prefers-reduced-motion: reduce){*{animation:none!important}}"
    "</style>"
)


def hex_s_drawn(x: float, y: float, h: float, color: str) -> str:
    k = h / 214.78
    d = "M" + " L".join(f"{n(x + (px - 4) * k)},{n(y + (py - 20.61) * k)}" for px, py in HEX_S) + " Z"
    return (f'<path class="draw" d="{d}" pathLength="1" fill="{color}" stroke="{color}" stroke-width="2"'
            f' stroke-linejoin="round"/>')


def rise(inner: str, delay: float) -> str:
    return f'<g class="rise" style="animation-delay:{delay:.2f}s">{inner}</g>'


def signal_cell(W: int, H: int, cell: int, col: int, row: int) -> str:
    hh = cell * S3 / 2
    span = H / S3
    x0 = -span + math.ceil(span / cell) * cell
    cx, cy = x0 + row * cell / 2 + col * cell, hh * row
    pts = " ".join(f"{n(cx + cell * math.cos(i * TAU / 6))},{n(cy + cell * math.sin(i * TAU / 6))}" for i in range(6))
    return f'<polygon class="pulse" points="{pts}" fill="{SIGNAL}" fill-opacity=".12" stroke="{SIGNAL}" stroke-width="2"/>'


def wordmark(x: float, y: float, w: float, color: str) -> str:
    src = (ASSETS / "brand" / "wordmark-paper.svg").read_text(encoding="utf-8")
    vw, vh = [float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', src).group(1, 2)]
    ds = re.findall(r' d="([^"]+)"', src)
    k = w / vw
    paths = "".join(f'<path fill="{color}" fill-rule="evenodd" d="{d}"/>' for d in ds)
    return f'<g transform="translate({n(x)} {n(y)}) scale({k:.5f})">{paths}</g>'


def build(fonts: Path) -> None:
    display = Face(fonts / "Archivo.ttf", {"wght": 800, "wdth": 125})
    title = Face(fonts / "Archivo.ttf", {"wght": 700, "wdth": 112})
    body = Face(fonts / "Geist.ttf", {"wght": 400})
    label = Face(fonts / "Geist.ttf", {"wght": 500})

    # ---- cover
    W, H = 1280, 440
    hh = 44 * S3 / 2
    span = H / S3
    x0 = -span + math.ceil(span / 44) * 44  # first lattice vertex on the top edge
    cx, cy = x0 + 5 * 22 + 21 * 44, hh * 5  # a vertex five rows down, on the right
    cell = " ".join(f"{n(cx + 44 * math.cos(i * TAU / 6))},{n(cy + 44 * math.sin(i * TAU / 6))}" for i in range(6))
    cover = [
        f'<rect width="{W}" height="{H}" rx="16" fill="{INK}"/>',
        f'<g>{lattice(0, 0, W, H, 44, STONE, .1)}</g>',
        f'<rect width="{W}" height="{H}" rx="16" fill="url(#fade)"/>',
        signal_cell(W, H, 44, 21, 5),
        hex_s_drawn(64, 56, 34, PAPER),
        rise(text(label, "SNOWBROS  /  FOUNDER", 120, 82, 13, STONE, .16), .5),
        rise(text(label, "PATAN, GUJARAT  /  WORKING WORLDWIDE", W - 64, 82, 13, MUTE, .16, "end"), .6),
        rise(text(display, "VED CHAUHAN", 64, 250, 96, PAPER, .01, max_w=900), .9),
        rise(text(body, "I build the engine and the experience: Rust developer tools,", 64, 310, 21, STONE), 1.2),
        rise(text(body, "cross-platform products and interfaces that tell you what they did.", 64, 344, 21, STONE), 1.3),
        rise(text(label, "RUST  ·  TYPESCRIPT  ·  PYTHON  ·  FLUTTER", 64, 392, 13, MUTE, .16), 1.6),
        rise(text(label, "VED.EXE.SNOWBROS.ME", W - 64, 392, 13, SIGNAL, .16, "end"), 1.7),
    ]
    defs = (f'<defs><linearGradient id="fade" x2="1"><stop offset=".25" stop-color="{INK}"/>'
            f'<stop offset=".75" stop-color="{INK}" stop-opacity="0"/></linearGradient></defs>')
    (ASSETS / "cover.svg").write_text(svg(W, H, "Ved Chauhan, founder of SNOWBROS. I build the engine and the experience.",
                                          MOTION + defs + "".join(cover)), encoding="utf-8")
    build_org(display, title, body, label)

    # ---- project cards: each product keeps its own tone (snowbros.me work section)
    cards = [
        ("amr", "01", "RESEARCH INTERFACE", "AMR Screening", "AI-assisted screening of 1,761 approved medicines",
         "against four drug-resistant bacteria.", "PYTHON · RDKIT · AUTODOCK VINA · NEXT.JS", "#E7EFEC", "#10302A", "molecule"),
        ("nova", "02", "DESKTOP PRODUCT", "NOVA", "A privacy-first media player that shows only what",
         "its engine confirms. No account, no telemetry.", "RUST · TAURI 2 · REACT · LIBMPV", "#141312", "#F4F1EA", "play"),
        ("swiftdrop", "03", "CROSS-PLATFORM APP", "SwiftDrop", "Photos and files straight between phone and PC",
         "over your own Wi-Fi. No cloud, no account.", "FLUTTER · NODE · WEBRTC", "#191617", "#F6EFEC", "transfer"),
        ("accounic", "04", "CROSS-PLATFORM PRODUCT", "Accounic", "A multi-currency ledger: web, Android and Windows",
         "on one Postgres schema that owns every balance.", "NEXT.JS · FLUTTER · SUPABASE / POSTGRES", "#1B1A17", "#F2F0EB", "ledger"),
        ("atlas", "05", "DEVELOPER TOOL · OPEN SOURCE", "Snowbros Atlas", "Static analysis for JS, TS and Python that reports",
         "only what it can prove, with the evidence.", "RUST · TREE-SITTER · LSP · VS CODE", "#1F2B24", "#F2F0EB", "graph"),
        ("vedexe", "06", "INTERACTIVE PORTFOLIO", "VED.EXE", "A portfolio you play: terminal, CRT and RPG",
         "mechanics wired to live GitHub data.", "NEXT.JS · TYPESCRIPT · GSAP", INK, PAPER, "terminal"),
    ]
    W, H = 1280, 300
    for slug, idx, kicker, name, l1, l2, stack, tone, tink, kind in cards:
        muted = "#5C6B66" if tone.startswith("#E") else "#9C988F"
        body_c = tink
        parts = [
            f'<rect width="{W}" height="{H}" rx="16" fill="{tone}"/>',
            text(label, idx, 56, 66, 13, SIGNAL, .16),
            text(label, kicker, 96, 66, 13, muted, .16),
            text(title, name, 56, 150, 58, tink, 0, max_w=720),
            text(body, l1, 56, 204, 20, body_c),
            text(body, l2, 56, 234, 20, body_c),
            text(label, stack, 56, 264, 12, muted, .16),
            draw_emblem(kind, 1060, 150, 96, tink),
        ]
        (ASSETS / f"project-{slug}.svg").write_text(svg(W, H, f"{name}: {l1} {l2}", "".join(parts)), encoding="utf-8")

    # ---- sign-off
    W, H = 1280, 280
    off = [
        f'<rect width="{W}" height="{H}" rx="16" fill="{SIGNAL}"/>',
        hex_s(64, 52, 40, INK),
        text(display, "BRING ME SOMETHING", 64, 156, 38, INK, .01),
        text(display, "THAT HAS TO HOLD.", 64, 204, 38, INK, .01),
        text(label, "SNOWBROS.ME   ·   VEDCHAUHAN2107@GMAIL.COM   ·   LINKEDIN.COM/IN/VED-CHAUHAN2107",
             64, 244, 13, INK, .16),
    ]
    (ASSETS / "signoff.svg").write_text(svg(W, H, "Bring me something that has to hold. snowbros.me, vedchauhan2107@gmail.com",
                                            "".join(off)), encoding="utf-8")


ORG_OUT: Path | None = None


def build_org(display: Face, title: Face, body: Face, label: Face) -> None:
    """Artwork for the snowbros-labs organisation profile (written to ORG_OUT)."""
    if ORG_OUT is None:
        return
    ORG_OUT.mkdir(parents=True, exist_ok=True)

    # ---- hero
    W, H = 1280, 400
    hero = [
        f'<rect width="{W}" height="{H}" rx="16" fill="{INK}"/>',
        f'<g>{lattice(0, 0, W, H, 44, STONE, .1)}</g>',
        f'<rect width="{W}" height="{H}" rx="16" fill="url(#fade)"/>',
        signal_cell(W, H, 44, 25, 3),
        hex_s_drawn(64, 64, 132, PAPER),
        rise(wordmark(262, 92, 560, PAPER), .9),
        rise(text(display, "SOFTWARE THAT HOLDS ITS SHAPE.", 264, 184, 20, SIGNAL, .02, max_w=556), 1.2),
        rise(text(body, "An independent engineering studio. Developer tools, products and interfaces", 64, 280, 21, STONE), 1.5),
        rise(text(body, "that tell you what they actually did. Same input in, same result out.", 64, 314, 21, STONE), 1.6),
        rise(text(label, "RUST  ·  TYPESCRIPT  ·  PYTHON  ·  FLUTTER", 64, 360, 13, MUTE, .16), 1.9),
        rise(text(label, "SNOWBROS.ME", W - 64, 360, 13, SIGNAL, .16, "end"), 2.0),
    ]
    defs = (f'<defs><linearGradient id="fade" x2="1"><stop offset=".3" stop-color="{INK}"/>'
            f'<stop offset=".8" stop-color="{INK}" stop-opacity="0"/></linearGradient></defs>')
    (ORG_OUT / "hero.svg").write_text(svg(W, H, "SNOWBROS. Software that holds its shape.", MOTION + defs + "".join(hero)),
                                      encoding="utf-8")

    # ---- open-source cards (same system as the studio work cards)
    W, H = 1280, 300
    cards = [
        ("creative-engineering", "OPEN SOURCE · TOOLKIT", "Creative Engineering",
         "An agent skill and eight TypeScript packages for motion,", "scroll, interactive 3D and interfaces. It builds snowbros.me.",
         "TYPESCRIPT · THREE.JS · WEB COMPONENTS", "#16181C", "#EEF0F2", "#9AA0A8", "wave"),
        ("mentor", "OPEN SOURCE · CLAUDE CODE SKILL", "Mentor",
         "An engineering-intelligence skill that teaches or builds,", "routing each task to only the expertise it needs.",
         "AGENT SKILL · MARKDOWN", "#1A1916", "#F2F0EB", "#9C988F", "terminal"),
    ]
    for slug, kicker, name, l1, l2, stack, tone, tink, muted, kind in cards:
        parts = [
            f'<rect width="{W}" height="{H}" rx="16" fill="{tone}"/>',
            text(label, kicker, 56, 66, 13, muted, .16),
            text(title, name, 56, 150, 58, tink, 0, max_w=720),
            text(body, l1, 56, 204, 20, tink),
            text(body, l2, 56, 234, 20, tink),
            text(label, stack, 56, 264, 12, muted, .16),
            draw_emblem(kind, 1060, 150, 96, tink),
        ]
        (ORG_OUT / f"project-{slug}.svg").write_text(svg(W, H, f"{name}: {l1} {l2}", "".join(parts)), encoding="utf-8")

    # ---- principles: four rules as a spec sheet
    W, H = 1280, 360
    rules = [("01", "Deterministic", "Same input, identical output, sorted and stable."),
             ("02", "Evidence first", "Every finding, balance and status carries its proof."),
             ("03", "One source of truth", "One place does the maths. Clients only read it."),
             ("04", "Honest status", "We say what is tested, what is not, and where.")]
    parts = [f'<rect width="{W}" height="{H}" rx="16" fill="{PAPER}"/>',
             text(label, "HOW WE BUILD", 56, 64, 13, "#B8340D", .16)]
    colw = (W - 112) / 4
    # one heading size for all four, set by the longest so none crowds its neighbour
    head_size = min(20, min(20 * (colw - 36) / title.width(h, 20) for _, h, _ in rules))
    for i, (num, head, line) in enumerate(rules):
        x = 56 + i * colw
        parts += [
            f'<path d="M{n(x)},104H{n(x + colw - 24)}" stroke="{INK}" stroke-width="2"/>',
            rise(text(display, num, x, 170, 34, SIGNAL, .01), .2 + i * .12),
            rise(text(title, head, x, 228, head_size, INK, 0), .3 + i * .12),
        ]
        words, lines, cur = line.split(), [], ""
        for w_ in words:
            trial = (cur + " " + w_).strip()
            if body.width(trial, 16) > colw - 40 and cur:
                lines.append(cur); cur = w_
            else:
                cur = trial
        lines.append(cur)
        for j, ln in enumerate(lines):
            parts.append(rise(text(body, ln, x, 270 + j * 26, 16, "#3B3935"), .4 + i * .12))
    (ORG_OUT / "principles.svg").write_text(svg(W, H, "How we build: deterministic, evidence first, one source of truth, honest status.",
                                                MOTION + "".join(parts)), encoding="utf-8")

    # ---- sign-off
    W, H = 1280, 280
    off = [
        f'<rect width="{W}" height="{H}" rx="16" fill="{SIGNAL}"/>',
        hex_s(64, 52, 40, INK),
        text(display, "BRING US SOMETHING", 64, 156, 38, INK, .01),
        text(display, "THAT HAS TO HOLD.", 64, 204, 38, INK, .01),
        text(label, "SNOWBROS.ME   ·   HELLO@SNOWBROS.ME   ·   LINKEDIN.COM/COMPANY/SNOWBROS-STUDIO",
             64, 244, 13, INK, .16),
    ]
    (ORG_OUT / "signoff.svg").write_text(svg(W, H, "Bring us something that has to hold. snowbros.me, hello@snowbros.me",
                                             "".join(off)), encoding="utf-8")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--fonts", type=Path, required=True)
    ap.add_argument("--org", type=Path, default=None, help="also write the snowbros-labs profile art here")
    args = ap.parse_args()
    ORG_OUT = args.org
    build(args.fonts)
