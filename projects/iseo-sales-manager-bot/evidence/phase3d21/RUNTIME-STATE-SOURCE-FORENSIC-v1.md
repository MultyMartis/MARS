# RUNTIME STATE SOURCE FORENSIC v1

**Phase:** 3D.2.1  
**Clean lead exec hash:** `F14196515232982B`  
**Started:** 2026-07-31T17:47:30.074Z

## Path observed

Gmail fetch → Parse Lead → … → Send Telegram Lead Card → Telegram Result Gate (`telegram_ok=true`) → Append LEAD_EVENTS → Gmail PROCESSED / Remove Incoming → **Update Last Success / Runtime State** → Apply Runtime State CONFIG

## Defect

`Update Last Success / Runtime State` used `$input.first().json` only.

After Gmail finalize, `$input` was a Gmail API stub (`id`, `threadId`, `labelIds`) **without** `telegram_ok` / lead fields.

Therefore `isSuccess` evaluated false and the node wrote:

- `last_error_at`
- `last_error_code` = `processing_error`
- `last_error_stage` = `unknown`
- `last_delivery_status` = `failed`

It did **not** write `last_lead_success_at` / `last_processed_at` / success delivery fields.

## Consequences for `/status`

Admin Status reads `last_lead_success_at || last_success_at` from CONFIG. Those keys stayed at the pre-clean-lead stamp (**30.07.2026 22:49 МСК**), while polls correctly refreshed `last_poll_success_at`.

## Ruled out

- Test-name heuristics excluding the clean lead from success write (gate had `telegram_ok=true`; Update never saw it)
- Admin reading a different workbook (same CONFIG doc)
- Timestamp render bug (formatter correct; source stale)

## Fix pointer

See `LAST-LEAD-SUCCESS-FIX-v1.md`.
