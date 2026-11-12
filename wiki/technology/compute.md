---
id: technology-compute
title: Compute
type: technology
status: draft
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/iagon-compute/compute-overview.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-compute/compute-specifications.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-compute/compute-subscription.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-compute/compute-solutions/running-apps.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/compute-node/compute-requirements.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/compute-node/compute-rewards.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/compute-node/compute-fees.md
  - raw/docs-snapshots/2026-05-26/pages/provide-resources/compute-node-setup/compute-changelogs.md
  - raw/docs-snapshots/2026-05-26/pages/products/insight.md
related: [technology-overview, technology-products, technology-docs-feedback]
tags: [technology, compute]
---

# Compute

Docs: [Compute Overview](https://docs.iagon.com/iagon-compute/compute-overview) (the only compute page in the navigation). The other compute pages exist but are hidden from navigation and search.

> **Status: unclear, check before use.** The overview says "Iagon Compute is Coming Soon" and "work on compute is in the early stages". The roadmap lists "Decentralized Compute first iteration" as achieved. The compute node CLI had mainnet beta releases in June–July 2024. The Insight page says Insight is "powered by Iagon Enterprise Compute". Until the docs team confirms the current state, use "Iagon Compute" only in the Insight context and do not describe public compute as available. Raised in [Docs feedback](docs-feedback.md).

## What it is meant to do

Providers contribute CPU, memory and storage. Subscribers run apps and tasks on those nodes in isolated virtual machines. The stated goals: use idle computational resources, reward participation, reduce centralization risk, integrate with existing infrastructure.

## Architecture

| Part | Role |
|---|---|
| **Compute node** | The provider's machine. Node CLI (registration, benchmarks, eligibility, authorization key), internal monitoring server, task manager (decrypts, runs, encrypts the result). |
| **Compute backend server** | Node monitor (heartbeats, availability), security guard (filters malicious or invalid task requests), task distributor (picks the node that matches the subscription). The docs note this "can be a Hive Server". |
| **Provider dashboard** | Node status and performance for providers. |
| **Subscription manager** | Packages, validity, renewal. |

Task flow: subscribe → submit task → security check → encrypt → node selection → decrypt and run on the node → encrypt the result → return to the user.

Metrics tracked: CPU and memory for hosts, VMs and tasks; read/write speed; disk IO; network bandwidth.

## Requirements for a compute node

| Requirement | Minimum |
|---|---|
| OS | Ubuntu 22.04 |
| CPU | 4 cores, 2 GHz base, Sysbench 60 EPS |
| Memory | 8 GB; bandwidth 45,000 Mbps read, 40,000 Mbps write |
| Storage | 100 GB; sequential 5,000 Mbps read/write, random 300 Mbps |
| Network | 150 Mbps up and down; ping and latency at most 100 ms; public IP; virtualization support |

The specification page marks these as "not final".

Apps supported today: Node.js LTS 16, 18 and 20, from a public Git repository.

## Pricing and rewards

- Subscription price formula: `Price = 4 × (CPU cores + RAM GB / 2 + Storage GB / 100)`. The page does not state the currency or period.
- Fees: 90% to node providers, 7% to the treasury, 3% to IAG buyback (same split as storage).
- Rewards: 20,000,000 IAG over 15 years on the same declining curve as storage, capped at 30% APY until at least 6M IAG is staked. Marked "not final".

The 20M compute rewards do not appear as a line in the tokenomics allocations. Tokenomics earmarks 20M for "Storage Provider Hives" and 251M for "future programs like decentralized compute". Raised in [Docs feedback](docs-feedback.md).

## For marketing

- Compute is the second half of the category name ("Shared Storage and Compute Economy"). Today the only public, documented compute use is Insight.
- Do not quote the compute node requirements or pricing externally until the status is confirmed.
