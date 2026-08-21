# RECOVERY 10:15 DUPLICATE — 2026-08-21

## Verdict

**SAME-WINDOW DUPLICATE SEND OBSERVED**

## Execution

| Field | Value |
|------|-------|
| Execution ID | `36708` |
| UTC start | `2026-08-21T07:15:11.089Z` |
| UTC stop | `2026-08-21T07:15:55.884Z` |
| MSK | ~10:15 Europe/Moscow |
| Mode | schedule trigger |
| Status | success (workflow), but duplicate Telegram |

## Window identity

| Field | Value |
|------|-------|
| Business window key | `pending-reminder:2026-08-21:10:00:Europe/Moscow` (**same** as primary) |
| Gate proceed | true |
| `last_window` at gate | still empty |
| Recovery eligibility decision | treated ADMIN_A as eligible → **send** |

## Delivery

| Field | Value |
|------|-------|
| Pending | 13 |
| Recipients resolved | 1 (ADMIN_A) |
| Claim/send | Build Claims emitted `reminder_send: true` again |
| Telegram | `ok: true`, `message_id: 1061` (duplicate digest) |
| Upsert Delivered | **429** after send |
| Mark Window Complete | ran via Sheets-error path with decision `ERROR` (not SENT) |

## Operator-visible

Same digest title `🔔 Необработанные лиды — 13` as primary.
