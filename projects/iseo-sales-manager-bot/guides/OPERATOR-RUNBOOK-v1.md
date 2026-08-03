# Operator Runbook — i-SEO Sales Manager (v1)

**Audience:** Андрей (operator / Admin)  
**Contour:** production · AI OFF default  
**Version:** 1.5 · 2026-08-03 (Phase 3D.5 — public access + ACCESS_CONTROL moderator registry)

---

## 1. Safe mode baseline

| Item | Expected |
|------|----------|
| Sales-Manager-v2 | **inactive** |
| Operational.dev | **active** (sole Gmail intake) |
| Admin.dev | **active** |
| `environment` | `production` |
| `ai_enabled` | `false` |
| `parser_version` | `sm-parser-v3.2` |
| `message_format_version` | `sm-msg-v2.2` |
| Access SoT | **ACCESS_CONTROL** |
| Automatic client replies | **never** |
| New workflows | **do not create** |

**Never activate Sales-Manager-v2 while Operational is active.**  
**Never edit workflow code to add a moderator.**

---

## 2. Public vs staff

- Anyone may `/start` / `/help` (public texts).
- Public users do **not** see leads, callbacks, stats, health, AI, or staff lists.
- Working rights are granted individually.

---

## 3. Moderator registry (Admin)

| Command | Use |
|---------|-----|
| `/moderators` | Active moderators (no raw Telegram IDs; opaque codes) |
| `/moderator_pending` | Latest pending public requests |
| `/moderator_info CODE` | Safe profile (role/status/timestamps) |
| `/moderator_add CODE` | Approve pending → moderator active |
| `/moderator_remove CODE` | Revoke moderator (row kept; callbacks denied immediately) |

**Authority key = Telegram user ID** (stored in Sheets as text). Username is informational and may change.

Olya (@Ola4seo) remains **moderator-only**. Do not promote her to Admin without a separate charter.

Legacy CONFIG `manager_action_user_ids` is fallback only when no ACCESS_CONTROL row exists. Prefer registry.

---

## 4. Other Admin commands

`/start` `/help` `/status` `/health` `/stats` `/last_error` `/config` `/ai_status` `/ai_on` `/ai_off` `/leads`

AI ON only with explicit charter.

---

## 5. Tabs

- **ACCESS_CONTROL** — registry
- **ACCESS_EVENTS** — immutable access audit (not lead KPIs)
- **CONFIG** — environment / AI / versions; `admin_user_ids` bootstrap

---

## 6. Button safety

Lead cards with buttons go only to manager/Admin destinations. Public bot reachability ≠ lead visibility. In shared groups, buttons may be visible to members but callbacks still require registry auth.
