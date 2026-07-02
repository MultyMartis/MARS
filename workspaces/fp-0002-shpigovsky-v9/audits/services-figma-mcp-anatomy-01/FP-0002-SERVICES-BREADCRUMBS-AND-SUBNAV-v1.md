# FP-0002 — Services Breadcrumbs and Subnav v1

**Date:** 2026-06-26

## Breadcrumbs

| Field | Desktop | Mobile |
| ----- | ------- | ------ |
| Node ID | `1:1363` | SAFE UNKNOWN (inside `1:4625` — pending MCP) |
| Parent | `1:1311` (Inner Hero frame) | `1:4625` (per PNG) |
| Type | FRAME 660×18 | ~322×11 (forensic mobile pattern) |
| Chain (visible text) | `Главная` (`1:1364`) · `/` (`1:1365`) · `Услуги лечения и профилактики` (`1:1366`) | PNG: truncated trail |
| Separator | `/` text node | Same pattern assumed |
| Placement | **Below banner**, above tabs, still inside hero frame | Below hero image (PNG) |
| Classification | **INNER_PAGE_SHARED** (BLK-005) | — |

### V1 state

```text
PRESENT:  NO
MISPLACED: N/A
MERGED:   N/A
Verdict:  MISSING_COMPONENT
Root cause: incorrect reuse assumption — V1 reused hero-inner only; breadcrumbs never decomposed from target frame
```

### Semantic recommendation (future, no source change)

```html
<nav class="breadcrumbs" aria-label="Хлебные крошки">
  <ol class="breadcrumbs__list">
    <li class="breadcrumbs__item"><a href="/">Главная</a></li>
    <li class="breadcrumbs__item" aria-current="page">Услуги лечения и профилактики</li>
  </ol>
</nav>
```

## Page submenu / quick navigation

| Field | Value |
| ----- | ----- |
| Node ID | `1:1367` (`Табы`) |
| Parent | `1:1311` |
| Type | FRAME 1172×34 |
| Item components | 6× `Тэг` instances (`1:1368`–`1:1373`) |
| Item widths | 128, 204, 210, 113, 147, 134 px (labels from instance overrides — pending MCP text resolve) |
| Layout | Horizontal row, below breadcrumbs |
| PNG evidence | Pill/tab row with category shortcuts |
| Maps to categories? | **Yes** — 4 category sections + additional shortcuts (exact label→anchor map pending operator/XLSX) |

### Semantic role classification

```text
CATEGORY_SHORTCUTS + MIXED_NAVIGATION
(not global header nav — distinct from 1:1312 header links)
```

### V1 state

```text
MISINTERPRETED_AS_HUB_CONTENT: NO
MISSING: YES
Verdict: MISSING_COMPONENT
Root cause: page assembled from partial inventory before anatomy audit; submenu never identified as hero-frame sibling
```

## Spacing (approximate, offline)

| Gap | Evidence |
| --- | -------- |
| Banner bottom → breadcrumbs | Visible tight gap on PNG (~12–20px) |
| Breadcrumbs → tabs | ~8–16px |
| Tabs → Category 1 | Standard section padding (~50px desktop) |

Exact token values: **SAFE UNKNOWN** until MCP `get_design_context` on `1:1363`/`1:1367`.
