---
id: brand-data-visualization
title: Data visualization
type: brand
status: draft
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
related: [brand-colors-typography, brand-canvases, brand-grid-spacing, brand-icons, brand-art-direction, brand-proof-library]
tags: [visual, charts, diagrams, data-visualization, design-system]
---

# Data visualization

How Iagon shows numbers and systems: chart forms, color palettes, marks, labels, and diagrams. Art direction asks for "data visualized beautifully"; this page is how. All palettes here were checked with a colorblind-safety validator (OKLab ΔE under protanopia and deuteranopia simulation, normal-vision separation, contrast), not chosen by eye.

## 1. Principles

1. **One chart, one point.** The title states the finding ("Node earnings doubled in 2026"), not the topic ("Node earnings").
2. **Emphasis is the default.** One series in purple, everything else in gray. Most marketing charts tell one story; multi-color charts are for when the series themselves are the subject.
3. **The form comes before color.** Decide what the reader must do (compare, follow a trend, see a split), then pick the chart, then the colors.
4. **Sometimes it is not a chart.** One number is a big number, not a one-bar chart. A few headline numbers are a row of stat tiles.
5. **Honest axes.** Bars always start at zero. One y-axis only, never two scales on one chart. No 3D, no perspective.
6. **Every chart carries a source** in fine print, and network metrics carry "figures as of [date]" ([Proof Library](../messaging/proof-library.md)).

## 2. Which form

| The reader must… | Use | Not |
|---|---|---|
| See one number | Big number (Display number on canvases, Numbers styles on web) | A one-bar chart |
| See a few headline numbers | Row of stat tiles: label, value, optional change | A grouped bar chart |
| Compare amounts | Horizontal bars, sorted largest first | Pie or donut |
| Follow a trend | Line (area only for a single series) | Bars for long time series |
| See that one item stands out | Emphasis: that item purple, the rest gray | Rainbow bars |
| See one whole split into parts (≤ 6) | One segmented bar | Pie or donut |
| Compare several splits or a split over time | Stacked bars | Several pies |
| See above / below a baseline | Diverging bars | Two colors without a midpoint |
| See before → after per item | Dumbbell (two dots joined) | Two grouped bars |
| Read more than about 7 categories | A table | More colors |

Pies and donuts are not used. Bars compare more exactly and fit the grid.

## 3. Palettes

Chart surfaces: light `#F6F6FB`, dark `#13181E`. Purple on dark always uses Purple Shade, as everywhere else in the brand.

### Emphasis (default)

| Role | Light | Dark |
|---|---|---|
| Focus series | `#6F47FF` | `#7C75FF` |
| Context series | `#A9AEC0` | `#565D6E` |

One focus series per chart. If two things need focus, it is two charts or a categorical chart.

### Categorical (when the series are the subject)

Fixed order. Slot 1 is always purple, then the next slots in order. Never skip, never reorder, never generate extra colors.

| Slot | Hue | Light | Dark | Label inside the fill |
|---|---|---|---|---|
| 1 | Purple | `#6F47FF` | `#7C75FF` | white |
| 2 | Teal | `#009FA0` | `#00A4A4` | `#141A21` |
| 3 | Amber | `#BB7400` | `#BE7C1C` | `#141A21` |
| 4 | Magenta | `#C06099` | `#C3699E` | white |
| 5 | Olive | `#7C9217` | `#82972F` | `#141A21` |
| 6 | Sky | `#0091CE` | `#1997CF` | `#141A21` |

Validation results (both modes pass every check):

| Check | Light | Dark |
|---|---|---|
| Lightness and chroma bands | pass | pass |
| Worst neighbour, colorblind (ΔE, target ≥ 8) | 14.1 | 13.2 |
| Worst neighbour, normal vision (ΔE, floor ≥ 15) | 18.3 | 17.6 |
| Contrast against the surface (≥ 3:1) | all 6 pass | all 6 pass |
| First 3 slots, any pair (for scatter, maps, small multiples) | pass (16.6) | pass (16.2) |

**Series limits:**
- Bars, stacks, lines: up to 6 series. More: fold the smallest into "Other", or split into small multiples.
- Scatter plots, maps, small multiples (any two colors can touch): **3 series maximum**. Slot 4 is not safe next to slot 2 for colorblind readers in these forms.
- From 4 series on, direct labels or a legend next to the marks are mandatory.

**Color follows the item, never its rank.** If a filter removes a series, the others keep their colors.

### Sequential (more = darker)

One hue: purple. Use for heatmaps, maps and any "how much" scale.

| Step | 100 | 200 | 300 | 400 | 500 | 600 | 700 |
|---|---|---|---|---|---|---|---|
| Hex | `#E5E5FF` | `#C9C7FF` | `#AAA4FF` | `#8C7AFF` | `#6F47FF` | `#5936C8` | `#432A99` |

- Continuous scales (heatmaps, maps) may use all steps; 100 means "close to zero".
- Ordered groups (tiers, funnel stages, age bands): light mode steps 300–700, dark mode steps 600 → 200 (light end on dark is the bright step). Both checked: one hue, even steps, the faintest step still ≥ 2:1 against the surface.

The node tier chart (Tier 1–10) is the typical use: tiers are ordered, so they take this ramp, never the categorical colors.

