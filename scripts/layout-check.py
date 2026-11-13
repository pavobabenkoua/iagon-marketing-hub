#!/usr/bin/env python3
"""Check a new or changed layout against the attention rules, before approval.

Run it before the layout goes to the director. Approved layouts are not
re-checked on every render: only their data changes.

Usage:
  python3 scripts/layout-check.py --layout layouts/weekly-cover dist/development-update-weekly/2026-W44/cover.png
  python3 scripts/layout-check.py --strict card-1.png card-2.png

For the layout folder (--layout) it reads the HTML, CSS and SVG and reports
  colors outside the palette (wiki/brand/visual/colors-typography.md, logo.md)
  and grayscale filters: the palette neutrals are cool and slightly violet.
For every PNG it reports:
  purple share        purple pixels as a share of the canvas; limit 1/8
  purple spots        separate purple areas; limit 2 (the logo symbol + one accent)
  light purple tint   purple-tinted pale areas, a sign of decoration in purple
and writes <name>.squint.png next to it: the canvas at feed size (one third)
and the same blurred, for the squint test. The title must read first,
decoration last.

Lines starting with "!" are deviations. Without --strict the script only
reports them (the director decides); with --strict it exits with code 1.

Rules: wiki/brand/visual/colors-typography.md, section 5 (Color balance, Attention).
Needs Pillow, numpy and scipy.
"""
import argparse
import re
import sys
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage

# Brand purples: #6F47FF (253°), #7C75FF (243°), #885EFF (256°). Neutrals
# (#62687E 227°, #141A21 212°, #F6F6FB, #EAEBF5) fall outside this hue band
# or below the saturation floor.
HUE = (235, 280)
STRONG_SAT, STRONG_VAL = 0.35, 0.45
TINT_SAT, TINT_VAL = 0.08, 0.80

PURPLE_LIMIT = 1 / 8
SPOT_LIMIT = 2
TINT_LIMIT = 0.01
FEED_SCALE = 1 / 3


def hsv(img):
    a = np.asarray(img.convert("RGB"), dtype=np.float32) / 255
    r, g, b = a[..., 0], a[..., 1], a[..., 2]
    mx, mn = a.max(-1), a.min(-1)
    d = mx - mn
    s = np.where(mx > 0, d / np.maximum(mx, 1e-6), 0)
    h = np.zeros_like(mx)
    nz = d > 1e-6
    rr = nz & (mx == r)
    gg = nz & (mx == g) & ~rr
    bb = nz & ~rr & ~gg
    h[rr] = ((g - b)[rr] / d[rr]) % 6
    h[gg] = (b - r)[gg] / d[gg] + 2
    h[bb] = (r - g)[bb] / d[bb] + 4
    return h * 60, s, mx, d


def spots(mask, width):
    """Separate purple areas. Strokes closer than ~1.5% of the width count as one area."""
    if not mask.any():
        return []
    gap = max(3, int(width * 0.015))
    grown = ndimage.binary_dilation(mask, iterations=gap)
    labels, n = ndimage.label(grown)
    floor = mask.size * 0.0002  # ignore anti-aliasing specks
    out = []
    for sl, i in zip(ndimage.find_objects(labels), range(1, n + 1)):
        area = int((mask[sl] & (labels[sl] == i)).sum())
        if area >= floor:
            out.append((sl[1].start, sl[0].start, sl[1].stop, sl[0].stop, area))
    return out


