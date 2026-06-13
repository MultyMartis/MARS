# Website Factory — Runtime Gates v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** runtime gate system — **documentation only**  
**Связь:** [RUNTIME-ARCHITECTURE-SYSTEM-v1.md](RUNTIME-ARCHITECTURE-SYSTEM-v1.md), [PROJECT-STATE-MODEL-v1.md](PROJECT-STATE-MODEL-v1.md)

**Не является:** CI job, webhook, policy engine, automated enforcer.

---

## 1. Назначение

Runtime Gates v1 — **контрольные точки движения** проекта между архитектурными слоями. Каждый gate: purpose, inputs, pass criteria, failure criteria.

Runtime gates **coordinate** layer-specific gates; they do not replace [VALIDATION-CONTRACT-v1.md](../page-block-validation/VALIDATION-CONTRACT-v1.md), [GENERATION-GATES-v1.md](../generation-contracts/GENERATION-GATES-v1.md), or [PRODUCTION-QA-GATES-v1.md](../production-qa/PRODUCTION-QA-GATES-v1.md).

---

## 2. Gate index

| Gate ID | Name | Unlocks state |
|---------|------|---------------|
| `RG-INTAKE_COMPLETE` | Intake Complete | → `CLASSIFIED` path |
| `RG-CLASSIFICATION_COMPLETE` | Classification Complete | → `BLUEPRINT_READY` |
| `RG-BLUEPRINT_APPROVED` | Blueprint Approved | → `PAGE_READY` |
| `RG-PAGE_ARCHITECTURE_APPROVED` | Page Architecture Approved | → `BLOCK_READY` |
| `RG-BLOCK_MAPPING_COMPLETE` | Block Mapping Complete | → validation run |
| `RG-VALIDATION_PASS` | Validation Pass | → `SEO_READY` |
| `RG-SEO_APPROVED` | SEO Approved | → `DESIGN_READY` |
| `RG-DESIGN_APPROVED` | Design Approved | → `CONTENT_READY` |
| `RG-CONTENT_APPROVED` | Content Approved | → content validation run |
| `RG-CONTENT_VALIDATION_PASS` | Content Validation Pass | → `GENERATION_READY` path |
| `RG-LEGAL_COMPLETE` | Legal Complete | required for `GENERATION_READY` |
| `RG-ENTITY_VERIFIED` | Entity Verified | conditional for `GENERATION_READY` |
| `RG-GENERATION_READY` | Generation Ready | → `PRODUCTION_QA_READY` |
| `RG-PRODUCTION_QA_PASS` | Production QA Pass | → `FRONTEND_READY` |
| `RG-FRONTEND_HANDOFF_APPROVED` | Frontend Handoff Approved | → `COMPLETE` path |
| `RG-PROJECT_COMPLETE` | Project Complete | → `COMPLETE` |

---

## 3. Gate definitions

### `RG-INTAKE_COMPLETE` — Intake Complete

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm project chartered and in Factory scope |
| **Inputs** | Project charter, scope tier, operator assignment |
| **Pass criteria** | Charter documented; scope tier declared; exclusions listed if partial |
| **Failure criteria** | Missing charter; ambiguous scope; conflicting goals |

---

### `RG-CLASSIFICATION_COMPLETE` — Classification Complete

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm `site_type_code` and Registry compliance |
| **Inputs** | [SITE-TYPE-REGISTRY-v1.md](../registry/SITE-TYPE-REGISTRY-v1.md), project brief |
| **Pass criteria** | Single canonical `site_type_code`; Core path OR Extended + charter |
| **Failure criteria** | Ambiguous type; unapproved type; Extended without charter |

---

### `RG-BLUEPRINT_APPROVED` — Blueprint Approved

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm site-level IA and blueprint frozen |
| **Inputs** | Blueprint doc for `site_type_code`, [BLUEPRINT-SYSTEM-v1.md](../blueprints/BLUEPRINT-SYSTEM-v1.md) |
| **Pass criteria** | Canonical blueprint selected; operator sign-off; exclusions documented |
| **Failure criteria** | No blueprint for Core type; draft blueprint; unapproved IA change |

---

### `RG-PAGE_ARCHITECTURE_APPROVED` — Page Architecture Approved

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm all in-scope routes have page contracts |
| **Inputs** | [PAGE-ARCHITECTURE-SYSTEM-v1.md](../page-architecture/PAGE-ARCHITECTURE-SYSTEM-v1.md), route list |
| **Pass criteria** | Every route has `page_type` + PAGE-CONTRACT; legal routes mapped if required |
| **Failure criteria** | Orphan route; missing PAGE-CONTRACT; blueprint mismatch |

---

### `RG-BLOCK_MAPPING_COMPLETE` — Block Mapping Complete

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm block stacks resolved via Block Registry |
| **Inputs** | [BLOCK-REGISTRY-v1.md](../block-registry/BLOCK-REGISTRY-v1.md), PAGE-BLOCK-MAPPING |
| **Pass criteria** | All required blocks mapped; only registered `block_id`; dependencies noted |
| **Failure criteria** | Unregistered `block_id`; missing required block; mapping gap |

---

### `RG-VALIDATION_PASS` — Validation Pass

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm Page Block Validation PASS |
| **Inputs** | [PAGE-BLOCK-VALIDATION-SYSTEM-v1.md](../page-block-validation/PAGE-BLOCK-VALIDATION-SYSTEM-v1.md), validation run |
| **Pass criteria** | PASS recorded; no open FAIL/CRITICAL |
| **Failure criteria** | FAIL; CRITICAL; validation not run |

