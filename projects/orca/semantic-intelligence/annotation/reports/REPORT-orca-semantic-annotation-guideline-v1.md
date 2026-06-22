# REPORT — ORCA SEMANTIC INTELLIGENCE — ANNOTATION GUIDELINE V1

**Task:** P0-B operator approval checkpoint + P0-C Annotation Guideline drafting  
**Date:** 2026-06-22  
**Branch:** `mars/post-cycle8-live-tests`  
**P0-B checkpoint commit:** `3151953`  
**P0-C status:** `PROPOSED — OPERATOR APPROVAL REQUIRED` (uncommitted)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | `mars/post-cycle8-live-tests` — **CONFIRMED** |
| Architecture checkpoint `f17c270` in history | **CONFIRMED** (`git log`) |
| HEAD newer than `f17c270` | **CONFIRMED** (`3151953` — unrelated FP-0002 commits retained; no rollback) |
| P0-B files existed uncommitted at task start | **CONFIRMED** |
| P0-B decision record was PROPOSED before task | **CONFIRMED** |
| Corvonero frozen | **CONFIRMED** (OPERATIONAL-INDEX, clean-room PROJECT) |
| P0-C guideline did not exist at task start | **CONFIRMED** |
| Benchmark / classifier / semantic rerun not started | **CONFIRMED** |
| Unrelated WIP not staged in P0-B commit | **CONFIRMED** (55 files, ORCA semantic scope only) |

---

## 2. Operator Approval B1–B7

Recorded in:

- [`decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md`](../decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md)
- [`decisions/orca-p0-b-taxonomy-and-schema-operator-approval-v1.json`](../decisions/orca-p0-b-taxonomy-and-schema-operator-approval-v1.json)

| ID | Decision |
|----|----------|
| B1 | Taxonomy: `APPROVED — IMPLEMENTATION NOT STARTED` |
| B2 | Schema: `APPROVED — IMPLEMENTATION NOT STARTED` |
| B3 | Admission outputs: ACCEPT, REJECT, ABSTAIN |
| B4 | Core distinctions approved (intent ≠ eligibility, topic ≠ intent, etc.) |
| B5 | Schema authority for annotation, benchmark, baseline, evaluation, Semantic Core |
| B6 | Runtime validation not required for P0-B; required before benchmark/baseline/production |
| B7 | P0-C authorization: `AUTHORIZED` |

---

## 3. P0-B Status Updates

| Artifact | Prior | Current |
|----------|-------|---------|
| P0-B decision record | PROPOSED | APPROVED — IMPLEMENTATION NOT STARTED |
| Taxonomy/schema package headers | PROPOSED | APPROVED — IMPLEMENTATION NOT STARTED |
| semantic-intelligence README | PROPOSED | APPROVED — CHECKPOINTED |
| Promotion backlog P0-B | PROPOSED | APPROVED — CHECKPOINTED |

---

## 4. Selective P0-B Checkpoint

| Field | Value |
|-------|-------|
| Commit | `3151953` |
| Message | `docs(orca): approve semantic taxonomy and record schema v1` |
| Push | **SUCCESS** → `origin/mars/post-cycle8-live-tests` |
| Files | 55 (semantic-intelligence package + map updates in allowed scope) |
| Isolation | **PASS** — no P0-C, Corvonero diagnostic, MIG, OCPilot, Website Factory, `.recovery-temp` |

---

## 5. P0-C Authority

**Authoritative:** ADR v1, P0-B taxonomy/schema, invariants, admission policy, risk modes, D1–D7, A1–A7, B1–B7.

**Analytical support:** world-practice research, source ledger, failure-mode catalogue.

**Diagnostic only:** Corvonero clean-room examples, old over-admission patterns, Triumph lessons.

**Forbidden as annotation truth:** old Corvonero labels, ACTIVE/HOLD/EXCLUDE, prior mappings, model explanations from defective pipelines.

---

## 6. Annotation Guideline

