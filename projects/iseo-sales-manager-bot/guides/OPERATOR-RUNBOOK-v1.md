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
