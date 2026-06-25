# ORCA Benchmark Metric Plan v1

**Plan ID:** `orca-benchmark-metric-plan`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-metric-plan-v1.json`](orca-benchmark-metric-plan-v1.json)

---

## Purpose

Define **evaluation metrics** for P0-F/G using benchmark gold. Distinguishes operator-approved D3 thresholds from proposed metrics to validate during B0/B1.

---

## Operator-approved (D3)

| Metric | Threshold |
|--------|-----------|
| Commercial precision on auto-accept | **≥ 0.95** |
| Protected-strata FPR per class | **≤ 0.01** |

---

## Proposed — validate during B0/B1

| Metric | Proposed threshold |
|--------|-------------------|
| Overall auto-accept FPR | ≤ 0.03 |
| Service mapping precision | ≥ 0.97 |
| Ambiguity recall (blind hard) | ≥ 0.90 |
| Abstention rate (initial) | ≥ 0.15 |
| Annotator agreement κ (eligibility) | ≥ 0.75 |
| Calibration ECE | Corridor TBD |

---

## Evaluation splits

- **Primary gate:** `SPLIT_BLIND`
- **Secondary:** hard-negative pack, regression anchors
