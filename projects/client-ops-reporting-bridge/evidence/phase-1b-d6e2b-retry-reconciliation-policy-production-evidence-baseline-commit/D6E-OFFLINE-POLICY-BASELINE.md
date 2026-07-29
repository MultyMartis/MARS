# D6E-OFFLINE-POLICY-BASELINE

Four top-level decisions: SAFE_TO_RETRY · UNSAFE_TO_RETRY · RECONCILE_BEFORE_RETRY · FINAL_FAILURE

Invariant: NO PROOF OF NON-DELIVERY ≠ SAFE_TO_RETRY

Automatic execution remains disabled even when classification is SAFE_TO_RETRY.

Offline harness (re-run D6E2B pre-commit): **54/54 PASS** (E1–E40 + EC1–EC10 + 4 invariants).
Concurrency fixtures: **10/10 PASS**.
Python `test_retry_policy_d6e`: **10/10 PASS**.

Constants: AUTOMATIC_RETRIES_ENABLED=NO · MAX_AUTOMATIC_RETRIES=0 · MAX_SAFE_CONCURRENCY=1