**Maps to layer:** Page Block Validation gates.

---

### `RG-SEO_APPROVED` — SEO Approved

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm SEO architecture complete for scope |
| **Inputs** | [SEO-ARCHITECTURE-SYSTEM-v2.md](../seo-architecture/SEO-ARCHITECTURE-SYSTEM-v2.md), PAGE-SEO-CONTRACTs |
| **Pass criteria** | Strategy + per-page SEO contracts; operator sign-off |
| **Failure criteria** | Missing page SEO contract; strategy gap; pre-validation entry |

---

### `RG-DESIGN_APPROVED` — Design Approved

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm design mapping complete |
| **Inputs** | [DESIGN-SYSTEM-MAPPING-v1.md](../design-system/DESIGN-SYSTEM-MAPPING-v1.md), `VF_*` bindings |
| **Pass criteria** | Required visual patterns bound; operator sign-off |
| **Failure criteria** | Missing `VF_*` for required block; design before validation |

---

### `RG-CONTENT_APPROVED` — Content Approved

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm content signals bound per contracts |
| **Inputs** | [CONTENT-SYSTEM-v1.md](../content-contracts/CONTENT-SYSTEM-v1.md), signal bindings |
| **Pass criteria** | Required signals per block/page; operator sign-off |
| **Failure criteria** | Missing signal; forbidden signal present; content before design |

---

### `RG-CONTENT_VALIDATION_PASS` — Content Validation Pass

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm content signal architecture valid |
| **Inputs** | [CONTENT-VALIDATION-SYSTEM-v1.md](../content-validation/CONTENT-VALIDATION-SYSTEM-v1.md) |
| **Pass criteria** | PASS; no FAIL/CRITICAL on signal architecture |
| **Failure criteria** | FAIL; CRITICAL; validation skipped |

---

### `RG-LEGAL_COMPLETE` — Legal Complete

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm Legal Pack architecture applied |
| **Inputs** | [LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md), SITE-TYPE-LEGAL-MAPPING-v2 |
| **Pass criteria** | Required legal routes mapped; templates pinned; no unresolved legal gap |
| **Failure criteria** | Missing legal page; mapping mismatch; placeholder gate FAIL |

**Required before:** `RG-GENERATION_READY`.

---

### `RG-ENTITY_VERIFIED` — Entity Verified

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm Legal Entity Card when required |
| **Inputs** | [legal-entity/](../legal-entity/), project charter |
| **Pass criteria** | Entity Card READY or documented NOT_APPLICABLE + operator sign-off |
| **Failure criteria** | Entity required but NOT_READY or stale |

**Conditional:** skip when charter + mapping state not required.

---

### `RG-GENERATION_READY` — Generation Ready

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm all upstream gates; scope frozen for generation package |
| **Inputs** | All prior gate PASS records, [GENERATION-CONTRACT-v1.md](../generation-contracts/GENERATION-CONTRACT-v1.md) |
| **Pass criteria** | All mandatory runtime gates PASS; operator Generation Ready sign-off |
| **Failure criteria** | Any upstream gate open; legal/entity block; scope drift |

**Maps to layer:** [GENERATION-GATES-v1.md](../generation-contracts/GENERATION-GATES-v1.md).

---

### `RG-PRODUCTION_QA_PASS` — Production QA Pass

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm global architectural readiness for Frontend |
| **Inputs** | [PRODUCTION-QA-SYSTEM-v1.md](../production-qa/PRODUCTION-QA-SYSTEM-v1.md), full artefact set |
| **Pass criteria** | All Production QA gates PASS; checklist complete; operator sign-off |
| **Failure criteria** | Any category FAIL; QA skipped; Frontend attempted before QA |

**Maps to layer:** [PRODUCTION-QA-GATES-v1.md](../production-qa/PRODUCTION-QA-GATES-v1.md).

---

### `RG-FRONTEND_HANDOFF_APPROVED` — Frontend Handoff Approved

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm handoff package complete and acknowledged |
| **Inputs** | [GENERATION-OUTPUTS-v1.md](../generation-contracts/GENERATION-OUTPUTS-v1.md) FRONTEND_HANDOFF_PACKAGE |
| **Pass criteria** | Package complete per contract; Frontend ack; operator approval |
| **Failure criteria** | Incomplete package; QA bypass; no ack |

---

### `RG-PROJECT_COMPLETE` — Project Complete

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm Factory architecture track closed |
| **Inputs** | `FRONTEND_READY`, closure checklist |
| **Pass criteria** | Handoff approved; no open CRITICAL failures; operator closure |
| **Failure criteria** | Complete declared early; open blockers |

---

## 4. Gate dependency graph

```text
RG-INTAKE_COMPLETE
    → RG-CLASSIFICATION_COMPLETE
    → RG-BLUEPRINT_APPROVED
    → RG-PAGE_ARCHITECTURE_APPROVED
    → RG-BLOCK_MAPPING_COMPLETE
    → RG-VALIDATION_PASS
    → RG-SEO_APPROVED
    → RG-DESIGN_APPROVED
    → RG-CONTENT_APPROVED
    → RG-CONTENT_VALIDATION_PASS
    → [RG-LEGAL_COMPLETE + RG-ENTITY_VERIFIED if required]
    → RG-GENERATION_READY
    → RG-PRODUCTION_QA_PASS
    → RG-FRONTEND_HANDOFF_APPROVED
    → RG-PROJECT_COMPLETE
```

---

*Runtime Gates v1 — 2026-06-01.*
