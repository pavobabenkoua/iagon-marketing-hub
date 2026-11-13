---
id: decision-0012
title: Post history
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-13
updated: 2026-11-13
amends: decision-0008
---

# 0012: Post history

## Context
The post template was built for a series told in acts. It had no place for a recurring issue's inputs, for channels beyond X and LinkedIn, or for a reusable post that goes out many times. The first recurring post didn't fit it.

## Decision

### 1. File names by type

| Type | File | Example |
|---|---|---|
| Thematic with arc | `posts/NN-slug.md` | `03-print-is-not-an-event.md` |
| Thematic without arc | `posts/YYYY-MM-DD-slug.md` | `2026-11-20-slug.md` |
| Recurring | `posts/YYYY-MM-slug.md`, by the period it covers | `2026-10-monthly-recap.md` |
| Evergreen | `posts/slug.md`, one file for every run | `discord-invite.md` |
| Outside series | `wiki/posts/YYYY-MM-DD-slug.md` | `2026-08-03-windows-node-release.md` |

A post's ID never changes when its file is renamed ([0003](0003-metadata-standard.md)).

### 2. Evergreen: one file, many publications
A reusable post has one file. Each run adds an entry to `publications`, so the last run and the rotation are visible.

### 3. Texts as published
Every post keeps its text exactly as it went out, one block per channel. Recurring posts too: the issue templates change over time, and the history must not depend on today's templates.

### 4. No images in the repo
Published images are not stored in git. The publication links are the record; images are taken from the posts when needed. Recurring cards can also be rebuilt exactly from git: raw data, inputs, layout and script at the commit of the issue.

### 5. Sections by type
All posts: summary, as published, results, commitments, learning. Thematic with arc: role in the arc, builds on and sets up. Thematic and outside series: hook and angle. Recurring: inputs and numbers.

### 6. Results after 7 days
Per channel: impressions, engagements, reposts, replies, clicks, with the source of the numbers. A learning that repeats goes to the series' `learnings.md`, then to its rules ([0010](0010-series-rules.md)).

### 7. When a post enters the hub
When it is published, with status `approved` ([AGENTS.md](../AGENTS.md)). Drafts stay in the chat or on the canvas.

## Consequences
- `templates/post.md` rewritten with the fields `period` and sections by type.
- The October 2026 recap moves to `posts/2026-10-monthly-recap.md`; its ID `post-development-update-01` stays.
