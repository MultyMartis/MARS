# Website Factory — Generation Contract v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/generation-contracts/`  
**Статус:** канонический контракт production generation run — **documentation only**  
**Связь:** [GENERATION-SYSTEM-v1.md](GENERATION-SYSTEM-v1.md), [GENERATION-GATES-v1.md](GENERATION-GATES-v1.md)

**Не является:** JSON Schema, OpenAPI spec, runtime API, workflow definition, prompt payload, codegen manifest, deploy record.

---

## Назначение

Generation Contract v1 задаёт **обязательные поля** для одного production generation scope (site, phase, or release slice). Используется operator checklist **сейчас**; будущие orchestration tools **обязаны** emit compatible structure **без** добавления execution steps в v1 contract.

---

## Mandatory fields

### `generation_id`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Уникальный идентификатор generation run / production slice |
| **Формат** | `gen-{project_slug}-{YYYYMMDD}-{seq}` или operator-equivalent |
| **Пример** | `gen-triumph-landing-20260601-01` |
| **Rule** | Immutable after gate `Generation Ready`; new scope → new `generation_id` |

---

### `site_type_code`

| Атрибут | Требование |
|---------|------------|
| **Формат** | UPPER_SNAKE_CASE from [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md) |
| **v1 production matrix** | Core 5: `LANDING`, `PROMO`, `CATALOG`, `ECOMMERCE`, `CORPORATE` |
| **Extended** | `SAAS`, `WEB_APPLICATION`, `MARKETPLACE` — generation scope **SAFE UNKNOWN** until Extended charter |
| **Rule** | Drives blueprint selection, matrices, legal mapping |

---

### `required_inputs`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Checklist of input artefact refs required before `Generation Ready` |
| **Формат** | Array of `{ input_id, source_path_or_ref, status }` per [GENERATION-INPUTS-v1.md](GENERATION-INPUTS-v1.md) |
| **Rule** | Any `status` ≠ `READY` → generation contract `status` cannot be `READY` |
| **Минимум v1** | `project_brief`, `blueprint_ref`, `page_contracts`, `block_mapping`, `page_block_validation`, `seo_profile`, `design_mapping`, `content_contracts`, `content_validation`, `legal_pack_ref`, `entity_card` (when applicable) |

---

### `required_gates`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Ordered gate IDs that must be `PASS` before handoff |
| **Источник** | [GENERATION-GATES-v1.md](GENERATION-GATES-v1.md) |
| **Формат** | Array of `{ gate_id, status, signed_off_by, timestamp }` |
| **Rule** | Missing gate or `FAIL` → halt per failure library |

---

### `required_dependencies`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Upstream layer acceptance + version pins |
| **Формат** | Array of `{ layer, artefact_ref, version, acceptance_state }` |
| **Пример** | `{ layer: "SEO", artefact_ref: "SEO-ARCHITECTURE-SYSTEM-v2", version: "v2", acceptance_state: "ACCEPTED" }` |
| **Rule** | `acceptance_state` must be `ACCEPTED` or `FROZEN` for hard dependencies; `PENDING` blocks `Generation Ready` |

---

### `generation_scope`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Boundary of what this run covers |
| **Обязательные subfields** | `scope_type`, `included_page_types`, `included_routes`, `excluded_routes`, `blueprint_ref` |
| **`scope_type` v1** | `FULL_SITE` \| `PAGE_SUBSET` \| `LEGAL_ONLY` \| `PHASE_SLICE` |
| **Rule** | Scope **cannot** widen without new `generation_id` and gate re-run for affected pages |

---

### `expected_outputs`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Output artefact types to produce on successful completion |
| **Источник** | [GENERATION-OUTPUTS-v1.md](GENERATION-OUTPUTS-v1.md) |
| **Формат** | Array of `{ output_type, status, artefact_ref }` |
| **Минимум v1** | `PAGE_BUILD_SPEC`, `BLOCK_STACK_SPEC`, `SEO_SPEC`, `DESIGN_SPEC`, `CONTENT_SPEC`, `FRONTEND_HANDOFF_PACKAGE` |
| **Rule** | Definitions only — no file paths to generated code in v1 contract |

---

### `failure_conditions`

| Атрибут | Требование |
|---------|------------|
| **Содержание** | Conditions that force `status` = `BLOCKED` or `FAILED` |
| **Источник** | [GENERATION-FAILURE-LIBRARY-v1.md](GENERATION-FAILURE-LIBRARY-v1.md) |
| **Формат** | Array of `{ failure_id, severity, detected, resolution_ref }` |
| **Rule** | Any `CRITICAL` failure → `status` = `FAILED`; unresolved `ERROR` → `BLOCKED` |

---

### `status`

| Атрибут | Требование |
|---------|------------|
| **Допустимые значения** | `DRAFT` \| `IN_PROGRESS` \| `BLOCKED` \| `READY` \| `HANDED_OFF` \| `FAILED` |
| **Переходы** | `DRAFT` → `IN_PROGRESS` after Classify; `READY` only when all required gates PASS; `HANDED_OFF` after Frontend Handoff acknowledged |
| **Rule** | `READY` **запрещён** при placeholder leakage, validation FAIL, or legal unresolved |

---

## Optional fields (recommended, not mandatory v1)

| Field | Purpose |
|-------|---------|
| `project_slug` | Human traceability |
| `operator_notes` | HITL exceptions (must reference gate waiver charter if any) |
| `reference_workspace` | e.g. `website-factory-reference-v1`, pilot path |
| `target_locale` | Default `ru-RU` when unknown — document, do not auto-translate |

---

## Explicit exclusions (contract MUST NOT contain)

| Forbidden content | Rationale |
|-------------------|-----------|
| Prompts, system messages, model IDs | Generation Gaps — AI layer |
| Runtime steps (npm, gulp, deploy) | Not orchestration contract |
| Source code snippets | Frontend implementation |
| CMS credentials, API keys | Security |
| Auto-approval flags without HITL ref | Human authority protocol |

---

## Contract completeness rule

Generation Contract v1 считается **неполным**, если отсутствует любое mandatory field или `required_gates` не покрывает минимальный набор из GENERATION-GATES-v1 § «Minimum gate set».

---

*Generation Contract version: v1.*
