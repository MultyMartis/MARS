# UNIFIED REPLY PROFILE RESOLVER v1

**Phase:** 3G.2.2 (+ 3G.2.3 Start read-after-rehydrate)
**Version:** `reply_profile_resolver_version = iseo-reply-profile-resolver-v1.0`
**Status:** current authority for reply-profile resolution across all read paths
**Supersedes:** ad hoc per-path field projection described implicitly in [REPLY-PROFILE-CONTRACT-v1.md](REPLY-PROFILE-CONTRACT-v1.md) prior to 3G.2.2

---

## 1. Problem this contract solves

Before Phase 3G.2.2, each Telegram command surface and the Admin authorization gate independently read and projected ACCESS_CONTROL rows. One of those projections (`Check User Authorization` → `rowFromSheet()`) used a fixed field allowlist that did not include reply-profile columns, and the routine `/start` / `/my_status` last-seen upsert wrote the row back without those fields — silently wiping ADMIN_A and MOD_A profile data on ordinary authenticated traffic. See `evidence/phase3g2-2/AUTHORITATIVE-PROFILE-STORAGE-FORENSIC-v1.md` and `evidence/phase3g2-2/PROFILE-READ-PATH-MATRIX-v1.md` for the full forensic.

This contract establishes **one** resolution function and **one** anti-wipe projection allowlist that every read and write path must use.

---

## 2. Single authoritative store

Reply-profile fields live as additive columns on `ACCESS_CONTROL` rows only. There is no secondary or shadow profile table. See [REPLY-PROFILE-CONTRACT-v1.md](REPLY-PROFILE-CONTRACT-v1.md) for the field list.

---

## 3. Resolution function

`resolveReplyProfile(row, opts)` — `implementation/runtime-libs/reply-profile-resolver-v1.mjs`.

Fixed output contract:

```
resolver_version, profile_number, stable_user_ref, display_name, role, access_state,
recipient_eligible, reply_sender_name, reply_sender_enabled, reply_company_name,
profile_version, profile_valid, validation_warnings, validation,
recipient_reply_state, personalization_ready, intro_example,
role_label_ru, access_label_ru
```

`reply-profile-lib.mjs` retains `resolveRecipientReplyProfile(row)` as a compatible sibling used by the command-formatting helpers; both share `REPLY_PROFILE_RESOLVER_VERSION = 'iseo-reply-profile-resolver-v1.0'` and identical field semantics — see `evidence/phase3g2-2/UNIFIED-RESOLVER-CONTRACT-v1.md` for the equivalence proof.

---

## 4. Read paths bound to this contract

All eight enumerated read paths (`evidence/phase3g2-2/PROFILE-READ-PATH-MATRIX-v1.md`) resolve through this contract:

1. `Check User Authorization` (auth gate, all commands)
2. `/reply_profiles`
3. `/reply_profile N`
4. `/my_reply_profile`
5. `/start` reply-name line
6. `/start` / `/my_status` last-seen upsert (write path)
7. Operational recipient expansion (lead-card personalization)
8. `/config` Config Summary personalization line

---

## 5. Anti-wipe projection

`REPLY_PROFILE_ACCESS_FIELDS` (frozen list) is the mandatory allowlist for any ACCESS_CONTROL row projection that will later be used to construct an upsert. `pickReplyProfileFields(row)` extracts exactly these fields for merge-forward into a write. `Check User Authorization` must include this allowlist in its output — omitting it reproduces the Phase 3G.2 defect class.

```
reply_profile_number, reply_sender_name, reply_sender_enabled,
reply_company_name, reply_profile_version,
reply_profile_updated_at, reply_profile_updated_by
```

---

## 6. Auto-rehydrate on read and write

`buildProfileRehydratePatch(row, actorLabel)` and `mergeRehydrateIntoUpsert(row, actorLabel)`:

1. Resolve the row through the unified contract.
2. If `reply_profile_number`, `reply_sender_name`, or `reply_sender_enabled` are missing/blank, look up the approved seed for that stable identity via `approvedSeedForRow` (matched only against known approved display cues — never invented).
3. Return a patch that fills only the missing fields, stamped `reply_profile_updated_by=system_rehydrate`.
4. Never create a new row. Never change `role` or `status`. Never invent a name for an identity with no approved seed match (fail-closed — see §7).

Rehydrate is invoked:

- Before formatting any of the four profile-view commands (§4.2–4.5).
- Before every `/start` / `/my_status` last-seen upsert, merged into the write mapping so the write itself cannot re-wipe the row.

### Phase 3G.2.3 — `/start` must consume post-rehydrate output

Rehydrate in Check User Authorization alone is insufficient if Start still reads the pre-rehydrate sheet item. **Single-execution consistency:** moderator `/start` must resolve `Имя в ответах` from `access_upsert.reply_sender_name` (post-rehydrate) via this contract — not from the blank `Read ACCESS_CONTROL` snapshot and not from the next command. Helper: `resolveStartReplySenderName` in `reply-profile-resolver-v1.mjs`. Evidence: `evidence/phase3g2-3/`.

---

## 7. Fail-closed guarantee (unchanged, reaffirmed)

- Never derive a client-facing name from Telegram display name, username, actor label, or role label.
- A row with no approved seed match and no valid `reply_sender_name` resolves to `reply_sender_name=''`, `personalization_ready=false` — never a fallback guess.
- Rehydrate restores **only** approved seed values for identities that already had one; it does not create profiles for new identities.

Proof: `implementation/harness/phase3g22-harness.mjs` checks #11–14, #51–53 — PASS.

---

## 8. Version stamping

Every surface that resolves a profile — including the Operational.dev recipient expansion and the Admin `/config` summary line — stamps the same `resolver_version` string, so operators can confirm all paths are on one contract at a glance (harness check #22, #29).

---

## 9. Related

- [REPLY-PROFILE-CONTRACT-v1.md](REPLY-PROFILE-CONTRACT-v1.md)
- [REPLY-PROFILE-NUMBERING-v1.md](REPLY-PROFILE-NUMBERING-v1.md)
- [RECIPIENT-PERSONALIZED-REPLIES-v1.md](RECIPIENT-PERSONALIZED-REPLIES-v1.md)
- [../implementation/REPLY-PROFILE-READ-PATH-UNIFICATION-v1.md](../implementation/REPLY-PROFILE-READ-PATH-UNIFICATION-v1.md)
- Runtime: `implementation/runtime-libs/reply-profile-resolver-v1.mjs`, `reply-profile-lib.mjs`, `reply-profile-commands-v1.mjs`
- Evidence: `evidence/phase3g2-2/`
