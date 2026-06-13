# Website Factory — Production QA Gates v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** formal production QA gates — **documentation only**  
**Связь:** [PRODUCTION-QA-CONTRACT-v1.md](PRODUCTION-QA-CONTRACT-v1.md), [PRODUCTION-QA-SYSTEM-v1.md](PRODUCTION-QA-SYSTEM-v1.md)

**Не является:** CI job definitions, Playwright suite, deploy approval webhook, automated policy engine.

---

## 1. Назначение

Production QA Gates v1 — **формальные контрольные точки** финального architectural readiness review. Каждый gate: **purpose**, **inputs**, **pass criteria**, **failure criteria**.

**Minimum gate set** (required in every `FULL_SITE` production QA contract):

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

**Relationship to Generation gates:** Production QA gates **aggregate** upstream generation gates ([GENERATION-GATES-v1.md](../generation-contracts/GENERATION-GATES-v1.md)); they do not replace layer-specific validation.

---

## 2. Gate catalogue

### GATE_ARCHITECTURE_COMPLETE

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm site type, blueprint, page architecture, and block registry alignment for scope |
| **Inputs** | `site_type_code`, blueprint doc, page contracts (all in-scope routes), BLOCK-REGISTRY refs, PAGE-BLOCK-MAPPING / BLUEPRINT-BLOCK-MAPPING |
| **Pass criteria** | Canonical blueprint selected; every in-scope route has `page_type` + PAGE-CONTRACT; block mappings exist; no taxonomy drift |
| **Failure criteria** | Missing blueprint; missing page contract; orphan route; unregistered `block_id`; wrong `site_type_code` |

**Maps to category:** `ARCHITECTURE`

---

### GATE_LEGAL_COMPLETE

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm Legal Pack coverage for site type and legal routes in scope |
| **Inputs** | [LEGAL-PACK-v1-FREEZE.md](../legal/LEGAL-PACK-v1-FREEZE.md), SITE-TYPE-LEGAL-MAPPING-v2, LEGAL_PAGE contracts, legal route list |
| **Pass criteria** | Required legal documents mapped; LEGAL_PAGE contracts instantiated; template refs pinned; no unresolved legal architecture gap |
| **Failure criteria** | Missing Legal Pack ref; missing LEGAL_PAGE for required route; legal mapping mismatch with `site_type_code` |

**Maps to category:** `LEGAL`

---

### GATE_ENTITY_VERIFIED

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm Legal Entity Card ready when commercial entity disclosure required |
| **Inputs** | [legal-entity/](../legal-entity/) Entity Card, project charter, legal mapping |
| **Pass criteria** | Entity Card `READY` or documented `NOT_APPLICABLE` with operator sign-off |
| **Failure criteria** | Entity required but card missing, draft, or stale vs legal pack |
| **Conditional** | Skip only when mapping + charter state entity not required |

**Maps to category:** `ENTITY`

---

### GATE_SEO_COMPLETE

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm SEO architecture applied for all in-scope pages |
| **Inputs** | SEO-STRATEGY-CONTRACT, PAGE-SEO-CONTRACT per page, SITE-TYPE-SEO-MAPPING-v2 |
| **Pass criteria** | Strategy contract exists; each in-scope `page_type` has page SEO role; no unresolved SEO architecture gaps for scope |
| **Failure criteria** | Missing SEO profile; missing page SEO contract; intent mismatch with blueprint |

**Maps to category:** `SEO`

---

### GATE_DESIGN_COMPLETE

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm design system mapping bound for in-scope blocks/pages |
| **Inputs** | DESIGN-SYSTEM-MAPPING, BLOCK-VISUAL-MAPPING, PAGE-TYPE-DESIGN-MAPPING, `VF_*` selections |
| **Pass criteria** | Required blocks have visual pattern binding; no pattern contradicts forbidden blocks |
| **Failure criteria** | Missing design mapping for required block; `VF_*` on FORBIDDEN block |

**Maps to category:** `DESIGN`

---

