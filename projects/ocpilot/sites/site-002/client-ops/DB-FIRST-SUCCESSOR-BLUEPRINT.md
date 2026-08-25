# SITE-002 / Reusable — DB-First Successor Blueprint

**Preferred mature target:** PostgreSQL  
**Current production:** unchanged (n8n Data Table)

## Why PostgreSQL

Transactional state; explicit schema; unique constraints; idempotency; event history; concurrency control; cross-project tenancy; auditability; reporting; recovery; fewer hidden platform-specific limits.

## Suggested entities (illustrative)

| Entity | Purpose |
|--------|---------|
| sites | Tenancy / site_id / domain |
| import_runs | run_id, trigger_source, terminal class, timestamps |
| import_phases | catalog/offers phase results |
| source_files | filename, family, presence, checksum if available |
| client_ops_events | event_id, classification, link to run |
| delivery_attempts | channel, status, timestamps |
| watchdog_events | no-import evaluations |
| system_config | kill switch mirrors / non-secret flags |
| audit_log | operator/agent actions |

Exact names may evolve; preserve concepts.

## Design requirements

- Unique constraints on run_id / event_id
- Explicit idempotency keys
- Tenancy by site_id
- Indexes for time-range + site queries
- Retention policy
- Backup/restore story
- No big-bang cutover from Data Table
