---
id: brand-format-monthly-recap-cards
title: "Format: Development Update monthly recap cards"
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-13
reviewed: 2026-11-13
visibility: team
sources: [res-dev-update-canvas]
related: [series-development-update, brand-colors-typography, brand-logo, decision-0004]
tags: [visual, format, development-update, x]
---

# Format: Development Update monthly recap cards

Two square cards posted together as one multi-image post. Card 1 shows the month and the total. Card 2 shows the same total by type of work. Built on the canvas [res-dev-update-canvas](../../../resources.md), artboards `post-square-1` and `post-square-2`.

Approved by the director on 2026-11-13.

## Canvas

- **1080×1080 px**, both cards.
- Square, not 1200×700: X crops every image in a multi-image post from the centre to roughly 7:8. The October 2026 cards were 1200×700 and lost the logo and the series name in the feed.
- **Side safe zone 112 px.** Left and right padding is 112 px on every band, so a 7:8 centre crop still leaves about 45 px of air. Never place text or tiles closer than 112 px to a side edge.
- Two bands: **top 400 px** (identity), **bottom 680 px** (data). Card 2 inverts the colours of card 1.

## Card 1: the month

| Band | Element | Spec | Color |
|---|---|---|---|
| Top, dark `#13181E` | Background shape | dark form, left-anchored, bottom-aligned | as in the file |
| | Logo | top left, 160×36 | `iagon-horizontal-on-dark.svg` |
| | Eyebrow `DEVELOPMENT UPDATE` | 28/36, Semibold 600, caps, +4% | `#7C75FF` |
| | Title `[Month YYYY]` | 52/60, Semibold 600, −1% | `#F2F2FA` |
| | Lead `What we shipped last month, area by area.` | 28/40, Regular | `#9097B0` |
| Bottom, light `#F6F6FB` | Total | 180/168, Semibold 600, −1% | `#141A21` |
| | `changes shipped across` | 32/44, Regular, directly under the total | `#141A21` |
| | Area chips | 28/40, Regular, pill, `#EAEBF5` fill, 1 px border `rgba(98,104,126,0.15)`, gap 12 | `#141A21` |

Text blocks in the top band sit on the bottom edge of the band. Chips are sorted by number of changes, largest first. The sort order is not shown.

## Card 2: in detail

| Band | Element | Spec | Color |
|---|---|---|---|
| Top, light `#F6F6FB` | Logo | top left, 160×36 | `iagon-horizontal-on-light.svg` |
| | Eyebrow `DEVELOPMENT UPDATE` | 28/36, Semibold 600, caps, +4% | `#6F47FF` |
| | Title `[Total] in detail` | 52/60, Semibold 600, −1% | `#141A21` |
| | Lead `Every change in [Month], by the kind of work it took.` | 28/40, Regular | `#62687E` |
| Bottom, dark `#13181E` | Background shape | dark form, right-anchored, bottom-aligned | as in the file |
| | Grid | 3 columns, rows 132 px, gap 14 px, padding 48 px top and bottom | |
| | Tile | `#191E25` fill, 1 px border `rgba(144,151,176,0.15)`, radius 12, padding 12/20 | |
| | Tile number | 40/48, Regular 400 | `#F2F2FA` |
| | Tile label | 24/30, Regular | `#9097B0` |
| | Total tile, always last | fill `rgba(124,117,255,0.16)`, border `rgba(124,117,255,0.35)`, number Semibold 600 | `#F2F2FA` |

Tile order is fixed, the order of the source dashboard: Development, Security, Production deployments, Production-ready tests, Updates, New software and servers, Bug fixes, Performance, Server security, Server updates, Debugging, Total. A category with zero changes in the month is left out. The Total tile stays last.

## Colour rules for this format

- Purple marks the system, not the data: eyebrow on both cards and the Total tile tint. All numbers are neutral.
- No gradient on text. Solid accent per theme: `#7C75FF` on dark, `#6F47FF` on light.
- The background shapes are neutral graphics and sit outside the purple budget.
- No date note on the cards. The numbers describe a closed month, so they cannot change. The "figures as of" rule applies to live network figures only.

## Monthly checklist

1. Export the month from the development dashboard as CSV.
2. Card 1: change the month in the title, the total, the set and order of chips.
3. Card 2: change the total in the title, the month in the lead, the 11 tile numbers, the Total tile.
4. Check that the tile numbers add up to the total.
5. Load both cards into the X composer without posting. The logo and the outer tile edges must be fully visible.
