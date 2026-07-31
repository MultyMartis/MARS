# Operator Runbook — i-SEO Sales Manager (v1)

**Audience:** Андрей (operator)  
**Contour:** production · AI OFF default  
**Version:** 1.3 · 2026-08-01 (Phase 3D.3.1 — `/leads` multi-card archive repair + phone text safety)

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
| `/status` | Environment, AI flag, last poll / last lead success (`last_lead_success_at`) |
| `/health` | Connectivity / readiness summary |
| `/stats` | Bounded production statistics (exclude SYNTHETIC_TEST) |
| `/last_error` | Last structured error (ignore stale synthetic as active incident) |
| `/config` | Safe CONFIG summary (no secrets) |
| `/ai_status` | AI flag + model/probe flags |
| `/ai_on` | Enable AI — **only with explicit charter** |
| `/ai_off` | Force AI OFF (return to safe mode) |
| `/leads` | Recent CLEAN archive — default 5; exact `3`\|`5`\|`10`; one Telegram card per unique lead (ordinals 1..N); other counts rejected; damaged Sheets phones omitted |

Allowlist remains operator-only unless you explicitly expand it. Do **not** add Оля to Admin without a separate approval.

**Phase 3D.2.1:** readiness notices and Help must list canonical commands only (`/ai_status`, not `/aistatus`). Telegram messages must not show the n8n attribution footer.

**Phase 3D.3 — two separate allowlists:**

| CONFIG key | Gates | Current state |
|------------|-------|----------------|
| `admin_user_ids` | Text commands (`/status`, `/leads`, `/ai_on`, …) | Operator only |
| `manager_action_user_ids` | Inline lead-action callbacks (Отметить обработанным / Отметить как спам) | **Falls back to `admin_user_ids`** — Оля **not enrolled** |

Do not add Оля to `manager_action_user_ids` without a separate approval + controlled enrollment step (Phase 3D.4). Adding her there does **not** grant Admin text-command access — the two lists are independent.

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

## 4a. Callback (inline lead action) troubleshooting

Signals:

- Manager reports a button tap did nothing (no answer toast, no card change);
- `/last_error` shows a callback-stage error code;
- `LEAD_EVENTS` shows unexpected `conflict` or `unauthorized` entries for a lead;
- Same lead flips status repeatedly (should be idempotent, not toggling).

Checks:

1. Confirm the tapping user is on the correct allowlist for what they attempted (`admin_user_ids` for commands, `manager_action_user_ids` for callback actions — see §2 table).
2. Confirm the lead's current `lifecycle_status` in `lead_clean_v2` before assuming a bug — `processed↔spam` after settle is an **expected conflict**, not a defect.
3. Same-status repeat taps are **expected idempotent** no-ops, not failures.
4. Check `LEAD_EVENTS` for the callback's recorded outcome (`applied`/`idempotent`/`conflict`/`unauthorized`) before patching anything.
5. Do not manually edit `lifecycle_status` in Sheets to "fix" a conflict — capture evidence and treat as a workflow investigation first.

### Card edit failure (keyboard not clearing)

If a manager reports the buttons are still visible after tapping one (but the action otherwise worked — e.g. `/leads` later shows correct status):

- This is an **edit-failure** path: the Sheets lifecycle mutation already succeeded and is **not** rolled back; only the Telegram card edit (clearing the keyboard) failed.
- Check the operator-facing `Callback Edit Result` notice / ERRORS for the edit-stage error.
- Do **not** re-run the callback action to "force" the card to update — the lead is already in its new lifecycle state; a second tap on the same button is idempotent, a tap on the other button is a conflict.
- If the card visually needs refreshing, use `/leads` to pull a fresh archive view of that lead's current state instead of re-tapping.

## 4b. Lifecycle fields warning (Sheets)

`lead_clean_v2` carries manager lifecycle/callback state directly on the row (`lifecycle_status`, `manager_action_token`, `manager_action_user_id`, `manager_action_processed_at`, `manager_action_spam_at`, `telegram_chat_id`, `telegram_message_id`, …) — see SHEETS-MIGRATION-SPEC-v1 §3.1.

- **Do not hand-edit these columns in Sheets.** `manager_action_token` is the callback routing key; changing it can break a lead's inline buttons or point them at the wrong row.
- **Do not delete or blank `lifecycle_status`** — it must always be one of `pending`/`processed`/`spam`; an empty value is undefined behavior for the callback state machine.
- Existing `processed_at` (bot processing time) and `manager_action_processed_at` (manager lifecycle time) are **different fields** — do not conflate them when reading Sheets directly.
- Any correction to lifecycle state should go through a documented, evidenced action (Admin command/callback or an explicitly chartered manual fix), not an ad hoc cell edit.

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
