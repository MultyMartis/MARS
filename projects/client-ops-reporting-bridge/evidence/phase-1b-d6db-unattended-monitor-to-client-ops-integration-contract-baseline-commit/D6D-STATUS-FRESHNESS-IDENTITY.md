# D6D-STATUS-FRESHNESS-IDENTITY

## Source status mapping
- NO_ACTION_REQUIRED → OK
- ONBOARDING_REQUIRED → ATTENTION
- HYGIENE_REVIEW_REQUIRED → ATTENTION
- FAILURE_REVIEW_REQUIRED → FAILED
- unknown/malformed → BLOCKED
- nonzero monitor exit → FAILED

## Freshness (Workstream B)
- STALE_AFTER_SECONDS=93600
- Stale iff age **>** 93600
- Eligibility: FRESH_AND_ELIGIBLE / STALE_REVIEW_REQUIRED / NOT_SAFE_TO_SEND
- Factual source_status independent from freshness

## Event identity
- Same completed run/artifact → same event_id
- Retries/scans → same event_id
- New monitor run → new event_id
- Excludes evaluation time, retry count, scheduler invocation, activation session, cursor timestamp, timezone rendering
- Fingerprint: SHA-256 over normalized authoritative content
- Same identity + changed fingerprint → conflict BLOCKED / fail closed
