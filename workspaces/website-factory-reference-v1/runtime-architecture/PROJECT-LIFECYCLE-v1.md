# Website Factory — Project Lifecycle v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/runtime-architecture/`  
**Статус:** project lifecycle — **documentation only**  
**Связь:** [RUNTIME-ARCHITECTURE-SYSTEM-v1.md](RUNTIME-ARCHITECTURE-SYSTEM-v1.md), [PROJECT-STATE-MODEL-v1.md](PROJECT-STATE-MODEL-v1.md)

**Не является:** Gantt schedule, BPMN executable, sprint plan, Jira workflow.

---

## 1. Назначение

Project Lifecycle v1 описывает **полный жизненный цикл** Website Factory проекта от первого intake до terminal `COMPLETE` — в терминах **архитектурных фаз**, не исполнения.

---

## 2. Lifecycle overview

```text
Phase 0   INTAKE              → NEW_PROJECT
Phase 1   CLASSIFICATION      → CLASSIFIED
Phase 2   BLUEPRINT           → BLUEPRINT_READY
Phase 3   PAGE ARCHITECTURE   → PAGE_READY
Phase 4   BLOCKS              → BLOCK_READY
Phase 5   VALIDATION          → VALIDATED
Phase 6   SEO                 → SEO_READY
Phase 7   DESIGN              → DESIGN_READY
Phase 8   CONTENT             → CONTENT_READY
Phase 9   CONTENT VALIDATION  → CONTENT_VALIDATED
Phase 10  GENERATION READY    → GENERATION_READY
Phase 11  PRODUCTION QA       → PRODUCTION_QA_READY
Phase 12  FRONTEND HANDOFF    → FRONTEND_READY
Phase 13  CLOSURE             → COMPLETE

Parallel (FULL_SITE / legal scope):
  Legal Pack + Entity Discovery — gates GL-LEGAL throughout; mandatory before Phase 10 exit
```

---

## 3. Phase catalogue

| Phase | ID | Target state | Primary work | Gate (runtime) |
|-------|-----|--------------|--------------|----------------|
| **0** | `LC-00` | `NEW_PROJECT` | Project charter, scope, intake record | Intake Complete |
| **1** | `LC-01` | `CLASSIFIED` | Resolve `site_type_code`, Core vs Extended | Classification Complete |
| **2** | `LC-02` | `BLUEPRINT_READY` | Select & freeze blueprint | Blueprint Approved |
| **3** | `LC-03` | `PAGE_READY` | Instantiate page contracts | Page Architecture Approved |
| **4** | `LC-04` | `BLOCK_READY` | Map `block_id` stacks | Block Mapping Complete |
| **5** | `LC-05` | `VALIDATED` | Page → block validation | Validation Pass |
| **6** | `LC-06` | `SEO_READY` | Apply SEO architecture | SEO Approved |
| **7** | `LC-07` | `DESIGN_READY` | Bind visual patterns | Design Approved |
| **8** | `LC-08` | `CONTENT_READY` | Bind content signals | Content Approved |
| **9** | `LC-09` | `CONTENT_VALIDATED` | Content signal validation | Content Validation Pass |
| **10** | `LC-10` | `GENERATION_READY` | Legal + generation gates | Generation Ready |
| **11** | `LC-11` | `PRODUCTION_QA_READY` | Production QA review | Production QA Pass |
| **12** | `LC-12` | `FRONTEND_READY` | Handoff package to Frontend | Frontend Handoff Approved |
| **13** | `LC-13` | `COMPLETE` | Operator closure | Project Complete |

---

## 4. Lifecycle rules (global)

| Rule ID | Rule |
|---------|------|
| **LR-01** | Phases execute **in order** unless explicit rollback charter (human-operated). |
| **LR-02** | **No skip-forward** — e.g. cannot reach `SEO_READY` without `VALIDATED`. |
| **LR-03** | Upstream **FAIL / CRITICAL** → halt at current phase; state does not advance. |
| **LR-04** | Extended site types (`SAAS`, `WEB_APPLICATION`, `MARKETPLACE`) require **charter** before `CLASSIFIED` → production path. |
| **LR-05** | Legal Pack (FROZEN) — no architectural modification during lifecycle; only application per mapping. |
| **LR-06** | `COMPLETE` requires `FRONTEND_READY` + Frontend Handoff Approved + operator sign-off. |
| **LR-07** | Partial / design-only projects may **narrow scope** via charter — documented exclusions; default = full chain. |

