# LAST PRODUCTION PROCESSED CONTRACT v1

**Contract id:** `iseo-last-production-processed-v1.0`  
**Phase:** 3H.4.1  
**Audience:** Admin `/status` production line + CONFIG cache writers

## Meaning

The latest **genuine production** lead transition to status `processed` after the clean statistics epoch (`production_stats_epoch`).

## Exclusions

Must **not** count:

- test / synthetic / probable_test fixtures
- archived test fixtures
- technical events
- Telegram delivery events
- generated-reply events
- reminder / profile events
- duplicate callbacks as a *new* later time when timestamp unchanged
- legacy pre-epoch records
- spam or pending transitions

## Source precedence

1. Latest valid production `processed` event in **LEAD_EVENTS** (when available to the resolver)
2. Matching authoritative production **LEADS** `processed_at` / `lifecycle_changed_at`
3. Verified CONFIG cache `last_production_processed_at` (+ optional `last_production_processed_lead_id`)
4. Operator text `нет данных` only when no valid production processed transition exists

## CONFIG role

CONFIG `last_production_processed_*` is a **cache/summary**, not permission to contradict LEADS / LEAD_EVENTS.

Admin `/status` may use the cache when LEADS/LEAD_EVENTS are not attached to the command path, provided the cache write/read contract is tested.

## Display

- Timezone: **Europe/Moscow**
- Format: `DD.MM.YYYY HH:MM МСК` (seconds optional)
- Must not hardcode a calendar date or lead id in Status code
- Must not use `last_lead_success_at` / `last_success_at` as the production line (may be synthetic delivery)

## Writers

| Writer | May update production cache? |
|---|---|
| Genuine production processed transition / operator-approved backfill from LEADS | YES |
| Synthetic / test delivery success | NO |
| Empty Gmail poll heartbeat | NO |
| Spam / pending transitions | NO |

## Related

- `architecture/OPERATIONAL-STATUS-TRUTH-CONTRACT-v1.md`
- `architecture/CLEAN-PRODUCTION-LEDGER-v1.md`
- `implementation/LAST-PROCESSED-STATUS-READBACK-REPAIR-v1.md`
