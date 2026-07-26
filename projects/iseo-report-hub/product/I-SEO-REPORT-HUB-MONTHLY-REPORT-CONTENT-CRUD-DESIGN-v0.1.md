# I-SEO Report Hub — Monthly Report Content CRUD Design v0.1

**Status:** DESIGN ONLY — no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Monthly Report Content CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-CONTENT-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-MONTHLY-REPORT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-05-MONTHLY-REPORT-CONTENT-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-DESIGN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md)

---

## 1. Routes

| Method | Path | Auth | CSRF | Action |
|--------|------|------|------|--------|
| GET | `/reporting-periods/{period_id}/monthly-report` | Required (internal role) | — | Detail for period (existing row) or prompt/redirect toward create |
| GET | `/reporting-periods/{period_id}/monthly-report/create` | Required + create capability | — | Create form (only if missing) |
| POST | `/reporting-periods/{period_id}/monthly-report` | Required + create capability | Required | Store (create-if-missing; refuse duplicate) |
| GET | `/monthly-reports/{id}` | Required (internal role) | — | Detail by id |
| GET | `/monthly-reports/{id}/edit` | Required + edit capability | — | Edit form |
| POST | `/monthly-reports/{id}` | Required + edit capability | Required | Update (fields + status) |

**Optional (not required for MVP):**

| Method | Path | Notes |
|--------|------|-------|
| GET | `/monthly-reports` | Admin index only if useful; period-scoped entry is enough |

**Not routed in MVP:**

- Separate POST status-only routes (status lives in edit form)
- `DELETE /monthly-reports/{id}`
- Bulk endpoints
- Client-facing / public share URLs

**Routing note:** Existing `Router` is exact-match. Register static `/create` and `/monthly-report` segments before parameterized collisions. Nested period paths and flat monthly-report paths must not collide with `/reporting-periods/{id}` or weekly checkpoint routes. Prefer request-time exact-path registration (same pattern as Weekly Checkpoints CRUD).

**Create-if-missing UX:**

- If a row already exists for the period: GET create should redirect to detail/edit with flash; POST create must refuse duplicate safely.
- If missing: create form → POST → redirect to detail.

---

## 2. Controller / service / repository

### Controller

`app-source/app/Controllers/MonthlyReportContentController.php`

Methods (recommended):

- `showForPeriod(int $periodId)` — period-scoped detail
- `create(int $periodId)` — GET form when missing
- `store(int $periodId)` — POST create
- `show(int $id)` — detail by id
- `edit(int $id)` — GET form
- `update(int $id)` — POST update

Controller responsibilities:

- Auth gate (`isAuthenticated` + internal role / capability)
- CSRF validate on POST
- Map request → service input
- Render views or redirect with flash
- Never echo secrets / stack traces

### Service

`app-source/app/Services/MonthlyReportContentService.php`

Responsibilities:

- Validation rules (parent period, uniqueness, status transitions, source ids, users, text lengths)
- Status transition matrix + timestamp policy (`reviewed_at` / `finalized_at`)
- Field lock enforcement (immutable period; finalized locks)
- Role capability checks for mutations
- Resolve/default `source_weekly_checkpoint_ids` from parent period checkpoints
- Audit event emission (recommended)
- Friendly error messages

### Repository

`app-source/app/Repositories/MonthlyReportContentRepository.php`

Responsibilities:

- Find by id (with parent period join)
- Find by `reporting_period_id`
- Insert / update
- Exists check for `reporting_period_id` uniqueness
- Load parent period for context / lock checks
- Load weekly checkpoints for the parent period (source selection + link labels)
- Load internal users for owner/reviewer selects
- Optional count by status for dashboard

Prefer PDO via existing `DatabaseService`; no new ORM. May reuse `ReportingPeriodRepository` / `WeeklyCheckpointRepository` for parent/source loads.

Wire in `routes.php` + `bootstrap.php` (require classes) following Weekly Checkpoint / Reporting Period CRUD patterns.

---

## 3. Views

