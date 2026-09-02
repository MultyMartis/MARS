# i-SEO Sales — Relational Data Model v1

**Document:** `ISEO-SALES-DATA-MODEL-v1`  
**project_id:** `mars-data-layer`  
**Status:** Normative local schema design (not production-applied)  
**Date:** 2026-09-03  
**Base architecture:** `MARS-BOT-DATA-ARCHITECTURE-v1` @ `0482e9cd`  
**Product authority:** `projects/iseo-sales-manager-bot/` (newest production evidence wins over older intent docs)

---

## 1. Domain overview

i-SEO Sales Manager Bot ingests Gmail form/forward messages, normalizes them into manager-facing leads, notifies Telegram recipients (admins/moderators), records manager actions, schedules weekday pending-lead reminders, and logs errors/deferrals around Google Sheets and Telegram providers.

**Target:** PostgreSQL schema `app_iseo_sales` becomes the future runtime Source of Truth after controlled cutover. Google Sheets becomes projection/manual UI. n8n remains the workflow engine (SQLite unchanged).

**Design rule:** do **not** reproduce Sheets tabs one-for-one. Map domain meaning → normalized entities + constraints.

---

## 2. Current Sheets model

| Concept / tab | Workbook | Role today |
|---------------|----------|------------|
| `lead_raw_v2` (RAW) | RAW | Append intake evidence; durable `raw_text` / Gmail ids |
| `lead_clean_v2` (CLEAN) | CLEAN | Manager-facing current lead state (intended upsert; live Sep-1 evidence often append) |
| `DEDUP_INDEX` | CLEAN | Bounded lookup `dedup_key` → lead |
| `LEAD_EVENTS` | CLEAN | Append-only processing/admin events |
| `LEAD_DELIVERIES` | CLEAN | Telegram card message ids / sync |
| `REMINDER_DELIVERIES` | CLEAN | Reminder claim ledger |
| `ACCESS` / `ACCESS_CONTROL` | CLEAN | Staff recipients ACL (authority over CONFIG cache) |
| `CONFIG` | CLEAN | Key/value runtime + heartbeats + reminder window stamps |
| `ERRORS` | CLEAN | Structured/last errors |

Legacy historical tabs (`lead-base`, `lead-base-processed`) remain preserve-only.

---

## 3. Legacy concepts being removed/replaced

| Legacy | Disposition |
|--------|-------------|
| RAW row number / sheet order as identity | **DROP AS LEGACY** — use `inbound_events.id` + `(source_system, source_id)` |
| CLEAN as sole mutable log without history | **TRANSFORM** — `leads` current state + `lead_events` |
| `DEDUP_INDEX` tab | **MERGE** — `UNIQUE(inbound…)` + `lead_dedup_keys` for contact keys |
| CONFIG as dump for everything | **TRANSFORM** — typed `config` rows for app flags only; secrets out of DB |
| ERRORS sheet as single undifferentiated log | **TRANSFORM** — `errors` vs `lead_events` vs `audit_logs` |
| Reminder “day sent” only in CONFIG | **TRANSFORM** — `jobs` + delivery ledger |
| Sheets `retryOnFail` as only retry | **TRANSFORM** — `jobs` / `deliveries` status machines |
| Fake table per Sheet | **DROP AS LEGACY** |

---

## 4. Target entities

| Table | Purpose |
|-------|---------|
| `app_iseo_sales.inbound_events` | Durable Gmail/source intake (RAW semantics) |
| `app_iseo_sales.leads` | Current authoritative lead state (CLEAN semantics) |
| `app_iseo_sales.lead_dedup_keys` | Contact/message dedup lookup (justified; not a Sheet clone) |
| `app_iseo_sales.lead_events` | Immutable domain history |
| `app_iseo_sales.access_rules` | Staff ACL (ACCESS); moderator identity lives here in V1 |
| `app_iseo_sales.deliveries` | Telegram/outbox intents + results |
| `app_iseo_sales.jobs` | Reminders, defer, retries, reconciliation |
| `app_iseo_sales.idempotency_keys` | Exactly-once control for mutating ops |
| `app_iseo_sales.errors` | Structured failures |
| `app_iseo_sales.audit_logs` | Operator/privilege-sensitive action trail |
| `app_iseo_sales.config` | DB-worthy application config only |

