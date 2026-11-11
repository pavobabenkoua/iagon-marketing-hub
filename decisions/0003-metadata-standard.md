---
id: decision-0003
title: Metadata and naming standard
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-11
updated: 2026-11-11
---

# 0003: Metadata and naming standard

## Context

The hub is read by people, AI agents and, later, an API. Every page needs the same machine-readable header so tools can filter by status, check freshness, follow links between pages and keep private material out of the API.

## Decision

### 1. Frontmatter

Every Markdown page in `wiki/` and `decisions/` starts with a YAML frontmatter block:

```yaml
---
id: product-insight
title: Iagon Insight
type: product
status: approved
owner: Pavlo Babenko
updated: 2026-11-11
reviewed: 2026-11-11
visibility: team
sources: [raw/archive/2026-10-02-insight-brief.md]
related: [campaign-2026-insight-x-ads, series-wurth]
tags: [analytics, launch]
---
```

**Exempt:** folder `README.md` files, which only describe what a folder is for, and the hub files `index.md`, `log.md`, `AGENTS.md` and the root `README.md`.

### 2. Fields

| Field | Required | Values / rule |
|---|---|---|
| `id` | yes | Stable ID, see section 3 |
| `title` | yes | Human-readable title |
| `type` | yes | `brand`, `product`, `audience`, `data`, `channel`, `series`, `post`, `campaign`, `partner`, `playbook`, `decision`, `hub` |
| `status` | yes | `draft`: work in progress. `approved`: approved by the director. `deprecated`: outdated, kept so links still work |
| `owner` | yes | Person responsible for the page |
| `updated` | yes | Date of the last content change, `YYYY-MM-DD` |
| `reviewed` | no | Date the facts were last checked. Informational: there are no automatic staleness thresholds |
| `visibility` | no | `public`: may be shared outside. `team`: internal (**default**). `private`: never exposed through the API |
| `sources` | no | Where the information comes from: paths in `raw/` or resource IDs (`res-brandbook`) |
| `related` | no | IDs of connected pages. These links form the graph of the hub |
| `tags` | no | Free keywords, lowercase |

Deliberately left out: `author` (git records it) and an `in-review` status (approval happens in the chat, see [0002](0002-chat-approval-and-auto-merge.md)).

`hub` is the type for hub-level pages that are not knowledge themselves, such as `wiki/resources.md`.

### 3. IDs

- Format: `<type>-<slug>`, lowercase, words joined by hyphens.
- Examples: `product-insight`, `series-wurth`, `post-wurth-03`, `campaign-2026-insight-x-ads`, `decision-0003`.
- Resources in `wiki/resources.md` use the `res-` prefix: `res-brandbook`.
- **An ID never changes once set**, even if the file is renamed or moved.

### 4. File and folder names

- English, lowercase, hyphens, no spaces or special characters.
- Dates are always `YYYY-MM-DD`.
- Date-bound files (raw sources, reports) start with the date: `2026-11-11-x-ads-results.csv`.
- Campaign folders: `YYYY-slug` (`2026-insight-x-ads`).
- Posts in a series are numbered by their place in the arc: `posts/03-storage-myth.md`.
- Decisions: `NNNN-slug.md`, numbered in order.

## Consequences

- Templates (block 1.4) and automated checks (Phase 5) are built on this standard.
- The future API serves only `approved` pages whose visibility is not `private`.
