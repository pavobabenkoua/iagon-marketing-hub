# Brand

Who Iagon is and how it sounds and looks. Core section: changes need the director's approval.

| Folder / file | What it holds |
|---|---|
| `strategy/` | Vision, mission, Compliance Gap, DNA anchors, values, purpose and promise, narrative, archetype, positioning |
| `messaging/` | Frames, core message, message box, audience variants, narratives, proof library, objections |
| `voice/` | Personality, borders, tone spectrum, writing principles, vocabulary, mechanics, voice test |
| `visual/` | Design system: colors, typography, logo, art direction, formats |
| `brandbook.yaml` | Order of the parts of the Brandbook Package |
| `open-items.md` | What still needs work |

## The Brandbook Package as one document

The parts above make up the Brandbook Package. To get it as one file:

```
python3 scripts/build-brandbook.py
```

Output: `dist/iagon-brandbook-package.md`. Edit the parts, never the built file.
