# FP-0002 V9-06E24A Baseline Service Structured Sections Audit

**Wave:** V9-06E24A  
**Date:** 2026-07-08

## Operator reference vs resolved field

| Operator label | Resolved admin label |
|---|---|
| `Программа / условия` | `Пункты программы` (`programme_items`) |

No separate ACF field with label `Программа / условия` exists in source or runtime DB. Operator issue maps to the programme repeater inside **Service — Structured Sections**.

## ACF identity

| Property | Value |
|---|---|
| Group key | `group_fp02_service_structured_sections` |
| Group title | Service — Structured Sections |
| Field key | `field_fp02_programme_items_service` |
| Field name | `programme_items` |
| Type | repeater |
| Required (before) | 0 |
| Subfields | `title` (text), `text` (textarea) — both required 0 |

## Frontend usage

**Classification:** USED_FRONTEND

| Renderer | Behavior |
|---|---|
| `template-parts/service/program.php` | Reads `programme_items`; falls back to static V9 subdivision programme |
| `template-parts/service/approach.php` | Uses `programme_items` when non-empty |

Empty or partial rows do not break frontend; static fallback remains.

## Affected services (sample)

| ID | Title | Route | programme_items rows |
|---|---|---|---|
| 73 | Зависимости | `/uslugi/zavisimosti/` | 4 title-only rows |
| 74 | Лечение алкогольной зависимости | `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 4 title-only rows |

## E24 hero CTA relation

Unrelated. `hero_cta_label` lives in `group_fp02_service_layout_hero`. Values preserved on services 73/74.

Evidence: `validation/v9-06e24a-service-structured-sections-required-field-polish/baseline-service-structured-sections-audit.json`
