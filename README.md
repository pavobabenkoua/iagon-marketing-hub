# Iagon Marketing Hub

## What this is

The single source of truth for Iagon marketing: brand rules, products, audiences, data, channels, content series, campaigns and the way we work.

If it isn't in the hub, it isn't approved. If it's in the hub with `status: approved`, you can rely on it.

The hub is built for people and AI agents alike. People read it, AI agents help maintain it, and the Marketing Director approves every change.

## How it's organized

The hub follows the **LLM Wiki** pattern, with three layers:

| Layer | Folder | What it holds | Who writes |
|---|---|---|---|
| Raw sources | `raw/` | Notes, transcripts, stats exports, briefs | Anyone adds. Nobody edits. |
| Knowledge | `wiki/` | Structured, approved pages | AI drafts, the director approves |
| Rules | `AGENTS.md` | How AI agents work with the hub | The director |

Sections of `wiki/`: brand, products, audiences, data, channels, series, campaigns, partners, playbooks.

Key files:
- [`index.md`](index.md): map of every page. Start here.
- [`wiki/resources.md`](wiki/resources.md): decks, brandbook and other files that live outside GitHub.
- [`log.md`](log.md): what changed and when.
- [`decisions/`](decisions/): why the hub works the way it does.
- [`templates/`](templates/): starting points for new pages.

## How to use it with AI

Open the repo in Claude Code or Cursor, or connect it to a Claude Project. The agent reads `AGENTS.md` automatically (Claude through `CLAUDE.md`).

You can talk to the agent in any language. Everything it writes into the hub, and every piece of content, is in English.

Example requests:

| You want to | Ask |
|---|---|
| Find an answer | *"What are our messaging pillars for developers?"* |
| Add new material | *"Ingest the file in raw/inbox and update the hub."* |
| Write content | *"Write an X thread for the Würth series, post 5."* |
| Check the hub's health | *"Run a lint on the hub."* |

**The agent checks relevance first.** Before it adds material or writes content, it tells you whether the input is relevant to Iagon, whether it fits the brand and the series logic, what it overlaps with, and what it suggests changing. Work starts after you agree.

## How to add knowledge

- **Easiest:** drop the file into `raw/inbox/` and ask the agent to ingest it.
- **By hand:** copy a template from `templates/`, fill it in, add the page to `index.md`.
- **A file outside GitHub** (deck, Figma, Drive folder): add a row to `wiki/resources.md`.

## Rules in one screen

1. **English** in everything written into the hub.
2. **The director approves** every change to `main`. For now that happens in the chat ([0002](decisions/0002-chat-approval-and-auto-merge.md)).
3. **Nothing is invented.** Every number and claim has a source. Numbers come only from `wiki/data/`.
4. **Nothing is deleted.** Outdated pages get `status: deprecated`.
5. **No secrets** in the repo: no passwords, keys, tokens or ad-account access.

## Glossary of hub terms

| Term | Meaning |
|---|---|
| **Relevance check** | The agent's first step: is this relevant, does it fit, what should change |
| **Ingest** | Turning a raw file into updates of hub pages |
| **Query** | Asking the hub a question. Answers come from approved pages, with sources |
| **Lint** | A health check of the hub: missing metadata, unsourced numbers, contradictions, broken links |
| **Create** | Writing content (posts, threads, deck copy) based on the hub |
| **Status** | `draft`, `approved` or `deprecated` |
| **Visibility** | `public`, `team` (default) or `private` (never exposed through the API) |
| **ID** | A page's stable name, e.g. `product-insight`. It never changes |
