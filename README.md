# Iagon Marketing Hub

The single source of truth for Iagon marketing: brand rules, products, audiences, data, channels, content series, campaigns and the way we work.

The hub follows the **LLM Wiki** pattern:

| Layer | Folder | Who writes |
|---|---|---|
| Raw sources | `raw/` | Anyone adds. Nobody edits. |
| Structured knowledge | `wiki/` | AI drafts, the director approves via pull request |
| Rules (schema) | `AGENTS.md` | Director |

## Where to start

1. `index.md`: the map of every page in the hub.
2. `wiki/resources.md`: links to files that live outside GitHub (decks, brandbook, design sources).
3. `decisions/`: why the hub works the way it does.

## Ground rules

- All content is in **English**.
- Every change to `main` is approved by the Marketing Director. For now that happens in the chat with the AI agent ([decision 0002](decisions/0002-chat-approval-and-auto-merge.md)).
- Outdated pages are never deleted. Mark them `status: deprecated` so links keep working.

> Full onboarding guide comes in block 1.5.
