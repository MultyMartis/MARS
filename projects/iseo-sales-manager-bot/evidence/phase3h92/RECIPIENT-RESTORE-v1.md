# RECIPIENT RESTORE — Phase 3H.9.2

**Profile restored:** MOD_A (existing row, profile_no **3**, same staff identity hash `518CC34C4C0F`).  
**Profiles created:** 0. **Renumbered:** 0. **Other recipients mutated:** 0.

## Contract used

Existing Admin `/moderator_add <code>` (Unknown Command → Prepare Access Upsert → Upsert ACCESS_CONTROL → Append ACCESS_EVENTS).

Telegram Trigger is secret-gated; a **temporary** Admin webhook node `P3H92 Restore WH` was added for the restore wave and **removed** in `finally`. Admin code hashes vs pre-change: **0 deltas**. Node count 100. Temp webhook left: **false**.

## Executions (Europe/Moscow 2026-08-17)

| Exec | Command | Result |
|---|---|---|
| `33571` | `/moderator_add` as ADMIN_A | ACCESS_EVENTS `moderator_approved` revoked→active. Notify Access Subject **did not run** (Sheets nodes strip `notify_text`). |
| `33572` | `/start` as MOD_A identity, **ADMIN_A chat** | Existing `rehydrateReplyProfile` seed restored profile_no=3, name present, enabled=true. Reply targeted ADMIN_A chat. |
| `33573` | `/moderators` | Live staff = 4 |
| `33574` | `/reminder_status` | Recipients: 4 |
| `33575` | `/pending_count` | Authoritative pending 13 — statuses not mutated |

## Historical fan-out

Lead send nodes were not on this path. Reminder send was not invoked. Historical leads replayed: **0**.
