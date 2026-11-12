---
title: "Secure Lake"
# Sidebar/nav label is set in docs/.vitepress/sidebar.ts
---

Detailed Storage Architecture
# Secure Lake Technology

## Overview

Secure Lake is Iagon’s storage layer for encrypted, resumable file storage and sharing. Your files are encrypted on your own devices before anything is sent to the network. Storage node operators see ciphertext and opaque identifiers on the network, not file contents or readable file and folder names - so any potential breach of backend systems does not by itself expose what you stored or what you named it.

At the network layer, [sharding](./sharding.md) is a major part of that story: ciphertext is split and placed across storage providers so no single node need hold a complete reconstructable file without your keys, and the protocol can keep redundant fragments and fetch them in parallel - still without providers decrypting user file bodies.

That design supports real collaboration: subscriptions and automation, sharing with specific people, fine-grained permissions, and use from browsers, desktop apps, mobile apps, and APIs - including fully headless workflows when you need to script storage or pay without opening a graphical app (including flows that use your Cardano wallet where the product offers on-chain subscription and payment).

The sections below describe how Secure Lake works as a complete product: what it protects, how sharing and permissions behave, and how uploads and downloads stay reliable at scale.

## Privacy and Integrity

Encryption runs only on the client. File payloads do not leave your device as plaintext. Traffic and stored blobs are ciphertext; each file gets its own data encryption key, so a problem with one file does not drag down the rest. Confidentiality at rest is reinforced because what providers store is often fragmentary ciphertext spread by sharding rather than a single copy of a whole file on one disk.

When you decrypt, the software detects tampering, corruption, or truncation. You do not get a silently wrong file - if something is off, decryption fails in a clear way.

Very large files are handled with bounded memory: you can work with huge objects without loading an entire terabyte into RAM at once. Where needed, a large file may be represented as multiple encrypted segments derived from that file’s keys so uploads can resume at sensible boundaries while keeping a simple sharing model at the file level. Those segments (or the blobs derived from them) are then candidates for network distribution and redundancy under the same sharding rules that keep any one provider from seeing reconstructable plaintext.

## Organization, Names, and Search

You work in a normal folder hierarchy - nested folders and files the way you expect on a desktop. Names are protected too: the service stores opaque identifiers and encrypted naming material, not plaintext folder and file names sitting in databases where storage node operators could read them like a normal directory listing.

The server does not keep plaintext content hashes that could be used to fingerprint or correlate your data. Search runs over names you are allowed to see, using information available to your client after decryption - not by sending readable filenames to the server.

## Sharing Without Re-encrypting Bulk Data

When you share with someone, Iagon uses per-recipient access envelopes so the stored file data stays the same bytes on disk. The system is not forced to re-encrypt massive files for every new colleague. Revoking one person does not automatically strip others: each recipient’s access is carried in its own envelope.

Folders do not share a single key for everything underneath. Sharing a folder means envelopes for each file inside it, so each file keeps independent keying. When someone adds a new file to a folder that is already shared, the uploading client extends access to everyone who should already have that folder - new content is available without a manual “share again” step for every file.

The data encryption keys themselves are never exposed in plaintext on the server or on the wire in a form that storage node operators could use to decrypt your files.

## Two Layers of Access Control

Access is enforced in two independent layers that both matter:

1. On the server - policy decides who can reach a resource: list it, fetch ciphertext, create, rename, delete, and so on under your rules.
2. In the cryptography - envelopes decide who can unwrap keys and decrypt.

Someone with server access but no envelope might see that something exists (depending on listing rules) but cannot read names or content. Someone with an envelope but no server permission cannot pull the ciphertext. That defence in depth limits damage if either side is abused.

Permissions are granular: listing, creating, reading, writing, renaming, and deleting are separate ideas - giving one does not silently grant another.

Resources have an owning user and an owning group. People can belong to several named groups, with one primary group, so teams can share trees without hand-maintaining every file. Default is deny: new items are not visible to others until you say so.

## Inheritance, Expiry, Delegation, and Offboarding

Revoking access on a parent folder rolls through the tree so descendants do not keep stale rights that contradict the folder you just locked down. You can still share a single file more narrowly even when it sits deep inside a restricted area - the rules for how parent and child grants interact are consistent and predictable, so administrators and integrators know what to expect.

Grants can expire in time. They can also be limited by how many times they may be used, when the product exposes that - for example one-time style links.

You may delegate authority you hold to others, but never beyond what you already have. Delegation and sharing are built so clients can verify who added whom: the service cannot silently inject fake recipients into a folder’s access story. The system keeps a clear lineage of grants for audit and for revoking chains when someone leaves.

When a person offboards or loses access, operations can revoke everything they granted (including downstream) or reassign those grants - so access does not float ownerless. Important revocation and reassignment actions are recorded for compliance and troubleshooting.

## Uploads and Downloads

Interrupted uploads resume from the last confirmed position instead of starting over from byte zero. The server gives clients a reliable picture of progress so both sides agree where to continue. Downloads only complete for finished uploads - you do not get a “done” file that is still only partially written. When ciphertext is spread across providers, the client can often retrieve fragments in parallel and apply redundancy decoding on ciphertext before decrypting - consistent with the sharding model described above.

## Drives, Jurisdiction, Versions, Sync, and Automation

You can organise work into drives where data may live and how long versions are kept follow policies you set for that drive. Jurisdiction constraints help teams that must keep data in specific regions.

File history lets you restore earlier versions when your workflow needs rollbacks. Synchronisation keeps allowed data aligned across a user’s devices under the same policies.

Real-time events feed integrations and automation - hooks for the rest of your stack. Separately, you can allocate storage quota to other accounts without gaining access to what they put there - useful for admins and partners who should fund space but not read the contents.

## Open Clients, Solid Operations

Files you encrypt on one platform work on all supported platforms: the same cryptography and sharing semantics everywhere.

Independent developers can build compatible clients against Iagon’s documented client protocol - new platforms should not require secret server knowledge to interoperate.

Upload performance stays in line with what you would expect from fast encrypted transfers. Resumable uploads are designed to behave well through common proxies and CDNs. The storage nodes themselves hold opaque ciphertext - often as fragments placed through sharding; they do not branch on your file contents or unwrap your keys for you.

<br/>
