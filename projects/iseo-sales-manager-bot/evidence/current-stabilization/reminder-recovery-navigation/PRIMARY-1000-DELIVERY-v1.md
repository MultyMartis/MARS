# PRIMARY 10:00 DELIVERY — 2026-08-21

## Verdict

**PRIMARY DELIVERY = SUCCESS**

## Execution

| Field | Value |
|------|-------|
| Execution ID | `36699` |
| UTC start | `2026-08-21T07:00:11.079Z` |
| UTC stop | `2026-08-21T07:01:23.285Z` |
| MSK | ~10:00–10:01 Europe/Moscow |
| Mode | schedule trigger |
| Status | success |

## Schedule / window

| Field | Value |
|------|-------|
| Branch | Reminder Schedule Trigger → Gate → send path |
| Business window key | `pending-reminder:2026-08-21:10:00:Europe/Moscow` |
| Gate proceed | true |
| `last_window` before | empty / null |
| last_decision before | `SKIPPED_OUTSIDE_WINDOW` (prior outside-window eval) |

## Counts / recipients

| Field | Value |
|------|-------|
| Authoritative pending | **13** |
| Active recipients | **1** (ADMIN_A, ref prefix `3FBE2132`) |
| Claim created | yes — `…|3FBE21323E22BFC1` status `claimed` |
| Telegram attempt | yes |
| Telegram result | `ok: true`, `message_id: 1060` |
| Delivery ledger write | Upsert Delivered → status `delivered`, `msg:1060` |
| Sent marker | Reminder Stamp `status=delivered` |
| `last_window` after | **NOT written** (Mark Window Complete did not run on success path) |

## Notes

ACCESS 429 retries occurred (Wait 5s/15s/30s) before successful ACCESS + claim/send.
