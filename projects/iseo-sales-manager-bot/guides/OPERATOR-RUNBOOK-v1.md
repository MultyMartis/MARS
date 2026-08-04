# Operator runbook — i-SEO Sales Manager (v1)

## Contour

- Operational.dev `xSnXPy8cEHoZw6xG` — Gmail → CLEAN → multi-recipient Telegram
- Admin.dev `wLrLp4WQHm1VJmxz` — commands + callbacks
- Sales-Manager-v2 must stay **inactive**

## Delivery health

- `/delivery_status` — counts
- `/delivery_users` — eligible recipients (no raw IDs)

## ACCESS_CONTROL

Primary authority for roles and delivery eligibility. Moderators need a prior private bot chat (`/start`).

## Incidents

If only one person receives leads: verify OPS Send nodes use `telegram_delivery_chat_id` and Expand Delivery Recipients is on the path after Format.

## Phase 3D.8 — missing action buttons

If a new pending card has no buttons, inspect Format output before changing Admin or Parser: `telegram_has_buttons` must be true, callback fields must be `sm:p:<token12>` / `sm:s:<token12>`, and `telegram_reply_markup` must survive recipient expansion and claim restore. `/leads` archive cards are intentionally buttonless. Keep AI OFF and do not restore revoked staff roles during diagnosis.

## Phase 3D.8.1 — action buttons visible but click feels stuck

1. Confirm Admin.dev active and Telegram Trigger includes `callback_query`.
2. Expect immediate toast `Обрабатываю…`; then durable reply + both card copies updated.
3. If only one card updates: check `LEAD_DELIVERIES` tab exists and has delivered rows for the lead.
4. Do not replay clicks on already-processed leads; use fresh synthetic markers for acceptance.
5. Acceptance cards: `PHASE_3D8_1_ADMIN_PROCESSED` (Андрей → processed) and `PHASE_3D8_1_MODERATOR_SPAM` (Мопс → spam).
