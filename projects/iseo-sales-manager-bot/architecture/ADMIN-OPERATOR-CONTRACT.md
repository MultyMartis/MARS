# Admin Operator Contract

**Workflow:** Admin.dev / `wLrLp4WQHm1VJmxz`  
**Authority:** [CURRENT-PRODUCTION-ARCHITECTURE.md](CURRENT-PRODUCTION-ARCHITECTURE.md)

## Responsibilities

Admin.dev owns:

- Telegram callbacks;
- processed/spam lifecycle updates;
- raw-source callback;
- reminder schedule and reminder delivery;
- admin commands;
- CONFIG reads/writes where supported;
- LEAD_EVENTS and ERRORS recording;
- bounded forensic support for legacy raw fallback.

## Operator Boundary

Admin.dev is an operator surface. It is not an automatic CRM, delivery manager, or task list executor.

Do not add behavior that automatically:

- assigns work;
- changes lifecycle from reminders;
- creates delivery tasks;
- announces to managers without explicit command/contract;
- rewrites source data.

## Authorization

Admin actions must verify the Telegram user against production authorization config. Unauthorized users receive a safe denial. Do not reveal secret values or the full authorized list in docs or user-facing denial messages.

## Raw Source

Raw source is read-only. Admin.dev may resolve it by filtered RAW `lead_id`; legacy fallback may READ Gmail by `source_message_id` only when needed and bounded.

## Failure Posture

- If CONFIG is unavailable, deny risky writes.
- If a callback token cannot resolve a lead, do not guess.
- If Sheets hits rate limits, use scoped lookup patterns; do not broaden reads.
- If Telegram delivery fails, record enough evidence for recovery without exposing secrets or PII.

## Evidence

Admin behavior is proven by n8n workflow state, accepted stable baseline, events/errors, and targeted acceptance evidence. MARS documentation alone is not runtime proof.

