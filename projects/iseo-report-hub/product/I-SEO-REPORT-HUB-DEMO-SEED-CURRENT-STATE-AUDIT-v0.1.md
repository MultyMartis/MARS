# I-SEO Report Hub — Demo Seed Current State Audit v0.1

**Status:** read-only audit for seed design — **no DB mutation in this wave**  
**Date:** 2026-08-21  
**Wave:** Demo User and Scenario Seed Charter 01  
**Local DB:** `iseo_report_hub_dev` @ `127.0.0.1:3306`  
**Probe:** MySQL read-only + HTTP GET `/health` / `/login` (both **200**)

---

## 1. Current demo objects (preserve)

| Entity | Attested value | IDs |
|--------|----------------|-----|
| Client | `Demo Client` / slug `demo-client` | **1** |
| Project | `Demo SEO Project` / slug `demo-seo-project` / `service_corporate` | **1** |
| Site | `https://demo.example.test` / label `LOCAL_FIXTURE_ONLY` | **1** |
| Period July | `2026-07` / status `draft` / title `Demo July 2026` | **1** |
| Period August | `2026-08` / status `archived` | **3** |
| Monthly report 1 | July / status **`finalized`** / title contains `LOCAL_FIXTURE_ONLY` | **1** |
| Monthly report 5 | August / status **`draft`** / empty draft path accepted | **5** |
| Blocks under report 1 | **6** | — |
| Work entries under report 1 | **7** | — |
| Blocks / entries under report 5 | **0 / 0** | — |

**Hard rule for next seed:** do **not** reuse or mutate report **1** or report **5**. New scenario = separate client + project + periods + monthlies.

---

## 2. Current users / roles

| id | name | email | roles | status |
|----|------|-------|-------|--------|
| 1 | Local Admin | `admin@iseo-report-hub.test` | `admin_owner` | active |
| 2 | Polygon WS Local Test | `polygon-ws@mail.ru` | `admin_owner` | active |

| Finding | Evidence |
|---------|----------|
| Login is **email** | `/login` email input; `AuthService` lookup by email |
| Role key for SEO author | **`seo_specialist`** present in `roles` |
| Test user | **Absent** — no `test@reports.i-seo.local` / no `Тест Проверочнов` |
| Bare login `test` | Not a valid email credential for current UI |

Roles present: `admin_owner`, `seo_lead_reviewer`, **`seo_specialist`**, `account_client_manager`, `internal_viewer`, `client_viewer`.

---

## 3. Existing seed / fixture tools

| Tool | Path | Role |
|------|------|------|
| Local admin bootstrap | `app-source/tools/create-local-admin.php` | Creates `admin_owner`; local DB guard; `password_hash` |
| Local fixture | `app-source/tools/create-local-fixture.php` | Demo Client / project / site / July period; marker `LOCAL_FIXTURE_ONLY` |
| Nikita catalogue seed | `app-source/tools/seed-nikita-catalogue.php` | Categories + work items (+ fixture entries pattern) |
| Summary assembly safe fixture | `app-source/tools/summary-assembly-safe-fixture.php` | Temporary fixture; cleans up; avoids id 1/5 |
| Migrations CLI | `app-source/tools/db-migrate.php` | Schema apply only |

**Gap:** no dedicated demo-user / `ПРОВЕРКА.рa` scenario seed tool yet — planned as `tools/demo-proverka-seed.php` in Implementation 01.

---

## 4. Tables needed for new scenario

