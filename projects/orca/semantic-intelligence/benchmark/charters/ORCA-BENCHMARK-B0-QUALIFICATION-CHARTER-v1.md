# ORCA Benchmark B0 Qualification Charter v1

**Charter ID:** `orca-benchmark-b0-qualification-charter`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Define **B0** — the qualification phase that validates annotation protocol, tooling, adjudication loop, and quality metrics **before** scaling to B1 (Corvonero pilot + partial universal) and B2 (full universal target).

B0 is **not** a production evaluation set. Results inform protocol fixes and proposed threshold calibration only.

---

## Scope

| Parameter | Value |
|-----------|-------|
| Target size | **60–100** phrases |
| Intent strata represented | All 26 strata — minimum 2 phrases each where feasible |
| Domain coverage | Minimum 5 of 8 domains represented |
| Double annotation | **100%** — mandatory |
| Blind split | **None** — B0 is never used as blind evaluation |
| Gold authority | Adjudicator + operator spot-check |

---

## Entry criteria

- P0-D charter **operator-approved**
- P0-C guideline implementation readiness plan executed (annotator qualification per [`../annotation/quality/ORCA-ANNOTATOR-READINESS-PLAN-v1.md`](../../annotation/quality/ORCA-ANNOTATOR-READINESS-PLAN-v1.md))
- Benchmark record schema validated ([`../schemas/ORCA-BENCHMARK-RECORD-SCHEMA-v1.md`](../schemas/ORCA-BENCHMARK-RECORD-SCHEMA-v1.md))
- Source policy acknowledged — no Corvonero v1 labels as seed truth

---

## Exit criteria (B0 pass)

| Criterion | Target | Status |
|-----------|--------|--------|
| Schema validity on adjudicated records | 100% | PROPOSED — VALIDATE DURING B0 |
| Eligibility adjudication completion | 100% of disagreements resolved | Mandatory |
| Annotator agreement κ (eligibility) | ≥ 0.70 B0 floor; ≥ 0.75 B1 target | PROPOSED — VALIDATE DURING B0 |
| Protected-strata disagreement rate | Documented per stratum | PROPOSED — VALIDATE DURING B0 |
| Rationale specificity pass rate | ≥ 0.85 B0 floor | PROPOSED — VALIDATE DURING B0 |
| Adjudication SLA | No blocking backlog > operator-defined SLA | Operations |
| Tooling | Export/import round-trip without field loss | Mandatory |
| Operator sign-off | B0 pass record | **OPERATOR APPROVAL REQUIRED** |

Failure → remediate protocol or annotator readiness; **do not** advance to B1.

---

## Prohibited uses

- Training classifiers for production thresholds
- Corvonero rerun authorization
- Campaign or export decisions
- Inclusion in blind test pack

---

## Outputs

- B0 qualification report (human-maintained, post-execution)
- Proposed threshold adjustments for B1/B2 charter amendment
- **Operator decision** on long-term double-annotation sample rate (deferred U-C02)
