---
id: technology-token-and-onchain
title: Token and on-chain
type: technology
status: draft
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/blockchain/iagon-token/tokenomics.md
  - raw/docs-snapshots/2026-05-26/pages/blockchain/on-chain-activity.md
  - raw/docs-snapshots/2026-05-26/pages/overview/lspo.md
  - raw/docs-snapshots/2026-05-26/pages/products/borrow-stake.md
  - raw/archive/2023-11-18-fyeo-staking-contract-audit.pdf
related: [technology-nodes-and-staking, technology-key-figures, brand-proof-library]
tags: [technology, token, iag, cardano, on-chain, audit]
---

# Token and on-chain

Docs: [Tokenomics](https://docs.iagon.com/blockchain/iagon-token/tokenomics) · [On-Chain Activity](https://docs.iagon.com/blockchain/on-chain-activity) · [LSPO](https://docs.iagon.com/overview/lspo)

> **Token topics are regulated speech.** No price talk, no return promises, no "investment" framing in marketing copy. The docs [Disclaimer](https://docs.iagon.com/disclaimer) states IAG may have no value and the docs are not an offer. Describe what the token does in the network, not what it may be worth.

## IAG at a glance

| Fact | Value |
|---|---|
| Chain | Cardano (native asset). ERC-20 tokens discontinued after migration. |
| Supply | 1,000,000,000 IAG, fixed |
| Presale | Four rounds: Seed, Strategic, Private, Public. $3.6 million raised. |
| Policy ID | `5d16cc1a177b5d9ba9cfa9793b07e60f1fb70fea1f8aef064415d114` |
| Hex name | `494147` |
| Asset fingerprint | `asset1z62wksuv4sjkl24kjgr2sm8tfr4p0cf9p32rca` |

## Allocations (initial, on Cardano)

Each allocation sits in a named wallet (ADA Handle) that anyone can track. The docs state these tokens are controlled by the DAO and not owned by any company.

| Wallet | Amount | What it is for |
|---|---|---|
| `$iagon.incentives` | 461M | Community: 60M referral program, 30M LSPO (12-month vesting from April 2024), 100M node staking rewards over 15 years, 20M "Storage Provider Hives", 251M reserved for future programs such as decentralized compute |
| `$iagon.dev` | 112M | Development. Monthly expenses $140k since November 2025, converted linearly since October 2023. 500k IAG a month for the ERC-20 swap since March 2024. Covers advisor tokens since December 2024. |
| `$iagon.marketing` | not stated | Marketing and advisors. Unlocked, ad hoc use. |
| `$iagon.team` | 85M | Locked until October 2025, then distributed over 6 months. 10M is now the Borrow Stake pool. |
| `$iagon.liquidity`, `$iagon` | not stated | Liquidity and tokens reserved for the ERC-20 swap (ongoing). |

All other tokens are on the free market.

## What the token does

- **Stake:** operators and delegators lock IAG to activate storage capacity. The amount scales with capacity and price ([formula](nodes-and-staking.md#staking-how-much-iag-a-node-needs)).
- **Rewards:** node operators and delegators earn IAG from the 100M emission schedule.
- **Holder benefits:** Iagonauts storage tiers for holders of enough IAG value.
- **Buyback:** 3% of subscription fees buy IAG on the open market.

The docs also describe IAG as a payment medium priced against fiat ("NOK or EUR") and as "non-speculative". These passages predate the current model (subscriptions are paid in ADA or stablecoins). Do not reuse them. Raised in [Docs feedback](docs-feedback.md).

## On-chain footprint

Every node and every delegated position is recorded on-chain as a token next to its IAG stake in a UTxO. This is the "verifiable, not claimed" proof point: anyone can audit the network's commitments on Cardano.

| What | Identifier |
|---|---|
| Node token policy | `ac35ee89c26b1e582771ed05af54b67fd7717bbaebd7f722fbf430d6` |
| Delegation token policy | `faecb80eee6cadf9dac5184263ed4d164b38fe71d4f6f55e8f6b0da0` |
| Market batcher token policy | `3ec3f628639c989da3302724c61c90ced45571d611563d98cd528616` |
| Stake pool IAGL1 | `pool1ztk6dcj2nc3plnujf3ek6jqngtx8hcryufz56lyumemlcy2xxn0` |
| Stake pool IAGL2 | `pool1e59h5m5vyggszyafel7zvcnsayt2de7wyxyezlrsmm4a679q3zr` |

Payment addresses (node script, delegation script, rewards, market, subscriptions, Cyclone purchases, Borrow Stake) are on the docs page. Copy them from there, never from this hub.

The two ADA stake pools generate ADA for the IAG-ADA liquidity pairs on DEXs.

## Security audit

The staking contract was audited by **FYEO Inc.**, report v1.0 dated 18 November 2023, security level "Public". Testing ran 31 October to 18 November 2023 on `staking.ak` and `reward.ak`. Two findings, both rated Low, both remediated. Conclusion: the reviewed code implements the documented functionality.

The PDF sits in the docs repository but no docs page links to it. File: `raw/archive/2023-11-18-fyeo-staking-contract-audit.pdf`. Candidate for the Proof Library audit entry ([open item 1](../brand/open-items.md)).

## LSPO: Liquidity Providers Rewards Program

An always-on program (it replaced the earlier phases) that rewards people who delegate ADA to IAGL1 or IAGL2, or provide liquidity to IAG pairs on partner DEXs.

- Each reward token accumulates for about 12 months (about 73 epochs) from the day it joins the pool.
- Rewards are calculated once a year in a May-to-May cycle, then vest and are claimed monthly on DripDropz: IAG over about 12 months, most partner tokens over 6.
- Iagon contributes 10% of payback transactions. Partner projects have added tokens: Saturn Swap, Nuvola, House of Titans, Tokeo, FarmRoll, Metera, Midnight (NIGHT, date TBA).
