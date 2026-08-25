# DB-First Successor Blueprint

**Status:** ROADMAP / ARCHITECTURE ONLY — not production runtime  
**Current production persistence:** Google Sheets (accepted stable contour 2026-08-17)  
**Preferred successor system of record:** PostgreSQL  
**Related:** [DB-FIRST-MIGRATION-ROADMAP.md](DB-FIRST-MIGRATION-ROADMAP.md) · [SHEETS-DEPENDENCY-MAP.md](../architecture/SHEETS-DEPENDENCY-MAP.md)

Do **not** migrate the live stable contour from this document alone.

---

## 1. Why database-first

Google Sheets work for the current low-volume i-SEO contour, but they are a weak primary operational memory for reusable Sales Manager systems:

| Need | Sheets limitation | PostgreSQL benefit |
|------|-------------------|--------------------|
| Transactional consistency | Partial / race-prone updates | ACID transactions |
| Explicit schema | Header drift, soft typing | Migrated schema + constraints |
| Filtered queries | Costly / 429-prone broad reads | Indexed `WHERE` / joins |
| Concurrency | Soft locking only | Row locks / advisory locks |
| State-machine integrity | App-enforced only | Constraints + event log |
| Auditability | Sparse event tabs | Append-only event tables |
| Durable history | Cell overwrite risk | Immutable source + event history |
| Multi-project isolation | Workbook sprawl | Schema / tenant keys |
| Automation / reporting | Export friction | SQL / BI / APIs |

**Principle:** PostgreSQL is the preferred operational system of record for successors and new client builds. Sheets may remain optional for export, lightweight reporting, QA inspection, and temporary migration tooling — **not** primary state machine / operational memory.

---

## 2. Entity model (suggested)

Exact table names may evolve; concepts are required.

```text
projects
  └─ lead_sources (RAW / forensic authority)
  └─ leads (CLEAN / operational authority)
       ├─ lead_contacts
       ├─ lead_lifecycle_events
       ├─ lead_delivery_events
       ├─ lead_actions (callback / token outcomes)
       └─ lead_reminders (notification log; not lifecycle)
  system_config
  audit_log
```

| Entity | Role | Immutable? |
|--------|------|------------|
| `projects` | Tenant / client isolation | Mostly immutable identity |
| `lead_sources` | Durable original visible source body + provenance | Source body immutable after write |
| `leads` | Normalized operational lead + current lifecycle | Mutable status/ops fields only |
| `lead_contacts` | Structured contacts (optional normalize) | Mutable with audit |
| `lead_lifecycle_events` | Append-only status transitions | Append-only |
| `lead_delivery_events` | Telegram/email delivery attempts | Append-only |
| `lead_actions` | Callback / action-token outcomes | Append-only |
| `lead_reminders` | Reminder send / skip decisions | Append-only |
| `system_config` | Non-secret runtime keys | Mutable with audit |
| `audit_log` | Operator / admin mutations | Append-only |

### Suggested primary keys / uniqueness

- `projects.id` UUID PK  
- `leads.id` UUID PK (= `lead_id`)  
- `lead_sources.id` UUID PK; unique `(project_id, source_message_id)`  
- `leads.source_id` FK → `lead_sources`  
- Unique dedupe: `(project_id, source_message_id)`, optional contact fingerprints  
- Action tokens: opaque token → `lead_id` + action family; one successful apply per `(lead_id, action)`

### Indexes (minimum)

- `lead_sources(project_id, source_message_id)`  
- `leads(project_id, manager_status, created_at)` — reminder / pending selectors  
- `leads(project_id, updated_at)`  
- `lead_actions(token)` unique  
- `lead_lifecycle_events(lead_id, created_at)`  
- `lead_delivery_events(lead_id, created_at)`  
- `lead_reminders(project_id, reminded_at)`

---

## 3. RAW vs CLEAN in the database

| Layer | Table | Authority |
|-------|-------|-----------|
| RAW | `lead_sources` | Forensic / literal original visible body |
| CLEAN | `leads` | Operational normalized representation |

Rules:

- Capture full source **before** parser normalization.  
- Never reconstruct “raw” from CLEAN fields.  
- Never use CLEAN as substitute for `📄 Исходная заявка`.  
- Lifecycle mutations update `leads` + append `lead_lifecycle_events`.  
- Raw view reads `lead_sources.body` (or equivalent), with privacy/Telegram-safe cleanup only.

---

## 4. Callback / action tokens

- Store opaque action tokens bound to `lead_id` + allowed action.  
- Resolve token → authorize manager → apply once (idempotent).  
- Successful apply: lifecycle event + optional card edit; raw action: display only.  
- Conflicts (`processed` ↔ `spam`): record attempt; do not overwrite silently.

---

## 5. Delivery idempotency

- Separate delivery state from lifecycle.  
- Record each Telegram send attempt (`lead_delivery_events`).  
- Re-delivery ≠ re-ingestion: never re-fetch Gmail as if a new lead when re-sending a card.  
- Dedupe on `source_message_id` at ingest; delivery guards on `lead_id` / attempt counters.

---

## 6. Reminder queries

Reminder should be a filtered SQL query, not a sheet scan:

```text
SELECT leads still actionable pending
WHERE project_id = ?
  AND manager_status IN (actionable set)
  AND not spam/processed/test/archive
  AND schedule weekday Mon–Fri in Europe/Moscow
```

Monday includes weekend backlog (created Sat/Sun still pending). Reminder writes only to `lead_reminders` (notification log) — **no** lifecycle mutation.

---

## 7. Project tenancy

- Every operational row carries `project_id`.  
- Config, operators, and secrets references are project-scoped.  
- No cross-tenant joins in default queries.

---

## 8. Secrets / config / observability

- `system_config` stores non-secret keys (`ai_enabled`, reminder schedule, parser_version).  
- Secret values live in n8n credentials / secret store — **references only** in DB.  
- Observability: structured errors table + event log + workflow execution IDs (external).  
- Retention: policy per project (source bodies may be longer than ops notes).  
- Backup/restore: PostgreSQL backups are primary; Sheets export optional secondary.

---

## 9. Migrations

- Schema changes via versioned migrations only.  
- No silent ALTER in production without charter.  
- Seed config rows with fail-closed defaults (`ai_enabled=false`).

---

## 10. Explicit non-goals

- Big-bang cutover from Sheets without dual-read/write evidence.  
- Treating Sheets as ideal architecture for new builds.  
- Auto-CRM expansion, auto-reply to clients, or AI ON without separate charter.  
- Changing the current frozen production contour from this blueprint alone.
