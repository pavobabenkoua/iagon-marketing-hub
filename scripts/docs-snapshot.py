#!/usr/bin/env python3
"""Take a dated snapshot of docs.iagon.com and report what changed.

docs.iagon.com is a read-only source for the hub (decision 0005). Its pages
change over time, so the hub keeps dated copies of the English Markdown pages
and compares each new copy with the previous one.

Usage:
    python3 -I scripts/docs-snapshot.py <docs-dir> --date YYYY-MM-DD

    <docs-dir>  the `documentation/docs` folder of an unpacked export of the
                iagon-public-documentation repository (GitHub "Download ZIP").
    --date      the date of the docs state: the date of the last commit in the
                export. GitHub ZIPs stamp every file with that date.

Writes:
    raw/docs-snapshots/<date>/pages/...   English .md pages, unchanged
    raw/docs-snapshots/<date>/sidebar.ts.txt   the live navigation
    raw/docs-snapshots/<date>/manifest.json    hash, words, title, in-nav flag
    raw/docs-snapshots/<date>/CHANGES.md       diff against the previous snapshot
                                               and the wiki pages to re-check

Skips: Japanese pages (jp/), .archive/, images and build files.
Reads the export as data only. Nothing from it is executed.
"""
import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SNAPSHOTS = ROOT / "raw" / "docs-snapshots"
WIKI = ROOT / "wiki"
LIVE = "https://docs.iagon.com/"
SKIP_DIRS = {"jp", ".archive", ".vitepress", "public", "node_modules"}
SOURCE_REF = re.compile(r"raw/docs-snapshots/\d{4}-\d{2}-\d{2}/pages/([\w./-]+\.md)")
FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def collect(docs_dir):
    pages = {}
    for path in sorted(docs_dir.rglob("*.md")):
        rel = path.relative_to(docs_dir)
        if rel.parts[0] in SKIP_DIRS:
            continue
        pages[rel.as_posix()] = path
    return pages


def title_of(text):
    fm = FRONTMATTER.match(text)
    if fm:
        m = re.search(r'^title:\s*"?([^"\n]+)"?', fm.group(1), re.M)
        if m:
            return m.group(1).strip()
    m = re.search(r"^# (.+)$", text, re.M)
    return m.group(1).strip() if m else ""


def nav_links(sidebar_text):
    return set(re.findall(r'link:\s*"(/[^"#]*)"', sidebar_text))


def previous_snapshot(date):
    dates = sorted(p.name for p in SNAPSHOTS.iterdir()
                   if p.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", p.name) and p.name < date)
    return dates[-1] if dates else None


def wiki_sources():
    """Map docs page path -> wiki pages whose frontmatter cites it."""
    refs = {}
    for page in WIKI.rglob("*.md"):
        text = page.read_text(encoding="utf-8")
        fm = FRONTMATTER.match(text)
        if not fm:
            continue
        for docs_path in SOURCE_REF.findall(fm.group(1)):
            refs.setdefault(docs_path, set()).add(page.relative_to(ROOT).as_posix())
    return refs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docs_dir", type=Path)
    ap.add_argument("--date", required=True)
    args = ap.parse_args()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.date):
        sys.exit("--date must be YYYY-MM-DD")
    docs_dir = args.docs_dir.resolve()
    if not docs_dir.is_dir():
        sys.exit(f"Not a folder: {docs_dir}")

    out = SNAPSHOTS / args.date
    if out.exists():
        sys.exit(f"Snapshot {args.date} already exists. Snapshots are immutable.")

    sidebar = docs_dir / ".vitepress" / "sidebar.ts"
    sidebar_text = sidebar.read_text(encoding="utf-8") if sidebar.exists() else ""
    in_nav = nav_links(sidebar_text)

    pages = collect(docs_dir)
    manifest = {"date": args.date, "source": "iagon-public-documentation (export)",
                "live": LIVE, "pages": {}}
    for rel, path in pages.items():
        data = path.read_bytes()
        text = data.decode("utf-8", errors="replace")
        target = out / "pages" / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, target)
        url_path = "/" + rel[:-3]
        manifest["pages"][rel] = {
            "title": title_of(text),
            "sha256": hashlib.sha256(data).hexdigest(),
            "words": len(re.sub(r"<[^>]+>", " ", text).split()),
            "in_nav": url_path in in_nav,
            "url": LIVE + rel[:-3],
        }
    if sidebar_text:
        (out / "sidebar.ts.txt").write_text(sidebar_text, encoding="utf-8")
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    prev = previous_snapshot(args.date)
    lines = [f"# Docs snapshot {args.date}", ""]
    lines.append(f"{len(pages)} English pages, {sum(1 for p in manifest['pages'].values() if p['in_nav'])} in the navigation.")
    lines.append("")
    if not prev:
        lines += ["First snapshot. Nothing to compare.", ""]
    else:
        old = json.loads((SNAPSHOTS / prev / "manifest.json").read_text(encoding="utf-8"))["pages"]
        new = manifest["pages"]
        added = sorted(set(new) - set(old))
        removed = sorted(set(old) - set(new))
        changed = sorted(p for p in set(new) & set(old) if new[p]["sha256"] != old[p]["sha256"])
        nav_moved = sorted(p for p in set(new) & set(old) if new[p]["in_nav"] != old[p]["in_nav"])
        nav_changed = (SNAPSHOTS / prev / "sidebar.ts.txt").exists() and \
            (SNAPSHOTS / prev / "sidebar.ts.txt").read_text(encoding="utf-8") != sidebar_text
        lines.append(f"Compared with {prev}.")
        lines.append("")
        for label, items in (("Added", added), ("Removed", removed), ("Changed", changed),
                             ("Navigation status changed", nav_moved)):
            lines.append(f"## {label} ({len(items)})")
            lines += [f"- `{p}`" for p in items] or ["- none"]
            lines.append("")
        lines.append(f"Navigation file changed: {'yes' if nav_changed else 'no'}")
        lines.append("")
        refs = wiki_sources()
        hit = {}
        for p in removed + changed:
            for w in refs.get(p, ()):
                hit.setdefault(w, []).append(p)
        lines.append(f"## Wiki pages to re-check ({len(hit)})")
        if hit:
            for w in sorted(hit):
                lines.append(f"- `{w}`: {', '.join(f'`{p}`' for p in sorted(hit[w]))}")
        else:
            lines.append("- none")
        lines.append("")
        lines.append("Compare a page: `diff raw/docs-snapshots/%s/pages/<path> raw/docs-snapshots/%s/pages/<path>`" % (prev, args.date))
        lines.append("")
    (out / "CHANGES.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
