# REPORT — MARS Data Layer / iSEO Sales schema V1

**Document:** `REPORT-mars-data-layer-iseo-sales-schema-v1`  
**Date:** 2026-09-03  
**Base tip:** `0482e9cd` (`origin/mars/canonical-post-recovery`)  
**Worktree:** `X:\AI MARS STORAGE\git-sync-mars-data-layer-iseo-schema-v1-20260903-011614\repo`  
**Branch (work):** `mars/data-layer-iseo-schema-v1`

---

## 1. Verdict

**DATA MODEL READY — LOCAL POSTGRES RUNTIME REQUIRED FOR EXECUTION VALIDATION**

Relational model v1, versioned migrations, roles/grants (no passwords), synthetic fixtures, and apply/permission test scripts are in Git under `projects/mars-data-layer/`.

This machine has **no** `psql` and **no** Docker; `X:\MARS-Localhost\databases\mars-bot-data` does **not** exist. Migrations were **not** applied against a live database in this wave.

No VEESP / production PostgreSQL / n8n / Sheets / Operational.dev / Admin.dev mutation.

---

## 2. Current model forensic

Authority reconstructed from `projects/iseo-sales-manager-bot/` (newest production evidence preferred over early-phase docs).

| Concept | Current semantics (summary) |
|---------|----------------------------|
| Gmail identity | Stable `gmail_message_id` as source event id |
| Lead identity | Opaque `lead_id` text (`LEAD_<…>` patterns); mint algorithm **SAFE UNKNOWN** (open Q1) |
| Dedup | Keys `{type}:{normalized}`; live risk of append-not-upsert on CLEAN/DEDUP |
| RAW / CLEAN | Sheet tabs `lead_raw_v2` / `lead_clean_v2` — storage, not domain tables |
| Lifecycle | Dual vocab: CRM statuses + Telegram ops (`pending` / `processed` / `spam` / `reopened`) |
| ACCESS | ACL authority (Telegram identity + role + active/revoked) |
| CONFIG | Mixed secrets / app flags / constants — secrets **out** of DB |
| Deliveries / reminders / retries | Partial Sheets/runtime state → deliveries + jobs |
| Errors | Structured operational failures |

---

## 3. Target entities

**`mars_core`:** `apps`, `data_contract_versions`, `workflow_releases`, `schema_migrations`.

**`app_iseo_sales`:**

| Table | Role |
|-------|------|
| `inbound_events` | Durable Gmail/source ingest; replace RAW |
| `leads` | Current normalized lead state; replace CLEAN |
| `lead_dedup_keys` | Optional secondary uniqueness (not a Sheet clone) |
| `lead_events` | Immutable domain history |
| `access_rules` | ACL (no separate empty `moderators` table in V1) |
| `deliveries` | Telegram outbox |
| `jobs` | Reminders / defer / retry / reconciliation |
| `idempotency_keys` | Side-effect dedupe |
| `errors` | Structured errors (sanitized) |
| `audit_logs` | Actor/command/result audit |
| `config` | Non-secret application config only |

**Not created:** `dedup_index`, `moderator_actions` table, `app_seo_content` business tables (empty schema placeholder only).

---

## 4. Legacy concepts removed / replaced

| Legacy | Target |
|--------|--------|
| RAW row / sheet row number | `inbound_events` + `UNIQUE(source_system, source_id)` |
| CLEAN as SoT sheet | `leads` typed columns + optional JSONB metadata |
| DEDUP_INDEX sheet | UNIQUE constraints + `lead_dedup_keys` |
| LEAD_EVENTS sheet | `lead_events` |
| LEAD_DELIVERIES sheet | `deliveries` |
| Reminder / retry sheet state | `jobs` |
| ACCESS sheet | `access_rules` |
| CONFIG dump of secrets | Outside DB; non-secret → `config` |
| ERRORS sheet | `errors` |

---

## 5. Identity / idempotency

- Internal PK: `bigint GENERATED … AS IDENTITY`
- Business ids: separate unique text (`lead_id`, delivery/job business keys as designed)
- Inbound: `UNIQUE(source_system, source_id)` — `source_id` = Gmail message id
- Status transitions / deliveries / jobs: `idempotency_keys` + function-level checks
- Timestamps: `timestamptz` (UTC semantics)

---

## 6. Leads

Current-state table with typed contact/site/status/owner fields; flexible form metadata in JSONB; `version` for optimistic concurrency in `change_lead_status`.

---

## 7. Events

`lead_events`: insert-only domain history. Runtime grants: SELECT + INSERT only (no UPDATE/DELETE).

