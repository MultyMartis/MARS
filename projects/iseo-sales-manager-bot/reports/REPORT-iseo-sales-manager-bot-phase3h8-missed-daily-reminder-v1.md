# REPORT — ISEO Sales Manager Bot Phase 3H.8 Missed Daily Reminder

**Verdict:** `PHASE 3H.8 TECHNICAL REPAIR COMPLETE — REAL 10:00 REMINDER ACCEPTANCE PENDING`

## 1. Verdict
Technical root cause repaired; isolated harness passed; `REMINDER_PROD_LEAD_A` prepared pending for **2026-08-14 10:00 Europe/Moscow**. Final live reminder acceptance **not** declared.

## 2. Operator evidence
Genuine pending lead missed daily reminder; later manually marked Spam; second genuine spam lead also present. Aliases only in Git.

## 3. Failed real reminder
Window 2026-08-13 10:00 Europe/Moscow — no operator reminder received.

## 4. Failed-window timeline
See `evidence/phase3h8/FAILED-REMINDER-WINDOW-TIMELINE-v1.md` (exec 29969).

## 5. Pending state at 10:00
Evaluator saw pending=0 from obsolete `LEADS`; authoritative `lead_clean_v2` held the live lead.

## 6. Schedule execution
`REMINDER_TRIGGER_EXECUTED` — trigger ran at 10:00:21 MSK.

## 7. Timezone
Europe/Moscow correct in gate (`local_date=2026-08-13`, window key correct).

## 8. Reminder pipeline trace
See `REMINDER-END-TO-END-TRACE-v1.md` — failure at pending selector / count.

## 9. Pending selector
Wrong sheet (`LEADS` vs `lead_clean_v2`).

## 10. Minimum threshold
min=1; not the primary defect (count already 0).

## 11. Business-date guard
Did not false-suppress (last_window not stamped on zero_pending).

## 12. Claims
0 claims / 0 deliveries at failed window.

## 13. Test-claim isolation
No production suppression by test claims proven for failed date.

## 14. Recipient resolution
4 active recipients available at window; unused due to zero_pending.

## 15. Telegram delivery
No send attempted.

## 16. Observability
Upgraded to `iseo-reminder-observability-v1.1`.

## 17. Exact root cause
`live_pending_selector_queried_obsolete_LEADS_tab_instead_of_authoritative_lead_clean_v2`

## 18. Repair
Admin CLEAN retarget + observability; Operational unchanged.

## 19. Exactly-once harness
PASS (TEST-labelled 4/4; pass2=0; test window safe). Prior live dry selector pending≥1; ACCESS=4.

## 20. Post-repair backup
Private backups + sanitized manifest committed.

## 21. Real acceptance lead
`REMINDER_PROD_LEAD_A` chosen.

## 22. Reopen result
spam→pending; same ID; spam history preserved; event `manager_reopened`; no resurface.

## 23. Current pending count
`pending_count_estimate` after reopen ≥ 1 (live estimate ~39 including historical pending; acceptance lead included).

## 24. Next 10:00 readiness
Ready for **2026-08-14 10:00 Europe/Moscow** — no artificial invoke.

## 25. Operator action before window
Leave acceptance lead pending; do not Spam/Processed before check.

## 26. System health
Ops active; Admin active; v2 inactive; Gmail path not modified this phase.

## 27. Production invariants
reminders ON 10:00 MSK; recipients=4; reporting manual; AI OFF; workflows created=0.

## 28. Git
Clean worktree from `origin/mars/canonical-post-recovery`; scoped commits under `projects/iseo-sales-manager-bot/**` only.

| Commit | Message |
|---|---|
| `5c874279` | `fix(iseo-sales-manager-bot): repair missed daily reminder evaluation` |
| `983e56f2` | `fix(iseo-sales-manager-bot): expose reminder decision observability` |
| `d8b6fe1c` | `test(iseo-sales-manager-bot): prove reminder exactly-once isolation` |
| `62b6722c` | `docs(iseo-sales-manager-bot): prepare real reminder acceptance window` |

## 29. Soak status
`INTERRUPTED — REAL PENDING LEAD MISSED DAILY REMINDER WINDOW` — not restarted.

## 30. Phase 3I.1 gate
**Blocked.**

## 31. Stop condition
Stop after repair + harness + reopen + next-window readiness without claiming live 10:00 PASS.

## Counters
| Counter | Value |
|---|---|
| failed real reminder windows | 1 (2026-08-13) |
| pending leads at failed window (evaluator view) | 0 |
| pending leads at failed window (authoritative) | ≥1 |
| schedule executions at expected window | ≥1 (29969) |
| evaluator errors | 0 |
| stale pending-count reads | 1 (wrong sheet) |
| false same-day suppressions | 0 |
| test claims contaminating production | 0 |
| eligible reminder recipients | 4 |
| reminder claims (failed window) | 0 |
| Telegram reminder attempts (failed window) | 0 |
| Telegram reminder successes (failed window) | 0 |
| isolated test sends | 4 |
| duplicate reminder sends (harness pass2) | 0 |
| genuine lead reopened for next-window test | 1 |
| current production pending count | ≥1 |
| AI state | OFF |
| OpenRouter calls | 0 |
| customer auto-send | 0 |
| workflows created | 0 |
| final soak restarted | 0 |
| Phase 3I.1 started | 0 |
