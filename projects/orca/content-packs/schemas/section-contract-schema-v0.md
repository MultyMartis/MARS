# Section Contract Schema v0

## Purpose

Every landing section in a content pack is a **section contract** — structured semantics for export and Factory handoff, not HTML.

## Required fields (all sections)

| Field | Type | Description |
|-------|------|-------------|
| `section_id` | string | Canonical ID: `hero`, `specs`, `allowed_tasks`, `denied_tasks`, `order_flow`, `pricing`, `trust`, `b2b`, `faq`, `final_cta` |
| `section_order` | int | 01–10 |
| `section_title` | string | Human section name (RU) |
| `section_purpose` | string | Why this section exists on the page |
| `ppc_continuity` | string | How section continues ad intent |
| `seo_continuity` | string | H2/H3 intent support; no keyword stuffing note |
| `copy_blocks` | array | Ordered blocks — see below |
| `cta` | object | Primary/secondary targets |
| `proof_elements` | array | Trust, specs, ratings — evidence-backed only |
| `semantic_locks` | array | Strings or `{ field, locked: true }` |
| `safe_unknown` | array | Fields not verified — preserve in export |
| `frontend_notes` | string | Non-binding UI hints for Factory |
| `factory_implementation_notes` | string | v4 partial refs, anchor IDs, do-not-redesign |

## `copy_blocks[]` item

| Field | Type | Description |
|-------|------|-------------|
| `block_id` | string | e.g. `h1`, `subhead`, `bullet_1` |
| `block_type` | enum | `headline` \| `subhead` \| `body` \| `bullet` \| `chip` \| `faq_pair` \| `spec_row` \| `step` |
| `text` | string | Final Russian copy (or SAFE UNKNOWN placeholder) |
| `locked` | bool | If true, MODE 1 export must not alter |

## `cta` object

| Field | Description |
|-------|-------------|
| `primary_label` | e.g. `Рассчитать стоимость` |
| `primary_target` | e.g. `#contacts` |
| `secondary_label` | optional |
| `secondary_target` | optional |
| `tertiary_label` | optional (header CTA) |

## `proof_elements[]` item

| Field | Description |
|-------|-------------|
| `proof_type` | `spec` \| `rating` \| `review_source` \| `payment` \| `geo` |
| `text` | Claim text |
| `evidence_ref` | Path or SAFE UNKNOWN |

## Canonical section IDs

| order | section_id | section_title (default RU) |
|-------|------------|------------------------------|
| 01 | `hero` | Hero |
| 02 | `specs` | Параметры техники |
| 03 | `allowed_tasks` | Для каких задач подходит |
| 04 | `denied_tasks` | Что не перевозим |
| 05 | `order_flow` | Как заказать |
| 06 | `pricing` | Стоимость |
| 07 | `trust` | Доверие |
| 08 | `b2b` | Для организаций |
| 09 | `faq` | FAQ |
| 10 | `final_cta` | Финальный CTA |

## Example (minimal hero fragment)

```yaml
section_id: hero
section_order: 1
section_title: Hero
section_purpose: Мгновенное продолжение capability-интента с объявления
ppc_continuity: H1 и bullets = 5 т, 3 т, 14 м как в объявлении
copy_blocks:
  - block_id: h1
    block_type: headline
    text: "Манипулятор 5 тонн в Краснодаре"
    locked: true
semantic_locks:
  - "H1 must include 5 тонн + Краснодар"
safe_unknown: []
frontend_notes: "Single machine photo; no fleet collage"
factory_implementation_notes: "v4 screen-01-hero.html; remove hero-rate placeholder"
```

## Boundary

Contract shape only.
