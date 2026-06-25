# ORCA Benchmark Leakage Controls v1

**Controls ID:** `orca-benchmark-leakage-controls`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-leakage-controls-v1.json`](orca-benchmark-leakage-controls-v1.json)

---

## Purpose

Enumerate **leakage prevention controls** for benchmark splits, especially blind and hard-negative packs.

---

## Control catalog

| ID | Control | Severity |
|----|---------|----------|
| LC-01 | Blind split sealed before model label access | CRITICAL |
| LC-02 | No blind phrases in P0-C examples | CRITICAL |
| LC-03 | No Corvonero v1 labels in training | CRITICAL |
| LC-04 | Embedding index excludes blind | HIGH |
| LC-05 | Prompt/few-shot audit against blind | HIGH |
| LC-06 | Annotators blind to peer labels during pass | HIGH |
| LC-07 | Versioned hash on frozen packs | MEDIUM |
| LC-08 | Contamination → `CONTAMINATED` or `WITHDRAWN` | CRITICAL |

---

## Validation

Charter validation ([`../validation/ORCA-UNIVERSAL-BENCHMARK-CHARTER-VALIDATION-v1.md`](../validation/ORCA-UNIVERSAL-BENCHMARK-CHARTER-VALIDATION-v1.md)) includes leakage control presence checks.
