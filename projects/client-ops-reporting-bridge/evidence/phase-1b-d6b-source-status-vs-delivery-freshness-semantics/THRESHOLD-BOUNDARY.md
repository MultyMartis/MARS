# THRESHOLD-BOUNDARY

**Token:** `D6B_FRESHNESS_THRESHOLD_UNCHANGED`  
**Token:** `D6B_THRESHOLD_BOUNDARY_EXPLICIT`

| Constant | Value |
|----------|-------|
| `STALE_AFTER_SECONDS` | `93600` (unchanged) |
| Operator | `age_seconds > STALE_AFTER_SECONDS` |

| age_seconds | Eligibility |
|-------------|-------------|
| 93600 | `FRESH_AND_ELIGIBLE` (still fresh) |
| 93601 | `STALE_REVIEW_REQUIRED` |

No threshold tuning in D6B.
