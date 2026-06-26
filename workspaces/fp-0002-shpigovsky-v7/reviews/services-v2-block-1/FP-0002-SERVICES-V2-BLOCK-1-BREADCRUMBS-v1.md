# FP-0002 — Services V2 Block 1 Breadcrumbs v1

**Date:** 2026-06-26

## Figma evidence

| Field | Desktop (`1:1363`) | Mobile (`1:4672`) |
| ----- | ------------------ | ----------------- |
| Layout | HORIZONTAL, gap 8 | HORIZONTAL, gap 2 |
| Size | 660×18 | 308×11 |
| Chain | `1:1364` / `1:1365` / `1:1366` | same labels |

## Visible chain

```text
Главная / Услуги лечения и профилактики
```

## Implementation

| Field | Value |
| ----- | ----- |
| Partial | `src/partials/components/breadcrumbs.html` |
| Placement | After hero, before subnav (`page-uslugi-v2__upper-nav`) |
| Home link | `/` |
| Current item | `Услуги лечения и профилактики` (no link) |
| Separator | `/` via CSS `::before` |
| Semantic HTML | `<nav aria-label="Хлебные крошки"><ol>…</ol></nav>` |

## V1 state

```text
MISSING — V2 restores component
```
