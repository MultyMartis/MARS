# TELEGRAM-DELIVERY-IDEMPOTENCY-v1

**Phase:** 3D  
**Workflow:** Operational.dev (patched in place)

## Required evidence fields

| Field | Source |
|-------|--------|
| `gmail_message_id` | Parse Lead / lead object |
| stable `lead_id` | Parse Lead |
| `delivery_status` | Classify / Format (`pending` \| `retrying` \| `delivered` \| `exhausted`) |
| `telegram_delivered_at` | CONFIG key `tg_delivered:<gmail_message_id>` after success |
| `delivery_attempt_count` | CONFIG key `tg_attempts:<gmail_message_id>` + Format increment |

## Behavior

1. Before send, Classify reads CONFIG delivery keys for this Gmail message.  
2. If already delivered → Format sets `skip_telegram=true`.  
3. `IF Need Telegram Send` routes skip → `Telegram Skip Pass` → Result Gate (`telegram_ok=true`) → Gmail PROCESSED / remove incoming.  
4. If not delivered → Send Telegram as usual.  
5. On success, Update Runtime writes `tg_delivered:*` and `tg_attempts:*`.  
6. On failure, attempts increment; at **5** attempts Format forces `telegram_retry_exhausted` (no unlimited cards).

## Guarantees

- Same Gmail message cannot produce unlimited Telegram cards.  
- Successful delivery marks idempotency key independent of Gmail unread state.  
- Gmail finalization can safely resume without re-sending the card.  
- Does not depend only on Gmail unread.

## Nodes added (same workflow)

- `IF Need Telegram Send`
- `Telegram Skip Pass`

No new workflows. Sales-Manager-v2 untouched. AI remains OFF.
