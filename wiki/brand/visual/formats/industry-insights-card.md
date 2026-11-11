---
id: brand-format-industry-insights-card
title: "Format: Industry Insights card"
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources: [raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [brand-colors-typography, brand-logo, decision-0004]
tags: [visual, format, industry-insights, design-system]
---

# Format: Industry Insights card (v2.1)

Card for the Industry Insights series. v2 applies from the "Data resilience" episode (November 2026). Earlier cards stay as they are; new cards are made only this way.

v2.1 (2026-11-12) aligns v2 with [decision 0004](../../../../decisions/0004-design-system.md): background `#F6F6FB`, context line Regular 400, grid gradient `#7C75FF` → `#6F47FF`.

## What changed from v1

| Element | v1 (template before November 2026) | v2.1 | Why |
|---|---|---|---|
| Grey text (notes, source) | `#9097B0` | `#62687E` | `#9097B0` is the dark-mode text color, 2.69:1 on light. `#62687E` gives 5.13:1 |
| Eyebrow | gradient `#9E55FE → #6636FA` | solid `#6F47FF` | the gradient start is 3.76:1 at 19.5 px, 4.5:1 is needed. The gradient isn't in the palette |
| Purple insight line | the same gradient | solid `#6F47FF` | gradient text isn't allowed |
| Logo | wordmark only, `#050A30` | horizontal lockup with symbol, wordmark `#141A21` | wordmark without the symbol is forbidden; `#141A21` is the light-background color |
| Headline numbers | Bold 700 | Semibold 600 | headline numbers are Semibold; Bold only for emphasis in text |
| Context line | Medium 500 (v2) | Regular 400 | Medium isn't a brand weight |
| Background | `#F6F6FC` (v2) | `#F6F6FB` | brand Surface 1 |

## Canvas

- **1200×700 px**, exported at 2× (2400×1400) so text stays sharp on retina screens.
- Background `#F6F6FB`.
- Margins 70 px left and right. All text on one left axis, x = 70.

## Text (Figtree, coordinates for 1200×700)

| Element | Size / weight | Color | Ink bounds, vertical |
|---|---|---|---|
| Eyebrow `INDUSTRY INSIGHTS · [TAG]` | 19.5 px Regular, caps | `#6F47FF` | 98–112 |
| Single number | 214 px Semibold | `#141A21` | 180–338 |
| Pair "main + comparison" | main 190 px Semibold `#141A21` from x = 70; comparison 104 px Semibold `#62687E` from x = 480; bottoms on one baseline | see left | 184–322 |
| Note to the number | 23 px Regular, up to two lines, 29 px line step | `#62687E` | from ~41 px below the number |
| Insight, line 1 (context) | 44 px Regular | `#141A21` | 469–512 |
| Insight, line 2 (thought) | 44 px Semibold | `#6F47FF` | 525–568 |
| Source | 19 px Regular | `#62687E` | 610–629 |

**Two-number rule:** never put two equal numbers side by side. The main one carries the episode's fact: big, dark, first on the left. The comparison gives context: smaller, grey `#62687E`, on the right on the same baseline. 23 px notes under each, up to two lines.

**One purple line:** exactly one purple text line per card, and it's always a thought, not a fact. The eyebrow is a service element and doesn't count.

## Logo

- [iagon-horizontal-on-light.svg](../logos/iagon-horizontal-on-light.svg): gradient symbol `#7C75FF` → `#6F47FF`, wordmark `#141A21`.
- Width 192 px (wordmark ≈92 px). Right edge at x ≈ 1126, vertical bounds 597–640.
- Clear space: two "o" (≈41 px) on all sides. Currently 60 px to the bottom, 74 px to the right edge.

## Grid (right side)

- Frame: 12 columns × 6 rows, 21.5 px squares, radius 4.5, step 32.8 horizontally and 33 vertically. From x = 752 to the right margin, y 169–356.
- Base squares `#E3E2E9`. Accents: gradient `#7C75FF` → `#6F47FF` across the full grid width, about 15–20% of squares, scattered without shapes or lines.
- 4–6 gaps in random places, so the grid reads as a network, not wallpaper.
- The grid is always quieter than the number.

### Grid state by episode theme

| Theme | State |
|---|---|
| Sovereign cloud | Base: grey squares and scattered purple ones |
| Breach economics | One square darkened `#3A3D4A`, the rest intact |
| Data resilience / ransomware | One node darkened, purple fragments intact: the node is down, the system stands |
| Data sovereignty / AI | Density gradient: small pale on the left, dense purple on the right |
| Concentration risk | Three dense purple clusters, the rest small grey |
| Shadow data | Some squares outlined, no fill |

## Hard bans (this format)

- 3D, spheres, halftone globes, hexagons, glow, shadows.
- Gradient or neon text. Gradient only on grid squares and in the logo symbol.
- Red on cards. A negative state is a darkened grey square.
- Arrows unless there is movement between two states. Never more than one arrow, never chevrons.
- Icons of clouds, locks, shields. Year badges, vertical text.
- A number without a named source on the card.
- Wordmark without the symbol.

## Pre-publish check

1. Cover the logo: does it look like an Economist chart or a crypto pitch deck? It must be the first.
2. Voice of the post: does it sound like a trusted expert who cares about the person on the other side?
3. Contrast: grey text only `#62687E`, purple text only `#6F47FF`.
