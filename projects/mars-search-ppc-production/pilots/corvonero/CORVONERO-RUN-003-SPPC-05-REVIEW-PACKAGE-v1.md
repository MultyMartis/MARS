# CORVONERO RUN 003 — SPPC-05 REVIEW PACKAGE v1

**Run:** `corv-semantic-v2-20260626-003`  
**Verdict:** `FAILED`

## Operator decisions (recorded)

- ORCA repair: **APPROVED**
- Run 002: **BLOCKED / NON-RESUMABLE**
- Run 003: **SPPC-05 RETRY ONLY**
- PSR-AMB-01: **KNOWN AMBIGUITY — NON-BLOCKING**
- Phase 3: **NOT AUTHORIZED**

## Critical failures

- Product confirmation adversarial FPR exceeds 0.01
- Platform compatibility not full pass (PC-ABSTAIN-01 model variance)
- Focused repair repro: PQR-ABSTAIN-03 adjudicator ordering issue on SINGLE_ASSESSOR path
- Variance check: repair fixtures unstable

## Repair fixture evidence

### CFM-PROD-UPD-02
null

### PQR-ABSTAIN-03
"see problem_query_policy suite"

### PSR-AMB-01
{
  "record_id": "PSR-AMB-01",
  "query": "купить 1с с настройкой",
  "expected": "ABSTAIN",
  "observed": "UNKNOWN",
  "known_ambiguity": true,
  "non_blocking": true,
  "historically_observed": "ACCEPT",
  "expands_false_accept_family": false,
  "note": "Pre-existing ambiguous minimal pair; must remain visible in operator review"
}

## Suite matrix

| wave31f_bypass | PASS | 0 |
| under_admission | PASS | 0 |
| platform_compatibility | FAIL | 1 |
| focused_repair_repro | FAIL | 1 |
| problem_query_policy | PASS | 0 |
| confirmation_product | PASS | 0 |
| confirmation_geo_v2 | PASS | 0 |
| closed_dataset_regression | PASS | 0 |

## Cost

- Cumulative: **$0.0000**
- Hard cap: **$3**
