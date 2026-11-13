---
id: brand-format-weekly-cover
title: "Format: Development Update Weekly cover"
type: brand
status: draft
owner: Pavlo Babenko
updated: 2026-11-13
visibility: team
related: [series-development-update-weekly, brand-colors-typography, brand-logo, decision-0007]
tags: [visual, format, development-update, discord, telegram]
---

# Format: Development Update Weekly cover

One cover for every weekly issue. Only the dates change. Template: [`layouts/weekly-cover/`](../../../../layouts/weekly-cover/), filled by `scripts/weekly-update.py`.

Based on the September 2026 cover, rebuilt on the design system.

## Canvas
- **1200×675 px**, 16:9, exported at 2×. Discord and Telegram show it uncropped.
- Background `#F6F6FB`. Margins 72 px.
- Two text roles: eyebrow and H1 ([canvas type scale](../canvases.md)).

## Elements

| Element | Spec | Color |
|---|---|---|
| Sphere | halftone sphere, 480×480, top 36, right 64. Dots large in the middle, smaller and flatter toward the rim. `layouts/weekly-cover/assets/sphere.svg` | Violet `#885EFF` |
| Logo | 160×36, bottom-left block, 40 px above the eyebrow | `iagon-horizontal-on-light.svg` |
| Eyebrow: the week as dates | 28/36, Semibold 600, caps, +4%: `26 OCTOBER TO 1 NOVEMBER 2026` | `#6F47FF` |
| Title `Development Update` | H1 92/100, Semibold 600, −1%. Title Case: the series name | `#141A21` |

Text block bottom-left, 72 px from the left and bottom edges.

## Dates
- Same month: `9 to 15 November 2026`. Two months: `26 October to 1 November 2026`. Two years: `29 December 2026 to 4 January 2027`.
- "to", not a dash: the long dash is not used in our copy.

## Changes from the September cover
| Element | Was | Now | Why |
|---|---|---|---|
| Size | 1920×1080 | 1200×675 | Same 16:9; 1200 is our social canvas width and the type scale applies to it |
| Date | one day, purple, sentence case | the week as a range, eyebrow style | the issue covers a week; the eyebrow is the design system's label role |
| Logo | older wordmark | approved logo file | logos come from `wiki/brand/visual/logos/` only |
| Sphere | raster image | SVG built on the brand Violet | sharp at 2×, in the repo, on the palette |
