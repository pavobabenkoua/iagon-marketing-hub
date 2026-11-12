# Technology

What Iagon is technically, in facts marketing can use. The source is docs.iagon.com ([decision 0005](../../decisions/0005-docs-as-technical-source.md)). This section does not replace the docs: it selects what matters for marketing, marks the status of each fact, and records where the docs are wrong or out of date.

**Current snapshot: 2026-05-26** (state of the docs export uploaded on 2026-11-12). Files: `raw/docs-snapshots/2026-05-26/`.

## Pages

| Page | What it covers |
|---|---|
| [Overview](overview.md) | The protocol in one page: components, how they connect, what is live |
| [Storage](storage.md) | Secure Lake, sharding, subscriptions and pricing |
| [Nodes and staking](nodes-and-staking.md) | Node requirements, the 10-tier system, staking formula, rewards, fees, delegation, Borrow Stake, Cyclone |
| [Compute](compute.md) | Compute architecture, requirements, pricing, rewards; status |
| [Token and on-chain](token-and-onchain.md) | IAG supply, allocations, utility, on-chain identifiers, LSPO |
| [Products](products.md) | Every product the docs describe, with status |
| [Key figures](key-figures.md) | Every number in one table, with status and whether it can be quoted |
| [Terminology](terminology.md) | The docs vocabulary and how marketing uses it |
| [Docs feedback](docs-feedback.md) | Errors, stale passages and brand mismatches in the docs, with replacement text |

## Rules

1. **The docs own the number.** Do not round, restate or "improve" a technical figure. Copy it from [Key figures](key-figures.md), which points to the docs page.
2. **Status before use.** `Live` facts may be stated as current. `In development` and `Planned` facts need that wording in copy ("in development", "planned for Q1 2027"). `Legacy` facts are not used. **Exception:** the compliance claims of the brand (Message Box, Core Message, Boilerplate) are worded as in the approved Brandbook Package, by the director's decision (2026-11-12).
3. **Network metrics are not here.** Nodes, countries, capacity and staked IAG change every epoch. They come from the Ecosystem Stats App with "figures as of [date]" ([Proof Library](../brand/messaging/proof-library.md)).
4. **Technical is not the headline.** These facts are proof under a business message, not the message ([Vocabulary](../brand/voice/vocabulary.md): decentralization is how the promise is kept, not why anyone buys).
5. **Found a problem in the docs?** Add it to [Docs feedback](docs-feedback.md) with replacement text. Do not wait for the fix: write the correct fact here.

## Refreshing the snapshot

1. Download the docs repository as ZIP (GitHub: Code → Download ZIP) and upload it.
2. Unpack it into an empty folder outside the hub.
3. Run `python3 -I scripts/docs-snapshot.py <unpacked>/documentation/docs --date <date of last commit>`.
4. Read `raw/docs-snapshots/<date>/CHANGES.md`. It lists changed pages and the wiki pages that cite them.
5. Update those pages: facts, `sources` to the new snapshot, `updated` and `reviewed`. Log the ingest.
