# D6C Offline Lifecycle Baseline

Accepted state machine preserved: CONTAINED -> PREFLIGHT_PASSED -> ACTIVATING -> ACTIVE_READY|ACTIVE_NOT_READY -> REQUEST_WINDOW_OPEN -> REQUEST_WINDOW_CLOSED -> DEACTIVATING -> RECONTAINED|RECONTAINED_WITH_ANOMALY|CONTAINMENT_FAILED.

D6C invariants preserved: initial active=false, explicit charter, freshness and dedupe prechecks, readiness GET before any request, bounded request count/time, max_requests=1, max_retries=0, max_concurrency=1, max_activation_changes=2, deactivation toward containment, lock release only after recontainment.

Harness result: 30/30 PASS.
