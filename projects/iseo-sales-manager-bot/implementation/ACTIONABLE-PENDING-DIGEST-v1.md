# ACTIONABLE PENDING DIGEST — Phase 3H.10

## Implementation

Admin.dev `Reminder Build Claims` embeds `iseo-pending-digest-renderer-v1.0`.

`Merge Reminder Send Payload` rehydrates chat_id / reply_text / inline keyboard after claim upsert.

`Send Reminder Telegram` uses dynamic inline keyboard from digest buttons (`sm:q:`).

Callback handlers: `queue_open` · `full_card` · early ack · expand sync events.

## Test

ADMIN_A-only temporary webhook send (deleted after). Moderators/customers: **0** test messages. No production claims / status mutations.

## Docs

- [PENDING-DIGEST-UX-CONTRACT-v1.md](../architecture/PENDING-DIGEST-UX-CONTRACT-v1.md)
- [PENDING-DIGEST-ACTION-CONTRACT-v1.md](../architecture/PENDING-DIGEST-ACTION-CONTRACT-v1.md)
- Evidence: `evidence/phase3h10/`
