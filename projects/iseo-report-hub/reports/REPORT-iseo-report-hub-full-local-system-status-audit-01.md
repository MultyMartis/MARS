# REPORT — I-SEO REPORT HUB FULL LOCAL SYSTEM STATUS AUDIT 01

**Date:** 2026-08-24  
**Verdict:** `FULL LOCAL SYSTEM STATUS AUDIT ATTENTION`  
**Primary commit:** `ebebf467a06dc450f16c81831b6ca6429b69a9d7`  
**Hash-record commit:** `d0e0075730adb0c266d30810ed5d9e62bb9a71b5`  
**Tip HEAD:** `b97b4cc40e1b40eba860a743584da4a194375350`  
**Push:** no

---

## 1. Verdict

`FULL LOCAL SYSTEM STATUS AUDIT ATTENTION`

Локальный контур (source/runtime/DB/auth/demo) здоров и пригоден для продолжения разработки. ATTENTION: нет `public/.htaccess` в source; независимый host public GET из среды аудита дал 403/404; PDF/export/share parked; config normalization ещё впереди.

---

## 2. Execution Verification

| Item | Value |
|------|--------|
| Repo root | `X:\AI MARS` |
| Volume | `AI WS` (`X:`) |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `9aa018f254c46c696f2c756f20546b4adba1a7ae` |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-report-hub-full-local-system-status-audit-01\repo` on `iseo/full-local-system-status-audit-01` |
| Foreign WIP | preserved (unstaged; not staged/committed) |
| i-SEO preflight WIP | clean |
| Staged before start | empty |
| Runtime | read-only HTTP smoke |
| DB | read-only SQL counts/checks |
| Host | optional public GET only (no login) |
| Mutations | none (no app-source/runtime/DB/host upload) |

---

## 3. Current System Status Summary

После ручной выкладки demo на `https://reports.i-seo.su` и Host DB Guard Fix проект возвращается к локальной разработке. Локально demo `ПРОВЕРКА.рф`, отчёты 7/8, preview и work entries работают. Host по оператору работает после re-upload `DatabaseService.php`; этот аудит host независимо не подтвердил. Следующий фокус: baseline hygiene (`.htaccess`/config) + product polish; PDF/share позже.

---

## 4. Repo / Source Status

- SoT: `projects/iseo-report-hub/app-source`
- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`
- HEAD expected tip before docs: Host DB Guard Fix hash-record
- `public/.htaccess`: **missing** in source and local runtime public
- `tools/`: present; exclude from host
- `DatabaseService` host guard fix: present; source/runtime hash match
- `ConfigService`: `.env.local` only
- Routing via `public/index.php` + `app/routes.php`: stable

---

## 5. Local Runtime Status

| Check | Result |
|-------|--------|
| `/health`, `/login` | 200 |
| `/` anon | 302 → login |
| Auth `test@mail.ru` | OK |
| Periods, monthly 7/8, previews, work-entry create | 200 |
| Work-entry edit `/monthly-report-work-entries/28/edit` | 200 |
| Raw refused/fatal on smoked routes | none |

---

## 6. Local DB Status

Counts: users 3; roles 6; clients/projects/sites 1; periods 2; monthlies 2; blocks 12; work entries 22; snapshots/exports/shares 0; audit_log 68; weekly_checkpoints 0.

Verified: `test@mail.ru` + `seo_specialist`; admin_owner users present; only `ПРОВЕРКА.рф`; monthly 7 finalized / 8 in_progress; `sites.url=https://proverka.example`; no `.рa`; no content app URL `iseo-report-hub.test` (only admin email domain). No password hashes printed.

---

## 7. Host-known Status

**Operator-confirmed:** manual upload; host `.env.local`; host DB name not local; `DatabaseService.php` re-upload unblocked pages; main pages work; old export/share URLs 404 expected; no PDF/share expectation; SEO looked without actionable feedback.

**Not independently verified here:** authenticated host pages; full file set on host; public `/health`/`/login` (audit env saw 404; `/` 403).

---

## 8. Config / Env / DB Connection Status

`.env.local` model; ConfigService keys APP_* + DB_*; host guard fixed; debt → Production Config Normalization 01 (not implemented now).

---

## 9. Deployment Package Status

Readiness ATTENTION still valid: missing source `.htaccess`; `.env.local` required; document root `public`; exclude `tools/`; PHP 8.3; no WP URL replace. Manual process documented; optional later deploy builder.

---

## 10. Product / UX Status

Core internal UX present for demo. Gaps: SEO feedback; Browser Filled Demo Pass; August deltas; real users; onboarding; parked PDF/share empty states.

---

## 11. Export / PDF / Share Status

All zero in DB; parked; `ReportExportService` Windows headless assumptions; recommend Export Share PDF Readiness Charter before enablement.

---

## 12. Key Risks / Technical Debt

Missing `.htaccess`; config normalization; weak demo password; host/source drift possible; PDF hosting risk; foreign monorepo WIP; unpushed history (no push this wave).

---

## 13. Recommended Plan

Phases A–E per [LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1](../product/I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md): baseline hygiene → product polish → real usage → optional PDF → ops.

---

## 14. Recommended Next 3 Prompts

1. Pre-hosting Readiness Fix 01 (`.htaccess` + deploy hygiene)
2. Production Config Normalization 01
3. Browser Filled Demo Report Pass 01

---

## 15. Docs Created

- `product/I-SEO-REPORT-HUB-FULL-LOCAL-SYSTEM-STATUS-v0.1.md`
- `product/I-SEO-REPORT-HUB-LOCAL-ROADMAP-AFTER-HOST-DEMO-v0.1.md`
- `reports/REPORT-iseo-report-hub-full-local-system-status-audit-01.md`
- `OPERATIONAL-INDEX.md` updated

---

## 16. Evidence

`X:\AI MARS STORAGE\incoming\iseo-report-hub\full-local-system-status-audit-01\20260824-124948\`  
(`runtime-smoke.txt`, `db-status.json`, `route-status.json`, `source-status.txt`, leftovers/schema helpers) — **not committed**; no secrets.

---

## 17. Safety

| Item | Value |
|------|--------|
| DB changed | no |
| runtime changed | no |
| app-source changed | no |
| host upload | no |
| secrets printed | no |

---

## 18. Commit

- primary: `ebebf467a06dc450f16c81831b6ca6429b69a9d7`
- hash-record: `d0e0075730adb0c266d30810ed5d9e62bb9a71b5`
- tip HEAD: `b97b4cc40e1b40eba860a743584da4a194375350`
- push: no

---

## 19. SAFE UNKNOWN

- Exact host filesystem tree / whether rewrite `.htaccess` exists on host
- Whether host has only `DatabaseService.php` delta vs full local source
- Why audit-environment public GET to host returned 403/404 (WAF/IP/docroot/other)
- SEO team future feedback content
- Whether PDF will be required for MVP

---

## 20. Files Changed

Exact docs paths only (see §15). No app-source / runtime / evidence.

---

## 21. Git Actions

Clean worktree commit of exact docs; cherry-pick onto `mars/canonical-post-recovery` if needed; no push; foreign WIP untouched.
