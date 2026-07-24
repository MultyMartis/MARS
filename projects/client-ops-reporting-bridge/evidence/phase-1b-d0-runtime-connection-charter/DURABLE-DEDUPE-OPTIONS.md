# Durable Dedupe Options — Phase 1B-D0

**Status:** DECISION (not implemented)
**Current operational label:** `DEDUPE_DEFERRED_SANDBOX`
**Live response note:** `DEDUPE_NOT_ENABLED_SANDBOX` / `dedupe: "DEFERRED_SANDBOX"`

## Stage-ordering decision

| Option | Meaning | Verdict |
|--------|---------|---------|
| A | Mandatory before any runtime producer connection | **SELECTED** |
| B | Mandatory only before scheduler/unattended | Rejected as primary (too late once Telegram can fire) |
| C | Deferrable for one narrow manual live-source E2E | Rejected — B2 already proved duplicate `event_id` accepts; Pattern B would notify twice on retry |
| D | Not required | **FORBIDDEN** without conclusive contrary evidence (none) |

**Rationale:** Pattern B delivers Telegram after HTTP 202. Without durable dedupe, a producer retry or ambiguous timeout creates duplicate operator messages. Therefore durable dedupe precedes runtime producer connection.

## Option matrix

| Option | Installed/proven | Atomicity | Persistence | Operations | Complexity | Recommendation |
|--------|------------------|-----------|-------------|------------|------------|----------------|
| 1. n8n Data Table (OpenAPI `/api/v1/data-tables`, upsert) | **PROVEN API surface** (GET list 200, count=0); workflow node type **SAFE UNKNOWN** | Upsert documented; true CAS **SAFE UNKNOWN** | Across executions: expected; across workflow updates: expected (table is workspace resource) | Visible via API; backup/export **SAFE UNKNOWN** | Medium | **PRIMARY RECOMMENDATION** |
| 2. Legacy n8n Data Store | **Not in OpenAPI** on this install | N/A | N/A | N/A | N/A | Do not assume; treat as unavailable |
| 3. Workflow `staticData` | Mentioned in OpenAPI meta; MetaBOT anti-pattern as sole SoT | Weak / race-prone | Pollutes exports; drifts | Poor audit | Low | **Reject as sole authority** |
| 4. External database table | Not present for Client Ops | Strong if designed | Strong | Ops burden | High | Out of MVP unless already present |
| 5. Local producer-side durable ledger | Feasible on exporter host (filesystem) | File lock / atomic rename possible | Local only; not shared across producers | Operator-visible files | Low–medium | **FALLBACK** (and optional dual-write mirror) |
| 6. Google Sheets | Not in workflow; anti-pattern for authority | Weak | Spreadsheet | Manual | Medium | **Reject** |
| 7. Filesystem ledger on Storage | Paths known for SITE-002 Storage; Bridge PROFILE_B | Locking needed | Strong if promoted carefully | Audit-friendly | Medium | Optional PROFILE A audit mirror later |
| 8. Dedicated MARS bridge service | Does not exist | Designable | Designable | New product surface | High | **Deferred** — not for one-site MVP |

## Recommended architecture (PROPOSED)

**Primary:** n8n **Data Table** keyed by `event_id`, with documented columns for envelope hash, delivery status, attempt count, timestamps, n8n execution id, Telegram message id (if any). Prefer upsert / check-then-set proven in D1.

**Fallback:** producer-side append-only / replace-safe durable ledger under ignored local Client Ops runtime evidence (not Git), consulted before POST and updated after terminal outcomes. Use if Data Table node binding or atomicity cannot be proven in D1.

**Optional later mirror:** sanitized Storage audit record (PROFILE A style) — not required for first MVP path.

## Suitability

| Concern | Primary (Data Table) | Fallback (producer ledger) |
|---------|----------------------|----------------------------|
| One-site MVP | Yes | Yes |
| Multi-site migration | Per-site table or `site_id` column | Per-site ledger files |
| Secret requirements | None in table rows | None in ledger |
| Production dependency | n8n host durability | Exporter host durability |
| Rollback | Delete/disable table rows or table under charter | Restore/remove ledger file |

## Unresolved (SAFE UNKNOWN)

- Exact workflow node typeVersion for Data Table operations.
- Whether upsert is concurrency-safe under parallel webhook executions.
- Backup/restore procedure for Data Tables on this host.
- Retention/TTL native support vs manual purge job.
