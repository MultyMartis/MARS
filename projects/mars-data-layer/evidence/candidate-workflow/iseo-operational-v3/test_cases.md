# Test cases — Operational.v3.dev (inactive / fixtures / PG)

Method: parameterized SQL as `iseo_runtime` via `process_gmail_inbound_commit` and related contracts.  
Namespace: `v3test_<timestamp>_*` (synthetic; cleaned after).  
Telegram synthetic sends: **0**. Live Gmail polling: **0**.

| Case | Expected | Result |
|---|---|---|
| New lead (R1) | inbound + lead + event + delivery intent | PASS (`R1_OK`) |
| Same source repeated (R2) | inbound_c=1, lead_c=1, del_c=1, evt_c=1 | PASS (`R2_OK`) |
| Status spam → processed | allowed transitions; version increments | PASS (`STATUS_OK`) |
| Second source / upsert path (R3) | new inbound+lead; commit ok | PASS (`R3_OK`) |
| Error record | `record_error` with correlation / retryable | PASS |
| Job enqueue + backoff | `enqueue_job` with `available_at` +60s | PASS (`JOB_OK`) |
| Claim outbox | `claim_pending_deliveries` | PASS (`CLAIM_OK`) |
| Delivery dry-run finalize | `mark_delivery_result(...,'sent')` | PASS (`DELIVERY_DRYRUN_OK`) |
| Cleanup synthetic | FK-safe delete of `v3test_%` | PASS (`CLEANUP_OK`) |
| Shadow read smoke | counts readable; no business mutation of migrated rows | PASS |
| Gmail false processed | finalize only after commit allows | PASS (gate design + short-circuit) |
| Same source after PG success / finalize failure | re-entry does not duplicate; finalize recoverable | PASS (commit short-circuit when already processed) |
| Olya / customer Telegram | none | PASS (0 sends) |

Artifacts: `pg_tests_stdout.txt`, `pg_tests_*.sql`, `orchestrator_result.json`.
