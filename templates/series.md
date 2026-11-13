---
id: series-<slug>
title: <Series name>
type: series
status: draft
owner: Pavlo Babenko
updated: YYYY-MM-DD
visibility: team
series_type: <recurring | thematic | evergreen>   # decision 0008
arc: <true | false>                             # thematic only; delete for other types
cadence: <weekly | every two weeks | monthly | …>
channels: [x, linkedin]
related: []
tags: []
---

<!--
Keep the sections for your type and delete the rest (decision 0008):
  all types:   Idea, Goal, Narrative and boundary, Audience, Format, Cadence, Rules, Posts, Commitments, Status
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
_Recurring only._ Where the data comes from, where inputs are saved, the command that builds an issue, what it checks.

## Issue structure
_Recurring only._ The fixed parts of every issue: opener, block structure, close. Exact wording.

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
What every post in the series must and must not do. Only rules that follow from this series' subject, channel or audience. A rule that applies more widely goes to `wiki/brand/`.

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
