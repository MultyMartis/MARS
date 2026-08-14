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
# REMINDER EXACTLY-ONCE v1

Implementation notes for Admin.dev reminder path: window key + REMINDER_DELIVERIES per-recipient claims + CONFIG window stamps.
Source sheet must be LEADS.

## Phase 3H.4 note

`/reminder_status` Admin long-form builder repaired (SyntaxError). Active recipients count backfilled to 3. See `implementation/REMINDER-STATUS-COMMAND-REPAIR-v1.md`.

## Phase 3H.6

Active recipients count aligned to **4**. `/reminder_status` uses live ACCESS preference. Isolated four-recipient exactly-once proof PASS.
