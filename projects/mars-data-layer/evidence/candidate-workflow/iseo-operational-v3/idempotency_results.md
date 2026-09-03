# Idempotency results

Gate: `idempotency_r2=true` (orchestrator_result.json).

Repeated `process_gmail_inbound_commit` with identical Gmail `source_id`:

| Metric | Count after 2 commits |
|---|---|
| inbound_events for source | 1 |
| leads for lead_id | 1 |
| deliveries with matching idempotency_key pattern | 1 |
| lead_events for create event pattern | 1 |

Interpretation: DB invariant prevents second logical inbound / lead / delivery intent.  
n8n execution uniqueness is **not** relied upon.

Gmail finalize recovery: if inbound already `processed`, commit returns success with `gmail_finalize_allowed` without recreating lead/delivery.