**Not created in V1:** separate empty `moderators` table (ACCESS/`access_rules` is the production ACL authority).  
**Not created:** `app_seo_content` business tables (placeholder schema only).  
**mars_core:** `apps`, `workflow_releases`, `data_contract_versions`, `schema_migrations`.

---

## 5. Identity model

| Entity | Internal PK | Business / external id |
|--------|-------------|-------------------------|
| inbound_events | `bigint` identity | `UNIQUE(source_system, source_id)` where `source_id` = Gmail `gmail_message_id` |
| leads | `bigint` identity | `lead_id text UNIQUE` (production shapes: `LEAD_<12 hex>` and occasional `lead_<hex>`; preserve as opaque string) |
| lead_events | `bigint` identity | optional `event_id text UNIQUE` |
| deliveries | `bigint` identity | optional `delivery_id text UNIQUE`; provider `external_message_id` |
| jobs | `bigint` identity | optional `dedupe_key` unique when present |
| access_rules | `bigint` identity | `principal_key` (e.g. `ADMIN_A`, `MOD_B`) |
| idempotency_keys | `bigint` identity | `UNIQUE(scope, idempotency_key)` |

**UUID usage:** not required for internal PKs. `lead_id` may be UUID/ULID-like string minted at parse **outside** DB — stored as text unique column.

---

## 6. Inbound event / idempotency model

Hard invariant: the same stable Gmail message must not create two intake authorities.

- `source_system = 'gmail'`
- `source_id = gmail_message_id` (proven stable in product)
- DB enforcement: `UNIQUE(source_system, source_id)`
- Re-sight updates `last_seen_at` / attempts via `register_inbound_event` — does not insert a second row
- `raw_payload jsonb` + `raw_text` hold durable evidence (full visible body when available)
- Processing statuses: `received | processing | processed | failed | deferred | skipped`

Sheets quota defer maps to `deferred` + a `jobs` row (`job_type=sheets_quota_defer`) rather than a static n8n memory map long-term.

---

## 7. Lead current-state model

`leads` is the **current** manager-facing state (one row per `lead_id`).

Typed columns for searchable/business-critical fields (contacts, status, quality, duplicate classification, versions). Flexible form/provider extras in `form_metadata jsonb`.

`version int` supports optimistic concurrency for moderator transitions.

**Operational status vocabulary (live Telegram/reminder path):**  
`new`, `pending`, `processed`, `spam`, `reopened`, `error` (+ CRM-oriented values retained for documented lifecycle: `reviewing`, `contacted`, `waiting_client`, `qualified`, `not_target`, `closed`).

CHECK constraint admits the union; application layer documents which subset each workflow path may write.

---

## 8. Lead event / history model

`lead_events` is append-only domain history (`INSERT` + `SELECT`; no runtime `UPDATE`/`DELETE`).

Typical `event_type` values (non-exhaustive; open set as text):  
`status_changed`, `lead_created`, `lead_upserted`, `manager_reopened`, `marked_spam`, `manager_raw_source_viewed`, `moderator_revoked`, …

Payload is jsonb; actor fields separate from payload.

---

## 9. Moderator / action model

**Separation:**

| Kind | Table | When |
|------|-------|------|
| Domain | `lead_events` | Business-meaningful transition (`status_changed`) |
| Audit | `audit_logs` | Who/command/result (`telegram_callback`, `/moderator_remove`, …) |
| ACL | `access_rules` | Whether principal may receive cards/reminders |

A moderator status click produces **both** a domain event and an audit row inside `change_lead_status` — not a third `moderator_actions` table in V1 (avoids triple write of the same fact).

---

## 10. Delivery / outbox model

`deliveries` replaces `LEAD_DELIVERIES` + generalizes reminder sends.

Statuses: `pending | processing | sent | retry | dead | cancelled`.

Fields include recipient principal, channel, `external_message_id` (Telegram message id), `idempotency_key`, attempts/lease columns for worker claim.

**No secrets** (no bot token). Chat ids may appear as operational identifiers; treat as sensitive in exports.

---

## 11. Reminder / job model

Reminders are `jobs` with `job_type = pending_reminder` (window key in `dedupe_key` / payload, e.g. `pending-reminder:YYYY-MM-DD:10:00:Europe/Moscow`).

Claim contract (future workers): `FOR UPDATE SKIP LOCKED` on `status IN ('pending','retry') AND available_at <= now()`; set `running`, `locked_by`, `lease_until`.

