# I-SEO Report Hub — Monthly Report Content CRUD Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-MIGRATION-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-RESULT-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый управляемый CRUD/editor-слой** для `monthly_report_contents` на локальном MVP после:

- DB-backed auth baseline;
- Reporting Period CRUD Implementation 01;
- Weekly Checkpoints CRUD Implementation 01;
- DB-05 `monthly_report_contents` migration apply + local demo monthly row for `2026-07`.

Цель charter:

1. Зафиксировать текущий baseline после DB-05 apply.
2. Спроектировать MVP internal CRUD (period-scoped create-if-missing / detail / edit / status lifecycle).
3. Определить routes / controller / service / repository / views / nav и связь с `reporting_periods` + `weekly_checkpoints`.
4. Определить status workflow, field locks, validation, role access.
5. Подготовить smoke/validation plan для следующей implementation wave.
6. Явно исключить report blocks / PDF-export / Topvisor / client portal / DELETE.
7. Не менять app-source / runtime / DB в этой волне.

Эта волна — **documentation / policy only**. CRUD **не** кодируется здесь.

---

## 2. Current Baseline

### Auth implementation

| Item | Value |
|------|-------|
| Primary commit | `d4b3b2e2155f41e8f99d4ac56a47de870ea6b10c` — `feat(iseo-report-hub): add auth persistence bootstrap` |
| Hash-record | `0cd2cfb7735e59d3d54bf8dd9002ba45949dd47d` |
| Users / roles | **1** / **6** |
| Local admin | `admin@iseo-report-hub.test` / `admin_owner` (password/hash **not** recorded) |

### Reporting Period CRUD

| Item | Value |
|------|-------|
| Primary commit | `392258fc572ac17b479618ba888b6b2ffe0feb68` — `feat(iseo-report-hub): add reporting period crud` |
| Hash-record | `f1d8a17e52fd7eb401b34cb3d044a061ebb6f5e7` |
| Surface | list/detail/create/edit/archive-by-status; auth + CSRF; no DELETE |
| Periods | `2026-07` id **1** draft fixture; `2026-08` id **3** archived smoke |

### Weekly Checkpoints CRUD

| Item | Value |
|------|-------|
| Primary commit | `911db07d8ca51bb1778c53ca570ef3b8950234a0` — `feat(iseo-report-hub): add weekly checkpoints crud` |
| Hash-record | `64c42cbe6616be19b6d8ea3340466e7bab1f7bf9` |
| Clarify | `6f968ed2` / `865cd4b5` |
| Surface | period-scoped list/create; flat detail/edit; skip/archive-by-status; auth + CSRF; no DELETE |
| Checkpoints | W1 id **1** completed; W2 id **2** reviewed; W3 id **3** draft; W4 id **7** skipped — all `LOCAL_FIXTURE_ONLY` |

### DB-05 Monthly Report Content migration apply

| Item | Value |
|------|-------|
| Primary commit | `aac9c18ef49fc3b715106882893e18e280176800` — `feat(iseo-report-hub): add monthly report content migration` |
| Hash-record | `32674ea911ce9fd8740b329db114b87eb65a9389` |
| Migration | `2026_07_26_000004_create_monthly_report_contents_table.sql` |
| Checksum (SHA-256) | `91f367cdf73d1a4b1fcfa3175f190c0470cda86e5cd5706749e2d566c82430b8` |
| Batch | **4** |
| Validation | FK / unique / CHECK / JSON expected failures + rollback; Reporting Period + Weekly Checkpoint CRUD regression PASS |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migrations | **4** |
| Tables | **12** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **4** |
| monthly_report_contents | **1** |

### Demo monthly report content

| Field | Value |
|-------|-------|
| Id | **1** |
| Parent period | id **1** / `2026-07` / draft |
| Status | `draft` |
| Title | `Demo Monthly Report — July 2026 — LOCAL_FIXTURE_ONLY` |
| Text fields | all `LOCAL_FIXTURE_ONLY` |
| `source_weekly_checkpoint_ids` | `[1, 2, 3, 7]` (W1–W4) |
| owner / created_by / updated_by | admin id **1** |

### Current limitation

- **No** monthly report content CRUD / UI / routes / controller / service / repository.
- **No** monthly report editor beyond future CRUD form in next wave.
- **No** report block editor / PDF / export.
- **No** Topvisor / API integration.
- **No** client portal / public share.
- Parent reporting period detail does **not** yet embed a monthly report section.

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Scope

### In scope

- Internal monthly report content **detail / create-if-missing / edit**
- Period-scoped entry: `/reporting-periods/{period_id}/monthly-report`
- Status lifecycle via edit form (no hard DELETE)
- Auth required on all CRUD routes; CSRF on all POST
- Role-aware create/edit/status boundaries (MVP matrix)
- Source weekly checkpoint selection/reference (`source_weekly_checkpoint_ids`)
- Validation for parent period uniqueness, status transitions, source ids, text lengths, owners
- Optional audit events for create/update/status/reviewed/finalized/archived
- Navigation: period detail → monthly report section (status/title/link or create)
- Local fixture smoke using period `2026-07` + existing monthly id **1** + W1–W4 sources
- Design + implementation + validation plans for next wave

### Out of scope

- Report content blocks / block editor (future DB-06+)
- PDF / export / public share
- Topvisor / API imports / n8n reminders / evidence uploads
- Client portal / `client_viewer` access
- Hard DELETE / bulk actions
- Schema / migration changes
- Real client data
- Production deployment

---

## 4. Product Rules

