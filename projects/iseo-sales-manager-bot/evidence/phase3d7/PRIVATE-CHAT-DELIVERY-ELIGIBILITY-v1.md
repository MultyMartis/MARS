# PRIVATE CHAT DELIVERY ELIGIBILITY v1

## Fact

For Telegram bots, a usable **private** chat target equals the user’s Telegram user id (same numeric string). Documented and used as `telegram_delivery_chat_id`.

## Confirmed by

Prior `/start` / direct bot interaction updating ACCESS_CONTROL `last_seen_at` / `first_seen_at`.

## Do not infer from

- username
- display name
- approval code
- group membership

## Runtime fields (derived or stored)

- `telegram_private_chat_available`
- `lead_delivery_enabled`
- `last_lead_delivery_at` / `last_lead_delivery_status` / `last_lead_delivery_error_code` (optional; LEAD_DELIVERIES is source of delivery truth)