No Redis queue in V1.

---

## 12. Retry / defer model

| Current behavior | Target |
|------------------|--------|
| Sheets Quota Defer Gate (5m TTL by message id) | `inbound_events.processing_status=deferred` + `jobs.job_type=sheets_quota_defer` |
| n8n `retryOnFail` on Sheets nodes | Prefer durable job/delivery retry after cutover |
| Telegram send failure after CLEAN | `errors` + `deliveries.status=retry|dead`; Gmail label policy remains workflow concern |

---

## 13. Access model

`access_rules` mirrors production ACCESS authority:

- `principal_key`, Telegram user id (nullable in fixtures), display name, role (`admin|moderator|viewer`)
- `is_active`, `receives_cards`, `receives_reminders`
- revoked principals remain rows (`is_active=false`, `revoked_at`)

CONFIG recipient caches are **not** authoritative after cutover.

---

## 14. Config model

Only DB-worthy keys enter `config` (examples):  
`ai_enabled`, `ai_model`, `pending_reminders_enabled`, `message_format_version`, `reply_template_version`, `parser_version`, `dedupe_contact_window_days`, `gmail_query_limit`, heartbeat stamps (`last_success_at`, …), reminder window stamps.

**Not in DB:** Telegram bot token, Gmail/OpenRouter OAuth, n8n credentials.  
Sensitive app identifiers (chat ids) may be marked `is_secretish` but prefer secret store when practical.

---

## 15. Error model

`errors` stores sanitized structured failures: class/code/stage/provider/http_status/retryable/correlation/entity refs/context jsonb.  
Known classes include `sheets_quota_exceeded`, `telegram_delivery_failed`, `processing_error`.

---

## 16. Audit model

`audit_logs` for operator/admin/privilege-sensitive actions and command outcomes. Distinct from domain `lead_events`.

---

## 17. Relationships

```text
inbound_events 1—0..1 leads (via inbound_event_id / source_message_id)
leads 1—* lead_events
leads 1—* lead_dedup_keys
leads 1—* deliveries
access_rules 1—* deliveries (recipient_principal_key)
jobs may reference lead_id (soft)
errors soft-referenced from deliveries.last_error_id
mars_core.apps 1—* workflow_releases
```

Cross-schema: apps only → `mars_core`. No FK to `app_seo_content`.

---

## 18. Constraints

- `uq_inbound_events_source` on `(source_system, source_id)`
- `uq_leads_lead_id`
- unique index on `leads.source_message_id` where not null
- `uq_lead_dedup_keys_dedup_key`
- `uq_idempotency_keys_scope_key`
- status CHECKs on leads/jobs/deliveries/inbound
- one active `mars_core.workflow_releases` per `(app_id, workflow_family)` (partial unique)

---

## 19. Indexes

Hot paths: inbound processing status; leads by `manager_status`; deliveries/jobs `(status, available_at)`; lead_events `(lead_id, occurred_at)`; access active recipients.

---

## 20. Retention policy

| Class | V1 guidance |
|-------|-------------|
| inbound_events / raw_text | Long retention (forensic); bound size at write |
| leads | Indefinite while product active |
| lead_events / audit_logs | Append-only; prune only under explicit charter |
| deliveries / jobs completed | Retain ≥ 90 days operationally; archive later |
| errors | Retain ≥ 90 days; resolved flag for UX |
| idempotency_keys | TTL via `expires_at` (e.g. 7–30 days) |

Exact production purge jobs are **not** automated in this wave.

---

## 21. Sheets mapping

See `ISEO-SALES-DATA-MAPPING-v1.md`.

---

## 22. Migration considerations

- Import must collapse duplicate CLEAN rows by `lead_id` / `source_message_id` (live append risk).
- Preserve opaque `lead_id` strings as-is.
- Map reminder CONFIG window keys → `jobs.dedupe_key`.
- ACCESS revoked rows migrate with `is_active=false`.
- Do not migrate OAuth/bot tokens.
- Shadow mode writes PG without cutting Sheets SoT.

---

## 23. Open questions

See `ISEO-SALES-DATA-OPEN-QUESTIONS-v1.md` (kept small).

---

## Status type strategy (decision)

**text + CHECK** (not PG ENUM): migration-friendly expand/contract during early bot evolution.

## Timestamp strategy

All instants: `timestamptz` (UTC storage; Europe/Moscow at presentation edge).
