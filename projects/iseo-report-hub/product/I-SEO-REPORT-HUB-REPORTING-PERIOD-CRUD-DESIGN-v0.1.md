# I-SEO Report Hub — Reporting Period CRUD Design v0.1

**Status:** DESIGN ONLY — no app-source/runtime/DB mutation  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-25  
**Authority:** Operator I-SEO Report Hub Reporting Period CRUD Charter 01  
**Related:** [I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-CRUD-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md](I-SEO-REPORT-HUB-REPORTING-PERIOD-LIFECYCLE-v0.1.md), [I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md](I-SEO-REPORT-HUB-DB-03-REPORTING-PERIODS-SCHEMA-PLAN-v0.1.md)

---

## 1. Routes

| Method | Path | Auth | CSRF | Action |
|--------|------|------|------|--------|
| GET | `/reporting-periods` | Required (internal role) | — | List |
| GET | `/reporting-periods/create` | Required + create capability | — | Create form |
| POST | `/reporting-periods` | Required + create capability | Required | Store |
| GET | `/reporting-periods/{id}` | Required (internal role) | — | Detail |
| GET | `/reporting-periods/{id}/edit` | Required + edit capability | — | Edit form |
| POST | `/reporting-periods/{id}` | Required + edit capability | Required | Update |

**Not routed in MVP:**

- `DELETE /reporting-periods/{id}`
- Bulk endpoints
- Client-facing period URLs

**Routing note:** Register static `/reporting-periods/create` before parameterized `{id}` routes so `create` is not captured as an id.

---

## 2. Controller / service / repository

### Controller

`app-source/app/Controllers/ReportingPeriodController.php`

Methods (recommended):

- `index()` — list
- `show(int $id)` — detail
- `create()` — GET form
- `store()` — POST create
- `edit(int $id)` — GET form
- `update(int $id)` — POST update

Controller responsibilities:

- Auth gate (`isAuthenticated` + internal role / capability)
- CSRF validate on POST
- Map request → service input
- Render views or redirect with flash
- Never echo secrets / stack traces

### Service

`app-source/app/Services/ReportingPeriodService.php` (preferred orchestration)

Responsibilities:

- Validation rules
- Role capability checks for mutations
- `finalized_at` policy
- Audit event emission (optional but recommended)
- Friendly error messages

### Repository

`app-source/app/Repositories/ReportingPeriodRepository.php` **or** repository methods inside the service if keeping the layer count low for MVP.

Responsibilities:

- List with joins (project, client, owner/reviewer names)
- Find by id
- Insert / update
- Exists check for `(project_id, period_key)`
- Load project options for create form
- Load internal users for owner/reviewer selects

Prefer PDO via existing `DatabaseService` patterns; no new ORM.

---

## 3. Views

| View path | Purpose |
|-----------|---------|
| `app/Views/pages/reporting-periods/index.php` | List table + empty state + create link |
| `app/Views/pages/reporting-periods/show.php` | Detail |
| `app/Views/pages/reporting-periods/form.php` | Shared create/edit form |

Reuse:

- `layout.php`
- `partials/header.php` (nav link added)
- Existing CSS (`public/assets/css/...` as present); minimal additions only if needed

Optional small JS: none required for MVP (no client-side SPA). Optional helper to derive `period_key` from start date may be plain HTML/PHP defaulting.

---

## 4. Form fields

### Create (`GET/POST /reporting-periods`)

| Field | Control | Required | Notes |
|-------|---------|----------|-------|
| `project_id` | `<select>` of existing projects | Yes | Local fixture: Demo SEO Project |
| `period_key` | text (`YYYY-MM`) | Yes | May auto-suggest from start month |
| `period_start` | date | Yes | Prefer first day of month |
| `period_end` | date | Yes | Prefer last day of month |
| `status` | select | Yes | Default `draft` |
| `title` | text | No | Smoke: include `LOCAL_FIXTURE_ONLY` when demo |
| `summary` | textarea | No | Smoke: `LOCAL_FIXTURE_ONLY` |
| `owner_user_id` | select users (nullable) | No | Internal roles only |
| `reviewer_user_id` | select users (nullable) | No | Internal roles only |
| `_csrf` | hidden | Yes | Via `CsrfService::field()` |

Server-set (not user inputs):

- `created_by` = current user id
- `updated_by` = null on create (or same as created_by — pick one; recommend null until first update)
- `finalized_at` = null unless status starts as `finalized` (discouraged; default draft)

### Edit (`GET/POST /reporting-periods/{id}`)

Editable inputs:

- `status`
- `title`
- `summary`
- `owner_user_id`
- `reviewer_user_id`
- `period_start` / `period_end` — only if status in (`draft`, `active`)
- `period_key` — only if status = `draft`

