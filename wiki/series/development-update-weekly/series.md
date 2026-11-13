---
id: series-development-update-weekly
title: Development Update Weekly
type: series
status: approved
owner: Pavlo Babenko
updated: 2026-11-13
visibility: team
summary: Every Monday, an overview of what the development team worked on the week before, for the community.
series_type: recurring
narrative: "05"
cadence: weekly
state: planned
channels: [discord, telegram]
related: [series-development-update, brand-format-weekly-cover, decision-0013, channel-discord, channel-telegram]
tags: [development, proof, recurring]
---

# Development Update Weekly

## Idea
Every Monday, a short overview of what the team worked on the week before. Its sibling, the [Monthly Recap](../development-update/series.md), shows the shape of the month to a wider audience.

## Goal
Show the community that work moves every week, in the open. The weekly run is the habit that makes the monthly numbers believable.

## Narrative and boundary
- **Narrative:** 05, The Proof File: continuous, small, dated.
- **Never becomes:** a roadmap, an announcement or a promise. It reports the week that ended.

## Audience
The community, node operators, IAG holders.

## Format
- **Visual:** one cover, the same every week except the week number. [Format page](../../brand/visual/formats/weekly-cover.md), template in `layouts/weekly-cover/`.
- **Text:** an overview of the week, no blocks by area.
- **Channels:** Discord and Telegram, the same text. Channel rules: [Discord](../../channels/discord.md), [Telegram](../../channels/telegram.md).

## Cadence
Every Monday, about the ISO week that ended the day before.

## Data source and build
- **Source:** the development dashboard, week view. Copy three things as they are: the week line, the counts line and the marketing statements. Save as `raw/archive/YYYY-MM-DD-dev-statements-YYYY-Www.txt` (publication date first).
- **Build:** `python3 scripts/weekly-update.py --input <that file>`. It checks that the week number matches the dates, fills the cover and writes the texts for Telegram and Discord.
- No inputs file: every statement goes in, in the dashboard's order.

## Issue structure
The wording lives in [`issue/`](issue/README.md): [Telegram](issue/telegram.txt), [Discord](issue/discord.txt). Title with the week number, the number of changes, the statements, thanks to the community. No closing announcement, no question: it is a regular information post.

## Rules
- **The week as a number, not dates:** "Week 44, 2026", on the cover and in the title. The point is what the team did; the period is secondary, and a date range pulls attention from it (director, 2026-11-13).
- **Statements word for word.** They are already written for the outside by the team; rewriting them would make two versions of the same fact.
- **"What we worked on", not "what shipped",** above the statements. Some statements describe ongoing work ("Ongoing development of…"); calling them shipped would be untrue.
- **Only the number of changes,** not topics. "Topics" is how the dashboard groups work; a reader can't use it.

## Approval
- The director approves each issue in the chat before it goes out.
- What stops a post: a statement that shows how our defence works, or a week whose numbers don't match the dashboard.

## Posts
| Period | Post | Published |
|---|---|---|

## Commitments
| Made in | Commitment | Closed in | How |
|---|---|---|---|

## Status
Planned. First issue: Monday 16 November 2026, about 9 to 15 November.

Open:
- Week 44 in the dashboard shows 94 changes and 15 topics; the October export holds 46 changes and 8 topics for the same week. Find out why before weekly and monthly numbers are compared.
- Automate the dashboard copy later.
