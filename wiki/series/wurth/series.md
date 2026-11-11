---
id: series-wurth
title: Würth × Iagon
type: series
status: draft
owner: Pavlo Babenko
updated: 2026-11-11
reviewed: 2026-10-22
visibility: team
channels: [x, linkedin]
sources: [raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [partner-iagon-wurth-project, brand-colors-typography]
tags: [enterprise, 3d-printing, ip, catalyst]
---

# Würth × Iagon

Post series about the enterprise pilot with Würth. Migrated from the series context doc of 2026-10-22. Project facts live in [Iagon & Würth Catalyst project](../../partners/catalyst/iagon-wurth-project.md). Check them before every post.

## Idea

Industrial 3D printing is moving from shipping boxes to sending files. The series shows what breaks when the file is the product, what Iagon built for it and who it is for.

## Goal

_To be defined in Phase 4._

## Audience

Enterprise and manufacturing decision makers. Token vocabulary (NFT, tokenized) only on Cardano channels, never for enterprise.

## Format

- X posts with a two-panel visual. LinkedIn long-form article where the thesis needs space.
- LinkedIn: the link goes in the first comment, not in the body.

### Visual system

Set with post 1, kept in posts 2 and 3.

- Title + subtitle top left, Iagon logo top right.
- Two panels: light `#F6F6FB` on the left, dark `#13181E` on the right.
- Under each panel: a purple eyebrow + the name of the state.
- Eyebrow pairs: `Today` / `Where it is going`, `Today` / `What it takes`.
- Purple `#6F47FF` on light, `#7E67FF` on dark. Only on the eyebrow and one accent.
- No dashed frames, no neon, no hexagon grids, no mascot.

Recurring render errors, check every time:
- Dashed guides from the mockup stay in the export.
- Panels come out with different visual weight (one side brighter or more styled).
- The element carrying the argument is smaller than the labels around it.
- The purple accent duplicates the logo color and reads as branding, not meaning.

## Narrative arc

| Act | Purpose | Posts | Status |
|---|---|---|---|
| I. What is broken | Market shift and the problem | 1, 1a, 2 | Closed. The planned "unlimited print problem" post was cancelled, absorbed by post 1 and the article |
| II. What we built | Architecture and control | — | Not started |
| III. Economics | Why it pays | 3 | Opened by post 3 |
| IV. Who it is for | Why industrial IP raised the bar for everyone | — | Not started |

**Act II plan**
- Architecture: encryption, sharding, IoT orchestrator, **deleting the file from the machine after printing** (the most concrete unused proof).
- Digital Passport: what is on chain and what is not.
- The IP owner sets the terms. The key word **before** is never cut.

**Act III plan**
- ~~Unit economics~~: done in post 3.
- Invisible blockchain: enterprise can't hold wallets, settlement is in fiat.
- Logistics reversal (needs a number with a source).
- Shared print shops.

**Outside the plan, strongest:** the 3D printer demo at Token2049, if it was filmed. A real part printed in front of people beats any argument.

## Rules

- One pillar per post, named before writing.
- Open with a gap, not a category. The category name comes second.
- Rule 06: at least one person in every text. In this series: the engineer opening the file, the IP owner setting terms, the manager going down the parts list.
- Every number has a date. Every external fact has an author and a year.
- Blockchain and Cardano never in the headline or the first paragraph. They appear as the answer to "why this way", and once.
- Token vocabulary (NFT, tokenized) only on Cardano channels, not for enterprise.
- Don't give up our own territory for rhetorical effect (the "encryption has been solved" story).
- The "not X, but Y" construction at most once per text. Twice already sounds like a device.
- End with the consequence for the client, not a description of the mechanism.
- Open ending instead of announcing the next post.
- LinkedIn: link in the first comment.
- American spelling: `license`, `catalog`, `specialized`.
- **Disclaimer on any graphic with numbers or proportions:** `Figures are illustrative. The point is the ratio, not the numbers.` or `Proportions are illustrative.` Bottom left, small, `#9EA3B8`. Best: build the graphic without numbers at all.
- **Don't state architecture specifics without checking with the tech lead.** Post 3 went through three graphic revisions because specific on-chain steps were drawn as fact before they were confirmed. The final wording `whatever shape that takes on-chain` removes the risk.
- **Check part examples for physical plausibility.** "Three-cent screw" is our internal name for the cost-threshold problem, fine for talks and the booth. But standard fasteners aren't 3D printed: stamping is cheaper and stronger. In public texts use what really comes out of a printer: a bracket, a housing, a spare part for a specific machine.

### Status of the pilot: how to talk about it publicly

- **Pilot / validation, not production.** Say "validating", "building", "working on". Never "secures its IP on our network" in the present tense.
- **Partner: Würth Canada within Würth Group.** Not "Würth Group" as a whole (€21B, 400+ companies).
- The pilot is public, naming the partner is legitimate. Co-branding and quotes from Würth staff need written approval.

### Forbidden topic

The closure of Würth Additive Group (Greenwood, Indiana, mid-2026) with names of executives. Keep the structural argument (hardware-heavy model vs software-centric), never publish the WAG story.

### Phrases already used (don't repeat word for word)

- "One file, unlimited prints"
- "Send the file, or ship the box" / "Most ship the box"
- "Control moves from the file to the contract"
- "Designs travel. Control stays." (Token2049 headline)
- "A record none of them owns"
- "Which parts are worth licensing / which parts are worth shipping"

## Posts

| # | Post | Channel | Role | Published |
|---|---|---|---|---|
| — | CEO visit to Würth Canada HQ | X + LinkedIn | Evidence of the relationship. Photo, "validating" wording, zero project details | 2026-07 |
| 01 | From freight to files | X | Market shift + problem. "One file, unlimited prints" | _date_ |
| 01a | Manufacturing is ready to send files. It still ships boxes. | LinkedIn article, ~750 words | Same thesis in depth. Mitskos quote. Section on contractual control | _date_ |
| 02 | The hard part is the record | X | Four parties, four versions of the truth. Why a record nobody owns is needed. First mention of blockchain, as the answer, not the topic | _date_ |
| 03 | A print is not a single event | X | Unit economics: cost of tracking vs cost of the part. Opens Act III | _date_ |
| — | Token2049 Singapore, booth + 3D printer demo | Offline | Slides: "In 3D printing, the file is the product", "Designs travel. Control stays.", "The hard part is the record" | 2026-10 |

Post pages (`posts/NN-slug.md`) come in Phase 4.

## Assets

**Quote from Dimitrios Mitskos** (Head of Systems & Solutions, Würth Canada; Project Manager Additive Manufacturing; Project Manager Würth ORSYconnect):

> "We are shipping 30,000 boxes in Germany right now. Hopefully in 5 to 7 years we'll be shipping 30,000 files a day to our customers."

Used in the LinkedIn article in shortened form ("and really staying ahead of our competition" removed). Approve the wording before every new use. Check the spelling of the name: Dimitrios Mitskos / Demetrios Mitzkos.

**Numbers without a source, don't publish:** EUR 8B additive manufacturing market, CAGR 18.2%, $10–100M DIS potential (Würth internal research, needs attribution and approval).

## Open questions

- For the tech lead: how many on-chain records per print, and are they aggregated? Needed for all of Act II.

## Status

Active. Next: Act II.
