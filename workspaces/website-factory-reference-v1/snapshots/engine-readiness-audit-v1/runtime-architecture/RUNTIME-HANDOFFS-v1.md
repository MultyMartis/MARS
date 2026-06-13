# Website Factory — Runtime Handoffs v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** layer handoff contracts — **documentation only**  
**Связь:** [RUNTIME-ARCHITECTURE-SYSTEM-v1.md](RUNTIME-ARCHITECTURE-SYSTEM-v1.md), [GENERATION-OUTPUTS-v1.md](../generation-contracts/GENERATION-OUTPUTS-v1.md)

---

## 1. Назначение

Runtime Handoffs v1 определяет **передачу ответственности и артефактов** между архитектурными слоями: producer, consumer, required artefacts, blocked conditions.

**Handoff ≠ execution.** Consumer **reviews and binds** upstream artefacts; does not auto-run pipelines.

---

## 2. Handoff index

| Handoff ID | From → To | Runtime state boundary |
|------------|-----------|------------------------|
| `HO-01` | Intake → Classification | `NEW_PROJECT` → `CLASSIFIED` |
| `HO-02` | Classification → Blueprint | `CLASSIFIED` → `BLUEPRINT_READY` |
| `HO-03` | Blueprint → Page Architecture | `BLUEPRINT_READY` → `PAGE_READY` |
| `HO-04` | Page Architecture → Block Registry | `PAGE_READY` → `BLOCK_READY` |
| `HO-05` | Block Registry → Validation | `BLOCK_READY` → `VALIDATED` |
| `HO-06` | Validation → SEO | `VALIDATED` → `SEO_READY` |
| `HO-07` | SEO → Design | `SEO_READY` → `DESIGN_READY` |
| `HO-08` | Design → Content | `DESIGN_READY` → `CONTENT_READY` |
| `HO-09` | Content → Content Validation | `CONTENT_READY` → `CONTENT_VALIDATED` |
| `HO-10` | Content Validation → Generation | `CONTENT_VALIDATED` → `GENERATION_READY` |
| `HO-11` | Generation → Production QA | `GENERATION_READY` → `PRODUCTION_QA_READY` |
| `HO-12` | Production QA → Frontend | `PRODUCTION_QA_READY` → `FRONTEND_READY` |
| `HO-13` | Frontend → Complete | `FRONTEND_READY` → `COMPLETE` |

---

## 3. Handoff definitions

### `HO-01` — Intake → Classification

| Attribute | Value |
|-----------|-------|
| **Producer** | Operator / project intake |
| **Consumer** | Site Type Registry workstream |
| **Required artefacts** | Project charter, scope tier, stakeholder contacts |
| **Blocked conditions** | Missing scope; conflicting site type hints without resolution |

---

### `HO-02` — Classification → Blueprint

| Attribute | Value |
|-----------|-------|
| **Producer** | Site Type Registry |
| **Consumer** | Blueprints layer |
| **Required artefacts** | `site_type_code`, Registry matrix refs, Core/Extended flag |
| **Blocked conditions** | Unclassified project; Extended without charter |

---

### `HO-03` — Blueprint → Page Architecture

| Attribute | Value |
|-----------|-------|
| **Producer** | Blueprints layer |
| **Consumer** | Page Architecture layer |
| **Required artefacts** | `blueprint_ref`, IA page list, site-level block intent, operator Blueprint Approved |
| **Blocked conditions** | Draft blueprint; blueprint/page_type mismatch |

---

### `HO-04` — Page Architecture → Block Registry

| Attribute | Value |
|-----------|-------|
| **Producer** | Page Architecture layer |
| **Consumer** | Block Registry mapping |
| **Required artefacts** | Per-route `page_type`, PAGE-CONTRACT refs, required/forbidden blocks at page level |
| **Blocked conditions** | Orphan routes; missing PAGE-CONTRACT; Page Architecture not approved |

---

### `HO-05` — Block Registry → Validation

| Attribute | Value |
|-----------|-------|
| **Producer** | Block Registry mapping |
| **Consumer** | Page Block Validation layer |
| **Required artefacts** | Resolved `block_id` stacks, PAGE-BLOCK-MAPPING resolve, BLUEPRINT-BLOCK-MAPPING alignment |
| **Blocked conditions** | Unregistered `block_id`; incomplete stacks; mapping not complete |

