# I-SEO Report Hub — Reporting Period CRUD Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no app-source; no runtime; no DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Reporting Period CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md)

---

## 1. Purpose

Зафиксировать **первый управляемый CRUD-слой** для `reporting_periods` на локальном MVP после:

- DB-backed auth baseline;
- DB-03 `reporting_periods` migration apply;
- local fixture apply (demo client/project/site/period).

Цель charter:

1. Зафиксировать текущий baseline после fixture apply.
2. Спроектировать MVP CRUD (list / detail / create / edit / archive-by-status).
3. Определить маршруты, контроллеры, views, формы, CSRF, access roles.
4. Определить safe validation для `period_key` / dates / status / project uniqueness.
5. Определить list/detail/create/edit boundaries.
6. Явно исключить weekly checkpoint / report content / editor / client portal.
7. Подготовить implementation plan для следующей волны.

Эта волна — **documentation / policy only**. CRUD **не** кодируется здесь.

---

## 2. Current Baseline

### Auth implementation

| Item | Value |
|------|-------|
| Primary commit | `d4b3b2e2155f41e8f99d4ac56a47de870ea6b10c` — `feat(iseo-report-hub): add auth persistence bootstrap` |
| Hash-record follow-up | `0cd2cfb7735e59d3d54bf8dd9002ba45949dd47d` — `docs(iseo-report-hub): record auth persistence bootstrap commit hash` |
| Local admin | `admin@iseo-report-hub.test` (password/hash **not** recorded) |
| Auth capabilities | DB-backed login/logout; dashboard protected; health DB status; audit for auth events |
| Users / roles | **1** / **6** |

### DB-03 migration apply

| Item | Value |
|------|-------|
| Primary commit | `c19c29b8be79ecfc8c946dd624e8f21023c2db39` — `feat(iseo-report-hub): add db03 reporting periods migration` |
| Hash-record follow-up | `2f88d0ced9f32e11414a02c8b6a08aad7b047099` — `docs(iseo-report-hub): record db03 reporting periods migration commit hash` |
| Migration file | `2026_07_25_000002_create_reporting_periods_table.sql` |
| Batch | **2** |
| Table | `reporting_periods` |

### Local fixture apply

| Item | Value |
|------|-------|
| Primary commit | `348b40896a86f5652ea8f7ba5ab5574ebc2abf2b` — `feat(iseo-report-hub): add local fixture bootstrap` |
| Hash-record follow-up | `7c543116765a3a25630039a5c732c1884731b0fc` — `docs(iseo-report-hub): record local fixture bootstrap commit hash` |
| client_id **1** | `Demo Client` / `demo-client` |
| project_id **1** | `Demo SEO Project` / `demo-seo-project` |
| site_id **1** | `https://demo.example.test` |
| reporting_period_id **1** | `2026-07` (title `Demo July 2026`, summary `LOCAL_FIXTURE_ONLY`, status `draft`) |
| Audit | `local_fixture.created` |
| Counts after | clients/projects/sites/reporting_periods = **1/1/1/1** |
| FK joins | validated |
| Duplicate `(project_id, period_key)` | rejected and rolled back |
| Health / app smoke | **PASS** |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration count | **2** |
| Table count | **10** |
| users / roles | **1** / **6** |
| clients / projects / sites / reporting_periods | **1** / **1** / **1** / **1** |

### Current limitation

- **No** CRUD UI for reporting periods yet.
- **No** weekly checkpoints table.
- **No** monthly report content table.
- **No** client portal.
- **No** real client data.
- Dashboard card still shows “Reporting CRUD — pending”.

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Scope

### In scope

- Internal reporting period **list / detail / create / edit**
- Archive via status `archived` (no hard DELETE)
- Auth required on all CRUD routes; CSRF on all POST
- Role-aware create/edit/status boundaries (MVP matrix)
- Validation for project existence, `period_key`, dates, status set, uniqueness
- Optional audit events for create/update/status_changed
- Navigation links from header + dashboard
- Local fixture smoke using demo project + optional second smoke period `2026-08`
- Design + implementation + validation plans for next wave

### Out of scope

- Weekly checkpoint DB/UI / editor
- Monthly report content / blocks / evidence uploads
- Client portal / `client_viewer` access to periods
- Hard DELETE of periods
- Bulk actions
- Real client / project / domain import
- Topvisor / API import
- n8n reminders
- Production deployment
- Schema / migration changes
- App-source / runtime / DB mutation **in this charter wave**
- HealthController expected table-count wording fix (prefer separate small charter if needed)

---

## 4. Product Rules

1. A reporting period is a **monthly shell** for one project (`period_key` = `YYYY-MM`).
2. Status lifecycle follows [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md):  
   `draft → active → weekly_review → monthly_review → finalized → archived`.
