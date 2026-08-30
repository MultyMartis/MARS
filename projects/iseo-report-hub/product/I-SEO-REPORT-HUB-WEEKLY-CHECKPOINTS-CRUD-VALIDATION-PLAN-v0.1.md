# I-SEO Report Hub — Weekly Checkpoints CRUD Validation Plan v0.1

**Status:** VALIDATION PLAN ONLY — execute in implementation wave  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-IMPLEMENTATION-PLAN-v0.1.md)

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
| Migrations / tables | **3** / **11** |
| users / roles | **1** / **6** |
| clients / projects / sites / reporting_periods | **1** / **1** / **1** / **2** |
| weekly_checkpoints before create smoke | **3** (W1/W2/W3) |
| Parent period | id **1**, `2026-07`, `draft` |
| Auth | Local admin can authenticate (password never printed) |
| Migration file present | `2026_07_26_000003_create_weekly_checkpoints_table.sql` |

STOP if DB-04 baseline missing or DB target wrong.

---

## 2. Route smoke

| Step | Request | Expect |
|------|---------|--------|
| Unauth list | GET `/reporting-periods/1/weekly-checkpoints` | Redirect `/login` |
| Auth list | GET `/reporting-periods/1/weekly-checkpoints` | **200**; shows W1/W2/W3 |
| Auth detail W1 | GET `/weekly-checkpoints/1` | **200**; key `2026-07-W1`; parent context |
| Auth create form | GET `/reporting-periods/1/weekly-checkpoints/create` | **200**; period context visible |
| Auth edit form W3 or W4 | GET `/weekly-checkpoints/{id}/edit` | **200** when capability allows |
| Missing id | GET `/weekly-checkpoints/999999` | **404** or safe not-found |
| No DELETE | Any DELETE method / UI | Absent |

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
| POST create under period 1: week_index **4**, key `2026-07-W4`, dates inside July 2026, status `draft`, title/text with `LOCAL_FIXTURE_ONLY` | New row; `created_by` = admin |
| Counts | weekly_checkpoints **4**; reporting_periods still **2** |
| POST edit W4 title | Persisted; `updated_by` set |
| POST status on W4 → `in_progress` or `ready_for_review` (optional) | Persisted if transition allowed |
| POST status → `skipped` **or** `archived` | Soft-retired; row still exists (no DELETE) |
| Prefer not mutate W1/W2 | Intact unless documented exception |
| If W3 used for edit | Document final status in implementation result |

---

## 5. Uniqueness / validation errors

| Case | Expect |
|------|--------|
| Duplicate W4 key or week_index 4 | Refused; friendly error; count unchanged |
| `week_index` 0 or 7 | Refused |
| Bad `checkpoint_key` (wrong period part / format) | Refused |
| `checkpoint_start > checkpoint_end` | Refused |
| Dates outside parent period range | Refused |
| Invalid status / illegal transition | Refused |
| Non-existent parent period | Refused / 404 |
| Edit `week_index` / `checkpoint_key` while not draft | Refused / field locked |
| Edit text while `completed` as non-admin | Refused / field locked |

---

## 6. Access-role smoke

Practical MVP (one local admin):

| Step | Expect |
|------|--------|
| Admin (`admin_owner`) | Full create/edit/status/archive-or-skip path PASS |
| Unauthenticated | All weekly routes denied/redirect |
| `client_viewer` | N/A until such user exists — document as deferred |
| Specialist denial of reviewed/completed/archive | If only admin user exists: **policy covered / not multi-user smoked** |

Do **not** create extra users/passwords in CRUD wave unless a separate bootstrap charter authorizes it.

---

## 7. Audit smoke

If audit implemented:

| Event | When |
|-------|------|
| `weekly_checkpoint.created` | After W4 create |
| `weekly_checkpoint.updated` | After title/field edit |
| `weekly_checkpoint.status_changed` | After status change |
| `weekly_checkpoint.reviewed` / `.completed` | Only if those statuses are entered in smoke |

No secrets in audit payload. If audit deferred, document as SAFE SIMPLIFICATION in implementation result.

---

## 8. Regression smoke

| Check | Expect |
|-------|--------|
| GET `/reporting-periods` (auth) | **200**; `2026-07` / `2026-08` still listed |
| GET `/reporting-periods/1` | **200**; includes weekly checkpoint section/links |
| GET `/login` | **200** |
| GET `/health` | **200** (no secrets) |
| GET `/not-existing` | **404** |
| Auth services / password bootstrap | Untouched |
| Fixture client/project/site | Counts **1/1/1** unchanged |

---

## 9. Data policy

| Rule | Expect |
|------|--------|
| Smoke markers | `LOCAL_FIXTURE_ONLY` on W4 title/text |
| Real client data | None |
| Schema | Unchanged |
| reporting_periods rows | Unchanged by weekly CRUD |
| W1/W2 preferred intact | Confirmed or documented |
| Credentials | Never printed / committed |

---

## 10. STOP conditions

STOP implementation smoke / commit if:

- Preflight fails (root/volume/branch/DB target)
- DB-04 baseline destroyed unexpectedly
- DELETE route/UI introduced
- Monthly editor / report blocks / portal / Topvisor creep in
- Real client data would be written
- Schema/migration mutated
- Non-allowlist paths staged
- Push without charter

Token:

`STOP — I-SEO WEEKLY CHECKPOINTS CRUD VALIDATION SAFETY CONDITION FAILED`

---

## 11. Recommended smoke sequence (next wave)

1. List W1/W2/W3 under period `2026-07`
2. Detail W1
3. Create W4 `2026-07-W4` with `LOCAL_FIXTURE_ONLY`
4. Duplicate W4 refused
5. Edit W4 title/status
6. Mark W4 skipped or archived
7. Parent period detail shows checkpoint section
8. Confirm no DELETE route/UI
9. Regression: reporting periods / login / health / 404
