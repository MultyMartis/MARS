# SCHEMA-DECISION

**Decision:** `D6A_EXISTING_SCHEMA_SUFFICIENT`

## Required for safe state machine

| Need | Satisfied by |
|------|----------------|
| Terminal delivery value | Existing `delivery_state` ∈ {PENDING, SENT, FAILED} |
| Event identity | Existing `event_id` |
| Conditional filter | `event_id` + `delivery_state=PENDING` on update node |

## Optional for observability (NOT added in D6A)

| Candidate | Why deferred |
|-----------|--------------|
| telegram_message_id | Useful audit; recoverable from n8n execution for now |
| delivery_finished_at | Useful audit; not required for SENT/FAILED distinction |
| delivery_error_class | Useful; kept in classify output / execution, not DT column |

## Production migration

**None in D6A.** Live table remains 15 columns. Future D6A2 may optionally extend if operator charter requires durable message_id without execution lookup.
