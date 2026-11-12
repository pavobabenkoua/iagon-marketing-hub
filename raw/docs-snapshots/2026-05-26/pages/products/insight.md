---
title: "Insight"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---
# Insight


## Overview

**Insight** is Iagon’s hosted **Cardano data and transaction API** for partners who need reliable access to the ledger without operating their own Cardano nodes, indexers, or supporting infrastructure. Teams can integrate custody workflows, treasury tools, analytics, and staking-related products using a single versioned HTTP API and standard JSON responses, while Iagon maintains synchronization, availability, and operational burden behind the scenes.

For banks, custodians, exchanges, and other institutional builders, that model lowers the barrier to participating in Cardano: you interact with addresses, balances, UTXOs, transaction history, and submission through documented endpoints instead of provisioning and staffing long-lived node clusters.

Insight is **powered by Iagon Enterprise Compute**. The service runs on Iagon’s decentralized compute layer, aligning high-availability chain access with the same resource network that supports the broader Iagon ecosystem.


## What the API Encompasses

At a high level, the [Iagon Insight API](https://docs.fireblocks.partners.iagon.com/api/) groups capabilities into the areas most teams need to build on Cardano:

- **Chain health** - Simple checks that the API and backing services are responsive.
- **UTXOs and balances** - Query unspent outputs and asset balances by address and related identifiers so wallets and custodians can construct and validate transactions.
- **Assets** - Work with asset metadata and aggregated balances in line with how applications account for ADA and native tokens.
- **Transactions** - Inspect historical and detailed transaction views, fetch individual transaction detail, and **submit** signed transactions to the network through the API when your architecture does not include a local node.
- **Staking accounts** - Read stake-related context such as account summary, rewards, delegations, withdrawals, associated addresses, held assets, and registration history for staking integrations and reporting.
- **Stake pools** - Access pool information, metadata, delegator views, and block production context for dashboards and delegation products.
- **Network** - Reference network-level data such as the latest epoch so applications stay aligned with chain progression.

Responses follow a consistent pattern (`success`, `data`, and structured errors), and the reference documentation describes authentication, types, and examples across languages.


## Access and Documentation

API access uses **API keys** issued to partners (see [Authentication](https://docs.fireblocks.partners.iagon.com/api/authentication.html) in the Insight API docs). For integration details, endpoint reference, and examples, use the full guide:

**[Iagon Insight API documentation](https://docs.fireblocks.partners.iagon.com/api/)**

<br/>
