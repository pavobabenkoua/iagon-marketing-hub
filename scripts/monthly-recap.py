#!/usr/bin/env python3
"""Build the Development Update monthly recap: two cards and the post texts.

Usage:
  python3 scripts/monthly-recap.py --csv raw/archive/2026-11-12-dev-changelog-2026-10.csv \
      --inputs wiki/series/development-update/inputs/2026-10.txt

Output (dist/development-update/YYYY-MM/):
  card-1.png, card-2.png   1080x1080 cards rendered at 2x (2160x2160)
  numbers.md               totals by area and by category, with checks
  x-thread.txt             tweets separated by a line of "====="
  telegram.txt             one message
  discord-1.txt            first message (cards go here)
  discord-2.txt            second message

Rules: wiki/series/development-update/series.md
Layout: layouts/monthly-recap/ (spec: wiki/brand/visual/formats/monthly-recap-cards.md)
Wording: wiki/series/development-update/issue/ (x-thread.txt, telegram.txt, discord.txt).
         The script holds no wording of its own: edit the files, not this script.

The inputs file is the editorial choice of 3-4 lines per area, copied from the
export's Change column. Format:

  # Iagon Storage Node
  - Self-healing Iagon Storage Nodes
  - Live node alerts in the Iagon Dashboard

Without --inputs the script renders the cards and numbers only.
Needs Playwright with Chromium: pip install playwright && playwright install chromium
"""
import argparse
import calendar
import csv
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LAYOUT = ROOT / "layouts" / "monthly-recap"
ISSUE = ROOT / "wiki" / "series" / "development-update" / "issue"
DISCORD_LIMIT = 2000

# Fixed tile order on card 2: the order of the source dashboard.
CATEGORIES = [
    "Development", "Security", "Production deployments", "Production-ready tests",
    "Updates", "New software and servers", "Bug fixes", "Performance",
    "Server security", "Server updates", "Debugging",
]
NUMBER_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight",
                "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]


def fail(msg):
    sys.exit(f"ERROR: {msg}")


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load(csv_path):
    rows = list(csv.DictReader(open(csv_path, encoding="utf-8-sig")))
    if not rows:
        fail("the export is empty")
    months = {r["Month"] for r in rows}
    if len(months) != 1:
        fail(f"the export holds more than one month: {sorted(months)}")
    year, month = (int(x) for x in months.pop().split("-"))
    return rows, year, month


def count(rows):
    total = len(rows)
    by_cat = Counter(r["Category"] for r in rows)
    unknown = set(by_cat) - set(CATEGORIES)
    if unknown:
        fail(f"unknown categories {sorted(unknown)}: add them to CATEGORIES in the agreed order")
    if sum(by_cat.values()) != total:
        fail("categories do not add up to the total")
    by_area = Counter(r["Area"] for r in rows)
    areas = sorted(by_area, key=lambda a: (-by_area[a], a))
    topics = {r["Topic"] for r in rows}
    return total, by_cat, by_area, areas, topics


def fill(template, slots):
    for name, value in slots.items():
        pattern = re.compile(rf"(<!-- slot:{name} -->).*?(<!-- /slot:{name} -->)", re.S)
        if not pattern.search(template):
            fail(f"slot '{name}' not found in the template")
        template = pattern.sub(lambda m: m.group(1) + value + m.group(2), template)
    return template


def render_cards(out, month_label, month_name, total, by_cat, areas):
    chips = "".join(f'\n      <span class="chip">{esc(a)}</span>' for a in areas) + "\n    "
    tiles = "".join(
        f'\n    <div class="tile"><p class="tile-num">{by_cat[c]}</p><p class="tile-label">{esc(c)}</p></div>'
        for c in CATEGORIES if by_cat.get(c)
    )
    tiles += f'\n    <div class="tile tile-total"><p class="tile-num">{total}</p><p class="tile-label">Total</p></div>\n  '
    pages = {
        "card-1": fill((LAYOUT / "card-1.html").read_text(encoding="utf-8"),
                       {"month": month_label, "total": str(total), "chips": chips}),
        "card-2": fill((LAYOUT / "card-2.html").read_text(encoding="utf-8"),
                       {"total": str(total), "month_name": month_name, "tiles": tiles}),
    }
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        fail("Playwright is required: pip install playwright && playwright install chromium")
    temp = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1080, "height": 1080}, device_scale_factor=2)
            for name, html in pages.items():
                tmp = LAYOUT / f".render-{name}.html"  # next to the template so relative paths work
                tmp.write_text(html, encoding="utf-8")
                temp.append(tmp)
                page.goto(tmp.as_uri())
                page.evaluate("document.fonts.ready")
                page.wait_for_load_state("networkidle")
                page.locator(".card").screenshot(path=str(out / f"{name}.png"))
            browser.close()
    finally:
        for t in temp:
            t.unlink(missing_ok=True)


