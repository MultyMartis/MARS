# I-SEO Report Hub — DB-04 Weekly Checkpoints Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no SQL created; no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints DB-04 Charter 01  
**Related:** [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md)

---

## 1. Purpose

Define the **DB-04 Weekly Checkpoints** data-model layer so the next implementation wave can add a single `weekly_checkpoints` table to local `iseo_report_hub_dev` without building a report editor or monthly content store.

DB-04 is the first **child report-domain** table under `reporting_periods`. It stores weekly status/checkpoint shells (and lightweight free-text progress fields) inside one reporting period.

This charter is **documentation / policy only**. It does **not** authorize migration SQL, app edits, runtime sync, fixture mutation, or DB mutation in this wave.

---

## 2. Current Baseline

### Reporting Period CRUD (dependency)

| Item | Value |
|------|-------|
| Primary commit | `392258fc572ac17b479618ba888b6b2ffe0feb68` — `feat(iseo-report-hub): add reporting period crud` |
| Hash-record follow-up | `f1d8a17e52fd7eb401b34cb3d044a061ebb6f5e7` — `docs(iseo-report-hub): record reporting period crud commit hash` |
| Surface | Internal list/detail/create/edit/archive-by-status; CSRF; no DELETE |
| Smoke period | `2026-08` archived (id **3**) |
| Fixture period | `2026-07` draft (id **1**) |

### Supporting baseline commits (context)

| Wave | Primary | Hash-record |
|------|---------|-------------|
| Auth persistence | `d4b3b2e2…` | `0cd2cfb7…` |
| DB-03 reporting_periods | `c19c29b8…` | `2f88d0ce…` |
| Local fixture apply | `348b4089…` | `7c543116…` |
| Reporting Period CRUD charter | `4e416d33…` | clarify `6b143852…` |

### DB baseline (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration count | **2** |
| Tables count | **10** |
| Users / roles | **1** / **6** |
| Clients / projects / sites | **1** / **1** / **1** |
| Reporting periods | **2** (`2026-07` draft, `2026-08` archived) |
| `weekly_checkpoints` | **Absent** (expected) |

### Current limitation

- Period shell CRUD exists.
- No weekly checkpoint DB model.
- No weekly checkpoint CRUD/UI.
- No monthly report content model.
- No report block editor / client portal / production deployment.

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Problem

Reporting periods exist as monthly shells, but the product model requires **weekly progress checkpoints** inside each period. Without a child table:

1. Weekly status cannot be stored in DB.
2. Period `status` remains a coarse rollup only.
3. Future weekly CRUD/UI has no schema target.
4. Demo/smoke for weekly workflow cannot be structural.

DB-04 closes the schema gap for weekly checkpoint rows only. It does **not** deliver the editor or monthly final content.

---

## 4. Scope

### In scope

- `weekly_checkpoints` table design (fields, statuses, FKs, indexes, uniqueness, date rules)
- Weekly checkpoint lifecycle (states, transitions, timestamps, no-delete policy)
- Validation / apply / smoke plan for the next migration wave
- OPERATIONAL-INDEX status update

### Out of scope

- Migration SQL authoring (deferred to apply wave)
- App-source / runtime / DB mutation in this charter wave
- Weekly checkpoint CRUD UI
- Monthly report content table / editor
- Report blocks, evidence/uploads, Topvisor metrics tables
- Automatic week generation UI/tool (deferred; apply wave may insert demo rows only)
- n8n reminders / client portal / production
- Real client data

**Refinement vs Initial Schema Plan v0.1:** that plan grouped `reporting_periods` + `weekly_checkpoints` + `monthly_reports` under “DB-03”, and placed blocks under “DB-04”. Programme reality after DB-03 charter:

- DB-03 = `reporting_periods` only (**done**)
- **DB-04 = `weekly_checkpoints` only** (this charter)
- Monthly report content = later **DB-05 or Report Content module**
- Blocks/KPI/evidence remain later phases

---

## 5. Product Model

