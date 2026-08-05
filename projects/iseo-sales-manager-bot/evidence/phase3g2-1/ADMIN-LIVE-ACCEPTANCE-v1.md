# Admin live acceptance — Phase 3G.2.1

**Status:** ENGINEERING READY — OPERATOR VISUAL PENDING

Agent cannot inject Telegram Trigger updates (webhook returns `Provided secret is not valid`). Pre-repair silent executions forensically proven. Post-repair Code nodes parse; offline harness **37/37 PASS**.

## Operator checklist (required)

As ADMIN_A send exactly once each:

1. `/help` — expect full Admin help (reply-profile section present)
2. `/start` — INTLSEO ready text; AI/reminders выключены
3. `/config` — safe summary; no secrets
4. `/ai_status` — OFF
5. `/stats` — epoch 05.08.2026 posture
6. `/reply_profiles`
7. `/reply_profile 3`

Expect: one response each; no silence; no duplicates; no malformed HTML.