| View path | Purpose |
|-----------|---------|
| `app/Views/pages/monthly-reports/show.php` | Detail / preview + parent context + source checkpoint links |
| `app/Views/pages/monthly-reports/form.php` | Shared create/edit fields (textareas + status + sources) |
| `app/Views/pages/monthly-reports/create.php` | Create wrapper |
| `app/Views/pages/monthly-reports/edit.php` | Edit wrapper |
| optional `app/Views/pages/monthly-reports/index.php` | Only if top-level index is implemented |

Parent integration:

- Update `app/Views/pages/reporting-periods/show.php` with a monthly report section (status/title/link/edit or create link)

Reuse:

- `layout.php`, `partials/header.php`
- Existing CSS (`public/assets/css/app.css`); extend status badges if needed
- No CDN / external assets

---

## 4. Form fields

### Create (`GET/POST …/monthly-report`)

| Field | Control | Required | Notes |
|-------|---------|----------|-------|
| `reporting_period_id` | from route | Yes | Display only; not editable |
| `title` | text | Yes | Smoke: keep / include `LOCAL_FIXTURE_ONLY` |
| `status` | select | Yes | Default `draft` |
| `executive_summary` | textarea | No | Smoke: `LOCAL_FIXTURE_ONLY` |
| `work_completed` | textarea | No | |
| `results_summary` | textarea | No | |
| `key_findings` | textarea | No | |
| `risks_and_blockers` | textarea | No | |
| `next_month_plan` | textarea | No | |
| `client_notes` | textarea | No | |
| `internal_notes` | textarea | No | |
| `source_weekly_checkpoint_ids` | multi-select / checkboxes of period checkpoints | No | Default all current period checkpoint ids when present |
| `owner_user_id` | select users (nullable) | No | Internal users only |
| `reviewer_user_id` | select users (nullable) | No | Internal users only |
| `_csrf` | hidden | Yes | Via `CsrfService::field()` |

Server-set:

- `created_by` = current user id
- `updated_by` = null on create (or same as created_by — pick one; recommend null until first update)
- `reviewed_at` / `finalized_at` = null unless status starts as reviewed/finalized (discouraged; prefer draft)

### Edit (`GET/POST /monthly-reports/{id}`)

| Field | Editable when |
|-------|---------------|
| `reporting_period_id` | **Never** (immutable) |
| `title` | Until `finalized`, unless `admin_owner` |
| Content TEXT fields | Until `finalized`, unless `admin_owner` |
| `source_weekly_checkpoint_ids` | Until `finalized`, unless `admin_owner` |
| `status` | Per transition + role matrix |
| `owner_user_id` / `reviewer_user_id` | `admin_owner` / `seo_lead_reviewer` |

Server-set:

- `updated_by` = current user id
- `reviewed_at` / `finalized_at` per timestamp policy

---

## 5. Detail page fields

Show all schema fields relevant to ops:

- Identity: id, title, status badge
- Parent: reporting period id / period_key / title / status (link to `/reporting-periods/{id}`)
- Status timestamps: reviewed_at / finalized_at
- All content TEXT sections
- Source weekly checkpoints: resolved list with links to `/weekly-checkpoints/{id}` (key/status/title)
- Owner / reviewer / created_by / updated_by
- created_at / updated_at

No secrets. No private metrics. No DELETE control.

---

## 6. Relation to reporting periods

| Rule | Design |
|------|--------|
| Parent FK | Required; RESTRICT delete |
| Uniqueness | Exactly one monthly content row per period |
| Nested detail/create | Under `/reporting-periods/{period_id}/monthly-report…` |
| Flat detail/edit | `/monthly-reports/{id}` (+ `/edit`) |
| Period show integration | Monthly report section: if exists → status/title/view/edit; if missing → create link |
| Parent lock | If parent status is `archived` or `finalized`, create/edit denied for non-`admin_owner` |
| Rollup | MVP does **not** auto-update parent period status from monthly content changes |

---

## 7. Relation to weekly checkpoints

