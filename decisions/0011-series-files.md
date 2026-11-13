---
id: decision-0011
title: Where series files live
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-13
updated: 2026-11-13
amends: decision-0007
---

# 0011: Where series files live

## Context
The first recurring series kept its fixed wording twice: in `series.md` and inside the build script. A change in one place would not reach the other. Its editorial input sat in a folder named after one task (`picks/`), which says nothing to the next series.

## Decision

| What | Where | In git |
|---|---|---|
| Visual template | `layouts/<format>/` ([0007](0007-approved-layouts-live-as-html.md)) | yes |
| Fixed wording of an issue | `wiki/series/<series>/issue/`, one file per channel | yes |
| Raw data (exports, stats) | `raw/archive/YYYY-MM-DD-<name>.<ext>`, never edited | yes |
| Editorial input of an issue (picked lines, choices) | `wiki/series/<series>/inputs/<period>.txt` | yes |
| Build script | `scripts/` | yes |
| Build output (images, texts) | `dist/<series>/<period>/` | no: it can always be rebuilt |
| Published post | `wiki/series/<series>/posts/` | yes |
| Drafts | chat or design canvas | no ([AGENTS.md](../AGENTS.md): a post enters the hub when published) |

1. **Wording lives in files, not in code.** A script reads the `issue/` files and holds no wording of its own. Anyone can change a phrase without touching code. `series.md` links to the files instead of repeating them.
2. **Issue files** have three parts separated by a line `=====`: opening, the block repeated for each item, close. Placeholders in square brackets are listed in the folder's README; an unknown placeholder stops the build.

## Consequences
- Development Update: wording moved from `scripts/monthly-recap.py` to `issue/`; `picks/` renamed `inputs/`; the script option is now `--inputs`. Output is byte-identical to before.