def squint(img, path):
    w, h = img.size
    small = img.convert("RGB").resize((max(1, int(w * FEED_SCALE / 2)), max(1, int(h * FEED_SCALE / 2))), Image.LANCZOS)
    blurred = small.filter(ImageFilter.GaussianBlur(radius=max(2, small.width // 120)))
    sheet = Image.new("RGB", (small.width * 2 + 24, small.height), "#d9dbe6")
    sheet.paste(small, (0, 0))
    sheet.paste(blurred, (small.width + 24, 0))
    sheet.save(path)


def check(path, scale=2):
    """Return (report lines, number of deviations)."""
    path = Path(path)
    img = Image.open(path)
    h, s, v, _ = hsv(img)
    total = h.size
    band = (h >= HUE[0]) & (h <= HUE[1])
    strong = band & (s >= STRONG_SAT) & (v >= STRONG_VAL)
    tint = band & (s >= TINT_SAT) & (s < STRONG_SAT) & (v >= TINT_VAL)

    share = strong.sum() / total
    found = spots(strong, img.width)
    tint_share = tint.sum() / total

    lines, bad = [f"{path.name}  {img.width // scale}x{img.height // scale}"], 0

    def row(ok, text):
        nonlocal bad
        bad += not ok
        lines.append(f"  {'  ' if ok else '! '}{text}")

    row(share <= PURPLE_LIMIT, f"purple: {share:.1%} of the canvas (limit {PURPLE_LIMIT:.1%})")
    where = ", ".join(f"{x0 // scale},{y0 // scale} {(x1 - x0) // scale}x{(y1 - y0) // scale}" for x0, y0, x1, y1, _ in found)
    row(len(found) <= SPOT_LIMIT, f"purple spots: {len(found)} (limit {SPOT_LIMIT}: logo symbol + one accent)" + (f" at {where}" if where else ""))
    row(tint_share <= TINT_LIMIT, f"light purple tint: {tint_share:.1%} (decoration stays in palette neutrals)")
    sq = path.with_name(path.stem + ".squint.png")
    squint(img, sq)
    lines.append(f"  squint test: {sq.name} (title first, decoration last)")
    return lines, bad


ROOT = Path(__file__).resolve().parent.parent
PALETTE_PAGES = [ROOT / "wiki/brand/visual/colors-typography.md", ROOT / "wiki/brand/visual/logo.md"]
HEX = re.compile(r"#([0-9a-fA-F]{6}|[0-9a-fA-F]{3})\b")
RGB = re.compile(r"rgba?\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)")


def norm(h):
    h = h.lstrip("#").upper()
    return "#" + ("".join(c * 2 for c in h) if len(h) == 3 else h)


def palette():
    return {norm(m.group(0)) for p in PALETTE_PAGES for m in HEX.finditer(p.read_text(encoding="utf-8"))}


def check_source(folder):
    """Colors outside the palette and grayscale filters in a layout folder."""
    folder = Path(folder)
    allowed, lines, bad = palette(), [f"{folder.name}/ (source)"], 0
    for f in sorted(folder.rglob("*")):
        if f.suffix not in (".html", ".css", ".svg") or f.name.startswith(".render"):
            continue
        text = f.read_text(encoding="utf-8")
        used = {norm(m.group(0)) for m in HEX.finditer(text)}
        used |= {"#%02X%02X%02X" % tuple(int(x) for x in m.groups()) for m in RGB.finditer(text)}
        for c in sorted(used - allowed):
            lines.append(f"  ! {f.relative_to(folder)}: {c} is not in the palette"); bad += 1
        if re.search(r"grayscale|saturate\(0", text):
            lines.append(f"  ! {f.relative_to(folder)}: grayscale filter; use a palette neutral"); bad += 1
    if not bad:
        lines.append("    colors: all from the palette, no grayscale filters")
    return lines, bad


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("png", nargs="*", help="rendered layouts")
    ap.add_argument("--layout", help="layout folder to check for colors outside the palette")
    ap.add_argument("--scale", type=int, default=2, help="render scale, for sizes in the report (default 2)")
    ap.add_argument("--strict", action="store_true", help="exit with code 1 on any deviation")
    args = ap.parse_args()
    bad = 0
    if args.layout:
        lines, n = check_source(args.layout)
        print("\n".join(lines))
        bad += n
    for p in args.png:
        lines, n = check(p, args.scale)
        print("\n".join(lines))
        bad += n
    print(f"{bad} deviation(s)" if bad else "No deviations.")
    sys.exit(1 if bad and args.strict else 0)


if __name__ == "__main__":
    main()
