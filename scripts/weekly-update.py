#!/usr/bin/env python3
"""Build the Development Update Weekly: the cover and the post texts.

Usage:
  python3 scripts/weekly-update.py --input raw/archive/2026-11-16-dev-statements-2026-W46.txt

The input is copied from the development dashboard as is, three things:

  Week 44, 2026 (26.10.2026 to 01.11.2026)
  15 topics, 94 changes
  Usability improvements for the Insight Dashboard and the Würth Partner platform
  Security improvements for the Iagon Infrastructure
  ...

Statements may start with "- " or "• ". They go into the post word for word.

Output (dist/development-update-weekly/YYYY-Www/):
  cover.png       1200x675 rendered at 2x (2400x1350)
  telegram.txt
  discord.txt

Rules: wiki/series/development-update-weekly/series.md
Layout: layouts/weekly-cover/ (spec: wiki/brand/visual/formats/weekly-cover.md)
Wording: wiki/series/development-update-weekly/issue/. The script holds no wording of its own.
Needs Playwright with Chromium: pip install playwright && playwright install chromium
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAYOUT = ROOT / "layouts" / "weekly-cover"
ISSUE = ROOT / "wiki" / "series" / "development-update-weekly" / "issue"
DISCORD_LIMIT = 2000

WEEK = re.compile(r"Week\s+(\d{1,2}),\s*(\d{4})\s*\((\d{2})\.(\d{2})\.(\d{4})\s+to\s+(\d{2})\.(\d{2})\.(\d{4})\)")
COUNTS = re.compile(r"(\d+)\s+topics?,\s*(\d+)\s+changes?")
PLACEHOLDER = re.compile(r"\[(Dates|Changes)\]")
LEFTOVER = re.compile(r"\[[A-Za-z][A-Za-z ]*\]")


def fail(msg):
    sys.exit(f"ERROR: {msg}")


def read_input(path):
    week = counts = None
    statements = []
    for n, raw in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        line = raw.strip().lstrip("▼").strip()
        if not line or line.lower() in ("marketing statements", "copy"):
            continue
        if m := WEEK.search(line):
            week = m
        elif m := COUNTS.search(line):
            counts = (int(m.group(1)), int(m.group(2)))
        else:
            statements.append(re.sub(r"^[-•*]\s+", "", line))
    if not week:
        fail("no week line like 'Week 44, 2026 (26.10.2026 to 01.11.2026)'")
    if not counts:
        fail("no counts line like '15 topics, 94 changes'")
    if not statements:
        fail("no statements")
    num, year = int(week.group(1)), int(week.group(2))
    start = dt.date(int(week.group(5)), int(week.group(4)), int(week.group(3)))
    end = dt.date(int(week.group(8)), int(week.group(7)), int(week.group(6)))
    if (start, end) != (dt.date.fromisocalendar(year, num, 1), dt.date.fromisocalendar(year, num, 7)):
        fail(f"week {num}, {year} is {dt.date.fromisocalendar(year, num, 1)} to "
             f"{dt.date.fromisocalendar(year, num, 7)}, not {start} to {end}")
    return year, num, start, end, counts, statements


def date_range(start, end):
    """26 October to 1 November 2026 / 9 to 15 November 2026 / 29 December 2026 to 4 January 2027."""
    if start.year != end.year:
        return f"{start.day} {start:%B} {start.year} to {end.day} {end:%B} {end.year}"
    if start.month != end.month:
        return f"{start.day} {start:%B} to {end.day} {end:%B} {end.year}"
    return f"{start.day} to {end.day} {end:%B} {end.year}"


def fill(template, values, lines, where):
    out = PLACEHOLDER.sub(lambda m: str(values[m.group(1)]), template)
    unknown = [x for x in LEFTOVER.findall(out) if x != "[Lines]"]
    if unknown:
        fail(f"{where}: unknown placeholder(s) {unknown}")
    return out.replace("[Lines]", lines)


def render_cover(out, dates):
    html = (LAYOUT / "cover.html").read_text(encoding="utf-8")
    slot = re.compile(r"(<!-- slot:dates -->).*?(<!-- /slot:dates -->)", re.S)
    if not slot.search(html):
        fail("slot 'dates' not found in the cover template")
    html = slot.sub(lambda m: m.group(1) + dates + m.group(2), html)
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        fail("Playwright is required: pip install playwright && playwright install chromium")
    tmp = LAYOUT / ".render-cover.html"  # next to the template so relative paths work
    try:
        tmp.write_text(html, encoding="utf-8")
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1200, "height": 675}, device_scale_factor=2)
            page.goto(tmp.as_uri())
            page.evaluate("document.fonts.ready")
            page.wait_for_load_state("networkidle")
            page.locator(".cover").screenshot(path=str(out / "cover.png"))
            browser.close()
    finally:
        tmp.unlink(missing_ok=True)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--input", required=True, help="the week copied from the dashboard")
    ap.add_argument("--out", help="output folder (default dist/development-update-weekly/YYYY-Www)")
    args = ap.parse_args()

    year, num, start, end, (topics, changes), statements = read_input(args.input)
    dates = date_range(start, end)
    out = Path(args.out) if args.out else ROOT / "dist" / "development-update-weekly" / f"{year}-W{num:02d}"
    out.mkdir(parents=True, exist_ok=True)

    values = {"Dates": dates, "Changes": changes}
    lines = "\n".join(f"- {s}" for s in statements)
    for name in ("telegram.txt", "discord.txt"):
        text = fill((ISSUE / name).read_text(encoding="utf-8").strip("\n"), values, lines, name) + "\n"
        if name == "discord.txt" and len(text) > DISCORD_LIMIT:
            fail(f"discord.txt is {len(text)} characters, over the Discord limit of {DISCORD_LIMIT}")
        (out / name).write_text(text, encoding="utf-8")
    render_cover(out, dates)
    print(f"Done: {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    print(f"  {dates}: {changes} changes, {topics} topics, {len(statements)} statements")


if __name__ == "__main__":
    main()
