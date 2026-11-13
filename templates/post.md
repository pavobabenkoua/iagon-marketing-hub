---
id: post-<series-slug>-<NN | YYYY-MM | slug>
title: <Short title of the post>
type: post
status: draft                  # approved once published
owner: Pavlo Babenko
updated: YYYY-MM-DD
visibility: team
series: series-<series-slug>   # leave empty for a post outside series
position: <NN>                 # thematic with arc only: place in the arc
period: <YYYY-MM>              # recurring only: the period the issue covers
publications:                  # one entry per channel; evergreen posts add one entry per run
  - channel: x                 # x | linkedin | discord | telegram | blog | youtube | other
    date: YYYY-MM-DD
    url: https://...
sources: []                    # recurring: the raw data and the inputs file
related: []
tags: []
---

<!--
File name (decision 0012):
  thematic with arc:  posts/NN-slug.md
  thematic, no arc:   posts/YYYY-MM-DD-slug.md
  recurring:          posts/YYYY-MM-slug.md
  evergreen:          posts/slug.md (one file, publications grow with every run)
  outside series:     wiki/posts/YYYY-MM-DD-slug.md
Keep the sections for the type and delete the rest. No images in the repo: the publication links are the record.
-->

# <Title>

## Summary
What the post said, in one or two sentences.

## Role in the arc
_Thematic with arc only._ What this post does in the arc: opens, deepens, proves, or calls to action.
- **Builds on:** which earlier post or idea it relies on.
- **Sets up:** what it prepares for the next post.

## Hook and angle
_Thematic and outside series._ The hook used and why this angle was chosen.

## Inputs and numbers
_Recurring only._ Link the raw data and the inputs file. The numbers the issue showed.

## As published
The text exactly as it went out, one block per channel. Write "Same as X" if identical.

### X
```
```

## Results
Recorded 7 days after publication. Source of the numbers in the last column.

| Channel | Impressions | Engagements | Reposts | Replies | Clicks | Source |
|---|---|---|---|---|---|---|
| X | | | | | | |

What the numbers mean, in one line.

## Commitments
Promises this post made, or closed. Also listed in the series' Commitments table.

## Learning
One takeaway. If it repeats in a later post, it moves to the series' `learnings.md`, then to its rules.
