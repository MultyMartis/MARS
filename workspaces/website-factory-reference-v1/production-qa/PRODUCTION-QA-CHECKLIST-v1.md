# Website Factory — Production QA Checklist v1

**Версия:** v1  
**Область:** `workspaces/website-factory-reference-v1/production-qa/`  
**Статус:** master architectural readiness checklist — **documentation only**  
**Связь:** [PRODUCTION-QA-CONTRACT-v1.md](PRODUCTION-QA-CONTRACT-v1.md), [PRODUCTION-QA-MATRIX-v1.md](PRODUCTION-QA-MATRIX-v1.md), [../frontend-rules/WF-GRID-DISCIPLINE-v1.md](../frontend-rules/WF-GRID-DISCIPLINE-v1.md), [../frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md](../frontend-rules/WF-LAYOUT-DISCIPLINE-v1.md)

**Не является:** runtime test script, Playwright spec, deploy checklist, code review template.

---

## Назначение

Master checklist для operator-led Production QA run. Каждый пункт — **architecture artefact** presence/consistency, не implementation quality.

**How to use:** Complete for `project_scope`; attach completed checklist ref to `qa_run_id` in Production QA Contract.

**Legend:** ☐ unchecked | ☑ pass | ⚠ pass with waiver | ✗ fail

---

## A. Project identification

| # | Check | Gate / category |
|---|-------|-----------------|
| A1 | ☐ `project_slug` and `qa_run_id` assigned | Contract |
| A2 | ☐ `site_type_code` ∈ Core 5 (or Extended with charter) | ARCHITECTURE |
| A3 | ☐ `scope_type` and route list documented | Contract |
| A4 | ☐ `generation_id` linked to active generation contract | GENERATION_READINESS |

---

## B. Architecture foundation

| # | Check | Gate / category |
|---|-------|-----------------|
| B1 | ☐ Site type registered and matches project charter | ARCHITECTURE |
| B2 | ☐ **Blueprint exists** — canonical doc for `site_type_code` | GATE_ARCHITECTURE_COMPLETE |
| B3 | ☐ Blueprint exclusions respected in scope | ARCHITECTURE |
| B4 | ☐ **Page contracts exist** for every in-scope route | GATE_ARCHITECTURE_COMPLETE |
| B5 | ☐ Each `page_type` allowed for `site_type_code` per PAGE-TYPE-REGISTRY | ARCHITECTURE |
| B6 | ☐ **Block mapping exists** — PAGE-BLOCK-MAPPING + blueprint block intent | ARCHITECTURE |
| B7 | ☐ All `block_id` in scope ∈ BLOCK-REGISTRY (29) | ARCHITECTURE |
| B8 | ☐ No FORBIDDEN blocks on any in-scope page | VALIDATION |

---

## C. Validation layers

| # | Check | Gate / category |
|---|-------|-----------------|
| C1 | ☐ Page block validation runs exist for all in-scope pages | GATE_VALIDATION_COMPLETE |
| C2 | ☐ **Validation passed** — no FAIL; no unresolved CRITICAL | GATE_VALIDATION_COMPLETE |
| C3 | ☐ Content validation runs exist for in-scope blocks/pages | CONTENT_VALIDATION |
| C4 | ☐ Content validation **passed** — no open ERROR | CONTENT_VALIDATION |

---

## D. SEO

| # | Check | Gate / category |
|---|-------|-----------------|
| D1 | ☐ **SEO profile exists** — SITE-TYPE-SEO-MAPPING-v2 + strategy contract | GATE_SEO_COMPLETE |
| D2 | ☐ PAGE-SEO-CONTRACT per in-scope `page_type` | SEO |
| D3 | ☐ Search intent model aligned with blueprint IA | SEO |

---

## E. Design

