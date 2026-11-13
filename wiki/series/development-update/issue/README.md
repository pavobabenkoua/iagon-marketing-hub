# Issue templates

The fixed wording of every Monthly Recap issue. `scripts/monthly-recap.py` reads these files; edit the wording here, never in the script.

Each file has three parts separated by a line `=====`:

1. the opening,
2. the block for one area, repeated for every area in order of number of changes,
3. the close.

| Placeholder | Becomes |
|---|---|
| `[Month YYYY]` | `October 2026` |
| `[Month]` | `October` |
| `[Total]` | total number of changes |
| `[Areas]` | number of areas in words (`nine`) |
| `[Tweets]` | number of numbered tweets (areas + 1) |
| `[n]` | number of this tweet |
| `[Area]` | area name from the export |
| `[Lines]` | the picked lines as `- ` bullets |

Discord goes out as two messages: the opening and the first half of the areas, then the rest and the close.
