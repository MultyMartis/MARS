# REMINDER CURRENT-STATE CONTRACT v1

`pending_count = count(unique lead_id where resolved_status=pending AND eligible=true)`

One normalized current-state object per unique business key. Not CLEAN row count, not Telegram deliveries, not card instances.

Filter order per unique lead:

1. Resolve authoritative current status (precedence contract).
2. Exclude test (unless include_tests).
3. Exclude archive (unless include_archive).
4. Decide reminder eligibility.

Fail closed on resolution error: `ERROR_CURRENT_STATE_RESOLUTION` → claims=0, Telegram=0, day not stamped.
