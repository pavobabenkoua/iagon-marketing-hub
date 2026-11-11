---
id: product-insight
title: Iagon Insight
type: product
status: draft
owner: Pavlo Babenko
updated: 2026-11-11
reviewed: 2026-10-14
visibility: team
sources: [raw/archive/2026-11-11-claude-project-iagon-sources.md, res-insight-landing, res-insight-api-docs, res-insight-logo-svg]
related: [campaign-2026-insight-x-ads]
tags: [insight, api, cardano, beta]
---

# Iagon Insight

Reference for posts, decks and pitches. Collected on 2026-10-14 from the landing page insight.iagon.com (including FAQ), the API docs (insight.iagon.com/docs/api), the Insight page in the Iagon docs (docs.iagon.com), the promo page and public sources. Numbers and prices are as of that date, during Beta. Later updates from the X Ads campaign (2026-10-22) are marked **[update]**.

## What it is

**Iagon Insight is a hosted API for Cardano data.** Addresses, balances, UTxOs, assets, transactions, staking, pools and governance come back as clean JSON. No need to run your own node or indexer. Signed transactions can be submitted to the network through the same API.

Main argument: Insight answers the same requests as Blockfrost and Koios. To switch, change the base URL and the key. No code rewrite.

**One-liner:** Cardano data through one API. Your Blockfrost and Koios calls already work.

## Status and context