| Rule | Design |
|------|--------|
| Source hint | JSON array `source_weekly_checkpoint_ids` |
| Validation | Each id exists; belongs to same `reporting_period_id`; valid JSON array |
| Empty sources | Allowed; show warning / “no sources selected” |
| UI | Checkboxes/multi-select of parent period checkpoints; detail page shows links |
| Coupling | Weekly status changes do **not** auto-change monthly status |
| Aggregation | No automatic copy of weekly TEXT into monthly TEXT |
| Mutation | Monthly CRUD must **not** UPDATE/DELETE weekly checkpoint rows |

Prefer resolving smoke sources by checkpoint_key (`2026-07-W1`…`W4`) rather than hard-coding ids in application logic; fixture docs may still cite known ids `[1,2,3,7]`.

---

## 8. Status workflow

Allowed statuses (DB CHECK + app):

`draft`, `in_progress`, `ready_for_review`, `reviewed`, `finalized`, `archived`

Recommended transitions:

| From | To |
|------|----|
| `draft` | `in_progress` |
| `in_progress` | `ready_for_review` |
| `ready_for_review` | `reviewed` |
| `reviewed` | `finalized` |
| any non-`finalized` | `archived` |
| `ready_for_review` | `in_progress` (revision request; optional if simple) |
| `finalized` reopen | `draft` or `in_progress` — **`admin_owner` only** |
| `archived` reopen | Prefer `admin_owner` only |

Timestamps:

| Event | Policy |
|-------|--------|
| Enter `reviewed` | Set `reviewed_at` if null |
| Enter `finalized` | Set `finalized_at` if null |
| Leave reviewed/finalized (admin reopen) | **Keep** timestamps as history by default; set `updated_by` + audit |
| Enter `archived` | Do not require `finalized_at` |

Finalized content locked except `admin_owner`. Status changes occur via the edit form (no separate status POST routes in MVP).

---

## 9. Validation

| Rule | Expect |
|------|--------|
| `reporting_period_id` exists | Required |
| Only one monthly row per period | Unique guard + friendly error |
| Parent not archived/finalized | Block create/edit unless `admin_owner` |
| `title` | Required; ≤255 |
| Status | In allowlist + transition legal for role |
| `source_weekly_checkpoint_ids` | Valid JSON array; ids exist; same period; empty OK with warn |
| Text fields | Soft length ≤20000 chars each (unless existing convention differs) |
| Owner/reviewer | Exist; internal users if set |
| Smoke content | No real client data; prefer `LOCAL_FIXTURE_ONLY` |

Surface uniqueness/CHECK/JSON violations as friendly form errors; no SQL errors in HTML.

---

## 10. Audit

Recommended events:

- `monthly_report_content.created`
- `monthly_report_content.updated`
- `monthly_report_content.status_changed`
- `monthly_report_content.reviewed`
- `monthly_report_content.finalized`
- `monthly_report_content.archived`

Payload: monthly content id, period id, old/new status when relevant. No secrets / private metrics.

---

## 11. Navigation

| Surface | Change |
|---------|--------|
| Reporting period show | Monthly report section + view/edit or create |
| Monthly detail | Link back to parent period; source weekly checkpoint links |
| Monthly edit/create | Parent period context always visible |
| Header top-level | Optional; **not required** — monthly is period-scoped |
| Dashboard | Optional count / ready_for_review count if simple |

---

## 12. Error handling

- Unauthenticated → `/login`
- Forbidden role → safe 403 or redirect with flash
- Missing period/monthly row → safe 404 (or create prompt on period path when missing)
- Duplicate create → friendly error / redirect to existing
- Validation failure → re-render form with errors + old input
- CSRF failure → reject; no mutation
- DB unique/CHECK/JSON → catch and map to friendly message
- Never leak stack traces, SQL, passwords, hashes, session ids

---

## 13. No-delete policy

| Action | MVP |
|--------|-----|
| DELETE route | **Forbidden** |
| DELETE UI button | **Forbidden** |
| Soft path | `archived` via status on edit form |
| Smoke cleanup DELETE | Not in this feature wave |
| Period delete while monthly exists | Blocked by FK RESTRICT |
| Archive frees unique slot | **No** — reopen/edit the same row |

Prefer archive over inventing hard-delete escapes.