Created [`guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md) + JSON counterpart with 20 required sections (Purpose through Versioning).

---

## 7. Required Annotation Order

Mandatory 10-step sequence documented in guideline § and cross-referenced in decision trees:

1. Read literally  
2. Identify likely next user action  
3. Extract signals  
4. Assign primary and secondary intent (no eligibility yet)  
5. Assess competing interpretations  
6. Assess provider-hire likelihood  
7. Check landing compatibility  
8. Assign eligibility (ACCEPT / REJECT / ABSTAIN)  
9. Assess risk and review requirement  
10. Record decision trace  

---

## 8. Commercial Evidence Standard

[`guidelines/ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md`](../guidelines/ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md) — strong/weak evidence, lexicon (услуга, заказать, подрядчик, …), evidence ≠ auto-ACCEPT.

---

## 9. Protected Non-Commercial Standard

[`guidelines/ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md`](../guidelines/ORCA-PROTECTED-NONCOMMERCIAL-INTENT-STANDARD-v1.md) — career, employee hiring, education, DIY, regulatory, navigational, free/download.

---

## 10. Problem Query Standard

[`guidelines/ORCA-PROBLEM-QUERY-ADJUDICATION-v1.md`](../guidelines/ORCA-PROBLEM-QUERY-ADJUDICATION-v1.md) — three interpretations; problem signal alone ≠ ACCEPT.

---

## 11. Product-versus-Service Standard

[`guidelines/ORCA-PRODUCT-VS-SERVICE-ADJUDICATION-v1.md`](../guidelines/ORCA-PRODUCT-VS-SERVICE-ADJUDICATION-v1.md).

---

## 12. Short Head Term Standard

[`guidelines/ORCA-SHORT-HEAD-TERM-ADJUDICATION-v1.md`](../guidelines/ORCA-SHORT-HEAD-TERM-ADJUDICATION-v1.md).

---

## 13. ACCEPT Standard

[`guidelines/ORCA-ACCEPT-STANDARD-v1.md`](../guidelines/ORCA-ACCEPT-STANDARD-v1.md) — 7 requirements; explicit / implicit / operator-seed types.

---

## 14. REJECT Standard

[`guidelines/ORCA-REJECT-STANDARD-v1.md`](../guidelines/ORCA-REJECT-STANDARD-v1.md).

---

## 15. ABSTAIN Standard

[`guidelines/ORCA-ABSTAIN-STANDARD-v1.md`](../guidelines/ORCA-ABSTAIN-STANDARD-v1.md).

---

## 16. Phrase-Specific Rationale Standard

[`guidelines/ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md`](../guidelines/ORCA-PHRASE-SPECIFIC-RATIONALE-STANDARD-v1.md).

---

## 17. Decision Trees

[`decision-trees/ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md`](../decision-trees/ORCA-SEMANTIC-ANNOTATION-DECISION-TREE-v1.md) + JSON — 9 subtrees; terminals ACCEPT / REJECT / ABSTAIN only.

---

## 18. Example Library

[`examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md`](../examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md) + JSON — 110 training illustrations (≥ minimums for all required classes). **Not gold benchmark.**

---

## 19. Anti-Pattern Library

[`examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md`](../examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md) — 16 anti-patterns with detection rules.

---

## 20. Reviewer Checklist

[`reviewer-tools/ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md`](../reviewer-tools/ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md) + JSON.

---

## 21. Annotator Roles

[`reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md`](../reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md).

---

## 22. Disagreement and Adjudication

[`adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md`](../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md) + JSON.

---

## 23. Annotation Quality Gates

[`quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md`](../quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md) + JSON. D3 thresholds operator-approved; new numerics `PROPOSED — BENCHMARK CHARTER REQUIRED`.

---

## 24. Annotator Readiness Plan

[`quality/ORCA-ANNOTATOR-READINESS-PLAN-v1.md`](../quality/ORCA-ANNOTATOR-READINESS-PLAN-v1.md) — 6-step future certification; no qualification answers created.

---

## 25. Validation

[`validation/ORCA-ANNOTATION-GUIDELINE-VALIDATION-v1.md`](../validation/ORCA-ANNOTATION-GUIDELINE-VALIDATION-v1.md) + JSON — documentation validation **PASS** (all Part 25 criteria).

---

## 26. P0-C Decision Record

[`decisions/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md`](../decisions/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md) + JSON — status `PROPOSED — OPERATOR APPROVAL REQUIRED`.

---

## 27. Map and Backlog Updates

Updated (uncommitted with P0-C):

- ORCA Operational Index — P0-C section added
- ORCA README — P0-C proposed
- Semantic Intelligence README — annotation locus
- Architecture semantic-intelligence README — gates
- Promotion backlog MD + JSON — P0-C PROPOSED

| Gate | Status |
|------|--------|
| P0-A | APPROVED — CHECKPOINTED |
| P0-B | APPROVED — CHECKPOINTED (`3151953`) |
| P0-C | PROPOSED — OPERATOR REVIEW |
| P0-D | BLOCKED UNTIL P0-C APPROVAL |
| Corvonero | FROZEN |
| Campaign Production | BLOCKED |

---

## 28. Files Created or Changed

### Committed (P0-B checkpoint `3151953`)

55 files under `projects/orca/semantic-intelligence/` + map updates in allowed scope.

### Created uncommitted (P0-C)

30 files under `projects/orca/semantic-intelligence/annotation/`:

- README.md
- guidelines/ (11 files)
- decision-trees/ (2)
- examples/ (3)
- reviewer-tools/ (3)
- adjudication/ (2)
- quality/ (3)
- validation/ (2)
- decisions/ (2)
- reports/ (this file)

### Modified uncommitted (P0-C map updates)

- `projects/orca/semantic-intelligence/README.md`
- `projects/orca/OPERATIONAL-INDEX.md`
- `projects/orca/README.md`
- `projects/orca/architecture/semantic-intelligence/README.md`
- `projects/orca/research/ppc-semantic-intelligence/world-practice-2026-06/promotion/*`

---

## 29. Git Status

```
 M projects/orca/OPERATIONAL-INDEX.md
 M projects/orca/README.md
 M projects/orca/architecture/semantic-intelligence/README.md
 M projects/orca/research/.../promotion/* (2 files)
 M projects/orca/semantic-intelligence/README.md
?? projects/orca/semantic-intelligence/annotation/ (30 files)
```

P0-C intentionally **not committed** per task stop condition.

---

## 30. SAFE UNKNOWN

| Item | Status |
|------|--------|
| Automated AJV validator for semantic records | Not implemented; required before benchmark automation |
| Qualification set answers for annotator certification | Not created (deferred) |
| Numerical quality-gate thresholds beyond D3 | PROPOSED — BENCHMARK CHARTER REQUIRED |
| Corvonero pilot phrase selection | Deferred to P0-E |

---

## 31. Operator Approval Items

Operator must approve P0-C package:

1. Annotation handbook and 10-step order  
2. Commercial evidence and protected-intent standards  
3. Problem / product / short-head adjudication standards  
4. ACCEPT / REJECT / ABSTAIN standards  
5. Phrase-specific rationale requirement  
6. Decision trees  
7. Example library role (training only)  
8. Anti-pattern library  
9. Reviewer checklist and role model  
10. Disagreement and adjudication policy  
11. Quality gates (proposed numerics)  
12. Annotator readiness plan  
13. P0-C decision record sign-off  

---

## 32. Next Gate

**OPERATOR APPROVAL OF ORCA SEMANTIC ANNOTATION GUIDELINE V1**

After approval → **P0-D BENCHMARK CHARTER**

---

## 33. Stop Condition

**MET.**

- P0-B approval recorded and checkpointed (`3151953`)  
- P0-C guideline drafted (uncommitted)  
- No benchmark, gold labels, classifier, Corvonero rerun, or campaign production started  
- No P0-C self-approval on behalf of operator  

**STOP.**
