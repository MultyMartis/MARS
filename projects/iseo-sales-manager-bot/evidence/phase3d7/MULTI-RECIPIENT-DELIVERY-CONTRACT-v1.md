# MULTI-RECIPIENT DELIVERY CONTRACT v1

## Scope

Every accepted production lead fans out to every eligible active Admin and moderator private chat.

## Rules

1. Business processing remains exactly-once (one CLEAN row / one lead identity).
2. Expansion happens **after** parse, dedupe, CLEAN upsert, Format.
3. One delivery item per eligible recipient; same card content; distinct chat target.
4. Per-recipient idempotency key: `lead_delivery:<stable_lead_ref>:<recipient_ref>`.
5. Failure isolation: one recipient failure does not roll back others or duplicate Admin cards.
6. Finalization (Admin-anchor): Gmail PROCESSED only when Admin anchor delivered and all other recipients are settled (`delivered|failed_retryable|failed_terminal|skipped_ineligible`).
7. Public / pending / revoked / blocked never receive cards.
8. Username is never delivery authority.
9. AI stays OFF; no client auto-messages; no new workflows.
