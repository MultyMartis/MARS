# Website Factory — Production QA Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** канонический контракт production QA run — **documentation only**  
**Связь:** [PRODUCTION-QA-SYSTEM-v1.md](PRODUCTION-QA-SYSTEM-v1.md), [PRODUCTION-QA-GATES-v1.md](PRODUCTION-QA-GATES-v1.md)

**Не является:** JSON Schema, OpenAPI spec, runtime API, test report format, Playwright config, deploy record, CI artefact.

---

## Назначение

Production QA Contract v1 задаёт **обязательные поля** для одного production QA run (site, phase, or release slice). Используется operator checklist **сейчас**; будущие QA tools **обязаны** emit compatible structure **без** добавления execution steps в v1 contract.

---

## Mandatory fields

### `qa_run_id`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Уникальный идентификатор production QA run |
| **Формат** | `pqa-{project_slug}-{YYYYMMDD}-{seq}` или operator-equivalent |
| **Пример** | `pqa-triumph-landing-20260601-01` |
| **Rule** | Immutable after `GATE_PRODUCTION_QA_PASS`; new scope → new `qa_run_id` |

---

### `project_scope`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Boundary of architectural QA review |
| **Обязательные subfields** | `project_slug`, `site_type_code`, `scope_type`, `included_page_types`, `included_routes`, `excluded_routes`, `blueprint_ref`, `generation_id` |
| **`scope_type` v1** | `FULL_SITE` \| `PAGE_SUBSET` \| `LEGAL_ONLY` \| `PHASE_SLICE` |
| **`site_type_code`** | From [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md); v1 matrix: Core 5 |
| **Rule** | Scope **cannot** widen without new `qa_run_id` and full category re-check |

---

### `required_inputs`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Checklist of upstream artefact refs required before QA run |
| **Формат** | Array of `{ input_id, source_path_or_ref, acceptance_state, status }` |
| **Минимум v1** | `site_type_registry`, `blueprint_ref`, `page_contracts`, `block_registry_ref`, `page_block_validation_runs`, `seo_profile`, `design_mapping`, `content_contracts`, `content_validation_runs`, `legal_pack_ref`, `entity_card` (when applicable), `generation_contract` |
| **Rule** | Any `status` ≠ `READY` → QA contract cannot reach `PASS` |

**Input catalogue (reference):**

