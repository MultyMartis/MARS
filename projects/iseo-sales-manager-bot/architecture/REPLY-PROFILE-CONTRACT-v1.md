# REPLY PROFILE CONTRACT v1

**Phase:** 3G.1 (+ **3G.2** number field)  
**Version:** `iseo-recipient-name-v1.1` (was v1.0 in 3G.1)  
**Storage:** additive fields on `ACCESS_CONTROL` rows

## Fields

| Field | Type | Notes |
|-------|------|-------|
| `reply_profile_number` | positive int | **immutable** after assignment; independent of row order / Telegram ID; see [REPLY-PROFILE-NUMBERING-v1.md](REPLY-PROFILE-NUMBERING-v1.md) |
| `reply_sender_name` | string | approved client-facing first name (**only** source for client copy) |
| `reply_sender_enabled` | bool | personalization on/off |
| `reply_company_name` | string | default `INTLSEO` |
| `reply_profile_version` | string | contract version stamp |
| `reply_profile_updated_at` | string | ISO timestamp |
| `reply_profile_updated_by` | string | admin actor label |

## Validation (fail-closed name)

- Length 2–32
- Letters (Latin/Cyrillic); optional hyphen/apostrophe; no multi-token full names (no auto-shorten surname)
- Reject: empty, `@`, URLs, phones/digits, emoji, role labels, company tokens

## Resolution states

| State | Meaning |
|-------|---------|
| `ready` | valid name + enabled |
| `blocked_sender_disabled` | valid name but disabled |
| `blocked_missing_sender_name` | missing/invalid name |

## Commands

**Current (Phase 3G.2):** number-based — see [REPLY-PROFILE-ADMIN-COMMANDS-v2.md](../implementation/REPLY-PROFILE-ADMIN-COMMANDS-v2.md).

- `/reply_profiles`, `/reply_profile <N>`, `/reply_name_set <N> <имя>`, `/reply_name_enable <N>`, `/reply_name_disable <N>`
- Moderator: `/my_reply_profile` (view only)

**Obsolete (Phase 3G.1):** username/display-token addressing in [REPLY-PROFILE-COMMANDS-v1.md](../implementation/REPLY-PROFILE-COMMANDS-v1.md) — superseded; do not use for new Admin wiring.

Name/enable commands **must not** mutate ACCESS_CONTROL role or access status.

## Related

- Runtime: `implementation/runtime-libs/reply-profile-lib.mjs`
- Commands: `implementation/runtime-libs/reply-profile-commands-v1.mjs`
- Numbering: [REPLY-PROFILE-NUMBERING-v1.md](REPLY-PROFILE-NUMBERING-v1.md)
- Text: [TELEGRAM-TEXT-CONTRACT-v2.md](TELEGRAM-TEXT-CONTRACT-v2.md)

## Phase 3G.1.1 live state (historical seed)

- ACCESS_CONTROL columns **Q–V** (`reply_sender_name` … `reply_profile_updated_by`) **live and seeded**
- ADMIN_A → Андрей, enabled; MOD_A → Михаил, enabled
- MOD_B_REVOKED / MOD_C_REVOKED: prepared names **disabled**; access remains revoked
- Live Admin readback matches contract — see `evidence/phase3g1-1/LIVE-PROFILE-READBACK-v1.md`

## Phase 3G.2 number seed

| № | Label | Client name | Enabled | Access |
|---|-------|-------------|---------|--------|
| 1 | ADMIN_A | Андрей | yes | active |
| 2 | MOD_B_REVOKED | Оля | no | revoked |
| 3 | MOD_A | Михаил | yes | active |
| 4 | MOD_C_REVOKED | Никита | no | revoked |

## Phase 3G.2.2 unified resolver + anti-wipe

- Root cause proven: the routine `/start`/`/my_status` last-seen upsert wrote ACCESS_CONTROL without `reply_profile_*` fields (the upstream authorization projection had stripped them), wiping ADMIN_A and MOD_A columns on ordinary authenticated traffic — not a mutation-command defect.
- All resolution now goes through one contract, `iseo-reply-profile-resolver-v1.0` — see [UNIFIED-REPLY-PROFILE-RESOLVER-v1.md](UNIFIED-REPLY-PROFILE-RESOLVER-v1.md).
- Anti-wipe allowlist (`REPLY_PROFILE_ACCESS_FIELDS`) and auto-rehydrate (`buildProfileRehydratePatch`) deployed on the same Admin.dev workflow; fail-closed guarantees (§ above) reaffirmed and proven under wipe conditions — harness `phase3g22-harness.mjs` **53/53 PASS**.
- Evidence: `evidence/phase3g2-2/`.
