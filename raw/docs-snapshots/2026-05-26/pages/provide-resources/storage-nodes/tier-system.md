---
title: "Node Tier System"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
Storage Node
# Node Tier System

<br/>

Our 10-Tier System is designed to create a fair base for reward calculation and to provide a strong incentive to sustain a healthy ecosystem and network. Bad actors who attempt to game the system are prevented from receiving rewards, ensuring that node operators who act legitimately are treated fairly. At the same time, operators who take their role seriously and contribute to the stability and performance of the network are rewarded accordingly.

Rather than relying on a single metric, the system evaluates multiple performance dimensions simultaneously. To qualify for a specific tier, a storage node must meet or exceed all defined minimum thresholds for that tier - not just a subset. This ensures that consistent, real-world performance determines reward eligibility. Committed storage is judged the same way: a large pledge is not, by itself, a way to reach a higher tier if it does not match what the node can credibly deliver.

## Tier 0 - Flagged

Nodes that do not meet the minimum requirements defined in Tier 1 are automatically placed into Tier 0 (Flagged). Tier 1 represents the baseline performance level required to participate in the network and therefore in the reward system.

Tier 0 also includes nodes that are identified through internal validation mechanisms as behaving inconsistently with expected real-world performance. These nodes are considered flagged and are excluded from receiving rewards.

**Tier 0 applies when any of the following is true:**

- The node does not meet the minimum technical performance requirements
- The node has been identified through validation checks as not operating in a reliable or consistent manner
- The node’s committed storage or declared capacity is inconsistent with realistic, observed performance according to validation

Node operators in this tier are encouraged to review their setup, improve performance, and ensure stable operation. Once the node meets the required performance thresholds again, it will automatically move into a reward-eligible tier and start receiving rewards.

## Performance Threshold Overview
<br/>

| Tier    | Upload (Mbps) | Download (Mbps) | Read (MB/s) | Write (MB/s) | Epoch Uptime (%) |
| ------- | ------------- | --------------- | ----------- | ------------ | ---------- |
| **Tier 0**  | --            | --              | --          | --           | --         |
| **Tier 1**  | 20            | 20              | 2.5         | 2.5          | 90         |
| **Tier 2**  | 50            | 50              | 50          | 50           | 92         |
| **Tier 3**  | 100           | 100             | 200         | 200          | 94         |
| **Tier 4**  | 200           | 200             | 500         | 500          | 96         |
| **Tier 5**  | 300           | 500             | 800         | 800          | 97         |
| **Tier 6**  | 400           | 600             | 1,200       | 1,200        | 98         |
| **Tier 7**  | 500           | 800             | 2,000       | 2,000        | 99         |
| **Tier 8**  | 1,000         | 1,000           | 3,000       | 3,000        | 99.5       |
| **Tier 9**  | 2,000         | 2,000           | 4,000       | 4,000        | 99.8       |
| **Tier 10** | 10,000        | 10,000          | 5,000       | 5,000        | 99.9       |

::: info NOTE
The 10-Tier System does not treat committed storage as a number in isolation. It reviews that commitment in context and weighs it against whether the node’s declared capacity and behavior look **realistic** for the performance it actually delivers - and whether the node would genuinely help the network, or would be effectively useless despite a large on-paper pledge.

Because of that, **you cannot earn higher rewards simply by staking or committing extreme amounts of storage** while the rest of the picture does not add up. Tier placement still depends on meeting the performance and consistency requirements described in this document; inflating commitments is not a shortcut around them.
:::

## How It Works

Each tier represents a clearly defined performance baseline across five key metrics:

- Network throughput (upload and download)
- Storage performance (read and write speeds)
- Operational reliability (uptime)

To be classified into a tier, a node must consistently meet or exceed all of these requirements. Falling short in any single metric will place the node into a lower tier, even if all other metrics are satisfied. This ensures that only well-balanced and consistently performing nodes reach higher tiers. Those checks run alongside review of how much storage is committed relative to actual behavior, so performance - not an inflated commitment - drives tier placement.

In addition to these visible thresholds, the system includes multiple internal validation layers, consistency checks, and behavioral indicators. These continuously verify that performance reflects real, sustained operation over time. Nodes that attempt to manipulate or artificially influence their results are identified and excluded from receiving rewards.

## Tier Score

For nodes in **Tier 1 through Tier 10**, tier placement is only part of the picture. Each node also gets a **Tier Score** from **1 to 100** that applies **within** that tier - it measures how well the node performs **relative to other nodes in the same tier**. Tier 0 does not use a Tier Score.

The score is meant to reflect the node as a **whole data-handling pipeline**, not isolated leaderboard stats. Data coming in must be pulled from the network and written to disk; data going out must be read from disk and sent out on the network. Those two directions - often thought of as **ingest** (download paired with write) and **egress** (read paired with upload) - are evaluated so that **balance matters**: if one step in a direction is strong and the other is weak, the weak step limits the result instead of being masked by the strong one.

Those path-level results feed into an overall performance picture, which is then combined with **uptime**. Even excellent speeds earn less if the node is not reliably online. **Network demand** and **how much of the node’s committed storage is in use** can apply **modest** optional adjustments - enough to nudge rewards toward nodes that are genuinely useful, without drowning out the core performance signal.

The Tier Score is a whole number from 1 to 100. **Inside a given tier**, that score works together with the node’s **stake** to determine its **share of that tier’s reward pool** - so among nodes in the same tier, Tier Score governs how rewards are split between them.

## Our Goals

The 10 Tier System is built to give node operators a clear and actionable understanding of their current standing and what is required to move to a higher tier. It provides a transparent reference point for improving performance - whether through better hardware, improved connectivity, or higher uptime.

At the same time, the system allows IAGON to adapt to changes in technology and infrastructure. As new hardware becomes available or global performance standards evolve, thresholds can be adjusted to maintain fairness and relevance across the network.

**In short, the system is designed to:**

- Reward reliable and consistent node operators fairly
- Encourage continuous performance improvements
- Actively detect, stop, and exclude bad actors from participating in rewards
- Maintain a strong, healthy, and trustworthy network

This creates a sustainable and competitive environment where long-term contribution is recognized and rewarded.

<br/>
