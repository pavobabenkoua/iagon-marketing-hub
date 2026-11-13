---
id: post-development-update-01
title: "Development Update | October 2026"
type: post
status: approved
owner: Pavlo Babenko
updated: 2026-11-13
visibility: team
series: series-development-update
period: 2026-10
publications:
  - channel: x
    date: 2026-11-12
    url: https://x.com/IagonOfficial/status/2120992144714547452
  - channel: telegram
    date: 2026-11-12
    url: https://t.me/iagonofficial/1167
  - channel: discord
    date: 2026-11-12
    url: https://discord.com/channels/837215135999197246/846654998096117791/1570552925099524226
sources: [raw/archive/2026-11-12-dev-changelog-2026-10.csv, wiki/series/development-update/inputs/2026-10.txt]
related: [series-development-update, brand-format-monthly-recap-cards, res-dev-update-canvas]
tags: [development-update, monthly-recap]
---

# Development Update | October 2026

## Summary
First issue of the Monthly Recap: 176 changes shipped in October across nine areas, three or four lines per area. Published 2026-11-12 as an X thread, one Telegram message and two Discord messages.

## Inputs and numbers

Raw data: [`raw/archive/2026-11-12-dev-changelog-2026-10.csv`](../../../../raw/archive/2026-11-12-dev-changelog-2026-10.csv). Picked lines: [`inputs/2026-10.txt`](../inputs/2026-10.txt).

From the October export: 176 changes, 26 topics, 9 areas. Weeks W40–W44 (28 September to 1 November 2026).

| Area | Changes |
|---|---|
| Iagon Storage Node | 44 |
| Würth Partner platform | 32 |
| Insight API | 28 |
| Iagon Infrastructure | 19 |
| Iagon Dashboard | 16 |
| Iagon Admin Dashboard | 12 |
| Iagon Platform | 10 |
| Mesh SDK | 9 |
| Insight Dashboard | 6 |

| Category | Changes |
|---|---|
| Development | 82 |
| Security | 20 |
| Production deployments | 16 |
| Production-ready tests | 15 |
| Updates | 11 |
| New software and servers | 8 |
| Bug fixes | 7 |
| Performance | 6 |
| Server security | 5 |
| Server updates | 4 |
| Debugging | 2 |

Visual: two cards, 1200×700, made on the design canvas ([res-dev-update-canvas](../../../resources.md)) before the square format and the repo template existed. X cropped their left side in the feed. Not rebuildable from the repo; the images are in the publications.

## As published

### X

```
Development Update | October 2026

176 changes shipped across nine areas.

What shipped in each area, in the thread below ⬇️.

🧵 1/10
```

```
Iagon Storage Node

- Self-healing Iagon Storage Nodes
- Higher fault tolerance, files readable with many Storage Nodes offline
- Automatic repair well before stored data is at risk
- Live node alerts in the Iagon Dashboard

🧵 2/10
```

```
Würth Partner platform

- Storage platform for Würth: Storage API compatible with the existing system, folders, zip downloads and share links
- Würth Partner platform dashboard with file explorer, share links, API tokens, team and audit log
- Portal of the Würth Royalty platform with catalog, orders, print queue and feedback
- Royalty payouts as IOU tokens

🧵 3/10
```

```
Insight API

- More Blockfrost compatible endpoints for accounts, addresses, assets, scripts and governance
- Mempool endpoints in the Insight API
- Insight reseller accounts with their own customers, keys and usage

🧵 4/10
```

```
Iagon Infrastructure

- Insight API live on the Cardano preprod network
- Security hardening of all production servers
- Operating system and kernel updates on all production servers

🧵 5/10
```

```
Iagon Dashboard

- New Iagon Dashboard with wallet login, storage quotes, delegation and withdrawals
- Storage Node Operator pages with performance, tiers and rewards
- On-chain transaction tracking in the new Iagon Dashboard

🧵 6/10
```

```
Iagon Admin Dashboard

- Iagon Admin Dashboard for all Iagon Services
- Access rights per service and team member in the Iagon Admin Dashboard
- Faster page loads in the Iagon Admin Dashboard

🧵 7/10
```

```
Iagon Platform

- Security page in the Würth Partner platform with passkeys, authenticator app and sessions
- Automatic blocking of scans and attacks for Insight and the Würth Partner platform
- Attack protection for Insight on production

🧵 8/10
```

```
Mesh SDK

- Mesh SDK provider for the Insight API: fetch, submit, evaluate and listen
- Mesh provider published on npm as @iagon/insight-mesh
- Transaction evaluation and raw transaction submit in the Insight API

🧵 9/10
```

```
Insight Dashboard

- Encryption key rotation for stored secrets
- Navigation improvements of the Insight Frontend
- Rows per page setting in the Insight Dashboard and its admin dashboard

🧵 10/10
```

```
That was October.

From here, a recap like this goes out every month. Weekly updates, with every change as it lands, go out in our Discord:
https://discord.gg/TCS23VWuWm

Thank you to the community. You move this ecosystem forward.

What would you like to see in the next one?
```

### Telegram
_To add: copy the text from the post._

### Discord
_To add: copy the text of both messages from the post._

## Results
Due 2026-11-19, 7 days after publication.

| Channel | Impressions | Engagements | Reposts | Replies | Clicks | Source |
|---|---|---|---|---|---|---|
| X | | | | | | X analytics |
| Telegram | | | | | | channel stats |
| Discord | | | | | | |

First reading on X, 8 minutes after posting: 595 views, 18 likes, 2 reposts, 2 replies on tweet 1.

## Commitments
Made: "From here, a recap like this goes out every month." The November issue closes it.

## Learning
Multi-image posts in X need square cards with a wide side safe zone: the 1200×700 cards lost the logo and the series name in the feed. Already a rule of the format.
