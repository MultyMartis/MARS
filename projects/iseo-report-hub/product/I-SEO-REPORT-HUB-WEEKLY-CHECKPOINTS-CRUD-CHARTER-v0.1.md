# I-SEO Report Hub — Weekly Checkpoints CRUD Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-MIGRATION-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый управляемый CRUD-слой** для `weekly_checkpoints` на локальном MVP после:

- DB-backed auth baseline;
- Reporting Period CRUD Implementation 01;
- DB-04 `weekly_checkpoints` migration apply + local W1–W3 smoke.

Цель charter:

1. Зафиксировать текущий baseline после DB-04 apply.
2. Спроектировать MVP internal CRUD (list / detail / create / edit / archive-or-skip-by-status).
3. Определить routes / controller / service / repository / views / nav и связь с `reporting_periods`.
4. Определить status workflow, field locks, validation, role access.
5. Подготовить smoke/validation plan для следующей implementation wave.
6. Явно исключить monthly editor / report blocks / Topvisor / client portal / DELETE.
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

### DB-04 Weekly Checkpoints migration apply

| Item | Value |
|------|-------|
| Primary commit | `f7a26aa354635c90c6f6e040583c241c7800a7dd` — `feat(iseo-report-hub): add weekly checkpoints migration` |
| Hash-record | `228965d73f918abd0b4013481b96d743c88fd602` |
| Clarify | `e18c537d65c4c8c6ba2767201bccaad7248287c4` |
| Migration | `2026_07_26_000003_create_weekly_checkpoints_table.sql` |
| Checksum (SHA-256) | `8ab9c0e84a262ab9c8662cd502ab18943810dc6a034d2cd25a89935e2ddaacd3` |
| Batch | **3** |
| Validation | FK / unique / CHECK expected failures + rollback; Reporting Period CRUD regression PASS |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migrations | **3** |
| Tables | **11** |
| users / roles | **1** / **6** |
| clients / projects / sites | **1** / **1** / **1** |
| reporting_periods | **2** |
| weekly_checkpoints | **3** |

### Demo weekly checkpoints (under period `2026-07`)

| Id | Key | Status | Marker |
|----|-----|--------|--------|
| 1 | `2026-07-W1` | `completed` | `LOCAL_FIXTURE_ONLY` |
| 2 | `2026-07-W2` | `reviewed` | `LOCAL_FIXTURE_ONLY` |
| 3 | `2026-07-W3` | `draft` | `LOCAL_FIXTURE_ONLY` |

### Current limitation

- **No** weekly checkpoint CRUD / UI / routes / controller / service / repository.
- **No** monthly report content model / report block editor.
- **No** Topvisor / API integration.
- **No** client portal.
- Parent reporting period detail does **not** yet embed a weekly checkpoint section.

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Scope

### In scope

- Internal weekly checkpoint **list / detail / create / edit**
- Nested list/create under reporting period context
- Archive / skip via status (`archived` / `skipped`) — **no** hard DELETE
- Auth required on all CRUD routes; CSRF on all POST
- Role-aware create/edit/status boundaries (MVP matrix)
- Validation for parent period, week_index, checkpoint_key, dates, uniqueness, owners
- Optional audit events for create/update/status/reviewed/completed
- Navigation: period detail → checkpoints list/create; checkpoint detail → parent period
- Local fixture smoke using period `2026-07` + existing W1–W3; optional create W4
- Design + implementation + validation plans for next wave

### Out of scope

- Monthly report content editor
- Report content blocks / evidence uploads
- Topvisor / API imports / n8n reminders
- Client portal / `client_viewer` access
- Hard DELETE / bulk actions
- Schema / migration changes
- Real client data
- Production deployment

---

## 4. Product Rules

