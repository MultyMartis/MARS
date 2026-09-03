# Gmail commit-point tests

## Required durable state before success

`process_gmail_inbound_commit` returns only after:

1. inbound registered/idempotent
2. lead upserted
3. required lead_event appended
4. delivery/outbox intents enqueued (when recipients exist / enqueue flag)

`commit_point` field: `inbound+lead+event+delivery_intents`.

## Ordering

1. PG commit
2. Gmail finalize gate (candidate: simulated; no production mailbox mutation)
3. Outbox claim / dry-run delivery mark

## Failure modes

| Scenario | Expected |
|---|---|
| DB failure before commit returns | Gmail not finalized |
| PG success, Gmail finalize fails | No duplicate lead on re-entry; finalize recoverable via short-circuit |
| Candidate inactive | No live Gmail Trigger; finalize simulated only |

False Gmail processed before DB: **0** in this wave (no live poller on candidate).
