# Website Factory — Runtime Failure Library v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** runtime movement failures — **documentation only**  
**Связь:** [STATE-TRANSITION-RULES-v1.md](STATE-TRANSITION-RULES-v1.md), [RUNTIME-GATES-v1.md](RUNTIME-GATES-v1.md)

---

## 1. Назначение

Каталог **сбоев движения** проекта (не layer-specific validation failures — те в layer failure libraries). Каждая запись: cause, impact, severity, correction.

---

## 2. Failure catalogue

### `RF-SKIP-STATE` — State skipped

| Attribute | Value |
|-----------|-------|
| **Cause** | Operator or process declared later state without completing intermediate layer (e.g. `CLASSIFIED` → `SEO_READY`) |
| **Impact** | Downstream artefacts invalid; hidden dependency gaps; Frontend risk |
| **Severity** | **CRITICAL** |
| **Correction** | Halt; rollback to last valid state; re-run skipped layers; record in project log |

---

### `RF-INVALID-TRANSITION` — Invalid transition

| Attribute | Value |
|-----------|-------|
| **Cause** | Transition violates [STATE-TRANSITION-RULES-v1.md](STATE-TRANSITION-RULES-v1.md) (FT-* or DR-*) |
| **Impact** | Architecture chain broken; audit trail unreliable |
| **Severity** | **CRITICAL** |
| **Correction** | Revert declared state; apply allowed transition only after gate PASS |

---

### `RF-MISSING-DEPENDENCY` — Missing dependency

| Attribute | Value |
|-----------|-------|
| **Cause** | Consumer layer started without required upstream artefact (e.g. SEO without PAGE-SEO inputs from validated stack) |
| **Impact** | Rework; inconsistent bindings; Production QA FAIL |
| **Severity** | **HIGH** |
| **Correction** | Stop consumer work; complete producer handoff; re-handoff |

---

### `RF-MISSING-APPROVAL` — Missing approval

| Attribute | Value |
|-----------|-------|
| **Cause** | State advanced without operator HITL sign-off (Blueprint, SEO, Design, Content, Generation Ready, Handoff) |
| **Impact** | Unauthorized scope freeze; accountability gap |
| **Severity** | **HIGH** |
| **Correction** | Hold state; obtain retroactive approval only if artefacts valid — else rollback |

---

### `RF-GATE-FAILURE` — Gate failure

| Attribute | Value |
|-----------|-------|
| **Cause** | Runtime or layer gate recorded FAIL/CRITICAL but state advanced anyway |
| **Impact** | Invalid generation package; legal/compliance exposure |
| **Severity** | **CRITICAL** |
| **Correction** | Halt at current phase; remediate per layer failure library; re-run gate |

---

### `RF-QA-BYPASS` — Frontend handoff before QA

| Attribute | Value |
|-----------|-------|
| **Cause** | `FRONTEND_READY` or handoff package issued before `RG-PRODUCTION_QA_PASS` |
| **Impact** | Frontend implements incomplete architecture; rework cost |
| **Severity** | **CRITICAL** |
| **Correction** | Block Frontend start; complete Production QA; re-issue handoff after PASS |

---

### `RF-HANDOFF-BYPASS` — Complete before readiness

| Attribute | Value |
|-----------|-------|
| **Cause** | `COMPLETE` declared without `FRONTEND_READY` or Frontend Handoff Approved |
| **Impact** | False closure; open Factory obligations |
| **Severity** | **CRITICAL** |
| **Correction** | Reopen project state to `PRODUCTION_QA_READY` or `FRONTEND_READY`; complete handoff |

---

### `RF-SEO-BEFORE-VALIDATION` — SEO before validation

| Attribute | Value |
|-----------|-------|
| **Cause** | SEO work started or `SEO_READY` declared while Page Block Validation FAIL/CRITICAL or pre-`VALIDATED` |
| **Impact** | SEO contracts misaligned with block reality |
| **Severity** | **HIGH** |
| **Correction** | Rollback to `BLOCK_READY`/`VALIDATED` path; fix validation; re-apply SEO |

---

### `RF-CONTENT-BEFORE-DESIGN` — Content before design

| Attribute | Value |
|-----------|-------|
| **Cause** | Content binding or `CONTENT_READY` before `DESIGN_READY` |
| **Impact** | Signals without `VF_*` context; design/content drift |
| **Severity** | **HIGH** |
| **Correction** | Rollback to `DESIGN_READY`; complete design mapping first |

---

### `RF-LEGAL-BLOCK` — Legal block at generation

| Attribute | Value |
|-----------|-------|
| **Cause** | `GENERATION_READY` attempted with Legal placeholder FAIL or entity NOT_READY |
| **Impact** | Non-compliant generation scope; Triumph-class STOP scenarios |
| **Severity** | **CRITICAL** |
| **Correction** | Complete Legal Pack path; resolve entity card; re-gate `RG-LEGAL_COMPLETE` / `RG-ENTITY_VERIFIED` |

---

### `RF-EXTENDED-NO-CHARTER` — Extended type without charter

| Attribute | Value |
|-----------|-------|
| **Cause** | `SAAS` / `WEB_APPLICATION` / `MARKETPLACE` entered production path without charter |
| **Impact** | Missing blueprint/validation matrices; false production claim |
| **Severity** | **HIGH** |
| **Correction** | Remain in `CLASSIFIED`; obtain charter or reclassify to Core type |

---

### `RF-ROLLBACK-CHAOS` — Undocumented rollback

| Attribute | Value |
|-----------|-------|
| **Cause** | Multi-layer rollback without charter or log |
| **Impact** | Artefact version confusion; duplicate work |
| **Severity** | **MEDIUM** |
| **Correction** | Document rollback target; invalidate downstream artefacts; re-handoff per HO-* |

---

### `RF-FROZEN-LEGAL-MOD` — Frozen Legal Pack modification

| Attribute | Value |
|-----------|-------|
| **Cause** | Architectural change to Legal Pack during project lifecycle |
| **Impact** | Freeze violation; pilot baseline drift |
| **Severity** | **CRITICAL** |
| **Correction** | Revert change; use frozen docs only; charter required for any legal architecture change |

---

## 3. Severity summary

| Severity | Count (v1) | Default action |
|----------|------------|----------------|
| **CRITICAL** | 7 | Mandatory halt |
| **HIGH** | 5 | Halt until remediated |
| **MEDIUM** | 1 | Document + remediate |

---

## 4. Cross-reference to layer libraries

| Runtime failure | Layer library |
|-----------------|---------------|
| Validation content | [VALIDATION-FAILURE-LIBRARY-v1.md](../page-block-validation/VALIDATION-FAILURE-LIBRARY-v1.md) |
| Content signals | [CONTENT-FAILURE-LIBRARY-v1.md](../content-validation/CONTENT-FAILURE-LIBRARY-v1.md) |
| Generation | [GENERATION-FAILURE-LIBRARY-v1.md](../generation-contracts/GENERATION-FAILURE-LIBRARY-v1.md) |
| Production QA | [PRODUCTION-QA-FAILURE-LIBRARY-v1.md](../production-qa/PRODUCTION-QA-FAILURE-LIBRARY-v1.md) |

Runtime failures describe **movement** violations; layer libraries describe **artefact** violations.

---

*Runtime Failure Library v1 — 2026-06-01.*
