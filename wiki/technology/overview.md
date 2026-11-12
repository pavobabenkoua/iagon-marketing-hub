---
id: technology-overview
title: Technical overview
type: technology
status: draft
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/overview/introduction.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/high-level-architecture.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/storage-overview.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-compute/compute-overview.md
  - raw/docs-snapshots/2026-05-26/pages/blockchain/on-chain-activity.md
  - raw/docs-snapshots/2026-05-26/pages/overview/terminology.md
related: [technology-storage, technology-nodes-and-staking, technology-compute, technology-token-and-onchain, technology-products, technology-key-figures]
tags: [technology, architecture, docs]
---

# Technical overview

Iagon is a protocol on Cardano that turns storage and compute capacity owned by independent operators into one network, with encryption on the client and the economy settled on-chain.

Docs: [Introduction](https://docs.iagon.com/overview/introduction) · [High-Level Architecture](https://docs.iagon.com/iagon-storage/high-level-architecture)

## The components

| Component | What it does | Status per docs |
|---|---|---|
| **Iagon client** | How users reach storage: web app, browser extension, native clients, API. | Live in part. The docs say the client "ships, or will ship" in these forms. |
| **Secure Lake** | Encrypted, resumable storage and sharing layer. Encryption runs only on the client. Two access layers: server policy and cryptographic envelopes. | In development. The full product is "on track" for Q1 2027. |
| **Sharding** | Splits ciphertext into fragments placed across nodes, with redundancy and parallel download. Iagon's own placement logic, not IPFS. | In development, as part of the new storage stack. |
| **Rubato** | Storage marketplace. Encodes supply and demand. Static pricing for enterprise providers, dynamic pricing for retail nodes. | Described as architecture. No separate product page. |
| **Fermato** | Subscription layer. Connects users to Cardano smart contracts. A subscription is an NFT locked in a contract, paid in ADA or stablecoin, signed with a wallet. | In development ("behaviour and interfaces may change"). |
| **Adagio** | Rewards layer. Connects consumer demand with node supply: commitment, staking, tiers, rewards. | Live. Runs the staking and tier system. |
| **Storage nodes** | Operator devices that commit capacity, stake IAG, serve data and are measured for uptime and throughput. | Live. |
| **Iagon dashboard** | Operators verify nodes, stake, monitor and claim. Delegators find nodes and delegate. | Live: [dashboard.iagon.com](https://dashboard.iagon.com/stake). |
| **Cardano** | Where node registration, stake, delegation, subscriptions and rewards are recorded. | Live. |
| **Compute** | Nodes that run apps and tasks in isolated virtual machines. | Docs page says "Coming Soon" and "early stages". Insight is described as running on Iagon Enterprise Compute. See [Compute](compute.md). |

## How the pieces connect

Consumers subscribe through Fermato and store data in Secure Lake. Rubato matches that demand with capacity committed by storage nodes. Adagio measures nodes, places them in tiers and pays rewards. Cardano records stake, delegation, subscriptions and payouts. Operators and delegators work through the dashboard.

The docs diagram is in [High-Level Architecture](https://docs.iagon.com/iagon-storage/high-level-architecture).

## Two income streams for the supply side

1. **Fees:** ADA from storage subscriptions. 90% goes to nodes and their delegators, monthly.
2. **Rewards:** IAG from a 15-year emissions schedule of 100 million IAG, per epoch, by tier.

Details: [Nodes and staking](nodes-and-staking.md).

## Basic facts

| Fact | Value | Status |
|---|---|---|
| Founded | 2017. The idea started with healthcare data ownership. | Structural |
| Chain | Cardano. IAG launched as an ERC-20 token, then migrated to Cardano because of Ethereum scaling issues. | Structural |
| Epoch | 5 days, aligned with Cardano epochs. 73 epochs a year. | Live |
| Privacy posture | Client-side encryption for every file body: no "skip encryption" path. Nodes hold only ciphertext. | Stated as design of the new storage stack (in development) |

## What marketing should know

- The docs still open with the 2021-era framing: "Initially, our focus lies in creating a transparent storage marketplace", with problem examples from 2017–2021. The brand has moved to enterprise focus and the Compliance Gap. Use the architecture facts, not the introduction's framing. Fix proposed in [Docs feedback](docs-feedback.md).
- The strongest current technical proof points: client-side encryption with two independent access layers, on-chain subscriptions as verifiable records, performance-measured nodes with a public 10-tier system, and a public on-chain footprint anyone can audit.
- Most of the new storage product (Secure Lake, Fermato, sharding) is labelled in development. Say "is building" or "in development", not "offers".
