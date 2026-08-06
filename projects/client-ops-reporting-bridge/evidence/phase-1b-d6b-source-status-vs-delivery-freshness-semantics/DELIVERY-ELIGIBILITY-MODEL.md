# DELIVERY-ELIGIBILITY-MODEL

**Token:** `D6B_DELIVERY_ELIGIBILITY_MODEL_DEFINED`

Implemented in `delivery_eligibility.py`.

| Value | Meaning |
|-------|---------|
| `FRESH_AND_ELIGIBLE` | Authority valid; age ≤ threshold (`age_seconds > 93600` is false); no safety block |
| `STALE_REVIEW_REQUIRED` | Authority valid; factual status preserved; age > 93600; no automatic/live send |
| `NOT_SAFE_TO_SEND` | Authority invalid/conflicting/incomplete/security reject — independent of age |

`BLOCKED` is **not** a synonym for stale when factual status remains OK/ATTENTION/FAILED.

Live gate requires `delivery_eligibility == FRESH_AND_ELIGIBLE`.
