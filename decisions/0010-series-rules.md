---
id: decision-0010
title: Series rules
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-13
updated: 2026-11-13
amends: decision-0008
---

# 0010: Series rules

## Context
The first series page collected everything it needed: channel limits, markup rules, colour rules, partner constraints. Each new series would do the same, and the copies would drift apart. The design system and the rules have to stay one set.

## Decision
1. **A series keeps only its own rules.** Rules that follow from the series' subject stay in `series.md`. Everything else lives once, in its own place, and the series links to it:

   | Rules about | Live in |
   |---|---|
   | Voice, colours, type | `wiki/brand/` |
   | A visual | its format page and `layouts/` ([0007](0007-approved-layouts-live-as-html.md)) |
   | A channel: limits, markup, communication approach, audience | `wiki/channels/` |
   | Numbers and claims | `wiki/data/`, Proof Library |
   | A partner or project | `wiki/partners/` |

   If a rule applies beyond one series, it moves to its place. Pages that don't exist yet are created as drafts and filled later.

2. **Every rule comes with its reason.** One line for the rule, then why. A rule without a reason gets broken or argued again.

3. **Approval is light.** Every series has an Approval section: who approves an issue and what is checked. Only what can actually stop a post.

4. **How rules change.**
   - Rules, cadence, boundary or format: a logic change, on a branch, approved by the director.
   - New posts, results, learnings: log additions.
   - A learning that repeats moves from `learnings.md` into the rules, with its date.

## Consequences
- `templates/series.md` gets the link table and the Approval section. `templates/channel.md` gets Communication approach and Formats and limits.
- New draft pages `wiki/channels/x.md`, `discord.md`, `telegram.md` take the channel rules from Development Update.
- Würth: content about the project needs no partner approval (director, 2026-11-13). Updated in the partner pipeline.
