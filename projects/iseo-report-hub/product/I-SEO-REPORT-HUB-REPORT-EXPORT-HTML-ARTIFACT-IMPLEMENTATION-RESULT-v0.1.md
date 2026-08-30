# I-SEO Report Hub — Report Export HTML Artifact Implementation Result v0.1

**Status:** complete  
**Date:** 2026-07-27  
**Programme:** i-SEO Report Hub  
**Branch:** `mars/canonical-post-recovery`

---

## 1. Status

| Item | Value |
|------|-------|
| Overall | **complete** |
| Export service implemented | **yes** |
| Export routes implemented | **yes** |
| HTML artifact created | **yes** |
| Metadata row created | **yes** (`report_exports.id` **1**) |
| Idempotency | **yes** — repeat POST returns existing export; row count stays **1**; artifact checksum stable |
| Final DB state | migrations **7**; tables **15**; `report_exports` **1**; `report_snapshots` **1** unchanged; monthly/blocks/periods/weekly unchanged |
| No PDF/public/share | **yes** |

---

## 2. Source Changes

**Created**

- `app-source/app/Controllers/ReportExportController.php`
- `app-source/app/Services/ReportExportService.php`
- `app-source/app/Repositories/ReportExportRepository.php`
- `app-source/app/Views/pages/report-exports/index.php`
- `app-source/app/Views/pages/report-exports/show.php`

**Modified**

- `app-source/app/routes.php`
- `app-source/app/bootstrap.php`
- `app-source/app/Controllers/ReportSnapshotController.php`
- `app-source/app/Views/pages/report-snapshots/show.php`
- `app-source/app/Views/pages/monthly-reports/show.php`
- `app-source/public/assets/css/app.css`
- `app-source/README.md`

---

## 3. Runtime Changes

**Synced (exact allowlist)**

- `app/routes.php`
- `app/bootstrap.php`
- `app/Controllers/ReportExportController.php`
- `app/Services/ReportExportService.php`
- `app/Repositories/ReportExportRepository.php`
- `app/Controllers/ReportSnapshotController.php`
- `app/Views/pages/report-exports/index.php`
- `app/Views/pages/report-exports/show.php`
- `app/Views/pages/report-snapshots/show.php`
- `app/Views/pages/monthly-reports/show.php`
- `public/assets/css/app.css`

`.env.local` — **untouched** (not read into Git; not modified).

---

## 4. Artifact

| Field | Value |
|-------|-------|
| Relative path | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html` |
| Absolute runtime path | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html` |
| File size | **5360** bytes |
| File checksum (SHA-256) | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| Outside public webroot | **yes** |
| Not in Git | **yes** |

---

## 5. Routes

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/report-snapshots/{id}/exports` | List exports for snapshot |
| POST | `/report-snapshots/{id}/exports/html` | Create/idempotent HTML export |
| GET | `/report-exports/{id}` | Export metadata detail |
| GET | `/report-exports/{id}/download` | Authenticated artifact download |

No PDF, public share, or token routes.

---

## 6. Export Rules

| Rule | Implementation |
|------|----------------|
| Source of truth | `report_snapshots` payload/fields only — **not** live `report_blocks` / monthly content |
| Gates | Snapshot exists; status `active`; valid payload; format `html`; create roles `admin_owner` / `seo_lead_reviewer` |
| Artifact generation | Standalone HTML; embedded CSS; escaped content; snapshot header; blocks; weekly refs; flat fields |
| Metadata | `report_exports` row with relative `storage_path`, file checksum, source snapshot checksum |
| Idempotency | Ready HTML export for same snapshot checksum + existing file → return existing; no duplicate row |
| Missing file policy | If metadata exists but file missing → fail safely (no silent row mutation) |
| Download policy | Auth-only controller stream; path traversal rejected; no direct filesystem URL |
| PDF | **Deferred** — not implemented |

---

## 7. Access / Auth

| Role | Create HTML | View / download |
|------|-------------|-----------------|
| admin_owner | yes | yes |
| seo_lead_reviewer | yes | yes |
| seo_specialist | no | yes |
| account_client_manager | no | yes |
| internal_viewer | no | yes |
| client_viewer | no | no |

Smoke limitation: HTTP smoke used **admin_owner** session injection only (single local fixture user).

---

## 8. DB Actions

| Check | Before | After |
|-------|--------|-------|
| schema_migrations | 7 | 7 |
| tables | 15 | 15 |
| report_exports | 0 | **1** |
| report_snapshots | 1 | 1 (unchanged) |
| monthly_report_contents | 1 finalized | 1 finalized |
| report_blocks | 6 reviewed | 6 reviewed |

**Export row (id 1)**

- `export_key` = `snapshot-1-html-v1`
- `format` = `html`
- `status` = `ready`
- `storage_path` = `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html`
- `source_snapshot_checksum_sha256` = `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38`

**Idempotency:** second POST — count remains **1**; same export id; artifact checksum stable.

**Audit events:** `report_export.created`, `report_export.idempotent_hit` (on repeat POST).

No snapshot/monthly/block/period/weekly mutations. No DELETE/DROP/TRUNCATE.

---

## 9. UI / Snapshot Integration

- Snapshot detail — HTML export card (create / metadata / download / idempotent re-check)
- Export index — table of exports per snapshot
- Export detail — immutable metadata + download button
- Monthly report — link to snapshot exports when snapshot exists

---

## 10. Smoke Tests

| Suite | Result |
|-------|--------|
| PHP lint (changed PHP files) | **0 errors** |
| DB preflight | PASS |
| Unauth GET/POST exports | PASS (redirect login) |
| Auth create HTML export | PASS |
| Artifact file + checksum vs DB | PASS |
| Download content | PASS (snapshot key, period, checksum, summary fields; no script tags) |
| Idempotent second POST | PASS |
| Snapshot export card | PASS |
| Regression routes | PASS (47/47; `/login` returns 302 when already authenticated — expected) |
| No PDF/public routes | PASS |

HTTP smoke host: `127.0.0.1:8088` PHP built-in server (Apache not listening on port 80 this session).

---

## 11. Restrictions

Confirmed: no production DB; no real client data; no schema edits; no db-migrate; no auth/health edits; no fixture tool changes; no business row mutations; no DELETE/DROP/TRUNCATE; no PDF/public share; no public webroot writes; no secrets in Git/reports; no push.

---

## 12. What Still Does Not Exist

- PDF export
- Public share / client portal download
- Email delivery
- Object storage
- Export archive UI
- Forced regeneration
- Multi-format exports beyond HTML

---

## 13. Next Phase

**Report Export PDF Engine Charter 01**

---

## 14. SAFE UNKNOWN

- Whether Laragon Apache vhost smoke on `iseo-report-hub.test` would differ from built-in server smoke when Apache is stopped (this session used `127.0.0.1:8088`).
- Multi-role HTTP smoke beyond single `admin_owner` fixture user.