1. A **reporting period** is a monthly (or reporting-interval) shell for one project.
2. A **weekly checkpoint** is one weekly status/progress row inside that period.
3. Typical month: **3 weekly checkpoints** + **1 monthly/final report step** (monthly content **not** in this table).
4. DB must allow a **flexible** number of weekly checkpoints (`week_index` 1–6), not hard-code exactly three.
5. Weekly content for MVP is **free-text** fields (`summary`, `work_done`, `findings`, `next_steps`, `risks`) — richer report blocks deferred.
6. Ownership: `weekly_checkpoint` → `reporting_period` → `project` → `client`.
7. Period status remains the **rollup**; checkpoint status is the child state machine.
8. Unique identities per period: `week_index` and `checkpoint_key` (e.g. `2026-07-W1`).

### Design resolutions

| Question | Decision |
|----------|----------|
| Must checkpoint dates fall inside parent period dates? | **Yes** — enforce in app/service validation first; DB CHECK cannot easily reference parent row |
| Allow `week_index` 4/5/6? | **Yes** — allow **1–6** for flexible calendar months |
| Free-text weekly content now? | **Yes** — simple TEXT fields for MVP |
| Auto-generate weeks in migration? | **No** — migration creates table only; generation tool/UI deferred |
| Seed demo weeks in migration? | **No** — no seed in migration; apply-wave smoke may insert 3 demo rows for fixture period `2026-07` |
| Monthly final content in this table? | **No** — deferred to later DB-05 / Report Content module |

---

## 6. Safety Boundary

| Boundary | Rule |
|----------|------|
| This wave | Docs only under allowlisted Active Brain paths |
| App-source | **No** edits |
| Runtime | **No** edits / **no** sync |
| DB | **No** mutation; optional read-only status only |
| SQL / migration files | **Not** created in this wave |
| Fixtures / period rows | **Unchanged** |
| Admin / password / hash | **Unchanged** |
| `.env` / `.env.local` | **Unchanged** |
| Real client data | **Forbidden** |
| Production | **Forbidden** |
| Foreign WIP | **Preserve** |
| Push | **No** |

---

## 7. Migration Boundary

Next apply wave (not this charter) may:

- Author **one** migration SQL file for `weekly_checkpoints`
- Sync that migration file only to Localhost runtime
- Run `db-migrate.php apply` against `iseo_report_hub_dev` @ `127.0.0.1`
- Optionally insert **local demo** weekly checkpoint smoke rows for fixture period `2026-07`
- Update result docs / OPERATIONAL-INDEX if chartered

Next apply wave must **not**:

- Add weekly checkpoint CRUD controllers/views
- Edit prior migrations (`000001`, `000002`)
- Mutate auth users/roles/passwords
- Insert real client data
- Create monthly report content schema (unless a separate explicit charter)

Planned migration filename:

`2026_07_26_000003_create_weekly_checkpoints_table.sql`

(Sequence `_000003` is authoritative; date prefix follows project convention / charter day.)

---

## 8. Validation Gates

Charter wave gates (this wave):

1. Preflight: root / `AI WS` / branch / empty staged / clean i-SEO WIP.
2. Docs created on allowlist only.
3. No app-source / runtime / DB / SQL changes.
4. Scoped docs commit; no push.

Future apply-wave gates (summary; detail in validation plan):

1. Migration count **2 → 3**; table count **10 → 11**.
2. Columns / indexes / FKs / CHECKs present.
3. Idempotent re-apply.
4. Demo W1/W2/W3 for `2026-07` (if smoke chartered).
5. Duplicate `week_index` / `checkpoint_key` rejected.
6. Invalid parent FK rejected.
7. Health/app regression (period CRUD still works; no secrets printed).

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Overbuilding weekly table into full report editor | Keep TEXT fields; defer blocks/evidence |
| Confusing DB-04 numbering vs Initial Schema Plan | Explicit refinement in this charter |
| Seeding real-looking client weeks | Local markers `LOCAL_FIXTURE_ONLY`; no production |
| Date range outside parent period | App/service validation; document as required |
| Deleting checkpoints / cascading period deletes | No DELETE in MVP; FK `ON DELETE RESTRICT` on period |
| Auto-generation complexity in migration | Table-only migration; generation deferred |

---

## 10. Next Implementation Wave

**One next action only:**

`I-SEO Report Hub — Weekly Checkpoints DB-04 Migration Apply 01`

That wave authors/applies migration `_000003`, validates structure, and may insert local demo weekly checkpoints for fixture period `2026-07`. It does **not** implement weekly checkpoint CRUD UI.
