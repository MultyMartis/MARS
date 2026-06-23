# Strategy Reviewer Contract v1 — Wave 4.1

**Role:** Independent strategy quality reviewer (not strategist, not answer key).

## Inputs (allowed)

- Analytical pack (full)
- Generated strategy (full)
- Quality policy (`strategist-quality-model-v1.md`)
- Evidence authority matrix summary

## Inputs (forbidden)

- Expected strategy / campaign count
- Evaluation constraints file
- Case label or scenario name
- Strategist self-rationale as authority
- Historical Commander output

## Output schema

```json
{
  "verdict": "PASS | PASS WITH WARNINGS | REPAIR REQUIRED | INVALID",
  "groundedness": { "score": 0-1, "notes": [] },
  "internal_consistency": { "score": 0-1, "notes": [] },
  "campaign_logic": { "score": 0-1, "notes": [] },
  "risk_flags": [],
  "missing_blockers": [],
  "invented_claims": [],
  "bidding_fit": "PASS | WARN | FAIL",
  "budget_honesty": "PASS | WARN | FAIL",
  "landing_fit": "PASS | WARN | FAIL",
  "measurement_fit": "PASS | WARN | FAIL",
  "repair_recommendations": []
}
```

## Verdict rules

| Verdict | Condition |
|---------|-----------|
| **INVALID** | Fabricated fact, invented budget authority, hidden critical blocker |
| **REPAIR REQUIRED** | Any critical invariant fail or missing mandatory blocker |
| **PASS WITH WARNINGS** | Warnings only; no critical defects |
| **PASS** | All critical checks pass; architecture coherent |

## Independence

Reviewer uses separate evaluation path from strategist adapter. Model enrichment from strategist is **context only**, not authority.
