# Storage layer — Google Sheets

**Role:** Primary **durable** store for MetaBOT operational data described in operations (not schema-exported here).

---

## Documented uses

| Concern | Sheets role |
|---------|-------------|
| **Memory** | Longer-lived context for reuse across tasks — [memory-and-task-reuse.md](memory-and-task-reuse.md). |
| **seo_active_jobs** | Active job queue / status table for worker lifecycle — [task-lifecycle.md](task-lifecycle.md). |
| **Metadata** | Task and run metadata — **SAFE UNKNOWN** tab layout. |
| **User metadata** | May mirror Telegram fields for auditing — [user-metadata.md](user-metadata.md). |

---

## Limitations

- **Quota / rate limits:** frequent reads (e.g. `/health`) can trigger *“The service is receiving too many requests from you”* — [known-issues.md](known-issues.md).
- **Consistency:** not a transactional DB; race conditions possible between lock state and job rows.
- **Schema drift:** avoid **massive refactors** and **unnecessary new tables** per product decisions; prefer editorial layers for quality.

---

## SAFE UNKNOWN

- Spreadsheet IDs, tab names, column mappings.
- Whether multiple spreadsheets separate **memory** vs **jobs**.
- Backup / export procedures.

---

*See [integration-boundary.md](integration-boundary.md) — credentials stay in n8n.*
