# LAST LEAD SUCCESS FIX v1

**Phase:** 3D.2.1  
**Node:** Operational.dev → `Update Last Success / Runtime State`  
**Code hash after:** `88C40D32B162A4EE`

## Changes

1. Prefer `$('Telegram Result Gate').first().json` for delivery truth when the gate ran.
2. Keep empty-poll detection from Switch Intake Route flags (`__empty_poll` / `intake_route=empty`).
3. On success, write: `last_lead_success_at`, `last_processed_at`, `last_success_at`, `last_delivery_status=delivered`, `last_processing_mode`, `workflow_version`, optional `parser_version`, per-message tg keys.
4. Monotonic guard: do not regress `last_lead_success_at` when CONFIG already holds a newer success timestamp.
5. Empty polls write only `last_poll_success_at`.
6. Failed Telegram paths write error fields only — never success lead stamps.

## Safe backfill

One bounded CONFIG upsert (no Gmail replay, no Telegram resend, no RAW/CLEAN rows):

| Key | Value |
|-----|-------|
| `last_lead_success_at` | `2026-07-31T17:47:40.000Z` |
| `last_processed_at` | same |
| `last_success_at` | same |
| `last_delivery_status` | `delivered` |
| `last_processing_mode` | `ai_off` |
| `workflow_version` | `Operational.dev` |

Moscow display for operators: **31.07.2026 20:47 МСК**.
