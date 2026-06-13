# Website Factory — Validation Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/page-block-validation/`  
**Статус:** канонический контракт полей validation run — **documentation only**  
**Связь:** [PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md), [PAGE-BLOCK-VALIDATION-RULES-v1.md](PAGE-BLOCK-VALIDATION-RULES-v1.md)

**Не является:** JSON Schema, OpenAPI spec, runtime API, database record

---

## Назначение

Validation Contract v1 задаёт **обязательные поля** для одного validation run (одна страница или один Blueprint scope). Используется operator checklist **сейчас**; будущие validators **обязаны** emit compatible structure.

---

## Input fields (validation target)

### `validation_target`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Идентификация объекта проверки |
| **Обязательные subfields** | `site_type_code`, `page_type`, `page_id` or URL slug, `blueprint_ref` |
| **Пример** | `{ site_type_code: "LANDING", page_type: "LANDING_PAGE", page_id: "primary", blueprint_ref: "LANDING-BLUEPRINT-v1" }` |
| **Rule** | `site_type_code` ∈ [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) Core Types for v1 |

---

### `required_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Ordered list `block_id` **ожидаемых** на странице после resolve rules |
| **Источник** | [PAGE-BLOCK-MAPPING-v1.md](../block-registry/PAGE-BLOCK-MAPPING-v1.md) + [CORE-PAGE-ARCHITECTURES-v1.md](../page-architecture/CORE-PAGE-ARCHITECTURES-v1.md) + OR-group expansion |
| **Формат** | Array of UPPER_SNAKE_CASE strings |
| **Пример** | `["HERO", "BENEFITS", "PROCESS", "FAQ", "LEAD_FORM", "CTA", "CONTACTS", "FOOTER", "LEGAL_LINKS"]` |
| **Rule** | Must include all REQUIRED stances for `page_type`; OR-groups documented as `required_block_groups` in project notes (v1 manual) |

---

### `optional_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Allow-list `block_id` — presence **не влияет** на PASS/FAIL |
| **Источник** | OPTIONAL cells in PAGE-BLOCK-MAPPING-v1 |
| **Пример** | `["PRICING", "CASES", "MAP"]` |
| **Rule** | Blocks present in stack but **not** in required, optional, or forbidden → `unexpected_blocks` |

---

### `forbidden_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | `block_id`, которые **не должны** присутствовать на странице |
| **Источник** | FORBIDDEN cells in PAGE-BLOCK-MAPPING-v1 + Blueprint exclusions + Page Contract |
| **Пример** | `["CART", "CHECKOUT", "CATEGORIES", "PRODUCT_GRID"]` on `LANDING_PAGE` |
| **Rule** | Presence of any forbidden block → validation FAIL (severity per block — see severity system) |

---

## Output fields (validation result)

### `validation_result`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Structured outcome of the run |
| **Обязательные subfields** | `missing_blocks`, `unexpected_blocks`, `warnings`, `status` |
| **Rule** | Single run → single `validation_result` object |

---

### `missing_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | `block_id` from `required_blocks` **absent** from actual stack |
| **Формат** | Array of `{ block_id, severity }` |
| **Пример** | `[{ "block_id": "LEAD_FORM", "severity": "ERROR" }]` |
| **Rule** | OR-group partial satisfaction: list group id if **no** member present |

---

### `unexpected_blocks`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | `block_id` present in actual stack but **not** in required ∪ optional for this page_type |
| **Формат** | Array of `{ block_id, severity, reason }` |
| **Пример** | `[{ "block_id": "CART", "severity": "CRITICAL", "reason": "FORBIDDEN on LANDING_PAGE" }]` |
| **Rule** | FORBIDDEN blocks listed here **and** drive `status` = FAIL |

---

