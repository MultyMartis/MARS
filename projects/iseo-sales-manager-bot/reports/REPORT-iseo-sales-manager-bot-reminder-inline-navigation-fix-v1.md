# REPORT — ISEO Sales Manager Bot — Reminder Inline Navigation Fix v1

Date: 2026-08-25  
Process-line: PRODUCTION REMINDER INLINE GROUP NAVIGATION FORENSIC AND REPAIR  
Workflow: `wLrLp4WQHm1VJmxz` (Admin.dev)

## 1. Verdict

**REMINDER INLINE NAVIGATION LIVE PASS — MAIN DIGEST → GROUP → EXACT LEAD**

Natural digest previously arrived as plain text because n8n dropped whole-object `inlineKeyboard` expressions. Field-expression keyboards are deployed; ADMIN_A acceptance messages show live `reply_markup` for digest → group → exact lead.

## 2. Operator-visible defect

Natural morning reminder to ADMIN_A had correct pending text/categories/age but **no clickable inline buttons**.

## 3. Latest natural reminder

| Field | Value |
|---|---|
| Execution | **40019** |
| Window | `pending-reminder:2026-08-25:10:00:Europe/Moscow` |
| Pending | 19 |
| Renderer keyboard | present (`telegram_has_buttons: true`, 5 `sm:g:` buttons) |
| Telegram result markup | **absent** (pre-fix) |

## 4. Renderer output

Digest renderer `iseo-pending-digest-renderer-v1.1` produced `telegram_inline_keyboard_ui` with packed group/filter buttons. Post-fix also emits `rm_bN_text` / `rm_bN_cb` flatten fields.

## 5. Telegram send payload

Pre-fix: `inlineKeyboard: ={{$json.telegram_inline_keyboard_ui}}` → silent omit of `reply_markup`.  
Post-fix: static packed/vertical fixedCollection with per-field expressions.

## 6. Exact root cause

n8n Telegram node silently drops whole-object expression keyboards; field-expression static keyboards work. First divergence: renderer/merge had UI → Telegram API result had none.

## 7. Repair

1. Flatten helper in Reminder Build Claims + Prepare Callback Answer  
2. Send Reminder Telegram → field-expression packed keyboard  
3. Safe Telegram replies with buttons → Switch bands KB4/8/12/14  
4. No schedule / claims / last_window / ACCESS / recipient changes

## 8. Main digest buttons

`sm:g:` category/meta filters only (count > 0). Compact 1–2 per row. Acceptance digest message_id **1090** with `reply_markup`.

## 9. Group navigation

Production `group_open` recomputes current pending; sends compact list + `sm:q:` buttons via Prepare + KB bands. Acceptance group message_id **1091** with markup.

## 10. Exact lead navigation

`sm:q:` opens compact lead via existing renderer. Acceptance lead message_id **1092**. Wrong lead resolutions: **0**.

## 11. Current-state behavior

Group click uses live CLEAN pending membership (counts may differ from morning snapshot). Expected.

## 12. Full-card callback safety

Full card included only with non-empty callback. `empty_callback_buttons: 0`.

## 13. Current ACCESS

Unchanged. Test routed to ADMIN_A only (hash12 `3FBE21323E22`). Olya / Nikita / Michael not restored.

## 14. Reminder delivery/dedupe invariant

Natural window 40019: one reminder for logical window, no recovery duplicate observed → `DELIVERY/DEDUPE LIVE STABLE` for text delivery. Separate from navigation defect.

## 15. Test routing

ADMIN_A = 3 · MOD_A/B/C = 0 · customers = 0 · claims by test = 0 · status mutations = 0

## 16. Backup

PRE sha16 `E692EA72EBD213B4` → POST sha16 `6CFE53A51F840A9E` (private STORAGE manifests). See PRE/POST backup evidence files.

## 17. Git

Worktree: `worktrees/iseo-smb-reminder-inline-nav-01`  
Branch: `iseo-smb/reminder-inline-nav-01`  
Base: `origin/mars/canonical-post-recovery` @ `e87a7356`  
Scope: `projects/iseo-sales-manager-bot/**`

## 18. Remaining stabilization work

- Operator visual click of buttons on ADMIN_A Telegram (messages 1090–1092) confirms UX in the client UI.  
- Next natural 10:00 window should attach markup via production Send Reminder path (same field-expression pattern proven in acceptance).  
- Optional polish: reduce pad slots on fixed-size keyboards (cosmetic only).

## Counters

| Counter | Value |
|---|---|
| natural reminders inspected | 1 |
| renderer group buttons generated (natural) | 5 |
| Telegram group buttons sent (acceptance digest) | 8 (incl. pads) |
| group click tests | 1 |
| exact lead click tests | 1 |
| wrong lead resolutions | 0 |
| empty callback buttons | 0 |
| production reminder claims created by test | 0 |
| real lead status mutations by test | 0 |
| moderator test messages | 0 |
| customer test messages | 0 |
| workflows modified | 1 (Admin.dev) |
| AI calls | 0 |