1. Monthly report content is a **child** of one `reporting_periods` row (`ON DELETE RESTRICT`); **at most one** row per period (`uniq_monthly_report_contents_period`).
2. UX is an **internal editor**, not a generic multi-row CRUD index: create usually means “create/get monthly report for period”.
3. Status lifecycle follows [MONTHLY-REPORT-LIFECYCLE-v0.1](I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md).
4. Soft retire via `archived` only — **no DELETE** route/UI in MVP. Archiving does **not** free the unique period slot.
5. Parent period `archived` / `finalized` blocks create/edit for non-`admin_owner`.
6. Field locks: `reporting_period_id` immutable; title/content/`source_weekly_checkpoint_ids` editable until `finalized` unless `admin_owner`.
7. `source_weekly_checkpoint_ids` must reference checkpoints that exist and belong to the same period; empty array allowed with warning / “no sources” marker.
8. Smoke / demo rows must carry `LOCAL_FIXTURE_ONLY` markers; no real client data.
9. Reuse existing i-SEO Report Hub internal UI patterns (Reporting Period + Weekly Checkpoint CRUD style); no CDN.
10. MVP does **not** auto-rollup parent `reporting_periods.status` or mutate weekly checkpoint rows from monthly edits.

---

## 5. Access Model

| Role | Detail / preview | Create / edit draft–in_progress | ready_for_review | reviewed / finalized | archived | Reopen finalized |
|------|------------------|----------------------------------|------------------|----------------------|----------|------------------|
| `admin_owner` | Yes | Yes | Yes | Yes | Yes | Yes |
| `seo_lead_reviewer` | Yes | Yes | Yes | Yes | Yes | No (admin only) |
| `seo_specialist` | Yes | Yes | Yes (submit) | No | No | No |
| `account_client_manager` | Read-only | No | No | No | No | No |
| `internal_viewer` | Read-only | No | No | No | No | No |
| `client_viewer` | **No** | No | No | No | No | No |

Unauthenticated → redirect `/login`.

Current smoke may only have `admin_owner`. Multi-role HTTP denial paths may be **policy covered / not multi-user smoked**.

---

## 6. Data Policy

| Rule | Policy |
|------|--------|
| Parent period for smoke | `2026-07` (id **1**) |
| Existing monthly row | Prefer edit id **1**; do **not** create a second row for `2026-07` except duplicate-guard attempt that fails |
| Source checkpoints | Prefer resolve by key `2026-07-W1`…`W4`; known ids `[1,2,3,7]` |
| Create-if-missing smoke | Prefer existing row path; optional second period only if safe and documented (`2026-08` is archived — treat carefully / prefer admin-only or skip) |
| Real client data | **Forbidden** |
| Schema changes | **Forbidden** in CRUD implementation wave |
| Credentials in docs | **Forbidden** |

---

## 7. Implementation Boundary

This charter wave:

- **May** create/update Active Brain product docs + OPERATIONAL-INDEX + closeout REPORT.
- **Must not** edit `app-source/**`, Localhost runtime, SQL/migrations, fixtures, env, users/passwords.
- **Must not** mutate `monthly_report_contents`, `weekly_checkpoints`, or `reporting_periods` rows.
- **Must not** push / fetch / pull / reset / clean / stash / broad git add.

Next wave implements CRUD per design + implementation plan under a separate operator charter.

---

## 8. Validation Gates

Before declaring next-wave implementation complete (summary; detail in validation plan):

1. Preflight: root / volume / branch / DB target / DB-05 baseline intact.
2. Route smoke: period monthly detail, create-if-missing, flat detail/edit; unauth redirect.
3. Form/CSRF smoke: POST rejected without valid CSRF.
4. DB edit/status smoke on monthly id **1**; duplicate create for `2026-07` refused.
5. Source weekly checkpoint validation (invalid ids / wrong period refused); source links shown.
6. Parent reporting period show embeds monthly report section.
7. Audit events present if implemented.
8. Regression: reporting period CRUD, weekly checkpoint CRUD, `/login`, `/health`, `/not-existing`.
9. No DELETE route/UI; no real client data; no schema change.

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Nested period path + flat `/monthly-reports/{id}` confuse Router exact-match | Mirror Weekly Checkpoint pattern: static segments before dynamic id; request-time exact-path registration |
| Duplicate create against unique period constraint | Create-if-missing UX + service uniqueness guard + friendly error on 1062 |
| Editing finalized content by non-admin | Field/status locks in service; admin_owner reopen only |
| Parent archived (`2026-08`) create smoke side-effects | Prefer smoke on `2026-07` existing row; document if archived period used |
| Invalid / cross-period source checkpoint ids | Service validates existence + same `reporting_period_id` |
| Multi-role matrix untested (one admin user) | Document SAFE SIMPLIFICATION / deferred multi-user smoke |
| Status transition graph only app-enforced | Align service with lifecycle doc; DB CHECK only values |
| Over-scope into report blocks / PDF / portal | Hard out-of-scope list; STOP if charter expands |

---

## 10. Next Implementation Wave

**`I-SEO Report Hub — Monthly Report Content CRUD Implementation 01`**

Implement internal monthly report content CRUD/editor over existing DB-05 table using Model A source → runtime sync, local fixture period `2026-07`, and monthly demo id **1** (+ W1–W4 source references) — without report blocks, PDF/export, client portal, schema changes, or hard delete.

See:

- [DESIGN-v0.1](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md)
- [IMPLEMENTATION-PLAN-v0.1](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md)
- [VALIDATION-PLAN-v0.1](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-VALIDATION-PLAN-v0.1.md)
