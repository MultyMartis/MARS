# REPORT — ISEO-SALES-MANAGER-BOT PHASE 3H.10 REMINDER DELIVERY AND ACTIONABLE DIGEST

**Process-line:** ISEO-SALES-MANAGER-BOT — PHASE 3H.10 REMINDER DELIVERY REPAIR AND ACTIONABLE QUEUE DIGEST UX  
**Captured:** 2026-08-20  
**Workflows:** Admin.dev `wLrLp4WQHm1VJmxz` (102 nodes) · Operational.dev `xSnXPy8cEHoZw6xG` (45, unchanged)

## 1. Verdict

`PHASE 3H.10 TECHNICAL COMPLETE — REMINDER DELIVERY REPAIRED; ACTIONABLE DIGEST DEPLOYED; NATURAL 10:00 ACCEPTANCE PENDING`

Also satisfies: `COMPLETE — ADMIN_A DIGEST UX PASS; NATURAL PRODUCTION DELIVERY PENDING`

## 2. Operator-approved reminder UX

One actionable pending-queue digest per recipient: grouped human categories, oldest-first leads, inline `sm:q:` actions → compact lead view. Full card / raw / status reuse existing contracts. No full cards inside the reminder body.

## 3. Current active recipient baseline

Live ACCESS: **ADMIN_A, MOD_B, MOD_C** → **3**. CONFIG cache reconciled **4 → 3**.

## 4. MOD_A intentional disable

MOD_A status **revoked**. Not restored. Not classified as unauthorized drift.

## 5. Recent natural reminder windows

Inspected Aug 18–20: 10:00/10:15 error at Wait; 10:30 success `SKIPPED_OUTSIDE_WINDOW`. See `evidence/phase3h10/RECENT-REMINDER-WINDOWS-v1.md`.

## 6. Latest SHOULD_SEND window

No completed SHOULD_SEND→Telegram path in inspected windows. Latest in-window attempts **35821** (10:00) and **35830** (10:15) classed **ERROR_BEFORE_DECISION** (pending `not_computed`).

## 7. Exact reminder failure root cause

**Primary:** `WAIT_RETRY_DATETIME_INVALID`  
**Secondary:** `SHEETS_429` (ACCESS) · `TELEGRAM_SEND_PATH_NOT_REACHED` · `CONFIG_RECIPIENT_CACHE_DRIFT`

## 8. Delivery repair

Prepare Wait → `wait_until_iso`; Wait → `specificTime`. Soft ACCESS retryOnFail. Deployed Admin.dev PUT 200.

## 9. Recipient resolution

Live ACCESS authority. Active = 3. Stale CONFIG cannot restore MOD_A.

## 10. Claims

Natural failing windows: claims **0** (path not reached).

## 11. Telegram delivery path

Natural: attempts **0**. ADMIN_A-only UX test: **1** success (test mode, no production claim).

## 12. Window completion/recovery

Failing windows did not mark day as successfully sent. Recovery 10:15 hit same Wait defect pre-repair.

## 13. New digest renderer

`iseo-pending-digest-renderer-v1.0` inlined in Reminder Build Claims. Harness PASS.

## 14. Category mapping

Deterministic presentation map → Аудит / SEO / Реклама / Разработка сайта / Другое / Требует уточнения.

## 15. Sorting/age semantics

Oldest-first; сегодня / N день|дня|дней; ⚠️ 3–4d; 🔴 5+d.

## 16. Digest counters

From authoritative unique pending set (total / today / older_than_24h / oldest).

## 17. Actionable lead entries

Inline buttons `sm:q:<opaque>` cap 25 + overflow `📋 Все необработанные`.

## 18. Compact lead view

`iseo-pending-digest-action-v1.0` compact structure implemented.

## 19. Full-card action

`sm:f:` → canonical full-card renderer reuse.

## 20. Raw action

Reuses repaired raw-access contract (infra ≠ permission deny).

## 21. Status actions

Processed / Spam reuse existing lifecycle (no second engine).

## 22. Stale digest behavior

Click resolves current state (harness spam compact PASS).

## 23. Overflow behavior

Button cap 25; body budget ~3500; overflow CTA to pending list.

## 24. ADMIN_A-only live test

PASS — one digest message, buttons present, tmp WF deleted.

## 25. Test recipient counters

ADMIN_A=1 · MOD_A=0 · MOD_B=0 · MOD_C=0 · customer=0 · production claim pollution=0 · status mutations=0

## 26. /reminder_status

Updated for delivery/recipients/error stage clarity. Natural line proof at next 10:00.

## 27. Current genuine pending count

Read-only probe at ADMIN_A digest test: **51** (not window-retroactive). Re-check at natural window.

## 28. Next natural 10:00 readiness

**2026-08-21 10:00 Europe/Moscow**. Manual production trigger forbidden.

## 29. System invariants

Gmail intake preserved · Sheets auth healthy on recent reads · AI **OFF** · workflows created **0** · PostgreSQL migration **0** · MOD_A not restored

## 30. Backup

Pre-change + post-change private backups under STORAGE incoming; sanitized manifests in `evidence/phase3h10/`.

## 31. Git

Clean worktree `agent/iseo-sm-phase3h10-reminder-digest` · scope `projects/iseo-sales-manager-bot/**` only.

## 32. Soak state

`SOAK INTERRUPTED / LIVE REMINDER ACCEPTANCE PENDING` — restart only after natural production digest PASS.

## 33. Phase 3I.1 gate

**BLOCKED**

## 34. Stop condition

Delivery root cause proven and repaired · digest UX deployed · ADMIN_A test PASS · moderators/customers untested · natural window not manually triggered · AI OFF · Phase 3I.1 blocked · MOD_A remains disabled.

---

## Counters

| Metric | Value |
|--------|-------|
| natural reminder windows inspected | 5+ (18–20 Aug slots) |
| SHOULD_SEND windows completed | 0 |
| ERROR_BEFORE_DECISION | 4 (10:00/10:15) |
| trigger executions | TRIGGER_RAN on listed slots |
| credential failures (these windows) | 0 invalid_grant |
| 429 events | yes (ACCESS) |
| current active reminder recipients | 3 |
| intentionally disabled recipients | 1 (MOD_A) |
| authoritative pending (probe) | 51 |
| claims expected (failing windows) | n/a (not reached) |
| claims created (failing windows) | 0 |
| Telegram attempts (natural) | 0 |
| Telegram successes (natural) | 0 |
| ADMIN_A test messages | 1 |
| MOD_* / customer test messages | 0 |
| production claims by tests | 0 |
| workflows created (permanent) | 0 |
| AI state | OFF |
| soak restarted | no |
| Phase 3I.1 started | no |

## Evidence

[evidence/phase3h10/](../evidence/phase3h10/)