def read_inputs(path, rows, areas):
    changes = defaultdict(set)
    for r in rows:
        changes[r["Area"]].add(r["Change"])
    picks, current = {}, None
    for n, line in enumerate(Path(path).read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        if line.startswith("# "):
            current = line[2:].strip()
            if current not in changes:
                fail(f"inputs line {n}: area '{current}' is not in the export")
            picks[current] = []
        elif line.startswith("- "):
            if current is None:
                fail(f"inputs line {n}: a line before any area")
            text = line[2:]
            if text not in changes[current]:
                fail(f"inputs line {n}: not found word for word under '{current}': {text}")
            picks[current].append(text)
        else:
            fail(f"inputs line {n}: start with '# ' for an area or '- ' for a line")
    missing = [a for a in areas if a not in picks]
    if missing:
        fail(f"every area must appear in the post; missing: {missing}")
    for a, lines in picks.items():
        if not 1 <= len(lines) <= 4:
            fail(f"'{a}' has {len(lines)} lines; use 3-4")
    return picks


PLACEHOLDER = re.compile(r"\[(Month YYYY|Month|Total|Areas|Tweets|n|Area)\]")
LEFTOVER = re.compile(r"\[[A-Za-z][A-Za-z ]*\]")


def load_issue(name):
    path = ISSUE / name
    parts = re.split(r"\n=====\n", path.read_text(encoding="utf-8").strip("\n"))
    if len(parts) != 3:
        fail(f"{path.relative_to(ROOT)}: needs three parts (opening, area block, close) separated by a line =====")
    return [part.strip("\n") for part in parts]


def fill_text(template, values, lines=None, where=""):
    out = PLACEHOLDER.sub(lambda m: str(values[m.group(1)]) if m.group(1) in values else m.group(0), template)
    unknown = [x for x in LEFTOVER.findall(out) if x != "[Lines]"]
    if unknown:
        fail(f"{where}: unknown placeholder(s) {unknown}")
    if "[Lines]" in out:
        out = out.replace("[Lines]", lines or "")
    return out


def build_texts(out, month_label, month_name, total, areas, picks):
    n = len(areas)
    common = {"Month YYYY": month_label, "Month": month_name, "Total": total,
              "Areas": NUMBER_WORDS[n] if n < len(NUMBER_WORDS) else n, "Tweets": n + 1}
    bullets = {a: "\n".join(f"- {l}" for l in picks[a]) for a in areas}

    def render(name, numbered=False):
        head, block, close = load_issue(name)
        blocks = [fill_text(block, {**common, "n": i, "Area": a}, bullets[a], name)
                  for i, a in enumerate(areas, 2 if numbered else 1)]
        return fill_text(head, common, where=name), blocks, fill_text(close, common, where=name)

    head, blocks, close = render("x-thread.txt", numbered=True)
    (out / "x-thread.txt").write_text("\n\n=====\n\n".join([head, *blocks, close]) + "\n", encoding="utf-8")

    head, blocks, close = render("telegram.txt")
    (out / "telegram.txt").write_text("\n\n".join([head, *blocks, close]) + "\n", encoding="utf-8")

    head, blocks, close = render("discord.txt")
    split = (len(blocks) + 1) // 2  # 9 areas -> 5 + 4
    d1 = "\n\n".join([head, *blocks[:split]]) + "\n"
    d2 = "\n\n".join([*blocks[split:], close]) + "\n"
    for name, text in (("discord-1.txt", d1), ("discord-2.txt", d2)):
        if len(text) > DISCORD_LIMIT:
            fail(f"{name} is {len(text)} characters, over the Discord limit of {DISCORD_LIMIT}")
        (out / name).write_text(text, encoding="utf-8")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--csv", required=True, help="monthly dashboard export")
    ap.add_argument("--inputs", help="chosen lines per area (wiki/series/<series>/inputs/YYYY-MM.txt)")
    ap.add_argument("--out", help="output folder (default dist/development-update/YYYY-MM)")
    args = ap.parse_args()

    rows, year, month = load(args.csv)
    month_name = calendar.month_name[month]
    month_label = f"{month_name} {year}"
    total, by_cat, by_area, areas, topics = count(rows)
    out = Path(args.out) if args.out else ROOT / "dist" / "development-update" / f"{year}-{month:02d}"
    out.mkdir(parents=True, exist_ok=True)

    lines = [f"# Numbers: {month_label}", "",
             f"{total} changes, {len(topics)} topics, {len(areas)} areas. Categories add up to the total: yes.", "",
             "| Area | Changes |", "|---|---|"] + [f"| {a} | {by_area[a]} |" for a in areas] + \
            ["", "| Category | Changes |", "|---|---|"] + [f"| {c} | {by_cat[c]} |" for c in CATEGORIES if by_cat.get(c)]
    (out / "numbers.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    render_cards(out, month_label, month_name, total, by_cat, areas)
    if args.inputs:
        build_texts(out, month_label, month_name, total, areas, read_inputs(args.inputs, rows, areas))
    print(f"Done: {out.relative_to(ROOT) if out.is_relative_to(ROOT) else out}")
    print(f"  {total} changes, {len(topics)} topics, {len(areas)} areas")


if __name__ == "__main__":
    main()
