# DAILY PENDING REMINDER CONTRACT v1

- enabled production: true (Phase 3H.3)
- time 10:00 · Europe/Moscow · min pending 1
- source: production **LEADS**
- tests/archive excluded · active recipients only · once per business date
- ledger: REMINDER_DELIVERIES
- message: compact pending count + /pending_leads · no PII
- zero pending → zero sends
- `/reminder_status` must return visible reply (Phase 3H.4 — Admin long-form SyntaxError repaired)
- Evidence: `evidence/phase3h4/REMINDER-CONFIG-INVARIANTS-v1.md`
