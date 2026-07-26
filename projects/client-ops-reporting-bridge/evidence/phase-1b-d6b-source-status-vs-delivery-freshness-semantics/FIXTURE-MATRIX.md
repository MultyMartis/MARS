# FIXTURE-MATRIX (B1–B15)

All PASS via `tests/test_delivery_eligibility_d6b.py` / `n8n/harness/d6b-freshness-semantics-harness.py`.

| Case | Input | source_status | delivery_eligibility | Live |
|------|-------|---------------|----------------------|------|
| B1 | fresh ONBOARDING_REQUIRED | ATTENTION | FRESH_AND_ELIGIBLE | yes (preview) |
| B2 | stale ONBOARDING_REQUIRED | ATTENTION | STALE_REVIEW_REQUIRED | no |
| B3 | fresh NO_ACTION_REQUIRED | OK | FRESH_AND_ELIGIBLE | — |
| B4 | stale NO_ACTION_REQUIRED | OK | STALE_REVIEW_REQUIRED | no |
| B5 | fresh FAILURE_REVIEW_REQUIRED | FAILED | FRESH_AND_ELIGIBLE | — |
| B6 | stale FAILURE_REVIEW_REQUIRED | FAILED | STALE_REVIEW_REQUIRED | no |
| B7 | authority conflict | BLOCKED | NOT_SAFE_TO_SEND | no |
| B8 | missing authority file | BLOCKED | NOT_SAFE_TO_SEND | no |
| B9 | age == 93600 | ATTENTION | FRESH_AND_ELIGIBLE | — |
| B10 | age == 93601 | ATTENTION | STALE_REVIEW_REQUIRED | no |
| B11 | fresh then stale same artifact | ATTENTION | fresh→stale | same event_id |
| B12 | new run same class | ATTENTION | fresh | different event_id |
| B13 | stale preview | ATTENTION | STALE_REVIEW_REQUIRED | no customer payload |
| B14 | blocked preview | BLOCKED | NOT_SAFE_TO_SEND | no |
| B15 | fresh ATTENTION D5 path | ATTENTION | FRESH_AND_ELIGIBLE | approved |
