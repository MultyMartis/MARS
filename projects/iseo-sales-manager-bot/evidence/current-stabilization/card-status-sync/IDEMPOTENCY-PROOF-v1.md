# IDEMPOTENCY PROOF — post-repair

## Spam (execs `36665` → `36666`)

| Step | outcome | status | events | updates | edit |
|------|---------|--------|--------|---------|------|
| first Spam | applied | spam | 1 | 1 | ok |
| second Spam | idempotent | spam | 0 | 0 | message not modified (expected) |

No duplicate lifecycle event. Authoritative status remains spam.

## Processed (exec `36658`)

| Step | outcome | status | events | updates |
|------|---------|--------|--------|---------|
| repeat Processed | idempotent | processed | 0 | 0 |

## Note on Telegram `message is not modified`

Idempotent re-edit of an already-terminal card can return Telegram’s unchanged-message error. Aggregate may record `card_sync_ok=0` for that repeat. This is distinct from the empty-button failure class and does not regress authoritative state or first-transition UI sync.
