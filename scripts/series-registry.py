#!/usr/bin/env python3
"""Build the series registry in wiki/series/README.md (decision 0009).

Usage:
  python3 scripts/series-registry.py          rewrite the registry table
  python3 scripts/series-registry.py --check  fail if the table is out of date or a field is missing

Reads the frontmatter of every wiki/series/<slug>/series.md and the
`publications` dates of the posts in wiki/series/<slug>/posts/.
"""
import argparse
import datetime as dt
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
SERIES = ROOT / "wiki" / "series"
README = SERIES / "README.md"
START, END = "<!-- registry:start -->", "<!-- registry:end -->"

TYPES = {"recurring", "thematic", "evergreen"}
STATES = {"planned", "active", "paused", "finished"}
OVERDUE_DAYS = {"weekly": 14, "biweekly": 28, "monthly": 62, "quarterly": 184, "irregular": None}
NARRATIVES = {"01": "The Compliance Gap", "02": "The Patient's File", "03": "The Idle World",
              "04": "The Hardest Customer", "05": "The Proof File"}
CHANNELS = {"x": "X", "linkedin": "LinkedIn", "discord": "Discord", "telegram": "Telegram",
            "blog": "Blog", "youtube": "YouTube"}
REQUIRED = ["id", "title", "summary", "series_type", "narrative", "cadence", "state", "channels", "owner"]
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def frontmatter(path):
    m = FRONTMATTER.match(path.read_text(encoding="utf-8"))
    return yaml.safe_load(m.group(1)) if m else {}


def last_post(folder):
    dates = []
    for post in sorted((folder / "posts").glob("*.md")):
        for pub in frontmatter(post).get("publications") or []:
            d = pub.get("date")
            if isinstance(d, str):
                d = dt.date.fromisoformat(d)
            if isinstance(d, dt.date):
                dates.append(d)
    return max(dates) if dates else None


def rows(today):
    errors, out = [], []
    for page in sorted(SERIES.glob("*/series.md")):
        fm = frontmatter(page)
        rel = page.relative_to(SERIES).as_posix()
        missing = [f for f in REQUIRED if not fm.get(f)]
        if missing:
            errors.append(f"{rel}: missing {', '.join(missing)}")
            continue
        narrative = str(fm["narrative"]).zfill(2)
        checks = [(fm["series_type"] in TYPES, f"series_type '{fm['series_type']}'"),
                  (fm["state"] in STATES, f"state '{fm['state']}'"),
                  (fm["cadence"] in OVERDUE_DAYS, f"cadence '{fm['cadence']}'"),
                  (narrative in NARRATIVES, f"narrative '{fm['narrative']}'")]
        bad = [msg for ok, msg in checks if not ok]
        if bad:
            errors.append(f"{rel}: unknown {', '.join(bad)}")
            continue
        last = last_post(page.parent)
        state = fm["state"]
        limit = OVERDUE_DAYS[fm["cadence"]]
        if state == "active" and limit and (last is None or (today - last).days > limit):
            state = "active · **overdue**"
        kind = fm["series_type"] + (" (arc)" if fm.get("arc") is True else "")
        channels = ", ".join(CHANNELS.get(c, c) for c in fm["channels"])
        cell = lambda s: str(s).replace("|", "\\|")  # a pipe inside a cell breaks the table
        out.append((fm["title"], f"| [{cell(fm['title'])}]({rel}) | {cell(fm['summary'])} | {kind} | "
                    f"{narrative} {NARRATIVES[narrative]} | {fm['cadence']} | {channels} | {state} | "
                    f"{last.isoformat() if last else '—'} | {fm['owner']} |"))
    return errors, [r for _, r in sorted(out)]


def table(lines):
    head = ["| Series | About | Type | Narrative | Cadence | Channels | State | Last post | Owner |",
            "|---|---|---|---|---|---|---|---|---|"]
    body = lines or ["| _No series yet_ | | | | | | | | |"]
    return "\n".join([START, "", *head, *body, "", END])


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="fail instead of writing")
    args = ap.parse_args()

    errors, lines = rows(dt.date.today())
    if errors:
        sys.exit("ERROR:\n  " + "\n  ".join(errors))
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        sys.exit(f"ERROR: markers {START} / {END} not found in {README.relative_to(ROOT)}")
    new = re.sub(re.escape(START) + r".*?" + re.escape(END), lambda _: table(lines), text, flags=re.S)
    if args.check:
        if new != text:
            sys.exit("Registry is out of date: run python3 scripts/series-registry.py")
        print("Registry is up to date.")
        return
    README.write_text(new, encoding="utf-8")
    print(f"Registry written: {len(lines)} series.")


if __name__ == "__main__":
    main()
