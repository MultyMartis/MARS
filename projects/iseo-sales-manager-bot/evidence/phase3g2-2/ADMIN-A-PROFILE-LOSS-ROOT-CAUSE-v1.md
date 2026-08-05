# ADMIN_A profile loss — root cause

**Phase:** 3G.2.2
**Status:** FILLED — root cause proven from live execution
**Sanitized labels only:** ADMIN_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Symptom

ADMIN_A (`reply_profile_number=1`, client name Андрей, enabled) intermittently showed a blank `reply_sender_name` / disabled personalization on `/my_reply_profile` and on the `/start` reply-name line, despite the profile having been correctly seeded and previously confirmed enabled in Phase 3G.1.1 / 3G.2.

## 2. Execution trace (proven)

1. ADMIN_A sends `/start` (or `/my_status`).
2. **Check User Authorization** reads the ACCESS_CONTROL row and projects it through `rowFromSheet()`.
3. `rowFromSheet()` used a **fixed output field allowlist** that did not include `reply_profile_number`, `reply_sender_name`, `reply_sender_enabled`, `reply_company_name`, `reply_profile_version`, `reply_profile_updated_at`, or `reply_profile_updated_by`. These fields were silently dropped from the in-memory authorization context.
4. Downstream **last-seen upsert** (`appendOrUpdate` targeting ACCESS_CONTROL) built its write mapping from this already-stripped context plus a small set of top-level fields (`display_name`, `role`, `status`, `last_seen_at`). The upsert mapping mixed top-level core fields with `access_upsert.*` profile fields but did not carry the actual profile values forward.
5. Because `appendOrUpdate` performs a full-row style upsert keyed by stable identity, columns not present in the write mapping are written as empty rather than left untouched.
6. Net effect: the same `/start` execution that authenticated ADMIN_A also **wiped** ADMIN_A's own profile columns on that row.

## 3. Execution proof

- Live admin `/start` was observed to wipe ADMIN_A's profile columns in the same request/response cycle that produced the greeting reply — i.e. the wipe is a side effect of a **read-then-upsert** path triggered by routine `/start` traffic, not a separate mutation command.
- No `/reply_name_set`, `/reply_name_disable`, or other explicit profile-mutation command was involved in the wipe.
- No duplicate row was created; the same row (same stable identity, same `reply_profile_number=1`) was rewritten in place.

## 4. Why `/reply_profile 3` and moderator `/start` could still show Михаил in the same window

Telegram command handling in the same operator session could read an ACCESS_CONTROL snapshot fetched **before** the wiping upsert had executed for that particular row (each command performs its own fresh Sheets read at dispatch time). A `/my_reply_profile` issued **after** the wipe on the same row correctly showed blanks, because it read the now-wiped cells. This is a **point-in-time ordering artifact of repeated independent reads**, not evidence of two storage locations, a race inside the resolver, or values "shifting" between rows.

## 5. Root cause classification

| Item | Class |
|------|-------|
| Defect | Field-mapping omission in `rowFromSheet()` projection (read side) + `appendOrUpdate` upsert mapping (write side) |
| Trigger | Any authenticated `/start` or `/my_status` from ADMIN_A |
| Data damage | Value wipe on 5 of 7 profile columns (`reply_profile_number` observed intact in this row; sender fields wiped) |
| Row/number integrity | Unaffected — no duplicate row, no renumbering |

## 6. Fix

- `Check User Authorization` no longer strips `reply_profile_*` fields (`REPLY_PROFILE_ACCESS_FIELDS` allowlist added to the projection).
- Last-seen upsert mapping now sources profile fields from top-level Prepare output (`mergeRehydrateIntoUpsert`) instead of from the stripped context, so a routine `/start` can no longer silently blank profile columns.
- Auto-rehydrate (`buildProfileRehydratePatch`) restores approved seed values for ADMIN_A the next time a rehydrate-covered command runs against this row, without requiring a manual admin re-entry of the name.

## Result

- [x] Root cause proven from live execution, not simulation
- [x] Wipe mechanism isolated to `/start` / `/my_status` upsert path
- [x] Fix deployed to same workflow (see `UNIFIED-RESOLVER-CONTRACT-v1.md` and `ADMIN-A-RESTORE-v1.md` in this evidence set)
