# i-SEO Sales — Migration Validation Spec v1

**Document:** `ISEO-SALES-MIGRATION-VALIDATION-v1`  
**project_id:** `mars-data-layer`  
**Date:** 2026-09-03  
**Status:** Spec only — for future Sheets → PG import / shadow waves  
**Depends on:** `ISEO-SALES-DATA-MODEL-v1`, `ISEO-SALES-DATA-MAPPING-v1`

---

## 1. Purpose

Define deterministic checks that must pass before any cutover that treats PostgreSQL as Source of Truth for i-SEO Sales Manager.

This wave does **not** import production data.

---

## 2. Pre-import inventory (Sheets / export)

Record for each tab:

| Check | Method |
|-------|--------|
| Row counts | Export counts per tab (RAW, CLEAN, DEDUP, EVENTS, DELIVERIES, ACCESS, CONFIG, ERRORS, REMINDER_*) |
| Header fingerprint | Ordered header list hash |
| Export timestamp | Evidence note |

---

## 3. Post-load checks (PostgreSQL)

### 3.1 Counts

| Check | Pass rule |
|-------|-----------|
| `inbound_events` vs RAW unique `gmail_message_id` | Equal (± documented RAW empty/orphan exclusions) |
| `leads` vs unique CLEAN `lead_id` after collapse | Equal |
| Duplicate CLEAN rows collapsed | Report `dup_clean_rows_before` → `leads_after` |
| `lead_dedup_keys` vs DEDUP keys | ≥ message keys; contact keys reconciled |
| `access_rules` vs ACCESS principals | Equal active+revoked set |
| `errors` vs ERRORS rows (sanitized) | Within documented filter |

### 3.2 Uniqueness

| Check | Pass rule |
|-------|-----------|
| Unique `lead_id` | Zero duplicates in `leads` |
| Unique `(source_system, source_id)` | Zero duplicates in `inbound_events` |
| Unique `source_message_id` where present | Zero duplicates |
| Unique `dedup_key` | Zero duplicates |

### 3.3 Duplicate / quality analysis

- Distribution of `duplicate_status` (`new`/`reprocessed`/`repeat`/`possible`)
- Count of CLEAN rows sharing `source_message_id` before collapse
- Orphan DEDUP keys with missing lead

### 3.4 Lifecycle / status

- `manager_status` histogram
- Unknown status values → **blocker** unless mapped
- Terminal vs pending counts vs reminder selector expectations

### 3.5 NULL analysis

Critical fields: `lead_id`, `source_message_id`/`source_id`, `manager_status`, `created_at`  
Report NULL rates; block if `lead_id` or `manager_status` NULL > 0.

### 3.6 Timestamps

- Max/min `created_at` / `updated_at` / `received_at`
- Timezone sanity (all timestamptz)
- “Latest lead” sample matches Sheets export sample

### 3.7 Relationship integrity

- `leads.inbound_event_id` → inbound exists (or NULL with documented reason)
- `lead_events.lead_id` ⊆ `leads.lead_id`
- `lead_dedup_keys.lead_id` ⊆ `leads.lead_id`
- `deliveries.lead_id` ⊆ `leads.lead_id` when not null
- Active `access_rules` have role + principal_key

### 3.8 Access / moderator integrity

- Active recipients who should receive cards/reminders match operator roster
- Revoked never `is_active=true`
- No bot tokens in any column

### 3.9 Event counts

- `lead_events` count vs LEAD_EVENTS (after transform)
- Spot-check status_changed coverage for known moderator actions

### 3.10 Deterministic samples

Pick N fixed `lead_id`s (hash-selected): compare key fields Sheets vs PG.  
Record checksum of sorted `(lead_id, manager_status, source_message_id, updated_at)`.

### 3.11 Hash / checksum

| Object | Checksum |
|--------|----------|
| Sorted lead_id list | sha256 |
| Sorted gmail/source_id list | sha256 |
| Config keys set | sha256 of key list |

---

## 4. Hard cutover blockers

Any of the following **blocks** PG-primary cutover:

1. Duplicate `lead_id` remaining in `leads`
2. Duplicate Gmail `source_id` in `inbound_events`
3. Active access principal missing vs operator-approved roster
4. Secrets detected in tables (token patterns)
5. Sample field mismatches above agreed tolerance (default: **zero** on identity fields)
6. Reminder job semantics cannot reconstruct last successful window (if reminders still required)
7. Runtime role can DDL or can read/write `app_seo_content`
8. Migration ledger tip ≠ expected schema versions
9. Unmapped `manager_status` values in import
10. Missing backup/dump evidence for production apply window

---

## 5. Soft warnings (non-blocking with sign-off)

- CLEAN append duplicates collapsed with operator note
- Historical RAW lossy snippets vs full-body contract
- CONFIG keys classified “leave in vault” not imported
- Event type vocabulary gaps (unknown types stored as text)

---

## 6. Evidence artifact

Future import wave must file a report under `projects/mars-data-layer/reports/` with counts, checksums, blocker list, and git SHA of migrations applied.
