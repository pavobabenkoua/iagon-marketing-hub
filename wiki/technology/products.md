---
id: technology-products
title: Products in the docs
type: technology
status: draft
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/products/insight.md
  - raw/docs-snapshots/2026-05-26/pages/products/ecosystem-stats.md
  - raw/docs-snapshots/2026-05-26/pages/products/staking-platform.md
  - raw/docs-snapshots/2026-05-26/pages/products/borrow-stake.md
  - raw/docs-snapshots/2026-05-26/pages/products/web-hosting.md
  - raw/docs-snapshots/2026-05-26/pages/products/ledgerflow.md
  - raw/docs-snapshots/2026-05-26/pages/products/kliq.md
  - raw/docs-snapshots/2026-05-26/pages/products/statur.md
  - raw/docs-snapshots/2026-05-26/pages/products/volo.md
  - raw/docs-snapshots/2026-05-26/pages/products/cyclone/cyclone-qs.md
  - raw/docs-snapshots/2026-05-26/pages/overview/terminology.md
  - raw/docs-snapshots/2026-05-26/pages/roadmap/roadmap.md
  - raw/docs-snapshots/2026-05-26/pages/developers/api.md
related: [technology-overview, technology-compute, technology-storage, technology-nodes-and-staking]
tags: [technology, products, roadmap]
---

# Products in the docs

Every product the docs describe, with its status and its role for marketing. Product pages with positioning live in [Products](../products/README.md). This page is only the technical record.

## Products in the navigation

| Product | What it is (technically) | Status per docs | Role for marketing |
|---|---|---|---|
| **Insight** | Hosted Cardano data and transaction API for institutions: UTXOs and balances, assets, transactions (including submit), staking accounts, stake pools, network. API keys per partner. Responses `success` / `data` / structured errors. "Powered by Iagon Enterprise Compute." | Live (partner access) | Enterprise lead product. The Insight brief adds governance, evaluate and Blockfrost/Koios compatibility, which the docs page does not mention yet. |
| **Ecosystem Stats** | Web app joining Cardano on-chain data and Iagon backend network stats in one view. | Live | Source of every network metric in public content. |
| **Staking Platform** | Delegation of IAG to nodes, Quick Delegate, Market for selling positions, Swap from ADA into staked positions. [dashboard.iagon.com/stake](https://dashboard.iagon.com/stake) | Live | Community and token holder audience. |
| **Borrow Stake** | Delegated-node operators borrow IAG from a 10M pool at 5–10% APR, paid up front in ADA. | Live (25-month program) | Node operator audience only. |
| **Web Hosting** | Websites served from Iagon storage. The Iagon Identifier maps domains to storage folders. Caching. | Listed as achieved on the roadmap | Developer and community use case. |
| **LedgerFlow** | Cardano Multisender (batch sends, address book) and Multisig wallets. Terminology adds bills and tax tracking. | Overhaul "coming soon" | Not for current campaigns. |
| **Kliq** | Contact app with QR sharing of .vcf contacts. | Demo app: built to "demonstrate the use of Iagon's storage and application deployment" | Not a product to market. Can illustrate the platform. |
| **Statur** | Self-sovereign pseudonymous reputation model: soulbound tokens enforced by a Cardano validator, dynamic NFTs pointing to files in Iagon storage. | On the roadmap ("Statur Reputational Model", integration with cloud services) | Concept. Do not present as available. |
| **Volo** | End-to-end encrypted chat for web and mobile. | Specification only | Concept. Do not present as available. |
| **Cyclone Qs / Qs Pro** | Plug-and-play node hardware with Cyclone OS. | Pre-sales; setup guides published | Node operator audience. |

## Named only in Terminology

| Name | Definition in the docs | Note |
|---|---|---|
| **Transfer** | File sharing for storage subscribers with expiring, optionally password-protected links | No page. Status unknown. |
| **HealthSafe** | Decentralized health portal for records and journals | No page. Echoes the 2017 healthcare origin. Status unknown. |
| **Fantasy Brawl** | Fantasy sports league built on Iagon Storage and Compute | No page. Status unknown. |
| **Network Explorer** | Network of nodes that process backend tasks: file distribution, availability logging | On the roadmap as "Network Explorer". |

Ask the docs team whether these are live, paused or retired before any mention.

## Developer access

- **Iagon API:** Postman collection at [api.docs.iagon.com](https://api.docs.iagon.com/). Personal Access Token from the settings page of [app.iagon.com](https://app.iagon.com).
- **Insight API:** separate reference documentation for partners, API keys required.
- **Developers Guide:** "Page under development".

## Roadmap page (hidden)

The roadmap page exists but is not in the navigation. Undated.

- **Achieved (as listed):** decentralized compute first iteration, voting power, subscription manager, decentralized storage mainnet, website hosting, tokenomics on Cardano, Agora system first iteration, API for resource providers, LedgerFlow, MVP releases, IAG migration to Cardano, ISPO with Maestro.
- **Next (as listed):** storage marketplace, revenue sharing on the Staking Platform, Bee-Hive architecture (backend tasks such as sharding and encryption run by public nodes), LedgerFlow overhaul, enterprise user roles, GDPR compliance tracker, full security and architecture audit, DAO launch, Network Explorer, Statur, CDN browser extension, pilots onboarding, "Decentralized AI Alexandria Protocol", Fluxion query language.

**For marketing:** do not cite the roadmap page. It is hidden and undated. Use dates only where a live page states them, such as storage in Q1 2027.
