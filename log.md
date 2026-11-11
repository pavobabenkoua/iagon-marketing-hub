# Log

Chronological record of what changed in the hub, when and from which source. Newest entries on top.

Format: `## YYYY-MM-DD: type: short description`. Types: `ingest`, `update`, `structure`, `decision`, `lint`.

---

## 2026-11-12: update: Idle capacity proof
- Proof Library: "Idle capacity" entry (NRDC 2014; Koomey and Taylor 2015, 2017). Narrative 03 now points to it. Open item 2 closed.

## 2026-11-12: structure: partnership pipeline
- New private page `wiki/partners/pipeline.md`: stages concept → pilot → integration → production → closed, with external-mention rules.
- Würth (pilot), Fireblocks (integration), Cloud Court, Fortune 500, healthcare (concepts), Volksbank (closed).
- Positioning names only Würth and Fireblocks plus the pipeline. Open item 5 closed.

## 2026-11-12: update: Volksbank removed, Fireblocks source
- Volksbank removed from the brand pages: the partnership did not go ahead.
- Fireblocks 2400+ institutions sourced (fireblocks.com, 1 July 2026) and added to the Proof Library as the first external research entry. Open items 3 and 4 closed.

## 2026-11-12: update: Iagon Ecosystem Stats App frequency
- Confirmed: updates automatically every Cardano epoch (5 days). Positioning and proof library aligned, open item 7 closed.
- Positioning statement: "the only architecture" → "an architecture". Open item 8 closed.

## 2026-11-12: ingest: Brandbook Package, part 3 (Tone of Voice)
- 7 approved pages in `wiki/brand/voice/`. The Brandbook Package is fully in the hub.
- Edits: enterprise focus in the Composed and Rule 05 examples, "Figures as of [Day Month Year]" in the documentary example, numbers and dates on graphics defer to format pages, "The writer" label restored.
- `AGENTS.md`: Create now names the brand pages to follow.

## 2026-11-12: ingest: Brandbook Package, part 2 (Messaging System)
- 7 approved pages in `wiki/brand/messaging/`.
- Edits: pillar 01 and 04 proof, pillar 02 data vaults (no production claim), Fortune 500 must-hear and objection evidence aligned with the enterprise focus; primary audience register fixed; Proof Library carries placeholders for deployments and research (open item 1).

## 2026-11-12: ingest: Brandbook Package, part 1 (Brand Strategy)
- Source: [raw/archive/2026-11-12-iagon-brandbook-package.md](raw/archive/2026-11-12-iagon-brandbook-package.md) (Markdown export of the Google Doc).
- 8 approved pages in `wiki/brand/strategy/`, one per section of the original.
- "Visual Implications" moved to `wiki/brand/visual/art-direction.md`, aligned with the design system (Figtree only, actual palette).
- Edits approved by the director: Würth wording, Fireblocks scale as their reach, "Seven years later" → "Since then", enterprise focus instead of sector-by-sector deployment claims, thousands without separator in text, no long dashes.
- New: `wiki/brand/brandbook.yaml` (manifest), `scripts/build-brandbook.py`, `dist/iagon-brandbook-package.md`, `wiki/brand/open-items.md` (8 open items).

## 2026-11-12: decision: design system
- [0004](decisions/0004-design-system.md): Purple Shade `#7C75FF`, background `#F6F6FB`, Insight logo exception, minimum logo sizes, weights 400/600/700 only, format-specific bans.
- New approved pages: `brand/visual/colors-typography.md`, `brand/visual/logo.md`, three formats in `brand/visual/formats/`.
- 8 logo SVG files in `brand/visual/logos/`, including new light-background versions.
- Sources: Brand Guidelines v1.0, Claude Project docs `iagon-colors-design-rules.md`, `iagon-logo-svg-source.md`, `claude/iagon-insight-logo-svg.md`, `claude/industry-insights-card-spec.md`, `claude/wurth-series-context.md`, `claude/iagon-ecosystem-stats-earned-selfcontained.html`.

## 2026-11-11: structure: README and relevance check
- Full `README.md` with onboarding (block 1.5).
- New rule in `AGENTS.md`: a relevance check before every ingest and create. The agent reports relevance, fit, overlap, placement and proposed changes, then waits for agreement.

## 2026-11-11: structure: templates
- Nine templates in `templates/` (block 1.4): product, audience, channel, series, post, campaign, playbook, decision, fact.
- A post can be published on several channels. Each publication has its own date, URL and results.

## 2026-11-11: structure: rules for AI agents
- Full `AGENTS.md` (block 1.3): reading order, ingest / query / lint / create, approval, prohibitions, writing rules.
- No automatic staleness thresholds: the brand is stable.
- Added `CLAUDE.md` pointing to `AGENTS.md`.

## 2026-11-11: decision: metadata standard
- [0003](decisions/0003-metadata-standard.md): frontmatter fields, statuses, visibility, ID format, file naming (block 1.2).
- Added frontmatter to `wiki/resources.md`.

## 2026-11-11: decision: chat approval and auto-merge
- [0002](decisions/0002-chat-approval-and-auto-merge.md): while the director is the only member, approval happens in the chat and the AI agent merges.

## 2026-11-11: structure: hub skeleton created
- Folder structure set up (block 1.1).
- Added `wiki/resources.md` for files that live outside GitHub.

## 2026-11-11: decision: foundation
- [0001 Foundation](decisions/0001-foundation.md): English content, private repo on a personal account, director approves all logic changes.
