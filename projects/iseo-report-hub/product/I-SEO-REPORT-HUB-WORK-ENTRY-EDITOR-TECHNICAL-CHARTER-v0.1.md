# I-SEO Report Hub — Work Entry Editor Technical Charter v0.1

**Status:** CHARTER FOR FUTURE IMPLEMENTATION — **do not implement in this wave**  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-08-17  
**Wave:** Work Entry Editor Charter 01  
**Recommended next impl wave:** `I-SEO Report Hub — Work Entry Editor Implementation 01`

---

## 1. Goal

Implement the MVP editor against existing DB-11 tables and read-only UI, with **no new migration**.

Source of truth: `projects/iseo-report-hub/app-source/`  
Runtime sync (implementation wave only): `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`

---

## 2. Schema

| Change | Decision |
|--------|----------|
| New migration | **No** |
| ALTER / CHECK change | **No** |
| New table | **No** |
| Seed mutation of 13/31 catalogue rows | **No** |
| `monthly_report_work_entries` writes | **Yes** (INSERT/UPDATE only) in implementation wave |

Existing columns are sufficient (see Field Contract).

---

## 3. Routes

Add in `app/routes.php`. **More specific patterns before** `/monthly-reports/(\d+)$`.

```
GET  /monthly-reports/{id}/work-entries/create
POST /monthly-reports/{id}/work-entries
GET  /monthly-report-work-entries/{entry_id}/edit
POST /monthly-report-work-entries/{entry_id}
```

Do **not** add:

- `DELETE` / `POST .../delete`
- `POST .../status`
- public `/share/...` variants

Wire new controller methods in the same `preg_match` / `$router->get|post` style as report blocks.

---

## 4. Controller

**New file:** `app/Controllers/MonthlyReportWorkEntryController.php`

Extend `BaseController`. Constructor needs: Auth, Csrf, View, Config, plus repositories (and optional thin service).

| Method | Behavior |
|--------|----------|
| `create(int $monthlyReportId)` | Auth; load monthly report; 404 if missing; render form; catalogue option lists |
| `store(int $monthlyReportId)` | POST + CSRF; validate; insert; redirect show `#work-entries` |
| `edit(int $entryId)` | Auth; load entry + parent; 404; render form |
| `update(int $entryId)` | POST + CSRF; validate; **do not change** `monthly_report_id` / `created_by_user_id`; update; redirect |

Reuse `requireInternalUser()`, `guardMethod(['POST'])`, flash, deny/404 helpers from existing CRUD.

**Do not** fold write actions into `MonthlyReportContentController` beyond adding list CTAs / `$canCreateWorkEntry` flags on `renderShow`.

Show page changes:

- Pass `canCreateWorkEntry` / per-card edit hrefs (all internal users who can see the page may edit in this MVP).
- Replace “editor later” notice with operational + finalized warnings per UX Flows.

---

## 5. Service (recommended, thin)

**New file:** `app/Services/MonthlyReportWorkEntryService.php`

Mirrors `ReportBlockService` at a smaller scale: validate payload, derive category/title, persist via repository. Keeps controller free of SQL.

If Implementation 01 stays very small, validation may live in the controller **only if** the file remains readable. Preferred: service.

---

## 6. Repository methods

**Edit:** `app/Repositories/MonthlyReportWorkEntryRepository.php`

Existing: `findById`, `listByMonthlyReportId`, counts (already join category/item — treat `findById` as `findWithRelations`).

**Add:**

| Method | Purpose |
|--------|---------|
| `create(array $row): int` | INSERT; return new id |
| `update(int $id, array $row): bool` | UPDATE by id; never writes `monthly_report_id` or `created_by_user_id` |

**Edit (read lists for forms):**

- `SeoWorkCategoryRepository::listActive()` — already exists  
- `SeoWorkItemRepository::listActive()` / `listByCategoryId()` — already exist  

No catalogue write methods.

Bind PDO parameters. Do not interpolate user strings into SQL.

---

## 7. Views

| File | Role |
|------|------|
| `app/Views/pages/monthly-report-work-entries/create.php` | Thin wrapper → form partial |
| `app/Views/pages/monthly-report-work-entries/edit.php` | Thin wrapper → form partial |
| `app/Views/pages/monthly-report-work-entries/form.php` | Shared form (`$mode` = create\|edit) |
| `app/Views/partials/monthly-work-entries.php` | Add CTA + «Изменить»; update notice; dim cancelled/deferred |

Follow `report-blocks/create.php` + `form.php` include pattern.

Layout: existing app layout / `rp-form` classes.

---

## 8. Support / CSS

| File | Change |
|------|--------|
| `app/Support/UiLabels.php` | Only if new strings are needed; enums already mapped |
| `app/Support/helpers.php` | Only if a new `ui_*` helper is required |
| `public/assets/css/app.css` | Minimal: form spacing if needed; `work-entry-card--inactive`; do not restyle the 6-block client template |

No new JS module required.

---

## 9. DI / routes bootstrap

`app/routes.php` already constructs `MonthlyReportWorkEntryRepository`. Implementation must construct the new controller (and service) next to `$monthlyReports` / `$reportBlocks`.

Do not change public share controller wiring.

---

## 10. Runtime sync allowlist (implementation wave)

Exact source → runtime copy of **changed** files only, typical set:

- `app/Controllers/MonthlyReportWorkEntryController.php` (new)
- `app/Services/MonthlyReportWorkEntryService.php` (new, if used)
- `app/Repositories/MonthlyReportWorkEntryRepository.php`
- `app/Controllers/MonthlyReportContentController.php` (show flags only)
- `app/routes.php`
- `app/Views/pages/monthly-report-work-entries/*`
- `app/Views/partials/monthly-work-entries.php`
- `app/Support/UiLabels.php` / `helpers.php` if touched
- `public/assets/css/app.css` if touched

**Never sync:** `.env`, `.env.local`, `storage/`, export artifacts, vendor, WordPress, DB dumps.

---

## 11. Backup before implementation validation

**Required.** Path:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\work-entry-editor-implementation-01\backup\`

Suggested files:

- Full local dump: `iseo_report_hub_dev-before-work-entry-editor-YYYYMMDD-HHMMSS.sql`
- Table dump: `monthly_report_work_entries-before.sql`

Method: Laragon `mysqldump --single-transaction` (same as Catalogue Implementation 01). Not committed to git.

---

## 12. Validation plan (implementation wave)

See Safety Policy for mutation strategy (Option D default).

Technical checks:

1. PHP lint on all changed PHP.  
2. Before counts: entries_r1 = 7; blocks = 6; exports = 4; shares = 7 (active 1 / revoked 6); export 4 checksum prefix `a8c4d61c6216e8d70b19`.  
3. GET create/edit 200 (auth).  
4. POST create test entry.  
5. POST update that entry (`deferred` + `internal`).  
6. GET monthly show lists the test card then, after cleanup, 7 again (if Option D).  
7. Unauthenticated POST → login.  
8. Invalid CSRF → fail closed.  
9. Invalid enum → re-render errors.  
10. Confirm **no** DELETE route (404 or no match).  
11. Share/export/PDF unchanged.  
12. HTTP smoke of existing monthly/preview/blocks/exports/shares routes still 200.

---

## 13. Git (implementation wave)

Exact-path commits only under `projects/iseo-report-hub/`. Foreign WIP preserved. No push unless a later operator charter says so.

This charter wave: docs only.

---

## 14. Explicit non-goals

- DB-12 / any migration  
- Summary assembly  
- PDF regen  
- Catalogue editor  
- Reopen of monthly report 1  
