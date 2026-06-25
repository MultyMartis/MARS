# REPORT — ORCA SEMANTIC INTELLIGENCE — UNIVERSAL BENCHMARK CHARTER V1

**Task:** P0-C operator approval checkpoint + P0-D Universal Benchmark Charter v1  
**Date:** 2026-06-22  
**Branch:** `mars/post-cycle8-live-tests`  
**P0-C checkpoint commit:** `78b0557` (pushed)  
**P0-D status:** `PROPOSED — OPERATOR APPROVAL REQUIRED` (uncommitted)

---

## 1. Preflight

| Check | Result |
|-------|--------|
| Branch | **CONFIRMED** — `mars/post-cycle8-live-tests` |
| HEAD before P0-C commit | `684e169` (unrelated FP-0002 work retained; no rollback) |
| P0-B checkpoint `3151953` in history | **CONFIRMED** |
| P0-C package existed uncommitted | **CONFIRMED** |
| P0-C decision was PROPOSED before task | **CONFIRMED** |
| Benchmark dataset did not exist | **CONFIRMED** |
| No Corvonero relabelling started | **CONFIRMED** |
| Classifier/runtime not started | **CONFIRMED** |
| Unrelated WIP not staged in P0-C commit | **CONFIRMED** (38 files, ORCA P0-C scope only) |

---

## 2. Operator Approval C1–C7

Recorded in [`annotation/decisions/ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md`](../annotation/decisions/ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md) and JSON counterpart.

| ID | Decision |
|----|----------|
| C1 | Guideline: `APPROVED — IMPLEMENTATION NOT STARTED` |
| C2 | Mandatory 10-step annotation order approved |
| C3 | ABSTAIN governance: mandatory safety outcome |
| C4 | Example library: training illustrations only |
| C5 | Double annotation direction authorized; SLA deferred to P0-D |
| C6 | D3 thresholds approved; all other numerics `PROPOSED — BENCHMARK VALIDATION REQUIRED` |
| C7 | P0-D authorization: `AUTHORIZED` |

---

## 3. P0-C Status Updates

| Artifact | Before | After |
|----------|--------|-------|
| P0-C decision record | PROPOSED | APPROVED — IMPLEMENTATION NOT STARTED |
| Annotation README | PROPOSED | APPROVED |
| Validation status | PROPOSED | APPROVED — DOCUMENTATION VALIDATION |
| Promotion backlog P0-C | PROPOSED | APPROVED — CHECKPOINTED |

---

## 4. Selective P0-C Checkpoint

| Field | Value |
|-------|-------|
| Commit | `78b0557` |
| Message | `docs(orca): approve semantic annotation guideline v1` |
| Files | 38 (annotation locus + map/backlog updates) |
| Push | **SUCCESS** — `origin/mars/post-cycle8-live-tests` |
| Isolation | **PASS** — no P0-D, Corvonero diagnostic, MIG, OCPilot, Website Factory, `.recovery-temp` |

---

## 5. P0-D Authority

**Authoritative:** ADR v1, P0-B taxonomy/schema, P0-C guideline (C1–C7), invariants, decision trees, reviewer roles, disagreement policy, D1–D7, A1–A7, B1–B7, C1–C7.

**Analytical support:** world-practice research, source ledger, benchmark recommendations, failure-mode catalogue, promotion matrix.

**Diagnostic only:** Corvonero clean-room failure, old over-admission examples — **not** ground truth.

**Forbidden as gold:** old Corvonero labels, ACTIVE/HOLD/EXCLUDE, old service mappings, example-library labels without independent re-annotation.

---

## 6. Benchmark Purpose and Non-Goals

Charter: [`charters/ORCA-UNIVERSAL-SEMANTIC-BENCHMARK-CHARTER-v1.md`](charters/ORCA-UNIVERSAL-SEMANTIC-BENCHMARK-CHARTER-v1.md)

Independent evaluation source of truth for semantic admission; measures commercial precision, protected FPR, ABSTAIN behavior, intent/ambiguity detection. Non-goals: maximize size, reproduce Wordstat exactly, campaign core, train=test leakage, automation rate over precision.

---

## 7. Universal Benchmark and Corvonero Pilot Model

| Product | Size | Purpose |
|---------|------|---------|
| Universal ORCA Benchmark | 1,200–2,000 adjudicated phrases | Cross-domain evaluation, regression, model comparison |
| Corvonero Pilot Set | 300–500 phrases | B2B 1C/ERP domain pilot; restart gate |

