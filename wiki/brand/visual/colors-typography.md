---
id: brand-colors-typography
title: Colors and typography
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-13
reviewed: 2026-11-12
visibility: team
sources: [res-brandbook, raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [decision-0006, brand-logo, brand-format-industry-insights-card, brand-format-two-panel-post, brand-format-stats-earned-post, decision-0004]
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

This is the brand's version of the 60-30-10 rule used in interface and graphic design: most of the canvas neutral, a smaller share of text and structure, a small accent.

### Attention

The eye goes first to the most saturated, highest-contrast element. Every layout decides what that is.

- **One accent point per canvas.** The logo symbol is the brand signature and stays in color ([logo rules](logo.md)). Besides it, purple goes to at most one element: the one number or word the piece is about. Many canvases need none. 1/8 is a ceiling, not a target: purple in several places splits attention even within 1/8.
- **Decoration stays below content.** Spheres, patterns, grids and shapes are texture, not message. They are tonal and light: the palette neutral at low opacity (`#62687E` on light, `#9097B0` on dark, about 20 to 35%), never a midtone that competes with text. They take purple only if they are the accent point themselves.
- **Neutrals come from the palette.** No pure grey and no grayscale filters: the Iagon neutrals are cool and slightly violet, and a pure grey next to them looks dirty.
- **Order of reading:** title, then the accent, then everything else, decoration last. Check it at feed size (about one third, see [canvases](canvases.md)) or by squinting at the layout: if decoration is seen before the title, it is too strong.

These rules match the leading design systems: Apple ("apply your accent color judiciously… too broadly can overwhelm and dilute its impact", "branding always defers to content"), Google Material 3 ("the human eye is particularly drawn to vibrant colors"; neutral surfaces "represent the majority"), IBM Carbon (neutral grey dominant, accents "used sparingly and purposefully", avoid midtones), Refactoring UI (tinted greys, "one primary element per view") and the Nielsen Norman Group squint test.

### Gradients

- Allowed only in the logo symbol and in a graphic element (shape, grid square) that is the canvas's accent point.
- **Never on text.** No gradient or neon text anywhere.
- Brand gradient: `#7C75FF` → `#6F47FF`.

## 6. Typography

**One brand typeface: Figtree** ([Google Fonts](https://fonts.google.com/specimen/Figtree)). For code and technical strings only: JetBrains Mono (see Code below). Source of the scale: the Figma type specimen "Fonts" (web and product). Decision [0006](../../../decisions/0006-type-scale.md).

### Weights

| Weight | Use |
|---|---|
| Semibold (600) | titles, display numbers on graphics, buttons, emphasis inside text |
| Regular (400) | body text, data numbers in interfaces and tables |

**Two weights only.** No Bold 700, no Medium 500, no Light 300. No italic. (JetBrains Mono: 400 only.)

### Web and product scale

Units in rem, base 16 px. All values in px are multiples of 2.

**Titles (Semibold 600)**

| Style | Size | Line height | Tracking |
|---|---|---|---|
| Title-60 | 3.75rem (60) | 3.75rem (60) | −1% |
| Title-56 | 3.5rem (56) | 3.875rem (62) | −1% |
| Title-46 | 2.875rem (46) | 3.125rem (50) | −1% |
| Title-40 | 2.5rem (40) | 2.75rem (44) | −1% |
| Title-32 | 2rem (32) | 2.375rem (38) | −1% |
| Title-26 | 1.625rem (26) | 1.875rem (30) | 0 |
| Title-20 | 1.25rem (20) | 1.5rem (24) | 0 |
| Title-20-alt | 1.25rem (20), **Regular 400** | 1.5rem (24) | 0 |
| Title-16 | 1rem (16) | 1.25rem (20) | 0 |
| Title-14 | 0.875rem (14) | 1.125rem (18) | 0 |
| Title-12 | 0.75rem (12) | 1rem (16) | 0 |

**Text (Regular 400)**

| Style | Size | Line height | Variants |
|---|---|---|---|
| Body-18 | 1.125rem (18) | 1.75rem (28) | |
| Body | 1rem (16) | 1.625rem (26) | Body-strong (600), Body-underline |
| Body-14 | 0.875rem (14) | 1.375rem (22) | Body-14-strong (600), Body-14-underline |
| Body-12 | 0.75rem (12) | 1rem (16) | Body-12-underline |
| Body-10 | 0.625rem (10) | 0.875rem (14) | interface legal notes only |

Underline variants are for links.

**Numbers (Regular 400)**, for data in interfaces, dashboards and tables

| Style | Size | Line height |
|---|---|---|
| Numbers-20 | 1.25rem (20) | 1.5rem (24) |
| Numbers-24 | 1.5rem (24) | 1.75rem (28) |
| Numbers-28 | 1.75rem (28) | 2rem (32) |
| Numbers-36 | 2.25rem (36) | 2.25rem (36) |
| Numbers-40 | 2.5rem (40) | 2.5rem (40) |
| Numbers-46 | 2.875rem (46) | 2.875rem (46) |

### Rules

- **Numbers by role.** Data numbers up to 46 px use the Numbers styles, Regular 400. Display numbers on graphics (posts, cards, slides, larger than 46 px) are Semibold 600, as in the [formats](formats/README.md).
- **Colors.** Titles and numbers `#141A21`, text `#62687E`, links and labels `#6F47FF` (light mode). Dark mode: section 4.
- **Purple text on `#EAEBF5`** (Bg-1) is 4.40:1, below 4.5:1. On that background purple text must be at least 24 px, or 19 px Semibold. On `#F6F6FB` the normal rules apply.
- **Minimum sizes.** Body-10 only for legal notes in interfaces. Never below 14 px on graphics at 1200 px width.
- **Line length** for running text: 60–75 characters.
- **Tracking:** −1% only from 32 px up. Never on text sizes. One exception: +4% on caps eyebrows (see Roles).
- Emphasis inside text: Semibold 600, combined with a color highlight. Never weight alone.

Not allowed: line height so tight that lines touch, tracking so tight that letters overlap, weights or styles outside this page.

### Code: JetBrains Mono

A monospace font: every character has the same width. It keeps characters that look alike in Figtree apart (`0` / `O`, `1` / `l` / `I`) and tells the reader "copy this exactly". Free, [Google Fonts](https://fonts.google.com/specimen/JetBrains+Mono). Already used by docs.iagon.com (Figma style "specialHighlight").

| Style | Size / line height | Weight | Use |
|---|---|---|---|
| Code | 14 / 22 (0.875rem / 1.375rem) | 400 | Inline code and code blocks on web and in docs |
| Code-12 | 12 / 18 (0.75rem / 1.125rem) | 400 | Dense tables of identifiers |

Inline code on light: text `#141A21`, background `#6F47FF` at 10%, radius 6 px, horizontal padding 8 px (as in the docs).

**Use only for:** code, API requests and responses, CLI commands, wallet and contract addresses, policy IDs, hashes, transaction IDs, file names and paths.

**Never for:** headlines, ordinary numbers, labels, or decoration to look "technical".

### Roles

Which style to use for which element. Use roles in briefs and code (`H2`, `Button`), not raw sizes.

**Headings**

| Role | Desktop ≥1280 | Tablet 768–1279 | Mobile <768 | Notes |
|---|---|---|---|---|
| Display | Title-60 | Title-46 | Title-40 | Hero of a landing page only. At most one per page |
| H1 | Title-46 | Title-40 | Title-32 | Page title. Exactly one per page |
| H2 | Title-32 | Title-32 | Title-26 | Section |
| H3 | Title-26 | Title-26 | Title-20 | Subsection, large card title |
| H4 | Title-20 | Title-20 | Title-16 | Card title, block title |
| H5 | Title-16 | Title-16 | Title-14 | Small group title, list heading |
| Subtitle | Title-20-alt | Title-20-alt | Body-18 | One or two lines under H1 or Display |
| Eyebrow | Title-14, caps, +4% tracking, `#6F47FF` | same | Title-12, caps, +4% | Short label above a title: category, series name |

**Text**

| Role | All sizes | Mobile | Notes |
|---|---|---|---|
| Lead | Body-18 | Body | First paragraph of an article or section |
| Body | Body | Body | Running text. Never below 16 px on mobile |
| Body emphasis | Body-strong | Body-strong | With a color highlight, see Rules |
| Secondary | Body-14 | Body-14 | Card text, descriptions, table cells |
| Caption | Body-12 | Body-12 | Image captions, sources, dates, timestamps |
| Legal | Body-10 | Body-12 | Interface legal notes only |
| Link | the underline variant of the surrounding size | same | `#6F47FF` on light, `#7C75FF` on dark |
| Quote | Title-26, Regular 400 | Title-20-alt | Pull quotes. Weight 400 to set them apart from H3 |

**Interface**

| Role | Style | Notes |
|---|---|---|
| Button large | Title-16 | Hero and main calls to action. Min. height 48 px |
| Button | Title-14 | Default. Min. height 44 px (touch target) |
| Button small | Title-12 | Dense tables and toolbars, desktop only |
| Navigation | Title-14 | Top and side navigation |
| Tab, chip, badge | Title-12 | |
| Form label | Title-14 | Above the field |
| Input text | Body | 16 px, also on mobile: smaller text makes iOS zoom in |
| Helper and error text | Body-14 | Error in the error color, never only red without text |
| Table header | Title-14 | |
| Table cell | Body-14 | Numbers in cells: Body-14, right-aligned |
| Tooltip | Body-12 | |

**Numbers**

| Role | Desktop | Tablet | Mobile |
|---|---|---|---|
| KPI (main figure in a stat card) | Numbers-46 | Numbers-40 | Numbers-36 |
| Stat (secondary figure) | Numbers-28 | Numbers-28 | Numbers-24 |
| Inline data | Numbers-20 | Numbers-20 | Numbers-20 |

### Logic behind the roles

- **No new sizes.** Every role and every breakpoint uses a style from the specimen.
- **Each level stays at least ~1.2× the next** (desktop 46 → 32 → 26 → 20 → 16, mobile 32 → 26 → 20 → 16 → 14), so hierarchy survives on small screens.
- **Large titles shrink, text does not.** Display and H1 step down most; body sizes stay, because reading distance on a phone is shorter, not longer.
- **One H1, no skipped levels** (H2 after H1, H3 after H2). This is also what screen readers and search engines expect.
- **Caps need air.** Eyebrows are the one place with positive tracking (+4%). Caps text only in eyebrows, never longer than one line.
- **Title-56 is not mapped.** It duplicates Title-60 (open item D1).

### Not defined yet

The scale for fixed canvases (posts, carousels, slides) is in [Canvas sizes and canvas type scale](canvases.md).

Grid and spacing: [Grid and spacing](grid-spacing.md).

## Brandbook errata

Errors in Brand Guidelines v1.0, fixed on this page:

1. **"RGB" values are actually HSB.** For `#6F47FF` the brandbook lists "rgb: 253, 72, 100", the real RGB is 111, 71, 255. Same on every card.
2. **Purple Shade has two values.** The palette page says `#7E67FF`, the contrast page and the logo files use `#7C75FF`. **`#7C75FF` is correct**: `#7E67FF` gives 4.48:1 on dark and fails for text.
3. **The dark-mode contrast page** labels `#7C75FF` as Main and `#6F47FF` as Shade. The names stay as in the palette; the rule "purple text on dark = `#7C75FF`" is what that page meant.
4. **Purple Main on light** is listed as 5.2:1. The real value on `#F6F6FB` is 4.85:1. It still passes.
5. **Pages 25–26** are titled "Primary Colors" but show the secondary palette.
6. **The Action section** (branded visuals, brand in use, mascot) is listed in the contents with page "xx" and is missing from the file.
