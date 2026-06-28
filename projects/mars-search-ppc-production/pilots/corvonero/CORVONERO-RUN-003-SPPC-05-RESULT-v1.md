# CORVONERO RUN 003 — SPPC-05 RESULT v1

**Run ID:** `corv-semantic-v2-20260626-003`  
**Completed:** 2026-06-26T13:29:20.099Z  
**Gate B:** `FAILED`  
**Lifecycle:** `BLOCKED_AT_SPPC_05`

## Summary

| Item | Value |
|------|-------|
| Provider | openrouter |
| Model | openai/gpt-5-mini |
| Prompt contract | orca-semantic-assessment-prompt-v1.4 |
| Adjudicator | v1.4 |
| Corpus processed | 0 / 2368 |
| Cumulative cost (USD) | 0.0000 |
| Isolation | OLD_RUN_ISOLATION — PASS |
| Repair authority | APPROVED ORCA REPAIR AUTHORITY — FROZEN |

## Suite Results

- **wave31f_bypass**: PASS (exit 0, 0s)
- **under_admission**: PASS (exit 0, 0s)
- **platform_compatibility**: FAIL (exit 1, 124s)
- **focused_repair_repro**: FAIL (exit 1, 83s)
- **problem_query_policy**: PASS (exit 0, 178s)
- **confirmation_product**: PASS (exit 0, 3355s)
- **confirmation_geo_v2**: PASS (exit 0, 3953s)
- **closed_dataset_regression**: PASS (exit 0, 5230s)

## Critical Gates

| Gate | Result |
|------|--------|
| Product FPR ≤ 0.01 | FAIL |
| Geo commercial recall ≥ 0.90 | FAIL |
| Geo adversarial FPR = 0 | FAIL |
| Problem query 10/10 | PASS |
| Under-admission | PASS |
| Wave 3.1F bypass | PASS |
| Platform compatibility | FAIL |
| Repair fixtures stable | FAIL |

## PSR-AMB-01 (known ambiguity)

- Expected: **ABSTAIN**
- Observed: **UNKNOWN**
- Non-blocking: **yes** (isolated; no product FPR breach from this pair alone)

## Failures

- Product confirmation adversarial FPR exceeds 0.01
- Platform compatibility not full pass (PC-ABSTAIN-01 model variance)
- Focused repair repro: PQR-ABSTAIN-03 adjudicator ordering issue on SINGLE_ASSESSOR path
- Variance check: repair fixtures unstable

## Stop Condition

Run **BLOCKED_AT_SPPC_05** — no canary, no corpus processing.
