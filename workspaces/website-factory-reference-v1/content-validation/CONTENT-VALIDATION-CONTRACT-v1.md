# Website Factory — Content Validation Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/content-validation/`  
**Статус:** канонический контракт полей content validation run — **documentation only**  
**Связь:** [CONTENT-VALIDATION-RULES-v1.md](CONTENT-VALIDATION-RULES-v1.md), [content-contracts/CONTENT-CONTRACT-v1.md](../content-contracts/CONTENT-CONTRACT-v1.md)

**Не является:** JSON Schema, OpenAPI spec, runtime API, CMS record, generated copy payload.

---

## Назначение

Content Validation Contract v1 задаёт **обязательные поля** для одного content validation run (block scope или page scope). Используется operator checklist **сейчас**; будущие validators **обязаны** emit compatible structure.

---

## Mandatory fields (single run)

### `validation_target`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Идентификация объекта проверки |
| **Обязательные subfields** | `scope` (`BLOCK` \| `PAGE` \| `LEGAL_ROUTE`), `site_type_code`, `page_type`, `blueprint_ref` |
| **Условные subfields** | `block_id` (required when `scope` = `BLOCK`), `page_id` or URL slug, `legal_document_ref` (when `LEGAL_ROUTE`) |
| **Пример (block)** | `{ scope: "BLOCK", site_type_code: "LANDING", page_type: "LANDING_PAGE", block_id: "HERO", blueprint_ref: "LANDING-BLUEPRINT-v1" }` |
| **Rule** | `site_type_code` ∈ Core 5 for v1 matrix; `page_type` ∈ PAGE-TYPE-REGISTRY-v1 (10); `block_id` ∈ BLOCK-REGISTRY-v1 (29) |

---

### `site_type_code`

| Атрибут | Требование |
|---------|------------|
| **Формат** | UPPER_SNAKE_CASE from Site Type Registry |
| **v1 values** | `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Rule** | Drives SITE-TYPE-CONTENT-MAPPING overlays and commerce path rules |

---

### `page_type`

| Атрибут | Требование |
|---------|------------|
| **Формат** | UPPER_SNAKE_CASE from Page Type Registry |
| **v1 count** | **10** — no extensions in validation v1 |
| **Rule** | Must be allowed for `site_type_code` per PAGE-TYPE-REGISTRY + SITE-TYPE-PAGE-MATRIX |

---

### `block_id`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Target block when `validation_target.scope` = `BLOCK` |
| **Формат** | UPPER_SNAKE_CASE — one of 29 registry ids |
| **Rule** | Omit or `null` for pure page-level runs; required for block runs |
| **Gate** | Do not validate signals for `block_id` marked FORBIDDEN on page by page-block validation |

---

### `required_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Ordered list of `signal_id` **ожидаемых** после resolve rules |
| **Источник** | BLOCK-CONTENT-CONTRACTS + PAGE-CONTENT-CONTRACTS + SITE-TYPE-CONTENT-MAPPING (merged) |
| **Формат** | Array of lowercase snake_case strings from CONTENT-SIGNAL-REGISTRY-v1 |
| **Пример** | `["offer", "benefit", "cta"]` for `HERO` |
| **Rule** | Union of block required + applicable page required; dedupe |

---

### `optional_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Allow-list `signal_id` — presence improves completeness; absence alone ≠ FAIL |
| **Источник** | optional columns in content contracts |
| **Пример** | `["proof", "trust", "urgency"]` on `HERO` |
| **Rule** | Signals present but not in required ∪ optional → listed in `unexpected_signals` |

---

### `forbidden_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | `signal_id`, которые **не должны** быть bound в scope |
| **Источник** | forbidden columns in BLOCK/PAGE contracts + site-type forbidden patterns |
| **Пример** | `["consent", "payment", "legal_disclosure"]` on `HERO` |
| **Rule** | Presence of any forbidden signal → contributes to FAIL (severity per CONTENT-SEVERITY-SYSTEM-v1) |

---

## Result fields (output)

### `missing_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | `signal_id` from `required_signals` **not satisfiable** in architecture declaration |
| **Формат** | Array of `{ signal_id, severity, block_id? }` |
| **Пример** | `[{ "signal_id": "offer", "severity": "ERROR", "block_id": "HERO" }]` |
| **Rule** | OR-group: document group id if no member satisfiable (manual v1) |

---

### `unexpected_signals`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | `signal_id` bound in scope but not in required ∪ optional |
| **Формат** | Array of `{ signal_id, severity, reason }` |
| **Пример** | `[{ "signal_id": "payment", "severity": "CRITICAL", "reason": "FORBIDDEN on HERO / LANDING_PAGE" }]` |
| **Rule** | Forbidden signals listed here **and** drive FAIL when severity ≥ ERROR |

---

### `warnings`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Non-blocking issues — optional signal absent, evidence_rule not yet documented, site-type soft gap |
| **Формат** | Array of `{ code, message, severity }` |
| **Пример** | `[{ "code": "MISSING_OPTIONAL_PROOF", "message": "proof optional on HERO but recommended for LANDING", "severity": "WARNING" }]` |
| **Rule** | Warnings alone → `status` may be `PASS_WITH_WARNINGS` |

---

### `status`

| Значение | Условие |
|----------|---------|
| **PASS** | All required signals satisfiable; no forbidden present; no ERROR/CRITICAL in missing/unexpected |
| **PASS_WITH_WARNINGS** | PASS conditions met + ≥1 WARNING (no ERROR/CRITICAL) |
| **FAIL** | Any CRITICAL missing/forbidden/unexpected; or any ERROR missing/forbidden per rules |

**Gate:** `FAIL` → halt before Frontend and before Generation Contracts. `PASS_WITH_WARNINGS` → operator documents decision in project log.

---

## Example run (block — HERO on LANDING_PAGE)

```yaml
validation_target:
  scope: BLOCK
  site_type_code: LANDING
  page_type: LANDING_PAGE
  block_id: HERO
  blueprint_ref: LANDING-BLUEPRINT-v1
required_signals: [offer, benefit, cta]
optional_signals: [proof, trust, experience, urgency]
forbidden_signals: [legal_disclosure, consent, payment, comparison]
missing_signals: []
unexpected_signals: []
warnings: []
status: PASS
```

---

## Aggregation (page-level)

When multiple block runs exist for one page:

| Page `status` | Rule |
|---------------|------|
| **FAIL** | Any block run FAIL; or page-level required signal missing |
| **PASS_WITH_WARNINGS** | No FAIL; any block or page WARNING |
| **PASS** | All block + page runs PASS |

Page-level `required_signals` / `forbidden_signals` come from [PAGE-CONTENT-CONTRACTS-v1.md](../content-contracts/PAGE-CONTENT-CONTRACTS-v1.md) **in addition to** block runs.

---

## Compatibility

Future semi-automatic validators **must** preserve field names and `status` enum. Extensions (e.g. `evidence_refs[]`) — only via CONTENT-VALIDATION-GAPS charter.

---

## SAFE UNKNOWN

- Standard file format for persisted runs (YAML vs JSON) — **not frozen** in v1.
- Multi-locale signal instances — **FUTURE**.

---

*Content Validation Contract version: v1.*
