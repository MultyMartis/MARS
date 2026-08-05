# SINGLE FLIGHT GUARD v1

**Status:** DEPLOYED; offline overlap model PASS; no live overlap incident observed.

The Intake Gate acquires workflow static-data lock before the lead path, blocks a fresh overlap, and permits stale-lock recovery after a 4-minute TTL. Final schedule is `minutesInterval=2`.

The final proof completed two claims/two sends, and five later polls produced zero resends. Single-flight is a load/race reducer, not a replacement for the delivery ledger.