---

## 8. Moderators / access

`access_rules` holds Telegram identity, role, active/revoked. No Telegram tokens. Profile vs ACL not split further until evidence requires it.

---

## 9. Deliveries / outbox

`deliveries` with status set including pending / processing / sent / retry / dead / cancelled; attempts; external message id; idempotency key; optional `lead_id`; no secrets.

---

## 10. Jobs / retry / defer

`jobs` with `status + available_at`, lease fields, `dedupe_key`. `claim_jobs` documents `FOR UPDATE SKIP LOCKED`. No Redis in V1.

---

## 11. Errors / audit

`errors` sanitized + context JSONB. `audit_logs` for actor/command/result. Moderator status change → domain event **and** audit via `change_lead_status` (no third action table).

---

## 12. mars_core

Minimal: apps seed, data contract versions, workflow releases with one-active partial unique on `(app_id, workflow_family)`. No leads/jobs/errors in core.

---

## 13. Roles / security

Roles (no passwords in Git): `mars_migrator`, `iseo_runtime`, `iseo_agent`, `iseo_reader`.

- Runtime: DML on business tables as granted; **no** DDL; **no** UPDATE/DELETE on immutable event/audit tables
- Agent: primarily EXECUTE on narrow read functions + limited SELECT
- No access to `app_seo_content` business objects (schema placeholder isolated)
- No `execute_sql` / generic upsert

---

## 14. DB functions / contracts

Implemented: `register_inbound_event`, `upsert_lead`, `change_lead_status`, `enqueue_delivery`, `enqueue_job`, `claim_jobs`, `get_lead`, `list_pending_leads`, `fn_is_allowed_status_transition`.

Atomic status transition validates expected version/status, updates lead, appends event + audit, optional delivery enqueue.

---

## 15. Sheets mapping

Canonical matrix: `architecture/ISEO-SALES-DATA-MAPPING-v1.md`.  
v0 marked superseded.

---

## 16. Migrations

| File | Purpose |
|------|---------|
| `database/roles/001_create_roles.sql` | Role objects (no passwords) |
| `database/core/migrations/0001_roles_and_schemas.sql` | Schemas + role bootstrap |
| `database/core/migrations/0002_mars_core.sql` | Core tables + seeds |
| `database/app_iseo_sales/migrations/0001_base_tables.sql` | App tables |
| `0002_indexes.sql` | Indexes |
| `0003_functions.sql` | Functions + EXECUTE grants |
| `0004_grants.sql` | Table grants / immutability |

Status values: **text + CHECK** (migration-friendly; not ENUM).

---

## 17. Local runtime status

| Check | Result |
|-------|--------|
| `psql` on PATH | **Missing** |
| Docker | **Missing** |
| `X:\MARS-Localhost\databases\mars-bot-data` | **Absent** |
| System PostgreSQL install this wave | **Not performed** (policy) |

**LOCAL POSTGRES RUNTIME INSTALLATION REQUIRED** before apply/validation.

---

## 18. Tests

- `tests/iseo_sales/01_schema_apply.sh` — empty DB apply
- `02_constraints.sql` — uniqueness / transition / idempotency expectations
- `03_permissions.sql` — role isolation expectations
- Fixtures: `fixtures/iseo_sales/synthetic_v1.sql` (sanitized, deterministic)

Execution blocked until local PG exists.

---

## 19. Open questions

See `architecture/ISEO-SALES-DATA-OPEN-QUESTIONS-v1.md` (lead_id mint; live append vs upsert; delivery status enums; dual lifecycle vocab; local PG install timing). None block schema design; some block live cutover.

---

## 20. Server Ops impact

No mandatory handoff rewrite. Business tables remain migration-owned. Foundation handoff still covers VPS PG install/roles infrastructure only — operators do **not** hand-create app tables.

---

## 21. Git

- Clean worktree from `origin/mars/canonical-post-recovery` @ `0482e9cd`
- Selective paths: `projects/mars-data-layer/**` + `registry/project-registry.md`
- Push target: `origin/mars/canonical-post-recovery` (non-force)
- Commit SHAs: filled after commit/push in closeout

---

## 22. Next gate

1. Install/configure local disposable PostgreSQL under MARS Localhost conventions  
2. Run `01_schema_apply.sh` + constraint/permission tests  
3. Human accept model + open questions that affect cutover  
4. Only then: candidate workflow / Operational.v3.dev design (separate charter)

**Stop:** no production mutation, no Sheets/n8n cutover, no SEO Content schema build.
