---
id: decision-0004
title: Design system
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-12
updated: 2026-11-12
---

# 0004: Design system

## Context

The visual rules lived in several places: Brand Guidelines v1.0 (PDF), an extract with corrections, SVG code in a project doc, and format specs inside series docs. They contradicted each other on colors, background and font weights, and there were no logo files for light backgrounds.

## Decision

1. **`wiki/brand/visual/` is the source of truth for the visual identity.** Where it differs from the brandbook PDF, the hub wins.
2. **Purple Shade = `#7C75FF`.** The brandbook value `#7E67FF` is an error: it gives 4.48:1 on dark and fails for text, while `#7C75FF` gives 4.97:1 and matches the logo gradient. Purple text on light is `#6F47FF`, on dark `#7C75FF`.
3. **Light background Surface 1 = `#F6F6FB`.** `#F6F6FC` in the Industry Insights spec is aligned to it.
4. **Iagon Insight logo is an approved exception** to the sub-logo rule: blue → violet gradient symbol, "insight" in `#5786FF`. Applies to Insight only.
5. **Minimum logo sizes are a standard:** horizontal 140 px / 30 mm, stacked 70 px / 18 mm, symbol 24 px / 8 mm.
6. **Font weights: 400, 600, 700 only.** _(Superseded by [0006](0006-type-scale.md): 400 and 600 only.)_ Headline numbers and titles are Semibold 600. No Medium 500.
7. **Formats follow the brand rules.** "Total Earned By Nodes" moves to Semibold 600 and a palette green; Industry Insights context line moves to Regular 400.
8. **Format bans are format-specific.** The Industry Insights ban on spheres and globes applies to that series only; the "Total Earned By Nodes" post keeps its globe.
9. **Logo files are in the repo**, named by background (`-on-dark`, `-on-light`), with new light-background versions of the horizontal and stacked lockups.

## Consequences

- New visuals are checked against `colors-typography.md`, `logo.md` and the format page.
- Posts 1–3 of the Würth series used `#7E67FF` on dark and stay as published. New posts use `#7C75FF`.
- The "Total Earned By Nodes" HTML template needs an update to the new values before the next monthly post.