Corvonero pilot cannot dominate universal benchmark; explicit split/provenance required for any contribution.

---

## 8. Domain Coverage

[`strata/ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md`](strata/ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md) + JSON — 8 domains including B2B IT, local professional, repair/technical, logistics, ecommerce+service, compliance, integration/implementation. Source availability marked per domain; no false data-exists claims.

---

## 9. Intent Strata

[`strata/ORCA-BENCHMARK-INTENT-STRATA-v1.md`](strata/ORCA-BENCHMARK-INTENT-STRATA-v1.md) + JSON — **26 strata** covering all task-required intent classes, ambiguity families, short head, malformed, irrelevant, unknown.

---

## 10. Difficulty Strata

[`strata/ORCA-BENCHMARK-DIFFICULTY-STRATA-v1.md`](strata/ORCA-BENCHMARK-DIFFICULTY-STRATA-v1.md) — EASY, MODERATE, HARD, ADVERSARIAL with multi-signal difficulty model (not length-only).

---

## 11. Source Policy

[`sources/ORCA-BENCHMARK-SOURCE-POLICY-v1.md`](sources/ORCA-BENCHMARK-SOURCE-POLICY-v1.md) + JSON — provenance fields, licensing, synthetic tagging, forbidden old-label authority.

---

## 12. Sampling Plan

[`sampling/ORCA-UNIVERSAL-BENCHMARK-SAMPLING-PLAN-v1.md`](sampling/ORCA-UNIVERSAL-BENCHMARK-SAMPLING-PLAN-v1.md) + JSON — stratified + random within strata, protected oversampling, domain/frequency/tail balancing, minimal pairs, blind sampling; anti-cherry-picking rules.

---

## 13. Size Plan

| Phase | Size | Purpose |
|-------|------|---------|
| B0 | 60–100 | Qualification — protocol only |
| B1 | 300–500 | Pilot + first comparison |
| B2 | 1,200–2,000 | Production gating baseline |

Sizes are operator-approved planning ranges, not statistical sufficiency proof.

---

## 14. Split Policy

[`splits/ORCA-BENCHMARK-SPLIT-POLICY-v1.md`](splits/ORCA-BENCHMARK-SPLIT-POLICY-v1.md) + JSON — qualification, development, validation, blind test, hard-negative test, regression anchor, Corvonero pilot, future domain transfer. Group-aware splitting for near-duplicates and minimal pairs.

---

## 15. Blind Test Governance

[`leakage-control/ORCA-BLIND-TEST-GOVERNANCE-v1.md`](leakage-control/ORCA-BLIND-TEST-GOVERNANCE-v1.md) — owner, access boundary, logging, contamination response, prompt/training restrictions. Corvonero blind planning minimum: **≥ 100 unseen phrases**. Blind set **not created** in this task.

---

## 16. Double Annotation

[`annotation/ORCA-BENCHMARK-DOUBLE-ANNOTATION-POLICY-v1.md`](annotation/ORCA-BENCHMARK-DOUBLE-ANNOTATION-POLICY-v1.md) + JSON — independent blind passes, mandatory for B0, Corvonero pilot, blind test, protected strata, hard negatives, adversarial. Long-term universal %: **OPERATOR DECISION REQUIRED AFTER B0**.

---

## 17. Adjudication

[`adjudication/ORCA-BENCHMARK-ADJUDICATION-POLICY-v1.md`](adjudication/ORCA-BENCHMARK-ADJUDICATION-POLICY-v1.md) + JSON — mandatory adjudication on eligibility, protected-intent, ACCEPT vs ABSTAIN disagreements; adjudicator must not choose more commercial interpretation by default.

---

## 18. Gold Label Authority

[`adjudication/ORCA-GOLD-LABEL-AUTHORITY-v1.md`](adjudication/ORCA-GOLD-LABEL-AUTHORITY-v1.md) — 8-step gold criteria; no model output as gold without human adjudication.

---

## 19. Hard Negatives

[`hard-negatives/ORCA-HARD-NEGATIVE-SET-DESIGN-v1.md`](hard-negatives/ORCA-HARD-NEGATIVE-SET-DESIGN-v1.md) + JSON — 10 required families testing `TOPICAL RELEVANCE MISCLASSIFIED AS COMMERCIAL INTENT`.

