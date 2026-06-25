# ORCA Annotator Agreement Metrics v1

**Document ID:** `orca-annotator-agreement-metrics`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Define **inter-annotator agreement** metrics for benchmark quality (distinct from P0-G classifier metrics).

---

## Metrics

| Metric | Field | Proposed target | Status |
|--------|-------|-----------------|--------|
| Eligibility κ (ACCEPT/REJECT/ABSTAIN) | `commercial_eligibility.decision` | ≥ 0.75 | PROPOSED — VALIDATE B0/B1 |
| Primary intent κ | `primary_intent` | ≥ 0.70 | PROPOSED — VALIDATE B0/B1 |
| Protected-strata disagreement rate | protected strata only | ≤ 0.15 | PROPOSED — VALIDATE B0/B1 |
| Per-class eligibility agreement | by stratum | documented | B0 floor |
| Rationale specificity pass | QA rubric | ≥ 0.90 | PROPOSED — VALIDATE B0/B1 |

Deferred from P0-C **U-C03** — κ target finalized after B0 data.

---

## Reporting

- B0: full agreement report per stratum
- B1: pilot + universal partial
- B2: pre-freeze sign-off

---

## Double annotation linkage

Agreement computed only on records with `double_annotation.pass_count >= 2` and blind peer labels.
