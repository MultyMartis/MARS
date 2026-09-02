# i-SEO Sales Manager — Data Mapping v0

**Document:** `ISEO-SALES-DATA-MAPPING-v0`  
**Status:** Placeholder inventory — **NOT** final schema  
**Date:** 2026-09-03  
**Source packs:** `projects/iseo-sales-manager-bot/` (Sheets + n8n product)

Do **not** create one PostgreSQL table per Sheet.

---

## 1. Classification legend

| Class | Meaning |
|-------|---------|
| `BUSINESS ENTITY` | Durable business object |
| `RUNTIME STATE` | Queues, leases, flags, processing state |
| `EVENT` | Domain transition |
| `AUDIT` | Operator/admin action trail |
| `PROJECTION` | Derived view for humans (Sheets/UI) |
| `LEGACY SHEETS CONCEPT` | Spreadsheet artifact that should merge/disappear |

---

## 2. Concept inventory

| Current concept | Likely class | PostgreSQL direction (v0) |
|-----------------|--------------|---------------------------|
| **RAW** | `BUSINESS ENTITY` + payload | Durable intake record / message source table; keep full source; not a forever “sheet tab” |
| **CLEAN** | `BUSINESS ENTITY` | Normalized lead (or lead_revision) entity |
| **DEDUP_INDEX** | `RUNTIME STATE` / constraint | Unique indexes + `idempotency_keys` / natural keys — **not** a separate Sheet-like table forever |
| **LEAD_EVENTS** | `EVENT` | `events` (typed domain events) |
| **LEAD_DELIVERIES** | `RUNTIME STATE` + outbox | `deliveries` / outbox rows with provider results |
| **ACCESS** | `BUSINESS ENTITY` or config | Access control list / allowlist — typed table or config; clarify vs Telegram rights |
| **CONFIG** | `RUNTIME STATE` / config | Small typed config in `app_iseo_sales` — avoid dumping entire Sheets Config blindly |
| **ERRORS** | `EVENT` / error store | `errors` table with retryability |
| **reminders** | `RUNTIME STATE` + jobs | `jobs` (or `reminders` specializing jobs) with `available_at` |
| **retry / defer** | `RUNTIME STATE` | Job status machine (`retry`, `available_at`, attempts) |
| **moderator actions** | `AUDIT` (+ maybe `EVENT`) | `audit_logs` + domain events when state changes |

---

## 3. Merge / disappear candidates

| Sheets-era idea | Disposition |
|-----------------|-------------|
| DEDUP as manual tab | Replace with constraints + idempotency |
| Parallel “log everything in one Errors sheet” | Split errors vs events vs audit |
| CLEAN as only mutable row without history | Consider explicit revisions or event-sourced transitions if needed |
| Delivery success only in chat memory | Durable outbox mandatory |

---

## 4. Non-goals for v0

- Final DDL;
- production migration;
- forcing UUID everywhere;
- preserving every Sheets column name.

---

## 5. Next mapping gate

Produce `ISEO-SALES-DATA-MAPPING-v1` with proposed tables, keys, and uniqueness rules after Architecture V1 acceptance.
