---
title: "Storage Overview"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---

# Iagon Storage - How It Works for You

<br/>

Iagon Storage is decentralized cloud storage: you get familiar folders, files, sharing, and quotas, while your data is protected by encryption you control and is served from a network of independent storage providers rather than a single company’s data center. Your data is encrypted and sharded, then stored across multiple storage nodes so storage and retrieval are not tied to a single device, and your data cannot be re-assembled from any one storage source. This page summarizes the experience and benefits from an **end-user** perspective. For component names, diagrams, and deeper technical detail, see [High-level architecture](./high-level-architecture) and the [detailed architecture](./detailed-storage-architecture/adagio) pages.

:::info Under Development
The following details may not reflect the current product state, but rather what is being developed. The following state is on-track to be available in Q1 2027.
:::

## What You Get

- **Encrypted storage and sharing** - Files are encrypted on your devices before anything is uploaded. What providers hold is ciphertext, and [file sharding](./detailed-storage-architecture/sharding) distributes those encrypted pieces across the network so no single node is required to hold a complete reconstructable file without your keys. Storage node operators are not able to read your file contents or readable names. You get integrity checks so tampering or corruption surfaces as a failed decrypt rather than a silently wrong file.
- **A normal way to work** - Nested folders, geographically-placable drives, file history, sync across devices, resumable uploads (including very large files - often handled as encrypted segments on the client that then flow into the same sharded storage path), and integrations driven by events where the product supports them. You can use the web app or desktop application for easy access to your storage, or the API for scripted or headless workflows.
- **Fine-grained collaboration** - Share with specific people, use groups and inheritance, set expiry where available, and revoke access in predictable ways. Sharing uses cryptography so large files are not re-uploaded or re-encrypted for every new recipient when the product follows that model.
- **Choice in how you subscribe** - You can use website-based subscriptions or on-chain subscriptions paid with cryptocurrency. On-chain plans give you a publicly verifiable subscription tied to your wallet. Details and flows are in [Fermato](./detailed-storage-architecture/fermato).
- **Economy aligned with the network** - Behind the scenes, storage capacity comes from storage nodes run by independent operators; the protocol measures performance and availability so service quality and rewards can track how the network actually behaves. You do not need to manage that layer to use storage - think of it as the reason the network can offer resilient, competitively priced capacity.

## Subscriptions and Tiers

Storage is sold in tiers (storage amount, performance and optional extras depending on plan). Pricing is described in [Storage Subscriptions](./subscription), including Iagonauts tiers for users who hold enough IAG token value to unlock better price-to-storage ratios.

If a subscription stays unpaid after it has expired, data is deleted after a defined period. Tier parameters can change for new purchases without affecting existing subscriptions.

## Privacy and “Who Can Do What”

Two ideas work together:

1. **Network policy** - Who may list, read, upload, rename, or delete objects under your rules.
2. **Cryptographic access** - Who can unwrap keys and decrypt.

That way, a problem on one side does not automatically expose your content; defaults lean toward deny until you share.

At rest, your file bodies are not just “one blob on one disk” in the clear: sharding spreads encrypted fragments, which reinforces confidentiality alongside the crypto model above. Optional jurisdiction or drive policies help teams that must keep data in certain regions or retention rules (placement still follows the same encrypted, sharded model - see [File sharding](./detailed-storage-architecture/sharding)).

## Reliability and Performance

File sharding is central here: after encryption, ciphertext is split and spread so the protocol can keep redundant fragments and download in parallel from multiple providers instead of one bottleneck - improving both durability and speed when the network has capacity. You still interact through one product experience; [how fragments are placed and rebuilt](./detailed-storage-architecture/sharding) is what makes “not dependent on a single machine” true in practice.

## Cardano Wallet

Where the product uses Cardano, a wallet can connect identity and payment to on-chain subscription and participation. That is optional for users who only use traditional checkout, but it unlocks wallet sign-in and verifiable on-chain subscription state where those flows are available. Token holders can also participate in the broader staking and delegation ecosystem via the [Staking Platform](../products/staking-platform) if they want to support the network economically and earn from their participation.

## Where to Read More

| Topic | Page |
|--------|------|
| Plans, pricing, Iagonauts tiers | [Storage Subscriptions](./subscription) |
| Clients, Secure Lake, nodes, network | [High-Level Architecture](./high-level-architecture) |
| Encrypted storage, sharing, permissions | [Secure Lake](./detailed-storage-architecture/secure-lake) |
| On-chain subscriptions, wallet pay, renewal | [Fermato](./detailed-storage-architecture/fermato) |
| Storage node rewards, staking context | [Adagio](./detailed-storage-architecture/adagio) |
| Why fragments and redundancy help privacy and speed | [Sharding](./detailed-storage-architecture/sharding) |

<br/>
