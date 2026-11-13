---
id: decision-0007
title: Approved layouts live in the repo as HTML
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-13
updated: 2026-11-13
---

# 0007: Approved layouts live in the repo as HTML

## Context
Layouts were designed on Claude Design canvases and kept there. A canvas is good for exploring, but it ties the layout to one chat and one account: a colleague can't open it, the data is typed in by hand every time, and nothing checks the numbers. The first recurring data layout, the Development Update monthly recap, made the cost clear: 11 numbers, a total twice and nine chips retyped each month.

## Decision
1. **Design on a canvas, keep in the repo.** Once a layout is approved, it moves to `layouts/<format>/` as plain HTML and CSS. The repo copy is the source of truth; the canvas stays as a sketchbook.
2. **Self-contained.** Fonts, background images and other assets sit in `layouts/<format>/assets/`. Logos are linked from `wiki/brand/visual/logos/`, never copied or redrawn. No external requests: a layout renders the same offline.
3. **Openable as is.** Each HTML file opens in a browser with real sample data. Values that change are marked `<!-- slot:name -->…<!-- /slot:name -->`.
4. **Data layouts get a script.** When a layout is filled from data, a script in `scripts/` fills the slots from the source file, checks the numbers and renders PNG files at 2×.
5. **Spec and template together.** Every layout has a format page in `wiki/brand/visual/formats/` that links to its folder. The format page holds the rules; the HTML holds the implementation. If they differ, the format page wins and the HTML is fixed.

## Consequences
- First layout moved: `layouts/monthly-recap/` with `scripts/monthly-recap.py`.
- Existing formats with templates outside the repo (Total Earned By Nodes, Industry Insights card, two-panel post) move in when they are next used.
- Editing a layout visually means opening it in a canvas again, then bringing the approved change back into the repo.
