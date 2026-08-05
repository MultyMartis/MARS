# REPLY PROFILE NUMBERING v1

**Phase:** 3G.2  
**Field:** `reply_profile_number`  
**Personalization version:** `iseo-recipient-name-v1.1`  
**Status:** immutable numbering contract

---

## 1. Rules

1. Every Admin/moderator ACCESS_CONTROL row that participates in reply profiles receives a **positive integer** `reply_profile_number`.
2. Numbers are **immutable after assignment**. Never renumber when sorting, editing names, enabling/disabling, granting, or revoking access.
3. Numbers are **independent** of:
   - Google Sheets row order
   - Telegram user ID
   - username / display_name
   - grant/revoke chronology
4. **No reuse:** a retired number is not reassigned to a different person. New people get `max(existing)+1` (see runtime `nextProfileNumber`).
5. Admin mutation commands address profiles **only by number** (`/reply_profile N`, `/reply_name_set N …`, etc.).
6. Changing `reply_sender_name` / enable flags **must not** change ACCESS_CONTROL `role` or `status`.

---

## 2. Initial assignment (seed — do not rearrange)

| reply_profile_number | Sanitized label | Internal display cue | Client-facing name | Enabled | Access |
|---------------------:|-----------------|----------------------|--------------------|---------|--------|
| 1 | ADMIN_A | Андрей | Андрей | enabled | active |
| 2 | MOD_B_REVOKED | Ola4seo | Оля | disabled | revoked |
| 3 | MOD_A | Мопс | Михаил | enabled | active |
| 4 | MOD_C_REVOKED | Никита | Никита | disabled | revoked |

Notes:

- №2 and №4 keep numbers while revoked — ineligible for cards until access restored by a separate access command.
- Client copy for №3 uses **Михаил** only; nickname «Мопс» never appears in customer text.

---

## 3. Resolution

| State | Condition |
|-------|-----------|
| `ready` | valid `reply_sender_name` + enabled + (for delivery) active Admin/moderator |
| `blocked_sender_disabled` | valid name, enabled=false |
| `blocked_missing_sender_name` | missing/invalid name |

Delivery eligibility remains ACCESS_CONTROL role+status; numbering alone does not grant cards.

---

## 4. Related

- [REPLY-PROFILE-CONTRACT-v1.md](REPLY-PROFILE-CONTRACT-v1.md) (fields; + number delta)
- [REPLY-PROFILE-ADMIN-COMMANDS-v2.md](../implementation/REPLY-PROFILE-ADMIN-COMMANDS-v2.md)
- [UNIFIED-REPLY-PROFILE-RESOLVER-v1.md](UNIFIED-REPLY-PROFILE-RESOLVER-v1.md) — Phase 3G.2.2 resolver contract
- Runtime: `implementation/runtime-libs/reply-profile-lib.mjs`
- Evidence stubs: `PROFILE-NUMBER-CONTRACT-v1.md`, `PROFILE-NUMBER-SEED-v1.md`, `PROFILE-NUMBER-STABILITY-v1.md` under `evidence/phase3g2/`

## 5. Phase 3G.2.2 — numbering held through wipe/rehydrate

The ADMIN_A/MOD_A profile-value wipe (Phase 3G.2.2 forensic) did **not** touch `reply_profile_number` on any row — numbers 1–4 remained intact and unique throughout. Auto-rehydrate only fills blank name/enabled fields for an identity with an existing approved seed; it never assigns or reassigns a number. Proof: `evidence/phase3g2-2/PROFILE-NUMBER-INVARIANTS-v1.md`.
