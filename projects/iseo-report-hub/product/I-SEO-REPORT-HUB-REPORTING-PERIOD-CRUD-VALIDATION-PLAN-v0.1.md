# I-SEO Report Hub — Reporting Period CRUD Validation Plan v0.1

**Status:** VALIDATION PLAN ONLY — execute in implementation wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Reporting Period CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-IMPLEMENTATION-PLAN-v0.1.md)

---

## 1. Preflight

Before implementation smoke:

| Check | Expected |
|-------|----------|
| Repo root | `X:\AI MARS` |
| Drive / volume | `X:` / `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| Staged index | Empty (or only intentional allowlist mid-wave) |
| DB name / host | `iseo_report_hub_dev` / `127.0.0.1` |
| Migrations / tables | **2** / **10** |
| users / roles | **1** / **6** |
| Fixture counts before smoke create | clients/projects/sites/reporting_periods = **1/1/1/1** |
| Demo period | id **1**, `period_key=2026-07`, summary/title markers as fixture |
| Auth | Local admin can login (password never printed) |

STOP if fixture baseline missing or DB target wrong.

---

## 2. Route smoke

| Step | Request | Expect |
|------|---------|--------|
| Unauth list | GET `/reporting-periods` | Redirect `/login` (or equivalent deny) |
| Auth list | GET `/reporting-periods` (session) | **200**; shows `2026-07` |
| Auth detail | GET `/reporting-periods/1` | **200**; demo period fields |
| Auth create form | GET `/reporting-periods/create` | **200**; project select includes Demo SEO Project |
| Auth edit form | GET `/reporting-periods/1/edit` | **200** |
| Missing id | GET `/reporting-periods/999999` | **404** or safe not-found handling |

---

## 3. Form / CSRF smoke

| Step | Expect |
|------|--------|
| Create/edit forms include `_csrf` | Present |
| POST create without CSRF / bad token | Rejected; no row insert |
| POST create with valid CSRF | Accepted when payload valid |
| POST update without CSRF | Rejected; no change |
| Validation errors re-render form | Safe messages; old input preserved where practical |
| No stack traces / SQL errors in HTML | Confirmed |

---

## 4. DB create / edit / archive smoke

| Step | Expect |
|------|--------|
| POST create `project_id=1`, `period_key=2026-08`, dates Aug 2026, status `draft`, title/summary with `LOCAL_FIXTURE_ONLY` | New row; `created_by` = admin |
| Counts | reporting_periods **2** (or documented ≥2) |
| POST edit title | Persisted; `updated_by` set |
| POST status → `active` | Persisted |
| POST status → `finalized` | `finalized_at` set (non-null) |
| POST status → `archived` | Archived; row still exists (no DELETE) |
| Leave smoke rows | Do not delete unless separate charter |

---

## 5. Uniqueness / validation errors

| Case | Expect |
|------|--------|
| Duplicate `(1, 2026-08)` | Refused; friendly error; count unchanged |
| Bad `period_key` (`2026-13`, `202607`) | Refused |
| `period_start > period_end` | Refused |
| `period_key` month ≠ `period_start` month | Refused |
| Invalid status | Refused |
| Non-existent `project_id` | Refused |
| Edit `period_key` while not draft | Refused / field locked |
| Edit dates while finalized/archived | Refused / field locked |

---

## 6. Access-role smoke

Practical MVP (one local admin):

| Step | Expect |
|------|--------|
| Admin (`admin_owner`) | Full create/edit/status/archive path PASS |
| Unauthenticated | All mutating + list/detail denied/redirect |
| `client_viewer` | N/A until such user exists — document as deferred |
| Specialist finalize denial | If only admin user exists: document as **policy covered / not multi-user smoked** (SAFE UNKNOWN until second user seeded) |

Do **not** create extra users/passwords in CRUD wave unless a separate bootstrap charter authorizes it.

---

## 7. Audit smoke

If audit implemented:

| Event | Expect |
|-------|--------|
| `reporting_period.created` | Present for smoke create |
| `reporting_period.updated` and/or `reporting_period.status_changed` | Present for edits |
| Metadata | ids/keys/status only; **no** secrets |

If audit deferred: document explicitly in implementation result; do not fail whole wave solely for audit omission unless charter made audit mandatory (this plan: **recommended**, fail soft with explicit note).

---

## 8. Regression smoke

| URL | Expect |
|-----|--------|
| `/login` | **200** |
| Login success / dashboard | Still works |
| Logout | Still works |
| `/health` | **200**; DB ok; name `iseo_report_hub_dev`; migrations **2** |
| `/not-existing` | **404** |
| Fixture client/project/site | Still **1/1/1**; unchanged by CRUD except period rows |

---

## 9. Data policy checks

- No real client names/domains introduced
- Smoke period marked `LOCAL_FIXTURE_ONLY`
- No password/hash in reports, flashes, HTML, Git
- No `.env` / `.env.local` commits
- No production DB touched

---

## 10. STOP conditions

STOP implementation smoke / commit if:

- Preflight identity fails
- DB target mismatch
- Fixture baseline absent before create
- DELETE used for “cleanup”
- Schema changed
- Real client data inserted
- Secrets printed
- Scope creep (weekly editor / portal)
- Staging allowlist cannot be guaranteed

Token:

`STOP — I-SEO REPORT HUB REPORTING PERIOD CRUD VALIDATION SAFETY CONDITION FAILED`

---

## 11. Pass / fail summary template (for implementation REPORT)

| Gate | Result |
|------|--------|
| Preflight | PASS / FAIL |
| Routes | PASS / FAIL |
| CSRF / forms | PASS / FAIL |
| Create / edit / archive | PASS / FAIL |
| Uniqueness / validation | PASS / FAIL |
| Access | PASS / FAIL / PARTIAL |
| Audit | PASS / FAIL / DEFERRED |
| Regression | PASS / FAIL |
| Data policy | PASS / FAIL |
