# SOURCE-STATUS-AUTHORITY

**Token:** `D6B_SOURCE_STATUS_AUTHORITY_DEFINED`

## Factual mapping (unchanged)

| Source classification | normalized_status |
|-----------------------|-------------------|
| `NO_ACTION_REQUIRED` | `OK` |
| `ONBOARDING_REQUIRED` | `ATTENTION` |
| `HYGIENE_REVIEW_REQUIRED` | `ATTENTION` |
| `FAILURE_REVIEW_REQUIRED` | `FAILED` |
| true conflict / malformed / incomplete / unsupported / unsafe | `BLOCKED` |

## Authority precedence (preserved)

1. Required artifacts present and parseable  
2. monitor-classification = action classification authority  
3. changed-summary = metrics  
4. run-summary = health/exit/identity  
5. run-summary.classification must equal monitor classification  
6. mismatch → `BLOCKED`  
7. logs = debugging only  

Freshness evaluation occurs **after** authority is valid enough to map factual status.

**Token:** `D6B_AUTHORITY_PRECEDES_FRESHNESS`
