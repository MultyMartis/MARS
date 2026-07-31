# Operator Runbook — i-SEO Sales Manager (v1)

**Audience:** Андрей (operator)  
**Contour:** production · AI OFF default  
**Version:** 1.1 · 2026-08-01

---

## 1. Safe mode baseline

| Item | Expected |
|------|----------|
| Sales-Manager-v2 | **inactive** (rollback source only) |
| Operational.dev | **active** (sole Gmail intake) |
| Admin.dev | **active** |
| `environment` | `production` |
| `ai_enabled` | `false` |
| `parser_version` (display) | `sm-parser-v3.1` |
| Automatic client replies | **never** |
| New workflows | **do not create** for hotfixes |

AI OFF is the normal safe production mode.

**Never activate Sales-Manager-v2 while Operational is active.**

---

## 2. Admin commands

| Command | Use |
|---------|-----|
| `/start` | Open Admin panel (contour + AI mode summary) |
| `/help` | Command list |
| `/status` | Environment, AI flag, last poll / last lead success |
| `/health` | Connectivity / readiness summary |
| `/stats` | Bounded production statistics (exclude SYNTHETIC_TEST) |
| `/last_error` | Last structured error (ignore stale synthetic as active incident) |
| `/config` | Safe CONFIG summary (no secrets) |
| `/ai_status` | AI flag + model/probe flags |
| `/ai_on` | Enable AI — **only with explicit charter** |
| `/ai_off` | Force AI OFF (return to safe mode) |

Allowlist remains operator-only unless you explicitly expand it. Do **not** add Оля to Admin without a separate approval.

---

## 3. How to identify intake failure

Signals:

- `/status` or `/health` shows stale/failed poll;
- Gmail eligible messages accumulate with incoming label and no Telegram card;
- Operational executions error before Telegram;
- Sales-Manager-v2 accidentally active (dual intake risk).

Actions:

1. Confirm only Operational.dev is active for Gmail.
2. Capture `/status` `/health` `/last_error` screenshots/text.
3. Do not broad-relabel Gmail.
4. Do not flood test leads.

---

## 4. How to identify Telegram delivery failure

Signals:

- Lead processed in Sheets but no manager card;
- `/last_error` shows `telegram_delivery_failed` or `telegram_retry_exhausted`;
- Incoming label still present after repeated polls;
- delivery attempt counters climbing for same message.

Actions:

1. Check manager destination in CONFIG (do not paste IDs into chat logs).
2. Confirm Admin/Operational Telegram credential still bound.
3. Prefer resume/finalize path over resending cards.
4. Capture evidence before patching.

---

## 5. When to use rollback

Use Sales-Manager-v2 reactivation **only** if Operational.dev cannot safely intake and you need temporary continuity.

Rollback rules:

1. Deactivate Operational.dev first (or ensure no dual-active Gmail intake).
2. Activate Sales-Manager-v2 only after dual-active check.
3. Keep Admin.dev unless it is part of the failure.
4. Record timestamps and `/last_error`.
5. Do not enable AI during emergency rollback unless separately approved.

See `plans/ROLLBACK-PLAN-v1.md`.

---

## 6. Avoid dual-active workflows

**Never activate Sales-Manager-v2 while Operational is active.**

Never leave both Sales-Manager-v2 and Operational.dev **active** with Gmail intake.

Checklist before any activation change:

- [ ] Who is the sole intake?
- [ ] What is inactive rollback source?
- [ ] Admin still reachable?
- [ ] Evidence captured?

---

## 7. Evidence to capture before changes

1. Workflow active states (v2 / Operational / Admin).  
2. `/status` `/health` `/stats` `/last_error` `/ai_status`.  
3. Time window of incident.  
4. Whether Telegram card already delivered.  
5. Whether Gmail was finalized (PROCESSED / incoming removed).  
6. Backup/export note path under Storage (sanitized before git).

---

## 8. Olya handoff boundary

- Оля receives manager cards and uses the prepared reply manually.
- Оля updates lifecycle in Sheets.
- Оля does **not** need n8n, Gmail, credentials, or Admin allowlist.
- Operator remains on-call for failures.

Guide: `guides/OLYA-LEAD-WORK-GUIDE-v1.md`.

---

## 9. Retry / flood notes (post–Phase 3D)

- Telegram delivery is idempotent per Gmail message after successful send.
- Same message must not produce unlimited cards.
- After delivery success, Gmail finalization may resume without re-sending.
- Retry attempts are bounded; exhaustion goes to error path.

---

*No credentials, chat IDs, Gmail IDs, or workbook IDs in this runbook.*