### Diverging (above / below a baseline)

Purple ↔ amber with a gray midpoint. Equal number of steps on each side.

| | Amber arm | Midpoint | Purple arm |
|---|---|---|---|
| Light | `#742E00` `#A95F00` `#E5A14B` | `#DADCE6` | `#AAA4FF` `#6F47FF` `#432A99` |
| Dark | `#E5A14B` `#CB7F00` `#8D4500` | `#2A303A` | `#5936C8` `#8C7AFF` `#C9C7FF` |

Purple is the "positive" or "Iagon" side unless the data says otherwise.

### Status (reserved)

Status uses the [tertiary palette](colors-typography.md#3-tertiary-palette-functional): green good, yellow warning, orange serious, red critical. Status colors never stand in for a series, and a series color never means a status. A status always comes with an icon and a word, never color alone.

Never in charts: gradients, the brand gradient, transparency stacks, glow.

## 4. Marks

| Element | Web | Canvas (posts, slides: ×2) |
|---|---|---|
| Bar thickness | max 24 px | max 48 px |
| Bar end | 4 px rounded at the data end, square at the baseline | 8 px |
| Gap between touching bars or stacked segments | 2 px in the surface color | 4 px |
| Line | 2 px, round joins | 4 px |
| Point marker | ≥ 8 px, with a 2 px surface-colored ring | ≥ 16 px, 4 px ring |
| Area fill | series color at 10% | same |
| Gridlines | 1 px solid, light `#E1E3EE`, dark `#262C35` | 2 px |
| Baseline / axis | 1 px, light `#A9AEC0`, dark `#3A414D` | 2 px |

- No borders around marks: the surface gap separates them.
- Gridlines only horizontal for bar and line charts, as few as needed (3–5). Never dashed.

## 5. Text in charts

All text is Figtree, in text colors, never in the series color. Identity comes from the colored mark next to the text (a dot or short line), not from colored text.

| Element | Web | Canvas | Color |
|---|---|---|---|
| Chart title (the finding) | Title-20 | H2 64 / H3 52 | `#141A21` |
| Subtitle (what is measured, unit, period) | Body-14 | Small 28 | `#62687E` |
| Axis labels, ticks | Body-12 | Caption 24 | `#62687E` |
| Direct labels, values | Body-14 / Body-14-strong | Small 28 / Caption 24 | `#141A21` |
| Legend | Body-14 | Caption 24 | `#62687E` |
| Big number | Numbers styles | Display number | `#141A21` |
| Source, "figures as of" | Body-12 | Fine print 18–20 | `#62687E` |

Dark mode: `#F2F2FA` and `#9097B0` instead.

- **Label selectively.** The last point of a line, the highlighted bar, the extreme. Never a number on every point.
- **Legend** for 2 or more series; none for one series (the title says what it is).
- **Numbers:** as in [Mechanics](../voice/mechanics.md). Axis ticks compact (10K, 2.4M). Display numbers on graphics follow their format page. Tables and axis ticks use tabular figures so columns align.
- Labels never overflow or get clipped by their bar. If a label does not fit inside, it goes outside the bar end or into the tooltip.

## 6. Interactive charts (web, dashboards)

- Hover: a tooltip on every bar, point or cell; on lines a vertical crosshair with all series values at that point.
- Hit area larger than the mark (at least 24 × 24 px).
- Filters in one row above the chart. Changing a filter never repaints the remaining series.
- A table view of the same data is always available (accessibility and copying).
- Dark mode uses the dark columns above. It is never an automatic color inversion.

## 7. Diagrams (architecture, flows, systems)

For the "architectural and system diagrams" in art direction: clean, accurate, technical.

| Element | Rule |
|---|---|
| Nodes (boxes) | Rounded rectangles, radius 8 web / 16 canvas, 1.5 px outline `#A9AEC0` (dark `#3A414D`), fill the surface or Surface 2 (`#EAEBF5` / `#191E25`) |
| The one element the diagram is about | Purple outline 2 px, or purple fill with white text. One per diagram |
| Connections | 1.5 px lines (3 px on canvas), `#62687E`, round caps. Arrows: small open chevrons, not filled triangles |
| Line routing | Straight or right-angle only, no curves across the diagram, no crossings where avoidable |
| Labels | Title-14 inside boxes, Body-12 on lines (canvas: ×2) |
| Icons | From the [icon library](icons.md), same color as the box text, 20 web / 40 canvas |
| Groups | A dashed outline is not used. Group with a Surface 2 background panel and a Title-12 caps label |
| Direction | Left → right for flows, top → bottom for hierarchies. One direction per diagram |

Keep a diagram under about 12 boxes. More than that is two diagrams or a zoom-in.

Never in diagrams: hexagon grids, glow, 3D, isometric servers, decorative particles or "network" backgrounds.

## 8. Checklist before publishing

1. The title states the finding.
2. The form fits the task (section 2); no pie, no dual axis, bars from zero.
3. Colors come from this page, in slot order; ≤ 6 series (≤ 3 in scatter and maps).
4. One focus at most in purple; status colors only for status.
5. Labels sparing, in text colors; source and date present.
6. Checked at real size: a 1200 px post viewed on a phone.
