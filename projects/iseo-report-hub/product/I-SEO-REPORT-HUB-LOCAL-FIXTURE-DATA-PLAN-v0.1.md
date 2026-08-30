# I-SEO Report Hub — Local Fixture Data Plan v0.1

**Status:** PLANNING ONLY — no rows created; no SQL authored in this wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Project/Client Local Fixture Charter 01  
**Related:** [I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md)  
**Schema authority (read-only):** `app-source/database/migrations/2026_07_24_000001_create_core_tables.sql`, `app-source/database/migrations/2026_07_25_000002_create_reporting_periods_table.sql`

---

## 1. Target tables

| Table | Fixture action (next apply wave) | Required? |
|-------|----------------------------------|-----------|
| `clients` | Insert **1** demo client | **Yes** |
| `projects` | Insert **1** demo project | **Yes** |
| `sites` | Insert **1** demo site | **Yes** (completes org chain; not FK for periods) |
| `reporting_periods` | Insert **1** demo period | **Yes** (preferred for FK/unique smoke in same wave) |
| `project_type_profiles` | Optional 1 profile row | Optional |
| `audit_log` | Optional fixture event | Optional |
| `users` / `roles` / `user_roles` | Reuse existing local admin | **No create** |
| `schema_migrations` | Untouched | **No** |

---

## 2. Planned demo client fields

Source columns (confirmed in first migration):

| Column | Planned value | Notes |
|--------|---------------|-------|
| `name` | `Demo Client` | Explicitly fake |
| `slug` | `demo-client` | Unique; idempotency key |
| `status` | `active` | ENUM default also `active` |
| `notes` | `LOCAL_FIXTURE_ONLY` | Primary fixture marker for client |
| `id` / timestamps | DB-generated | Do not hardcode IDs in docs |

Forbidden: real company names, phones, emails, contracts, credential notes.

---

## 3. Planned demo project fields

Source columns (confirmed):

| Column | Planned value | Notes |
|--------|---------------|-------|
| `client_id` | ID of demo client | FK required |
| `name` | `Demo SEO Project` | Explicitly fake |
| `slug` | `demo-seo-project` | Unique per client; idempotency key with `client_id` |
| `project_type` | `service_corporate` | Safe default ENUM present in schema |
| `status` | `active` | |
| `notes` | **N/A** | **Column does not exist** on `projects` |

Fixture marking for projects without `notes`:

- Stable slug `demo-seo-project`
- Parent client `notes = LOCAL_FIXTURE_ONLY`
- Optional `project_type_profiles.settings_json` marker (if profile row created)

---

## 4. Planned demo site fields

Source columns (confirmed):

| Column | Planned value | Notes |
|--------|---------------|-------|
| `project_id` | ID of demo project | FK required |
| `url` | `https://demo.example.test` or host-only `demo.example.test` | Prefer reserved/example-style; **no real client domain** |
| `label` | `LOCAL_FIXTURE_ONLY` | Fixture marker |
| `is_primary` | `1` | Single site |

**SAFE UNKNOWN:** exact preferred string format for `url` (with vs without scheme) until apply wave inspects any app validators — schema is `VARCHAR(255) NOT NULL` only.

Forbidden: real i-SEO client domains, production URLs, login URLs with secrets.

---

## 5. Planned demo reporting_period fields

Source columns (confirmed in DB-03 migration):

| Column | Planned value | Notes |
|--------|---------------|-------|
| `project_id` | ID of demo project | FK → `projects` RESTRICT |
| `period_key` | `2026-07` | CHAR(7); unique with project |
| `period_start` | `2026-07-01` | Must be ≤ end |
| `period_end` | `2026-07-31` | |
| `status` | `draft` | Allowed by CHECK |
| `title` | `Demo July 2026` | Fake |
| `summary` | `LOCAL_FIXTURE_ONLY` | Fixture marker; no report content |
| `owner_user_id` | Local admin user id if resolvable | Optional; SET NULL FK |
| `created_by` | Local admin user id if resolvable | Optional |
| `reviewer_user_id` | NULL | |
| `updated_by` | NULL | |
| `finalized_at` | NULL | |

No weekly/monthly content rows. No published snapshots.

---

## 6. Idempotency keys

| Entity | Lookup key | Re-run behavior |
|--------|------------|-----------------|
| Client | `slug = demo-client` | Reuse existing row; do not insert duplicate |
| Project | `(client_id, slug = demo-seo-project)` | Reuse |
| Site | Prefer `(project_id + is_primary = 1)` or `(project_id + url)` | Reuse; do not multiply primary sites |
| Reporting period | `(project_id, period_key = 2026-07)` | Reuse; second insert must fail unique if forced |

Tool must print whether each entity was **created** vs **already present**.

---

## 7. How to mark local fixture only

| Location | Marker |
|----------|--------|
| `clients.notes` | Exact text `LOCAL_FIXTURE_ONLY` (or contains that token) |
| `sites.label` | `LOCAL_FIXTURE_ONLY` |
| `reporting_periods.summary` | `LOCAL_FIXTURE_ONLY` |
| Project | No notes column — rely on slug + parent client marker; optional profile JSON |
| Audit metadata (optional) | `{"fixture":true,"marker":"LOCAL_FIXTURE_ONLY"}` |

Future cleanup may delete **only** rows matching these markers / demo slugs. Never TRUNCATE whole tables.

---

## 8. What real data is forbidden

- Real i-SEO client / company names
- Real project titles from production portfolio
- Real domains / production site URLs
- Contacts, phones, emails of real people
- Credentials, API keys, Topvisor tokens
- Copied report content from Storage corpus
- Any production DB target

---

## 9. Dependency on current table columns

Confirmed from migrations (this charter wave):

| Table | Relevant facts |
|-------|----------------|
| `clients` | Has `slug` UNIQUE, `notes` TEXT, `status` ENUM |
| `projects` | Has `slug` unique per `client_id`; **no** `notes`; has `project_type` ENUM |
| `sites` | Has `url`, `label`, `is_primary`; **no** unique on url |
| `reporting_periods` | Unique `(project_id, period_key)`; FK to `projects` RESTRICT; user FKs SET NULL |
| `project_type_profiles` | Optional; unique `(project_id, profile_code)` |

**SAFE UNKNOWN:**

- Whether apply wave will also create a `project_type_profiles` row (optional; not required for period FK).
- Exact local admin numeric `id` until apply wave reads it (do not hardcode in charter).
- Whether future cleanup tool is CLI sibling vs separate charter.

---

## 10. Recommended row set for next apply wave

| # | Entity | Identity |
|---|--------|----------|
| 1 | Client | `Demo Client` / `demo-client` |
| 2 | Project | `Demo SEO Project` / `demo-seo-project` |
| 3 | Site | `demo.example.test` |
| 4 | Reporting period | `2026-07` / `Demo July 2026` / `draft` |

Target post counts: **clients 1 / projects 1 / sites 1 / reporting_periods 1** (unless period insert is explicitly deferred and documented in apply report).
