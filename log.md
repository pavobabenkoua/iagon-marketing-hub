# Log

Chronological record of what changed in the hub, when and from which source. Newest entries on top.

Format: `## YYYY-MM-DD: type: short description`. Types: `ingest`, `update`, `structure`, `decision`, `lint`.

---

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