---

## 20. Minimal Pairs

[`hard-negatives/ORCA-SEMANTIC-MINIMAL-PAIR-DESIGN-v1.md`](hard-negatives/ORCA-SEMANTIC-MINIMAL-PAIR-DESIGN-v1.md) — design illustrations only (1C examples per task); group-aware split policy.

---

## 21. Regression Anchors

[`regression/ORCA-SEMANTIC-REGRESSION-ANCHOR-POLICY-v1.md`](regression/ORCA-SEMANTIC-REGRESSION-ANCHOR-POLICY-v1.md) + JSON — 10 anchor families; old Corvonero labels cannot be imported as truth.

---

## 22. Leakage Controls

[`leakage-control/ORCA-BENCHMARK-LEAKAGE-CONTROLS-v1.md`](leakage-control/ORCA-BENCHMARK-LEAKAGE-CONTROLS-v1.md) + JSON — duplicate, morphological, cluster, example-library, prompt, old-label, post-hoc editing controls with severity/remediation.

---

## 23. Benchmark Record Schema

[`schemas/ORCA-BENCHMARK-RECORD-SCHEMA-v1.md`](schemas/ORCA-BENCHMARK-RECORD-SCHEMA-v1.md), [`schemas/orca-benchmark-record-schema-v1.schema.json`](schemas/orca-benchmark-record-schema-v1.schema.json), [`schemas/orca-benchmark-record-template-v1.json`](schemas/orca-benchmark-record-template-v1.json) — wraps semantic record; empty template only.

---

## 24. Metric Plan

[`quality/ORCA-BENCHMARK-METRIC-PLAN-v1.md`](quality/ORCA-BENCHMARK-METRIC-PLAN-v1.md) + JSON

**Operator-approved (D3):** Commercial Precision on auto-accept ≥ 0.95; protected-strata FPR ≤ 0.01 per class.

**All other thresholds:** `PROPOSED — VALIDATE DURING B0/B1`.

---

## 25. Agreement Metrics

[`quality/ORCA-ANNOTATOR-AGREEMENT-METRICS-v1.md`](quality/ORCA-ANNOTATOR-AGREEMENT-METRICS-v1.md) — raw agreement, κ, class-specific disagreement; high agreement can still be wrong if guideline is biased.

---

## 26. Release States

Defined in charter and [`README.md`](README.md): DRAFT → ANNOTATION IN PROGRESS → ADJUDICATION IN PROGRESS → FROZEN INTERNAL → BLIND EVALUATION → RELEASED FOR DEVELOPMENT → SUPERSEDED / CONTAMINATED / WITHDRAWN.

---

## 27. Versioning

[`quality/ORCA-BENCHMARK-VERSIONING-POLICY-v1.md`](quality/ORCA-BENCHMARK-VERSIONING-POLICY-v1.md) — semver semantics, contamination bump, immutable snapshots.

---

## 28. B0 Qualification Charter

[`charters/ORCA-BENCHMARK-B0-QUALIFICATION-CHARTER-v1.md`](charters/ORCA-BENCHMARK-B0-QUALIFICATION-CHARTER-v1.md) — 60–100 phrases, balanced coverage, no classifier comparison unless separately approved.

---

## 29. Corvonero Pilot Boundary

[`charters/ORCA-CORVONERO-PILOT-BOUNDARY-v1.md`](charters/ORCA-CORVONERO-PILOT-BOUNDARY-v1.md) — 300–500, clean MIG corpus, old labels forbidden, blind ≥ 100, CONSERVATIVE mode, no campaign/Commander. Phrase selection **not started**.

---

## 30. Governance Roles

[`annotation/ORCA-BENCHMARK-GOVERNANCE-ROLES-v1.md`](annotation/ORCA-BENCHMARK-GOVERNANCE-ROLES-v1.md) — 10 roles with separation of duties.

---

## 31. Quality Gates

[`quality/ORCA-BENCHMARK-QUALITY-GATES-v1.md`](quality/ORCA-BENCHMARK-QUALITY-GATES-v1.md) + JSON — source, sampling, annotation, adjudication, freeze, evaluation gate families.

---

## 32. Validation

[`validation/ORCA-UNIVERSAL-BENCHMARK-CHARTER-VALIDATION-v1.md`](validation/ORCA-UNIVERSAL-BENCHMARK-CHARTER-VALIDATION-v1.md) + JSON — charter completeness validation; no benchmark rows created.

