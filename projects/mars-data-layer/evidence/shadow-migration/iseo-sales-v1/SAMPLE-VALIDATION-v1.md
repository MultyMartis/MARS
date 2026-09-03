# Sample lead validation (sanitized) — ISEO Sales shadow

Selection is deterministic from collapsed CLEAN statuses / counters. No PII committed.

| Sample class | Selection rule | Sheets evidence | PG evidence | Match |
|---|---|---|---|---|
| Newest-ish active (`pending`) | status=pending in collapsed set (n=29) | present in CLEAN collapse | `manager_status=pending` count=29 | PASS (aggregate) |
| Terminal processed | status=processed (n=3) | CLEAN collapse | PG count=3 | PASS |
| Spam | status=spam (n=29) | CLEAN collapse | PG count=29 | PASS |
| New | status=new (n=4) | CLEAN collapse | PG count=4 | PASS |
| Bootstrap event | every imported lead | n/a | `lead.migrated_from_sheets` = 65 | PASS |
| Domain sheet events | LEAD_EVENTS non-orphan | 126 migrated | event_type mix includes sheet + telegram_sent + manager_* | PASS |
| ACCESS admin active | ACCESS_CONTROL is_active | 1 active admin | `tg:<redacted>` admin true | PASS |
| ACCESS revoked mods | revoked/pending | 3 revoked + 1 pending | 4 inactive moderators | PASS |
| Delivery safety | historical | 264 rows | `pending_deliveries=0`; statuses sent/cancelled only | PASS |
| Reminder durable | REMINDER_DELIVERIES | 13 | 13 as `delivery_type=reminder` | PASS |

## Temporal

- Naive Sheets timestamps interpreted as Europe/Moscow (`+03:00`) → `TIMESTAMPTZ`.
- Bootstrap events use `now()` at import (not backdated to original create).
- Sheet event `occurred_at` from source `ts` when present.

## Intentionally not claimed

- Exact per-lead PII field equality (redacted; operator may spot-check offline).
- Row-number identity (rejected by design).