Immutable on edit form (display only):

- `id`
- `project_id` / project name
- `created_by` / `created_at`

Server-set:

- `updated_by` = current user id
- `finalized_at` per status policy

---

## 5. List columns

| Column | Source |
|--------|--------|
| ID | `reporting_periods.id` |
| Period key | `period_key` |
| Title | `title` (fallback to period_key) |
| Project | `projects.name` |
| Client | `clients.name` via project |
| Date range | `period_start` – `period_end` |
| Status | `status` (visible badge/text) |
| Owner | owner user name/email or `—` |
| Reviewer | reviewer user name/email or `—` |
| Actions | View / Edit (capability-gated) |

Empty state: message + link to create when user can create.  
With fixture: at least one demo row (`2026-07`) visible after auth.

---

## 6. Detail fields

Show:

- id, period_key, title, summary, status, finalized_at
- period_start, period_end
- project name + slug + id
- client name + slug
- primary site url/label if join practical
- owner / reviewer
- created_by / updated_by + timestamps
- Actions: Edit (if allowed); Back to list

Do **not** show weekly/monthly content panels (out of scope) — optional placeholder text: “Weekly checkpoints / monthly report content: not implemented”.

---

## 7. Status workflow

Allowed statuses (DB ENUM / app set):

```text
draft | active | weekly_review | monthly_review | finalized | archived
```

Happy path:

```text
draft → active → weekly_review → monthly_review → finalized → archived
```

Revision path:

```text
monthly_review → active → monthly_review → finalized
```

### `finalized_at` policy

| Transition | `finalized_at` |
|------------|----------------|
| Any → `finalized` | Set to current timestamp if null; if already set, keep (or refresh — MVP: set if null, else keep) |
| `finalized` → other (admin/lead exceptional) | Clear to NULL |
| Other transitions | Leave unchanged |

Archive = set `status = archived` (no DELETE).

Specialist cannot transition to `finalized` or `archived`.  
Account manager cannot change status.

---

## 8. Validation

Application-level (mandatory):

| Rule | Error (safe) |
|------|--------------|
| Auth + CSRF on POST | Redirect with flash; do not process |
| `project_id` exists | “Selected project was not found.” |
| `period_key` matches `^[0-9]{4}-(0[1-9]|1[0-2])$` | “Period key must be YYYY-MM.” |
| `period_start <= period_end` | “Period start must be on or before period end.” |
| Month of `period_start` equals `period_key` | “Period key must match the start month.” |
| `status` in allowed set | “Invalid status.” |
| Unique `(project_id, period_key)` | “A reporting period for this project and month already exists.” |
| Owner/reviewer null or existing user with internal role | “Owner/reviewer must be an internal user.” |
| Role capability for action | 403 page or redirect with flash |
| Field locks (key/dates) | “Period key can only be changed while draft.” / similar |

DB constraints remain backstop (unique, FK, CHECK). Catch PDO unique violation and map to friendly message.

No stack traces to browser. Log minimally if existing logger pattern exists; otherwise silent safe flash only.

---

## 9. Audit

Optional but recommended events via existing `audit_log` patterns:

| Event | When | Metadata (safe) |
|-------|------|-----------------|
| `reporting_period.created` | Successful create | id, project_id, period_key, status |
| `reporting_period.updated` | Successful update (non-status or any update) | id, changed field names only |
| `reporting_period.status_changed` | Status value changed | id, from, to |

Rules:

- No passwords / secrets / PII dumps
- Actor = current user id
- Failures of audit write should not silently corrupt period write — prefer same transaction or best-effort after commit; document choice in implementation (recommend same transaction if easy).

---

## 10. Navigation

Update:

- `partials/header.php` — add “Reporting periods” link when `$currentUser !== null`
- `DashboardController` cards — set Reporting CRUD card to “ready” / link to `/reporting-periods` after implementation
- Optional dashboard quick link button

No external CDN. Keep current visual language.

---

## 11. Error handling

| Case | Behavior |
|------|----------|
| Unauthenticated | Redirect `/login` |
| Authenticated without internal role / client_viewer | Deny (403 or login redirect) |
| CSRF fail | Flash warn; redirect back |
| Validation fail | Re-render form with errors + old input (create/edit) |
| Not found id | 404 via existing not-found path or dedicated flash + redirect list |
| Unique conflict | Form error; no partial commit |
| Unexpected DB error | Generic flash; HTTP 500 page without stack |

---

## 12. No-delete policy

- No DELETE route, method, or UI control in MVP.
- Soft retirement = `status = archived`.
- Future hard delete requires explicit destructive charter + child-table review (DB-04+ RESTRICT).
- Smoke must not DELETE fixture or smoke periods unless separately approved.
