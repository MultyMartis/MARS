# ORCA Benchmark Split Policy v1

**Policy ID:** `orca-benchmark-split-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-split-policy-v1.json`](orca-benchmark-split-policy-v1.json)

---

## Purpose

Define **mutually exclusive splits** for benchmark gold: dev, calibration, blind, regression anchors, and hard negatives.

---

## Split catalog

| split_id | Purpose | Size guidance | Leakage tier |
|----------|---------|---------------|--------------|
| `SPLIT_DEV` | Rules/guideline iteration | ≤ 40% of adjudicated gold | INTERNAL |
| `SPLIT_CALIBRATION` | Threshold calibration | ≤ 25% of gold | INTERNAL |
| `SPLIT_BLIND` | P0-G gate | 300–400 phrases | **SEALED** |
| `SPLIT_REGRESSION_ANCHOR` | Version regression | Fixed pack | ANCHOR |
| `SPLIT_HARD_NEGATIVE` | FP traps | Fixed pack | **SEALED** |

---

## Rules

1. A `query_id` belongs to **exactly one** primary split.
2. Blind and hard-negative packs: state `BLIND EVALUATION` or `FROZEN INTERNAL` before any model sees labels.
3. B0 records: **no blind assignment**.
4. Dev+calibration combined must leave sufficient blind quota at B2.

---

## Release interaction

Blind pack transition to `BLIND EVALUATION` requires: double annotation complete, adjudication complete, leakage checklist pass.
