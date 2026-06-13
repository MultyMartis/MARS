# Website Factory — State Transition Rules v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** transition discipline — **documentation only**  
**Связь:** [PROJECT-STATE-MODEL-v1.md](PROJECT-STATE-MODEL-v1.md), [RUNTIME-GATES-v1.md](RUNTIME-GATES-v1.md)

---

## 1. Назначение

State Transition Rules v1 — **полная дисциплина переходов** между canonical project states. Правила обязательны для human-operated Factory tracking; не исполняются автоматически в v1.

---

## 2. Forward transition matrix (allowed)

| From → To | Rule ID | Preconditions |
|-----------|---------|---------------|
| `NEW_PROJECT` → `CLASSIFIED` | **TR-01** | Intake Complete; `site_type_code` assigned |
| `CLASSIFIED` → `BLUEPRINT_READY` | **TR-02** | Classification Complete; canonical blueprint exists (Core) or charter (Extended) |
| `BLUEPRINT_READY` → `PAGE_READY` | **TR-03** | Blueprint Approved |
| `PAGE_READY` → `BLOCK_READY` | **TR-04** | Page Architecture Approved |
| `BLOCK_READY` → `VALIDATED` | **TR-05** | Block Mapping Complete |
| `VALIDATED` → `SEO_READY` | **TR-06** | Validation Pass |
| `SEO_READY` → `DESIGN_READY` | **TR-07** | SEO Approved |
| `DESIGN_READY` → `CONTENT_READY` | **TR-08** | Design Approved |
| `CONTENT_READY` → `CONTENT_VALIDATED` | **TR-09** | Content Approved |
| `CONTENT_VALIDATED` → `GENERATION_READY` | **TR-10** | Content Validation Pass; Legal gates PASS when required |
| `GENERATION_READY` → `PRODUCTION_QA_READY` | **TR-11** | Generation Ready; spec package assembled |
| `PRODUCTION_QA_READY` → `FRONTEND_READY` | **TR-12** | Production QA Pass |
| `FRONTEND_READY` → `COMPLETE` | **TR-13** | Frontend Handoff Approved |

---

## 3. Forbidden transitions (hard rules)

| Rule ID | Forbidden transition | Rationale |
|---------|---------------------|-----------|
| **FT-01** | Any → `SEO_READY` without prior `VALIDATED` | SEO consumes validated block architecture |
| **FT-02** | Any → `DESIGN_READY` without prior `SEO_READY` | Design mapping follows SEO contracts |
| **FT-03** | Any → `CONTENT_READY` without prior `DESIGN_READY` | Content binds to visual pattern families |
| **FT-04** | Any → `CONTENT_VALIDATED` without prior `CONTENT_READY` | Validation requires bound signals |
| **FT-05** | Any → `GENERATION_READY` without prior `CONTENT_VALIDATED` | Generation requires validated content architecture |
| **FT-06** | Any → `PRODUCTION_QA_READY` without prior `GENERATION_READY` | QA reviews generation package |
| **FT-07** | Any → `FRONTEND_READY` without prior `PRODUCTION_QA_READY` | **No Frontend before Production QA Pass** |
| **FT-08** | Any → `COMPLETE` without prior `FRONTEND_READY` | **No Complete before Frontend Handoff Approved** |
| **FT-09** | Skip states (e.g. `CLASSIFIED` → `VALIDATED`) | No layer bypass |
| **FT-10** | `COMPLETE` → any | Terminal state |
| **FT-11** | `NEW_PROJECT` → `COMPLETE` | No empty closure |
| **FT-12** | `VALIDATED` → `DESIGN_READY` (skip SEO) | SEO layer mandatory in chain |
| **FT-13** | `BLOCK_READY` → `SEO_READY` (skip validation) | Validation gate mandatory |
| **FT-14** | `GENERATION_READY` → `FRONTEND_READY` (skip Production QA) | Production QA mandatory |
| **FT-15** | `PRODUCTION_QA_READY` → `COMPLETE` (skip Frontend) | Handoff mandatory |

---

## 4. Dependency rules (layer order)

```text
Classification < Blueprint < Page < Blocks < Validation
Validation < SEO < Design < Content < Content Validation
Content Validation < Generation Ready < Production QA < Frontend < Complete
```

| Rule ID | Statement |
|---------|-----------|
| **DR-01** | Cannot enter `SEO_READY` before `VALIDATED`. |
| **DR-02** | Cannot enter `CONTENT_READY` before `DESIGN_READY`. |
| **DR-03** | Cannot enter `FRONTEND_READY` before Production QA PASS (`PRODUCTION_QA_READY`). |
| **DR-04** | Cannot enter `COMPLETE` before Frontend Handoff Approved (`FRONTEND_READY`). |
| **DR-05** | Cannot enter `GENERATION_READY` before `CONTENT_VALIDATED`. |
| **DR-06** | Cannot enter `DESIGN_READY` before `SEO_READY`. |
| **DR-07** | Cannot enter `VALIDATED` before `BLOCK_READY`. |

