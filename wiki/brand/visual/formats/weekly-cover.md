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

One cover for every weekly issue. Only the week number changes. Template: [`layouts/weekly-cover/`](../../../../layouts/weekly-cover/), filled by `scripts/weekly-update.py`.

Based on the September 2026 cover, rebuilt on the design system.

## Canvas
- **1200×675 px**, 16:9, exported at 2×. Discord and Telegram show it uncropped.
- Background `#F6F6FB`. Margins 72 px.
- Two text roles: H1 and Small, the week chip ([canvas type scale](../canvases.md)).
- Purple only in the logo symbol: one accent point.

## Elements

| Element | Spec | Color |
|---|---|---|
| Sphere | halftone sphere, 600×600, top −170, right −150: bleeds off the top-right corner as background texture, never touches the title. `layouts/weekly-cover/assets/sphere.svg` | neutral gray (grayscale, 32% opacity). Pending: gray or a 30% Violet tint, director to choose |
| Logo | 200×45, top of the text block, 48 px above the chip | `iagon-horizontal-on-light.svg` |
| Week chip | Small 28/40, Regular 400, padding 8/24, full radius, 1 px border `#62687E` at 15%: `Week 44, 2026`. Same chip as the Monthly Recap | background `#EAEBF5`, text `#141A21` |
| Title `Development Update` | H1 92/100, Semibold 600, −1%, 24 px under the chip. Title Case: the series name | `#141A21` |

Logo, chip and title form one block, bottom-left, 72 px from the left and bottom edges. One block reads as one unit in a small Discord or Telegram preview.

## Week, not dates
- `Week 44, 2026`: the ISO week from the dashboard. The script checks it against the dates.
- No dates on the cover. The post is about what the team did; the period is secondary and dates draw the eye away from the title (director, 2026-11-13).

## Changes from the September cover
| Element | Was | Now | Why |
|---|---|---|---|
| Size | 1920×1080 | 1200×675 | Same 16:9; 1200 is our social canvas width and the type scale applies to it |
| Date | one day, purple | week number in a neutral chip | the issue covers a week; the title carries the cover |
| Logo | older wordmark | approved logo file, above the title | logos come from `wiki/brand/visual/logos/` only |
| Sphere | raster image, full purple | SVG, muted, cropped by the corner | sharp at 2×; purple stays within its share of the canvas |