---

## 33. P0-D Decision Record

[`decisions/ORCA-UNIVERSAL-BENCHMARK-CHARTER-DECISION-v1.md`](decisions/ORCA-UNIVERSAL-BENCHMARK-CHARTER-DECISION-v1.md) + JSON — status `PROPOSED — OPERATOR APPROVAL REQUIRED`.

---

## 34. Map and Backlog Updates

Updated (uncommitted with P0-D):

- ORCA Operational Index — P0-D section added
- ORCA README — P0-D proposed
- Semantic Intelligence README — benchmark locus
- Architecture README — P0-D proposed
- Research promotion matrix — P0-D drafted
- Promotion backlog MD + JSON — P0-D PROPOSED; P0-E BLOCKED

| Gate | Status |
|------|--------|
| P0-A | APPROVED — CHECKPOINTED (`f17c270`) |
| P0-B | APPROVED — CHECKPOINTED (`3151953`) |
| P0-C | APPROVED — CHECKPOINTED (`78b0557`) |
| P0-D | PROPOSED — OPERATOR REVIEW |
| P0-E | BLOCKED UNTIL P0-D APPROVAL |
| Corvonero | FROZEN |
| Campaign production | BLOCKED |

---

## 35. Files Created or Changed

### Committed (P0-C checkpoint `78b0557`)

- Full `semantic-intelligence/annotation/` package (32 new files)
- P0-C approval records
- Map/backlog updates for P0-C approval

### Created uncommitted (P0-D)

- `semantic-intelligence/benchmark/` — 42 charter/schema/policy files

### Modified uncommitted (P0-D maps)

- `projects/orca/OPERATIONAL-INDEX.md`
- `projects/orca/README.md`
- `projects/orca/semantic-intelligence/README.md`
- `projects/orca/architecture/semantic-intelligence/README.md`
- `projects/orca/architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-RESEARCH-PROMOTION-MATRIX-v1.md`
- `projects/orca/research/.../promotion/` (MD + JSON)

P0-D intentionally **not committed** per task stop condition.

---

## 36. Git Status

```
 M projects/orca/OPERATIONAL-INDEX.md
 M projects/orca/README.md
 M projects/orca/architecture/semantic-intelligence/README.md
 M projects/orca/architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-RESEARCH-PROMOTION-MATRIX-v1.md
 M projects/orca/research/ppc-semantic-intelligence/world-practice-2026-06/promotion/*
 M projects/orca/semantic-intelligence/README.md
?? projects/orca/semantic-intelligence/benchmark/
```

P0-C pushed at `78b0557`. P0-D and map updates remain local uncommitted.

---

## 37. SAFE UNKNOWN

- Exact Corvonero clean MIG corpus row counts at pilot selection time — **SAFE UNKNOWN** until P0-E phrase selection.
- Optimal long-term double-annotation percentage for universal benchmark beyond mandatory strata — **OPERATOR DECISION REQUIRED AFTER B0**.
- Statistical power for all proposed metrics at B2 size — planning ranges only; not proven sufficient for every metric.

---

## 38. Operator Approval Items

Operator must approve P0-D package:

1. Universal benchmark charter and two-product model  
2. Domain and intent strata (26 intent strata)  
3. Difficulty strata and sampling plan  
4. Source and split policy  
5. Blind test governance  
6. Double annotation and adjudication policies  
7. Gold label authority  
8. Hard negatives and minimal pairs design  
9. Regression anchor policy  
10. Leakage controls  
11. Benchmark record schema  
12. Metric plan (D3 preserved; other thresholds proposed)  
13. B0 qualification charter  
14. Corvonero pilot boundary  
15. Quality gates and validation  
16. P0-D decision record sign-off  

---

## 39. Next Gate

**OPERATOR APPROVAL OF ORCA UNIVERSAL SEMANTIC BENCHMARK CHARTER V1**, then **B0 QUALIFICATION SET DESIGN** or **P0-E CORVONERO PILOT CHARTER**.

---

## 40. Stop Condition

**MET.**

- P0-C approval recorded and checkpointed (`78b0557`, pushed)  
- P0-D charter drafted (uncommitted)  
- No benchmark rows, gold labels, annotation, classifier, or campaign work started  
- Corvonero remains FROZEN  
- Campaign production remains BLOCKED  
