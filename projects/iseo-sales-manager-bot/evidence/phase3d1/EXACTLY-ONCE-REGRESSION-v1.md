# EXACTLY-ONCE-REGRESSION-v1

**Phase:** 3D.1

## Preserved from Phase 3D

- Intake Gate + Switch route
- `IF Need Telegram Send` / `Telegram Skip Pass`
- CONFIG keys `tg_delivered:<gmail_message_id>` / `tg_attempts:<gmail_message_id>`
- Max attempts bound → `telegram_retry_exhausted`
- Resume Gmail finalize without resend when already delivered

## Parser repair interaction

- Already PROCESSED malformed audit-form message was **not** auto-replayed.
- Preferred path: one **new** clean website test after readiness notice.
- Idempotency nodes untouched by parser patch (node count remained 34).

## Post-repair observation

See `CLEAN-LEAD-END-TO-END-v1.md` / `PRODUCTION-TELEGRAM-CARD-ACCEPTANCE-v1.md` for whether a new lead arrived in the observe window and whether duplicate cards stayed at zero across ≥3 later polls.
