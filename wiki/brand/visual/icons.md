---
id: brand-icons
title: Icons
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
related: [brand-colors-typography, brand-canvases, brand-grid-spacing, brand-art-direction]
tags: [visual, icons, iconography, design-system]
---

# Icons

The rules for using and making icons. The library is the designer's Figma page "Icons": about 280 line icons in 25 categories, based on the Xnix pack with Iagon optimisations and custom icons. Every new icon, drawn by a designer or generated, follows the construction rules in section 3, so it cannot be told apart from the library.

## 1. Style in one line

**Outline icons, 1.5 px stroke on a 24 px grid, round caps and joins, one color, no fills.**

| Property | Value |
|---|---|
| Frame | 24 × 24 px |
| Live area | 20 × 20 px, 2 px padding on every side |
| Stroke | 1.5 px, centered on the path |
| Caps and joins | round |
| Color | one color, set by the context (section 4) |
| Fill | none. Exception: dots up to 3 px (the dot of "i", "more" dots), filled in the stroke color |
| Corner radius | 2 px on squares and rectangles at 24 px, 1 px on small inner shapes |
| Angles | 0°, 45°, 90° only. Other angles only when the metaphor requires it (a lightning bolt, a pen) |

## 2. Sizes

| Context | Icon size | Stroke | Paired with |
|---|---|---|---|
| Web, dense | 16 | 1.5 × 16/24 ≈ 1 | Body-14, Title-14, buttons |
| Web, default | 20 | 1.25 | Body, Body-strong |
| Web, large | 24 | 1.5 | Title-20 and larger, navigation |
| Canvas (posts, slides) | 32 / 40 / 48 | 2 / 2.5 / 3 | canvas Small / Body / H4 and up |
| Feature illustration | 64–96 | 4–6 | only as a single centred element, never in a row |

**The stroke scales with the icon.** An icon is always drawn at 24 and scaled as a whole. Never redraw a large icon with a 1.5 px stroke: it looks thin and off-brand.

Icon to text gap: 8 px at 16–20, 12 px at 24, 16 px on canvases. Icon centred on the first line of text.

## 3. Construction rules (for new icons)

### Keylines

Basic shapes fill the live area to the same optical weight. Outer edges, stroke included:

| Shape | Size |
|---|---|
| Circle | 20 × 20 |
| Square | 18 × 18 |
| Portrait rectangle | 16 × 20 |
| Landscape rectangle | 20 × 16 |

### Detail

- **Minimum gap** between two parallel strokes: 2 px. Below that, lines merge at 16 px.
- **Maximum detail:** an icon reads in under a second at 16 px. If it needs more than about 6 strokes, simplify.
- **Modifiers** (plus, cross, check, arrow) sit in the bottom right, inside a 10 × 10 area, with a 1.5 px cut-out gap around them in the main shape.
- **Open shapes:** strokes end with round caps, never sharp.
- **Perspective:** none. Everything is flat and frontal. No 3D, no isometric.
- **Text inside icons:** only short tokens that are part of the metaphor ("31" on a calendar, "HDR"). Never words.

### Metaphors for Iagon

Use the most literal, widely known metaphor. If a user would need a caption to understand the icon, it is the wrong icon.

| Concept | Metaphor |
|---|---|
| Storage | a stacked cylinder (database) or a drive |
| Node | a server unit: rounded rectangle with two indicator dots |
| Network | three or four circles joined by lines |
| Encryption | a file with a lock |
| Ownership, keys | a key |
| Compliance | a document with a check mark and a shield |
| Jurisdiction, data region | a map pin over a globe |
| Audit, access log | a list with a magnifier |
| Blockchain | two linked rounded squares |
| Token | a circle with an inner ring (no currency symbol) |
| Staking | a token with a lock |
| Wallet | a wallet shape |
| Compute | a chip |

Never: hexagon grids, glowing or neon effects, crypto clichés (rockets to the moon, coins with rays, lightning around a coin).

### Delivery format

Every icon is one SVG file:

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"
     fill="none" stroke="currentColor" stroke-width="1.5"
     stroke-linecap="round" stroke-linejoin="round">
  <!-- paths only, on whole or half pixels -->
</svg>
```

- `viewBox="0 0 24 24"`, color through `currentColor` so the icon takes the text color.
- Strokes stay strokes (editable). No outlined strokes, no masks, no transforms, no embedded images, no IDs.
- Coordinates on whole or half pixels so 1.5 px strokes render sharp.
- File name: `icon-<category>-<name>.svg`, lowercase, hyphens (`icon-security-file-lock.svg`). Categories as in the library.

### Checklist for a generated icon

1. 24 frame, nothing outside the 20 × 20 live area.
2. Stroke 1.5, round caps and joins, no fills except dots.
3. Same optical size as a library icon next to it (compare with a circle icon).
4. Readable at 16 px.
5. Only 0°, 45°, 90° unless the metaphor needs otherwise.
6. SVG matches the delivery format above.

## 4. Color

| Where | Color |
|---|---|
| Next to text | the color of that text: `#141A21` or `#62687E` |
| On dark backgrounds | `#F2F2FA` or `#9097B0` |
| Active state, one accent | `#6F47FF` on light, `#7C75FF` on dark |
| Disabled | 40% opacity of the normal color |

- Meaningful icons need 3:1 contrast against the background (WCAG 2.1 non-text contrast).
- **Never** gradients on icons, never two colors in one icon, never colored backgrounds behind each icon in a list.

## 5. Use

- **One set only.** Never mix with other packs, filled or duotone styles, or emoji.
- **Icons support text, they do not replace it.** In marketing an icon is never the hero of a post. Exception: one large feature icon (section 2) as the single visual of a slide.
- **Lists of benefits:** 3–6 items, same icon size, same distance to text, all icons from the same category style.
- **Icon-only buttons** carry a text label for screen readers and a tooltip. Decorative icons are hidden from screen readers (`aria-hidden="true"`).
- **Social network icons** only for links to our own profiles. Brand logos of other companies follow their own guidelines and are not redrawn.

## 6. Library gaps

To draw by the rules above (designer task):

- Node / server unit
- Network of nodes
- Blockchain link
- Wallet
- Token, staking (token with lock)
- File with lock (encryption)
- Compliance document (check + shield)
- Jurisdiction (pin over globe)
- Audit log (list + magnifier)
- Social: Telegram, GitHub, if we use these channels

Open questions (open item D4): the license of the Xnix base pack covers marketing use and every person working with the file; which social channels Iagon actively uses.
