---
id: brand-logo
title: Logo
type: brand
status: draft
owner: Pavlo Babenko
updated: 2026-11-11
visibility: team
sources: [res-brandbook, res-logo-svg-source, raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [brand-colors-typography, product-insight]
tags: [visual, logo]
---

# Logo

Rules from Brand Guidelines v1.0 (2026). SVG code for all files lives in the Claude Project doc `iagon-logo-svg-source.md` ([res-logo-svg-source](../../resources.md)).

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
- Exception: Iagon Insight uses the version from its website (blue → violet gradient, "insight" in `#5786FF`). See [Iagon Insight](../../products/insight/product-brief.md#logo).

## Files

| File | What it is | SVG size | Use |
|---|---|---|---|
| `horizontal-color-light.svg` | gradient symbol + white wordmark | 605×136 | dark backgrounds, site header, dark-mode decks |
| `stacked-color-light.svg` | the same, stacked | 295×300 | dark backgrounds, narrow and square spaces, merch |
| `symbol-color.svg` | symbol only, gradient | 295×148 | dApp icon, avatar, favicon, merch |
| `logotype-white.svg` | wordmark only, white | 260×102 | building block for lockups, never used alone |

Symbol gradient: `#6F47FF` → `#7C75FF`, from bottom left to top right. Wordmark: `#FEFEFE`. For a light background, replace `#FEFEFE` with `#141A21` in the code.

"Light" in the file names means a light wordmark, i.e. a file for a **dark** background. Easy to mix up. Suggested rename: `-on-dark` / `-on-light`.

### Missing from the set

- Version for light backgrounds (same lockup, wordmark `#141A21`). Doesn't exist yet, although most brand materials are light.
- Monochrome white and monochrome black for print, stamps, embroidery.
- Symbol for dark backgrounds (the brandbook shows three circles: black, purple, white).
- Favicon 32×32 and 16×16 as separate files. At 16 px the symbol blurs and needs a simplified outline.

## Formats

- **SVG:** the base for web and print. Scales without loss, color changes in code.
- **PNG with transparency:** decks, documents, places without SVG support. Export @1x, @2x, @3x.
- **Vector PDF:** for printers.
- Never upscale raster. Need bigger? Use SVG.

## Minimum sizes

Working proposal. The brandbook has no section on this. Check in print before fixing.

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