---

## 5. Stop points (lifecycle halt)

| Stop ID | Phase | Trigger | Resume |
|---------|-------|---------|--------|
| **LS-01** | LC-01 | Unclassifiable `site_type_code` | Operator classification |
| **LS-02** | LC-02 | No canonical blueprint (Core) | Blueprint delivery or reclassify |
| **LS-03** | LC-05 | Page Block Validation FAIL/CRITICAL | Fix stack; re-validate |
| **LS-04** | LC-06 | SEO contract gaps | Complete SEO profile |
| **LS-05** | LC-07 | Missing `VF_*` for required block | Complete design mapping |
| **LS-06** | LC-09 | Content Validation FAIL/CRITICAL | Fix signals |
| **LS-07** | LC-10 | Legal placeholder / entity NOT_READY | Legal path complete |
| **LS-08** | LC-11 | Production QA FAIL | Remediate per PRODUCTION-QA-FAILURE-LIBRARY |
| **LS-09** | LC-12 | Handoff package incomplete | Complete GENERATION-OUTPUTS |

---

## 6. Approval points (HITL)

| Approval ID | Phase transition | Approver |
|-------------|------------------|----------|
| **AP-01** | `NEW_PROJECT` → `CLASSIFIED` | Operator |
| **AP-02** | → `BLUEPRINT_READY` | Operator — Blueprint Approved |
| **AP-03** | → `PAGE_READY` | Operator — Page Architecture Approved |
| **AP-04** | → `SEO_READY` | Operator — SEO Approved |
| **AP-05** | → `DESIGN_READY` | Operator — Design Approved |
| **AP-06** | → `CONTENT_READY` | Operator — Content Approved |
| **AP-07** | → `GENERATION_READY` | Operator — Generation Ready sign-off |
| **AP-08** | → `FRONTEND_READY` | Operator — Frontend Handoff Approved |
| **AP-09** | → `COMPLETE` | Operator — project closure |

Validation Pass (LC-05) and Content Validation Pass (LC-09) are **gate outcomes** — operator confirms recorded PASS; not implicit automation.

---

## 7. Rollback (documentation semantics)

Rollback = **declared move to earlier state** with operator record:

| From | Allowed rollback target | Condition |
|------|---------------------------|-----------|
| `SEO_READY` | `VALIDATED` | SEO architecture rework |
| `DESIGN_READY` | `SEO_READY` | Design mapping rework only |
| `CONTENT_READY` | `DESIGN_READY` | Content contract rework |
| `GENERATION_READY` | `CONTENT_VALIDATED` | Scope change — charter |
| `FRONTEND_READY` | `PRODUCTION_QA_READY` | Handoff rejected |

**Forbidden rollback:** `COMPLETE` → any (terminal); `FRONTEND_READY` → skip Production QA.

---

## 8. Relationship to Generation Lifecycle

[GENERATION-LIFECYCLE-v1.md](../generation-contracts/GENERATION-LIFECYCLE-v1.md) describes **production stages inside** Generation Layer.

Project Lifecycle v1 is **superset** — includes pre-generation architecture phases (Classification through Content Validation) and post-generation Production QA / Handoff / Complete.

| Generation stage | Project lifecycle phase |
|------------------|---------------------------|
| GL-01 Classify | LC-01 |
| GL-02 Blueprint | LC-02 |
| GL-03–05 Page/Block/Validation | LC-03–05 |
| GL-06 SEO | LC-06 |
| GL-07–09 Design/Content/Content Val | LC-07–09 |
| GL-10–11 Legal & Generation Ready | LC-10 |
| GL-12–13 Spec / Handoff | LC-10–12 |
| — Production QA | LC-11 |
| — Complete | LC-13 |

---

*Project Lifecycle v1 — 2026-06-01. Documentation only.*
