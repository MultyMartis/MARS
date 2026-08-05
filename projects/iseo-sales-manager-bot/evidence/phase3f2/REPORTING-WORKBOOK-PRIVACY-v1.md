# REPORTING WORKBOOK PRIVACY v1 — Phase 3F.2

## Privacy contract for any reporting workbook

The reporting workbook described in [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md) is **aggregate/statistical only**. It must not become a second copy of CLEAN's client-identifying columns.

| Rule | Detail |
|---|---|
| No PII columns | No `client_name`, `primary_contact`, `phone`, `email`, `messenger`, `site` (where site could be client-identifying), and no free-text `summary`/`manager_notes`/`quality_comment` copy |
| No raw identifiers | No `lead_id`, no `gmail_message_id`/`gmail_thread_id`, no `telegram_action_token`, no Telegram numeric IDs/usernames, no spreadsheet IDs/URLs |
| Aggregation level | Counts, rates, and dated buckets (e.g. leads per day, pending age distribution, source/service breakdowns) only — never a per-lead identifiable row |
| Real-only filter | Must apply the same `real-only-v1` / `archive_excluded` scoping as [PRODUCTION-STATS-EPOCH-v1.md](PRODUCTION-STATS-EPOCH-v1.md) so test volume never inflates business-facing numbers |
| Access | Same-or-narrower audience than CLEAN itself — a reporting workbook must not widen access to lead data beyond who could already see CLEAN |

## Rationale

This mirrors the same discipline already applied elsewhere in the programme (e.g. the i-SEO Report Hub's exclusion of credential-bearing material from its product corpus) — reporting surfaces are treated as **more** exposed than operational tabs, not less, because they are built to be shared/read by a wider or less access-controlled audience over time.

## Status

| Item | Status |
|---|---|
| Privacy contract (this document) | **IMPLEMENTED** (design-level) |
| Enforcement in a live reporting workbook | **PENDING OPERATOR** — depends on [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md) actually existing |

*Related: [REPORTING-WORKBOOK-CREATION-v1.md](REPORTING-WORKBOOK-CREATION-v1.md), [REPORTING-SYNC-v1.md](REPORTING-SYNC-v1.md).*