---

### `HO-06` — Validation → SEO

| Attribute | Value |
|-----------|-------|
| **Producer** | Page Block Validation |
| **Consumer** | SEO Architecture layer |
| **Required artefacts** | Validation PASS record, validated block stacks, `site_type_code` |
| **Blocked conditions** | FAIL/CRITICAL open; validation skipped; pre-VALIDATED state |

---

### `HO-07` — SEO → Design

| Attribute | Value |
|-----------|-------|
| **Producer** | SEO Architecture layer |
| **Consumer** | Design System Mapping layer |
| **Required artefacts** | SEO strategy ref, PAGE-SEO-CONTRACT per in-scope page, operator SEO Approved |
| **Blocked conditions** | Missing page SEO contract; SEO before validation |

---

### `HO-08` — Design → Content

| Attribute | Value |
|-----------|-------|
| **Producer** | Design System Mapping layer |
| **Consumer** | Content Contracts layer |
| **Required artefacts** | `VF_*` bindings per required block/page, design mapping audit, operator Design Approved |
| **Blocked conditions** | Content before design; missing visual pattern for required block |

---

### `HO-09` — Content → Content Validation

| Attribute | Value |
|-----------|-------|
| **Producer** | Content Contracts layer |
| **Consumer** | Content Validation layer |
| **Required artefacts** | Signal bindings (`signal_id` refs), BLOCK/PAGE content contracts resolved |
| **Blocked conditions** | Unbound required signals; Content not approved |

---

### `HO-10` — Content Validation → Generation

| Attribute | Value |
|-----------|-------|
| **Producer** | Content Validation layer |
| **Consumer** | Generation Contracts layer |
| **Required artefacts** | Content validation PASS, Legal Complete (+ Entity when required), full upstream artefact index |
| **Blocked conditions** | Content validation FAIL; legal placeholder FAIL; entity NOT_READY when required |

---

### `HO-11` — Generation → Production QA

| Attribute | Value |
|-----------|-------|
| **Producer** | Generation Contracts layer |
| **Consumer** | Production QA layer |
| **Required artefacts** | GENERATION-CONTRACT READY, specification bundle per [GENERATION-OUTPUTS-v1.md](../generation-contracts/GENERATION-OUTPUTS-v1.md), `generation_id` |
| **Blocked conditions** | Generation Ready not signed; incomplete spec; upstream gate open |

---

### `HO-12` — Production QA → Frontend

| Attribute | Value |
|-----------|-------|
| **Producer** | Production QA layer |
| **Consumer** | Frontend Layer (implementation workstream) |
| **Required artefacts** | Production QA PASS, PRODUCTION-QA-CHECKLIST complete, FRONTEND_HANDOFF_PACKAGE |
| **Blocked conditions** | **Frontend handoff before QA PASS**; Production QA FAIL; incomplete handoff bundle |

---

### `HO-13` — Frontend → Complete

| Attribute | Value |
|-----------|-------|
| **Producer** | Frontend Layer (acknowledgement) |
| **Consumer** | Operator closure |
| **Required artefacts** | Handoff ack, Frontend Handoff Approved, no open Factory CRITICAL items |
| **Blocked conditions** | Complete before handoff approved; open CRITICAL runtime failures |

---

## 4. Legal parallel handoff

| Handoff ID | From → To | Notes |
|------------|-----------|-------|
| `HO-L1` | Legal Pack → Generation | Legal routes + templates bound before `HO-10` exit |
| `HO-L2` | Legal Entity Discovery → Generation | Entity Card when commercial disclosure required |

**Blocked:** Generation handoff (`HO-10`) while `RG-LEGAL_COMPLETE` or `RG-ENTITY_VERIFIED` (when required) = FAIL.

---

## 5. Handoff checklist (operator)

Before declaring consumer state ready:

1. All **required artefacts** listed for handoff ID present.
2. Producer layer gate **PASS** recorded.
3. No **blocked conditions** true.
4. Handoff recorded in project log (format — SAFE UNKNOWN, see GAPS).

---

*Runtime Handoffs v1 — 2026-06-01.*
