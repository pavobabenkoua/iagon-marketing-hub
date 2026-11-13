---
id: series-<slug>
title: <Series name>
type: series
status: draft
owner: Pavlo Babenko
updated: YYYY-MM-DD
visibility: team
summary: <One sentence: what the series is about, for someone who has never seen it>   # decision 0009
series_type: <recurring | thematic | evergreen>   # decision 0008
arc: <true | false>                             # thematic only; delete for other types
narrative: <01 | 02 | 03 | 04 | 05>             # wiki/brand/messaging/five-narratives.md
cadence: <weekly | biweekly | monthly | quarterly | irregular>
state: <planned | active | paused | finished>   # the life of the series; `status` is the page approval
channels: [x, linkedin]
related: []
tags: []
---

<!--
Keep the sections for your type and delete the rest (decision 0008):
  all types:   Idea, Goal, Narrative and boundary, Audience, Format, Cadence, Rules, Approval, Posts, Commitments, Status
  recurring:   + Data source and build, Issue structure
  thematic:    + Arc (only if arc: true), Lines already used
  evergreen:   + Post set and rotation
-->

# <Series name>

## Idea
The series in one or two sentences.

## Goal
What the series should achieve: awareness, education, conversion, community. How we measure it.

## Narrative and boundary
- **Narrative:** which of the five brand narratives it carries (`wiki/brand/`).
- **Never becomes:** the nearby version of this series we don't publish.

## Audience
Which segments from `wiki/audiences/` it targets.

## Format
Post format, length, channels. For every visual, link its format page in `wiki/brand/visual/formats/` and its template in `layouts/` (decision 0007).

## Cadence
How often a post goes out, on which channels, and what happens when there is nothing to publish.

## Data source and build
_Recurring only._ Where the data comes from (`raw/archive/`), the inputs file (`inputs/`), the command that builds an issue, what it checks (decision 0011).

## Issue structure
_Recurring only._ The fixed parts of every issue: opener, block structure, close. The exact wording lives in `issue/`, one file per channel; link to it here.

## Arc
_Thematic with `arc: true` only._ The stages of the series and what each stage does.

| Stage | Purpose | Posts | Status |
|---|---|---|---|
| 1. Opening | | | |

## Lines already used
_Thematic only._ Key phrases already published. Don't repeat them word for word.

## Post set and rotation
_Evergreen only._ The posts in rotation, the minimum gap before one repeats on the same channel, and the order.

| Post | Channels | Last published |
|---|---|---|
| [title](posts/slug.md) | | YYYY-MM-DD |

## Rules
Only rules that follow from this series' subject. Each rule on one line, then why it exists.

Link, don't copy (decision 0010):

| Rules about | Live in |
|---|---|
| Voice, colours, type | `wiki/brand/` |
| A visual | its page in `wiki/brand/visual/formats/` and `layouts/` |
| A channel: limits, markup, communication approach, audience | `wiki/channels/` |
| Numbers and claims | `wiki/data/`, `wiki/brand/messaging/proof-library.md` |
| A partner or project | `wiki/partners/` |

## Approval
Who approves an issue and what is checked before it goes out. Keep it short: only what can stop a post.

## Posts
| # | Post | Role | Published |
|---|---|---|---|
| 01 | [title](posts/01-slug.md) | | YYYY-MM-DD |

## Commitments
Promises made in published posts ("we will confirm when…", "every month from now on") and how each was closed.

| Made in | Commitment | Closed in | How |
|---|---|---|---|

## Status
Active, paused or finished. Planned next steps and open items.
