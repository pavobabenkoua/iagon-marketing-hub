---
id: technology-storage
title: Storage
type: technology
status: draft
owner: Pavlo Babenko
updated: 2026-11-12
reviewed: 2026-11-12
visibility: team
sources:
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/storage-overview.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/subscription.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/high-level-architecture.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/detailed-storage-architecture/secure-lake.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/detailed-storage-architecture/sharding.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/detailed-storage-architecture/fermato.md
  - raw/docs-snapshots/2026-05-26/pages/iagon-storage/detailed-storage-architecture/adagio.md
related: [technology-overview, technology-nodes-and-staking, technology-key-figures, brand-message-box]
tags: [technology, storage, encryption, subscriptions]
---

# Storage

Docs: [Storage Overview](https://docs.iagon.com/iagon-storage/storage-overview) · [Secure Lake](https://docs.iagon.com/iagon-storage/detailed-storage-architecture/secure-lake) · [Sharding](https://docs.iagon.com/iagon-storage/detailed-storage-architecture/sharding) · [Fermato](https://docs.iagon.com/iagon-storage/detailed-storage-architecture/fermato) · [Subscriptions](https://docs.iagon.com/iagon-storage/subscription)

> **Status.** The Storage Overview carries an "Under Development" banner: the page describes what is being built, "on track to be available in Q1 2027". Copy must say "in development" or "coming in Q1 2027" for everything on this page except the subscription tiers, which describe the current offer.

## What the user gets

Familiar folders, files, sharing and quotas, while the data is encrypted on the user's device and served by independent storage providers rather than one company's data center.

- **Encrypted storage and sharing.** Files are encrypted before upload. Providers hold ciphertext.
- **A normal way to work.** Nested folders, drives placed by geography, file history, sync across devices, resumable uploads for very large files, event-driven integrations.
- **Fine-grained collaboration.** Share with people or groups, inheritance, expiry, predictable revocation.
- **Choice of subscription.** Website checkout or an on-chain subscription paid in crypto, tied to a wallet.

## Secure Lake: how privacy works

| Property | What the docs say |
|---|---|
| Where encryption runs | Only on the client. File bodies never leave the device as plaintext. |
| Keys | Each file has its own data encryption key. Keys are never exposed in plaintext on the server or on the wire. |
| Integrity | Decryption detects tampering, corruption or truncation and fails clearly. No silently wrong file. |
| Names and search | The server stores opaque identifiers and encrypted names, no plaintext names and no plaintext content hashes. Search runs on the client after decryption. |
| Sharing | Per-recipient access envelopes. Big files are not re-encrypted for each new recipient. Folders do not share one key: each file keeps its own. |
| Access control | Two independent layers: server policy (who can list, fetch, create, rename, delete) and cryptography (who can unwrap keys). Default is deny. Permissions are separate: granting one does not grant another. |
| Lifecycle | Revocation rolls down the folder tree. Grants can expire or be limited by use count. Delegation never exceeds the delegator's own rights. Offboarding revokes or reassigns everything a person granted. Revocations are recorded. |
| Large files | Bounded memory. Very large files are split into encrypted segments. Uploads resume from the last confirmed position. |
| Drives and jurisdiction | Per-drive policies for where data lives and how long versions are kept. Jurisdiction constraints for teams that must keep data in certain regions. |
| Admin | Storage quota can be allocated to other accounts without access to their content. |
| Open clients | Same cryptography on all platforms. Independent developers can build compatible clients from the documented protocol. |

**For marketing:** jurisdiction-aware drives, revocation records and quota without access map directly to the Compliance Gap message. These are the strongest enterprise proof points in the docs, and all are in development.

## Sharding

Ciphertext is split into fragments and placed with providers that match the consumer's requirements (capacity, tier, geography). The protocol may add error-correcting or replicated fragments so a subset is enough to rebuild a file. Downloads pull fragments in parallel. Decoding and decryption happen on the client.

Three stated benefits: no single provider holds a reconstructable file, lower risk of data loss, faster downloads.

Earlier designs used IPFS-style lookups. The current placement logic is Iagon's own.

## Fermato: on-chain subscriptions

A subscription can be an NFT locked in a Cardano smart contract instead of a row in a database. The user picks a plan, pays in ADA or stablecoin, and signs with a wallet. The backend sees the transaction and activates storage. Sign-in is a wallet challenge-response.

| | On-chain subscription | Traditional subscription |
|---|---|---|
| Record | NFT in a contract, publicly verifiable | Database entry, provider-controlled |
| Proof of purchase | Immutable transaction history | Receipt email |
| Resilience | Survives backend outages or data loss | Lost if the database fails |
| Authentication | Wallet signature | Username and password |

Both paths give access to the same storage. Status: in development.

## Subscription tiers (current offer)

Formula from the docs: price per tier = cost per GB × total GB + charges for services in the tier.

| Plan | Monthly | Annual | Storage |
|---|---|---|---|
| Basic | $2.20 | $24 | 500 GB |
| Iagonauts Basic | $2.20 | $24 | 1,000 GB |
| Standard | $11.00 | $120 | 2,000 GB |
| Iagonauts Standard | $11.00 | $120 | 4,000 GB |
| Business | $33.00 | $360 | 5,000 GB |
| Iagonauts Business | $33.00 | $360 | 10,000 GB |
| Enterprise | $115.50 | $1,260 | 15,000 GB |
| Iagonauts Enterprise | $115.50 | $1,260 | 30,000 GB |

- **Iagonauts** tiers give double storage for the same price to users who hold the required value of IAG. The docs state $0.20 of IAG held per GB.
- Data is deleted if an expired subscription stays unpaid for 3 months.
- Tier parameters may change for new purchases. Existing subscriptions are not affected.

**For marketing:** prices are consumer-scale. They do not carry the enterprise message. Do not lead with them in enterprise material.