---

## 5. Gate-gated transitions

Transition **executes** only when named runtime gate = PASS (see [RUNTIME-GATES-v1.md](RUNTIME-GATES-v1.md)):

| Transition | Gate required |
|------------|---------------|
| → `CLASSIFIED` | `RG-INTAKE_COMPLETE` |
| → `BLUEPRINT_READY` | `RG-CLASSIFICATION_COMPLETE` + `RG-BLUEPRINT_APPROVED` |
| → `PAGE_READY` | `RG-PAGE_ARCHITECTURE_APPROVED` |
| → `BLOCK_READY` | (mapping complete — no separate approval) |
| → `VALIDATED` | `RG-VALIDATION_PASS` |
| → `SEO_READY` | `RG-SEO_APPROVED` |
| → `DESIGN_READY` | `RG-DESIGN_APPROVED` |
| → `CONTENT_READY` | `RG-CONTENT_APPROVED` |
| → `CONTENT_VALIDATED` | `RG-CONTENT_VALIDATION_PASS` |
| → `GENERATION_READY` | `RG-GENERATION_READY` (+ legal sub-gates) |
| → `PRODUCTION_QA_READY` | `RG-PRODUCTION_QA_PASS` |
| → `FRONTEND_READY` | `RG-FRONTEND_HANDOFF_APPROVED` |
| → `COMPLETE` | `RG-PROJECT_COMPLETE` |

---

## 6. Rollback transitions (allowed with record)

| From | To | Rule ID | Condition |
|------|-----|---------|-----------|
| `CLASSIFIED` | `NEW_PROJECT` | **RB-01** | Intake rework |
| `BLUEPRINT_READY` | `CLASSIFIED` | **RB-02** | Reclassification |
| `PAGE_READY` | `BLUEPRINT_READY` | **RB-03** | Blueprint change |
| `BLOCK_READY` | `PAGE_READY` | **RB-04** | Page contract change |
| `VALIDATED` | `BLOCK_READY` | **RB-05** | Block stack change |
| `SEO_READY` | `VALIDATED` | **RB-06** | SEO rework only |
| `DESIGN_READY` | `SEO_READY` | **RB-07** | Design-only rework |
| `CONTENT_READY` | `DESIGN_READY` | **RB-08** | Content contract rework |
| `CONTENT_VALIDATED` | `CONTENT_READY` | **RB-09** | Signal binding fix |
| `GENERATION_READY` | `CONTENT_VALIDATED` | **RB-10** | Scope change — charter |
| `PRODUCTION_QA_READY` | `GENERATION_READY` | **RB-11** | Package rework |
| `FRONTEND_READY` | `PRODUCTION_QA_READY` | **RB-12** | Handoff rejected |

**Forbidden rollback:** any state → skip backward across more than one architectural layer without charter; `COMPLETE` → any.

---

## 7. Parallel legal track rules

| Rule ID | Statement |
|---------|-----------|
| **LR-01** | Legal Pack gates may be **worked** in parallel with LC-02–LC-09 but must **PASS** before `GENERATION_READY`. |
| **LR-02** | `card_status = NOT_READY` when entity required → **block** TR-10. |
| **LR-03** | Legal placeholder gate FAIL → **block** TR-10 (see Legal Pack generation contract). |

---

## 8. Extended type rules

| Rule ID | Statement |
|---------|-----------|
| **ER-01** | `SAAS`, `WEB_APPLICATION`, `MARKETPLACE` — TR-02 requires **operator charter** before `BLUEPRINT_READY`. |
| **ER-02** | Extended without charter — remain in `CLASSIFIED` or `NEW_PROJECT` (stop LS-01). |

---

## 9. Transition violation severity

| Violation | Severity | Action |
|-----------|----------|--------|
| Skip-forward (FT-09) | **CRITICAL** | Halt; record RF-SKIP-STATE |
| Frontend before QA (FT-07) | **CRITICAL** | Halt; record RF-QA-BYPASS |
| Complete before handoff (FT-08) | **CRITICAL** | Halt; record RF-HANDOFF-BYPASS |
| SEO before validation (FT-01) | **HIGH** | Halt; rollback to `VALIDATED` path |
| Content before design (FT-03) | **HIGH** | Halt; rollback |

See [RUNTIME-FAILURE-LIBRARY-v1.md](RUNTIME-FAILURE-LIBRARY-v1.md).

---

*State Transition Rules v1 — 2026-06-01.*
