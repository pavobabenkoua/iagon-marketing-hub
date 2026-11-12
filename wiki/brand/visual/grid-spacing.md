---
id: brand-grid-spacing
title: Grid and spacing
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
related: [brand-colors-typography, brand-canvases, brand-art-direction]
tags: [visual, grid, spacing, layout, design-system]
---

# Grid and spacing

Columns, margins and spacing for the four places we design: web pages, event and promo landing pages, social canvases and presentations. Built on the same base as the type scale (multiples of 8, breakpoints 768 and 1280), following the common practice of Material Design and IBM Carbon: an 8 px system, 12 columns on wide layouts, fewer columns as the width shrinks.

## 1. Spacing scale

Every gap, padding and margin comes from this list. No in-between values.

| Token | px | Typical use |
|---|---|---|
| space-1 | 4 | Icon to its label, tight inline gaps |
| space-2 | 8 | Eyebrow to title, items inside a chip or button |
| space-3 | 12 | Label to field, list items |
| space-4 | 16 | Title to text, mobile margins and card padding |
| space-5 | 24 | Grid gutter, text to button, card padding |
| space-6 | 32 | Between groups inside a section, desktop card padding |
| space-7 | 40 | |
| space-8 | 48 | Section padding on mobile |
| space-9 | 64 | Section padding on tablet, canvas margins |
| space-10 | 80 | |
| space-11 | 96 | Section padding on desktop |
| space-12 | 128 | Large gaps between page parts, hero padding |
| space-13 | 160 | Hero padding on wide screens |

Line heights in the type scale sit on a 4 px grid. Everything else sits on 8 px.

**Proximity rule:** the space between two related elements is always smaller than the space around the group. If a title is closer to the block above than to its own text, the layout is wrong.

## 2. Web pages

### Columns

| Breakpoint | Columns | Gutter | Side margin | Content width |
|---|---|---|---|---|
| Mobile < 768 | 4 | 16 | 16 (20 from 390 px) | fluid |
| Tablet 768–1279 | 8 | 24 | 32 | fluid |
| Desktop ≥ 1280 | 12 | 24 | auto, min. 40 | **1200 max**, centred |

At 1200 px a desktop column is 78 px (12 × 78 + 11 × 24 = 1200). Wide screens (1440, 1920) keep the 1200 container and grow the side margins. Full-bleed backgrounds may run edge to edge; content stays in the container.

**Reading width:** running text max 720 px (about 8 columns on desktop, 60–75 characters at 16 px). Never full container width.

### Vertical rhythm

| | Desktop | Tablet | Mobile |
|---|---|---|---|
| Section padding (top and bottom) | 96 | 64 | 48 |
| Gap between major page parts | 128 | 96 | 64 |
| Hero padding | 128–160 | 96 | 64 |
| Eyebrow → title | 8 | 8 | 8 |
| Title → text | 24 | 16 | 16 |
| Text → button | 32 | 32 | 24 |
| Card padding | 32 | 24 | 16 |
| Gap between cards | 24 | 24 | 16 |

### Common layouts (desktop columns)

| Layout | Columns | Tablet | Mobile |
|---|---|---|---|
| Text + image | 6 + 6, or 5 + 7 | 8 (stacked) | 4 (stacked) |
| Three cards | 4 + 4 + 4 | 4 + 4, third below | 4, stacked |
| Four cards / logos | 3 × 4 | 4 + 4 | 2 + 2 |
| Stat row (KPI) | 3 × 4 or 4 × 3 | 4 + 4 | 2 + 2 or stacked |
| Article | 8, centred (offset 2) | 8 | 4 |

## 3. Event and promo landing pages

Same grid and spacing as web pages. What changes is the structure: one goal, one action.

1. **First screen answers four questions on a 375 × 667 phone without scrolling:** what it is (H1), when (date, time with time zone), where (city and venue, or "Online"), and the one action (primary button).
2. **One primary action, repeated.** The same button after the hero, after the agenda and at the end. On mobile it may be sticky at the bottom (height 56, side margins 16).
3. **Order of sections:** hero → why attend (three cards, 4 + 4 + 4) → agenda → speakers → proof (partners, past numbers, quotes) → FAQ → final call to action.
4. **Agenda:** one row per slot, time in a fixed column (2 columns on desktop) and title + speaker in the rest (10 columns). Mobile: time above title.
5. **Speakers:** 4 per row on desktop (3 columns each), 2 on tablet and mobile. Photo 1:1, name Title-16, role Body-14.
6. **Countdown or "seats left"** only if true and updated. Never fake urgency.
7. Section padding may drop one step (desktop 64) to keep the page short. The landing page stays under about six screens on desktop.

## 4. Social canvases

Margins match [Canvas sizes](canvases.md). Columns help align text, numbers and graphic elements across posts in a series.

| Canvas | Columns | Gutter | Side margin | Top / bottom margin | Column width |
|---|---|---|---|---|---|
| 1200 × 700 (and 1200 × 675, 1200 × 630) | 12 | 24 | 72 | 64 | 66 |
| 1080 × 1080, 1080 × 1350 | 8 | 24 | 64 | 64 | 98 |
| 1080 × 1920 | 8 | 24 | 64 | 250 / 340 (safe zones) | 98 |

Check: 72 + 12 × 66 + 11 × 24 + 72 = 1200. 64 + 8 × 98 + 7 × 24 + 64 = 1080.

**Inside a canvas:**

| Between | px |
|---|---|
| Eyebrow → title | 16 |
| Title → text, number → note | 24–32 |
| Between blocks | 48–64 |
| Logo clear space | per [logo rules](logo.md) |

- All text on one left axis (the first column edge) unless the format says otherwise.
- The logo sits in a corner, inside the margins, in the same position across a series.
- Existing formats keep their approved coordinates (Industry Insights uses x = 70, within 2 px of the grid).

## 5. Presentations (1920 × 1080)

| Columns | Gutter | Side margin | Top margin | Bottom zone |
|---|---|---|---|---|
| 12 | 24 | 96 | 96 | 64 for logo, page number, source |

Column width 122 px (96 + 12 × 122 + 11 × 24 + 96 = 1920).

**Zones:**
- **Title zone:** from the top margin, title (H1 or H2 of the canvas scale) and an optional eyebrow above it.
- **Content zone:** starts 48–64 px below the title.
- **Footer zone:** bottom 64 px. Logo symbol, page number and fine print (sources). Same position on every slide.

**Common slide layouts (columns):**

| Layout | Columns |
|---|---|
| Title + text | text in 8, rest empty |
| Big number + explanation | number 7 + text 5 |
| Two options / before–after | 6 + 6 |
| Three points | 4 + 4 + 4 |
| Image + text | 7 + 5, image may bleed off the edge |
| Section divider | title in 8, vertically centred |

One idea per slide. If the content needs more than the content zone, it is two slides.