| Domain | Table(s) | Notes |
|--------|----------|-------|
| Users | `users`, `user_roles`, `roles` | Email unique; status `active`/`disabled`; no username column |
| Org | `clients`, `projects`, `sites`, optional `project_type_profiles` | No client/project UI CRUD routes today → **must seed** |
| Periods | `reporting_periods` | Unique `(project_id, period_key)`; status CHECK listed below |
| Monthly | `monthly_report_contents` | One row per period; text fields for summary sections |
| Blocks | `report_blocks` | Types include shells + `metric_snapshot` / `custom_text` / `weekly_summary` |
| Work | `monthly_report_work_entries` (+ catalogue `seo_work_categories` / `seo_work_items`) | Catalogue already seeded (13 / 31) |
| Weekly (optional) | `weekly_checkpoints` | Desirable for realism; not mandatory for MVP demo |
| Metrics | **No dedicated metrics table** | Use prose + optional `metric_snapshot` blocks / `data_json` / `source_metric_refs` with `"demo": true` |
| Artifacts | `report_snapshots`, `report_exports`, `report_export_shares` | **Do not create** for new demo reports in seed |

### Status enums (exact allowed values)

**`reporting_periods.status`:** `draft`, `active`, `weekly_review`, `monthly_review`, `finalized`, `archived`

**`monthly_report_contents.status`:** `draft`, `in_progress`, `ready_for_review`, `reviewed`, `finalized`, `archived`

**`report_blocks.status`:** `draft`, `in_progress`, `ready_for_review`, `reviewed`, `approved`, `archived`

**`monthly_report_work_entries.status`:** `planned`, `in_progress`, `done`, `blocked`, `cancelled`, `deferred`

**`monthly_report_work_entries.period_role`:** `done`, `planned_next`, `risk`, `note`

**`monthly_report_work_entries.client_visibility`:** `internal`, `client_safe`, `client_facing`

---

## 5. Export / share / PDF state to preserve

| Object | Count / state | Scope |
|--------|---------------|-------|
| Snapshots | **1** active (`monthly-1-v1` on monthly **1**) | Demo Client only |
| Exports | **4** (html/pdf on monthly **1**) | Demo Client only |
| Shares | **7** total — **6** revoked + **1** active on export **4** | Demo Client only |
| PDF/export/share for new scenario | **Must remain 0** | Seed + browser fill |

Seed must refuse if any export/share/PDF rows appear for **new** demo monthly IDs after create (or if seed would touch monthly 1/5).

---

## 6. Auth / finalization constraints (design impact)

| Topic | Finding |
|-------|---------|
| Specialist can submit for review | `seo_specialist` ∈ submit roles |
| Finalize / mark reviewed | Requires `admin_owner` or `seo_lead_reviewer` |
| Finalization service | Does **not** auto-create export/share; snapshot is a **separate** flow |
| Client/project CRUD UI | **Absent** in `routes.php` — seed required for org entities |

---

## 7. Risk notes

1. **`LOCAL_FIXTURE_ONLY`** strings remain in Demo Client titles/labels/site — sanitizer may strip in some UI surfaces; **new** `ПРОВЕРКА.рa` scenario must **not** use that marker (use `MARS_DEMO_PROVERKA_20260821` instead).
2. Do **not** overwrite Demo Client periods `2026-07` / `2026-08` on `project_id=1` — create periods under the **new** project (period keys may repeat across projects).
3. Existing exports/shares on report 1 are frozen — no regenerate / revoke / create in seed wave.
4. Password `test` is local/demo only — never ship to `reports.i-seo.su` without rotate/disable.
5. Mixed-script display name `ПРОВЕРКА.рa` must stay literal; technical slug ASCII only.
6. No `is_demo` column on `users` — idempotency via email + notes/marker conventions + evidence JSON.

---

## 8. Catalogue readiness

| Catalogue | Count |
|-----------|-------|
| `seo_work_categories` | **13** |
| `seo_work_items` | **31** |
| `weekly_checkpoints` (Demo Client) | **4** |

New scenario work entries may link to existing catalogue items or use manual titles.

---

## 9. SAFE UNKNOWN

- Exact password policy length for non-admin create helpers beyond `create-local-admin.php` (admin tool requires min 12 for interactive admin; demo password `test` is operator-approved **local-only** exception for Implementation 01).
- Whether period create UI can bind to a newly seeded project without extra UI work — Implementation 01 must verify after seed; browser fill remains content-primary.
