# REPORT — ISEO Sales Manager Bot — Keyboard duplicate «Все» fix

**Document:** `REPORT-iseo-sales-manager-bot-keyboard-duplicate-all-fix-v1.md`  
**Date:** 2026-08-27  
**Process-line:** Reminder inline keyboard duplicate-All regression forensic/fix + MOD_B live lead-state preservation

---

## 1. Verdict

`DUPLICATE ALL FIXED — KEYBOARD UX PASS — OLYA LIVE STATE PRESERVED`

---

## 2. Operator-visible regression

Natural morning reminder showed multiple `📋 Все` buttons after the field-expression keyboard repair. Execution `41719` Telegram markup contained one legitimate All plus **three** padded All slots (rows with bare `📋 Все` / `sm:g:all`).

---

## 3. Exact root cause

**Class:** `UNUSED_SLOT_DEFAULTS_TO_ALL`

`flattenInlineKeyboardUi(..., 8, '📋 Все', 'sm:g:all')` filled missing fixed slots with All text/callback. With 5 real buttons, slots 6–8 became duplicate All. Same helper padded callback-reply bands.

Evidence: `evidence/.../ROOT-CAUSE-v1.md`, `NATURAL-DUPLICATE-ALL-EVIDENCE-v1.md`.

---

## 4. Keyboard slot architecture

Pre-fix: single fixed-8 field-expression Telegram node.  
Post-fix: flatten emits empty unused slots; Switch routes to exact `KB{n}`; archived fixed-8 disabled.

---

## 5. Repair

Admin.dev only (`wLrLp4WQHm1VJmxz`), stamp `2026-08-27T14-56-02-910Z`:

1. Empty unused flatten slots (All pad only if zero real buttons).
2. Exact `rm_kb_band` / Switch Reminder Keyboard Size → KB1…KB8.
3. Reply path exact KB1…KB14.

Operational.dev **not** modified. Field-expression binding retained.

---

## 6. Post-fix keyboard

ADMIN_A acceptance message_id `1142`:

- Audit · 12, Other · 4, Older · 15, All · 16  
- SEO omitted (count 0)  
- **All actual = 1**, duplicate All = 0, empty cb = 0

---

## 7. Group selector regression check

Group-filter code unchanged. Offline set sizes at acceptance: Audit 12 / SEO 0 / Other 4 / older24 15 / All 16. Unique callbacks = 4. `group_set_mismatches = 0`.

Interactive Telegram clicks after acceptance were not executed this wave (see acceptance evidence).

---

## 8. Live ACCESS

`MOD_B_ACCESS_BEFORE = ACTIVE`  
`MOD_B_ACCESS_AFTER = ACTIVE`  
ACCESS sheet not written by repair.

---

## 9. MOD_B/Olya current state

Olya / MOD_B remains **ACTIVE**. Other moderators remain revoked/pending as live ACCESS already stated. No ACCESS overwrite from stale CONFIG.

---

## 10. Olya today's processed-lead integrity

Identified **7** MOD_B-attributed real lead status updates today (sanitized hashes in evidence). Repair mutated **0** of them; status regressions **0**; duplicate repair events **0**; lost **0**.

---

## 11. ADMIN_A test

One ADMIN_A-only keyboard message via production Switch+KB path. No claim / no `last_window` / no pending pollution / no other-moderator or customer traffic.

---

## 12. Natural Send Reminder path

Live graph: Merge → Switch Reminder Keyboard Size → KB{n} → Reminder Stamp. Archived fixed-8 disabled. Next natural reminder uses the patched path.

---

## 13. Reminder invariants

Schedule, 10:00/10:15, window key, claims, `last_window`, delivery ledger, recipient logic: **not modified**.

| Counter | Value |
|---------|------:|
| reminder claims created by test | 0 |
| last_window mutations by test | 0 |

---

## 14. CLEAN/DEDUP invariants

Operational.dev `updatedAt` unchanged. CLEAN `appendOrUpdate`/`lead_id` and DEDUP `appendOrUpdate`/`dedup_key` markers still present.

---

## 15. Soak reset

```
SOAK RESET REQUIRED — DUPLICATE ALL KEYBOARD REGRESSION PATCH
READY FOR NEW 48H SOAK T+0
```

Prior soak from `a6b3dceb` is invalid after this production patch. New soak **not** auto-started.

---

## 16. Backup

Private PRE/POST Admin.dev JSON under STORAGE worktree `private/backups/` (sanitized manifests in evidence; secrets not in Git).

---

## 17. Git

Clean worktree → selective commits under `projects/iseo-sales-manager-bot/**` → push `origin/mars/canonical-post-recovery` (no force). Foreign WIP on dirty main preserved.

---

## 18. Next gate

Operator authorization to start **new** 48h soak T+0. Optional: ADMIN_A spot-click groups on message 1142 for visual callback confirmation.

---

## Counters summary

| Counter | Value |
|---------|------:|
| expected logical main buttons (acceptance) | 4 |
| actual main buttons | 4 |
| All logical buttons expected | 1 |
| All buttons actual | 1 |
| duplicate All buttons | 0 |
| empty callback buttons | 0 |
| group set mismatches | 0 |
| wrong group resolutions (live click) | n/a (not clicked) |
| wrong lead resolutions (live click) | n/a (not clicked) |
| generic `Группа` replies | 0 |
| verify errors | 0 |
| MOD_B active before | 1 |
| MOD_B active after | 1 |
| Olya real leads processed today identified | 7 |
| Olya real leads mutated by repair | 0 |
| Olya status regressions | 0 |
| duplicate Olya action events caused by repair | 0 |
| Olya processed leads lost | 0 |
| reminder claims created by test | 0 |
| last_window mutations by test | 0 |
| moderator test messages (non-ADMIN_A) | 0 |
| customer test messages | 0 |
| Operational.dev modifications | 0 |
| Admin.dev modifications | 1 |
| AI calls | 0 |