3. Unique identity: `(project_id, period_key)` — one period per project/month.
4. `period_key` must match the calendar month of `period_start`.
5. `period_start <= period_end`; prefer full calendar month bounds for MVP.
6. `created_by` / `updated_by` set from current authenticated user.
7. `finalized_at` set when status becomes `finalized`; cleared only on exceptional admin correction away from `finalized` (MVP: clear when leaving `finalized`; keep when staying finalized).
8. No DELETE in MVP — archive via `status = archived`.
9. Smoke-created rows must carry `LOCAL_FIXTURE_ONLY` marker in title and/or summary when created by CRUD smoke.
10. Keep UI simple internal admin style; no CDN / external assets; reuse current layout/CSS.
11. Safe errors only — no stack traces, no secrets, no password output.
12. CRUD manages the **period shell only** — not report body content.

---

## 5. Access Model

| Role | List / Detail | Create | Edit metadata (title/summary/owner/reviewer) | Edit dates / period_key | Status transitions | Finalize | Archive |
|------|---------------|--------|----------------------------------------------|-------------------------|--------------------|----------|---------|
| `admin_owner` | Yes | Yes | Yes | Yes (with draft/active rules below) | Full | Yes | Yes |
| `seo_lead_reviewer` | Yes | Yes | Yes | Yes while draft (key); dates while draft/active | Yes including finalize | Yes | Yes |
| `seo_specialist` | Yes | Yes | Yes (own/assigned preferred; MVP: all local demos OK) | Yes while draft (key); dates while draft/active | Up to `weekly_review` / `monthly_review`; **not** finalize / archive | No | No |
| `account_client_manager` | Yes | No | Limited: title/summary only | No | No (read status only) | No | No |
| `internal_viewer` | Yes | No | No | No | No | No | No |
| `client_viewer` | **No** (out of scope) | No | No | No | No | No | No |

**Field edit locks (all mutating roles):**

| Field | Editable when |
|-------|---------------|
| `period_key` | Only while `status = draft` |
| `period_start` / `period_end` | Only while `status` in (`draft`, `active`) |
| `project_id` | **Immutable after create** |
| `status` / `title` / `summary` / owner / reviewer | Per role matrix; `archived` rows: admin/lead may unarchive/edit under HITL; specialist/account: read-only |

Unauthenticated users and users without internal role → redirect `/login`.  
`client_viewer` sessions (if ever present) → deny CRUD routes (403 or redirect).

---

## 6. Data Policy

- Target DB only: `iseo_report_hub_dev` @ `127.0.0.1`.
- Use current local demo fixture as FK baseline (`project_id = 1`).
- **No** real client rows in CRUD smoke.
- Implementation smoke may create a second demo period (e.g. `2026-08`) marked `LOCAL_FIXTURE_ONLY`.
- Do **not** delete smoke rows unless a later explicit destructive charter approves; leave documented local demo rows.
- No passwords, hashes, or credentials in docs/Git/UI errors.
- No production / remote DB writes.

---

## 7. Implementation Boundary

### This charter wave (allowed)

- Product docs: charter, design, implementation plan, validation plan
- Closeout report
- OPERATIONAL-INDEX update
- Read-only docs/code review; optional read-only DB status

### This charter wave (forbidden)

- Any `app-source/**` edit
- Any Localhost runtime edit
- Any DB INSERT/UPDATE/DELETE/DDL
- Any SQL/tool creation
- Source → runtime sync
- Env / admin / password changes
- Push / fetch / pull / reset / clean / stash

### Next implementation wave (planned)

- App-source routes/controller/service/repository/views/nav
- Source → runtime sync for allowlisted files only
- Local CRUD smoke (may INSERT/UPDATE period rows + optional audit)
- Result docs + closeout
- Exact-path commit(s); **no push** unless separately authorized

---

## 8. Validation Gates

Charter wave:

1. Preflight identity (repo / X: / AI WS / branch / empty index / empty i-SEO WIP).
2. Docs-only write scope.
3. Optional DB read-only baseline matches fixture expectations.
4. Scoped docs commit; staged allowlist only; no push.

Implementation wave (next) must pass gates in [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-VALIDATION-PLAN-v0.1.md):

- Route smoke (list/detail/create/edit)
- CSRF + validation errors
- Create `2026-08` + duplicate refuse
- Edit title/status + archive-by-status
- Role checks where practical
- Auth / health / 404 regression
- No secrets in output

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Role matrix over-engineered for one local admin | Implement matrix in service; smoke primarily as `admin_owner`; document specialist/finalize denial as unit/policy check |
| Editing `period_key` after draft breaks uniqueness / history | Lock `period_key` after draft |
| Accidental DELETE | No delete route; archive status only |
| Smoke creates unlabeled fake data | Require `LOCAL_FIXTURE_ONLY` on smoke create |
| Scope creep into weekly/monthly editor | Explicit out-of-scope + STOP if attempted |
| Health expected tables still `9/9` wording | Prefer separate health charter; do not block CRUD |
| Foreign WIP pollution | Exact-path staging only |

---

## 10. Next Implementation Wave

**Name:** `I-SEO Report Hub — Reporting Period CRUD Implementation 01`

**Deliverable:** working internal CRUD for `reporting_periods` against local fixture + auth, without content editor / client portal / schema changes.

**Entry docs:** this charter + design + implementation plan + validation plan.

**Exit:** smoke PASS; result + REPORT docs; OPERATIONAL-INDEX updated; exact-path commit(s); push only if separately authorized.
