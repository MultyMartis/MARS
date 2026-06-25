# ORCA Hard Negative Set Design v1

**Design ID:** `orca-hard-negative-set-design`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-hard-negative-set-design-v1.json`](orca-hard-negative-set-design-v1.json)

---

## Purpose

Design a **fixed hard-negative pack** — phrases engineered or selected to trap commercial over-admission, especially protected strata (D3 FPR ≤ 0.01).

**No real phrases in this document** — categories and design goals only.

---

## Pack properties

- Separate from random stratified sample
- Assigned to `SPLIT_HARD_NEGATIVE`
- **100% double annotation**
- Evaluated in P0-G protected-strata FPR metrics

---

## Category catalog

| ID | Protected class | Design goal |
|----|-----------------|-------------|
| HN_PROTECTED_CAREER | career | Commercial keyword trap |
| HN_PROTECTED_EDUCATIONAL | educational | Course vs service trap |
| HN_PROTECTED_DIY | diy_how_to | Self-service vs hire trap |
| HN_PROTECTED_REGULATORY | regulatory | Info vs consulting trap |
| HN_PROTECTED_NAVIGATIONAL | navigational | Brand/login trap |
| HN_PROBLEM_FALSE_COMMERCIAL | — | Problem query over-admission |
| HN_SHORT_HEAD | — | Head-term ambiguity |

---

## Size

Target pack size: **PROPOSED — VALIDATE DURING B0/B1** (suggested 80–150 at B2).
