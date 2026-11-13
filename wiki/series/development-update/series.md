---
id: series-development-update
title: Development Update
type: series
status: draft
owner: Pavlo Babenko
updated: 2026-11-13
visibility: team
channels: [x, discord, telegram]
sources: [raw/archive/2026-11-12-dev-changelog-2026-10.csv]
related: [brand-format-monthly-recap-cards]
tags: [development, proof, recurring]
---

# Development Update

## Idea
A regular record of what the team shipped. Weekly for the community, monthly as a recap for a wider audience.

## Goal
Show that development moves, steadily and in the open. The series carries Narrative 05, The Proof File: continuous, small, dated. It is a habit, not a campaign.

The series describes what was shipped, never what is planned. It never becomes a roadmap, an announcement or a pitch.

## Audience
Community, node operators, IAG holders. The monthly recap also reaches builders on Cardano who follow Insight and Mesh SDK.

## Format

The series has two formats with different jobs.

| | Weekly Update | Monthly Recap |
|---|---|---|
| Job | The record: every change, as it lands | The shape of the month: scale and direction |
| Channels | Discord | X, Discord, Telegram |
| Visual | to be defined | two square cards, [format page](../../brand/visual/formats/monthly-recap-cards.md) |
| Text | to be defined | grouped by area, 3–4 lines per area |
| Status | not finalised | approved 2026-11-13 |

Discord and Telegram are public. The series gets no extra freedom there because the audience is "ours".

### Monthly Recap

**Source.** The development dashboard export for the month, as CSV. Columns: `Week, Month, Area, Topic, Category, Group, Change`. A month is the set of ISO weeks the dashboard assigns to it, so it can start or end a few days outside the calendar month. Archive every export in `raw/archive/` as `YYYY-MM-DD-dev-changelog-YYYY-MM.csv`.

**Counts.**
- The total is every row of the export, `Preparing` topics included, exactly as the dashboard header shows it. No filtering, no deduplication.
- Card 2 shows the total by `Category`. The categories must add up to the total.
- The text shows no counts per area. A count above a few lines makes the reader ask where the rest is, and invites comparisons between areas that only reflect how finely tasks are logged.

**Grouping.** By `Area`, in order of number of changes, largest first. Area names exactly as in the export.

**Line selection.** 3–4 lines per area, copied from `Change` **character for character**. Never reword, merge, shorten or add punctuation. Prefer lines a reader can use or see (something live, a new feature) over internal ones. In security areas, take the lines that reveal least about how defence works. Before publishing, check every line against the export with an exact match.

**X thread.** One numbered tweet per area, plus an opener and an unnumbered close. X Premium removes the 280-character limit, but the first ~280 characters of each tweet are what the feed shows.

- Tweet 1, with both cards attached:
  ```
  Development Update | [Month YYYY]

  [Total] changes shipped across [N] areas.

  What shipped in each area, in the thread below ⬇️.

  🧵 1/[N+1]
  ```
- Area tweets: area name, blank line, lines as `- ` bullets, blank line, `🧵 [n]/[N+1]`.
- Closing tweet, no number:
  ```
  That was [Month].

  From here, a recap like this goes out every month. Weekly updates, with every change as it lands, go out in our Discord:
  https://discord.gg/TCS23VWuWm

  Thank you to the community. You move this ecosystem forward.

  What would you like to see in the next one?
  ```

**Telegram.** One message: same opener without the thread line, all areas with `**bold**` names, the close with the Discord link. No closing question unless comments are open in the channel.

**Discord.** Same text with `##` title, split into two messages after the fifth area so each stays under 2,000 characters. Cards attach to the first message. The close says "go out right here" instead of the link, and keeps the question.

## Narrative arc
The series has no arc. Each issue stands alone and is dated. Its value is the run of issues: one month is a claim, twelve months in a row are proof.

## Rules
- Shipped work only. Nothing planned, nothing promised with a date.
- Copy, never rewrite, the engineers' wording. Brand voice applies only to the frame: opener, close, card leads.
- No claim of completeness ("all changes", "every change"). The dashboard itself notes "Plus other development work" that is not logged.
- No changelog link. The weekly updates in Discord are the full record.
- Partners may be named: Würth is cleared (director, 2026-11-12).
- No em dashes. Colons and pipes instead.
- One 🧵 marker per numbered tweet. No other emoji, except the ⬇️ in the opener.
- Live network figures (nodes, capacity, earnings) are not part of this series. If they ever are, they carry "figures as of [D Month YYYY]" and follow `wiki/data/`.

## Posts
| # | Post | Role | Published |
|---|---|---|---|
| 01 | [October 2026 Monthly Recap](posts/01-october-2026-monthly-recap.md) | First issue of the Monthly Recap | 2026-11-12 |

The two bi-weekly updates of 1 and 14 September 2026 predate this format and are not part of the series record.

## Status
Monthly Recap: active, format approved 2026-11-13. Next issue: November 2026, first half of December.

Open:
- Weekly Update: visual and text format not defined yet.
- Card 2 lead says "Every change in [Month]", which conflicts with the no-completeness rule. Suggested: "All [Total] changes, by the kind of work each took." Decide before the November issue.
- Chip names on card 1 mix short and full area names ("Storage Node", "Admin Dashboard" next to "Iagon Platform"). Align with the export's `Area` names.
- "Insight API live on the Cardano preprod network" is logged under Iagon Infrastructure. Ask engineering whether preprod work should move to Insight API in the export.
- Owner of the monthly export and of publishing.
