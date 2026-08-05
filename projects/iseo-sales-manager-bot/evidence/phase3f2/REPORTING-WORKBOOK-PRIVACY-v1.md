# REPORTING WORKBOOK PRIVACY v1 — Phase 3F.2

## Access model (live)

| Role | Access |
|---|---|
| Owner / service credential | Full (current default) |
| Employee | Not shared yet — requires explicit operator instruction |
| External client | No access by default |
| Anyone with link / public | **Forbidden** — not enabled |

## Data rules

- Spreadsheet ID / URL never committed to Git; only private CONFIG `reporting_workbook_ref`.
- No Telegram chat IDs, internal hashes, workflow execution IDs, or backend workbook IDs on employee-facing sheets.
- Employee workbook may contain business lead fields (client, contacts, status) for authorized staff — it is **not** a public client export.
- External client views require a separately approved filtered surface (out of scope for automatic share in 3F.2).

## Status

| Item | Status |
|---|---|
| Private creation (no public link) | **PASS** |
| Automatic share to employees/clients | **Not performed** |
| Operator-directed share | **PENDING OPERATOR** (name recipient + access level) |

*Related: [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md).*
