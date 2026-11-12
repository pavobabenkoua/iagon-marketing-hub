---
id: technology-docs-feedback
title: Docs feedback
type: technology
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/index.md
  - raw/docs-snapshots/2026-05-26/pages/overview/introduction.md
  - raw/docs-snapshots/2026-05-26/pages/blockchain/iagon-token/tokenomics.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/fees.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/iag-staking.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/compute-node/compute-fees.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/compute-node/compute-rewards.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-compute/compute-overview.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-compute/compute-subscription.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/high-level-architecture.md
  - raw/docs-snapshots/2026-05-26/pages/products/insight.md
  - raw/docs-snapshots/2026-05-26/pages/design-proof.md
  - raw/docs-snapshots/2026-05-26/pages/roadmap/roadmap.md
  - raw/docs-snapshots/2026-05-26/sidebar.ts.txt
related: [technology-overview, decision-0005, brand-vocabulary, brand-narrative]
tags: [technology, docs, feedback]
---

# Docs feedback

Problems found in docs.iagon.com, each with ready text for whoever has access to the docs repository. Snapshot 2026-05-26. Paths are relative to `documentation/docs/` in the docs repository. Links inside replacement text are docs-site paths and work only on docs.iagon.com.

How to use: send the open items to the docs owner as one batch. When a fix appears in a new snapshot, move the item to **Closed** with the snapshot date.

Priority: **P1** wrong or risky in public, **P2** contradicts the brand or another docs page, **P3** cleanup.

## Open

### Site level

**F1 · P2 · Category name in the site title**
`.vitepress/config.ts`, line 184: `Iagon Documentation | Storage & Compute Economy`
→ `Iagon Documentation | Shared Storage and Compute Economy`

**F2 · P3 · Copyright year**
`.vitepress/config.ts`, lines 156 and 377: `Copyright © 2024 Iagon Worldwide`
→ `` `Copyright © ${new Date().getFullYear()} Iagon Worldwide` `` (always current), or `Copyright © 2026 Iagon Worldwide`.

**F3 · P2 · "AI-driven" in the meta description**
`index.md` front matter and `.vitepress/config.ts` line 192: "Iagon's AI-driven storage and compute solutions". The brand does not lead with AI, and the docs describe no AI feature.
→ `Technical documentation for the Iagon protocol: decentralized storage and compute on Cardano, node operation, staking, tokenomics and APIs.`

**F4 · P2 · Brand Kit link**
`.vitepress/sidebar.ts`, lines 113–114 and 229: Brand Kit points to `https://iagon.com/brandAssets`. Check that this page serves the current approved logo files (8 SVG, on dark and on light, Purple Shade `#7C75FF`). If not, replace the files there or point the link to the approved set.

**F28 · P2 · Off-brand font on the home page**
`.vitepress/theme/custom.css`, around lines 2081 and 2091: `.home-hero-strong` and `.home-hero-light` use `"Poppins"`, weights 600 and 300. The brand has one typeface, Figtree, in weights 400 and 600 only.
→ `font-family: var(--vp-font-family-base);` in both rules, and `font-weight: 400;` instead of `300` in `.home-hero-light`.

### Introduction and home page

**F5 · P2 · Opening framing is from 2021**
`index.md` and `overview/introduction.md`, first paragraph: "Initially, our focus lies in creating a transparent storage marketplace, empowering providers to trade their surplus storage to consumers at fair prices…"
The brand now leads with enterprise focus. Proposed replacement:
> Iagon is the infrastructure behind the Shared Storage and Compute Economy: a network on Cardano where storage and compute come from independent providers, data is encrypted before it leaves the owner's device, and every commitment is recorded on-chain. Our focus is enterprise: organizations with the strictest requirements for their data. This documentation explains how the protocol works, how to run a node, and how to build on it.

