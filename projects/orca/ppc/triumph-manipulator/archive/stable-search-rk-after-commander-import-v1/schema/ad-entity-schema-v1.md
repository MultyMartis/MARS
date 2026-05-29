# Ad Entity Schema v1

**Entity:** `Ad`  
**Role:** Yandex Search creative continuing **exact group intent**.  
**Parent:** `Group`

---

## Design rules

1. **Intent continuation** — user must feel «это именно то, что я искал» ([doctrine](../doctrine/generation-logic-v0.md)).  
2. **Keyword → headline alignment** — primary phrase in `headline_1` (bold-highlight doctrine).  
3. **Mobile-first readability** — short lines; no wall of text in H1.  
4. **Anti-generic** — forbidden vanity phrases without intent anchor.  
5. **Draft support** — ads may be `draft` until human publish.

---

## Field specification

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `entity_id` | string | yes | Stable internal ID |
| `parent_group_id` | string | yes | FK to group |
| `headline_1` | string | yes | Primary headline — main keyword anchor |
| `headline_2` | string | no | Secondary headline — geo or qualifier |
| `description` | string | yes | Continues H1; capability/use-case/trust |
| `display_url` | DisplayUrl | yes | Visible URL path |
| `fastlinks` | Fastlink[] | no | Up to platform max — intent-continuing only |
| `callouts` | string[] | no | Qualification/trust extensions |
| `cta_semantics` | CtaSemantics | yes | Commercial action intent |
| `keyword_alignment` | KeywordAlignment | yes | Traceability to cluster |
| `mobile_first_readability` | MobileReadability | yes | Structured mobile checks |
| `yandex_bold_highlight` | BoldHighlightMeta | yes | Bold-highlight continuation plan |
| `landing_url` | string | yes | Usually = group `landing_route.final_url` |
| `ad_status` | enum | yes | `draft` \| `active` |
| `notes` | string | no | Operator notes |

---

## `DisplayUrl`

| Field | Type | Required | Notes |
|-------|------|----------|-------|
| `domain` | string | yes | e.g. `triumph-krd.ru` |
| `path_1` | string | no | Commander path segment |
| `path_2` | string | no | Second segment |

Display URL is **not** a substitute for correct `landing_url`.

---

## `Fastlink`

| Field | Type | Required |
|-------|------|----------|
| `title` | string | yes |
| `description` | string | no |
| `url` | string | no — may inherit landing sections |

**Good:** `Перевозка бытовок`, `Манипулятор 5 т`, `Безналичный расчёт`  
**Bad:** `О компании`, `Главная`, `Наши услуги`

Max count: per [validation-schema-v1.md](validation-schema-v1.md) symbol rules + template.

---

## `CtaSemantics`

| Field | Type | Required | Values / notes |
|-------|------|----------|----------------|
| `primary_cta` | enum | yes | `call` \| `calculate` \| `order` \| `whatsapp` |
| `cta_phrase` | string | no | Visible CTA wording if used |
| `urgency_level` | enum | no | `high` \| `medium` \| `low` |
| `b2b_friendly` | boolean | no | Required true for B2B groups |

Must be coherent with group intent and landing blueprint CTA.

---

## `KeywordAlignment`

| Field | Type | Required |
|-------|------|----------|
| `primary_keyword` | string | yes | From group cluster `is_primary` or operator pick |
| `phrase_in_headline_1` | boolean | yes | Must be `true` for launch-ready |
| `phrase_in_description` | boolean | yes | Must be `true` for launch-ready |
| `phrase_in_fastlink` | boolean | no | Optional boost |
| `alignment_notes` | string | no | e.g. morphological variant allowed |

---

## `MobileReadability`

| Field | Type | Required | Rule |
|-------|------|----------|------|
| `h1_line_break_ok` | boolean | yes | H1 readable on narrow screen |
| `no_stuffed_keywords` | boolean | yes | No keyword spam |
| `description_scannable` | boolean | yes | Short clauses, not one endless sentence |
| `estimated_mobile_grade` | enum | no | `ok` \| `review` \| `fail` |

---

## `BoldHighlightMeta` (Yandex doctrine)

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `target_query` | string | yes | Query phrase expected to bold |
| `highlight_planned_in` | string[] | yes | Subset of `headline_1`, `headline_2`, `description`, `fastlinks` |
| `continuation_ok` | boolean | yes | Description continues highlighted concept |

**Rule:** Primary keyword phrase should appear in headline and description for relevance + bold behavior ([export foundation](../export/direct-commander-foundation-v0.md)).

---

## Symbol limits (validation contract)

Counts include **spaces and punctuation**. Exact limits are authoritative in Commander template annotations; validation schema uses these **default contract values** until template diff says otherwise:

| Field | Max chars (contract v1) | Truncation risk check |
|-------|-------------------------|------------------------|
| `headline_1` | 56 | required |
| `headline_2` | 30 | required if present |
| `description` | 81 | required |
| `fastlink.title` | 30 | per link |
| `callout` | 25 | per callout |
| `display_url` path segments | 20 | per segment |

**SAFE UNKNOWN:** If Yandex Direct UI changes limits, template + live import win over this table.

---

## Anti-generic guard (semantic)

Forbidden as **primary** H1 without intent anchor:

- Лучшие цены  
- Надёжная компания  
- Качественные услуги  
- Лидер рынка  

Full list: [validation-schema-v1.md](validation-schema-v1.md) § semantic.

---

## Minimal valid example (logical)

```yaml
entity_id: ad_grp03_a1_v1
parent_group_id: grp_03_bytovka_v1
headline_1: "Перевозка бытовок в Краснодаре"
headline_2: "Манипулятор на объекте"
description: "Перевозка и установка бытовок. Борт 5 т, стрела 14 м. Без посредников."
display_url:
  domain: triumph-krd.ru
  path_1: bytovka
fastlinks:
  - { title: "Манипулятор 5 т" }
  - { title: "Безналичный расчёт" }
callouts: ["Борт 5 т", "Стрела 14 м", "Работа по краю"]
cta_semantics:
  primary_cta: call
  urgency_level: high
keyword_alignment:
  primary_keyword: перевозка бытовки краснодар
  phrase_in_headline_1: true
  phrase_in_description: true
mobile_first_readability:
  h1_line_break_ok: true
  no_stuffed_keywords: true
  description_scannable: true
yandex_bold_highlight:
  target_query: перевозка бытовки
  highlight_planned_in: [headline_1, description]
  continuation_ok: true
landing_url: "https://example.ru/bytovka"
ad_status: draft
```

---

## Validation touchpoints

| Class | Checks |
|-------|--------|
| Structural | Required fields, parent group exists |
| Symbol | Per-field limits, truncation |
| Semantic | Alignment, anti-generic, fastlink quality |
| Commercial | CTA fit, capability truth |
| Continuation | `landing_url` matches group route |

---

## Export touchpoints

Ad fields map to Commander ad rows — [export-mapping-schema-v1.md](export-mapping-schema-v1.md). Exporter does **not** rewrite copy for alignment.
