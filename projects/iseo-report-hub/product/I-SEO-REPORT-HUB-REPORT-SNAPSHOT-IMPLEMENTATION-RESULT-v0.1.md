# I-SEO Report Hub — Report Snapshot Implementation Result v0.1

**Status:** COMPLETE  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-27  
**Authority:** Operator I-SEO Report Hub Report Snapshot Implementation 01  
**Related:** [I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md](I-SEO-REPORT-HUB-REPORT-SNAPSHOT-CHARTER-v0.1.md), [I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md](I-SEO-REPORT-HUB-DB-07-REPORT-SNAPSHOTS-MIGRATION-APPLY-RESULT-v0.1.md)

---

## 1. Status

| Item | Value |
|------|-------|
| Wave | **complete** |
| Snapshot service implemented | **yes** |
| Snapshot routes implemented | **yes** |
| Snapshot v1 created | **yes** (`id=1`, `monthly-1-v1`) |
| Idempotency | **yes** (repeat POST → same active row; audit `report_snapshot.idempotent_hit`) |
| Final DB state | migrations **6**; tables **14**; `report_snapshots` **1**; monthly **1** `finalized`; blocks **6** `reviewed`; periods **2**; weekly **4** |
| No public/export/PDF | **yes** |

---

## 2. Source Changes

Created:

- `app-source/app/Controllers/ReportSnapshotController.php`
- `app-source/app/Services/ReportSnapshotService.php`
- `app-source/app/Repositories/ReportSnapshotRepository.php`
- `app-source/app/Views/pages/report-snapshots/show.php`

Modified:

- `app-source/app/routes.php`
- `app-source/app/bootstrap.php`
- `app-source/app/Controllers/MonthlyReportContentController.php`
- `app-source/app/Controllers/ReportPreviewController.php`
- `app-source/app/Views/pages/monthly-reports/show.php`
- `app-source/app/Views/pages/report-preview/show.php` (print includes this)
- `app-source/public/assets/css/app.css`
- `app-source/README.md`

Not modified: Auth/CSRF/Database/Health services; migrations; tools; `app.js`.

---

## 3. Runtime Changes

Exact allowlist sync source → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`:

- mirrors of all created/modified app-source files listed above (except docs).

`.env.local` untouched. No broad sync.

---

## 4. Routes

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/monthly-reports/{id}/snapshot` | Active snapshot summary or “no snapshot yet” |
| POST | `/monthly-reports/{id}/snapshot` | Create / idempotent return (CSRF) |
| GET | `/report-snapshots/{id}` | Immutable snapshot detail |

No DELETE. No public. No PDF/export.

---

## 5. Snapshot Rules

| Rule | Policy |
|------|--------|
| Gates | monthly exists; status `finalized`; `finalized_at` present; preview assemble; render mode `blocks_primary`/`flat_fallback`; non-archived blocks; required canonical keys; no draft/in_progress; weekly refs resolve; create roles `admin_owner` / `seo_lead_reviewer` |
| Payload | metadata / period / client / project / site / monthly_report / ordered blocks / weekly_sources / diagnostics / render |
| Checksum | SHA-256 over canonical key-sorted JSON; excludes volatile `created_at` / `generated_at`; `snapshot_version` null in hash identity |
| Idempotency | active same checksum → return existing + `report_snapshot.idempotent_hit` |
| Versioning | v1 created; v2 after reopen/re-finalize deferred (supersede scaffolding present) |

---

## 6. Access / Auth

- Auth required for all snapshot routes.
- View: internal roles except `client_viewer`.
- Create: `admin_owner`, `seo_lead_reviewer`.
- CSRF on POST.
- Smoke limitation: HTTP smoke via admin_owner session injection only (single local user).

---

## 7. DB Actions

| Metric | Before | After |
|--------|--------|-------|
| schema_migrations | 6 | 6 |
| tables | 14 | 14 |
| report_snapshots | 0 | **1** |
| monthly_report_contents | 1 | 1 |
| report_blocks | 6 | 6 |
| reporting_periods | 2 | 2 |
| weekly_checkpoints | 4 | 4 |

Snapshot row:

- `id` 1; `monthly_report_content_id` 1; `reporting_period_id` 1
- `snapshot_key` `monthly-1-v1`; `version` 1; `status` `active`
- `render_mode` `blocks_primary`
- checksum short `0d0c863c5c28…` (64 hex)
- `source_block_ids` 6; `source_weekly_checkpoint_ids` `[1,2,3,7]`
- `rendered_text` present; `rendered_html` null

No monthly/report_blocks/period/weekly mutations. Audit: `report_snapshot.created`, `report_snapshot.idempotent_hit`.

---

## 8. UI / Preview Integration

- Monthly detail: snapshot card (none / active meta + view link + create when allowed).
- Preview: snapshot state cue + link.
- Snapshot detail: immutable badge, metadata, checksum, ordered blocks, weekly refs; no edit/delete/public.

---

## 9. Smoke Tests

**64/64 PASS** — lint; unauth deny; create v1; payload 6 blocks; checksum stable; idempotent second POST; monthly card; preview cue; preview/print; regression (`/health`, `/login`, periods, weekly, monthly, blocks); DB invariants.

---

## 10. Restrictions

Confirmed: no production/remote DB; no real client data; no schema edits; no db-migrate; no DELETE/DROP/TRUNCATE; no PDF/export/public share; no secrets in Git/report; no `.env` commit; runtime `.env.local` not printed/committed; no push.

---

## 11. What Still Does Not Exist

- PDF / export
- public share / client portal
- v2 versioning smoke
- snapshot vs source diff UI
- archive/supersede UI
- client approval

---

## 12. Next Phase

**Report Export / PDF Charter 01**

---

## 13. SAFE UNKNOWN

- Multi-role HTTP smoke beyond admin_owner (local fixture has one user).
- Exact Apache session cookie domain/path variance across alternate Laragon profiles.
- Future checksum stability if payload schema fields are intentionally extended without version bump.