| # | Check | Gate / category |
|---|-------|-----------------|
| E1 | ☐ **Design mapping exists** — DESIGN-SYSTEM-MAPPING for site type | GATE_DESIGN_COMPLETE |
| E2 | ☐ BLOCK-VISUAL-MAPPING for all required in-scope blocks | DESIGN |
| E3 | ☐ `VF_*` pattern selections documented (architecture, not CSS) | DESIGN |
| E4 | ☐ **Frontend handoff** cites WF Grid Discipline — implementation QA must run WF-GRID-005 before visual PASS | DESIGN / HANDOFF |
| E5 | ☐ **Frontend handoff** cites WF Layout Discipline — inner-zone authority documented; WF-LAYOUT-006 collapse not SAFE UNKNOWN before production freeze | DESIGN / HANDOFF |

---

## F. Content

| # | Check | Gate / category |
|---|-------|-----------------|
| F1 | ☐ **Content contracts exist** — block + page level for scope | GATE_CONTENT_COMPLETE |
| F2 | ☐ Required `signal_id` declared per CONTENT-SIGNAL-REGISTRY | CONTENT |
| F3 | ☐ **No placeholder leakage** in signal architecture declarations | CONTENT / DOCUMENTATION |
| F4 | ☐ Forbidden signals absent on FORBIDDEN blocks | CONTENT |

---

## G. Legal & entity

| # | Check | Gate / category |
|---|-------|-----------------|
| G1 | ☐ **Legal Pack complete** for `site_type_code` — FROZEN refs pinned | GATE_LEGAL_COMPLETE |
| G2 | ☐ LEGAL_PAGE contracts for all required legal routes | LEGAL |
| G3 | ☐ **Entity verified** — Entity Card READY or signed N/A | GATE_ENTITY_VERIFIED |
| G4 | ☐ Legal template hardening refs current (v1.1 where applicable) | LEGAL |

---

## H. Generation & handoff

| # | Check | Gate / category |
|---|-------|-----------------|
| H1 | ☐ **Generation contract ready** — all generation gates PASS | GATE_GENERATION_READY |
| H2 | ☐ Expected outputs declared (PAGE_BUILD_SPEC, BLOCK_STACK_SPEC, SEO_SPEC, DESIGN_SPEC, CONTENT_SPEC, FRONTEND_HANDOFF_PACKAGE) | GENERATION_READINESS |
| H3 | ☐ Generation not started before upstream readiness (no PQF-009) | GENERATION_READINESS |
| H4 | ☐ **No unresolved failures** in upstream contracts (validation, content, generation) | All |
| H5 | ☐ Production QA categories reviewed (10) | GATE_PRODUCTION_QA_PASS |
| H6 | ☐ **Handoff not approved** before QA pass (no PQF-010) | HANDOFF_READINESS |

---

## I. Documentation integrity

| # | Check | Gate / category |
|---|-------|-----------------|
| I1 | ☐ All layer refs point to ACCEPTED or FROZEN artefacts | DOCUMENTATION_INTEGRITY |
| I2 | ☐ No superseded docs without banner (e.g. SEO v1 alone) | DOCUMENTATION_INTEGRITY |
| I3 | ☐ Version pins recorded in `required_inputs` | DOCUMENTATION_INTEGRITY |
| I4 | ☐ Operator sign-off fields populated for PASS | Contract |

---

## J. Aggregate sign-off

| # | Check | Result |
|---|-------|--------|
| J1 | ☐ All **R** matrix cells satisfied per [PRODUCTION-QA-MATRIX-v1.md](PRODUCTION-QA-MATRIX-v1.md) | |
| J2 | ☐ Production QA contract `status` computed | |
| J3 | ☐ `GATE_PRODUCTION_QA_PASS` = PASS or PASS_WITH_WARNINGS | |
| J4 | ☐ `GATE_FRONTEND_HANDOFF_APPROVED` — operator explicit approval | |

---

## Checklist outcome template

```text
qa_run_id:     pqa-{slug}-{date}-{seq}
project_slug:  _______________
site_type:     _______________
scope_type:    FULL_SITE | PAGE_SUBSET | ...
checklist_date: _______________
operator:      _______________

Summary:
  PASS items:     __ / __
  WARN items:     __
  FAIL items:     __
  BLOCKED items:  __

Contract status: PASS | PASS_WITH_WARNINGS | FAIL | BLOCKED
```

---

*Production QA Checklist v1 — architecture readiness only.*
