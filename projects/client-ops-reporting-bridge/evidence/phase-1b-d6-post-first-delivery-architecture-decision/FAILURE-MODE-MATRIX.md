# FAILURE-MODE MATRIX — Phase 1B-D6

`D6_FAILURE_MODE_MATRIX_COMPLETE`

| Failure | Current Detection | Current Durable Evidence | Safe Automatic Action Today | Required Future Capability |
|---------|-------------------|--------------------------|-----------------------------|----------------------------|
| Stale source | Normalizer age > 93600 → status BLOCKED (conflated); D5 orchestrator separate eligibility checks | Artifact timestamps; preview age fields | No auto send; operator review | Freshness axis separate from source_status (B) |
| Conflicting authority JSON | Adapter/normalizer BLOCKED / conflict reasons | ProcessResult reason_codes; no POST | Abort; no POST | Keep BLOCKED for authority only; escalate |
| Event already seen | DT lookup DUPLICATE / D5 event_unseen gate | DT row intake_state FIRST_SEEN | Suppress Telegram (workflow); producer abort | Unchanged + respect SENT ledger |
| Inactive webhook / 404 | HTTP 404; D5R2 proven | Producer HTTP result; no DT row | Do not retry as success; activate only under charter | C3 readiness check before POST |
| Activation failure | Activation API error | Orchestrator evidence | Abort; no POST | Alert + no window open |
| Ambiguous POST timeout | Producer CLASS_READ_TIMEOUT_AMBIGUOUS | Often incomplete | GET-only reconcile; **no** auto retry | Ledger + execution reconcile API |
| HTTP 202 but execution failure | Exec list / status | Partial | Operator; no second POST without reconcile | Workflow error → FAILED delivery state |
| DT insert but Telegram failure | Exec node inspect; DT PENDING | Row PENDING | No auto retry | Persist FAILED; optional retryable after policy |
| Telegram success with PENDING delivery_state | D5R2A proven gap | Telegram message_id in exec; DT PENDING | Treat as delivered via evidence; **no** re-send | Durable SENT + message_id (A) |
| Recontainment failure (deactivate) | GET active=true after finally | Activation client result | Emergency deactivate phrase; halt new POSTs | C3 watchdog + alert |
| Dirty runtime | git status porcelain | Runtime checkout checks | Abort Client Ops live | Hard gate in unattended producer |
| Scheduler overlap | Task state Running | Scheduler API | Do not start second producer/monitor pair blindly | Overlap lock / lease |
| HTTP 5xx before claim | Status + no row | Weak | GET-only then careful future retry | Reconcile policy (E) |
| HTTP 5xx after claim | Row exists PENDING | DT row | No Telegram assumption; no blind retry | SENT/FAILED ledger |
| Secret/auth failure 401/403 | HTTP class | Producer classify | Terminal; fix secret offline | Unchanged |
| Concurrent producers | Not instrumented | Unproven | Forbidden (concurrency=1) | Remain 1 until proven otherwise |

No live mutations performed to generate this table.
