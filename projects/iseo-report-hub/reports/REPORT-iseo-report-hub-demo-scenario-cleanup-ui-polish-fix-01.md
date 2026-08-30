# REPORT — I-SEO REPORT HUB DEMO SCENARIO CLEANUP AND UI POLISH FIX 01

**Date:** 2026-08-21  
**Verdict:** `DEMO SCENARIO CLEANUP UI POLISH PASS`  
**Primary commit:** `dc90c35cda49e00b30dd1a5e15408616a8d62ad0`  
**Hash-record commit:** `0682dda67c59394aab9f4e123a7e8d24fd18e3b4`  
**Tip HEAD:** `bd5cd1c8e34d1a2ef45f3ec43e2d83a2d84a88c2`  
**Push:** no

---

## 1. Verdict

`DEMO SCENARIO CLEANUP UI POLISH PASS`

---

## 2. Execution Verification

| Item | Value |
|------|-------|
| Repo root | `X:\AI MARS` |
| Volume | `AI WS` (`X:`) |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `774bc773ea8f341bea5751723c41fd3c5bfa7bd0` |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-report-hub-demo-scenario-cleanup-ui-polish-fix-01\repo` on branch `iseo-demo-cleanup-polish-fix-01` |
| Foreign WIP | preserved (unstaged; not staged/committed) |
| i-SEO preflight WIP | clean |
| Runtime | `http://iseo-report-hub.test/` — `/health` 200, `/login` 200 |
| DB | `iseo_report_hub_dev` @ local loopback |

---

## 3. Backup

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-scenario-cleanup-ui-polish-fix-01\backup\iseo_report_hub_dev-before-demo-cleanup-polish-20260821-141053.sql` |
| Size | 113003 bytes |
| SHA256 | `b1d484fe278947c65268ccee4b32c6423d8d62394684d297e0dba7b33db99a89` |

---

## 4. Old Demo Cleanup

**Deleted (proven Demo Client path):** client 1, project 1, site 1, periods 1+3, monthlies 1+5, 4 weekly checkpoints, 6 blocks, 7 work entries, 1 snapshot, 4 exports, 7 shares; 4 storage export files under runtime `storage/exports/` mapped from deleted export rows.

**Not deleted:** user `test@mail.ru`; ПРОВЕРКА scenario (client/project/site 2; periods 5–6; monthlies 7–8; 12 blocks; 22 work entries); seed tool; backups/evidence.

**Counts after:** users 3; clients/projects/sites 1; periods 2; monthlies 2; blocks 12; work entries 22; snapshots/exports/shares 0.

---

## 5. Rename to ПРОВЕРКА.рф

Affected IDs: client 2, project 2, site 2, periods 5–6, monthlies 7–8 (+ block bodies / period summary follow-up). Marker/slug/URL unchanged. Remaining `.рa` in demo path: **no**. Demo Client string scrubbed from July `internal_notes`.

---

## 6. UI Polish

| Area | Fix |
|------|-----|
| Username `\uXXXX` | `UiLabels::decodeLiteralUnicodeEscapes` + AuthService session write; DB name already UTF-8 |
| Dashboard | Dynamic scenario from DB; honest PDF/share; no Demo Client hardcode |
| Periods table | nowrap; Russian status; monthly status badges |
| Status/role labels | `ui_status_label` / `ui_role_label` |
| Report detail/preview | titles/body `.рф`; PDF «еще не создан» when absent |

---

## 7. Validation

| Area | Result |
|------|--------|
| PHP syntax | PASS |
| DB checks | PASS |
| HTTP routes (test user) | PASS — all required 200 |
| Assertions | PASS — no `\u`, no `.рa`, has `.рф`, no Demo Client, no raw EN status badges |
| Screenshots | PASS — evidence folder |

---

## 8. Evidence

`X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-scenario-cleanup-ui-polish-fix-01\20260821-140904\`

---

## 9. Safety

| Item | Changed? |
|------|----------|
| DB | **yes** (expected local cleanup + rename) |
| New demo | **yes** (rename/scrub only) |
| Old demo deleted | **yes** |
| Export/share/PDF generated | **no** (old rows/files removed only) |
| Production / host upload | **no** |
| Token / hash printed | **no** |

---

## 10. Commit

| Item | Value |
|------|-------|
| Primary | `dc90c35cda49e00b30dd1a5e15408616a8d62ad0` — `fix(iseo-report-hub): clean demo scenario and polish UI` |
| Hash-record | `0682dda67c59394aab9f4e123a7e8d24fd18e3b4` — `docs(iseo-report-hub): record demo cleanup polish hash` |
| Tip HEAD | `bd5cd1c8e34d1a2ef45f3ec43e2d83a2d84a88c2` |
| Push | **no** |

---

## 11. SAFE UNKNOWN

- Whether operator wants PDF/share for ПРОВЕРКА.рф before hosting: deferred to later waves.
- Whether Browser Fill Pass will further edit August content: deferred.

---

## 12. Remaining Queue

1. Browser Filled Demo Report Pass 01  
2. Pre-hosting Deployment Readiness Charter 01 (after demo accepted)  
3. Parked: Client Report Export HTML Alignment Implementation 01

---

## 13. Recommended Next Action

`I-SEO Report Hub — Browser Filled Demo Report Pass 01`

---

## 14. Files Changed

- `projects/iseo-report-hub/app-source/app/Support/UiLabels.php`
- `projects/iseo-report-hub/app-source/app/Support/helpers.php`
- `projects/iseo-report-hub/app-source/app/Controllers/DashboardController.php`
- `projects/iseo-report-hub/app-source/app/Controllers/ReportingPeriodController.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/dashboard.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/reporting-periods/index.php`
- `projects/iseo-report-hub/app-source/app/Views/pages/monthly-reports/show.php`
- `projects/iseo-report-hub/app-source/app/Services/AuthService.php`
- `projects/iseo-report-hub/app-source/public/assets/css/app.css`
- `projects/iseo-report-hub/app-source/tools/demo-proverka-seed.php`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEMO-SCENARIO-CLEANUP-UI-POLISH-FIX-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-demo-scenario-cleanup-ui-polish-fix-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

Runtime sync (not git): exact allowlisted app-source files listed above.

---

## 15. Git Actions

Exact-path commits via clean worktree; cherry-pick onto `mars/canonical-post-recovery`; foreign WIP preserved; **no push**.
