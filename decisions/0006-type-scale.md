---
id: decision-0006
title: Type scale
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-12
updated: 2026-11-12
---

# 0006: Type scale

## Context

The brand had one typeface (Figtree) and weights, but no sizes or line heights (open item D1). The director provided the Figma type specimen "Fonts": 33 named styles for web and product, in two weights (400 and 600). It differs from [0004](0004-design-system.md) on two points: 0004 allows Bold 700 for emphasis, and the formats set headline numbers in Semibold while the specimen's Numbers styles are Regular. The specimen file itself is not stored in the hub.

## Decision

1. **The Figma specimen is the web and product type scale.** It is recorded in [Colors and typography](../wiki/brand/visual/colors-typography.md#6-typography).
2. **Two weights: Regular 400 and Semibold 600.** Bold 700 is dropped. Emphasis inside text is Semibold 600. This supersedes point 6 of 0004.
3. **Numbers by role.** Data numbers in interfaces, dashboards and tables (up to 46 px) are Regular 400, as in the specimen. Display numbers on graphics (larger than 46 px) stay Semibold 600, as in the approved formats.
4. **No italic.** The snapshot note in "Total Earned By Nodes" becomes Regular.
5. **Purple text on `#EAEBF5`** (4.40:1) only at 24 px and up, or 19 px Semibold.
6. **Body-10** only for legal notes in interfaces. Nothing below 14 px on graphics at 1200 px width.

## Consequences

- D1 is half done: role mapping, mobile sizes, a marketing canvas scale, monospace and the layout grid are still open.
- Fixes for the specimen go to the designer (open items, D1).
