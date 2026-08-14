<!-- Phase 3H.8.2 addendum 2026-08-14 -->
## Phase 3H.8.2 addendum

- Contract: `iseo-sheets-429-retry-v1.0` on reminder-critical Sheets reads (Admin.dev only).
- ACCESS_CONTROL 429: explicit Wait 5s/15s/30s loop (max 4 attempts); fail closed `ERROR_SHEETS_429_ACCESS`; no stale ACCESS send fallback.
- `/reminder_status` exposes ERROR + stage + quota reason + retry count.
- Soak remains: **INTERRUPTED — REAL REMINDER WINDOW FAILED ON SHEETS 429** (not restarted).
- Next live acceptance: **2026-08-15 10:00 Europe/Moscow** with `REMINDER_ACCEPTANCE_LEAD_2` left pending.
- Do not claim REMINDER LIVE PASS until that scheduled window succeeds.
- Phase 3I.1 blocked; AI OFF; Admin **92** nodes; Ops **45**; v2 inactive.
- Evidence: [evidence/phase3h82/](evidence/phase3h82/) · Report: [reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md](reports/REPORT-iseo-sales-manager-bot-phase3h82-reminder-sheets429-resilience-v1.md)

# MISSED DAILY REMINDER REPAIR v1

**Phase:** 3H.8

## Defect
Reminder evaluator read obsolete `LEADS` sheet → false `zero_pending` while genuine pending leads existed in `lead_clean_v2`.

## Repair
Retarget Admin CLEAN reads to `lead_clean_v2`; add observability v1.1; preserve exactly-once (no last_window stamp on zero pending).

## Verification
- Failed-window forensic (exec 29969)
- Isolated TEST harness (4/4 deliveries; pass2=0)
- Operator-approved reopen of `REMINDER_PROD_LEAD_A` for next natural 10:00 window
