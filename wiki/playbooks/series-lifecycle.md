---
id: playbook-series-lifecycle
title: How we run a content series
type: playbook
status: draft
owner: Pavlo Babenko
updated: 2026-11-13
visibility: team
related: [decision-0007, decision-0008, decision-0009, decision-0010, decision-0011, decision-0012, series-development-update]
tags: [series, process]
---

# How we run a content series

From an idea to a series that closes. The rules behind each step are in decisions [0007](../../decisions/0007-approved-layouts-live-as-html.md)–[0012](../../decisions/0012-post-history.md); this page is the order to apply them in.

The director approves in the chat. Every change goes on a branch and is merged after approval ([0002](../../decisions/0002-chat-approval-and-auto-merge.md)).

## When to use
- You have an idea for posts that will repeat: same subject, same data or same purpose.
- You prepare an issue of an existing series.
- It's the quarterly review.

A single post that won't repeat is not a series: it goes to `wiki/posts/`.

## Steps

### A. Start a series

1. **Check the registry** in [`wiki/series/README.md`](../series/README.md). If a series already covers the same narrative and audience, the idea is an issue of that series. Stop here.
2. **Pick the type** ([0008](../../decisions/0008-series-types.md)):
   - `recurring`: a regular issue built from data, only the data changes;
   - `thematic`: one theme, every post written from scratch; `arc: true` if the order of posts matters;
   - `evergreen`: a set of reusable posts on rotation.
3. **Write `series.md`** from `templates/series.md` in `wiki/series/<slug>/`. Fill the frontmatter (`summary`, `series_type`, `narrative`, `cadence`, `channels`) with `state: planned`. Keep only the sections for the type. Rules: only the series' own, each with its reason; everything else is a link ([0010](../../decisions/0010-series-rules.md)).
4. **Run** `python3 scripts/series-registry.py`. The series appears in the registry as planned.
5. **Design the visual** on a canvas. Once approved, move it to `layouts/<format>/` with a format page in `wiki/brand/visual/formats/` ([0007](../../decisions/0007-approved-layouts-live-as-html.md)).
6. **Recurring only:** put the fixed wording in `issue/`, one file per channel, and the build script in `scripts/` ([0011](../../decisions/0011-series-files.md)).
7. **Get the series approved** in the chat. Merge.

### B. Publish an issue

**Recurring**
1. Save the raw data to `raw/archive/YYYY-MM-DD-<name>`.
2. Write the editorial choice to `inputs/<period>.txt`.
3. Run the build script. It checks the numbers and that every line is in the source word for word.
4. Check the visuals where they will be seen (for X, the composer preview).
5. Approval in the chat, then publish.

**Thematic**
1. Read `series.md`, the previous posts and the lines already used.
2. Draft in the chat or on a canvas. Drafts don't enter the hub.
3. Approval in the chat, then publish.

**Evergreen**
1. Pick the next post from the set, respecting the minimum gap on that channel.
2. Publish.

**After publishing, every type**
1. Save the post page in `posts/` ([0012](../../decisions/0012-post-history.md)): texts as published per channel, links in `publications`. Evergreen: add a `publications` entry to the post's file.
2. Set the series to `state: active` after its first post.
3. Run `python3 scripts/series-registry.py`.
4. List any promise the post made in the series' Commitments table.
5. Merge.

### C. Seven days later
_Interim. The monitoring and review system is to be designed separately; until then, follow this._

Add the results to the post page, with their source. One learning per post. A learning that repeats moves to `learnings.md`, then to the rules.

### D. Quarterly review
_Interim, as C._

1. Run `python3 scripts/series-registry.py`. Every **overdue** series is paused with a reason in its Status section, or finished.
2. Move repeated learnings into rules.
3. Check that open commitments were closed.

### E. Pause or finish a series
Set `state: paused` or `state: finished`, write why in Status, run the registry script. A finished series stays in the hub: pages are never deleted.

## Checklist for an issue
- [ ] Raw data in `raw/archive/`, inputs in `inputs/` (recurring)
- [ ] Visual checked where it will be seen
- [ ] Approved in the chat
- [ ] Post page with texts as published and links
- [ ] Registry rebuilt
- [ ] Commitments listed
- [ ] Results added after 7 days

## Examples
- [Development Update | Monthly Recap](../series/development-update/series.md): recurring, the first series run this way. October 2026: [post](../series/development-update/posts/2026-10-monthly-recap.md).

## Common mistakes
- **A new series for what is an issue of an existing one.** Check the registry first.
- **Copying rules into the series.** Channel limits, colours and partner constraints live in their own pages; a copy drifts.
- **Typing numbers or lines by hand** in a recurring series. The script fills them and checks them.
- **Landscape images in a multi-image X post.** X crops the sides; see the channel page.
- **Letting a series go quiet.** Pause it with a reason instead.
