> **Production supersession (2026-08-17):** Current reminder contour is PRODUCTION STABLE — enabled Mon–Fri 10:00 Europe/Moscow with weekday gate and current-state pending selector. First natural Monday observation after weekday-gate change may still be pending at freeze. Canonical: [baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md](../baselines/PRODUCTION-STABLE-BASELINE-2026-08-17.md). Historical soak/429 addenda below remain historical.
> **Phase 3H.8.2.2 (2026-08-14):** Reminder pending eligibility uses `iseo-reminder-current-state-selector-v1.0` — unique `lead_id` → authoritative current status → eligibility. First CLEAN pending row no longer wins. Production Reminder Build Claims adds no per-lead Sheets calls. Duplicate CLEAN row source forensic is deferred. Real 10:00 acceptance still pending.

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

<!-- Phase 3H.8 addendum 2026-08-13 -->
## Phase 3H.8 addendum

- Reminder/pending CLEAN source of truth: `lead_clean_v2` (not obsolete `LEADS`).
- Observability contract: `iseo-reminder-observability-v1.1`.
- Soak: **INTERRUPTED — REAL PENDING LEAD MISSED DAILY REMINDER WINDOW**.
- Next live acceptance window: **2026-08-14 10:00 Europe/Moscow** with `REMINDER_PROD_LEAD_A` left pending.
- Phase 3I.1 blocked; AI OFF; do not artificially invoke production reminder.

---
# DAILY PENDING REMINDER CONTRACT v1

- enabled production: true (Phase 3H.3)
- time 10:00 · Europe/Moscow · min pending 1
- source: production **LEADS**
- tests/archive excluded · active recipients only · once per business date
- ledger: REMINDER_DELIVERIES
- message: compact pending count + /pending_leads · no PII
- zero pending → zero sends
- `/reminder_status` must return visible reply (Phase 3H.4 — Admin long-form SyntaxError repaired)
- **Phase 3H.6:** recipient count must match live ACCESS active staff (four under current baseline); CONFIG `pending_reminder_active_recipients_count` is a cache only; `/reminder_status` prefers `$('Read ACCESS_CONTROL')`
- Allowed reminder window: 20 minutes from configured time (10:00 inclusive … 10:20 exclusive Europe/Moscow). Schedule interval 15 minutes → 10:00 and 10:15 may evaluate the same business date if `last_window` is unset.
- Sheets HTTP 429 on ACCESS_CONTROL is retried per `iseo-sheets-429-retry-v1.0`; exhaustion fails closed (`ERROR_SHEETS_429_ACCESS`) and does **not** mark the day sent.

