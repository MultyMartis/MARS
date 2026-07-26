# I-SEO Report Hub — Weekly Checkpoints CRUD Design v0.1

**Status:** DESIGN ONLY — no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-26  
**Authority:** Operator I-SEO Report Hub Weekly Checkpoints CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINTS-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-WEEKLY-CHECKPOINT-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-04-WEEKLY-CHECKPOINTS-SCHEMA-PLAN-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-DESIGN-v0.1.md)

---

## 1. Routes

| Method | Path | Auth | CSRF | Action |
|--------|------|------|------|--------|
| GET | `/reporting-periods/{period_id}/weekly-checkpoints` | Required (internal role) | — | List within period |
| GET | `/reporting-periods/{period_id}/weekly-checkpoints/create` | Required + create capability | — | Create form |
| POST | `/reporting-periods/{period_id}/weekly-checkpoints` | Required + create capability | Required | Store |
| GET | `/weekly-checkpoints/{id}` | Required (internal role) | — | Detail |
| GET | `/weekly-checkpoints/{id}/edit` | Required + edit capability | — | Edit form |
| POST | `/weekly-checkpoints/{id}` | Required + edit capability | Required | Update |

**Not routed in MVP:**

- Separate POST status-only routes (status lives in edit form)
- `DELETE /weekly-checkpoints/{id}`
- Bulk endpoints
- Client-facing checkpoint URLs

**Routing note:** Existing `Router` is exact-match. Register static `/create` segments before parameterized ids. Use request-time exact-path registration (same pattern as Reporting Period CRUD). Nested period paths and flat checkpoint paths must not collide with `/reporting-periods/{id}` or `/reporting-periods/{id}/edit`.

---

## 2. Controller / service / repository

### Controller

`app-source/app/Controllers/WeeklyCheckpointController.php`

Methods (recommended):

- `index(int $periodId)` — list within period
- `show(int $id)` — detail
- `create(int $periodId)` — GET form
- `store(int $periodId)` — POST create
- `edit(int $id)` — GET form
- `update(int $id)` — POST update

Controller responsibilities:

- Auth gate (`isAuthenticated` + internal role / capability)
- CSRF validate on POST
- Map request → service input
- Render views or redirect with flash
- Never echo secrets / stack traces

### Service

`app-source/app/Services/WeeklyCheckpointService.php`

Responsibilities:

- Validation rules (parent period, week_index, key, dates, uniqueness, users)
- Status transition matrix + timestamp policy
- Field lock enforcement
- Role capability checks for mutations
- Audit event emission (recommended)
- Friendly error messages

### Repository

`app-source/app/Repositories/WeeklyCheckpointRepository.php`

Responsibilities:

- List by `reporting_period_id` (ordered by `week_index`)
- Find by id (with parent period join)
- Insert / update
- Exists checks for `(reporting_period_id, week_index)` and `(reporting_period_id, checkpoint_key)`
- Load parent period for context / date range
- Load internal users for owner/reviewer selects

Prefer PDO via existing `DatabaseService`; no new ORM. May reuse `ReportingPeriodRepository` for parent load.

Wire in `routes.php` + `bootstrap.php` (require classes) following Reporting Period CRUD patterns.

---

## 3. Views

| View path | Purpose |
|-----------|---------|
| `app/Views/pages/weekly-checkpoints/index.php` | List under period + empty state + create link |
| `app/Views/pages/weekly-checkpoints/show.php` | Detail + link back to parent period |
| `app/Views/pages/weekly-checkpoints/form.php` | Shared create/edit fields |
| `app/Views/pages/weekly-checkpoints/create.php` | Create wrapper |
| `app/Views/pages/weekly-checkpoints/edit.php` | Edit wrapper |

Optional:

- Partial table/card embedded into `reporting-periods/show.php` (parent period integration)

Reuse:

- `layout.php`, `partials/header.php`
- Existing CSS (`public/assets/css/app.css`); extend status badges if needed
- No CDN / external assets

---

## 4. Form fields

### Create (`GET/POST …/weekly-checkpoints`)

| Field | Control | Required | Notes |
|-------|---------|----------|-------|
| `reporting_period_id` | from route | Yes | Display only; not editable |
| `week_index` | number/select 1–6 | Yes | Smoke W4 → `4` |
| `checkpoint_key` | text | Yes | `YYYY-MM-WN`; may default from period + week |
| `checkpoint_start` | date | Yes | Inside parent period range |
| `checkpoint_end` | date | Yes | ≥ start; inside parent range |
| `status` | select | Yes | Default `draft` |
| `title` | text | Yes | Smoke: include `LOCAL_FIXTURE_ONLY` |
| `summary` | textarea | No | Smoke: `LOCAL_FIXTURE_ONLY` |
| `work_done` | textarea | No | Smoke: `LOCAL_FIXTURE_ONLY` |
| `findings` | textarea | No | |
| `next_steps` | textarea | No | |
| `risks` | textarea | No | |
| `owner_user_id` | select users (nullable) | No | Internal users only |
| `reviewer_user_id` | select users (nullable) | No | Internal users only |
| `_csrf` | hidden | Yes | Via `CsrfService::field()` |

Server-set:

- `created_by` = current user id
- `updated_by` = null on create (or same as created_by — pick one; recommend null until first update)
- `reviewed_at` / `completed_at` = null unless status starts as reviewed/completed (discouraged; prefer draft)

### Edit (`GET/POST /weekly-checkpoints/{id}`)

