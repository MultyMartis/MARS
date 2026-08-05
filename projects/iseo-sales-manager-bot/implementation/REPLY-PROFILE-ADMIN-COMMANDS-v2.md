# REPLY PROFILE ADMIN COMMANDS v2

**Phase:** 3G.2  
**Status:** current command contract (number-based)  
**Supersedes:** [REPLY-PROFILE-COMMANDS-v1.md](REPLY-PROFILE-COMMANDS-v1.md) for addressing syntax  
**Runtime:** `implementation/runtime-libs/reply-profile-commands-v1.mjs` (v2 number API) · `reply-profile-lib.mjs`

---

## 1. Addressing

| Current (v2) | Obsolete (v1) |
|--------------|---------------|
| `/reply_profile <N>` | `/reply_profile <user>` token / username match |
| `/reply_name_set <N> <имя>` | `/reply_name_set <user> <имя>` |
| `/reply_name_enable <N>` | `/reply_name_enable <user>` |
| `/reply_name_disable <N>` | `/reply_name_disable <user>` |

`resolveAccessRowByUserToken` remains in runtime as **deprecated** helper only — Admin mutations must use `resolveAccessRowByProfileNumber`.

---

## 2. Commands

| Command | Role | Mut | Behaviour |
|---------|------|-----|-----------|
| `/reply_profiles [page]` | Admin | R | List sorted by `reply_profile_number` |
| `/reply_profile <N>` | Admin | R | Card for number N |
| `/reply_name_set <N> <имя>` | Admin | W | Validate + write name; **preserve** enable flag; **no** access change |
| `/reply_name_enable <N>` | Admin | W | Enable if valid name and active card recipient |
| `/reply_name_disable <N>` | Admin | W | Disable personalization; access unchanged |
| `/my_reply_profile` | Admin + Moderator | R | Self view only |

Moderator mutation attempts → `Эта команда доступна только администратору.`

---

## 3. Validation (name)

Fail-closed: length 2–32; Latin/Cyrillic; optional hyphen/apostrophe; single token; reject `@`, URLs, phones/digits, emoji, role labels, company tokens, multi-token full names.

---

## 4. Help

- Admin help: full profile command block (see [ROLE-AWARE-HELP-BUILDER-v2.md](ROLE-AWARE-HELP-BUILDER-v2.md)).
- Moderator help: only `/my_reply_profile` among profile commands.

---

## 5. Invariants

- Client-facing name = `reply_sender_name` only.
- Numbers immutable ([REPLY-PROFILE-NUMBERING-v1.md](../architecture/REPLY-PROFILE-NUMBERING-v1.md)).
- AI OFF; reminders OFF; no customer auto-send.
- Access grant/revoke is a **separate** command family — never side-effect of name commands.

---

## 6. Seed reference (sanitized)

1 ADMIN_A Андрей enabled · 2 MOD_B_REVOKED Оля disabled · 3 MOD_A Михаил enabled · 4 MOD_C_REVOKED Никита disabled.

## 7. Phase 3G.2.2 — resolver unification

`/reply_profiles`, `/reply_profile N`, and `/my_reply_profile` now resolve through the unified contract (`resolveReplyProfile`, `iseo-reply-profile-resolver-v1.0`) with auto-rehydrate applied before formatting, so a previously wiped row (see `evidence/phase3g2-2/`) self-corrects on the next command rather than displaying stale blanks. Mutation commands (`/reply_name_set`, `/reply_name_enable`, `/reply_name_disable`) are unchanged. See [REPLY-PROFILE-READ-PATH-UNIFICATION-v1.md](REPLY-PROFILE-READ-PATH-UNIFICATION-v1.md).
