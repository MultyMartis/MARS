# START ROUTE + HELP RENDER FORENSIC v1

**Retest window:** 2026-08-04 ≈ 01:17–01:18 +07 (= 18:17–18:18 UTC)  
**Verdict:** ATTENTION — `/START` ROUTE STILL SILENT (pre-repair3) · ATTENTION — HELP CORRUPTS CANONICAL COMMAND NAMES (Markdown)

## Fresh executions

| Exec | command | status | last node | Operator result |
|---|---|---|---|---|
| 18325 | `/start` | success | Safe Telegram Reply | SILENT |
| 18327 | `/health` | success | Safe Telegram Reply | PASS |
| 18328 | `/start` | success | Safe Telegram Reply | SILENT |
| 18329 | `/help` | success | Safe Telegram Reply | PASS (underscores eaten) |
| 18330 | `/ai_status` | success | Safe Telegram Reply | PASS |

## `/start` comparison vs `/health`

| Step | `/start` (18325/18328) | `/health` (18327) |
|---|---|---|
| normalized command | `/start` | `/health` |
| auth_role | admin | admin |
| authorized | true | true |
| Route Command | Start branch | Health branch |
| formatter items in | 1 | 1 |
| formatter items out | 1 (`reply_text` set) | 1 |
| access_registry_write | **true** | false |
| IF Access Registry Write | **true → Upsert path** | n/a (direct Capture) |
| Prepare Access Upsert | keeps `reply_text` + `chat_id` | — |
| Upsert / Append | Sheets row only | — |
| **Restore Admin Reply Target** | **reply_text="" chat_id=""** | — |
| Capture Admin Reply | empty reply | has reply |
| Safe Telegram Reply | **error / empty send** | success |

### Exact `/start` defect

Not routing, not role filter, not zero items from Start.

Start produced the temporary recovery text correctly. Because Admin `/start` sets `access_registry_write=true` (last_seen upsert), the flow continued through Sheets. **`Restore Admin Reply Target` read `$input` (Sheets event row)** instead of Prepare/Start context → wiped `reply_text` and `chat_id` → Telegram send failed silently (execution still marked success at workflow level with error item on send).

## Help underscore defect

Help formatter output **contained** canonical `/last_error`, `/ai_status`, `/moderator_pending`.

Telegram stored message text showed `/lasterror`, `/moderatorpending` with **`italic` entities** — classic Markdown `_…_` consumption.

Cause: n8n Telegram node effectively applied Markdown when `parse_mode` was unset. Not a command-router rename.

## Repair-3 (applied 2026-08-03T18:28:36Z)

1. `Restore Admin Reply Target` restores from `$('Prepare Access Upsert')` / `$('Start')`.
2. Role-aware `/start` restored (`startReply`); temporary recovery string removed.
3. Admin help wraps commands in `<code>/…</code>`; Safe Telegram Reply `parse_mode=HTML`.
4. Operational.dev untouched; no new workflow.

## Retest

Ask Андрей for **one** real `/start` only.