**F6 · P2 · "In upcoming versions, we'll extend to compute"**
`overview/introduction.md`, What is Iagon, third paragraph. Insight already runs on Iagon Enterprise Compute ([products/insight.md](https://docs.iagon.com/products/insight)). Align with whatever F11 settles.

**F7 · P1 · Dated problem section**
`overview/introduction.md`, Problem Definition: AWS outage of December 2021, AWS outages "between July 2008 and January 2021", "$1.2 billion" in fines with no source, a March 2017 outage estimate. Footnote markers ("USD2") have no footnotes. Proposed: remove the section, or replace it with a short link to the current brand problem statement, so the docs do not carry unsourced statistics.

**F9 · P1 · Team allocation in future tense**
`blockchain/iagon-token/tokenomics.md`, Team: "This amount is ***locked until October 2025***, after which, it will be distributed over a 6-month period." The period has ended.
→ `This amount was locked until October 2025 and distributed over the following 6 months. 10,000,000 IAG from the unlocked Team allocation now funds the [Borrow Stake](/products/borrow-stake) pool.` (Docs team to confirm the distribution end date.)

**F10 · P1 · Legacy utility claims**
`blockchain/iagon-token/tokenomics.md`, IAG Token Utility Model: "services are priced against fiat currencies (e.g., NOK or EUR)… The payment in IAG will be facilitated at a later time" and "the IAG token is designed to be non-volatile and is not intended as a speculative financial instrument". Subscriptions are paid in ADA or stablecoins today, and "non-volatile" is a claim the project cannot guarantee. Also "stake their tokens in Adagio's ADA staking pool" mixes Adagio (rewards layer) with the IAGL ADA pools.
Proposed replacement for the list:
> - **Staking:** node operators and delegators lock IAG to activate storage capacity on the network. The required amount scales with committed storage and the IAG price.
> - **Rewards:** operators and delegators earn IAG from a 15-year emissions schedule, by node performance tier.
> - **Holder tiers:** holders of enough IAG value get Iagonauts storage tiers.
> - **Buyback:** 3% of subscription fees are used to buy back IAG on the open market.
> - **Governance:** (docs team to describe, or remove until the DAO launch).

**F11 · P2 · Compute rewards vs allocations**
`provide-resources/compute-node/compute-rewards.md` allocates 20,000,000 IAG to compute rewards. Tokenomics lists 20M for "Storage Provider Hives" ("more details will be unveiled soon") and 251M reserved for "future programs like decentralized compute". State which wallet and which line funds compute rewards, and update "Storage Provider Hives" (announced, never detailed).

### Network economics

**F12 · P2 · Fee split wording**
`provide-resources/storage-nodes/fees.md`: "7% of the remaining fees go to the Iagon treasury and 3% are used to buyback". Read literally, 7% of the remaining 10%.
→ `The remaining 10% is split: 7% of total fees go to the Iagon treasury and 3% are used to buy back IAG tokens on the open market.`

**F13 · P2 · Empty-tier rule contradicts itself**
`provide-resources/storage-nodes/iag-staking.md`: Empty-Tier Redistribution says an empty tier's pot is "passed down to the next tier". The FAQ says it is "redistributed proportionally to the occupied tiers based on their factor weights". Keep one. If the pass-down rule is current:
→ FAQ answer: `Its pot passes down to the next tier, together with any overflow it received from above.`

**F14 · P3 · Number formatting in the rewards table**
`provide-resources/storage-nodes/iag-staking.md`, year 9: `6,391529.571` → `6,391,529.57`. Years 10–15 use three decimals (`5,316,014.889`), years 1–8 two. Use two everywhere.

**F15 · P2 · APY caps not published**
`provide-resources/storage-nodes/iag-staking.md`, "Current APY Caps by Tier" has a heading and a note but no table. Add the table or remove the heading.

**F16 · P2 · LSPO "phases" still referenced**
`provide-resources/compute-node/compute-fees.md`: "as part of the Liquidity Providers Program's second phase". LSPO is now always-on ([overview/lspo.md](https://docs.iagon.com/overview/lspo)).
→ `…delegated to the IAGL1 stake pool for the [Liquidity Providers Rewards Program](/overview/lspo).`

**F17 · P3 · Fermato payment wording**
`iagon-storage/high-level-architecture.md`: Fermato collects "stablecoins for the subscription and ADA for transaction fees". `fermato.md`: users "pay in ADA or stablecoin". Align: `payment in ADA or stablecoins; network fees in ADA`.

### Compute

**F18 · P1 · Compute status is unclear**
`iagon-compute/compute-overview.md` says "Coming Soon" and "early stages". The roadmap lists "Decentralized Compute first iteration" as achieved, node CLI mainnet betas shipped in June–July 2024, and Insight is "powered by Iagon Enterprise Compute". Proposed status banner for the overview:
> Iagon Compute runs today as Iagon Enterprise Compute, which powers [Insight](/products/insight). Public compute for third-party apps is in development. The pages below describe the target design and may change.
(Docs team to confirm the facts before publishing.)

**F19 · P3 · Commented-out storage tables in the compute page**
`iagon-compute/compute-subscription.md` contains a long commented-out copy of the storage tiers. Remove it. Add currency and period to the compute price formula.

### Products

**F20 · P2 · Insight page is behind the product**
`products/insight.md`: governance, evaluate and Blockfrost/Koios compatibility are missing, and the access wording predates the current model. Text to follow from the Insight product brief (block: Insight migration).

**F22 · P3 · Products named only in Terminology**
`overview/terminology.md` defines Transfer, HealthSafe, Fantasy Brawl and Network Explorer, which have no pages. Mark each as live, planned or retired, or remove the entries.

### Hidden pages and leftovers

**F23 · P2 · Design proof page is public**
`design-proof.md` (lorem ipsum style test, `search: false`) is published at `/design-proof`. Exclude it from the build (`srcExclude` in the VitePress config) or move it out of `docs/`.

**F24 · P3 · Empty file**
`catalyst/wurth` is a 1-byte file. Remove it.

**F25 · P2 · Roadmap page**
`roadmap/roadmap.md` is not in the navigation, undated and partly outdated ("Decentralized AI Alexandria Protocol", "Fluxion"). Either date and refresh it and add it to the navigation, or remove it.

**F26 · P2 · Audit report not linked**
`Iagon-Staking-Contract-audit.pdf` (FYEO, November 2023) sits in the root of `docs/` with no link from any page. VitePress serves static files from `docs/public/`, so the file is probably not reachable. Move it to `docs/public/` and link it from `blockchain/on-chain-activity.md` under a new heading:
> ## Audits
> - Staking contract: security assessment by FYEO Inc., November 2023. [Report (PDF)](/Iagon-Staking-Contract-audit.pdf)

**F27 · P3 · Developers Guide placeholder**
`developers/developers-guide/developers-guide-overview.md` says "Page under development". Fill it or remove it from the build.

## Closed

| Item | Closed | Resolution |
|---|---|---|
| F8 · "Zero cookies policy" claim in the introduction | 2026-11-12 | Confirmed true by the director. No change needed |
| F21 · Partner name in public Insight URLs (`docs.fireblocks.partners.iagon.com`) | 2026-11-12 | Use of the name confirmed as cleared by the director. No change needed |
