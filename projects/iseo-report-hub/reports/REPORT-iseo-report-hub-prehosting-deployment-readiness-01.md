# REPORT — I-SEO REPORT HUB PRE-HOSTING DEPLOYMENT READINESS 01

**Date:** 2026-08-21  
**Verdict:** `PREHOSTING DEPLOYMENT READINESS ATTENTION`  
**Primary commit:** `ae90682c9703cd47d22a591374ae73f43ed34e5a`
**Hash-record commit:** `0895ecc7c632a4e26153b4ee6e3078099ba109b0`
**Tip HEAD:** `8e3b2bc9577ce1e96ebc42f2c49566fb66d69920`
**Push:** no

---

## 1. Verdict

`PREHOSTING DEPLOYMENT READINESS ATTENTION`

Pack готов для ручной выкладки. ATTENTION: в source нет `public/.htaccess`; env-файл на хосте должен называться **`.env.local`** (не `.env`); PDF на shared hosting отложен.

---

## 2. Execution Verification

| Item | Value |
|------|-------|
| Repo root | `X:\AI MARS` |
| Volume | `AI WS` (`X:`) |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `d7fb84344d0c776c00ba21ff4430efbd8c834af9` |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-report-hub-prehosting-deployment-readiness-01\repo` on `iseo/prehosting-deployment-readiness-01` |
| Foreign WIP | preserved (unstaged; not staged/committed) |
| i-SEO preflight WIP | clean |
| Staged before start | empty |
| Runtime | read-only smoke: `/health` 200, `/login` 200, `/` 302 |
| DB | read-only scan `iseo_report_hub_dev` |

---

## 3. Operator Answers

| Вопрос | Ответ |
|--------|--------|
| Можно ли выкладывать? | **Да**, вручную по readiness pack; учесть ATTENTION (rewrite + `.env.local`) |
| Что копировать? | Содержимое `app-source` (app/public/config/storage skeleton); не runtime целиком; не tools/ |
| Document root | **`public`** |
| PHP | **8.3** + pdo_mysql, mbstring, json, openssl, fileinfo, session |
| `.env` | Создать **`.env.local`** на хосте: `APP_URL=https://reports.i-seo.su`, production DB_*, `APP_DEBUG=false` |
| URL replace как WP? | **Нет** |
| Demo DB values | `sites.url=https://proverka.example`; имена `ПРОВЕРКА.рф`; user `test@mail.ru` |

---

## 4. File Package Map

См. `product/I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md`

- Source: `X:\AI MARS\projects\iseo-report-hub\app-source`
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`
- Include: `app/`, `public/`, `config/`, `storage/` skeleton, `.env.example`
- Exclude: `.env.local`, `tools/`, logs/cache contents, exports leftovers, evidence, MARS docs
- No Composer/vendor

---

## 5. PHP / Extensions

Required: PHP **8.3**; `pdo`, `pdo_mysql`, `mbstring`, `json`, `openssl`, `fileinfo`, `session`.  
Optional: `curl`, `intl`, `gd`, `dom`/`xml`.  
Deferred risk: Edge/Chrome headless PDF (Windows paths in `ReportExportService`) — not for shared hosting MVP.

---

## 6. ENV Template

Placeholders only (host `.env.local`):

```
APP_NAME="i-SEO Report Hub"
APP_ENV=production
APP_DEBUG=false
APP_URL=https://reports.i-seo.su
DB_HOST=CHANGE_ME_HOST
DB_PORT=3306
DB_DATABASE=CHANGE_ME_DB
DB_USERNAME=CHANGE_ME_USER
DB_PASSWORD=CHANGE_ME_PASSWORD
```

ConfigService loads **`.env.local` only**. Keys actually read: `APP_NAME`, `APP_ENV`, `APP_DEBUG`, `APP_URL`, `DB_*`.  
`UPLOAD_PATH`/`LOG_PATH` in `.env.example` are not consumed by ConfigService.

---

## 7. DB URL / Path Audit

См. `product/I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md`

- No WP-like system URL
- 0 hits for literal `http(s)://iseo-report-hub.test` in text columns
- `sites.url` = demo `https://proverka.example`
- `audit_log` has relative `storage/` and `127.0.0.1` — no action
- No `X:\` / `MARS-Localhost` absolute paths
- Optional leftover: `clients.notes` mentions `Demo Client`

---

## 8. DB Export / Import Notes

Export `iseo_report_hub_dev` (utf8mb4, structure+data). Import into host DB. Point `.env.local` to host credentials. Do not run local-only migrate/seed tools on host. Demo login `test@mail.ru` / `test` — change or restrict if public.

---

## 9. Storage / Permissions

Writable: `storage/`, `storage/exports/` (create empty), `logs/`, `cache/`, `uploads/`. Avoid 777 if possible.

---

## 10. Security Notes

Document root must be `public`. Exclude `tools/`. No dump/env in public. `APP_DEBUG=false`. Weak demo password. Add Apache/Nginx rewrite manually.

---

## 11. Host Smoke Checklist

`/health`, `/login`, dashboard `ПРОВЕРКА.рф`, `/reporting-periods`, monthly 7/8 + previews, work-entry create on 8. No PDF/share expectation.

---

## 12. Docs Created

- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-PREHOSTING-DEPLOYMENT-READINESS-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-PREHOSTING-DB-URL-PATH-AUDIT-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\product\I-SEO-REPORT-HUB-PREHOSTING-FILE-PACKAGE-MAP-v0.1.md`
- `X:\AI MARS\projects\iseo-report-hub\reports\REPORT-iseo-report-hub-prehosting-deployment-readiness-01.md`
- `X:\AI MARS\projects\iseo-report-hub\OPERATIONAL-INDEX.md` (updated)

---

## 13. Evidence

`X:\AI MARS STORAGE\incoming\iseo-report-hub\prehosting-deployment-readiness-01\20260821-143230\`  
(runtime-smoke.txt, db-url-path-scan.json, env-vars-found.json, file-tree-summary.txt, audit-storage-meta.json) — **not committed**

---

## 14. Safety

| Item | Status |
|------|--------|
| DB changed | no |
| Runtime changed | no |
| App-source changed | no |
| Host upload | no |
| Secrets printed | no |

---

## 15. Commit

- primary: `ae90682c9703cd47d22a591374ae73f43ed34e5a`
- hash-record: `0895ecc7c632a4e26153b4ee6e3078099ba109b0`
- tip HEAD: `8e3b2bc9577ce1e96ebc42f2c49566fb66d69920`
- push: no

---

## 16. SAFE UNKNOWN

- Exact Beget/panel PHP selector labels and Nginx vs Apache on host — operator confirms in panel
- Whether host allows custom `public` as document root — assumed yes (SSL subdomain already prepared)
- Whether leftover empty `storage/exports/reports/monthly-1` on runtime still has any hidden files — only empty dirs observed

---

## 17. Recommended Next Action

`Operator Manual Hosting Upload`

Optional follow-up charter: add `public/.htaccess` to `app-source` + HTTPS `cookie_secure` (`Pre-hosting Readiness Fix 01`).

---

## 18. Files Changed

Docs/index only (paths in §12). No app-source / runtime / DB.

---

## 19. Git Actions

Exact-path docs commit(s) via clean worktree; no push; foreign WIP preserved.
