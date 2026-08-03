# Operator Runbook — i-SEO Sales Manager (v1)

**Audience:** Андрей (operator / Admin)  
**Contour:** production · AI OFF default  
**Version:** 1.7 · 2026-08-04 (Phase 3D.6 — personal status and role notifications)

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

`/my_status` is public but returns the caller’s own status only. Verify it after role changes without exposing raw IDs.

AI ON only with explicit charter.

---

## 5. Tabs

- **ACCESS_CONTROL** — registry
- **ACCESS_EVENTS** — immutable access audit (not lead KPIs)
- **CONFIG** — environment / AI / versions; `admin_user_ids` bootstrap

---

## 6. Button safety

Lead cards with buttons go only to manager/Admin destinations. Public bot reachability ≠ lead visibility. In shared groups, buttons may be visible to members but callbacks still require registry auth.

## 7. Role notification acceptance
1. Use `/moderator_add CODE` or `/moderator_remove CODE`; do not edit workflow code or CONFIG to change a moderator.
2. ACCESS_CONTROL is mutated before the subject notification. If delivery fails, the role state remains changed and the reply is `Права изменены, но уведомление пользователю доставить не удалось.`
3. Check ACCESS_EVENTS for `moderator_grant_notification_sent/failed` or `moderator_revoke_notification_sent/failed`.
4. Ask the subject to confirm the exact Telegram notification and `/my_status`. Automated webhook injection failed with `SQLITE_ERROR`; this real operator loop remains pending for Phase 3D.6.


## Phase 3D.5.1 — Access registry population and SoT repair

- **ACCESS_CONTROL** is the primary authorization authority (Telegram user ID keyed; username informational only).
- `manager_action_user_ids` is legacy and is **not** an active moderator authority after registry acceptance.
- `admin_user_ids` remains recovery-only Admin bootstrap when ACCESS_CONTROL cannot be read technically.
- A revoked/blocked ACCESS_CONTROL row always overrides CONFIG allowlists.
- ACCESS_EVENTS append mapping must reference Prepare Access Upsert fields (never post-Upsert `` metadata).
- Evidence: `evidence/phase3d51/` · Report: `reports/REPORT-iseo-sales-manager-bot-phase3d51-access-registry-repair-v1.md`.

## Phase 3D.5.2 — Operator silence recovery

If Admin commands produce **complete silence**:

1. Check Admin.dev executions for the command timestamp (error vs success).
2. Common causes (fixed in 3D.5.2): disallowed `crypto` in Code nodes; CONFIG→ACCESS fan-out rate limits; missing reply on Sheets errors.
3. Do **not** activate Sales-Manager-v2; do **not** create workflow copies.
4. After repair, prove with real `/start` then `/config` before declaring Admin restored.

Webhook owner for the Sales Manager bot must remain **Admin.dev only**.
