# I-SEO Report Hub — DB-05 Monthly Report Content Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no SQL created; no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content DB-05 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md)

---

## 1. Purpose

Define the **DB-05 Monthly Report Content** data-model layer so the next implementation wave can add a single `monthly_report_contents` table to local `iseo_report_hub_dev` without building a block editor, export pipeline, or client portal.

DB-05 is the **monthly/final report working document** for one `reporting_period`. It sits above:

- `reporting_periods` (month/period shell);
- `weekly_checkpoints` (weekly internal progress snapshots).

This charter is **documentation / policy only**. It does **not** authorize migration SQL, app edits, runtime sync, fixture mutation, or DB mutation in this wave.

---

## 2. Current Baseline

### Weekly Checkpoints CRUD (primary dependency)

| Item | Value |
|------|-------|
| Primary commit | `911db07d8ca51bb1778c53ca570ef3b8950234a0` — `feat(iseo-report-hub): add weekly checkpoints crud` |
| Hash-record | `64c42cbe6616be19b6d8ea3340466e7bab1f7bf9` — `docs(iseo-report-hub): record weekly checkpoints crud commit hash` |
| Clarify commits | `6f968ed2` / `865cd4b5` |
| Expected HEAD at charter start | `865cd4b50a31e1605bf45ffa3256dc48499eedca` |
| Surface | Period-scoped list/create; flat detail/edit; skip/archive-by-status; auth + CSRF; **no DELETE** |
| Smoke | W4 id **7** `2026-07-W4` → `skipped`; W1–W3 preserved |

### DB-04 Weekly Checkpoints migration apply

| Item | Value |
|------|-------|
| Primary commit | `f7a26aa354635c90c6f6e040583c241c7800a7dd` — `feat(iseo-report-hub): add weekly checkpoints migration` |
| Hash-record | `228965d73f918abd0b4013481b96d743c88fd602` |
| Clarify | `e18c537d65c4c8c6ba2767201bccaad7248287c4` |
| Migration | `2026_07_26_000003_create_weekly_checkpoints_table.sql` |
| Checksum (SHA-256) | `8ab9c0e84a262ab9c8662cd502ab18943810dc6a034d2cd25a89935e2ddaacd3` |
| Batch | **3** |

### Supporting baseline commits (context)

| Wave | Primary | Hash-record |
|------|---------|-------------|
| Auth persistence | `d4b3b2e2…` | `0cd2cfb7…` |
| Reporting Period CRUD | `392258fc…` | `f1d8a17e…` |
| Weekly Checkpoints CRUD charter | `3a0569a5…` | `befeb9d0…` (+ clarify `7ae0ba79…`) |

### DB baseline (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration count | **3** |
| Tables count | **11** |
| Users / roles | **1** / **6** |
| Clients / projects / sites | **1** / **1** / **1** |
| Reporting periods | **2** (`2026-07` draft id **1**; `2026-08` archived id **3**) |
| Weekly checkpoints | **4** |
| `monthly_report_contents` | **Absent** (expected) |

### Current weekly checkpoint data (under period `2026-07`)

| Id | Key | Status | Marker |
|----|-----|--------|--------|
| 1 | `2026-07-W1` | `completed` | `LOCAL_FIXTURE_ONLY` |
| 2 | `2026-07-W2` | `reviewed` | `LOCAL_FIXTURE_ONLY` |
| 3 | `2026-07-W3` | `draft` | `LOCAL_FIXTURE_ONLY` |
| 7 | `2026-07-W4` | `skipped` | `LOCAL_FIXTURE_ONLY` |

### Current limitation

- Period shell CRUD exists.
- Weekly checkpoint CRUD exists.
- **No** monthly report content DB model / row.
- **No** monthly report editor / report block editor.
- **No** Topvisor / API metrics tables.
- **No** export / public share / client portal.

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Problem

Reporting periods and weekly checkpoints exist, but there is **no monthly report content model**. Without it:

1. The final/monthly working document cannot be stored in DB.
2. Structured executive narrative has no schema target.
3. Future monthly CRUD/UI has nothing to bind to.
4. Source weekly checkpoint linkage (even as a soft snapshot hint) cannot be recorded.
5. Review/finalize workflow for the monthly deliverable has no row lifecycle.

DB-05 closes the schema gap for **one structured monthly content row per reporting period**. It does **not** deliver the editor, block model, export, or client portal.

---

## 4. Scope

### In scope

- `monthly_report_contents` table design (fields, statuses, FKs, indexes, uniqueness, JSON hint policy)
- Relation to `reporting_periods` (1:0..1) and soft relation to `weekly_checkpoints` (JSON snapshot ids)
- Monthly report lifecycle (draft → review → finalized / archived)
- Constraints / validation / apply / smoke plan for the next migration wave
- OPERATIONAL-INDEX status update

### Out of scope

- Migration SQL authoring (deferred to apply wave)
- App-source / runtime / DB mutation in this charter wave
- Monthly report CRUD UI / routes / controllers / views
- Report block editor / block tables
- PDF / export / public share
- Client portal
- Topvisor / API integration
- Evidence / uploads
- n8n reminder automation
- Real client data / production

