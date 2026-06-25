# ORCA Benchmark Quality Gates v1

**Gates ID:** `orca-benchmark-quality-gates`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-benchmark-quality-gates-v1.json`](orca-benchmark-quality-gates-v1.json)

---

## Purpose

Quality **gates** blocking phase transitions and gold release.

---

## Gate catalog

| ID | Gate | Blocks |
|----|------|--------|
| BQG-01 | Charter operator approval | B0 execution |
| BQG-02 | B0 qualification pass | B1 scale-up |
| BQG-03 | Schema validity 100% on gold | Freeze (proposed validate B0) |
| BQG-04 | Double annotation complete (mandatory cohorts) | Gold freeze |
| BQG-05 | Adjudication backlog zero | Gold freeze |
| BQG-06 | Blind seal checklist | `BLIND EVALUATION` |
| BQG-07 | D3 commercial precision ≥ 0.95 | P0-G pass — **OPERATOR-APPROVED** |
| BQG-08 | D3 protected FPR ≤ 0.01 | P0-G pass — **OPERATOR-APPROVED** |
| BQG-09 | Leakage controls pass | P0-F baselines |
| BQG-10 | Operator gold freeze sign-off | `RELEASED FOR DEVELOPMENT` |

---

## Fail-closed

Any BQG-07/08 miss at P0-G → Corvonero rerun remains **BLOCKED**; campaign **BLOCKED** (D7).
