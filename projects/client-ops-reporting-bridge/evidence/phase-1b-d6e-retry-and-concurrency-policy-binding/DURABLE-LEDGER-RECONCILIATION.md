# DURABLE-LEDGER-RECONCILIATION

**Token:** `D6E_DURABLE_LEDGER_RECONCILIATION_DEFINED`

Data Table schema (15 columns; Workstream A preserved):

| # | Column |
|---|--------|
| 1 | `event_id` |
| 2 | `event_fingerprint` |
| 3 | `site_id` |
| 4 | `schema_name` |
| 5 | `schema_version` |
| 6 | `event_type` |
| 7 | `event_status` |
| 8 | `intake_state` |
| 9 | `delivery_state` |
| 10 | `first_seen_at` |
| 11 | `last_seen_at` |
| 12 | `duplicate_count` |
| 13 | `conflict_count` |
| 14 | `redaction_version` |
| 15 | `sandbox_marker` |

Reconciliation reads these columns GET-only. D6E does not mutate schema or rows.

Live baseline: 15 cols / 4 rows · historical PENDING · D6A2 SENT.
