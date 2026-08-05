# MOD_A self-profile root cause

**Phase:** 3G.2.2
**Status:** FILLED — root cause proven from live execution
**Sanitized labels only:** MOD_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Symptom

MOD_A (`reply_profile_number=3`, client name Михаил, enabled) showed blanks on `/my_reply_profile` after routine moderator `/start` traffic, mirroring the ADMIN_A symptom but for the moderator role.

## 2. Execution trace (proven)

Identical mechanism to ADMIN_A (see `ADMIN-A-PROFILE-LOSS-ROOT-CAUSE-v1.md` §2), exercised via the moderator path:

1. MOD_A sends `/start`.
2. **Check User Authorization** strips `reply_profile_*` fields via the same fixed-allowlist `rowFromSheet()` projection — role-agnostic defect, not Admin-only.
3. Moderator `/start` last-seen upsert writes ACCESS_CONTROL via `appendOrUpdate` with the same missing-profile-field mapping.
4. MOD_A's own row is rewritten with blank `reply_sender_name` / `reply_sender_enabled` / `reply_company_name` / `reply_profile_version`, while `reply_profile_number=3` remains intact.

## 3. Execution proof

- Live moderator `/start` was observed to wipe MOD_A's profile columns in the same execution that produced the moderator greeting (including the `Имя в ответах` line, which itself went blank as a consequence).
- `/my_reply_profile` issued after the wipe returned blank name / disabled state for the same row.
- `/reply_profile 3` (Admin-issued, read-only) could still show «Михаил» within the same operator session if that specific read occurred before the wiping upsert had executed against MOD_A's row — same point-in-time ordering artifact documented for ADMIN_A, not a second storage path.

## 4. Why this is not an Admin-only defect

The defect lives in the shared `Check User Authorization` node and the shared last-seen upsert mapping used by **every** authenticated actor (Admin and moderator alike). MOD_A's exposure confirms the defect is role-agnostic: any active Admin or moderator who sends `/start` or `/my_status` triggers the same wipe on their own row.

## 5. Root cause classification

| Item | Class |
|------|-------|
| Defect | Same field-mapping omission as ADMIN_A — shared authorization/upsert code path |
| Trigger | Any authenticated `/start` or `/my_status` from MOD_A |
| Data damage | Value wipe on sender-name/enabled/company/version columns; `reply_profile_number=3` intact |
| Row/number integrity | Unaffected — no duplicate row, no renumbering, revoked MOD_B_REVOKED/MOD_C_REVOKED numbers (2, 4) unaffected because they do not run active `/start` upserts |

## 6. Fix

Same deployed fix as ADMIN_A (`Check User Authorization` anti-wipe projection + upsert mapping sourced from top-level Prepare output + auto-rehydrate on profile-command paths). No moderator-specific patch was required because the defect and the fix are both in shared code.

## Result

- [x] Root cause proven from live execution for the moderator role
- [x] Confirmed shared (not Admin-only) defect class
- [x] Shared fix covers both ADMIN_A and MOD_A without role-specific patching
