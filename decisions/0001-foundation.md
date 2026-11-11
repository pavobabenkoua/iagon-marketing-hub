---
id: decision-0001
title: Foundation of the Iagon Marketing Knowledge Base
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-11
updated: 2026-11-11
---

# 0001 — Foundation

## Context

Iagon marketing knowledge (brand rules, product briefs, data, campaigns, content series logic) is spread across chats, project docs and files. We need one source of truth that people can read and AI agents can maintain, following the **LLM Wiki** pattern: raw sources → AI-maintained structured wiki → schema of rules (`AGENTS.md`).

Later the repo will feed an internal admin panel and an API for colleagues who have no repo access. The repo stays the source of truth; every other interface reads from it.

## Decisions

### 1. Language
- **All repo content is in English**: files, metadata, commit messages, PR titles and descriptions.
- Chat with AI agents can happen in any language, but anything written into the repo, along with every content request and every content output, is in English.

### 2. Location and name
- Repo: `pavobabenkoua/iagon-marketing-hub`, **private**.
- It lives on the director's personal GitHub account for now. It may move to the `IagonAS` organization later. GitHub keeps redirects on transfer, so the move is low-risk.

### 3. Ownership and approval
- **Single owner for now:** Pavlo Babenko owns every section.
- **Any change to logic** (brand, positioning, rules, data, structure, series logic) needs the director's approval through a pull request.
- Direct pushes to `main` are not allowed once branch protection is set up (Phase 5).
- Access for other colleagues and per-section owners will be defined later (Phase 6).

### 4. Way of working
- We build the repo phase by phase and block by block. Each block goes through: AI drafts → director reviews → revisions → approval → next block.
- AI agents work through branches and pull requests, never directly on `main`.

## Consequences
- One person approving everything is fine at this stage. This decision must be revisited before colleagues join, so the director doesn't become a bottleneck.
- English-only content keeps the base ready for international colleagues, agencies and the future API.
