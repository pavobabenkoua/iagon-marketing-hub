# Posts

Posts that belong to no series: releases, announcements, one-off posts ([decision 0008](../../decisions/0008-series-types.md)). Posts in a series live in that series' `posts/` folder instead.

- One file per post, named `YYYY-MM-DD-slug.md` with the publication date.
- Start from `templates/post.md` and leave the `series` field empty.
- One post can go out on several channels: list each in `publications`.
