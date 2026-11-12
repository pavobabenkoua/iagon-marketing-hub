# Raw sources

Unprocessed material the wiki is built from: notes, call transcripts, stats exports, partner briefs, screenshots.

- `inbox/`: new material waiting for ingest.
- `docs-snapshots/`: dated copies of docs.iagon.com pages, written by `scripts/docs-snapshot.py` ([0005](../decisions/0005-docs-as-technical-source.md)).
- `archive/`: material already ingested. Name files with the date first: `2026-11-11-x-ads-results.csv`.

**Rules:** add files, never edit them. After an ingest, the file moves from `inbox/` to `archive/` and the ingest is recorded in `log.md`.
