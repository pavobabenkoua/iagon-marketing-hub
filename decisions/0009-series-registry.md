---
id: decision-0009
title: Series registry
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-13
updated: 2026-11-13
amends: decision-0008
---

# 0009: Series registry

## Context
The only list of series lived in a Claude Project file outside the hub. Nothing showed which series are running, which have gone quiet, or whether a new idea is really a new series. Keeping that list by hand would copy every series' state, cadence and channels into a second place, and the two would drift apart.

## Decision

### 1. One registry, generated
The registry is a table in [`wiki/series/README.md`](../wiki/series/README.md), between the markers `<!-- registry:start -->` and `<!-- registry:end -->`. `scripts/series-registry.py` builds it from the frontmatter of every `series.md` and the publication dates of its posts. Nobody edits the table by hand. Run the script after any change to a series or a new post; `--check` fails if the table is out of date or a series misses a field.

### 2. Columns
Series, About, Type, Narrative, Cadence, Channels, State, Last post, Owner.

### 3. Series fields
Added to the fields of [0008](0008-series-types.md):

| Field | Required | Values |
|---|---|---|
| `summary` | yes | One sentence: what the series is about, for someone who has never seen it |
| `narrative` | yes | `01`–`05`, the brand narrative it carries ([five narratives](../wiki/brand/messaging/five-narratives.md)) |
| `state` | yes | `planned`, `active`, `paused`, `finished`. The life of the series. Not the same as `status`, which says whether the page itself is approved |
| `cadence` | yes | Now a fixed list: `weekly`, `biweekly`, `monthly`, `quarterly`, `irregular` |

### 4. Last post
The latest `publications` date across the series' `posts/`. A post without `publications` doesn't count.

### 5. Rules
- **A new series** starts only if no existing series covers the same narrative and audience. Otherwise the idea is an issue of an existing series.
- **Overdue.** An `active` series with no post for two of its cycles (weekly: 14 days, biweekly: 28, monthly: 62, quarterly: 184) is marked overdue in the registry. `irregular` series are never overdue.
- **Quarterly review.** Every quarter, each overdue series is paused with a reason in its Status section, or finished. A series that quietly stops costs more trust than one that ends.

## Consequences
- `templates/series.md` gets `summary`, `narrative`, `state` and the fixed `cadence` list.
- Development Update becomes the Monthly Recap series. The Weekly Update will be a separate series with its own cadence.
- The registry in the Claude Project is retired in step 7 of the series setup.
