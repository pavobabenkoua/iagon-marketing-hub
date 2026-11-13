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
| res-brandbook-package | Iagon Brandbook Package | Other | Brand strategy, messaging and tone of voice (Google Doc). The hub version lives in `wiki/brand/` and supersedes it; the Markdown export is archived in the repo. Original Google Doc _to add_ | [raw/archive](../raw/archive/2026-11-12-iagon-brandbook-package.md) | Pavlo Babenko | Team | 2026-11-12 | active |
| res-docs-iagon | Iagon public documentation | Other | docs.iagon.com, technical source of truth (decision 0005). Repository `iagon-public-documentation`, read-only for marketing. Snapshots in `raw/docs-snapshots/` | [docs.iagon.com](https://docs.iagon.com) | Docs team | Public | 2026-05-26 | active |
| res-fyeo-staking-audit | FYEO security assessment of the staking contract | PDF | v1.0, 18 November 2023, public. 2 Low findings, remediated. Copy in the repo | [raw/archive](../raw/archive/2023-11-18-fyeo-staking-contract-audit.pdf) | Docs team | Public | 2023-11-18 | active |
| res-dev-update-canvas | Development Update design canvas | Other | Claude Design canvas with the monthly recap cards. Spec: `wiki/brand/visual/formats/monthly-recap-cards.md`. Square artboards `post-square-1` and `post-square-2` are the template | [Claude artifact](https://claude.ai/artifact/NW3Yvcz8NTgo57Utkm9VsW) | Pavlo Babenko | Restricted | 2026-11-13 | active |

**Column guide**
- **ID:** stable, lowercase, starts with `res-`. Other pages and the future API refer to it. Never change an ID once it's set.
- **Type:** PDF, Deck, Figma, Canva, Drive folder, Sheet, Dashboard, Video, Other.
- **Access:** Public, Team, Restricted.
- **Status:** active, draft, deprecated.
