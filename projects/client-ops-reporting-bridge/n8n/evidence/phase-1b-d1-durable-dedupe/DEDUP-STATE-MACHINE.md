# Dedupe State Machine — D1

## Classifications

| State | Meaning | Telegram |
|---|---|---|
| FIRST_SEEN | No durable row for event_id | Allowed (Pattern B) |
| DUPLICATE | Same event_id + same fingerprint | Blocked |
| EVENT_ID_CONFLICT | Same event_id + different fingerprint | Blocked |

## Delivery states (row field)

| State | Meaning |
|---|---|
| PENDING | Claimed on FIRST_SEEN insert |
| SENT | Deferred — not updated after Telegram in D1 |
| FAILED | Deferred |
| NOT_ATTEMPTED | Not used on accepted path |

## Transitions (sequential)

new event → insert claim FIRST_SEEN/PENDING → Respond 202 → Telegram
replay same fp → DUPLICATE → Respond 200 DUPLICATE_SUPPRESSED → no Telegram
same id different fp → EVENT_ID_CONFLICT → Respond 409 → no Telegram; original row retained
