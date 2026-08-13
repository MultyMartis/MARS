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