### GATE_CONTENT_COMPLETE

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm content contracts bound for in-scope blocks/pages |
| **Inputs** | CONTENT-CONTRACT, BLOCK-CONTENT-CONTRACTS, PAGE-CONTENT-CONTRACTS, CONTENT-SIGNAL-REGISTRY |
| **Pass criteria** | Required signals declared per architecture (not copy); no signals on FORBIDDEN blocks |
| **Failure criteria** | Missing content contract binding; signal on wrong block |

**Maps to category:** `CONTENT`

---

### GATE_VALIDATION_COMPLETE

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm upstream validation layers PASS for scope |
| **Inputs** | Page block validation runs (VALIDATION-CONTRACT), content validation runs (CONTENT-VALIDATION-CONTRACT) |
| **Pass criteria** | All in-scope pages: page-block validation `PASS` or `PASS_WITH_WARNINGS` (no CRITICAL); content validation same; no open ERROR |
| **Failure criteria** | Any in-scope validation `FAIL`; CRITICAL block missing; unresolved content validation ERROR |

**Maps to category:** `CONTENT_VALIDATION` (+ partial `ARCHITECTURE` for block validation)

---

### GATE_GENERATION_READY

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm generation contract complete and generation gates PASS |
| **Inputs** | GENERATION-CONTRACT-v1, GENERATION-GATES evidence, expected outputs declared |
| **Pass criteria** | `generation_id` linked; `GATE_GENERATION_READY` = PASS; handoff package structure defined (architecture only) |
| **Failure criteria** | Generation contract missing; generation gate FAIL; outputs undefined |

**Maps to category:** `GENERATION_READINESS`

---

### GATE_PRODUCTION_QA_PASS

| Attribute | Value |
|-----------|-------|
| **Purpose** | Confirm this Production QA run completed with acceptable aggregate status |
| **Inputs** | Completed PRODUCTION-QA-CONTRACT, checklist, matrix overlay, failure/warning register |
| **Pass criteria** | Contract `status` ∈ { `PASS`, `PASS_WITH_WARNINGS` }; all gates 1–8 PASS; no BLOCKER; operator sign-off |
| **Failure criteria** | Contract `FAIL` or `BLOCKED`; unresolved BLOCKER/CRITICAL; checklist incomplete |

**Maps to category:** all categories aggregated

---

### GATE_FRONTEND_HANDOFF_APPROVED

| Attribute | Value |
|-----------|-------|
| **Purpose** | Authorize architectural handoff to Frontend Layer (not deploy) |
| **Inputs** | `GATE_PRODUCTION_QA_PASS`, FRONTEND_HANDOFF_PACKAGE ref from generation outputs, operator approval |
| **Pass criteria** | QA PASS recorded; handoff package complete per GENERATION-OUTPUTS; explicit operator approval timestamp |
| **Failure criteria** | Handoff before QA pass; incomplete handoff package; missing generation link |

**Maps to category:** `HANDOFF_READINESS`

---

## 3. Gate ordering

```text
GATE_ARCHITECTURE_COMPLETE
        ↓
GATE_LEGAL_COMPLETE ──→ GATE_ENTITY_VERIFIED (parallel when applicable)
        ↓
GATE_SEO_COMPLETE
        ↓
GATE_DESIGN_COMPLETE
        ↓
GATE_CONTENT_COMPLETE
        ↓
GATE_VALIDATION_COMPLETE
        ↓
GATE_GENERATION_READY
        ↓
GATE_PRODUCTION_QA_PASS
        ↓
GATE_FRONTEND_HANDOFF_APPROVED
```

**Hard stop:** any gate `FAIL` before step 9 → do not approve Frontend Handoff.

---

## 4. Gate status values

| Value | Meaning |
|-------|---------|
| `PASS` | Criteria met |
| `PASS_WITH_WARNINGS` | Met with documented waivers (upstream allowed) |
| `FAIL` | Criteria not met |
| `NOT_APPLICABLE` | Conditional gate skipped with evidence |
| `BLOCKED` | Cannot evaluate — prerequisites missing |

---

*Production QA Gates v1 — human-operated checkpoints only.*
