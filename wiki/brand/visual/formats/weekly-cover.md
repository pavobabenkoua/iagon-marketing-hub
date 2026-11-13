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
- Two text roles: H1 and Small ([canvas type scale](../canvases.md)).
- Purple only in the logo symbol: one accent point.

## Elements

| Element | Spec | Color |
|---|---|---|
| Sphere | halftone sphere, 600×600, top −170, right −150: bleeds off the top-right corner as background texture, never touches the title. `layouts/weekly-cover/assets/sphere.svg` | neutral gray (grayscale, 32% opacity). Pending: gray or a 30% Violet tint, director to choose |
| Logo | 220×49, top-left, 72 px from the edges | `iagon-horizontal-on-light.svg` |
| Title `Development Update` | H1 92/100, Semibold 600, −1%. Title Case: the series name | `#141A21` |
| Dates | Small 28/40, Regular 400, sentence case, 16 px under the title: `26 October to 1 November 2026` | `#62687E` |

Text block bottom-left, 72 px from the left and bottom edges.

## Dates
- Same month: `9 to 15 November 2026`. Two months: `26 October to 1 November 2026`. Two years: `29 December 2026 to 4 January 2027`.
- "to", not a dash: the long dash is not used in our copy.

## Changes from the September cover
| Element | Was | Now | Why |
|---|---|---|---|
| Size | 1920×1080 | 1200×675 | Same 16:9; 1200 is our social canvas width and the type scale applies to it |
| Date | one day, purple | the week as a range, gray, Small | the issue covers a week; the title carries the cover, the dates only label it |
| Logo | older wordmark | approved logo file | logos come from `wiki/brand/visual/logos/` only |
| Sphere | raster image, full purple | SVG, muted, cropped by the corner | sharp at 2×; purple stays within its share of the canvas |
