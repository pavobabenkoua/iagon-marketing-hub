---
id: brand-canvases
title: Canvas sizes and canvas type scale
type: brand
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
related: [brand-colors-typography, brand-art-direction, brand-format-industry-insights-card, brand-format-stats-earned-post, brand-format-two-panel-post, decision-0006]
tags: [visual, typography, social, canvases, sizes]
---

# Canvas sizes and canvas type scale

Sizes for every graphic we make (posts, carousels, stories, covers, slides) and the type scale that goes with them. The web and product scale is in [Colors and typography](colors-typography.md#6-typography). This page is its counterpart for fixed canvases.

Platform specs checked in November 2026 (sources at the end of the page). Platforms change them often: re-check twice a year.

## 1. The principle: design for the phone

A 1200 px wide post is seen on a phone about 360–400 px wide, so everything shrinks to about one third. Text that looks fine in Figma at 100% becomes unreadable in the feed.

This gives three rules, used by every serious brand system:

1. **One rule for the scale: canvas = web × 2.** The canvas scale is the web scale doubled. The hierarchy designers already know stays the same, and every value is an even number.
2. **A minimum: 24 px** for any text the reader should read, on any canvas 1080–1200 px wide (about 8 px on a phone). **Fine print** (sources, disclaimers, snapshot notes) is deliberately quiet: it must be there, not noticed. It may go down to 18 px, readable when the image is zoomed.
3. **Less text, larger.** A post carries one idea. If text does not fit at the minimum sizes, it belongs in the post copy, not on the image.

## 2. Canvas type scale

Applies to every canvas 1080–1200 px wide and to presented slides at 1920×1080. Figtree, weights 400 and 600, colors and contrast as in [Colors and typography](colors-typography.md).

| Role | Web style ×2 | Size / line height | Weight | Tracking |
|---|---|---|---|---|
| Display number | — | 160–220 / 1.0, set per format | 600 | −1% |
| Display | Title-60 | 120 / 120 | 600 | −1% |
| H1 | Title-46 | 92 / 100 | 600 | −1% |
| H2 | Title-32 | 64 / 76 | 600 | −1% |
| H3 | Title-26 | 52 / 60 | 600 | −1% |
| H4 | Title-20 | 40 / 48 | 600 | 0 |
| Subtitle | Title-20-alt | 40 / 48 | 400 | 0 |
| Lead | Body-18 | 36 / 52 | 400 | 0 |
| Body | Body | 32 / 48 | 400 | 0 |
| Small | Body-14 | 28 / 40 | 400 | 0 |
| Eyebrow | Title-14 | 28, caps | 600 | +4% |
| Caption (note to a number, label) | Body-12 | **24** / 32 | 400 | 0 |
| Fine print (source, disclaimer, snapshot note) | — | 18–20 / 24, `#62687E` | 400 | 0 |
| Stat (secondary number) | Numbers-28 | 56 / 64 | 400 | 0 |
| Code (JetBrains Mono) | Code | 28 / 44 | 400 | 0 |

Line heights for Lead, Body and Small are slightly tighter than web ×2 (1.4–1.45 instead of 1.6): on images, lines are short and loose leading breaks the block apart.

**Code on canvases:** at most a few lines. Long addresses and hashes are shortened in the middle on the image (`addr1qxd4…24cetc`), the full string goes in the post copy.

**Per canvas, use at most three roles** (for example Eyebrow, H1, Caption). More levels than that is a document, not a post.

### Reading decks

Decks sent as PDF to be read (not presented) may use a denser set at 1920×1080: Body 24 / 36, Small 22 / 32, Caption 20 / 28, H1 68 / 76, H2 48 / 56. Minimum 20 px, fine print 16 px. Presented decks use the canvas scale above.

## 3. Margins and safe zones

Columns and spacing inside canvases: [Grid and spacing](grid-spacing.md#4-social-canvases).

| Canvas width | Outer margin | Grid |
|---|---|---|
| 1080 | 64 px | 8 px steps |
| 1200 | 72 px | 8 px steps |
| 1920 | 96 px | 8 px steps |

- All text and the logo stay inside the margins.
- **Feed crops:** keep the key message in the centre 80% of the canvas. X and LinkedIn crop previews differently on mobile and desktop.
- **Vertical 1080×1920 (stories, reels, shorts):** keep text out of the top 250 px and the bottom 340 px, where the app puts the profile, buttons and caption.
- **Covers:** the avatar overlaps the bottom left of the X header and LinkedIn covers. Nothing important there.

## 4. Canvas sizes

### Our master sizes

| Canvas | Size | Ratio | Use |
|---|---|---|---|
| **Landscape post** | 1200×700 | ≈1.71:1 | Default for X and LinkedIn single images. Both show it uncropped: X shows ratios from 2:1 to 3:4 in full, LinkedIn crops only taller than 4:5. Used by the existing formats |
| **Square post** | 1080×1080 | 1:1 | LinkedIn and X when the post should take more space on a phone; multi-image posts; Instagram |
| **Portrait post / carousel page** | 1080×1350 | 4:5 | LinkedIn document carousels (PDF, every page the same size), Instagram feed. Takes the most feed space on a phone |
| **Vertical** | 1080×1920 | 9:16 | Stories, reels, shorts, X vertical video |
| **Slides, video** | 1920×1080 | 16:9 | Presentations, YouTube, X and LinkedIn video, webinar frames |

### Fixed platform sizes

| Item | Size | Note |
|---|---|---|
| X post, strict 16:9 | 1200×675 | When a template must be exactly 16:9, such as a video poster |
| Link preview (Open Graph) | 1200×630 | Website pages, blog posts. Shown on X, LinkedIn, Telegram, Slack |
| YouTube thumbnail | 1280×720 | |
| X header | 1500×500 | Avatar overlaps the bottom left |
| LinkedIn company page cover | 1128×191 | |
| LinkedIn personal cover | 1584×396 | Team members' profiles |
| Avatar (all platforms) | 400×400 | Logo symbol only, shown in a circle |

## 5. Export

- **Graphics with text:** PNG, exported at 2× (a 1200×700 post becomes 2400×1400), so text stays sharp on high-density screens. X accepts up to 5 MB on mobile. If the 2× PNG is too large, export at 1.5×.
- **Photos:** JPG, quality 85–90.
- **Carousels:** one PDF, all pages 1080×1350, fonts embedded, RGB. Aim under 10 MB.
- **Alt text** on every image on X and LinkedIn (LinkedIn has no alt text for PDF carousel pages: put the key line in the post copy).

## 6. Existing formats against the canvas scale

The approved formats predate this scale. Their main sizes fit it. Text meant to be read needs 24 px; fine print needs at least 18 px.

| Format | Element | Now | Canvas scale | Proposal |
|---|---|---|---|---|
| Industry Insights card | Eyebrow | 19.5 px Regular, caps | Eyebrow 28 Semibold, +4% | 28 px |
| | Note to the number | 23 px | Caption 24 | keep: 1 px off, not worth a change |
| | Insight lines | 44 px | between H4 (40) and H3 (52) | keep: fixed by the card layout |
| | Source | 19 px | Fine print 18–20 | keep |
| | Numbers | 214 / 190 / 104 px | Display number | keep |
| Total Earned By Nodes | Title | 35 px Semibold | H4 40 | 40 px |
| | Amount | 107 px | Display number | keep |
| | Snapshot note | 15 px | Fine print 18–20 | 18 px |
| Two-panel post | Disclaimer | "small" | Fine print 18–20 | 18 px |

These changes go into the next version of each format (open item D1). Existing posts are not redone.

## Sources

Platform specs, checked 2026-11-12:

- https://blog.hootsuite.com/social-media-image-sizes/
- https://skedsocial.com/blog/the-ultimate-up-to-date-social-media-image-sizes-guide
- https://skedsocial.com/blog/twitter-post-size-guide
- https://contentin.io/blog/linkedin-carousel-size/
- https://taplio.com/blog/linkedin-carousel-size
