# ORCA Annotation Quality Gates v1

**Gates ID:** `orca-annotation-quality-gates`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-annotation-quality-gates-v1.json`](orca-annotation-quality-gates-v1.json)

---

## Purpose

Quality metrics and gates for human annotation records, double-annotation workflows, and adjudication outputs. Documentation-level specification — not automated enforcement in this task.

---

## Operator-approved thresholds (D3)

These thresholds are **already authorized** by operator decision D3. They apply to **classifier auto-accept path** evaluation (P0-F/G), not to raw annotator agreement in isolation.

| Metric | Threshold | Status | Operator decision |
|--------|-----------|--------|-------------------|
| Commercial precision on auto-accept | **≥ 0.95** | OPERATOR-APPROVED | D3 |
| Protected-strata FPR per class | **≤ 0.01** | OPERATOR-APPROVED | D3 |

Protected classes: career, educational, diy_how_to, regulatory, navigational.

---

## Proposed annotation quality metrics

All metrics below require **P0-D Benchmark Charter** before numerical thresholds are operator-approved.

| Metric ID | Metric | Description | Threshold status |
|-----------|--------|-------------|------------------|
| AQG-01 | Field completeness | Required schema fields populated per annotation order | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-02 | Rationale specificity | Phrase-specific rationale rubric pass rate | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-03 | Schema validity | Records pass JSON Schema draft 2020-12 validation | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-04 | Annotator agreement | Cohen's κ or equivalent on eligibility | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-05 | Per-class disagreement | Disagreement rate by primary intent class | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-06 | Protected-strata disagreement | Disagreement rate within protected strata | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-07 | ABSTAIN consistency | ABSTAIN used when mandatory rules trigger | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-08 | Decision-tree compliance | Annotation path matches decision-tree terminal | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-09 | Provenance completeness | Annotator ID, guideline version, timestamp present | PROPOSED — BENCHMARK CHARTER REQUIRED |
| AQG-10 | Version completeness | Taxonomy and schema version references present | PROPOSED — BENCHMARK CHARTER REQUIRED |

### Illustrative proposed targets (not operator-approved)

The following numerical hints are **research-derived placeholders only**. They must not be used as production gates until P0-D charter and operator sign-off.

| Metric | Illustrative target | Status |
|--------|---------------------|--------|
| Annotator agreement (κ on eligibility) | ≥ 0.75 | PROPOSED — BENCHMARK CHARTER REQUIRED |
| Protected-strata disagreement rate | ≤ 0.15 | PROPOSED — BENCHMARK CHARTER REQUIRED |
| Rationale specificity pass rate | ≥ 0.90 | PROPOSED — BENCHMARK CHARTER REQUIRED |
| Field completeness | ≥ 0.98 | PROPOSED — BENCHMARK CHARTER REQUIRED |
| ABSTAIN consistency (rule-triggered cases) | ≥ 0.95 | PROPOSED — BENCHMARK CHARTER REQUIRED |

---

## Gate relationships

| Gate | Blocks |
|------|--------|
| P0-C guideline approval | P0-D benchmark charter |
| P0-D benchmark charter | Gold label creation |
| Annotation quality pass (charter-defined) | Benchmark freeze |
| D3 threshold pass (P0-G) | Corvonero rerun; campaign production |

---

## Measurement notes

1. **Commercial precision** is measured on **auto-accept path only** — human-resolved ACCEPT tracked separately (per architecture quality gates).
2. **Protected-strata FPR** is per-class; any class exceeding 0.01 fails D3 gate.
3. **Annotator agreement** is measured on double-annotation sample before gold freeze.
4. **ABSTAIN consistency** is audited against mandatory ABSTAIN rules in ABSTAIN standard — not against desired automation rate.
5. Fail closed: D3 miss → no production authorization regardless of annotation volume.

---

## Related documents

- [`../reviewer-tools/ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md`](../reviewer-tools/ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md)
- [`../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md`](../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md)
- [`../../../architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-QUALITY-GATES-v1.md`](../../../architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-QUALITY-GATES-v1.md)
