---
id: brand-format-stats-earned-post
title: "Format: Total Earned By Nodes post"
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources: [res-stats-earned-template]
related: [brand-colors-typography, brand-logo, decision-0004]
tags: [visual, format, ecosystem-stats, design-system]
---

# Format: Total Earned By Nodes post

Monthly post with one number: the total earned by Iagon nodes. Built from an HTML template ([res-stats-earned-template](../../../resources.md)). Every month change **only two values**: the amount and the snapshot date.

The number itself comes from `wiki/data/facts.yaml` (`fact-nodes-total-earned`). Update the fact first, then the post.

## Canvas

- **1200×700 px**. Open the template in a browser and screenshot the `.stage` area, or export to PNG.
- Background `#F6F6FB`.
- Right side: a globe image, the right part of a sphere bleeding off the right edge (top −20 px, height 740 px). The Industry Insights ban on spheres doesn't apply here: this is a separate layout.

## Elements

| Element | Position | Spec | Color |
|---|---|---|---|
| Logo | top 70, left 72, width 252 px | [iagon-horizontal-on-light.svg](../logos/iagon-horizontal-on-light.svg) | as in the file |
| Title "Total Earned By Nodes" | top 300, left 72 | 35 px **Semibold 600** | `#6F47FF` |
| Coin icon | left 70, row top 360, 80×80 | circle with a white `$` | circle `#1A8059`, `$` `#FEFEFE` |
| Amount | next to the coin, gap 26 px | 107 px **Semibold 600**, line height 0.74, space as thousands separator (`2 388 599`) | `#141A21` |
| Snapshot note | bottom right area (top 656, right 310) | 15 px Regular (no italic): `*Stats are as of [D Month YYYY], last epoch end time snapshot.` | `#62687E` |

## Changes from the original template (2026-11-12)

| Element | Was | Now | Why |
|---|---|---|---|
| Amount | Regular 400 | Semibold 600 | display numbers on graphics are Semibold |
| Snapshot note | Regular italic | Regular | italic is not part of the type scale |
| Title | Regular 400 | Semibold 600 | titles are Semibold |
| Coin circle | `#249465` | `#1A8059` | `#249465` isn't in the palette. Palette Green `#22AE78` gives only 2.82:1 under a white `$` and fails the 3:1 icon rule; Green text `#1A8059` gives 4.87:1 |
| Background | `#F6F6FB` | `#F6F6FB` | already correct |

**The HTML template itself still has the old values.** It needs one update before the next monthly post.

## Monthly checklist

1. Take the new value from Ecosystem Stats at the last epoch end.
2. Update `fact-nodes-total-earned` in `wiki/data/facts.yaml` (value + `as_of`).
3. In the template change only the amount and the date in the note.
4. Check the amount fits on one line at 107 px.
