# FP-0002 — Design Token Reality Map v1

**Audit ID:** `home-style-baseline-01`  
**Authority:** `f5a9ecd7` — `:root` in `src/scss/style.scss` L71–161  
**Date:** 2026-06-26

---

## Classification key

| Class | Meaning |
|-------|---------|
| CANONICAL_TOKEN | Active CSS custom property in `:root`, used in production rules |
| REPEATED_LITERAL_CANDIDATE | Literal value repeats 3+ times; not yet tokenized |
| SECTION_LOCAL_VALUE | Scoped to one section family |
| ONE_OFF_VALUE | Single use or geometry exception |
| LEGACY_OR_UNUSED | Defined but unused or superseded |

---

## Token and value table

| Token / value | Current uses | Classification | Keep | Future action |
| ------------- | -----------: | -------------- | ---: | ------------- |
| `--font-family-base` | body, buttons | CANONICAL_TOKEN | Yes | — |
| `--font-family-heading` | headings | CANONICAL_TOKEN | Yes | — |
| `--font-family-display` | none found | LEGACY_OR_UNUSED | No | Remove only with operator |
| `--font-size-base` 18px | body, many blocks | CANONICAL_TOKEN | Yes | — |
| `--line-height-base` 24px | body | CANONICAL_TOKEN | Yes | — |
| `--font-size-h1` 46px | global h1 | CANONICAL_TOKEN | Yes | Hero overrides separately |
| `--font-size-h2` 36px | section H2s | CANONICAL_TOKEN | Yes | — |
| `--font-size-h3` 26px | step titles, support | CANONICAL_TOKEN | Yes | — |
| `--font-size-small` 14px | header meta, articles | CANONICAL_TOKEN | Yes | — |
| `--font-size-large` 20px | genotyping subhead | CANONICAL_TOKEN | Yes | — |
| `--font-size-nav` 16px | nav, some links | CANONICAL_TOKEN | Yes | — |
| `--font-size-button` 14px | `.btn`, review links | CANONICAL_TOKEN | Yes | — |
| `--container-main` 1230px | `.container` | CANONICAL_TOKEN | Yes | — |
| `--container-hero` 1380px | **0 references** | LEGACY_OR_UNUSED | No | Document; do not use until wired |
| `--pad-x` 30px | container desktop gutter | CANONICAL_TOKEN | Yes | — |
| `--pad-y` 50px | section rhythm | CANONICAL_TOKEN | Yes | — |
| `--pad-gap` 30px | grids, gaps | CANONICAL_TOKEN | Yes | — |
| `--pad-gap-line` 15px | mobile gutter, small gaps | CANONICAL_TOKEN | Yes | — |
| `--pad-gap-mini` 5px | button gap | CANONICAL_TOKEN | Yes | — |
| `--pad-gap-tight` 10px | minor | CANONICAL_TOKEN | Yes | Low use |
| `--pad-box` 20px | header | CANONICAL_TOKEN | Yes | — |
| `--color-page-background` | body | CANONICAL_TOKEN | Yes | — |
| `--color-text-primary` | text, borders, dark bands | CANONICAL_TOKEN | Yes | — |
| `--color-text-secondary` | muted copy | CANONICAL_TOKEN | Yes | — |
| `--color-accent` | accents, icons | CANONICAL_TOKEN | Yes | — |
| `--color-accent-hover` | button hover | CANONICAL_TOKEN | Yes | — |
| `--color-border-subtle` | dividers | CANONICAL_TOKEN | Yes | — |
| `--color-surface` | white surfaces | CANONICAL_TOKEN | Yes | — |
| `--color-surface-frosted` | hero panel base | CANONICAL_TOKEN | Yes | Panel uses literal 0.25 override |
| `--radius-main` 30px | cards, images, hero | CANONICAL_TOKEN | Yes | — |
| `--radius-input` 15px | inputs | CANONICAL_TOKEN | Yes | — |
| `--radius-full` 999px | buttons, dots, pills | CANONICAL_TOKEN | Yes | — |
| `--pad-btns` / `--main-size-btns` | buttons | CANONICAL_TOKEN | Yes | — |
| `--icon-size-small` 16px | icons | CANONICAL_TOKEN | Yes | — |
| `--icon-size-medium` 30px | icons | CANONICAL_TOKEN | Yes | Low frequency |
| `--transition-base` | links, nav | CANONICAL_TOKEN | Yes | — |
| `--surface-frosted-blur` 5px | hero panel | CANONICAL_TOKEN | Yes | — |
| **16px / 20px** | card body, steps, FAQ answer | REPEATED_LITERAL_CANDIDATE | Yes | Tokenize only if 3rd page adopts |
| **70px / 70px** | `.hero__title` | SECTION_LOCAL_VALUE | Yes | Keep local to hero |
| **38px / 38px** | `.hero__tagline` | SECTION_LOCAL_VALUE | Yes | Keep local |
| **30px / 34px** | `.home-final-form__heading` | SECTION_LOCAL_VALUE | Yes | — |
| **40px / 40px** | CTA phone | SECTION_LOCAL_VALUE | Yes | — |
| **5px** accent border | lead bars | REPEATED_LITERAL_CANDIDATE | Yes | Could become `--accent-bar-width` later |
| `$hero-panel-width` 600px | SCSS only | SECTION_LOCAL_VALUE | Yes | Hero SCSS vars — not CSS tokens |
| `#fff` literal | messenger pills | ONE_OFF_VALUE | Yes | Could use `--color-surface` |
| `rgba(255,255,255,0.25)` hero panel | overrides frosted token | ONE_OFF_VALUE | Yes | INTENTIONAL_OPERATOR_CALIBRATION |

---

## Invalidated assumptions

| Old assumption | Actual @ f5a9ecd7 |
|----------------|-------------------|
| Container desktop padding 50px | **30px** (`--pad-x`) |
| `--container-hero` drives hero width | Hero uses **1400px** literal max-width |
| Gallery captions overlay | **Below image** (operator Package #001 correction) |
| Separate SCSS partials per section | **Single** `style.scss` monolith |
| `.final-form` root class | **`.home-final-form`** only |

---

## Unused / low-use variables

- `--font-family-display` — no references
- `--container-hero` — defined, never referenced
- `--control-height-compact`, `--control-padding-inline-compact` — minimal/no use in home audit scope

---

## Tokenization recommended now

**None.** Operator rule: no new tokens without evidence and approval. Repeated 16/20 and 5px accent bar are **candidates only**.

---

## Source changes required for tokenization

Any future token extraction requires edits to `style.scss` — **not authorized** in this audit. Prefer alias classes (Strategy A) before new `:root` entries.

---

*End of design token reality map v1.*