### `warnings`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Non-blocking issues — recommended blocks missing, registry gaps, OR-group ambiguity |
| **Формат** | Array of `{ code, message, severity }` |
| **Пример** | `[{ "code": "MISSING_RECOMMENDED", "message": "FAQ optional on HOME_PAGE but recommended for PROMO", "severity": "WARNING" }]` |
| **Rule** | Warnings alone → `status` may be `PASS_WITH_WARNINGS` |

---

### `status`

| Значение | Условие |
|----------|---------|
| **PASS** | All REQUIRED present; no FORBIDDEN present; no ERROR/CRITICAL in missing/unexpected |
| **PASS_WITH_WARNINGS** | PASS conditions met + ≥1 WARNING |
| **FAIL** | Any CRITICAL missing/forbidden; or any ERROR missing/forbidden per rules |

**Gate:** `FAIL` → halt before Design/Frontend. `PASS_WITH_WARNINGS` → operator documents decision.

---

## Example contract (PASS)

```yaml
validation_target:
  site_type_code: LANDING
  page_type: LANDING_PAGE
  page_id: primary
  blueprint_ref: LANDING-BLUEPRINT-v1

required_blocks:
  - HERO
  - BENEFITS
  - PROCESS
  - FAQ
  - LEAD_FORM
  - CTA
  - CONTACTS
  - FOOTER
  - LEGAL_LINKS

optional_blocks:
  - PRICING
  - FEATURES
  - CASES
  - TESTIMONIALS
  - CERTIFICATES
  - MAP

forbidden_blocks:
  - CART
  - CHECKOUT
  - CATEGORIES
  - PRODUCT_GRID
  - SERVICES

actual_blocks:  # operator-collected or future scanner
  - HERO
  - BENEFITS
  - PROCESS
  - TRUST
  - FAQ
  - LEAD_FORM
  - CTA
  - CONTACTS
  - FOOTER
  - LEGAL_LINKS

validation_result:
  missing_blocks: []
  unexpected_blocks: []
  warnings: []
  status: PASS
```

---

## Example contract (FAIL)

```yaml
validation_target:
  site_type_code: LANDING
  page_type: LANDING_PAGE
  page_id: primary
  blueprint_ref: LANDING-BLUEPRINT-v1

required_blocks: [HERO, BENEFITS, PROCESS, FAQ, LEAD_FORM, CTA, CONTACTS, FOOTER, LEGAL_LINKS]
forbidden_blocks: [CART, CHECKOUT]

actual_blocks:
  - HERO
  - BENEFITS
  - PROCESS
  - CART
  - CONTACTS
  - FOOTER

validation_result:
  missing_blocks:
    - { block_id: LEAD_FORM, severity: ERROR }
    - { block_id: FAQ, severity: WARNING }
    - { block_id: CTA, severity: ERROR }
  unexpected_blocks:
    - { block_id: CART, severity: CRITICAL, reason: FORBIDDEN on LANDING_PAGE; Blueprint reclassify to ECOMMERCE }
  warnings:
    - { code: OR_GROUP_SOCIAL_PROOF, message: TRUST or TESTIMONIALS — neither present, severity: ERROR }
  status: FAIL
```

---

## Relationship to Page Contract

| Page Contract field | Validation Contract field |
|---------------------|---------------------------|
| `page_type` | `validation_target.page_type` |
| `required_blocks` | Input to compare; must **match or superset** resolved REQUIRED from mapping |
| `optional_blocks` | Subset of mapping OPTIONAL |
| `forbidden_blocks` | Must **match or superset** mapping FORBIDDEN |

Page Contract authored **before** validation; validation **verifies** contract against authoritative mapping.

---

## SAFE UNKNOWN

- JSON Schema for this contract — **not defined** (see VALIDATION-GAPS-v1)
- `required_block_groups` formal syntax — **manual v1**; formal schema **FUTURE**
- Multi-page batch validation envelope — **FUTURE**

---

*Validation Contract version: v1. Canonical location: `workspaces/website-factory-reference-v1/page-block-validation/`.*
