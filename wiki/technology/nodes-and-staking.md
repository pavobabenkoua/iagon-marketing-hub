---
id: technology-nodes-and-staking
title: Nodes and staking
type: technology
status: approved
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/minimum-requirements.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/tier-system.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/iag-staking.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/storage-nodes/fees.md
  - raw/docs-snapshots/2026-05-26/pages/products/staking-platform.md
  - raw/docs-snapshots/2026-05-26/pages/products/borrow-stake.md
  - raw/docs-snapshots/2026-05-26/pages/products/cyclone/cyclone-qs.md
  - raw/docs-snapshots/2026-05-26/pages/products/cyclone/cyclone-qs-with-drives.md
  - raw/docs-snapshots/2026-05-26/pages/overview/terminology.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/detailed-storage-architecture/adagio.md
related: [technology-overview, technology-token-and-onchain, technology-key-figures, brand-proof-library]
tags: [technology, nodes, staking, rewards, tiers]
---

# Nodes and staking

The supply side of the network: who runs nodes, what they must deliver, how they are measured and how they earn. All of it is live.

Docs: [Minimum Requirements](https://docs.iagon.com/provide-resources/storage-nodes/minimum-requirements) · [Tier System](https://docs.iagon.com/provide-resources/storage-nodes/tier-system) · [IAG Staking](https://docs.iagon.com/provide-resources/storage-nodes/iag-staking) · [Fees](https://docs.iagon.com/provide-resources/storage-nodes/fees) · [Staking Platform](https://docs.iagon.com/products/staking-platform) · [Borrow Stake](https://docs.iagon.com/products/borrow-stake)

## Who takes part

| Role | What they do |
|---|---|
| **Operator** | Runs a node, commits capacity, stakes IAG (the *pledge*), sets a *margin* on delegators' earnings. |
| **Delegator** | Adds IAG to a node's stake through the Staking Platform in exchange for a share of its earnings. Runs no hardware. |
| **Subscriber** | Pays for storage. Their fees fund 90% of node income in ADA. |

Anyone with an always-online computer or server with spare storage can run a node.

## Minimum requirements (storage node)

Set for a 1 TB commitment. Larger commitments should scale speeds proportionately.

| Requirement | Minimum |
|---|---|
| Storage capacity | 900 GB |
| RAM | 4 GB |
| Upload / download | 20 Mbps (2.5 MB/s) |
| Read / write | 20 Mbps (2.5 MB/s) |
| Uptime | 90% |

## The 10-tier system

Every node is measured each epoch and placed in a tier from 0 to 10. A node must meet **all** thresholds of a tier. Missing one metric drops it to the tier below.

| Tier | Upload Mbps | Download Mbps | Read MB/s | Write MB/s | Epoch uptime |
|---|---|---|---|---|---|
| 0 Flagged | below Tier 1 or flagged by validation | | | | |
| 1 | 20 | 20 | 2.5 | 2.5 | 90% |
| 2 | 50 | 50 | 50 | 50 | 92% |
| 3 | 100 | 100 | 200 | 200 | 94% |
| 4 | 200 | 200 | 500 | 500 | 96% |
| 5 | 300 | 500 | 800 | 800 | 97% |
| 6 | 400 | 600 | 1,200 | 1,200 | 98% |
| 7 | 500 | 800 | 2,000 | 2,000 | 99% |
| 8 | 1,000 | 1,000 | 3,000 | 3,000 | 99.5% |
| 9 | 2,000 | 2,000 | 4,000 | 4,000 | 99.8% |
| 10 | 10,000 | 10,000 | 5,000 | 5,000 | 99.9% |

- **Tier 0** earns nothing for that epoch. It covers nodes below Tier 1 and nodes whose declared capacity does not match observed performance. Recovery in the next epoch restores earning.
- **Tier Score (1–100)** ranks a node within its tier. It measures the node as a whole pipeline (network to disk and disk to network), combined with uptime, demand and use of committed storage.
- **Staking extreme amounts does not raise rewards** if performance does not match the commitment.

**For marketing:** this is the "measured, not promised" proof point. Supply quality is checked every 5 days against public thresholds, and bad actors are excluded from rewards.

## Staking: how much IAG a node needs

```
IAG to be staked = Storage (GB) × (Base + Alpha × (Base / IAG price in USD))
Base  = $0.50 per GB committed
Alpha = 0.9 (may be adjusted)
```

- When the IAG price falls, more IAG is needed. When it rises, less.
- Cyclone pages put it as "about $500 of IAG per TB", plus at least 15 ADA in the wallet.
- **Unbonding: 3 months (90 days).** A retiring node or a withdrawing delegator gets tokens back 3 months after starting, so capacity does not disappear suddenly.
- **Margin** changes take 2 epochs (10 days).

## Earnings, part 1: ADA fees

| Share | Goes to |
|---|---|
| 90% | Nodes and their delegators, in proportion to staked storage and tier |
| 7% | Iagon treasury |
| 3% | Buyback of IAG on the open market |

- Fees are collected monthly and claimable at the start of the next month. Annual plans count as 1/12 per month.
- Until paid out, collected fees are delegated to the IAGL1 stake pool. The ADA rewards go to the Liquidity Providers Program.

## Earnings, part 2: IAG rewards

| Rule | Value |
|---|---|
| Total pool | 100,000,000 IAG over 15 years |
| Year 1 | 8,860,024.82 IAG (8.86%), declining to 5,316,014.889 IAG (5.32%) a year in years 10–15 |
| Epoch pot | Yearly allocation ÷ 73 |
| Split by tier | Tier factor ÷ sum of factors × epoch pot. Factors: T1 0.05, T2 0.15, T3 0.25, T4 0.30, T5 0.40, T6 0.50, T7 0.70, T8 0.80, T9 0.90, T10 1.00 |
| Within a tier | Node weight = Tier Score × stake |
| APY cap | Per tier. Excess flows down T10 → T1 as a bonus. Excess from T1 stays unallocated and may extend the schedule. Cap values are not published on the page. |
| Timing | Rewards for epoch n are calculated at n+1 and claimable at n+73 (about one year) |

## Delegation and the Staking Platform

- Delegators pick nodes by margin, reputation and availability, or use **Quick Delegate**, which picks the lowest-margin nodes with space.
- A delegated **position** can be sold on the Market for ADA at any time, or withdrawn with the 90-day unbonding.
- ADA holders can buy positions that are already staked (**Swap**) and receive all their future earnings.

## Borrow Stake

Operators of delegated nodes can borrow IAG from a pool and stake it to their own node at 100% margin.

| Detail | Value |
|---|---|
| Pool | 10,000,000 IAG, from the unlocked Team allocation |
| Duration | 6 to 24 whole months, no early exit |
| Fee | APR from 10% (6 months) to 5% (24 months), linear. Charged on the ADA value of the borrowed IAG, paid up front in ADA |
| Program length | 25 months. Last new loan in month 20 |
| End of term | Last 3 months are the withdrawal phase (still earning). Tokens return to the pool automatically |

The page does not give the program start date. Ask the docs team before quoting the timeline.

## Cyclone

A physical server built by Iagon to run a node plug-and-play, with Cyclone OS (Linux with Storage and Compute node software pre-installed). Models: Cyclone Qs and Qs Pro, with or without drives. Pre-sales accept ADA or stablecoins. Operating range 5–35 °C, 10–90% humidity.
