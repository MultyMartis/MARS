# I-SEO Report Hub — Monthly Report Content CRUD Validation Plan v0.1

**Status:** VALIDATION PLAN ONLY — execute in implementation wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-IMPLEMENTATION-PLAN-v0.1.md)

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
| Migrations / tables | **4** / **12** |
| users / roles | **1** / **6** |
| clients / projects / sites / reporting_periods | **1** / **1** / **1** / **2** |
| weekly_checkpoints | **4** (W1/W2/W3/W4) |
| monthly_report_contents before edit smoke | **1** (demo id **1**, period `2026-07`) |
| Parent period | id **1**, `2026-07`, `draft` |
| Auth | Local admin can authenticate (password never printed) |
| Migration file present | `2026_07_26_000004_create_monthly_report_contents_table.sql` |

STOP if DB-05 baseline missing or DB target wrong.

---

## 2. Route smoke

| Step | Request | Expect |
|------|---------|--------|
| Unauth period monthly | GET `/reporting-periods/1/monthly-report` | Redirect `/login` |
| Auth period monthly | GET `/reporting-periods/1/monthly-report` | **200**; shows demo id **1** / status / title |
| Auth detail by id | GET `/monthly-reports/1` | **200**; parent context; source checkpoint links |
| Auth edit form | GET `/monthly-reports/1/edit` | **200** when capability allows |
| Auth create form when row exists | GET `/reporting-periods/1/monthly-report/create` | Redirect/flash to existing **or** safe refuse (no second row) |
| Missing id | GET `/monthly-reports/999999` | **404** or safe not-found |
| No DELETE | Any DELETE method / UI | Absent |

---

## 3. Form / CSRF smoke

| Step | Expect |
|------|--------|
| Create/edit forms include `_csrf` | Present |
| POST create/update without CSRF / bad token | Rejected; no mutation |
| POST update with valid CSRF | Accepted when payload valid |
| Validation errors re-render form | Safe messages; old input preserved where practical |
| No stack traces / SQL errors in HTML | Confirmed |

---

## 4. DB create / edit / status smoke

| Step | Expect |
|------|--------|
| Prefer edit existing id **1** | Title/content updated; markers remain `LOCAL_FIXTURE_ONLY` |
| POST status → `in_progress` | Persisted; `updated_by` set |
| Optional POST status → `ready_for_review` | Only if still safe for field-lock smoke; else keep `in_progress` and document |
| Counts | monthly_report_contents **1** (unless create-on-other-period documented); reporting_periods **2**; weekly_checkpoints **4** |
| Prefer not mutate weekly / period rows | Intact |
| Document final monthly status | In implementation result |

---

## 5. Uniqueness / validation errors

| Case | Expect |
|------|--------|
| Duplicate create for period `2026-07` | Refused; friendly error; count unchanged |
| Invalid status / illegal transition | Refused |
| Non-existent parent period | Refused / 404 |
| Edit while parent archived/finalized as non-admin | Refused |
| Edit content while `finalized` as non-admin | Refused / field locked |
| Title empty or >255 | Refused |
| Text field over soft length cap | Refused |

---

## 6. Source weekly checkpoint validation

| Case | Expect |
|------|--------|
| Valid sources from period `2026-07` (ids resolved from W1–W4 keys) | Accepted |
| Empty sources | Allowed with warning / “no sources” marker |
| Non-existent checkpoint id | Refused |
| Checkpoint id from another period | Refused |
| Invalid JSON / non-array payload | Refused |
| Detail page source links | Show W1–W4 (or selected set) with links to weekly detail |

---

## 7. Access-role smoke

Practical MVP (one local admin):

| Step | Expect |
|------|--------|
| Admin (`admin_owner`) | Full create/edit/status/archive/reopen path PASS |
| Unauthenticated | All monthly routes denied/redirect |
| `client_viewer` | N/A until such user exists — document as deferred |
| Specialist denial of reviewed/finalized/archive | If only admin user exists: **policy covered / not multi-user smoked** |

Do **not** create extra users/passwords in CRUD wave unless a separate bootstrap charter authorizes it.

---

## 8. Audit smoke

If audit implemented:

| Event | When |
|-------|------|
| `monthly_report_content.created` | Only if a create path is exercised |
| `monthly_report_content.updated` | After title/field edit |
| `monthly_report_content.status_changed` | After status change |
| `monthly_report_content.reviewed` / `.finalized` / `.archived` | Only if those statuses are entered in smoke |

No secrets in audit payload. If audit deferred, document as SAFE SIMPLIFICATION in implementation result.

---

## 9. Regression smoke

| Check | Expect |
|-------|--------|
| GET `/reporting-periods` (auth) | **200**; `2026-07` / `2026-08` still listed |
| GET `/reporting-periods/1` | **200**; includes monthly report section/links |
| GET `/reporting-periods/1/weekly-checkpoints` | **200**; W1–W4 still listed |
| GET `/weekly-checkpoints/7` | **200**; W4 still `skipped` (or documented) |
| GET `/login` | **200** |
| GET `/health` | **200** (no secrets) |
| GET `/not-existing` | **404** |
| Auth services / password bootstrap | Untouched |
| Fixture client/project/site | Counts **1/1/1** unchanged |

---

## 10. Data policy

| Rule | Expect |
|------|--------|
| Smoke markers | `LOCAL_FIXTURE_ONLY` retained on monthly demo content |
| Real client data | None |
| Schema | Unchanged |
| reporting_periods rows | Unchanged by monthly CRUD |
| weekly_checkpoints rows | Unchanged by monthly CRUD |
| Duplicate `2026-07` monthly | Never persists |
| Credentials | Never printed / committed |

---

## 11. STOP conditions

STOP implementation smoke / commit if:

- Preflight fails (root/volume/branch/DB target)
- DB-05 baseline destroyed unexpectedly
- DELETE route/UI introduced
- Report blocks / PDF / portal / Topvisor creep in
- Real client data would be written
- Schema/migration mutated
- weekly_checkpoints or reporting_periods mutated unexpectedly
- Non-allowlist paths staged
- Push without charter

Token:

`STOP — I-SEO MONTHLY REPORT CONTENT CRUD VALIDATION SAFETY CONDITION FAILED`

---

## 12. Recommended smoke sequence (next wave)

1. Period `2026-07` monthly report detail shows existing demo row id **1**
2. Edit existing row title/content/status to `in_progress`
3. Duplicate create for `2026-07` refused safely
4. Invalid `source_weekly_checkpoint_ids` refused
5. Source weekly checkpoint links shown
6. Change status to `ready_for_review` **or** keep `in_progress` depending field-lock safety
7. Parent reporting period detail shows monthly report section
8. Confirm no DELETE route/UI
9. Regression: reporting periods / weekly checkpoints / login / health / 404
