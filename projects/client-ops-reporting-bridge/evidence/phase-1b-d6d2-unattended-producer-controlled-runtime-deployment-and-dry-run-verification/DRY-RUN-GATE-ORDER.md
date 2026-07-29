# DRY-RUN-GATE-ORDER

Observed gates_passed for this manual DRY_RUN (stopped at stale before activation):

1. acquire_producer_singleton_lock
2. verify_kill_switch
3. discover_candidates
4. validate_stabilize_artifact
5. derive_event_identity_fingerprint
6. inspect_local_cursor
7. derive_source_status
8. compute_freshness_eligibility

Then: STALE → BLOCKED_STALE → cursor EVALUATED / NO_SEND → receipt → lock released.

Did not enter: lifecycle charter, lifecycle lock, activate, readiness, webhook send, deactivate.

Token: D6D2_DRY_RUN_GATE_ORDER_VERIFIED
