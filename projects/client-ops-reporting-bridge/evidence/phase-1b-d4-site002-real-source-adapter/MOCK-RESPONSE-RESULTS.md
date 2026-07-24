# Mock Response Results

Same source event_id `803e01fa-e0b7-561a-9b70-3c2b988d0109`:

| Mock | business_result | notes |
|------|-----------------|-------|
| 202_accepted | INTAKE_ACCEPTED | intake only; telegram unknown |
| 200_duplicate_suppressed | DUPLICATE_SUPPRESSED | same event_id |
| 409_event_id_conflict | EVENT_ID_CONFLICT | same event_id |
| read_timeout_ambiguous | MANUAL_DEDUPE_CHECK_REQUIRED | automatic_retry=false |

network_calls=0 for all.
