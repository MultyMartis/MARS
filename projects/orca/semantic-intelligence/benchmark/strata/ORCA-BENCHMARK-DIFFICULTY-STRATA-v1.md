# ORCA Benchmark Difficulty Strata v1

**Strata set ID:** `orca-benchmark-difficulty-strata`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Orthogonal **difficulty** dimension for benchmark design — independent of intent stratum. Supports hard-case routing, ambiguity recall measurement, and adversarial pack design.

---

## Difficulty catalog

| difficulty_id | Label | Target share (B2) |
|---------------|-------|------------------:|
| `DIFF_CLEAR` | Clear — single dominant interpretation | 35% |
| `DIFF_MODERATE` | Moderate — competing signals resolvable with evidence | 35% |
| `DIFF_HARD` | Hard — borderline commercial vs protected | 20% |
| `DIFF_ADVERSARIAL` | Adversarial — deliberate near-miss / trap phrases | 10% |

---

## Rules

- `DIFF_ADVERSARIAL`: **100% double annotation**; included in hard-negative / minimal-pair programs.
- Difficulty assigned at **sampling design** time where possible; may be updated post-adjudication with audit.
- B0 must include at least one phrase per difficulty level.

---

## Evaluation use

| Difficulty | Primary metric focus |
|------------|---------------------|
| CLEAR / MODERATE | Baseline precision/recall |
| HARD | Protected FPR, abstention quality |
| ADVERSARIAL | Leakage resistance, commercial precision guardrail |
