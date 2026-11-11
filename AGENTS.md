# AGENTS.md: rules for AI agents

These rules apply to every AI agent working with the Iagon Marketing Hub: Claude, Cursor, the future admin-panel bot and any other tool. Read this file in full before doing anything in the hub.

## 1. Role and priorities

- **The hub is the source of truth** for Iagon marketing. Answer and write from the hub, not from general knowledge about Iagon.
- **If the hub doesn't have it, say so.** "This isn't in the hub yet" is a correct answer. A guess is not.
- **Everything written into the hub, and every piece of content, is in English.** The chat with the director can be in any language.

## 2. Reading order

1. `index.md`: the map of the hub.
2. This file.
3. The section the task is about.

Always:
- Take numbers only from `wiki/data/`.
- Check wording against `wiki/brand/` (positioning, messaging, tone of voice, glossary).
- Check `wiki/resources.md` before saying a file doesn't exist. It may live outside GitHub.

## 3. Operations

### Relevance check: always first
Before any ingest or create, assess the material or the request and report back **before doing the work**:

1. **Relevance:** does it relate to Iagon marketing (our products, audiences, channels, positioning)?
2. **Fit:** is it consistent with `wiki/brand/` and with the logic of the series or campaign it belongs to?
3. **Overlap:** does it duplicate or contradict anything already in the hub? Name the pages.
4. **Placement:** which pages it would change or create.
5. **Proposed changes:** what should be adjusted to make it stronger or consistent: a different angle, wording that matches the glossary, a number that needs a source, a better place in the series arc.

End with a verdict: **Relevant**, **Partly relevant** (say which part) or **Not relevant** (say why and suggest what to do instead). Continue only after the director agrees. For trivial additions, such as a result number for a post that's already in the hub, keep the check to one line.

### Ingest: turn raw material into knowledge
1. Take a file from `raw/inbox/` and run the relevance check.
2. Find every page it affects. Update existing pages first. Create a new page only when no page fits.
3. Add the source to each changed page's `sources` and update `updated`.
4. Add new pages to `index.md`. Add one entry to `log.md` with the type `ingest`.
5. Move the file to `raw/archive/`, with the date first in the name.
6. Give the director a short summary: which pages changed, what is new, what contradicts existing content. Wait for approval.

### Query: answer from the hub
- Answer from pages with `status: approved`. Content from `draft` pages must be labeled as draft.
- Name the files the answer comes from.
- If the answer isn't in the hub, say so and offer to add it.
- If an answer is useful beyond this one question, offer to save it as a page.

### Lint: health check
Report, don't fix silently. The report lists:
- pages without frontmatter or with missing required fields ([0003](decisions/0003-metadata-standard.md));
- numbers and claims without a source;
- contradictions between pages (different numbers, different wording of the same message);
- pages missing from `index.md`;
- broken links and unknown IDs in `related`;
- duplicated content that should be a link instead;
- terms that break the glossary.

Record the lint in `log.md` with the type `lint`, then propose fixes as a normal block for approval.

### Create: write content for Iagon
When writing posts, threads, articles, deck copy, ads or any other content:
- Run the relevance check on the request first. If the brief is off-brand, off-series or weaker than it could be, say so and propose the change before writing.
- Follow `wiki/brand/`: positioning, messaging pillars, tone of voice, glossary. Brand rules are not optional.
- Use only numbers from `wiki/data/`. If a needed number isn't there, leave a visible placeholder (`[NUMBER: what is needed]`) instead of inventing one.
- If the content belongs to a series, read `series.md` and the previous posts first. Respect the series arc and rules.
- Follow the rules of the target channel in `wiki/channels/`.
- For any visual: follow `wiki/brand/visual/` (colors, typography, logo) and the format page in `wiki/brand/visual/formats/` if one exists. Use logo files from `wiki/brand/visual/logos/`, never redraw them.
- Content drafts are not hub pages. Save a post to the hub only when it is published or when the director asks.

## 4. Changes and approval

- Work on a branch, **one block per branch**. Never commit directly to `main`.
- Merge into `main` only after the director's explicit approval in the chat, with a `--no-ff` merge commit that says `Approved by director in chat` ([0002](decisions/0002-chat-approval-and-auto-merge.md)).
- In every summary, separate the two kinds of change:
  - **Logic changes:** brand, positioning, rules, numbers, structure, series logic.
  - **Log additions:** new posts, results, learnings, raw files.
- Every page follows the metadata and naming standard ([0003](decisions/0003-metadata-standard.md)).

## 5. Never

- Invent numbers, quotes, partners, customers, dates or roadmap items.
- Edit files in `raw/`.
- Delete pages. Set `status: deprecated` and link to the replacement.
- Store passwords, API keys, tokens or ad-account access anywhere in the repo.
- Change `visibility: private` to `team` or `public` without the director's explicit approval.
- Commit directly to `main`.

## 6. How to write hub pages

- Short, plain, unambiguous sentences. One idea per paragraph.
- **One fact lives in one place.** Link to it instead of copying it.
- Every claim has a source in `sources` or a link to the page it comes from.
- Use relative Markdown links between pages and IDs in `related`.
- Start new pages from `templates/`.
