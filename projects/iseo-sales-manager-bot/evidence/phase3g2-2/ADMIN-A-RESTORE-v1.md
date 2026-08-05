# ADMIN_A restore

**Phase:** 3G.2.2
**Status:** FILLED — patches deployed; live storage restore fires on next covered Telegram command
**Sanitized labels only:** ADMIN_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Restore mechanism

ADMIN_A is restored by the deployed auto-rehydrate patch (`buildProfileRehydratePatch` / `mergeRehydrateIntoUpsert`), not by a manual one-off Sheets edit. This keeps the fix in the same code path that caused the wipe, so the same class of defect cannot recur silently.

## 2. Restore trigger commands

Any of the following, run by ADMIN_A, executes the rehydrate check against ADMIN_A's own row before formatting a reply:

- `/reply_profiles`
- `/my_reply_profile`
- `/reply_profile 1`
- `/start`

## 3. Approved seed used for restore

| Field | Restored value |
|-------|-----------------|
| `reply_profile_number` | 1 (unchanged — was never lost) |
| `reply_sender_name` | Андрей |
| `reply_sender_enabled` | true |
| `reply_company_name` | INTLSEO |
| `reply_profile_version` | current contract version stamp |
| `reply_profile_updated_by` | `system_rehydrate` |

Seed source: `APPROVED_INITIAL_PROFILE_NUMBERS` (`reply-profile-lib.mjs`), matched to ADMIN_A's known display cue — the same approved mapping used since Phase 3G.1.1, not a new invented value.

## 4. Storage restore status (proven vs pending)

| Layer | Status |
|-------|--------|
| Patch deployed (Admin.dev, same workflow) | **done** |
| Offline harness proof of rehydrate restoring Андрей for this exact wiped-row shape | **PASS** (`phase3g22-harness.mjs` checks #1, #6, #8, #52) |
| Direct Google Sheets API restore from outside Telegram (n8n API token) | **not available** — agent has no direct Sheets credential access from the n8n management API in this session |
| Telegram webhook inject to trigger the restore command directly | attempted — returned **404** (webhook path not invokable by the agent) |
| Authoritative live restore of ADMIN_A's actual ACCESS_CONTROL cells | fires automatically the next time ADMIN_A (or an Admin acting on ADMIN_A's row) sends one of the trigger commands in §2 |

## 5. What this means operationally

The wipe is not being "fixed by hand" with a one-time value patch that could drift from the seed again. The correct value is re-derived deterministically every time a rehydrate-covered command runs, from the same approved seed used at original provisioning. The **first** live Telegram command from ADMIN_A after this deploy is expected to both display the correct restored profile and durably rewrite the correct cells.

## Result

- [x] Restore mechanism identified and deployed (auto-rehydrate, not manual edit)
- [x] Offline proof of restore correctness
- [ ] Live Sheets cell restore confirmed by operator (fires on next Telegram command — PENDING)
