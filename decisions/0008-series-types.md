---
id: decision-0008
title: Series types
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-13
updated: 2026-11-13
amends: decision-0003
---

# 0008: Series types

## Context
The series template assumed one kind of series: a story told in acts, where every post has a role in an arc. That fits Würth × Iagon. It does not fit Development Update, where every issue has the same structure and only the data changes, and it does not fit reusable community posts. Without types, each new series page invents its own sections and the series can't be compared or reviewed the same way.

## Decision

### 1. Three types

| Type | What it is | Examples | Changes from post to post | Stays the same |
|---|---|---|---|---|
| `recurring` | A regular issue built from data | Development Update, Total Earned By Nodes | Only the data | Layout, text structure, data source |
| `thematic` | One theme, every post written from scratch | Würth × Iagon | Thesis, facts, text, elements on the visual | Theme, visual system, boundary |
| `evergreen` | A set of reusable posts on rotation | Discord and YouTube invitations | Which post from the set goes out | The set of texts |

Every type has a cadence.

### 2. Arc is a flag of thematic series
A thematic series sets `arc: true` when the order of posts matters (acts, a story that builds). It sets `arc: false` when posts are independent and only the theme and visual system tie them together.

### 3. Formats and channels are not types
An article for LinkedIn or the blog is a format. It belongs to a thematic series or stands alone.

### 4. Posts outside series
Posts that belong to no series (releases, announcements) live in `wiki/posts/`, named `YYYY-MM-DD-slug.md`, with the post template and an empty `series` field.

### 5. Metadata
Series pages add to the fields of [0003](0003-metadata-standard.md):

| Field | Required | Values |
|---|---|---|
| `series_type` | yes | `recurring`, `thematic`, `evergreen` |
| `arc` | thematic only | `true`, `false` |
| `cadence` | yes | Plain words: `weekly`, `every two weeks`, `monthly`, `first week of the month` |

### 6. Required sections by type

| Section of `series.md` | recurring | thematic | evergreen |
|---|---|---|---|
| Idea, goal, narrative, boundary, audience | yes | yes | yes |
| Formats and channels | yes | yes | yes |
| Cadence | yes | yes | yes |
| Data source and build | yes | — | — |
| Issue structure (fixed wording) | yes | — | — |
| Arc | — | if `arc: true` | — |
| Lines already used (not to repeat) | — | yes | — |
| Post set and rotation rules | — | — | yes |
| Rules, posts, commitments, status | yes | yes | yes |

### 7. Evergreen rules apply to every evergreen series
- Every invitation says what the reader gets there, not that they should hurry. No urgency, no FOMO.
- The same post does not repeat on a channel within a minimum gap set by the series.

## Consequences
- `templates/series.md` gets the type fields and the sections by type.
- Development Update gets `series_type: recurring`. Würth gets `series_type: thematic`, `arc: true` when it moves into the hub.
- A new type is added by a new decision that amends this one.
