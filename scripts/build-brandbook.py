#!/usr/bin/env python3
"""Join the parts of the Iagon Brandbook Package into one Markdown document.

Usage:  python3 scripts/build-brandbook.py
Output: dist/iagon-brandbook-package.md

Reads wiki/brand/brandbook.yaml, strips each part's frontmatter, drops hub-only
links, adds a title page and a table of contents.
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.exit("PyYAML is required: pip install pyyaml")

ROOT = Path(__file__).resolve().parent.parent
BRAND = ROOT / "wiki" / "brand"
OUT = ROOT / "dist" / "iagon-brandbook-package.md"

FRONTMATTER = re.compile(r"^---\n.*?\n---\n", re.S)
LINK = re.compile(r"\[([^\]]+)\]\((?!https?://)[^)]*\)")  # keep text, drop internal links


def slug(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def load_part(rel):
    path = BRAND / rel
    if not path.exists():
        sys.exit(f"Missing part: {rel}")
    text = FRONTMATTER.sub("", path.read_text(encoding="utf-8"), count=1)
    text = re.sub(r"\A\s*# [^\n]*\n", "", text)  # the group title replaces a part's own H1
    return LINK.sub(r"\1", text).strip()


def section(title, files):
    body = "\n\n".join(load_part(f) for f in files)
    return f"# {title}\n\n{body}", title


def main():
    manifest = yaml.safe_load((BRAND / "brandbook.yaml").read_text(encoding="utf-8"))
    blocks, toc = [], []
    for group in manifest.get("parts", []) + manifest.get("appendix", []):
        text, title = section(group["title"], group["files"])
        blocks.append(text)
        subs = re.findall(r"^## (.+)$", text, re.M)
        toc.append(f"- [{title}](#{slug(title)})")
        toc += [f"  - {s.split(' · ')[0]}" for s in subs]

    head = (
        f"# {manifest['title']}\n\n"
        f"Version {manifest['version']} · {manifest['updated']} · Owner: {manifest['owner']}\n\n"
        "Built from the Iagon Marketing Hub. Edit the parts in `wiki/brand/`, not this file.\n\n"
        "## Contents\n\n" + "\n".join(toc)
    )
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(head + "\n\n" + "\n\n".join(blocks) + "\n", encoding="utf-8")
    print(f"Built {OUT.relative_to(ROOT)} ({len(blocks)} parts)")


if __name__ == "__main__":
    main()
