---
id: brand-logo
title: Logo
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources: [res-brandbook, raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [brand-colors-typography, decision-0004]
tags: [visual, logo, design-system]
---

# Logo

Rules from Brand Guidelines v1.0 (2026), completed by [decision 0004](../../../decisions/0004-design-system.md). Files are in [`logos/`](logos/).

## Files

| File | What it is | Size | Use |
|---|---|---|---|
| [iagon-horizontal-on-dark.svg](logos/iagon-horizontal-on-dark.svg) | gradient symbol + white wordmark `#FEFEFE` | 605×136 | dark backgrounds, site header, dark-mode decks |
| [iagon-horizontal-on-light.svg](logos/iagon-horizontal-on-light.svg) | gradient symbol + dark wordmark `#141A21` | 605×136 | light backgrounds: posts, docs, light decks |
| [iagon-stacked-on-dark.svg](logos/iagon-stacked-on-dark.svg) | the same, stacked | 295×300 | dark backgrounds, narrow and square spaces, merch |
| [iagon-stacked-on-light.svg](logos/iagon-stacked-on-light.svg) | stacked, dark wordmark | 295×300 | light backgrounds, narrow and square spaces |
| [iagon-symbol.svg](logos/iagon-symbol.svg) | symbol only, gradient | 295×148 | dApp icon, avatar, favicon, merch |
| [iagon-wordmark-white.svg](logos/iagon-wordmark-white.svg) | wordmark only, white | 260×102 | building block for lockups, **never used alone** |
| [iagon-insight-on-dark.svg](logos/iagon-insight-on-dark.svg) | Iagon Insight sub-logo | 153×20 | Insight materials on dark |
| [iagon-insight-on-light.svg](logos/iagon-insight-on-light.svg) | Iagon Insight sub-logo | 153×20 | Insight materials on light |

The original brandbook file names said `-color-light` for the dark-background version. Here files are named by the background they go on: `-on-dark`, `-on-light`.

Symbol gradient: `#7C75FF` → `#6F47FF`, from bottom left to top right.

### Still missing

- Monochrome white and monochrome black for print, stamps, embroidery.
- Symbol on solid circles (the brandbook shows three: black, purple, white).
- Favicon 32×32 and 16×16. At 16 px the symbol blurs and needs a simplified outline.

## Composition

Symbol + wordmark, always together. Proportions never change.

- **Horizontal version:** the wordmark sits inside the symbol along the cut line. The gap between symbol and wordmark equals the width of the bowl of the letter "g".
- **Stacked version:** the wordmark sits inside the symbol along the contour cut. The gap equals the width of the letter "a".
- **Clear space:** take the letter "o" from the wordmark and double it. That is the minimum margin on every side.

## Symbol on its own

Can be used as a dApp icon, avatar for brand channels, on merch and on Iagon products (Cyclone etc.).

Clear space for icon and avatar: 1/4 of the symbol width. Or a 6×6 grid where the symbol takes the central 4×2. The same step works for corner radii.

## Co-branding

Both logos have the same real height and the same distance to the divider. Both brands' clear spaces must stay valid. For Cardano, for example, that is the width of six dots of the starburst.

## Modes and sub-logos

- **Three allowed modes:** light mode, dark mode, accent gradient.
- **Sub-logos:** "symbol + iagon + product name", with the product name in purple. Product wordmarks are drawn on Baboo Medium, tracking −1%.

### Iagon Insight exception

**Approved exception** ([decision 0004](../../../decisions/0004-design-system.md)). Insight uses the logo from its website, because that is what product users see:

| Part | Dark background | Light background |
|---|---|---|
| Symbol | gradient `#5786FF` → `#885EFF` | same |
| Wordmark "iagon" | `#F2F2FA` | `#141A21` |
| Product name "insight" | `#5786FF` | `#5786FF` |

On the site the logo is 20–24 px high. Action color in Insight materials: interface blue `#5786FF`. The exception applies only to Insight. Other products follow the sub-logo rule.

## Formats

- **SVG:** the base for web and print. Scales without loss, color changes in code.
- **PNG with transparency:** decks, documents, places without SVG support. Export @1x, @2x, @3x.
- **Vector PDF:** for printers.
- Never upscale raster. Need bigger? Use SVG.

## Minimum sizes

**Approved standard** ([decision 0004](../../../decisions/0004-design-system.md)).

| Version | Screen | Print |
|---|---|---|
| Horizontal | 140 px wide | 30 mm |
| Stacked | 70 px wide | 18 mm |
| Symbol | 24 px | 8 mm |

Below the threshold the wordmark is unreadable. Use the symbol alone.

## Don't

- Change logo colors. The gradient is fixed.
- Stretch or squash. Scale proportionally only.
- Rotate or skew.
- Change the gap between symbol and wordmark.
- Use the wordmark without the symbol.
- Place the logo on a busy photo or a gradient where it disappears. Need a photo background? Add a solid plate or a darkening overlay.
- Add shadow, outline, bevel or glow.
- Redraw the symbol or replace the wordmark font.
- Fit the logo tightly into a frame. Clear space is a double "o".
- Use the logo as part of a sentence or a headline.
