# REPORT — I-SEO REPORT HUB PRE-HOSTING READINESS FIX 01

**Date:** 2026-08-24  
**Verdict:** `PREHOSTING READINESS FIX PASS`  
**Primary commit:** `fd9855ce726ad7e06ddc0ccadbdb404b4a10715d`  
**Hash-record commit:** `804d2377e36f3d5acf73a475511d848b44de9c32`  
**Push:** no

---

## 1. Verdict

`PREHOSTING READINESS FIX PASS`

Canonical source и local runtime теперь содержат одинаковый безопасный Apache front-controller file. Local routes и DB baseline после sync сохранились.

---

## 2. Execution Verification

- Repo root: `X:\AI MARS`
- Volume: `AI WS` (`X:`)
- Canonical branch: `mars/canonical-post-recovery`
- HEAD before: `7110b663b40d5f0fb81c10f5bf2dd287357f33f6`
- Clean worktree: `X:\AI MARS STORAGE\git-sync-iseo-report-hub-prehosting-readiness-fix-01\repo`, branch `iseo/prehosting-readiness-fix-01`
- Foreign WIP: present outside i-SEO scope, preserved and not staged
- i-SEO scope before start: clean
- Staged index before start: empty
- Runtime: available; Apache GET smoke passed
- DB: local `iseo_report_hub_dev`, read-only baseline verification

---

## 3. Fix Implemented

- Added source `projects/iseo-report-hub/app-source/public/.htaccess`.
- Synced only `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public\.htaccess`.
- Content sets `DirectoryIndex index.php`, disables directory listing, and rewrites only non-file/non-directory requests to `index.php`.
- No project-root `/public` redirect, local path, secret, domain rule or host-specific hack was added.

---

## 4. Validation

- SHA-256 source/runtime: `90f735bade70b91c1f1090ea6b27d255d198ae6fdbf6f3f2bc88a5f7aad8fcb9` — match.
- `/health`: 200.
- `/login`: 200.
- `/` anonymous: 302; authenticated: 200.
- Authenticated `/reporting-periods`: 200.
- Authenticated monthly 7 and 8 detail + preview: 200.
- Authenticated `/monthly-reports/8/work-entries/create`: 200.
- DB counts before/after identical.
- Snapshots / exports / shares remain `0 / 0 / 0`; PDF/export/share flow was not invoked.

---

## 5. Host Operator Note

If host document root points to application `public`, upload exactly:

- from `projects/iseo-report-hub/app-source/public/.htaccess`;
- to host application `public/.htaccess`, physically `<document-root>/.htaccess`.

If `public_html` remains document root while the application is nested below it, this file is not a full substitute for a project-root redirect. Recommended structure remains document root = application `public`.

Host `.env.local` remains required and must stay host-specific. Use PHP 8.3, keep `APP_DEBUG=false`, exclude `tools/`, and do not perform WordPress-like DB URL replacement. No PDF/share expectation is introduced.

---

## 6. Docs Created

- `product/I-SEO-REPORT-HUB-PREHOSTING-READINESS-FIX-RESULT-v0.1.md`
- `reports/REPORT-iseo-report-hub-prehosting-readiness-fix-01.md`
- `OPERATIONAL-INDEX.md` updated

---

## 7. Evidence

Uncommitted, secret-free:

`X:\AI MARS STORAGE\incoming\iseo-report-hub\prehosting-readiness-fix-01\20260824-140349\`

- `runtime-smoke.txt`
- `htaccess-hashes.txt`

---

## 8. Safety

- DB changed: no.
- Runtime changed: yes — only `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public\.htaccess`.
- App-source changed: yes — only `projects/iseo-report-hub/app-source/public/.htaccess`.
- Host upload: no.
- Secrets printed: no.

---

## 9. Commit

- Primary: `fd9855ce726ad7e06ddc0ccadbdb404b4a10715d`
- Hash-record: `804d2377e36f3d5acf73a475511d848b44de9c32`
- Tip HEAD: this canonical hash-mapping report commit (exact value in Git log/final operator report)
- Push: no

---

## 10. SAFE UNKNOWN

- Exact current host filesystem layout and whether subdomain document root already points directly to application `public`.
- Whether host Apache permits `Options -Indexes` through `AllowOverride`; if it rejects the directive, remove only that line through a canonical source follow-up, not a permanent host-only edit.
- Exact host/source drift beyond the operator-confirmed `DatabaseService.php` re-upload.

---

## 11. Recommended Next Action

`I-SEO Report Hub — Production Config Normalization 01`

---

## 12. Files Changed

- `projects/iseo-report-hub/app-source/public/.htaccess`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-PREHOSTING-READINESS-FIX-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-prehosting-readiness-fix-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`
- Local runtime exact sync: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\public\.htaccess`

---

## 13. Git Actions

Exact-path staging and commit only; no broad add, no foreign WIP changes, no push.

---

## Execution safety

- cwd: clean worktree under `X:\AI MARS STORAGE`
- scope lock honored: yes
- destructive ops: none
- protected zone touch: none