| Field | Editable when |
|-------|---------------|
| `reporting_period_id` | **Never** (immutable) |
| `week_index` | Only while `status = draft` |
| `checkpoint_key` | Only while `status = draft` |
| `checkpoint_start` / `checkpoint_end` | While `draft` or `in_progress` |
| `status` | Per transition + role matrix |
| Text fields (`title`, `summary`, `work_done`, `findings`, `next_steps`, `risks`) | Until `completed`, unless `admin_owner` |
| `owner_user_id` / `reviewer_user_id` | `admin_owner` / `seo_lead_reviewer` |

Server-set:

- `updated_by` = current user id
- `reviewed_at` / `completed_at` per timestamp policy

---

## 5. List columns

Recommended columns for period-scoped index:

| Column | Source |
|--------|--------|
| Week | `week_index` |
| Key | `checkpoint_key` |
| Title | `title` |
| Status | badge from `status` |
| Dates | `checkpoint_start` – `checkpoint_end` |
| Owner | owner display name (join) |
| Updated | `updated_at` |
| Actions | View / Edit (capability-gated) |

Empty state: clear message + create link when user can create.

---

## 6. Detail fields

Show all schema fields relevant to ops:

- Identity: id, checkpoint_key, week_index
- Parent: reporting period id / period_key / title / status (link to `/reporting-periods/{id}`)
- Dates: checkpoint_start, checkpoint_end
- Status + reviewed_at / completed_at
- Title + all text fields
- Owner / reviewer / created_by / updated_by
- created_at / updated_at

No secrets. No private metrics.

---

## 7. Relation to reporting periods

| Rule | Design |
|------|--------|
| Parent FK | Required; RESTRICT delete |
| Nested list/create | Under `/reporting-periods/{period_id}/weekly-checkpoints…` |
| Flat detail/edit | `/weekly-checkpoints/{id}` (+ `/edit`) |
| Period show integration | Section/table of child checkpoints + links to list/create |
| Parent lock | If parent status is `archived` or `finalized`, create/edit denied for non-`admin_owner` |
| Rollup | MVP does **not** auto-update parent period status from checkpoint changes |

---

## 8. Status workflow

Allowed statuses (DB CHECK + app):

`draft`, `in_progress`, `ready_for_review`, `reviewed`, `completed`, `skipped`, `archived`

Recommended transitions:

| From | To |
|------|----|
| `draft` | `in_progress` |
| `in_progress` | `ready_for_review` |
| `ready_for_review` | `reviewed` |
| `reviewed` | `completed` |
| any non-`completed` | `skipped` |
| any non-`completed` | `archived` |
| `reviewed` / `completed` reopen | `admin_owner` only |

Timestamps:

| Event | Policy |
|-------|--------|
| Enter `reviewed` | Set `reviewed_at` if null |
| Enter `completed` | Set `completed_at` if null |
| Leave reviewed/completed (admin reopen) | **Keep** timestamps as history by default; set `updated_by` + audit |
| Enter `skipped` / `archived` | Do not require `completed_at` |

Status changes occur via the edit form (no separate status POST routes in MVP).

---

## 9. Validation

| Rule | Expect |
|------|--------|
| `reporting_period_id` exists | Required |
| Parent not archived/finalized | Block create/edit unless `admin_owner` |
| `week_index` | Integer 1–6 |
| `checkpoint_key` format | `YYYY-MM-WN` (e.g. `2026-07-W1`) |
| Key period part | Matches parent `period_key` |
| Dates | `checkpoint_start <= checkpoint_end` |
| Dates in parent range | Within parent `period_start`…`period_end` |
| Status | In allowlist + transition legal for role |
| Unique | `(reporting_period_id, week_index)` |
| Unique | `(reporting_period_id, checkpoint_key)` |
| Owner/reviewer | Exist; internal users if set |
| Title | Required; safe length (≤255) |
| Text fields | Safe length caps (TEXT; app soft limits OK) |
| Smoke content | No real client data; prefer `LOCAL_FIXTURE_ONLY` |

Surface uniqueness/CHECK violations as friendly 422-style form errors; no SQL errors in HTML.

---

## 10. Audit

Recommended events:

- `weekly_checkpoint.created`
- `weekly_checkpoint.updated`
- `weekly_checkpoint.status_changed`
- `weekly_checkpoint.reviewed`
- `weekly_checkpoint.completed`

Payload: checkpoint id, period id, old/new status when relevant. No secrets / private metrics.

---

## 11. Navigation

| Surface | Change |
|---------|--------|
| Reporting period show | Weekly checkpoints section/table + links to list/create |
| Weekly list | Breadcrumb/context: parent period |
| Weekly detail | Link back to parent period |
| Header / dashboard | Optional link or card only if needed; period nav remains primary |
| Create | Nested under period |

---

## 12. Error handling

- Unauthenticated → `/login`
- Forbidden role → safe 403 or redirect with flash
- Missing period/checkpoint → safe 404
- Validation failure → re-render form with errors + old input
- CSRF failure → reject; no mutation
- DB unique/CHECK → catch and map to friendly message
- Never leak stack traces, SQL, passwords, hashes, session ids

---

## 13. No-delete policy

| Action | MVP |
|--------|-----|
| DELETE route | **Forbidden** |
| DELETE UI button | **Forbidden** |
| Soft path | `skipped` or `archived` via status on edit form |
| Smoke cleanup DELETE | Not in this feature wave |
| Period delete while children exist | Blocked by FK RESTRICT |

Prefer archive/skip over inventing hard-delete escapes.