**Refinement vs Initial Schema Plan v0.1:** that plan grouped monthly under “DB-03” and used later “DB-05” for evidence/snapshots. Programme reality after DB-03/DB-04:

- DB-03 = `reporting_periods` only (**done**)
- DB-04 = `weekly_checkpoints` only (**done**)
- **DB-05 = `monthly_report_contents` only** (this charter)
- Blocks / evidence / publish snapshots remain later phases (DB-06+ or module charters)

---

## 5. Product Model

1. A **reporting period** is the monthly (or reporting-interval) shell for one project.
2. **Weekly checkpoints** are internal weekly progress snapshots under that period.
3. **Monthly report content** is the final/monthly working document for that period — at most **one** row per period in MVP.
4. MVP content is **structured TEXT fields** (executive summary, work completed, results, findings, risks, next month plan, client/internal notes) — **not** a block editor.
5. `source_weekly_checkpoint_ids` is an optional **JSON array of checkpoint ids** as a soft snapshot hint; normalized join table is deferred.
6. Ownership: `monthly_report_content` → `reporting_period` → `project` → `client`.
7. Monthly content status is **independent** of period status at DB level; future service may propose rollup — **no** DB auto-update of `reporting_periods.status`.
8. Finalized content is **read-only** except `admin_owner` reopen/archive (app policy later).
9. Content is **internal-only** in MVP — no public/client view now.

### Design resolutions

| Question | Decision |
|----------|----------|
| One row per reporting period? | **Yes** — `UNIQUE (reporting_period_id)` |
| Structured text vs block table? | **Structured text now**; blocks deferred to DB-06 / editor module |
| Normalized weekly source join? | **No for MVP** — JSON id list as snapshot hint |
| Auto-update period status from monthly status? | **No** at DB level; future service-level only |
| Finalized locks edits? | **Yes** — read-only except `admin_owner` reopen/archive |
| Public/client view now? | **No** — internal content model only |
| Seed rows in migration? | **No** — apply-wave demo smoke may insert one local row |

---

## 6. Safety Boundary

| Boundary | Rule |
|----------|------|
| This wave | Docs only under allowlisted Active Brain paths |
| App-source | **No** edits |
| Runtime | **No** edits / **no** sync |
| DB | **No** mutation; optional read-only status only |
| SQL / migration files | **Not** created in this wave |
| Monthly / weekly / period rows | **Unchanged** |
| Admin / password / hash | **Unchanged** |
| `.env` / `.env.local` | **Unchanged** |
| Real client data | **Forbidden** |
| Production | **Forbidden** |
| Foreign WIP | **Preserve** |
| Push | **No** |

---

## 7. Migration Boundary

Next apply wave (not this charter) may:

- Author **one** migration SQL file for `monthly_report_contents`
- Sync that migration file only to Localhost runtime
- Run `db-migrate.php apply` against `iseo_report_hub_dev` @ `127.0.0.1`
- Optionally insert **one** local demo monthly report content row for fixture period `2026-07`
- Update result docs / OPERATIONAL-INDEX if chartered

Next apply wave must **not**:

- Add monthly report CRUD controllers/views
- Edit prior migrations (`000001`–`000003`)
- Mutate auth users/roles/passwords
- Insert real client data
- Create report block / evidence / publish schema unless separately chartered

Planned migration filename:

`2026_07_26_000004_create_monthly_report_contents_table.sql`

(Sequence `_000004` is authoritative; date prefix follows project convention / charter day.)

---

## 8. Validation Gates

Charter wave gates (this wave):

1. Preflight: root / `AI WS` / branch / empty staged / clean i-SEO WIP.
2. Docs created on allowlist only.
3. No app-source / runtime / DB / SQL changes.
4. Scoped docs commit; no push.

Future apply-wave gates (summary; detail in validation plan):

1. Migration count **3 → 4**; table count **11 → 12**.
2. Columns / indexes / FKs / CHECKs present.
3. Idempotent re-apply.
4. Demo monthly row for `2026-07` (if smoke chartered).
5. Duplicate `reporting_period_id` rejected.
6. Invalid parent FK rejected.
7. Invalid status rejected.
8. JSON validity verified if CHECK/type supports it safely.
9. Health/app regression (period + weekly CRUD still work; no secrets printed).

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Overbuilding into block editor / publish stack | Keep structured TEXT; defer blocks/export/portal |
| Confusing DB-05 numbering vs Initial Schema Plan | Explicit refinement in this charter |
| Treating JSON weekly ids as hard FK | Document as soft hint; no FK cascade; resolve dynamically in smoke |
| Auto-coupling monthly status to period status | Forbid DB triggers; service-level later only |
| Seeding real-looking client monthly narrative | `LOCAL_FIXTURE_ONLY` markers; no production |
| Hard DELETE of monthly content | No DELETE in MVP; archive instead |
| Cascading period deletes wiping monthly history | FK `ON DELETE RESTRICT` |

---

## 10. Next Implementation Wave

**One next action only:**

`I-SEO Report Hub — Monthly Report Content DB-05 Migration Apply 01`

That wave authors/applies migration `_000004`, validates structure, and may insert one local demo monthly report content row for fixture period `2026-07`. It does **not** implement monthly report CRUD UI.
