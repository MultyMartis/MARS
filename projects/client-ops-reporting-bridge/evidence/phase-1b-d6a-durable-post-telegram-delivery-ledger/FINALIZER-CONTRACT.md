# FINALIZER-CONTRACT

**Token:** `D6A_FINALIZER_CONTRACT_DEFINED`

## Input (narrow)

| Field | Required | Notes |
|-------|----------|-------|
| event_id | YES | Must match row |
| expected_current_delivery_state | Preferred | Default PENDING |
| target_delivery_state | YES | SENT or FAILED |
| delivery_finished_at | Optional audit | Not persisted to 15-col schema in D6A |
| telegram_message_id | Optional audit | Not persisted to DT in D6A |
| sanitized_error_class | Optional audit | Class/code only; not DT column in D6A |

## Forbidden mutations

Finalizer MUST NOT accept or write:

- intake_state
- event_status
- event_id
- event_fingerprint
- site_id
- schema_*
- source_run_id (not a DT column; still forbidden if present in request)

## Side effects

Finalizer performs **ledger write only**. It must not send Telegram / customer notification.
