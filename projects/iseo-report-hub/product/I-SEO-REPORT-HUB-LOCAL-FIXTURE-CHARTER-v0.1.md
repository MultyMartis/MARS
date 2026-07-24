# I-SEO Report Hub — Local Fixture Charter v0.1

**Status:** PLANNING / CHARTER ONLY — no SQL; no fixture rows; no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Project/Client Local Fixture Charter 01  
**Related:** [I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-MIGRATION-APPLY-RESULT-v0.1.md), [I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md](I-SEO-REPORT-HUB-AUTH-PERSISTENCE-IMPLEMENTATION-RESULT-v0.1.md)

---

## 1. Purpose

Зафиксировать **безопасный local-only fixture baseline** для `clients` / `projects` / `sites` (и опционально одной demo-строки `reporting_periods`) после успешного apply DB-03.

Цель charter:

1. Задокументировать текущий DB baseline после DB-03.
2. Спроектировать минимальный fake fixture, достаточный для FK/unique smoke `reporting_periods`.
3. Решить, нужен ли fixture **до** Reporting Period CRUD.
4. Определить, какие строки допустимы в следующей apply-волне.
5. Зафиксировать ограничения: no real client data, no production DB, no secrets.
6. Определить validation/smoke gates.
7. Подготовить implementation plan для следующей волны.

Эта волна — **documentation / policy only**. Fixture rows **не** создаются здесь.

---

## 2. Current Baseline

### Auth implementation

| Item | Value |
|------|-------|
| Primary commit | `d4b3b2e2155f41e8f99d4ac56a47de870ea6b10c` — `feat(iseo-report-hub): add auth persistence bootstrap` |
| Hash-record follow-up | `0cd2cfb7735e59d3d54bf8dd9002ba45949dd47d` — `docs(iseo-report-hub): record auth persistence bootstrap commit hash` |
| Local admin | `admin@iseo-report-hub.test` (password/hash **not** recorded) |
| Users / roles | **1** / **6** |

### DB-03 charter

| Item | Value |
|------|-------|
| Primary commit | `51f3c1f6cd59665c4d59b5227b73c3764859a887` — `docs(iseo-report-hub): add db03 reporting periods charter` |
| Hash-record follow-up | `04c785a72ced2a2a0761a6b3cfb6033e0b4d1282` — `docs(iseo-report-hub): record db03 reporting periods charter commit hash` |

### DB-03 apply

| Item | Value |
|------|-------|
| Primary commit | `c19c29b8be79ecfc8c946dd624e8f21023c2db39` — `feat(iseo-report-hub): add db03 reporting periods migration` |
| Hash-record follow-up | `2f88d0ced9f32e11414a02c8b6a08aad7b047099` — `docs(iseo-report-hub): record db03 reporting periods migration commit hash` |
| Migration file | `2026_07_25_000002_create_reporting_periods_table.sql` |
| Checksum (SHA-256) | `5bc50e53ab20a347c8a278d1726be6c71d835b572f369a14d2256e3e986e3be9` |
| Batch | **2** |

### Current DB (read-only check this charter wave)

| Item | Value |
|------|-------|
| DB | `iseo_report_hub_dev` @ `127.0.0.1` |
| Migration count | **2** |
| Table count | **10** |
| users / roles | **1** / **6** |
| clients / projects / sites | **0** / **0** / **0** |
| reporting_periods rows | **0** |
| `reporting_periods` table | **exists** |
| Unique/FK row smoke | **structural only** (no project fixture) |
| Health | `/health` **200**; DB pass; migration count **2**; latest = DB-03 file |
| Health expected tables | still `9/9` wording — known HealthController limitation; **not** fixed in this wave |

### Current tables

`schema_migrations`, `users`, `roles`, `user_roles`, `audit_log`, `clients`, `projects`, `sites`, `project_type_profiles`, `reporting_periods`

### Source / runtime model

- **Model A** — `projects/iseo-report-hub/app-source/` is versioned SoT; sync **source → runtime**
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`
- Public URL: `http://iseo-report-hub.test/`

---

## 3. Scope

### In scope

- Local fixture design for demo client / project / site / optional reporting period
- Validation plan for FK/unique/health/auth smoke
- Implementation boundary for the next apply wave
- OPERATIONAL-INDEX status update
- Decision: fixture **before** Reporting Period CRUD

### Out of scope

- Production data
- Real i-SEO client / project / domain import
- Report content tables (weekly/monthly blocks, evidence, snapshots)
- Reporting Period CRUD UI
- Client portal
- Topvisor / API imports
- n8n reminders
- SQL authoring / seed migration / fixture tool creation (deferred to apply wave)
- App-source / runtime / DB mutation in this charter wave
- Automatic destructive cleanup

---

## 4. Why Fixture Is Needed

