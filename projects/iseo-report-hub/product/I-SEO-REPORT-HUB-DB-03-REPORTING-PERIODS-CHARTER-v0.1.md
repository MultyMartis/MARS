# I-SEO Report Hub — DB-03 Reporting Periods Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no SQL created; no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub DB-03 Reporting Periods Migration Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md), [I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md](I-SEO-REPORT-HUB-MIGRATION-POLICY-v0.1.md), [I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-INITIAL-SCHEMA-PLAN-v0.1.md)

---

## 1. Purpose

Define the **DB-03 Reporting Periods** schema and migration boundaries so the next implementation wave can add a single `reporting_periods` table to local `iseo_report_hub_dev` without overbuilding report content storage.

DB-03 is the first **report-domain** table after auth + org baseline. It anchors monthly history per project and a period-level status workflow before weekly/final report entities and CRUD UI exist.

This charter is **documentation / policy only**. It does **not** authorize migration SQL, app edits, runtime sync, or DB mutation in this wave.

---

## 2. Current Baseline

### Auth implementation

| Item | Value |
|------|-------|
| Primary commit | `d4b3b2e2155f41e8f99d4ac56a47de870ea6b10c` — `feat(iseo-report-hub): add auth persistence bootstrap` |
| Hash-record follow-up | `0cd2cfb7735e59d3d54bf8dd9002ba45949dd47d` — `docs(iseo-report-hub): record auth persistence bootstrap commit hash` |
| Auth smoke | **PASS** (lint, DB, admin bootstrap, login/logout, health, 404, audit events) |
| Local admin | `admin@iseo-report-hub.test` (password/hash **not** recorded) |

### DB baseline (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| First migration | `2026_07_24_000001_create_core_tables.sql` |
| Applied checksum | `71dd22d0a0a0af14854b4b40d72ae611c80d74af8bfe038a413110b0be722bb4` |
| Migration count | **1** |
| Tables count | **9** |
| Users / roles | **1** / **6** |
| Clients / projects | **0** / **0** |
| `reporting_periods` | **Absent** (expected) |

### Existing tables

`schema_migrations`, `users`, `roles`, `user_roles`, `audit_log`, `clients`, `projects`, `sites`, `project_type_profiles`

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Scope

### In scope

- `reporting_periods` table design (fields, statuses, FKs, indexes, uniqueness, date rules)
- Migration plan filename, ledger/idempotency/rollback/smoke policy
- Period lifecycle and access model for future period management
- Implementation plan for the next apply wave
- OPERATIONAL-INDEX status update

### Out of scope (this wave and DB-03 migration itself)

- Report **content** tables (`weekly_checkpoints`, `monthly_reports`, blocks, KPI, evidence, snapshots)
- Period / report **CRUD UI**
- Client portal / `client_viewer` workflows
- Topvisor / API imports
- n8n reminders
- Production DB
- Migration SQL authoring (deferred to apply wave)
- App-source / runtime / DB mutation in this charter wave

**Refinement vs Initial Schema Plan v0.1:** that plan grouped `reporting_periods` + `weekly_checkpoints` + `monthly_reports` under “DB-03”. This charter **narrows DB-03 to `reporting_periods` only**. Weekly/final entities move to **DB-04+**.

---

## 4. Product Rules

1. A **reporting period** is a calendar-like **monthly** cycle for one project.
2. MVP product model (from product charter / report model):
   - 3 weekly checkpoint reports;
   - 1 final monthly report;
   - partial auto/manual data;
   - specialist drafts;
   - internal review;
   - client-facing final link/report later.
3. Ownership chain: **period → project → client**; **site → project**.
4. MVP needs **history by project and month** (`period_key` such as `2026-07`).
5. MVP should support a **period status workflow** before a full report editor exists.
6. Unique constraint: one period per **project + period_key**.
7. Period-level status tracks lifecycle; individual checkpoint/final entities are deferred.

---

## 5. Data Ownership

