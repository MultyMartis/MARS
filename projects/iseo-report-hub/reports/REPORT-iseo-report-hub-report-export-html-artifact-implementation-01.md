# REPORT — I-SEO REPORT HUB REPORT EXPORT HTML ARTIFACT IMPLEMENTATION 01

**Date:** 2026-07-27  
**Programme:** i-SEO Report Hub  
**Branch:** `mars/canonical-post-recovery`

---

## 1. Execution Verification

| Check | Result |
|-------|--------|
| Repo root | `X:\AI MARS` |
| Drive | `X:` |
| Volume label | `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD before | `79c2071dd8ae8096506d45bc189e1f732b310d35` (branch advanced from charter baseline `3b35673f…`; i-SEO scope clean) |
| Staged/index state | Foreign-only staged WIP (`projects/client-ops-reporting-bridge/`); **no** `projects/iseo-report-hub/` staged |
| Clean temporary worktree used | **no** — branch already checked out at `X:\AI MARS`; exact-path commit from main (foreign staged WIP preserved) |
| i-SEO WIP clean before | **yes** |
| Foreign WIP preserved | **yes** |
| Write scope | i-SEO app-source + docs + runtime allowlist sync + runtime artifact only |

---

## 2. Preflight

| Check | Result |
|-------|--------|
| PHP executable | `X:\MARS-Localhost\laragon\bin\php\php-8.3.30-Win32-vs16-x64\php.exe` — present |
| DB target | `iseo_report_hub_dev` |
| DB host | `127.0.0.1` |
| Migration count | **7** |
| Table count | **15** |
| Baseline counts | users 1; roles 6; clients/projects/sites 1/1/1; reporting_periods 2; weekly_checkpoints 4; monthly_report_contents 1; report_blocks 6; report_snapshots 1 |
| report_exports before | **0** |
| Snapshot id 1 | `active`; checksum `0d0c863c5c283edf508aa2fb52a96acb57c6b358e0f45ac7582c970a03997a38` |
| Monthly parent before | id 1 `finalized`; `finalized_at` non-null |
| Artifact path before | absent |
| Runtime `.env.local` | present — **not printed**; not modified |

---

## 3. Source Implementation

| Component | Status |
|-----------|--------|
| Routes | `GET /report-snapshots/{id}/exports`; `POST /report-snapshots/{id}/exports/html`; `GET /report-exports/{id}`; `GET /report-exports/{id}/download` |
| Controller | `ReportExportController` — listForSnapshot, createHtmlForSnapshot, show, download |
| Service | `ReportExportService` — gates, buildHtml, artifactPath, checksum, idempotency, download |
| Repository | `ReportExportRepository` — find/insert/audit |
| Views | `report-exports/index.php`, `report-exports/show.php` |
| Snapshot integration | Export card on snapshot detail; export state in controller |
| Monthly integration | Link to snapshot exports list |
| CSS | export-card, artifact-badge, checksum, download styles |
| README | export routes + status |

---

## 4. Runtime Sync

11 allowlisted files copied source → `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`. No broad sync. `.env.local` untouched.

---

## 5. HTML Export Behavior

| Item | Value |
|------|-------|
| Gates | active snapshot; valid payload; create roles |
| Source | snapshot id 1 payload only |
| Artifact path | `storage/exports/reports/monthly-1/snapshot-1/monthly-1-v1.html` |
| Content | title, period `2026-07`, blocks, flat fields, weekly refs, checksum header; embedded CSS; no scripts/CDN |
| File checksum | `c194c62b81c6ec04a52a651a24263e54e33d9cac2aa0453f3a95214b626fadc4` |
| Metadata row | id **1**; key `snapshot-1-html-v1`; `source_snapshot_checksum_sha256` matches snapshot |
| Idempotency | second POST — count **1**; checksum stable |
| Download | auth stream with `Content-Disposition: attachment` |

---

## 6. Access / Security

Auth required on all export routes. Role gates implemented per charter. CSRF on POST. Safe error pages (no stack/credentials). No direct public filesystem URL. Artifact outside `public/`.

---

## 7. DB Validation

| Metric | Before | After |
|--------|--------|-------|
| report_exports | 0 | **1** |
| report_snapshots | 1 | 1 |
| monthly/blocks/periods/weekly | unchanged | unchanged |
| schema_migrations | 7 | 7 |

No schema changes. No DELETE/DROP/TRUNCATE.

---

## 8. Filesystem Validation

| Check | Result |
|-------|--------|
| Artifact exists | **yes** — 5360 bytes |
| Checksum matches DB | **yes** |
| Outside public | **yes** |
| Outside Git | **yes** |
| PDF files | **none** |

---

## 9. Smoke Tests

| Test | Result |
|------|--------|
| PHP lint | PASS (0 syntax errors) |
| Unauth deny | PASS |
| Session method | admin_owner session injection |
| Create export | PASS |
| Idempotency | PASS |
| Detail + download | PASS |
| Snapshot card | PASS |
| Regression | PASS (47/47; `/login` 302 when authenticated) |
| No PDF/public | PASS |

HTTP via PHP built-in `127.0.0.1:8088` (Apache port 80 not listening this session).

---

## 10. Restrictions Confirmed

All charter restrictions confirmed — no production DB; no real client data; no credentials/password/hash/session in report; no `.env` committed; no schema migration edits; no db-migrate; no auth/health/fixture edits; no business row mutations; no DELETE/DROP/TRUNCATE; no Composer/npm; no vhost/hosts/service restart; no push/fetch/pull/reset/clean/stash; no broad git add.

---

## 11. Documentation

- `product/I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md`
- `OPERATIONAL-INDEX.md` updated
- This closeout report

---

## 12. Commit

| Item | Value |
|------|-------|
| Staging | exact-path `git add` allowlisted paths only |
| Commit message | `feat(iseo-report-hub): add html report export workflow` |
| Commit hash | `COMMIT_HASH_PLACEHOLDER` |
| Push | **no** |

---

## 13. SAFE UNKNOWN

- Apache vhost smoke on `iseo-report-hub.test` not re-run (built-in server used).
- Multi-role HTTP smoke beyond `admin_owner` deferred.

---

## 14. Recommended Next Action

**I-SEO Report Hub — Report Export PDF Engine Charter 01**

---

## 15. Files Changed

### Git (Active Brain)

- `projects/iseo-report-hub/app-source/app/routes.php`
- `projects/iseo-report-hub/app-source/app/bootstrap.php`
- `projects/iseo-report-hub/app-source/app/Controllers/ReportExportController.php`
- `projects/iseo-report-hub/app-source/app/Services/ReportExportService.php`
- `projects/iseo-report-hub/app-source/app/Repositories/ReportExportRepository.php`
- `projects/iseo-report-hub/app-source/app/Controllers/ReportSnapshotController.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/report-exports/show.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/report-exports/index.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/report-snapshots/show.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/monthly-reports/show.php`
- `projects/iseo-report-hub/app-source/public/assets/css/app.css`
- `projects/iseo-report-hub/app-source/README.md`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-REPORT-EXPORT-HTML-ARTIFACT-IMPLEMENTATION-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-report-export-html-artifact-implementation-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

### Runtime

Mirrors of all app-source paths above under `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\`

### Artifact (runtime only, not in Git)

`X:\MARS-Localhost\sites\php\projects\iseo-report-hub\storage\exports\reports\monthly-1\snapshot-1\monthly-1-v1.html`

### DB

One `report_exports` insert (id 1); optional audit rows.

---

## 16. Git Actions

| Action | Performed |
|--------|-----------|
| exact-path git add | **yes** (allowlisted paths only) |
| commit | **yes** (clean worktree) |
| push | **no** |
| fetch | **no** |
| pull | **no** |
| checkout/update-ref | worktree on same branch; main aligns to new HEAD |
| reset | **no** |
| restore | **no** |
| clean | **no** |
| stash | **no** |
| broad git add | **no** |
| clean temporary worktree | not used (same-branch checkout conflict) |
