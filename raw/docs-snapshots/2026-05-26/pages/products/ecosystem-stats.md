---
title: "Ecosystem Stats"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Ecosystem Stats App

## Overview

**Ecosystem Stats** is a web app that brings Iagon's on-chain and network activity into one place. It tracks Iagon-related statistics across **Cardano** and the **Iagon network**, giving the community, node operators, and stakeholders a clear, up-to-date view of how the ecosystem is growing and performing.

Instead of piecing together numbers from separate dashboards, explorers, and internal tools, Ecosystem Stats surfaces the metrics that matter in a single, easy-to-read experience.

## What It Covers

At a high level, the app aggregates Iagon-related activity from two complementary layers:

- **On Cardano** - Public ledger data tied to Iagon, including token movement, staking, and other chain-visible activity that reflects how participants engage with the protocol.
- **On the Iagon network** - Operational and network-level statistics maintained by Iagon's backend, reflecting the live state of storage, nodes, and related ecosystem services.

Together, these sources provide a unified snapshot and historical tracking of ecosystem health, participation, and growth over time.


## Data Sources

Ecosystem Stats is built on two authoritative data layers:

| Source | Role |
|---|---|
| **Cardano Blockchain** | On-chain records for Iagon-related assets, staking, and other public ledger activity. |
| **Iagon Backend** | Network and platform statistics that reflect the current state of Iagon services and infrastructure. |

Data from both sources is combined in the app so metrics stay aligned with what is verifiable on-chain and what reflects real-time network operations.


## How It Works

```mermaid
%%{init: {'flowchart': {'padding': 0, 'nodeSpacing': 85, 'rankSpacing': 55}}}%%
flowchart LR
    A["<div class='iag-eco-mermaid-node'><img src='/img/ecosystem-stats/cardano-icon.svg' class='iag-eco-mermaid-badge' alt=''/><span class='iag-eco-mermaid-label'>Cardano Blockchain</span></div>"]
    B["<div class='iag-eco-mermaid-node'><div class='iag-eco-mermaid-icon-circle iag-eco-mermaid-icon-circle--bg-3'><img src='/img/iagon-logo.svg' class='iag-eco-mermaid-iagon-logo' alt=''/></div><span class='iag-eco-mermaid-label'>Iagon Backend</span></div>"]
    C["<div class='iag-eco-mermaid-node'><div class='iag-eco-mermaid-icon-circle iag-eco-mermaid-icon-circle--purple-alt-6'><span class='figma-inline-icon'><svg viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M21 12C21 16.9706 16.9706 21 12 21M21 12C21 7.02944 16.9706 3 12 3M21 12C21 10.136 16.9706 8.625 12.0001 8.625C7.02951 8.625 3 10.136 3 12M21 12C21 13.864 16.9706 15.375 12.0001 15.375C7.02951 15.375 3 13.864 3 12M12 21C7.02944 21 3 16.9706 3 12M12 21C13.864 21 15.375 16.9706 15.375 12C15.375 7.02944 13.864 3 12 3M12 21C10.136 21 8.625 16.9706 8.625 12C8.625 7.02944 10.136 3 12 3M3 12C3 7.02944 7.02944 3 12 3' stroke='currentColor' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/></svg></span></div><span class='iag-eco-mermaid-label'>Ecosystem Stats App</span></div>"]
    D["<div class='iag-eco-mermaid-node'><div class='iag-eco-mermaid-icon-circle iag-eco-mermaid-icon-circle--purple-alt-6'><span class='figma-inline-icon'><svg viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg'><path d='M3 12C3 12 6.27273 5.5 12 5.5C17.7273 5.5 21 12 21 12C21 12 17.7273 18.5 12 18.5C6.27273 18.5 3 12 3 12Z' stroke='currentColor' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/><path d='M12.0001 14.4373C13.3557 14.4373 14.4546 13.346 14.4546 11.9998C14.4546 10.6536 13.3557 9.56234 12.0001 9.56234C10.6445 9.56234 9.54553 10.6536 9.54553 11.9998C9.54553 13.346 10.6445 14.4373 12.0001 14.4373Z' stroke='currentColor' stroke-width='1.5' stroke-linecap='round' stroke-linejoin='round'/></svg></span></div><span class='iag-eco-mermaid-label'>Unified Ecosystem View</span></div>"]
    A e1@--> C
    B e2@--> C
    C e3@--> D
    e3@{ curve: linear }
```

1. **Collect** - On-chain data is read from Cardano; network statistics are sourced from Iagon's backend services.
2. **Combine** - Related metrics are brought together so on-chain and off-chain signals tell a coherent story.
3. **Present** - The app displays an at-a-glance view of Iagon ecosystem activity, updated from these live sources.

<br/>