1. `reporting_periods.project_id` → `projects(id)` **ON DELETE RESTRICT**. Without a project row, period insert smoke is impossible.
2. Unique constraint `uniq_reporting_periods_project_period` on `(project_id, period_key)` cannot be exercised with real insert/duplicate refusal while `projects = 0`.
3. Future Reporting Period CRUD needs at least one safe FK target; inventing real i-SEO clients for local smoke is forbidden.
4. Fixture-first keeps CRUD charter focused on UI/service behavior instead of inventing ad-hoc SQL in the CRUD wave.
5. Explicit fake markers (`LOCAL_FIXTURE_ONLY`) allow later selective cleanup without TRUNCATE/DROP.

**Decision:** Local fixture **is required before** Reporting Period CRUD and before non-structural FK/unique smoke.

---

## 5. Safety Boundary

| Rule | Requirement |
|------|-------------|
| Environment | Local only — `iseo_report_hub_dev` @ `127.0.0.1` |
| Production | **Forbidden** |
| Real client data | **Forbidden** (no real company names, domains, contacts, credentials) |
| Secrets | **Forbidden** in docs, tool output, Git |
| Schema | **No** schema change in fixture apply |
| Seed via migration | **Not preferred** — fixture is data, not schema history |
| Cleanup | Explicit future cleanup only; no DROP/TRUNCATE; only rows marked fixture |
| Tool guard | Fixture tool must refuse non-local / production DB names/hosts |

---

## 6. Data Ownership

| Layer | Role |
|-------|------|
| Active Brain docs | Policy + plans (this charter pack) |
| `app-source/tools/` (next wave) | Versioned local fixture CLI (preferred) |
| Local DB `iseo_report_hub_dev` | Only place where fixture rows live |
| Runtime | Receives tool via source→runtime sync in apply wave if required; **not** a second data SoT |
| Production / remote DB | **No ownership**, no fixture |

Fixture rows are **local operational test data**, not product corpus and not ATLAS identity.

---

## 7. Recommended Implementation Model

**Preferred:** local-only CLI tool `tools/create-local-fixture.php`

| Property | Decision |
|----------|----------|
| Location | `app-source/tools/create-local-fixture.php` (next wave) |
| Schema migration seed | **No** |
| One-off operator SQL | Less preferred (less reproducible) |
| Idempotency | Re-run must not duplicate; resolve by stable slug/key |
| Output | IDs and counts only; **no** secrets |
| Audit | Optional `audit_log` event if model supports it |
| Guardrails | Refuse unless DB name/host match local policy |

Recommended demo set (created only in apply wave):

| Entity | Planned identity |
|--------|------------------|
| Client | name `Demo Client`, slug `demo-client`, notes `LOCAL_FIXTURE_ONLY` |
| Project | name `Demo SEO Project`, slug `demo-seo-project`, type safe default |
| Site | url `demo.example.test` (or `example.test`), label marked fixture |
| Reporting period | `period_key` `2026-07`, status `draft`, summary `LOCAL_FIXTURE_ONLY` |

Details: [LOCAL-FIXTURE-DATA-PLAN-v0.1](I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md).

---

## 8. Validation Gates

Next apply wave must prove:

- Pre counts `clients/projects/sites/reporting_periods` = `0/0/0/0` (or documented variance)
- Post counts `1/1/1/1` (or documented if period row deferred)
- FK insert to `reporting_periods` succeeds against demo project
- Duplicate `(project_id, period_key)` refused
- `/health` remains **200**; login/dashboard still work
- No credentials/secrets in output or Git

Full matrix: [LOCAL-FIXTURE-VALIDATION-PLAN-v0.1](I-SEO-REPORT-HUB-LOCAL-FIXTURE-VALIDATION-PLAN-v0.1.md).

---

## 9. Risks

| Risk | Mitigation |
|------|------------|
| Fixture mistaken for real client data | Explicit fake names + `LOCAL_FIXTURE_ONLY` markers + slug prefixes |
| Seed baked into migration history | Prefer CLI tool; forbid fixture SQL in schema migrations |
| Accidental production run | Hard refuse non-local DB name/host |
| Over-broad cleanup | Cleanup only tagged rows; no TRUNCATE/DROP |
| Projects table has no `notes` column | Mark via client notes, site label, period summary, and stable demo slugs |
| Health still shows `9/9` expected tables | Document as known limitation; do not expand fixture wave into health code unless separately chartered |

---

## 10. Next Implementation Wave

**Name:** `I-SEO Report Hub — Project/Client Local Fixture Apply 01`

**Does:** create the fixture CLI, sync if needed, insert demo rows into local DB, run validation gates, write result/report docs.

**Does not:** Reporting Period CRUD UI; real client import; production; schema change; automatic destructive cleanup.

Plan: [LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1](I-SEO-REPORT-HUB-LOCAL-FIXTURE-IMPLEMENTATION-PLAN-v0.1.md).