| `input_id` | Typical source |
|------------|----------------|
| `site_type_registry` | [registry/SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| `blueprint_ref` | [blueprints/](../blueprints/) canonical doc |
| `page_contracts` | [page-architecture/PAGE-CONTRACT-v1.md](../page-architecture/PAGE-CONTRACT-v1.md) instances |
| `block_registry_ref` | [block-registry/BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md) |
| `page_block_validation_runs` | [page-block-validation/VALIDATION-CONTRACT-v1.md](../page-block-validation/VALIDATION-CONTRACT-v1.md) |
| `seo_profile` | [seo-architecture/](../seo-architecture/) strategy + page SEO |
| `design_mapping` | [design-system/DESIGN-SYSTEM-MAPPING-v1.md](../design-system/DESIGN-SYSTEM-MAPPING-v1.md) |
| `content_contracts` | [content-contracts/CONTENT-CONTRACT-v1.md](../content-contracts/CONTENT-CONTRACT-v1.md) |
| `content_validation_runs` | [content-validation/CONTENT-VALIDATION-CONTRACT-v1.md](../content-validation/CONTENT-VALIDATION-CONTRACT-v1.md) |
| `legal_pack_ref` | [legal/LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md) |
| `entity_card` | [legal-entity/](../legal-entity/) when commercial entity required |
| `generation_contract` | [generation-contracts/GENERATION-CONTRACT-v1.md](../generation-contracts/GENERATION-CONTRACT-v1.md) |

---

### `required_gates`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Ordered QA gate IDs that must be `PASS` (or allowed waiver) before Frontend Handoff |
| **Источник** | [PRODUCTION-QA-GATES-v1.md](PRODUCTION-QA-GATES-v1.md) |
| **Формат** | Array of `{ gate_id, status, evidence_ref, signed_off_by, timestamp }` |
| **Rule** | Missing gate or `FAIL` → halt per failure library |

**Minimum gate set (FULL_SITE):**

1. `GATE_ARCHITECTURE_COMPLETE`
2. `GATE_LEGAL_COMPLETE`
3. `GATE_ENTITY_VERIFIED` (conditional)
4. `GATE_SEO_COMPLETE`
5. `GATE_DESIGN_COMPLETE`
6. `GATE_CONTENT_COMPLETE`
7. `GATE_VALIDATION_COMPLETE`
8. `GATE_GENERATION_READY`
9. `GATE_PRODUCTION_QA_PASS`
10. `GATE_FRONTEND_HANDOFF_APPROVED`

---

### `qa_categories`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Per-category review outcome |
| **Формат** | Array of `{ category_id, status, findings_count, notes }` |
| **Канонические `category_id`** | `ARCHITECTURE`, `LEGAL`, `ENTITY`, `SEO`, `DESIGN`, `CONTENT`, `CONTENT_VALIDATION`, `GENERATION_READINESS`, `HANDOFF_READINESS`, `DOCUMENTATION_INTEGRITY` |
| **Per-category `status`** | `PASS` \| `PASS_WITH_WARNINGS` \| `FAIL` \| `NOT_APPLICABLE` |
| **Rule** | Any category `FAIL` → contract `status` = `FAIL` (unless `BLOCKED` takes precedence) |

---

### `failures`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Typed findings blocking or degrading pass |
| **Формат** | Array of `{ failure_id, category_id, severity, message, evidence_ref, correction_ref }` |
| **Источник** | [PRODUCTION-QA-FAILURE-LIBRARY-v1.md](PRODUCTION-QA-FAILURE-LIBRARY-v1.md) (`PQF-###`) |
| **Rule** | `BLOCKER` or `CRITICAL` → see severity → status mapping |

---

### `warnings`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Non-blocking findings (INFO, WARNING) |
| **Формат** | Array of `{ warning_id, category_id, severity, message, waiver_eligible }` |
| **Rule** | Accumulated WARNING may yield contract `PASS_WITH_WARNINGS` |

---

### `status`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Aggregate QA run outcome |
| **Допустимые значения** | `PASS` \| `PASS_WITH_WARNINGS` \| `FAIL` \| `BLOCKED` |
| **Источник mapping** | [PRODUCTION-QA-SEVERITY-SYSTEM-v1.md](PRODUCTION-QA-SEVERITY-SYSTEM-v1.md) |
| **Rule** | Operator sign-off required for `PASS` and `PASS_WITH_WARNINGS` before `GATE_FRONTEND_HANDOFF_APPROVED` |

---

## Status definitions

| Status | Meaning |
|--------|---------|
| **PASS** | All required gates PASS; no ERROR/CRITICAL/BLOCKER failures; warnings only INFO or none |
| **PASS_WITH_WARNINGS** | All gates PASS; one or more WARNING-level findings; operator waiver documented |
| **FAIL** | One or more ERROR or CRITICAL failures; or required gate FAIL |
| **BLOCKED** | Prerequisites missing; upstream layer incomplete; handoff attempted before QA; cannot proceed |

---

## Optional fields (recommended)

| Field | Purpose |
|-------|---------|
| `operator_id` | Human who signed QA run |
| `reviewed_at` | ISO timestamp |
| `generation_id` | Link to upstream generation contract |
| `checklist_ref` | Pointer to completed [PRODUCTION-QA-CHECKLIST-v1.md](PRODUCTION-QA-CHECKLIST-v1.md) |
| `matrix_overlay_ref` | Site-type row from [PRODUCTION-QA-MATRIX-v1.md](PRODUCTION-QA-MATRIX-v1.md) |
| `notes` | Free-text operator context |

---

## Contract lifecycle

```text
Prerequisites READY
        ↓
Populate required_inputs + upstream gate evidence
        ↓
Run qa_categories (checklist + matrix)
        ↓
Emit failures / warnings
        ↓
Compute status
        ↓
GATE_PRODUCTION_QA_PASS (if PASS or PASS_WITH_WARNINGS)
        ↓
GATE_FRONTEND_HANDOFF_APPROVED (operator)
```

---

*Production QA Contract v1 — fields only. No validator implementation claimed.*
