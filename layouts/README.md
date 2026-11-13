# Layouts

Approved graphic layouts as plain HTML and CSS ([decision 0007](../decisions/0007-approved-layouts-live-as-html.md)). One folder per format. Each folder is self-contained: open any `.html` file in a browser and it shows the layout with sample data.

| Folder | Format page | Script |
|---|---|---|
| [monthly-recap](monthly-recap/) | [Monthly recap cards](../wiki/brand/visual/formats/monthly-recap-cards.md) | `scripts/monthly-recap.py` |
| [weekly-cover](weekly-cover/) | [Weekly cover](../wiki/brand/visual/formats/weekly-cover.md) | `scripts/weekly-update.py` |

## Rules

- Rules live on the format page. The HTML implements them. If they differ, fix the HTML.
- Assets in `<format>/assets/`. Logos are linked from `wiki/brand/visual/logos/`.
- Values that change are marked `<!-- slot:name -->…<!-- /slot:name -->`. Scripts fill only these.
- No external requests: fonts are local, so a render is the same on every machine.

## Rendering

Scripts render with Playwright and Chromium: `pip install playwright && playwright install chromium`. Cards are rendered at 2× (a 1080 px card becomes a 2160 px PNG).

After every render the scripts run `scripts/layout-check.py` ([attention rules](../wiki/brand/visual/colors-typography.md#attention)): colors outside the palette and grayscale filters in the layout source; purple share, separate purple spots and purple-tinted decoration in each PNG; and a `<name>.squint.png` at feed size, sharp and blurred. It only reports: deviations go to the director with the layout. Run it by hand on any PNG: `python3 scripts/layout-check.py --layout layouts/<format> <file>.png`.

To change a layout visually: open it in a design canvas, get the change approved, then update the HTML here.
