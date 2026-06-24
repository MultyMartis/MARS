# FP-0002 V7 — Recovery Life Implementation Decision

## Decision

```text
CREATE_ONE_NEW_PARTIAL
```

## Proof

- Reuse audit: all candidates `PARTIAL_SIMILARITY` or `NO_MATCH`; none `EXACT_100` / `SAME_DOM_DIFFERENT_CONTENT`.
- Figma section `77:4225` has unique heading, highlight band, intro, and 3 stage cards not represented by any existing partial.

## Selected path

`src/partials/sections/home-recovery-life.html`

## Rejected alternatives

| Partial | Reason rejected |
| ------- | ---------------- |
| `home-why-us.html` | Would duplicate unrelated services accordion; wrong heading; deforms block |
| `home-feature-grid.html` | 6-card grid semantics; wrong content slots; no background image band |

## Reused systems

- `.container`, global section padding rhythm
- Tokens: `--font-size-h2`, `--font-size-base`, `--font-size-large`, `--pad-gap`, `--pad-gap-line`, `--radius-main`, `--color-text-primary`, `--color-accent`, `--border-width`
- No new JS; no new button system

## New classes (required)

`.home-recovery-life`, `__content`, `__heading`, `__highlight`, `__intro`, `__intro-text`, `__stages`, `__stage`, `__stage-title`, `__stage-list`, `__stage-item`
