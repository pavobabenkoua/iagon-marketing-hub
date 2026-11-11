---
id: campaign-2026-insight-x-ads
title: Iagon Insight X Ads test
type: campaign
status: draft
owner: Pavlo Babenko
updated: 2026-11-11
reviewed: 2026-11-03
visibility: team
start: 2026-10-27
end: 2026-11-01
channels: [x]
sources: [raw/archive/2026-11-11-claude-project-iagon-sources.md]
related: [product-insight]
tags: [insight, paid, x-ads, test]
---

# Iagon Insight X Ads test

Merged from three project docs: the campaign brief (2026-10-14, updated 2026-10-22), the Round 1 approval doc (2026-10-22) and the Round 1 setup and results log (2026-10-27, updated 2026-11-03). Product facts live in [Iagon Insight](../../products/insight/product-brief.md).

## Objective

- **Test campaign, round 1.** Find which product message gives the cheapest sign-up. Scale only the winners.
- **Target:** sign-ups and product testing. At least 100 users in about two weeks.
- **Main metric:** cost per confirmed sign-up. CTR is secondary. Likes don't count.
- The test answers two questions: which feature pulls developers in, and does the opener "Building on Cardano?" beat leading with the feature.

## Audience

People who already build on Cardano: dApp, wallet, DeFi and tooling developers. Teams that call Blockfrost or Koios today or use the MeshJS SDK. Not cold crypto audiences and not holders. Talk as one developer to another: code on the image, one concrete feature per ad, no explaining what Cardano is.

Excluded: broad crypto interests (ADA, trading, investing). Those people hold tokens, they don't sign up to test an API. Language: English.

## Message

Five messages, each one reason a developer might switch. Each rests on a fact from our docs or a public source.

| # | Message | Card title | Visual | Proof |
|---|---|---|---|---|
| 1 | Officially in MeshJS | Built into Mesh. | import of `IagonInsightProvider` | Official provider page on meshjs.dev. Also outside proof: another team chose to list us |
| 2 | All Cardano data through one API | Cardano data through one API. | JSON response, as on the landing | Addresses, UTxOs, assets, transactions, staking, pools, governance. No node, no indexer. Tests whether the plain pitch is enough |
| 3 | Blockfrost and Koios compatibility | Switch, don't rewrite. | base URL diff | Same paths and responses, only base URL and key change. Also speaks to teams that relied on Maestro |
| 4 | One key for everything | One key. Three APIs. | network tabs | `/api/v0`, `/koios/v1`, `/v1`; mainnet and preprod. Tests whether convenience sells |
| 5 | Read, evaluate, submit in one place | Read. Evaluate. Submit. | fetch → evaluate → submit | Submit and evaluate on the same key; evaluate sees up to 10 unconfirmed transactions. Tests whether builders respond to depth |

