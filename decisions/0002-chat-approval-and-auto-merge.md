---
id: decision-0002
title: Chat approval and auto-merge while the director is the only member
status: approved
owner: Pavlo Babenko (Marketing Director)
decided: 2026-11-11
updated: 2026-11-11
amends: decision-0001
---

# 0002: Chat approval and auto-merge

## Context

Decision 0001 requires every change to `main` to go through a pull request approved by the director. While the director is the only member of the hub, opening and merging each PR by hand adds clicks without adding control. The director already reviews every block in the chat with the AI agent.

## Decision

While the director is the only member of the hub:

1. **Approval happens in the chat.** The director's explicit approval of a block in the chat (e.g. "ok", "approved", "merge") counts as approval.
2. **The AI agent merges.** After approval, the agent merges the block's branch into `main` with a merge commit (`--no-ff`). The merge commit message says `Approved by director in chat`. Branches stay small: one block, one branch.
3. **No merge without explicit approval.** If the director leaves comments, the agent revises on the same branch and waits for approval again.
4. **History stays readable.** Every block remains visible in git as a separate branch merge, so we can see what changed and when it was approved.

## When this ends

This decision stops applying once another person gets write access to the hub. From then on, the pull request flow from decision 0001, with CODEOWNERS and branch protection (Phase 5), applies again.