- **Stage:** Beta is live. Access currently goes through a raffle: users win credits and test the product. No open purchase of packages yet. Prices on the landing page are the post-Beta plan.
- **How to join the Beta:** leave an email on the promo page and confirm it. Each round: 50 winners get 3M credits each for 30 days. Those who don't win stay in the pool for next rounds. Projects and companies can ask for a high-volume voucher.
- **Beta goal:** real users test the API on their own tasks before the open launch.
- **Timeline:** on 2026-07-26 Iagon announced that Insight would open to all builders in about six weeks. Before that, enterprise partners used it.
- **Fireblocks:** Fireblocks connected its RAW signing to Iagon enterprise nodes and the Insight API. Fireblocks clients can delegate ADA to pools and take part in Cardano governance directly from Fireblocks. Available to approved Fireblocks clients. In Fireblocks' open SDK (cardano-raw-sdk) an Iagon API key is required for balances, transaction history and transfers.
- **MeshJS:** on 2026-10-01 a PR with `IagonInsightProvider` was opened in MeshJS/providers, plus a provider page on meshjs.dev. **[update]** Insight is now an official Mesh provider: the page is [meshjs.dev/providers/iagon-insight](https://meshjs.dev/providers/iagon-insight), PR merged on 2026-10-14. One provider covers all four Mesh interfaces: fetcher, submitter, evaluator, listener. The Mesh page currently says "The provider serves Cardano mainnet". The same class is also on npm as `@iagon/insight-mesh` (Apache-2.0).
- **Link to Iagon:** Insight runs on **Iagon Enterprise Compute**, Iagon's decentralized compute layer. Iagon handles sync, availability and all operations.
- **Place in the Iagon lineup:** the docs list Insight among products next to Staking Platform, Borrow Stake, Decentralized Web Hosting, Ecosystem Stats, Ledgerflow, Kliq, Statur, Volo and Cyclone. Iagon Storage and Iagon Compute are listed separately. Insight is the data layer other products can rely on.

### Two voices of one product

- **The landing page talks to developers:** "switch the base URL", prices in euros per credit, giveaway, code in the hero.
- **The Iagon docs talk to institutions:** banks, custodians, exchanges, institutional builders. Scenarios: custody workflows, treasury tools, analytics, staking products. Core message: enter Cardano without hiring people and running node clusters.

Both voices are true. Developer content takes the landing tone. Enterprise pitches and the Fireblocks story take the docs tone.

## Who it's for

| Audience | Pain | What Insight gives |
|---|---|---|
| dApp, wallet and DEX developers on Cardano | A node and indexer cost time, money and DevOps | Ready data over HTTPS, no own infrastructure |
| Teams on Blockfrost or Koios | Dependence on one provider, prices, limits | Switch in minutes: same request shape |
| Projects on MeshJS | Need a provider for fetch, evaluate, submit | One provider for everything |
| Banks, custodians, exchanges, treasury teams | A node means staff, clusters, audits; high entry barrier to Cardano | One versioned HTTP API, Iagon handles sync and availability. 25 keys with IP allowlist, team roles, Fireblocks case |
| Staking products and delegation services | Pool, reward and delegation data for reporting | Accounts, rewards, withdrawals, pools, delegators, blocks |
| Analysts, explorers, dashboards | Historical data, governance | UTxO state at any slot, DReps, votes, proposals |

## Three APIs in one

One key works on all three surfaces and both networks (mainnet and preprod).

| Path | What it is | Why |
|---|---|---|
| `/api/v0` | Blockfrost-compatible: same paths, parameters, responses | Move from Blockfrost without code changes. The key can be sent as `project_id`, as Blockfrost SDKs do |
| `/koios/v1` | Koios-compatible: GET and POST, including DReps, committee votes and proposals | Move from Koios without code changes |
| `/v1` | Insight's own API | The same data plus submit, evaluate and queries Blockfrost and Koios don't have |

Base URLs: `https://mainnet.insight.iagon.com` and `https://preprod.insight.iagon.com`.

**[update]** Preview network: according to the team it's been added. As of 2026-10-22 it is not on the landing page, in the API docs or on the Mesh page. Don't mention it until it's in the docs.

## Data coverage

- **Network:** service health, supply and stake, genesis parameters.
- **Blocks and epochs:** latest block, block by hash, height or slot, protocol parameters with Plutus cost models.
- **Addresses:** UTxOs, balances, full transaction history. Query by address, payment credential or stake address.
- **Assets:** metadata, mint and burn history, all holders of an asset, all assets of a policy.
- **Transactions:** full transaction, inputs and outputs, metadata, redeemers, delegation certificates, reward withdrawals, required signers, CBOR. Plus **submit** and **evaluate**.
- **Accounts:** rewards, delegation, active stake history, registrations, addresses, assets.
- **Pools:** list, retiring and retired pools, metadata, relays, delegators, blocks, per-epoch history, pool governance votes.
- **Governance:** proposals, DReps, their delegators and votes.
- **Scripts and datums:** script by hash (native as JSON, Plutus as CBOR), redeemers, UTxOs at a script address, where a script sits as a reference script, datum by hash.
- **Metadata:** transactions by label.

## Features to build content on

### Painless switch
1. **Drop-in replacement for Blockfrost and Koios.** New URL, new key, done. Strongest argument for anyone who has already built something.
2. **One key for three APIs and two networks.** No separate keys for mainnet and preprod.
3. **Preprod costs the same as mainnet** and counts toward the same daily limit. Each network has its own rate limit. **[update]** Don't use "Your tests never slow down production": the daily limit and credits are shared between networks.

### Technical depth (developers)
4. **Submit and evaluate on the same key.** Reading, script evaluation and submission in one place.
5. **Evaluate sees unconfirmed transactions.** Pass up to 200 UTxOs and up to 10 unconfirmed transactions. This allows transaction chaining without waiting for a block.
6. **`atSlot` "time machine".** UTxOs of an address, credential, stake key or script as of any past slot. For audits, reporting, taxes, debugging.
7. **All outputs of an address together with what spent them** (`/v1/outputs/address`). The full flow of funds in one request.
8. **Filter: only outputs with an inline datum.** For DeFi and smart contracts.
9. **Reference script lookup:** where a script lives, including already spent outputs.
10. **Token metadata from three sources:** CIP-68, CIP-25, Token Registry. Tries them in order by default.
11. **Lovelace as strings.** Large amounts don't get lost to JavaScript number limits.
12. **Honest errors.** In the MeshJS provider a failed request throws an error instead of returning an empty list. A wallet never shows zero because of a network failure.
13. **Retries on 429/503 automatically**, but never submits twice.

### Control and security (teams and enterprise)
14. **Up to 25 keys per account.** Each with its own limit, an IP allowlist of up to 32 entries and a list of sites.
15. **Limit shared between keys:** the whole limit, a share of 10–75%, or a fixed amount.
16. **Teams with roles:** the owner invites people and sets what each can do: keys, usage, credits, team.
17. **CORS is open,** but the docs advise against putting a key in the frontend. If needed: a separate key with a small limit and a site list.
18. **Credit balance headers** (`X-Credits-Charged`, `X-Credits-Remaining`) in every response.

### Infrastructure
- **Powered by Iagon Enterprise Compute.** The API runs on Iagon's decentralized compute layer, not on a rented cloud server. The bridge between Insight and Iagon's main story.
- **Iagon carries the operational load:** sync, availability, node updates. The client gets an endpoint and JSON.
- **One versioned API with a consistent response format** (`success`, `data`, structured errors). No sudden breaking changes.

### Money (post-Beta)
19. **Pay for credits, not a subscription.** Buy what you need, from 3M credits.
20. **Graduated pricing: the bill never jumps.** The cheaper rate applies only to credits in its band.
21. **95% of endpoints cost 1 credit.** About ten heavier ones cost more, and the dashboard shows the price before the request.
22. **Pay by card, USDC or ADA** (after Beta; now credits come only through the raffle).
23. **A human reads your message.** The contact form promises a real reply and deletion of the message after a year.

## Pricing and billing

> During Beta credits are not sold, they're won in the raffle. Below is the post-Beta model as shown on the landing page. Never promote prices or credit purchases while payments aren't integrated.

### Example monthly packages

| | Starter | Standard | Business |
|---|---|---|---|
| Price | €8.49 | €24.90 | €69.00 |
| Credits | 3,000,000 | 9,000,000 | 30,000,000 |
| Daily limit | 100,000 requests | 300,000 requests | 1,000,000 requests |
| Rate limit | 1,000 / 10 s | 1,000 / 10 s | 1,000 / 10 s |
| Average per 1M | €2.83 | €2.77 | €2.30 |
| Valid | 30 days | 30 days | 30 days |

Examples only. Any amount from 3M can be bought.

### Price bands

| Band | Credits per month | Per 1M |
|---|---|---|
| Starter | 0 – 3M | €2.83 |
| Standard | 3 – 9M | €2.735 |
| Business | 9 – 30M | €2.10 |
| Custom | over 30M | €1.90 and below, on request |

Example: 30M = 3M × €2.83 (€8.49) + 6M × €2.735 (€16.41) + 21M × €2.10 (€44.10) = €69.00.

### How it works
- Each purchase is valid for 30 days. Requests use the credits that expire first.
- Daily limit = credits on hand / 30, maximum 1M per day. Buy more and the limit grows.
- Evaluate costs 7 credits, one at a time per account.

### Beta promo
- **30 Day Beta Celebration Giveaway, round 3.** 50 winners get 3M credits each for 30 days. Draw on 2026-10-22 at 18:00. One entry per person, email confirmation required.
- Those who don't win stay in the pool for future rounds for up to 12 months.
- Separate high-volume vouchers for projects and companies on request.

## Limits and errors

- **429:** rate limit or daily limit reached. The response says how many seconds to wait. The daily limit resets at the new UTC day.
- **402:** out of credits.
- **403:** the key is restricted to other IPs or sites, or the account is paused.
- **422** on evaluate: the script failed, the message explains why.
- Pagination depth: up to 100,000 rows.

## Positioning and competitors

Main competitors: **Blockfrost**, **Koios**, **Maestro**. Insight doesn't force a choice: it speaks the language of the first two.

**[update, checked 2026-10-22]**
- Maestro: the site and docs show only Bitcoin products, the Cardano API is no longer mentioned. No official shutdown announcement found.
- Blockfrost: running, site says "We provide an instant and scalable Cardano API for free". No signs of shutdown.
- Never claim a competitor has shut down. Present compatibility positively.

Angles we can hold:
- **"Switch, don't rewrite."** Compatibility as the main advantage over any new API.
- **"One key, not a zoo."** Three surfaces, two networks, submit and evaluate on one key.
- **"Pay for what you use."** Credits instead of rigid plans, the price doesn't jump at thresholds.
- **"Infrastructure Fireblocks trusts."** Social proof for enterprise.
- **"Part of Iagon."** Data, storage and compute in one ecosystem.
- **"Cardano without a DevOps team."** For banks and exchanges: addresses, balances, history and submit through documented endpoints instead of own node clusters.
- **"Decentralized compute under the hood."** Insight as live proof that Iagon Enterprise Compute handles production load.

Careful: price comparisons with competitors are not verified. Check current Blockfrost, Koios and Maestro pricing before publishing any comparison.

## Landing page tone

Worth keeping the same voice in posts:
- Headlines are short statements with a period: "Cardano data through one API.", "Use the API you already know.", "Buy what you need.", "Questions.", "Talk to us."
- Plain words, concrete numbers, no hype, no empty adjectives.
- Explains mechanics honestly: what happens at the limit, what happens to your message.
- Dark theme, blue accent, a code snippet as the hero of the first screen.

## Content ideas

**Posts for X / LinkedIn**
- "Switch, don't rewrite." Show the diff: old Blockfrost base URL → new Insight one. Two lines.
- "Your wallet will never show zero because of a timeout." About honest errors.
- "Time travel for UTxOs." Explain `atSlot` with an audit example.
- "Chain transactions without waiting for a block." Evaluate with unconfirmed UTxOs.
- "One key. Three APIs. Two networks."
- "Your bill never jumps." Visual with graduated price steps.

**Beta content (while access is through the raffle)**
- Main CTA now is "Enter the draw", not "Get started" or "Buy". Never promise in posts that credits can be bought.
- Frame "testers, not buyers": "Help us test Cardano's new data API. 50 builders get 3M credits every round."
- Scarcity and rhythm: each round is an event with a date, a timer and a winners announcement.
- "You didn't lose, you're in the queue": the entry stays in the pool for next rounds.
- Tester stories after each round: what they built, which provider they moved from, how long the switch took.
- A separate message for teams: high-volume vouchers for projects and companies.

**Formats**
- Thread "5 things Insight does that your provider doesn't" (submit + evaluate on one key, `atSlot`, outputs with spent_by, inline datum filter, ref scripts).
- Tutorial "MeshJS + Insight in 3 minutes".
- Fireblocks case for the enterprise audience.
- Compatibility comparison table (after fact-checking).

## Logo

Official product logo as on insight.iagon.com (taken from the site code on 2026-10-14). SVG code: Claude Project doc `claude/iagon-insight-logo-svg.md` ([res-insight-logo-svg](../../resources.md)).

| Part | Dark background | Light background |
|---|---|---|
| Symbol | gradient `#5786FF` → `#885EFF` | same |
| Wordmark "iagon" | `#F2F2FA` | `#141A21` |
| Product name "insight" | `#5786FF` | `#5786FF` |

ViewBox 153×20, no extra margins. On the site the logo is 20–24 px high.

This logo differs from the general brandbook rules: the symbol is a blue → violet gradient and "insight" is blue `#5786FF`, while the brandbook sub-logo rule says purple `#6F47FF`. For Insight materials use the website version, because that's what product users see. Action color: interface blue `#5786FF`.

## Open questions for the team

- Full list of the "about ten heavier endpoints" and their prices.
- Terms of the Custom band over 30M credits.
- Beta end date and start of paid packages.
- SLA, uptime stats, number of nodes and regions: strong enterprise messages not on the landing page yet.
- Official name in partner materials: Fireblocks writes "Insights API", the product is "Insight".
- Can enterprise partners other than Fireblocks be named publicly?
- Release status of the provider in `@meshsdk/core`. **[update]** As of 2026-10-22, import only from `@meshsdk/provider` (from `1.9.0-beta.107`); `@meshsdk/core@1.9.1` doesn't include it yet.
- **Access wording in the docs.** docs.iagon.com says keys are issued to partners. Access now goes through the Beta raffle, so the docs should explain how a regular developer gets in and link the promo.
- How many more raffle rounds are planned and when credit purchase opens.
- Is there a feedback channel for beta testers (Discord, form)? It should be mentioned in every Beta post.
- Can Beta numbers be published (participants, requests, credits won)? Social proof.
- docs.iagon.com doesn't list all data groups: governance, scripts, datums, evaluate and Blockfrost/Koios compatibility are missing. Worth adding, they're the main arguments.
- The Iagon docs have a Japanese version. Is there a plan for the Japanese market for Insight?
- Can we share numbers on Iagon Enterprise Compute (nodes, geography, uptime) to back the "decentralized compute under the hood" message?

## Sources

- Landing: https://insight.iagon.com
- API docs: https://insight.iagon.com/docs/api
- Insight page in the Iagon docs: https://docs.iagon.com (Products → Insight)
- Promo: https://insight.iagon.com/promotions
- MeshJS provider PR: https://github.com/MeshJS/providers/pull/14
- Mesh provider page PR: https://github.com/MeshJS/meshjs.dev/pull/9
- Fireblocks × Iagon: https://blockonomi.com/fireblocks-connects-raw-signing-to-cardano-via-iagon/
- Fireblocks SDK: https://github.com/fireblocks/cardano-raw-sdk
- Opening announcement (2026-07-26): https://www.coingabbar.com/en/crypto-currency-news/cardano-news-iagon-api-opens-to-all-builders-soon-in-2026