1. Weekly checkpoint is a **child** of one `reporting_periods` row (`ON DELETE RESTRICT`).
2. Prefer **3** weekly checkpoints per month; schema allows week_index **1–6** for calendar flexibility.
3. `checkpoint_key` format: `YYYY-MM-WN` (example `2026-07-W1`); period part must match parent `period_key`.
4. Status lifecycle follows [WEEKLY-CHECKPOINT-LIFECYCLE-v0.1](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md).
5. Soft retire via `skipped` / `archived` only — **no DELETE** route/UI in MVP.
6. Parent period `archived` / `finalized` blocks create/edit for non-`admin_owner`.
7. Field locks: `reporting_period_id` immutable; `week_index` / `checkpoint_key` editable only while `draft`; dates while `draft` / `in_progress`.
8. Text fields editable until `completed` unless `admin_owner`.
9. Smoke / demo rows must carry `LOCAL_FIXTURE_ONLY` markers; no real client data.
10. Reuse existing i-SEO Report Hub internal UI patterns (Reporting Period CRUD style); no CDN.

---

## 5. Access Model

| Role | List / detail | Create / edit draft–in_progress | ready_for_review | reviewed / completed | skipped / archived | Reopen reviewed/completed |
|------|---------------|----------------------------------|------------------|----------------------|--------------------|---------------------------|
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
| Existing rows | Prefer keep W1/W2/W3 intact |
| Create smoke | Optional W4 `2026-07-W4` with `LOCAL_FIXTURE_ONLY` |
| Edit smoke | Prefer W4; if W3 used, document final status |
| Real client data | **Forbidden** |
| Schema changes | **Forbidden** in CRUD implementation wave |
| Credentials in docs | **Forbidden** |

---

## 7. Implementation Boundary

This charter wave:

- **May** create/update Active Brain product docs + OPERATIONAL-INDEX + closeout REPORT.
- **Must not** edit `app-source/**`, Localhost runtime, SQL/migrations, fixtures, env, users/passwords.
- **Must not** mutate `weekly_checkpoints` or `reporting_periods` rows.
- **Must not** push / fetch / pull / reset / clean / stash / broad git add.

Next wave implements CRUD per design + implementation plan under a separate operator charter.

---

## 8. Validation Gates

Before declaring next-wave implementation complete (summary; detail in validation plan):

1. Preflight: root / volume / branch / DB target / DB-04 baseline intact.
2. Route smoke: nested list, detail, create/edit forms; unauth redirect.
3. Form/CSRF smoke: POST rejected without valid CSRF.
4. DB create W4 / edit / skipped-or-archived smoke; uniqueness refusal.
5. Parent period show embeds or links checkpoint section.
6. Audit events present if implemented.
7. Regression: reporting period CRUD, `/login`, `/health`, `/not-existing`.
8. No DELETE route/UI; no real client data; no schema change.

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Nested + flat routes confuse Router exact-match registration | Mirror Reporting Period pattern: static paths before dynamic id; request-time exact-path registration |
| Editing locked W1 (`completed`) / W2 (`reviewed`) by mistake | Prefer smoke on W4; enforce field/status locks in service |
| Parent archived/finalized still editable | Service gate for non-admin |
| Multi-role matrix untested (one admin user) | Document SAFE SIMPLIFICATION / deferred multi-user smoke |
| Status transition graph only app-enforced | Align service with lifecycle doc; DB CHECK only values |
| Over-scope into monthly content | Hard out-of-scope list; STOP if charter expands |

---

## 10. Next Implementation Wave

**`I-SEO Report Hub — Weekly Checkpoints CRUD Implementation 01`**

Implement internal weekly checkpoint CRUD over existing DB-04 table using Model A source → runtime sync, local fixture period `2026-07`, and W1–W3 (+ optional W4) smoke — without monthly editor, report blocks, client portal, schema changes, or hard delete.

See:

- [DESIGN-v0.1](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md)
- [IMPLEMENTATION-PLAN-v0.1](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md)
- [VALIDATION-PLAN-v0.1](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-VALIDATION-PLAN-v0.1.md)
