---
id: hub-resources
title: Resources outside GitHub
type: hub
status: approved
owner: Pavlo Babenko
updated: 2026-11-11
visibility: team
---

# Resources

Every marketing file that lives **outside GitHub**: decks, brandbooks, design sources, folders, dashboards. Keep one row per resource. When a resource is replaced, set the old row to `deprecated` instead of deleting it.

| ID | Name | Type | What it is | Link | Owner | Access | Updated | Status |
|---|---|---|---|---|---|---|---|---|
| res-brandbook | Iagon Brand Guidelines v1.0 | PDF | Visual guidelines (33 pages): brand intro, logo, colors, typography. Superseded where it differs from `wiki/brand/visual/` (decision 0004). Copy in the repo; original source _to add_ | [raw/archive](../raw/archive/2026-09-13-iagon-brandbook-v1.pdf) | Pavlo Babenko | Team | 2026-09-13 | active |
| res-stats-earned-template | "Total Earned By Nodes" post template | Other | Monthly 1200×700 HTML template. Spec: `wiki/brand/visual/formats/stats-earned-post.md`. Needs the 2026-11-12 updates | Claude Project "Iagon", `claude/iagon-ecosystem-stats-earned-selfcontained.html` | Pavlo Babenko | Restricted | 2026-10-21 | active |
| res-brandbook-package | Iagon Brandbook Package | PDF | Brandbook package with assets | _to add_ | Pavlo Babenko | Team | — | active |

**Column guide**
- **ID:** stable, lowercase, starts with `res-`. Other pages and the future API refer to it. Never change an ID once it's set.
- **Type:** PDF, Deck, Figma, Canva, Drive folder, Sheet, Dashboard, Video, Other.
- **Access:** Public, Team, Restricted.
- **Status:** active, draft, deprecated.
