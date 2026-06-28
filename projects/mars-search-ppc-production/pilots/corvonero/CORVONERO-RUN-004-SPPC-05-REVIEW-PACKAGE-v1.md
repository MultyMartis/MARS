# CORVONERO RUN 004 — SPPC-05 REVIEW PACKAGE v1

**Run:** `corv-semantic-v2-20260626-004`  
**Verdict:** `PASS — OPERATOR REVIEW REQUIRED`

## Repair fixture variance (3×)

| Fixture | Expected | Observed |
|---------|----------|----------|
| CFM-PROD-UPD-02 | REJECT | REJECT×3 |
| PQR-ABSTAIN-03 | ABSTAIN | ABSTAIN×3 |
| PC-ABSTAIN-01 | ABSTAIN | ABSTAIN×3 |
| PSR-AMB-01 | ABSTAIN | ACCEPT×3 (known ambiguity — non-blocking) |

## PSR-AMB-01

{
  "record_id": "PSR-AMB-01",
  "query": "купить 1с с настройкой",
  "expected": "ABSTAIN",
  "repetitions": 3,
  "verdict_distribution": {
    "ACCEPT": 3
  },
  "primary_distribution": {
    "ACCEPT": 3
  },
  "known_ambiguity": true,
  "non_blocking": true,
  "operator_decision": "KNOWN PRE-EXISTING AMBIGUITY — NON-BLOCKING FOR RUN 004 SPPC-05 — MUST REMAIN VISIBLE",
  "expands_false_accept_family": false,
  "closed_dataset_note": "PSR minimal pairs in closed dataset returned MODEL_API_ERROR — isolated from product FPR gate"
}

## Cost

- Product: $0.2181
- Geo: $0.2478
- Closed dataset: $0.1395
- Variance (est.): ~$0.08
- **Total:** ~$0.6853 (hard cap $3.00)
