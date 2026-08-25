# Sheets Dependency Map

**Gate:** `SM_CURRENT_SHEETS_REALITY_DOCUMENTED`  
**Current reality:** Google Sheets are production operational persistence for Sales Manager v2.  
**Future preference:** PostgreSQL system of record — [DB-FIRST-SUCCESSOR-BLUEPRINT.md](../roadmap/DB-FIRST-SUCCESSOR-BLUEPRINT.md)  
**Do not migrate live production from this map alone.**

Workbook IDs are held in n8n credentials / CONFIG references — **not** committed here.

---

## Dependency table

| Sheet / tab | Reader(s) | Writer(s) | Query shape | Mutation type | Criticality | Failure mode | Future PostgreSQL |
|-------------|-----------|-----------|-------------|---------------|-------------|--------------|-------------------|
| RAW `lead_raw_v2` | Admin.dev raw callback; forensics | Operational.dev | Filtered by `lead_id` (required) | Append-only | high | Empty/lossy source; 429 if broad read | `lead_sources` |
| CLEAN `lead_clean_v2` | Ops card path; Admin callbacks; reminders | Ops (upsert); Admin (lifecycle) | By `lead_id` / pending status filters | Upsert + lifecycle fields | **critical** | Cards/lifecycle/reminders fail | `leads` |
| `CONFIG` | Ops + Admin | Admin / operator | Key lookup | Key/value update | **critical** | Fail-closed AI/reminder/auth | `system_config` + secret refs |
| `LEAD_EVENTS` | Ops health; forensics | Ops + Admin | Append / recent window | Append-only | high | Weak audit trail | `lead_lifecycle_events` / `lead_actions` |
| `ERRORS` | Admin `/last_error`; forensics | Ops + Admin | Latest / recent | Append or last-error update | high | Blind failures | `errors` |
| `DEDUP_INDEX` | Ops ingest | Ops ingest | Key lookup by message/contact fingerprint | Upsert keys | **critical** | Duplicate leads | unique constraints + `dedupe_keys` |
| Historical RAW `lead-base` | Forensic only | **none** (preserve) | Ad-hoc | Frozen historical | low | Confusion if treated as SoR | archive import only |
| Historical CLEAN `lead-base-processed` | Forensic only | **none** (preserve) | Ad-hoc | Frozen historical | low | Contaminates dedupe if mixed | archive import only |

---

## Query-shape rules (production)

| Path | Allowed | Forbidden |
|------|---------|-----------|
| Raw callback | Filtered RAW by `lead_id` | Full-sheet / unbounded RAW dump |
| Reminder | Bounded CLEAN pending filter + CONFIG | Full CLEAN dump as “all rows” without filter |
| Dedupe | Index / keyed lookup | Matching solely on soft site strings without policy |
| CONFIG | Key reads | Embedding secret values into Sheets cells that get exported to Git |

---

## Criticality legend

- **critical** — contour cannot safely operate without it  
- **high** — core feature or recovery degraded  
- **low** — historical / forensic only  

---

## Known production incident link

Broad RAW lookup → Google Sheets API **429** → fixed by filtered `lead_id` lookup.  
See [LESSONS-LEARNED.md](../knowledge/LESSONS-LEARNED.md) §3 and evidence under `evidence/literal-gmail-body-raw-20260816/`.

---

## Reader / writer summary

1. Operational.dev: Gmail → append RAW → upsert CLEAN → delivery events → dedupe keys.  
2. Admin.dev: lifecycle callbacks → CLEAN status + events; raw callback → RAW read; reminder → CLEAN read + notify.  
3. Reminders never write lifecycle.  
4. Raw view never writes lifecycle.  

---

## Successor principle

`SM_DB_FIRST_SUCCESSOR_DIRECTION_DOCUMENTED`: new builds and next-generation i-SEO architecture should treat PostgreSQL as primary operational memory. Sheets may remain export/report/QA/migration surface only.
