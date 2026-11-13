# Series

One folder per content series. Every series has a type ([decision 0008](../../decisions/0008-series-types.md)):

| Type | What it is | Example |
|---|---|---|
| `recurring` | A regular issue built from data; only the data changes | Development Update |
| `thematic` | One theme, every post written from scratch; `arc: true` when the order of posts matters | Würth × Iagon |
| `evergreen` | A set of reusable posts on rotation | Discord and YouTube invitations |

Articles are a format, not a type: they belong to a thematic series or stand alone. Posts outside any series live in [`wiki/posts/`](../posts/README.md).

## Folder

- `series.md`: idea, goal, narrative, boundary, format, cadence, rules, and the sections required for its type. Start from `templates/series.md`.
- `posts/`: one file per post, from `templates/post.md`. Texts as published, links, results.
- `learnings.md`: what worked, what didn't, what we change.

The point is to keep the logic of each series, not just an archive of texts.
