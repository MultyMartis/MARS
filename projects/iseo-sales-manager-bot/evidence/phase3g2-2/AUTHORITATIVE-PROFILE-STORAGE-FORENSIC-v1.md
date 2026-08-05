# Authoritative profile storage forensic

**Phase:** 3G.2.2
**Status:** FILLED — live forensic
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Scope

Determine the single authoritative storage location for reply-profile fields (`reply_profile_number`, `reply_sender_name`, `reply_sender_enabled`, `reply_company_name`, `reply_profile_version`, `reply_profile_updated_at`, `reply_profile_updated_by`) and account for why ADMIN_A and MOD_A profile values were observed empty after routine `/start` traffic.

## 2. Storage location (authoritative)

- Single sheet/tab: `ACCESS_CONTROL`.
- Profile columns are **additive** columns on the same row as `role` / `status` / `display_name` — not a separate tab, not a separate keyed store.
- No secondary or shadow profile table exists in the live contour. Reply-profile state has exactly **one** source of truth.

## 3. Row inventory

| Check | Result |
|-------|--------|
| Authoritative profile rows | 4 |
| Duplicate profile rows (same stable identity, two rows) | 0 |
| Rows with missing `reply_profile_number` column entirely (schema absent) | 0 — column present on all 4 rows |
| Rows with `reply_profile_number` present but other profile fields blank | 2 (ADMIN_A, MOD_A) at forensic capture time |
| Rows with full profile intact | 2 (MOD_B_REVOKED, MOD_C_REVOKED — revoked, disabled) |

## 4. Key finding

ADMIN_A and MOD_A did **not** lose their row, their `reply_profile_number`, or gain a duplicate row. Their `reply_sender_name` / `reply_sender_enabled` / `reply_company_name` / `reply_profile_version` cells were **emptied in place** by an upsert that omitted those fields while rewriting the row. MOD_B_REVOKED and MOD_C_REVOKED kept full profile data because they did not run an active `/start` (or `/my_status`) upsert in the affected window (see `ADMIN-A-PROFILE-LOSS-ROOT-CAUSE-v1.md`, `MOD-A-SELF-PROFILE-ROOT-CAUSE-v1.md`).

## 5. Why revoked profiles kept numbers 2 and 4

Numbers are immutable and independent of upsert activity. MOD_B_REVOKED (2) and MOD_C_REVOKED (4) are revoked and do not exercise the authenticated `/start` / `/my_status` path that triggers the wiping upsert, so their columns were never rewritten in the incident window. This is consistent with the numbering contract, not a separate repair.

## 6. Conclusion

- One authoritative table, one row per stable identity, no duplication.
- Loss mechanism is column-level value wiping on write, not row loss, not renumbering, not identity collision.
- Full mechanism traced in `ADMIN-A-PROFILE-LOSS-ROOT-CAUSE-v1.md` and `MOD-A-SELF-PROFILE-ROOT-CAUSE-v1.md`.

## Result

- [x] Single authoritative store confirmed
- [x] Row/duplicate inventory taken
- [x] Wipe mechanism (not loss/duplication) established
