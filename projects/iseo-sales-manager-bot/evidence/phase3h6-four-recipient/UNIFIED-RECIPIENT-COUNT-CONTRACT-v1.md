# UNIFIED RECIPIENT COUNT CONTRACT — Phase 3H.6

Contract id: `iseo-four-recipient-baseline-v1.0`

Authoritative staff eligibility for counts:

- active access
- role admin|moderator
- valid Telegram binding
- (card path additionally requires personalization enabled + approved name + profile number)

Same live ACCESS resolution should drive:

- production lead fanout
- test lead fanout
- reminder recipient selection
- `/config`
- `/reminder_status`
- delivery status/user summaries

CONFIG `pending_reminder_active_recipients_count` is a **cache**, refreshed on baseline change; must not silently disagree with ACCESS.
