# FP-0002 — Services Category Section Anatomy v1

**Date:** 2026-06-26  
**Method:** offline tree (`_fig-hub1405-tree.json`, `_fig-services-targeted.json`) + PNG

## Summary table

| Hub | Figma frame | Main groups | Service items | Descriptions | «Подробнее» links | Media | CTA | Decor |
| --- | ----------- | ----------: | ------------: | -----------: | ----------------: | ----: | --: | ----- |
| Зависимости и пристрастия | `1:1405` | 4 (heading, marker, services grid, gallery) | 4 | Yes (visible) | External-link icons on items | 3 gallery | Button instance | Section decor |
| Психическое здоровье | `1:1474` | 4+ | 6 | Figma lorem (excluded in V1) | Icons | 3 gallery | Button | Shared decor asset in V1 |
| Расстройства пищевого поведения | `1:1569` | 3 (compact) | 3 | Figma lorem (excluded) | Icons | **0** | Button | Decor |
| Генотипирование | `32:4586` | 2 (compact) | 1 | Lead = lorem (excluded) | Icon | **0** | Button | Decor |

## Per-section trees (desktop)

### 1. Зависимости (`1:1405`)

```text
3- Услуги
├── Заг н2 (icon + H2 + lead paragraphs)
├── Маркер (secondary lead band)
├── Services list (4× Пункт услуги with title + body + link icon)
├── Gallery row (3× Услуга image cards)
└── CTA button
```

### 2. Психическое здоровье (`1:1474`)

Same structural family as addictions; taller frame (1698 vs 1413) due to 6 service rows + gallery.

### 3. РПП (`1:1569`)

Compact hub: heading + leads + 3 services, **no gallery** — matches V1 `--no-gallery --compact`.

### 4. Генотипирование (`32:4586`)

Minimal: heading + single service link; **no lead paragraphs** in visible Figma text (lorem hidden).

## Shared structure?

**Visual pattern shared** (heading band, marker, list, optional gallery, CTA) but **not proven as single Figma component** — different heights, gallery presence, item counts, decor instances differ.

## V1 per-dimension classification

| Hub | STRUCTURE | CONTENT | GEOMETRY | ASSETS | RESPONSIVE | INTERACTION |
| --- | --------- | ------- | -------- | ------ | ---------- | ----------- |
| Addictions | PARTIAL_MATCH | MATCH | PARTIAL_MATCH | MATCH | PARTIAL_MATCH | MATCH |
| Mental health | PARTIAL_MATCH | PARTIAL_MATCH | PARTIAL_MATCH | MATCH | PARTIAL_MATCH | MATCH |
| Eating disorders | MATCH | PARTIAL_MATCH | MATCH | N/A | MATCH | MATCH |
| Genotyping | PARTIAL_MATCH | PARTIAL_MATCH | MATCH | N/A | PARTIAL_MATCH | MATCH |

## Root-cause verdict

```text
incorrect reuse assumption — single parameterized partial before per-hub anatomy proof
missing node during decomposition — breadcrumbs/submenu omitted upstream
editorial groups preserved for hub 1 only; hubs 2–4 names-only where Figma had lorem
decor wrapper geometry caused empty zones in early passes (partially fixed in final polish)
compact variants (hubs 3–4) supported by Figma — V1 partially implements
```

## Content/media omitted in V1

- Mental health + eating disorders per-service descriptions (intentional lorem exclusion)
- Genotyping lead paragraphs (lorem)
- Distinct decor assets per hub (V1 uses shared `services-hub-decor.webp`)