| Entity | Owner |
|--------|-------|
| `clients` | Org/customer record |
| `projects` | Belongs to client; access/scope unit |
| `sites` | Belongs to project |
| `reporting_periods` | Belongs to **project** (not client directly) |
| Future weekly/final rows | Belong to period (DB-04+) |

Actors on a period (nullable FKs until assigned):

| Field | Meaning |
|-------|---------|
| `owner_user_id` | Primary specialist / period owner |
| `reviewer_user_id` | Lead / reviewer for period close |
| `created_by` / `updated_by` | Audit of who created/last edited the period row |
| `finalized_at` | When period reached `finalized` (nullable until then) |

---

## 6. Access Model

### Why `client_viewer` is not used yet

- Auth already excludes `client_viewer` from internal dashboard gates.
- Client-facing delivery is planned via **published snapshots / token URLs**, not period-table CRUD.
- DB-03 does not introduce client portal period access.
- Role remains seeded for future boundary; **no** period management rights for `client_viewer` in DB-03/MVP internal tools.

### Internal roles (future period management)

| Role | Expected period capability (future UI; not in DB-03) |
|------|------------------------------------------------------|
| `admin_owner` | Full manage |
| `seo_lead_reviewer` | Manage / review / finalize |
| `seo_specialist` | Create/edit owned or assigned periods; drive weekly work |
| `account_client_manager` | Manage/coordinate periods for accounts (policy TBD in UI wave) |
| `internal_viewer` | **Read-only** |
| `client_viewer` | **Not** used for internal period management |

DB-03 migration creates **storage only**. Role enforcement remains application-layer in a later wave.

---

## 7. Migration Boundaries

| Boundary | Rule |
|----------|------|
| Target DB | Local `iseo_report_hub_dev` only |
| SoT file location | `app-source/database/migrations/` |
| Planned filename | `2026_07_25_000002_create_reporting_periods_table.sql` |
| Runner | Existing `tools/db-migrate.php` (`status` / `apply`) |
| Ledger | `schema_migrations` is authority |
| App code | **No** health/auth/CRUD code required in DB-03 apply unless a separate charter says otherwise |
| Seeds | **No** real client data; optional local fixture only if implementation charter approves |
| Empty projects | Migration may be validated **structurally** without inserting a period row |
| UI | Period CRUD **not** part of DB-03 |

Charter wave: **no** SQL file, **no** apply, **no** sync.

---

## 8. Validation Gates

Future apply wave must prove:

1. Migration **apply** succeeds once.
2. **Idempotent** re-run is a no-op (ledger present; checksum match).
3. Table `reporting_periods` exists with required columns.
4. Foreign keys to `projects` and `users` behave as designed.
5. Unique `(project_id, period_key)` refuses duplicates.
6. Optional smoke insert only with safe local fixture / existing project — **no** real client data.
7. Checksum mismatch → **STOP**.
8. `/health` may show migration/table count increment after implementation (no health code edit in charter wave).

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Overbuilding DB-03 with weekly/final tables | Explicit deferral to DB-04+ |
| Status set drift vs Report Lifecycle v0.1 granular states | DB-03 uses simplified period statuses; map in lifecycle doc |
| No project rows for FK smoke | Structural validation without insert; fixture only if chartered |
| Destructive rollback habit | Forward-only preferred; destructive DROP only empty table + explicit approval |
| Accidental production apply | Runner refuses non-`iseo_report_hub_dev` |
| Scope creep into CRUD UI | Separate UI charter required |

---

## 10. Next Implementation Wave

**Wave name:** `I-SEO Report Hub — DB-03 Reporting Periods Migration Apply 01`

See [I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-IMPLEMENTATION-PLAN-v0.1.md).

Allowed in that wave (when operator charters it): author migration SQL in `app-source`, sync SQL to runtime, apply to local DB, structural smoke, optional result docs — **not** production, **not** real client data, **not** destructive rollback by default.
