---
id: brand-colors-typography
title: Colors and typography
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources: [res-brandbook, raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [brand-logo, brand-format-industry-insights-card, brand-format-two-panel-post, brand-format-stats-earned-post, decision-0004]
tags: [visual, colors, typography, design-system]
---

# Colors and typography

Based on Brand Guidelines v1.0 (2026), with the brandbook errors corrected by [decision 0004](../../../decisions/0004-design-system.md). Where this page and the brandbook PDF differ, **this page wins**.

All contrast ratios on this page were recalculated (WCAG 2.1).

## 1. Primary palette

### Light mode

| Role | Name | HEX | RGB |
|---|---|---|---|
| Accent, main | Purple Main | `#6F47FF` | 111, 71, 255 |
| Accent, lighter | Purple Shade | `#7C75FF` | 124, 117, 255 |
| Background Bg-2 | Surface 1 | `#F6F6FB` | 246, 246, 251 |
| Background Bg-1 | Surface 2 | `#EAEBF5` | 234, 235, 245 |
| Titles | Titles | `#141A21` | 20, 26, 33 |
| Body text | Body | `#62687E` | 98, 104, 126 |

### Dark mode

| Role | Name | HEX | RGB |
|---|---|---|---|
| Accent, main | Purple Main | `#6F47FF` | 111, 71, 255 |
| Accent, lighter | Purple Shade | `#7C75FF` | 124, 117, 255 |
| Background Bg-2 | Surface 1 | `#13181E` | 19, 24, 30 |
| Background Bg-1 | Surface 2 | `#191E25` | 25, 30, 37 |
| Titles | Titles | `#F2F2FA` | 242, 242, 250 |
| Body text | Body | `#9097B0` | 144, 151, 176 |

**Purple text by mode:**
- On light, purple text is always **Purple Main `#6F47FF`** (4.85:1).
- On dark, purple text is always **Purple Shade `#7C75FF`** (4.97:1). Purple Main on dark gives only 3.42:1 and fails for text.

## 2. Secondary palette

For designs that need to stand out: packaging, alternative app themes, infographics. Also the Iagon Insight sub-brand (see [Logo](logo.md#iagon-insight-exception)).

| Name | HEX | RGB | Use |
|---|---|---|---|
| Blu (main) | `#5786FF` | 87, 134, 255 | step 500 of the scale |
| Violet | `#885EFF` | 136, 94, 255 | step 500 of the scale |
| Blu Text (light mode) | `#446CD2` | 68, 108, 210 | text and links |
| Violet Text (dark mode) | `#9E7CFE` | 158, 124, 254 | text and links |

Surfaces, titles and body text are the same as in the primary palette. Blu works on dark as is (5.3:1). Violet on dark needs the lighter `#9E7CFE`.

## 3. Tertiary palette (functional)

System notifications, statuses, infographic accents.

| State | Light: background | Light: text | Dark: background | Dark: text |
|---|---|---|---|---|
| Green | `#22AE78` | `#1A8059` | `#1B9E6C` | `#25C286` |
| Yellow | `#FFA341` | `#975A18` | `#F59F43` | `#FFB566` |
| Orange | `#FF604F` | `#B94E42` | `#E16152` | `#FF7362` |
| Red | `#E3456A` | `#D7234D` | `#CE4162` | `#E3456A` |

Every color has a dark-mode pair. Never carry light values into dark layouts.

## 4. Contrast rule

- **3:1** for backgrounds, icons and large titles. Bright colors can be combined freely here.
- **4.5:1** for text, links and outline buttons. Light mode: take the darker shade of the scale. Dark mode: take the lighter one.

### Text colors on light `#F6F6FB`

| Color | Contrast | Allowed for |
|---|---|---|
| `#141A21` Titles | 16.25:1 | titles, numbers, body |
| `#62687E` Body | 5.13:1 | body, notes, sources, secondary numbers |
| `#6F47FF` Purple Main | 4.85:1 | purple text |
| `#7C75FF` Purple Shade | 3.33:1 | **not for text on light**, graphics only |
| `#9097B0` | 2.69:1 | **never on light**: it's the dark-mode body color |

### Text colors on dark `#13181E`

| Color | Contrast | Allowed for |
|---|---|---|
| `#F2F2FA` Titles | 16.02:1 | titles, numbers |
| `#9097B0` Body | 6.15:1 | body, notes |
| `#7C75FF` Purple Shade | 4.97:1 | purple text |
| `#6F47FF` Purple Main | 3.42:1 | **not for text on dark**, graphics only |

## 5. Color balance

The purple gradient must never dominate an interface or a poster.

- The background is always a light or dark neutral.
- Purple is an accent that leads the eye to what matters.
- Plenty of white space keeps readability and focus.

Working proportions: about 1/8 purple, 1/8 to 1/4 dark or grey, the rest background.

### Gradients

- Allowed only in the logo symbol and in graphic elements (shapes, grid squares).
- **Never on text.** No gradient or neon text anywhere.
- Brand gradient: `#7C75FF` → `#6F47FF`.

## 6. Typography

**One typeface: Figtree** ([Google Fonts](https://fonts.google.com/specimen/Figtree)).

| Weight | Use |
|---|---|
| Semibold (600) | titles, headline numbers, buttons |
| Regular (400) | body text |
| Bold (700) | emphasis inside text only |

No other weights (no Light 300, no Medium 500).

Allowed: slightly tightened line height in titles, light negative tracking in titles, bold emphasis combined with a color highlight.

Not allowed: line height so tight that lines touch, tracking so tight that letters overlap, emphasis with bold only, without color.

## Brandbook errata

Errors in Brand Guidelines v1.0, fixed on this page:

1. **"RGB" values are actually HSB.** For `#6F47FF` the brandbook lists "rgb: 253, 72, 100", the real RGB is 111, 71, 255. Same on every card.
2. **Purple Shade has two values.** The palette page says `#7E67FF`, the contrast page and the logo files use `#7C75FF`. **`#7C75FF` is correct**: `#7E67FF` gives 4.48:1 on dark and fails for text.
3. **The dark-mode contrast page** labels `#7C75FF` as Main and `#6F47FF` as Shade. The names stay as in the palette; the rule "purple text on dark = `#7C75FF`" is what that page meant.
4. **Purple Main on light** is listed as 5.2:1. The real value on `#F6F6FB` is 4.85:1. It still passes.
5. **Pages 25–26** are titled "Primary Colors" but show the secondary palette.
6. **The Action section** (branded visuals, brand in use, mascot) is listed in the contents with page "xx" and is missing from the file.