Rejected: "Your wallet never shows zero because of a timeout" (didn't land).

**Card headline (same on every ad, 44 characters):** `Iagon Insight: Cardano data through one API`

### Ad texts (as run)

Two texts per message. **A** opens with "Building on Cardano?", **B** opens with the feature. Summing all A against all B shows whether the opener helps.

| # | A | B |
|---|---|---|
| 1 | Building on Cardano with MeshJS? Iagon Insight is now an official Mesh provider. One import gives you chain data, script evaluation and transaction submission. | Iagon Insight is now built into Mesh. Fetch UTxOs, evaluate scripts and submit transactions through one provider, straight from the Mesh SDK. |
| 2 | Building on Cardano? Query addresses, UTxOs, assets, transactions, staking and governance through one API. Clean JSON, no node or indexer to run. | You shouldn't need your own node and indexer just to read the chain. Iagon Insight serves the Cardano data your app needs through one API. |
| 3 | Building on Cardano with Blockfrost or Koios calls? They already work on Iagon Insight. Change the base URL and the key. Keep your code. | Changing your Cardano data provider shouldn't mean a rewrite. Iagon Insight answers the Blockfrost and Koios calls your app already makes. |
| 4 | Building on Cardano? One Iagon Insight key covers Blockfrost-style, Koios-style and native endpoints, on mainnet and preprod. | One key. Three APIs. Two networks. Iagon Insight keeps your Cardano stack on a single credential, from preprod tests to mainnet. |
| 5 | Building on Cardano? Read the chain, evaluate Plutus scripts and submit transactions, all with one Iagon Insight key. | Evaluate a transaction that spends outputs not on chain yet. With Iagon Insight you can chain transactions without waiting for a block. |

Mesh B was edited before launch: `@meshsdk/provider` was removed from the text, because X turns it into an @meshsdk tag.

## Channels

X Ads only. Website card created in X Ads Manager (promoted-only, doesn't appear in the account feed). Every ad links to `https://insight.iagon.com`.

## Budget

Approved request: $1,000 from the existing X ads balance (plan: $500 static days 1–4, $350 winners days 6–10, $150 reserve). Actual spend: see Results. Budget details belong in `_private/`.

## Setup

- **Objective:** Website traffic, optimization "Link clicks", pay by link clicks (CPC). Pay-by can't be changed after launch. Manual mode, Grok creatives off.
- **Campaign:** `insight_test_r1` (ID 42869298). 5 ad groups = 5 messages (`r1_mesh`, `r1_onedata`, `r1_switch`, `r1_onekey`, `r1_submit`), 2 ads (A/B) in each, 1:1 images only.
- **Group budget:** $25/day, total spend cap $100. Max bid $3 (CPC).
- **Placements:** Home timeline, Profiles, Search results. Replies limited to "Only accounts you mention".
- **Optimize targeting:** OFF.
- **Follower look-alikes:** @meshsdk, @blockfrost_io, @CardanoKoios, @txpipe_tools, @DemeterRun, @IntersectMBO, @AnastasiaLabs.
- **Geo after the 29.10 change:** US, CA, UK, DE, NL, CH, FR, ES, PT, IT, PL, CZ, UA, SE, NO, DK, FI, AU, JP. Language English. Age 18+.
- **UTM:** `utm_source=x&utm_medium=paid&utm_campaign=insight_test_r1&utm_content=<message>_<a|b>`.
- **Creatives:** 5 static cards 1200×1200 PNG (`insight-x-r1-1-mesh` … `-5-submit`): dark background, Insight logo + BETA, title, subtitle, feature code, blue "Test Insight Now" button (`#5786FF`), `insight.iagon.com`. 8-second 1:1 video loops of the same cards were prepared for round 2.

### X Website card specs (X Business help, checked 2026-10-22)

| | Static | Video |
|---|---|---|
| Ratio | 1.91:1 or 1:1 | 16:9 or 1:1 |
| Size | 1200×628 or 1200×1200 | 1920×1080 or 1200×1200 |
| File | PNG / JPEG, up to 5 MB | MP4 / MOV, recommended up to 15 s |
| Card headline | up to 70 characters, best under 50 | same |

Main format: 1:1. On mobile the square takes about twice the height of 1.91:1, and X's audience is mostly mobile.

## Test rounds

| Round | Dates | What we tested | Result | Decision |
|---|---|---|---|---|
| R1 | 2026-10-27 → 2026-11-01 | 5 messages × A/B texts, static 1:1, look-alikes | $504.06 spent, 19,931 clicks, 1 sign-up (possibly not from the campaign). Target of 100 sign-ups missed | Don't continue X Ads with this setup. Move the remaining ~$500 to intent channels |

### What happened, in order

1. **27–29.10, no delivery.** After launch all 5 groups were Active and approved, but in about two days they gave 3 impressions and $0. Max bid $3 and cutting exclusions to 4 words didn't help. Control group `r1_control` (US only, no handles, no keywords, $5): about 3,200 impressions, 8–9 clicks, CTR 0.25%, CPM $1.5, CPC $0.6, so the account and payment were fine. Diagnosis on 29.10: a group with **handles only** started delivering at once. A group with **4 keywords only** (MeshJS, Blockfrost, Koios API, Mesh SDK) got 0 impressions.
2. **29.10, first run on handles, all countries** (about 16:30–19:00 Kyiv). $80.56 total, 2,596 clicks ($5 of it the control group). CPC about $0.03–0.05, CPM about $0.10–0.13, CTR 0.26–0.30%, the same in every group: the messages didn't differentiate. About 87% of clicks and 86% of spend went to 9 cheap countries: Brazil, Indonesia (together about half the budget), India, Philippines, Turkey, Nigeria, Kenya, Vietnam, Ethiopia. Age 13–17: 53K impressions, 169 clicks (age was set to All).
3. **29.10 evening, changes in all 5 groups:** removed BR, ID, IN, PH, TR, NG, KE, VN, ET. Age 18+. Bid and budgets unchanged.
4. **26.10–01.11 totals (campaign paused, groups hit their caps):** $504.06, 4.84M impressions, reach 2.2M, frequency 2.19, 19,931 clicks, CTR 0.41%, CPC $0.025, CPM $0.10. After the 29.10 geo change: about $423.5 and about 17,335 clicks. Western countries about $219 (FR, GB, DE, NL, SE, JP), Southern and Eastern Europe about $217 (ES, UA, PL, IT, PT, CZ). US about $1 from look-alikes (plus $5 control), CA $4, AU $1. Platforms: iOS 90% of budget (CTR 0.46%), Android 9%, desktop web 0.5% (115 clicks, CTR 0.09%). Age 18–24: 47% of budget. 39% of impressions were women. The profile matches X's general mobile audience, not developers.

## Results

- **$504, about 19.9K clicks, 1 sign-up.** The 100 sign-up target was not reached.
- The funnel was checked by hand on 03.11: ad → X in-app browser → email sign-up + code works. **The main cause is the audience, not the site.**
- X counts a click at the moment of the tap and opens links in its in-app browser, so click counts overstate real visits.
- **There is no tracking on the site.** We only see the fact of sign-ups. Real visits can be recovered from server/CDN logs (requests with `utm_campaign=insight_test_r1` for 29.10–01.11).

## Learnings

**About X Ads in this ad account**
1. Keyword targeting blocks delivery.
2. X follower look-alikes drift into the cheapest inventory, not to developers (2.2M reach, iOS 90%, desktop 0.5%).
3. Slovakia (SK) is closed for the Iagon ad account.
4. Don't use handles with a mass holder audience: @Cardano, @Cardano_CF, @IOGroup, @emurgo_io, @Catalyst_onX, @lace_io, @eternlwallet, @cardanoscanio, @cexplorer_io, @CardanoIndia.
5. If X fixes keywords: "Mesh SDK", MeshJS, meshsdk, Blockfrost, Ogmios, cardano-cli, PlutusTx, aiken-lang, "Koios API". Avoid ambiguous words (Plutus, Aiken, UTxO, "Lucid Evolution") and exclusions on common words (price, trading, moon, signals, pump).

**Rules for the future**
- **Never launch paid traffic without minimum tracking:** an analytics script on the site + UTM stored in the profile at sign-up (+ X pixel when possible).
- Small funnel fix: `autocomplete="one-time-code"` on the code field.
- No `@` before package names in ad texts.

**Content rules from the brief**
- No prices, credits or purchase in ads: payments aren't integrated.
- Never claim competitors shut down. No price comparisons with Blockfrost, Koios, Maestro.
- No tokens and no profit promises (X crypto ad rules).
- Preview network only after it's in the docs.
- MeshJS: don't say the provider works on preprod or preview while the Mesh page says "mainnet". Import only from `@meshsdk/provider`.

## Next steps

- Move the remaining ~$500 to intent channels: co-marketing with Mesh, search ads ("Cardano API", "Blockfrost alternative", "Koios API", "Cardano indexer"), developer communities, organic technical posts on X + retargeting people who engaged, direct work with teams.
- Send the X support request about keyword targeting. If fixed, a small $100 test is possible: desktop only + keywords.
