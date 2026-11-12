---
title: "Sharding"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---

Detailed Storage Architecture
# File Sharding

## Overview

In general, sharding is a method for horizontally splitting and distributing data across multiple storage providers in a decentralized network. In Iagon’s network, what gets distributed is ciphertext - your files are encrypted on the client first (see [Secure Lake](./secure-lake.md)); providers store opaque fragments, not plaintext.

Sharding provides:

- Stronger confidentiality at rest: No single provider necessarily holds a reconstructable plaintext file; storage node operators work with pieces that do not reveal content without your keys.
- Reduced risk of data loss: As more providers participate, the protocol can keep redundant copies of fragments so you can still retrieve a file when some nodes are unavailable.
- Faster downloads: When content is spread across many providers, the network can fetch fragments in parallel instead of hitting one bottleneck.

Earlier designs explored general-purpose content addressing (for example IPFS-style peer lookups). Iagon’s updated sharding and placement logic is part of its own storage and marketplace stack: where fragments live, how they are replicated or encoded for resilience, and how they are recovered or rebalanced are coordinated with subscription rules, node performance, and regional or jurisdiction preferences you configure alongside Secure Lake.

## Uploading a file

### From plaintext to ciphertext on your device

Before any sharding happens, the client encrypts the file. There is no "skip encryption" path for file bodies: storage node operators only ever handle ciphertext for those bodies, which is foundational to privacy. Very large files may be split into encrypted segments on the client so uploads can resume sensibly and memory use stays bounded; the network then distributes those segments or the resulting blobs according to policy.

### Redundancy on the network

The system may apply error-correcting or replication strategies to ciphertext fragments so that a subset of pieces is enough to rebuild a blob after loss or bit rot - without the server ever interpreting file content. The payload stays opaque to storage node operators.

### Distribute the fragments

Fragments are placed with storage providers that meet the consumer’s requirements - capacity, tier, geography, and other marketplace constraints - using performance and availability signals from the broader protocol stack, as summarized in the [high-level architecture](../high-level-architecture.md).

## Downloading a file

### Retrieve and reassemble

When you download, the client pulls the needed ciphertext fragments, confirms the upload is complete (you do not get a “finished” file from a half-uploaded object), and reassembles the layout the format expects.

### Decode and decrypt on the client

Any redundancy decoding happens on ciphertext. Decryption and integrity verification run on your device after the file is whole. Storage nodes do not decrypt user file bodies for you.

<br/>
