# REPORT — I-SEO REPORT HUB DEMO USER AND SCENARIO SEED IMPLEMENTATION 01

**Date:** 2026-08-21  
**Verdict:** `DEMO USER SCENARIO SEED PASS`  
**Primary commit:** `6102b9216b24ccc8d9f3cc7ee6c55714f099b04e`
**Hash-record commit:** `894fb902be968eb235abdc89d2a6e743df13dd9d`
**Tip HEAD:** `157d576a304ed52d491f876cc65984d194c67ab2`
**Push:** no

---

## 1. Verdict

`DEMO USER SCENARIO SEED PASS`

---

## 2. Execution Verification

| Item | Value |
|------|-------|
| Repo root | `X:\AI MARS` |
| Volume | `AI WS` (`X:`) |
| Branch (main checkout) | `mars/canonical-post-recovery` |
| HEAD before | `1b2f180e21ad4b2f109be6b11e7df92e2550eed0` |
| Clean worktree | `X:\AI MARS STORAGE\git-sync-iseo-report-hub-demo-user-scenario-seed-implementation-01\repo` on branch `iseo-demo-seed-impl-01` |
| Foreign WIP | preserved (unstaged; not staged/committed) |
| i-SEO preflight WIP | clean |
| Runtime | `http://iseo-report-hub.test/` — `/health` 200, `/login` 200 |
| DB | `iseo_report_hub_dev` @ `127.0.0.1:3306` |

---

## 3. Backup

| Field | Value |
|-------|-------|
| Path | `X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-user-scenario-seed-implementation-01\backup\iseo_report_hub_dev-before-demo-proverka-seed-20260821-134512.sql` |
| Size | 86712 bytes |
| SHA256 | `1f8e72e3aea3ef8b5f458add779767d13feb6237a687a999e793488f953fa751` |

---

## 4. Seed Tool

| Field | Value |
|-------|-------|
| Path | `projects/iseo-report-hub/app-source/tools/demo-proverka-seed.php` |
| Runtime sync | `X:\MARS-Localhost\sites\php\projects\iseo-report-hub\tools\demo-proverka-seed.php` |
| Modes | `--status`, `--create`, `--cleanup` |
| Guards | CLI-only; `APP_ENV=local`; DB name/host; local APP_URL; `--confirm-local-demo-seed` for mutations; refuses report 1/5; refuses cleanup if demo export/share/snapshot present |

---

## 5. Demo User

| Field | Value |
|-------|-------|
| Name | `Тест Проверочнов` |
| Email/login | `test@mail.ru` |
| Password (operator-approved demo) | `test` (hash **not** printed) |
| Role | `seo_specialist` |
| Status | active |
| user_id | 3 |

---

## 6. Demo Scenario Created

| Entity | ID / notes |
|--------|------------|
| Client `ПРОВЕРКА.рa` | client_id **2**, slug `proverka-demo`, marker in notes |
| Project | project_id **2** — `SEO-продвижение ПРОВЕРКА.рa` |
| Site | site_id **2** — `https://proverka.example` |
| July period/report | period **5** / monthly **7** — finalized texts+blocks; no publication artifacts |
| August period/report | period **6** / monthly **8** — in_progress through 2026-08-21 |
| Report blocks | 6 + 6 (required section keys) |
| Work entries | 12 July + 10 August |
| Metrics | prose + July `results_summary` / optional `data_json` on results block |

---

## 7. Validation

| Area | Result |
|------|--------|
| PHP syntax | PASS (`php -l` on seed tool) |
| DB checks | PASS — user/role/scenario; r1/r5 unchanged; exports/shares/snapshots unchanged; export 4 unchanged |
| HTTP routes | PASS — health/login/dashboard/periods/July+August detail+preview/work create+edit all 200 |
| Login as test user | PASS |
| Screenshots | PASS — evidence folder (not in git) |

---

## 8. Evidence

`X:\AI MARS STORAGE\incoming\iseo-report-hub\demo-user-scenario-seed-implementation-01\20260821-134512\`

- `demo-proverka-ids.json`
- `DEMO-SEED-SCREENSHOT-INDEX.md`
- `DEMO-SEED-ASSERTIONS.md`
- PNG `01`–`09` (+ `01b_post_login_landing.png`)

---

## 9. Safety

| Item | Changed? |
|------|----------|
| DB | **yes** (expected local seed) |
| Report 1 | **no** |
| Report 5 | **no** |
| Export / share / PDF / snapshot | **no** |
| Production / host upload | **no** |
| Token / hash printed | **no** |

---

## 10. Commit

| Item | Value |
|------|-------|
| Primary | `6102b9216b24ccc8d9f3cc7ee6c55714f099b04e` — `feat(iseo-report-hub): add proverka demo seed tool` |
| Hash-record | `894fb902be968eb235abdc89d2a6e743df13dd9d` — `docs(iseo-report-hub): record proverka demo seed hash` |
| Tip HEAD | `157d576a304ed52d491f876cc65984d194c67ab2` |
| Push | **no** |

---

## 11. SAFE UNKNOWN

- Whether host upload of this demo user is ever desired: operator must decide later; credential `test` must **not** ship to production as-is.
- Whether Browser Fill Pass will further edit August status/texts: deferred to next wave.

---

## 12. Remaining Queue

1. Browser Filled Demo Report Pass 01  
2. Pre-hosting Deployment Readiness Charter 01 (after demo accepted)  
3. Parked: Client Report Export HTML Alignment Implementation 01 (operator confirm only)

---

## 13. Recommended Next Action

`I-SEO Report Hub — Browser Filled Demo Report Pass 01`

---

## 14. Files Changed

- `projects/iseo-report-hub/app-source/tools/demo-proverka-seed.php`
- `projects/iseo-report-hub/product/I-SEO-REPORT-HUB-DEMO-USER-SCENARIO-SEED-IMPLEMENTATION-RESULT-v0.1.md`
- `projects/iseo-report-hub/reports/REPORT-iseo-report-hub-demo-user-scenario-seed-implementation-01.md`
- `projects/iseo-report-hub/OPERATIONAL-INDEX.md`

Runtime sync (not git): `tools/demo-proverka-seed.php` only.

---

## 15. Git Actions

Exact-path commits via clean worktree; cherry-pick onto `mars/canonical-post-recovery`; foreign WIP preserved; **no push**.
