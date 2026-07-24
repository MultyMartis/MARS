# I-SEO Report Hub — Local Fixture Apply Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Project/Client Local Fixture Apply 01  
**Related:** [I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md](I-SEO-REPORT-HUB-LOCAL-FIXTURE-DATA-PLAN-v0.1.md)

---

## 1. Status

| Field | Value |
|-------|-------|
| Wave status | **complete** |
| Fixture created | **yes** |
| Idempotency | **yes** (second run `already-present`, exit 0) |
| Real client data | **no** |
| Credentials in tool output / docs | **no** |

---

## 2. Tool

| Field | Value |
|-------|-------|
| Source path | `projects/iseo-report-hub/app-source/tools/create-local-fixture.php` |
| Runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\create-local-fixture.php` |
| Behavior | CLI-only; creates demo client + project + site + reporting_period; optional audit event |
| DB guard | Refuses unless DB name is exactly `iseo_report_hub_dev` and host is exactly `127.0.0.1` |
| Transaction | Single transaction; rollback on failure |
| Idempotency | If all four fixture rows match expected markers → `already-present` exit 0; partial mismatch → STOP non-zero |

---

## 3. Fixture Rows

| Entity | Safe identity | ID | Marker fields |
|--------|---------------|----|---------------|
| Client | name `Demo Client`, slug `demo-client`, status `active` | **1** | `notes = LOCAL_FIXTURE_ONLY` |
| Project | name `Demo SEO Project`, slug `demo-seo-project`, type `service_corporate`, status `active` | **1** | parent client marker + stable slug (no `notes` column on `projects`) |
| Site | url `https://demo.example.test`, `is_primary = 1` | **1** | `label = LOCAL_FIXTURE_ONLY` |
| Reporting period | `period_key = 2026-07`, `2026-07-01`–`2026-07-31`, status `draft`, title `Demo July 2026` | **1** | `summary = LOCAL_FIXTURE_ONLY` |
| Audit | event `local_fixture.created` | n/a | metadata marker only; **no secrets** |

`owner_user_id` / `created_by` set to local admin resolved by email `admin@iseo-report-hub.test`.  
`reviewer_user_id` / `updated_by` left NULL.

---

## 4. DB Validation

| Check | Result |
|-------|--------|
| Counts before | clients/projects/sites/reporting_periods = **0/0/0/0** |
| Counts after | **1/1/1/1** |
| FK joins | client → project → site / period **ok** |
| Unique `(project_id, period_key)` | present (`uniq_reporting_periods_project_period`) |
| Duplicate insert test | rejected (SQLSTATE `23000`); rolled back; count remains **1** |
| `reporting_periods` smoke | **non-structural** (real row + unique rejection evidenced) |

DB target throughout: `iseo_report_hub_dev` @ `127.0.0.1`.

---

## 5. App Smoke

| URL | Result |
|-----|--------|
| `http://iseo-report-hub.test/health` | **200**, overall **ok**, DB status **ok**, migration count **2**, DB name `iseo_report_hub_dev` |
| `http://iseo-report-hub.test/login` | **200** |
| `http://iseo-report-hub.test/not-existing` | **404** |

Auth baseline **not modified** in this wave. No password smoke.

---

## 6. Restrictions

- No production / remote DB
- No real client data
- No schema / migration changes
- No auth / app UI / CRUD code edits
- No secrets / password / hash in output or docs
- No `.env` / `.env.local` commits
- No DELETE / DROP / TRUNCATE

---

## 7. What Still Does Not Exist

- CRUD UI for clients / projects / sites / reporting periods
- Real client import
- Weekly checkpoints
- Monthly report content
- Client portal

---

## 8. Next Phase

**Recommend:** `Reporting Period CRUD Charter 01`

---

## 9. SAFE UNKNOWN

- Whether HealthController expected table count still reports `9/9` vs `10/10` in HTML (charter said not to fix in this wave; `/health` overall remained **ok**).
- Exact future cleanup policy for fixture rows (no cleanup tool in this wave).
