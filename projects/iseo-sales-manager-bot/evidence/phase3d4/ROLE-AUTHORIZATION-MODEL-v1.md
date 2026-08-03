# ROLE AUTHORIZATION MODEL v1

**Phase:** 3D.4  
**Product:** i-SEO Sales Manager Bot

---

## 1. Role tiers

| Role | CONFIG gate | Capabilities | Denied |
|------|-------------|--------------|--------|
| **admin** | `admin_user_ids` | All Admin text commands (`/status`, `/leads`, `/ai_on`, …) | — |
| **manager** | `manager_action_user_ids` | Inline lead-action callbacks only (processed / spam) | Admin text commands |
| **unauthorized** | neither list | — | All commands and callbacks |

Roles are **independent lists**. Manager membership does **not** imply Admin membership.

---

## 2. CONFIG keys

| Key | Type | Phase 3D.4 state |
|-----|------|------------------|
| `admin_user_ids` | string_list | **1** identity (operator hash **3FBE21323E22BFC1**) |
| `manager_action_user_ids` | string_list | **2** identities: operator + Olya (**E6714550214106BA**) |

**Fallback rule (Phase 3D.3):** when `manager_action_user_ids` was empty, callbacks fell back to `admin_user_ids`. Phase 3D.4 **breaks the fallback** by explicitly seeding manager IDs — Olya no longer depends on admin fallback for callback auth.

---

## 3. Olya placement

| List | Olya (hash E6714550214106BA) |
|------|------------------------------|
| `admin_user_ids` | **not present** |
| `manager_action_user_ids` | **present** |

Olya is **manager-only**: she may tap lifecycle buttons on lead cards; she may **not** run `/status`, `/leads`, `/config`, or any other Admin command.

---

## 4. Authorization flow

### Text commands (Admin.dev)

```
Telegram message → Normalize Command → Read CONFIG
  → Check User Authorization (admin_user_ids)
       allow → Route Command
       deny  → «Доступ запрещён.»
```

### Inline callbacks (Admin.dev)

```
callback_query → Normalize Command → Read CONFIG
  → Check Manager Action Authorization (manager_action_user_ids)
       allow → Resolve Lead by Token → State Machine → Sheets → Edit card
       deny  → «Доступ запрещён.» (no Sheets mutation)
```

---

## 5. Role-aware `/start` and `/help`

Managers enrolled in `manager_action_user_ids` but **not** in `admin_user_ids` receive a **manager-specific** greeting and help text when they `/start` or `/help` — not the Admin panel. See `MANAGER-START-HELP-ACCEPTANCE-v1.md`.

Unauthorized users receive `Доступ запрещён.` for both paths.

---

## 6. Security notes

- Do not reveal allowlist contents in Telegram replies (count-only in `/config` for admins).
- Do not add managers to `admin_user_ids` as a convenience shortcut.
- Hashes in documentation are for cross-reference only; runtime CONFIG stores the resolved numeric identity.

---

*Related: OLYA-IDENTITY-RESOLUTION-v1 · ADMIN-REGRESSION-v1 · architecture/ADMIN-COMMAND-CONTRACT-v1.md §7.3.*
