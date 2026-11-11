---
id: brand-colors-typography
title: Colors and typography
type: brand
status: draft
owner: Pavlo Babenko
updated: 2026-11-11
visibility: team
sources: [res-brandbook, raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [brand-logo, product-insight]
tags: [visual, colors, typography]
---

# Colors and typography

Extract from Brand Guidelines v1.0 (2026): everything needed for layout, UI and graphics. See [Open issues](#open-issues-to-confirm-with-the-designer) for places where the brandbook contradicts itself.

## 1. Primary palette

### Light mode

| Role | Name | HEX | RGB |
|---|---|---|---|
| Accent, main | Purple Main | `#6F47FF` | 111, 71, 255 |
| Accent, lighter | Purple Shade | `#7E67FF` | 126, 103, 255 |
| Background Bg-2 | Surface 1 | `#F6F6FB` | 246, 246, 251 |
| Background Bg-1 | Surface 2 | `#EAEBF5` | 234, 235, 245 |
| Titles | Titles | `#141A21` | 20, 26, 33 |
| Body text | Body | `#62687E` | 98, 104, 126 |

Purple Main on a light background has a 5.2:1 contrast ratio and passes AA.

### Dark mode

| Role | Name | HEX | RGB |
|---|---|---|---|
| Accent, main | Purple Main | `#6F47FF` | 111, 71, 255 |
| Accent, lighter | Purple Shade | `#7E67FF` | 126, 103, 255 |
| Background Bg-2 | Surface 1 | `#13181E` | 19, 24, 30 |
| Background Bg-1 | Surface 2 | `#191E25` | 25, 30, 37 |
| Titles | Titles | `#F2F2FA` | 242, 242, 250 |
| Body text | Body | `#9097B0` | 144, 151, 176 |

In dark layouts the lighter shade acts as the main purple. Otherwise contrast on the surfaces is too low.

## 2. Secondary palette

For designs that need to stand out: packaging, alternative app themes, infographics.

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

Brandbook example: in light mode `#7C75FF` as text gives 3.3:1 and fails, `#6F47FF` gives 4.9:1 and passes. In dark mode it's the other way round.

## 5. Color balance

The purple gradient must never dominate an interface or a poster.

- The background is always a light or dark neutral.
- Purple is an accent that leads the eye to what matters.
- Plenty of white space keeps readability and focus.

Working proportions from the brandbook: about 1/8 purple, 1/8 to 1/4 dark or grey, the rest background.

## 6. Typography

**One typeface: Figtree** ([Google Fonts](https://fonts.google.com/specimen/Figtree)).

| Weight | Use |
|---|---|
| Semibold (600) | titles, buttons |
| Regular (400) | body text |
| Bold (700) | emphasis inside text |

Allowed: slightly tightened line height in titles, light negative tracking in titles, bold emphasis combined with a color highlight.

Not allowed: line height so tight that lines touch, tracking so tight that letters overlap, emphasis with bold only, without color.

## Open issues to confirm with the designer

1. **"RGB" values in the brandbook are actually HSB.** For `#6F47FF` the brandbook lists "rgb: 253, 72, 100", but the real RGB is 111, 71, 255. Same on every card. The tables above use recalculated real RGB.
2. **Purple Shade has two values.** The palette page says `#7E67FF`, the contrast page says `#7C75FF`. The logo files use `#7C75FF` in the gradient, so `#7C75FF` is what's live; `#7E67FF` may be a brandbook error.
3. **The dark-mode contrast page** labels `#7C75FF` as Main and `#6F47FF` as Shade, the reverse of the palette page.
4. **Pages 25–26** are titled "Primary Colors" but show the secondary palette.
5. **The Action section** (branded visuals, brand in use, mascot) is listed in the contents with page "xx" and is missing from the file.
