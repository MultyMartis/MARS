# D6B-OFFLINE-SEMANTICS-BASELINE

## source_status (factual)

| Authority outcome | source_status |
|-------------------|---------------|
| NO_ACTION_REQUIRED | OK |
| ONBOARDING_REQUIRED | ATTENTION |
| HYGIENE_REVIEW_REQUIRED | ATTENTION |
| FAILURE_REVIEW_REQUIRED | FAILED |
| true source-authority defect | BLOCKED |

## delivery_eligibility

- FRESH_AND_ELIGIBLE
- STALE_REVIEW_REQUIRED
- NOT_SAFE_TO_SEND

## Stale preservation

| Case | Result |
|------|--------|
| stale ATTENTION | ATTENTION + STALE_REVIEW_REQUIRED |
| stale OK | OK + STALE_REVIEW_REQUIRED |
| stale FAILED | FAILED + STALE_REVIEW_REQUIRED |
| true defect | BLOCKED + NOT_SAFE_TO_SEND |

## Threshold

STALE_AFTER_SECONDS=93600; operator `age > 93600`.

## Identity

Evaluation clock is **not** identity-bearing.

## Notification boundary

Customer delivery requires FRESH_AND_ELIGIBLE; stale/blocked fail closed before intake.

Model: `D6B_INTERNAL_MODEL_ONLY` (no Data Table schema change; no event schema version bump).
