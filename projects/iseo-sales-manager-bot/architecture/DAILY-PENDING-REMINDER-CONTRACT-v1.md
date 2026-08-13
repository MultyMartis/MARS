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
- Evidence: `evidence/phase3h4/REMINDER-CONFIG-INVARIANTS-v1.md` · `evidence/phase3h6-four-recipient/`
