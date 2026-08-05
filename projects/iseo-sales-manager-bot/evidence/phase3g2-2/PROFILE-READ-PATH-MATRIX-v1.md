# Profile read-path matrix

**Phase:** 3G.2.2
**Status:** FILLED
**Sanitized labels only:** ADMIN_A · MOD_A · MOD_B_REVOKED · MOD_C_REVOKED
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Purpose

Enumerate every Admin.dev / Operational.dev code path that reads or projects ACCESS_CONTROL profile fields, and record whether each path was divergent (its own field mapping) or unified (single resolver) at forensic time versus after the Phase 3G.2.2 patch.

## 2. Matrix

| # | Read path | Command / trigger | Pre-patch behaviour | Post-patch behaviour |
|---|-----------|--------------------|----------------------|-----------------------|
| 1 | Check User Authorization | every command (auth gate) | `rowFromSheet()` projected a fixed field allowlist that **excluded** `reply_profile_*` columns — silently dropped them from the in-memory row | Projects full row incl. `reply_profile_*` fields (anti-wipe fix); unified resolver contract |
| 2 | `/reply_profiles` list | Admin | own mapping via `resolveRecipientReplyProfile` | unchanged mapping, now guaranteed to see intact fields upstream |
| 3 | `/reply_profile N` | Admin | own mapping via `resolveRecipientReplyProfile` | unified resolver `resolveReplyProfile` (aliased contract) |
| 4 | `/my_reply_profile` | Admin + moderator | own mapping via `formatReplyProfileCard` | unified via `formatMyReplyProfile` / `resolveReplyProfile` |
| 5 | `/start` reply-name line | Admin + moderator | read `reply_sender_name` off post-Check-User row (already stripped upstream) | reads post-rehydrate row; auto-rehydrate patch applied before formatting |
| 6 | `/start` / `/my_status` last-seen upsert | Admin + moderator | `appendOrUpdate` wrote `display_name` / `role` / `status` / `last_seen_at` only — **missing `reply_profile_*` keys in the upsert mapping wiped those cells on write** | Upsert now includes profile fields sourced from top-level Prepare output; rehydrate patch merged before upsert |
| 7 | Operational recipient expansion | lead card personalization | its own `resolveRecipientReplyProfile`-equivalent inline logic | now consumes `iseo-reply-profile-resolver-v1.0` contract fields; version stamped in Expand Delivery Recipients |
| 8 | Config Summary personalization line | `/config` | derived active-recipient count from its own scan | now stamps `resolver_version=iseo-reply-profile-resolver-v1.0` and reads the same unified fields |

## 3. Divergence count

| Counter | Pre-patch | Post-patch |
|---------|----------:|-----------:|
| Divergent profile read paths (own field mapping, no shared contract) | 6 of 8 | 0 of 8 |
| Paths sharing one resolver contract (`iseo-reply-profile-resolver-v1.0`) | 2 of 8 | 8 of 8 |

## 4. Note on apparent inconsistency

`/reply_profile 3` and moderator `/start` could still display «Михаил» from **pre-wipe** reads earlier in the same operator session (cached row from before the wiping upsert executed); `/my_reply_profile` issued **after** the wipe on the same identity showed blanks. This is consistent with a point-in-time column wipe, not with two different storage locations or a race in the resolver itself — see `ADMIN-A-PROFILE-LOSS-ROOT-CAUSE-v1.md` §4.

## Result

- [x] All read paths enumerated
- [x] Divergence counted pre/post patch
- [x] Unified contract now covers all 8 paths
