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

Every marketing file that lives **outside GitHub**: decks, brandbooks, design sources, folders, dashboards. Files kept in the repo for convenience (like the brandbook PDFs) are listed here too, so there is one place to look. Keep one row per resource. When a resource is replaced, set the old row to `deprecated` instead of deleting it.

| ID | Name | Type | What it is | Link | Owner | Access | Updated | Status |
|---|---|---|---|---|---|---|---|---|
| res-brandbook | Iagon Brand Guidelines v1.0 | PDF | Visual guidelines (33 pages): brand intro, logo, colors, typography. Copy in the repo; original source _to add_ | [raw/archive](../raw/archive/2026-09-13-iagon-brandbook-v1.pdf) | Pavlo Babenko | Team | 2026-09-13 | active |
| res-brandbook-package | Iagon Brandbook Package | PDF | Brand strategy (61 pages, exported from Google Docs): vision, mission, Compliance Gap, DNA anchors, values, positioning, message box, audiences, narratives, proof library, objections, tone of voice, vocabulary. Copy in the repo; original Google Doc _to add_ | [raw/archive](../raw/archive/2026-08-12-iagon-brandbook-package.pdf) | Pavlo Babenko | Team | 2026-08-12 | active |
| res-claude-project-iagon | Claude Project "Iagon" | Other | Source docs of the first migration. See the manifest | [manifest](../raw/archive/2026-11-11-claude-project-iagon-sources.md) | Pavlo Babenko | Restricted | 2026-11-11 | active |
| res-logo-svg-source | Iagon logo SVG code | Other | SVG code of the four logo files, in the Claude Project doc `iagon-logo-svg-source.md` | Claude Project "Iagon" | Pavlo Babenko | Restricted | 2026-09-13 | active |
| res-insight-logo-svg | Iagon Insight logo SVG code | Other | SVG code of the Insight logo (on dark, on light), in the Claude Project doc `claude/iagon-insight-logo-svg.md` | Claude Project "Iagon" | Pavlo Babenko | Restricted | 2026-10-14 | active |
| res-stats-earned-template | "Total Earned By Nodes" post template | Other | Monthly 1200×700 HTML template. Change only the amount and the snapshot date | Claude Project "Iagon", `claude/iagon-ecosystem-stats-earned-selfcontained.html` | Pavlo Babenko | Restricted | 2026-10-21 | active |
| res-insight-landing | Iagon Insight landing | Other | Product site, Beta sign-up | https://insight.iagon.com | Product team | Public | 2026-10-14 | active |
| res-insight-api-docs | Iagon Insight API docs | Other | API reference | https://insight.iagon.com/docs/api | Product team | Public | 2026-10-14 | active |
| res-insight-mesh-page | Insight on MeshJS | Other | Official Mesh provider page | https://meshjs.dev/providers/iagon-insight | MeshJS | Public | 2026-10-22 | active |
| res-insight-x-r1-creatives | Insight X Ads R1 creatives | Other | 5 static cards 1200×1200 + 8 s video loops (`insight-x-r1-<n>-<name>`) | _location to add_ | Pavlo Babenko | Team | 2026-10-22 | active |
| res-wurth-m4-evidence | Würth M4 evidence package | Other | Public Catalyst evidence: reports, feedback, logs, screenshots | https://github.com/IagonAS/iagon-wurth-catalyst-public/tree/main/docs/milestone-4 | Iagon | Public | 2026-11-05 | active |
| res-wurth-m4-video | Würth M4 video walkthrough | Video | About 8 minutes, one order end to end on testnet | https://youtu.be/VSj8q51m_9A | Iagon | Public | 2026-11-05 | active |
| res-wurth-m4-acceptance | Würth Canada acceptance statement | PDF | Signed via DocuSign, accepts M4 as complete | https://iagon.media/Wurth-iagon-evidence-M4-confirmation.pdf | Iagon | Public | 2026-11 | active |

**Column guide**
- **ID:** stable, lowercase, starts with `res-`. Other pages and the future API refer to it. Never change an ID once it's set.
- **Type:** PDF, Deck, Figma, Canva, Drive folder, Sheet, Dashboard, Video, Other.
- **Access:** Public, Team, Restricted.
- **Status:** active, draft, deprecated.
