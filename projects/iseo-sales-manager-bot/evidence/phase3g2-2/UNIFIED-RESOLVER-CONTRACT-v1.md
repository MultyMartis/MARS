# Unified resolver contract — evidence

**Phase:** 3G.2.2
**Status:** FILLED
**Sanitized labels only:** ADMIN_A · MOD_A
**Forbidden in this file:** Telegram IDs, chat IDs, usernames, workbook IDs, URLs, raw updates, secrets.

## 1. Contract identity

`resolver_version = iseo-reply-profile-resolver-v1.0`

Full narrative contract: `architecture/UNIFIED-REPLY-PROFILE-RESOLVER-v1.md`. Runtime: `implementation/runtime-libs/reply-profile-resolver-v1.mjs`.

## 2. Single authoritative resolution function

`resolveReplyProfile(row)` is now the one function all eight read paths in `PROFILE-READ-PATH-MATRIX-v1.md` consume (directly, or via the re-exported alias `resolveRecipientReplyProfile` in `reply-profile-lib.mjs`, which shares field semantics and resolver version string).

Output fields (fixed contract):

```
resolver_version, profile_number, stable_user_ref, display_name, role, access_state,
recipient_eligible, reply_sender_name, reply_sender_enabled, reply_company_name,
profile_version, profile_valid, validation_warnings, validation,
recipient_reply_state, personalization_ready, intro_example,
role_label_ru, access_label_ru
```

## 3. Anti-wipe projection

`REPLY_PROFILE_ACCESS_FIELDS` is the explicit allowlist of profile columns that **must** survive any ACCESS_CONTROL row projection (`pickReplyProfileFields`). `Check User Authorization` now includes this allowlist in its output instead of a fixed field set that omitted it.

## 4. Auto-rehydrate on write

`mergeRehydrateIntoUpsert(row, actorLabel)` is invoked before any last-seen upsert (`/start`, `/my_status`) and before profile-view commands (`/reply_profiles`, `/reply_profile N`, `/my_reply_profile`). It:

1. Resolves the current row through `resolveReplyProfile`.
2. If profile number, name, or enabled-flag are missing/blank, looks up the approved seed for that stable identity (`approvedSeedForRow`, matched by known display cue — never by inventing a name).
3. Returns a patch restoring only the missing fields, stamped `reply_profile_updated_by=system_rehydrate` and a fresh `reply_profile_updated_at`.
4. Never creates a new row, never changes `role` or `status`, never invents a name for an identity with no approved seed match (fail-closed).

## 5. Fail-closed guarantee (proven)

| Check | Result |
|-------|--------|
| Wiped ADMIN_A row resolved without rehydrate | `personalization_ready=false`, `reply_sender_name=''` |
| Wiped ADMIN_A row after `mergeRehydrateIntoUpsert` | `reply_sender_name='Андрей'`, `reply_sender_enabled=true` |
| Nickname fallback attempted (`display_name='Мопс'` only, no seed match path) | resolver still returns `reply_sender_name=''` — no invented name |
| Display-name-as-client-name fallback attempted | resolver returns `reply_sender_name=''` |
| Username-as-client-name fallback attempted | resolver returns `reply_sender_name=''` |

Source: `implementation/harness/phase3g22-harness.mjs` checks #11–14, #51–53 — **PASS**.

## 6. Version consistency

All resolved profiles report the same `resolver_version` string regardless of entry command (`/reply_profile`, `/my_reply_profile`, `/start` line, Operational recipient expansion, `/config` summary line) — harness check #22, #29.

## Result

- [x] One resolver function backs all eight read paths
- [x] Anti-wipe allowlist deployed at the authorization projection boundary
- [x] Auto-rehydrate proven to restore ADMIN_A/MOD_A without inventing values for anyone else
- [x] Fail-closed behaviour proven under nickname/display-name/username fallback attempts
