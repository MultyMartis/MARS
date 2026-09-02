# i-SEO Sales — Sheets → PostgreSQL Mapping v1

**Document:** `ISEO-SALES-DATA-MAPPING-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03  
**Supersedes:** `ISEO-SALES-DATA-MAPPING-v0` (placeholder)  
**Model:** `ISEO-SALES-DATA-MODEL-v1`  
**Status:** Mapping for future import — **no live data migration in this wave**

---

## Classification legend

| Class | Meaning |
|-------|---------|
| `MIGRATE` | Import durable rows into target table |
| `TRANSFORM` | Reshape / normalize during import |
| `MERGE` | Fold into constraints or another entity |
| `DROP AS LEGACY` | Spreadsheet artifact; do not keep as table |
| `PROJECTION ONLY` | May remain as Sheets/UI view after cutover |

---

## Matrix

| Current Sheet/tab/concept | Current role | Target table/field | Migration transform | Remains after cutover? |
|---------------------------|--------------|--------------------|---------------------|------------------------|
| RAW `lead_raw_v2` | Intake evidence | `inbound_events` | `MIGRATE`+`TRANSFORM`: `gmail_message_id`→`source_id`; body→`raw_text`/`raw_payload` | `PROJECTION ONLY` optional |
| RAW row number | Sheet identity | — | `DROP AS LEGACY` | No |
| RAW `lead_id` | Early business id | `inbound_events.lead_id` + `leads.lead_id` | `TRANSFORM` | Via leads |
| RAW `gmail_thread_id` | Thread | `inbound_events.gmail_thread_id` | `MIGRATE` | Projection optional |
| RAW parsed_* | Parser snapshot | `raw_payload` + typed lead columns on upsert | `TRANSFORM` | No separate RAW parse table |
| CLEAN `lead_clean_v2` | Current lead | `leads` | `MIGRATE`+`TRANSFORM`; collapse dup rows by `lead_id`/`source_message_id` | `PROJECTION ONLY` |
| CLEAN manager_* / telegram_action_token | Manager UX | `leads.*` | `MIGRATE` | Projection optional |
| CLEAN AI/reply/quality fields | Enrichment | `leads.*` typed cols | `MIGRATE` | Projection optional |
| `DEDUP_INDEX` | Lookup | `lead_dedup_keys` + `UNIQUE(inbound source)` | `MERGE`/`TRANSFORM` | No tab required |
| `DEDUP_INDEX.dedup_key` | key_type:value | `lead_dedup_keys.dedup_key` | `MIGRATE` | No |
| `LEAD_EVENTS` | History | `lead_events` | `MIGRATE`+`TRANSFORM` event_type/payload | `PROJECTION ONLY` |
| `LEAD_DELIVERIES` | Card sync | `deliveries` (`delivery_type=lead_card`) | `MIGRATE`+`TRANSFORM` | Projection optional |
| `REMINDER_DELIVERIES` / reminder_key | Reminder claims | `jobs` + `deliveries` (`delivery_type=reminder`) | `TRANSFORM`/`MERGE` | No separate tab required |
| `ACCESS` / `ACCESS_CONTROL` | Staff ACL | `access_rules` | `MIGRATE`+`TRANSFORM` roles/flags | `PROJECTION ONLY` |
| ACCESS revoked history | Revoked staff | `access_rules` `is_active=false` | `MIGRATE` | Projection optional |
| `CONFIG` app flags | Runtime flags | `config` | `MIGRATE` selective keys | Projection optional |
| `CONFIG` chat ids / admin ids | Sensitive identifiers | `config` (`is_secretish`) or secret store | `TRANSFORM` — prefer vault | Not in Git |
| `CONFIG` OAuth/bot tokens | Secrets | — | `DROP AS LEGACY` from DB plan | Secret store only |
| `CONFIG` reminder window stamps | Runtime | `jobs.dedupe_key` / payload + optional config mirrors | `TRANSFORM` | Optional mirror |
| `CONFIG` heartbeats (`last_*`) | Ops stamps | `config` | `MIGRATE` | Projection optional |
| `ERRORS` | Failures | `errors` | `MIGRATE`+`TRANSFORM` | `PROJECTION ONLY` |
| Moderator Telegram callbacks | Actions | `change_lead_status` → `lead_events`+`audit_logs` | `TRANSFORM` (runtime path) | N/A |
| Sheets `retryOnFail` | Provider retry | `jobs` / `deliveries` status | `DROP AS LEGACY` as sole mechanism | No |
| Quota defer static map | Defer by msg id | `inbound_events.deferred` + `jobs.sheets_quota_defer` | `TRANSFORM` | No |
| Historical `lead-base` / `lead-base-processed` | Legacy | — | `DROP AS LEGACY` (preserve Sheets archive) | Archive only |
| Gmail labels PROCESSED/ERROR | Mailbox state | Workflow concern; optional job | Not a PG SoT table | Remains Gmail |

---

## DEDUP_INDEX LEGACY → target mechanism

1. **Message identity:** `UNIQUE(inbound_events.source_system, source_id)` + `leads.source_message_id` unique index.  
2. **Contact / site keys:** `lead_dedup_keys` with `UNIQUE(dedup_key)` and `key_type` CHECK.  
3. **Idempotent ops:** `idempotency_keys(scope, idempotency_key)`.

No `dedup_index` table named after the Sheet.

---

## Non-goals

- Live import execution  
- Operational.v3.dev  
- Preserving every Sheets column name forever
