---
id: technology-key-figures
title: Key technical figures
type: technology
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/overview/introduction.md
  - raw/docs-snapshots/2026-05-26/pages/overview/terminology.md
  - raw/docs-snapshots/2026-05-26/pages/blockchain/iagon-token/tokenomics.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/minimum-requirements.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/tier-system.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/iag-staking.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/fees.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/storage-overview.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/subscription.md
  - raw/docs-snapshots/2026-05-26/pages/products/borrow-stake.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/compute-node/compute-rewards.md
  - raw/archive/2023-11-18-fyeo-staking-contract-audit.pdf
related: [technology-overview, brand-proof-library, brand-mechanics]
tags: [technology, figures, facts]
---

# Key technical figures

Every number marketing may need from the docs, in one place. Snapshot 2026-05-26.

**Quote** column:
- **Yes:** may appear in external material as written.
- **Context:** true, but only with the wording given in the note.
- **No:** internal knowledge only.

Network metrics (nodes, countries, capacity, staked IAG) are not here. They come from the Ecosystem Stats App.

## Company and protocol

| Figure | Value | Status | Quote | Note | Docs page |
|---|---|---|---|---|---|
| Founded | 2017 | Structural | Yes | | [Introduction](https://docs.iagon.com/overview/introduction) |
| Chain | Cardano | Live | Yes | | [Introduction](https://docs.iagon.com/overview/introduction) |
| Epoch length | 5 days, 73 a year | Live | Yes | Same as Cardano | [Terminology](https://docs.iagon.com/overview/terminology) |
| Staking contract audit | FYEO Inc., 18 November 2023, 2 Low findings, both remediated | Structural | Context | "Audited by FYEO (2023)". Cover the staking contract only, not the whole protocol | Not linked on any page. `raw/archive/2023-11-18-fyeo-staking-contract-audit.pdf` |

## Token

| Figure | Value | Status | Quote | Note | Docs page |
|---|---|---|---|---|---|
| IAG supply | 1,000,000,000, fixed | Live | Yes | | [Tokenomics](https://docs.iagon.com/blockchain/iagon-token/tokenomics) |
| Funds raised in presale | $3.6 million, four rounds | Structural | Context | Only in token or funding context, past tense | [Tokenomics](https://docs.iagon.com/blockchain/iagon-token/tokenomics) |
| Node staking rewards pool | 100,000,000 IAG over 15 years | Live | Context | Describe as network incentives, never as yield | [IAG Staking](https://docs.iagon.com/provide-resources/storage-nodes/iag-staking) |
| Compute rewards pool | 20,000,000 IAG over 15 years | Not final | No | Conflicts with tokenomics allocations | [Compute Rewards](https://docs.iagon.com/provide-resources/compute-node/compute-rewards) (hidden) |
| Community incentives wallet | 461,000,000 IAG | Live | Context | Token audience only | [Tokenomics](https://docs.iagon.com/blockchain/iagon-token/tokenomics) |
| Development wallet | 112,000,000 IAG | Live | No | | [Tokenomics](https://docs.iagon.com/blockchain/iagon-token/tokenomics) |
| Team wallet | 85,000,000 IAG | Live | No | | [Tokenomics](https://docs.iagon.com/blockchain/iagon-token/tokenomics) |

## Network economics

| Figure | Value | Status | Quote | Note | Docs page |
|---|---|---|---|---|---|
| Fee share to nodes and delegators | 90% of subscription fees | Live | Yes | "90% of what customers pay goes to the people who run the network" | [Fees](https://docs.iagon.com/provide-resources/storage-nodes/fees) |
| Treasury share | 7% | Live | Context | | [Fees](https://docs.iagon.com/provide-resources/storage-nodes/fees) |
| IAG buyback share | 3% | Live | Context | Token audience only. No price implication | [Fees](https://docs.iagon.com/provide-resources/storage-nodes/fees) |
| Unbonding period | 3 months (90 days) | Live | Yes | | [IAG Staking](https://docs.iagon.com/provide-resources/storage-nodes/iag-staking) |
| Reward claim delay | 73 epochs after the epoch earned | Live | Context | Node operator audience | [IAG Staking](https://docs.iagon.com/provide-resources/storage-nodes/iag-staking) |
| Base stake | $0.50 of IAG per GB committed (alpha 0.9) | Live | Context | "About $500 of IAG per TB" for operators | [IAG Staking](https://docs.iagon.com/provide-resources/storage-nodes/iag-staking) |
| Borrow Stake pool | 10,000,000 IAG | Live | Context | Node operator audience | [Borrow Stake](https://docs.iagon.com/products/borrow-stake) |
| Borrow fee | 5–10% APR, 6–24 months | Live | Context | Node operator audience | [Borrow Stake](https://docs.iagon.com/products/borrow-stake) |

## Node quality

| Figure | Value | Status | Quote | Note | Docs page |
|---|---|---|---|---|---|
| Performance tiers | 10 reward tiers plus Tier 0 (flagged) | Live | Yes | "Every node is measured every 5 days against public thresholds" | [Tier System](https://docs.iagon.com/provide-resources/storage-nodes/tier-system) |
| Minimum uptime | 90% (Tier 1) to 99.9% (Tier 10) | Live | Yes | | [Tier System](https://docs.iagon.com/provide-resources/storage-nodes/tier-system) |
| Minimum node | 900 GB, 4 GB RAM, 20 Mbps, 90% uptime | Live | Context | Operator recruitment only | [Minimum Requirements](https://docs.iagon.com/provide-resources/storage-nodes/minimum-requirements) |

## Storage product

| Figure | Value | Status | Quote | Note | Docs page |
|---|---|---|---|---|---|
| New storage availability | Q1 2027 | In development | Context | "On track for Q1 2027", as the docs say. Re-check each snapshot | [Storage Overview](https://docs.iagon.com/iagon-storage/storage-overview) |
| Entry plan | $2.20 a month, 500 GB (1,000 GB for Iagonauts) | Live | Context | Consumer material only | [Subscriptions](https://docs.iagon.com/iagon-storage/subscription) |
| Data retention after non-payment | 3 months | Live | No | | [Subscriptions](https://docs.iagon.com/iagon-storage/subscription) |

## Not in the docs

These brand facts have no source in the docs. They need their own source in the Proof Library ([open item 1](../brand/open-items.md)):

- Granted patents in 15+ jurisdictions
- National innovation funding
- Any named deployment or partner
