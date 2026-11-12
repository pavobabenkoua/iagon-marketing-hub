---
id: decision-0005
title: docs.iagon.com as the technical source
type: decision
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-12
updated: 2026-11-12
---

# 0005: docs.iagon.com as the technical source

## Context

docs.iagon.com holds the technical description of the ecosystem: architecture, node economics, tokenomics, on-chain identifiers, product pages. Marketing needs these facts every day, and they must match what the docs say. The docs are written by another team and change over time. Marketing can read the docs repository but cannot connect it to the hub or edit it.

World practice for this situation is "single source, reference, don't fork": technical facts have one owner (the docs), downstream teams cite them with a version, and changes flow back as change requests to the owner instead of silent local edits.

## Decision

1. **The docs own technical facts. The hub owns how marketing uses them.** The hub never invents or "improves" a technical number. If the docs and the hub disagree, the docs win until the docs team confirms a change.
2. **Dated snapshots.** Each time a fresh export of the docs repository is uploaded, `scripts/docs-snapshot.py` stores the English Markdown pages in `raw/docs-snapshots/<YYYY-MM-DD>/`. The date is the date of the docs state (last commit in the export), not the upload date. Snapshots are immutable like everything in `raw/`. Images, Japanese pages and the `.archive/` folder are not copied.
3. **Change report.** The script compares the new snapshot with the previous one and writes `CHANGES.md`: pages added, removed and changed, navigation changes, and every wiki page whose `sources` cite a changed page. Those wiki pages are re-checked in the same block.
4. **Every technical page cites its docs pages.** `sources` lists the snapshot paths. The page body links to the live docs URL so colleagues can open the current version.
5. **Status labels on every fact.** `Live`, `In development`, `Planned` or `Legacy`, as the docs state them. Marketing copy may present only `Live` facts as current. Everything else needs "in development" or "planned" wording.
6. **Feedback goes back as ready text.** Errors, stale passages and brand mismatches found in the docs go to `wiki/technology/docs-feedback.md` with the exact replacement text, so anyone with docs access can apply them. The hub does not wait for the fix: it records the correct fact and flags the docs passage.
7. **New page type `technology`** is added to the list in [0003](0003-metadata-standard.md) for pages in `wiki/technology/`.

## Consequences

- Refresh procedure: download the docs repository as ZIP, upload it, run the script, review `CHANGES.md`, update the affected pages, log the ingest.
- The Proof Library may promote a technical fact from `wiki/technology/` to a canonical phrasing. The technical page stays the source for the number.
- The snapshot in this block (2026-05-26) is the state of the export that was uploaded. If the live site changed after that date, the next export will show it.
