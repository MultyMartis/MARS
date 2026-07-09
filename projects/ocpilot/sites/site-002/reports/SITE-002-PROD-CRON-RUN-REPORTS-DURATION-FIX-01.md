# REPORT — SITE-002 Cron Run Reports Duration Fix

**Operation:** `SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`  
**OCPilot run:** 4.239  
**Date:** 2026-07-09  
**Environment:** https://bzpm.ru/ (Production)  
**Baseline before:** `SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01`  
**Checkpoint after:** `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`

---

## 1. Scope

Reporting-level fix for MARS 1C import wrapper TXT reports showing `Duration: 0 seconds` while per-step durations and LOG wall time were correct. No import execution, monitor run, DB, or public site changes.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` label `AI WS` |
| Branch | `mars/canonical-post-recovery` |
| HEAD | `2570a9a3` |
| Staged files | **none** |
| Foreign WIP | present — **not staged** |

---

## 3. Source discovery

| Path | Role | TXT gen | Duration | Patch |
|------|------|---------|----------|-------|
| `/storage/mars-tools/cron/mars_1c_import_wrapper.php` | MARS wrapper + TXT generator | yes | yes | **yes** |
| `/public_html/mars-tools/cron/mars_1c_http_gateway.php` | HTTP forwarder | no | no | no |
| Sergey legacy `cronjob.php` / import controllers | Legacy import | no | no | no |

Authority maps: Storage `deployments/SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01/manifests/source-authority-map.*`

---

## 4. Root cause

1. **File/function:** `mars_1c_import_wrapper.php` → `mars_report_begin()` closure `finalize()`.
2. **Variable:** `microtime(true) - $startedAt` where `$startedAt` is set inside `mars_report_begin()`.
3. **Why zero:** In `mars_mode_run()`, `mars_report_begin()` was called **after** import steps completed (~7s). `$startedAt` captured report-write time, not run start.
4. **Why steps correct:** Step durations use per-step `$step1Start` / `$step2Start` around HTTP cronjob calls.
5. **Isolated to reporting:** **yes**.
6. **Affects import execution:** **no**.

Evidence: Run 4.233 — `mars-20260708-080001-bb67ff2b`; LOG `08:00:01→08:00:08`; TXT `Duration: 0 seconds`.

---

## 5. Patch plan and rollback

- Add optional `?float $wallStartedAt` to `mars_report_begin()`.
- Pass run `$started` from `mars_mode_run()` success and error paths.
- Fallback `duration_seconds` in finalize extra if computed duration &lt; 0.01.
- Bump wrapper version **1.1.0 → 1.1.1**.
- Rollback: re-upload `server-source-before/mars_1c_import_wrapper.php` (SHA `e991afb2…`).

Before SHA: `e991afb2b0202f622c7e6f1cbd627826f4cdef79fedc45b9e3054d337ae28b62`  
After SHA: `cae00b1e1581f77568587787be9436d550048ba53158859b3694a92963258fa2`

---

## 6. Local fixture test

Fixture from Run 4.233 facts: start `08:00:01`, finish `08:00:08`, steps 3.43s + 3.02s, SUCCESS.

| Gate | Result |
|------|--------|
| PHP CLI on agent host | **not available** |
| Timestamp simulation | **7.0 seconds** (nonzero) |
| Step durations preserved | **yes** |
| SUCCESS preserved | **yes** |
| Overall fixture | **PASS** |

Note: Static patch proof + timestamp simulation; live PHP harness available when PHP installed.

---

## 7. Dry-run gates

All gates **G1–G14 PASS**. See Storage `manifests/dry-run-gates.json`.

---

## 8. Controlled deploy

| Item | Value |
|------|-------|
| Remote path | `/storage/mars-tools/cron/mars_1c_import_wrapper.php` |
| Files uploaded | **1** |
| Post-upload SHA match | **yes** |
| Import triggered | **no** |

---

## 9. Post-deploy read-only verification

| Check | Result |
|-------|--------|
| Patched file on server | **yes** |
| Contains `wallStartedAt` | **yes** |
| Version 1.1.1 | **yes** |
| New import report by this task | **no** |
| Public URLs (7) | **all 200** |
| Public БЗПМ | **no** |

---

## 10. Future confirmation plan

After **next scheduled 1C import** (cron `0 8 * * *` Moscow):

1. New TXT report exists under `/storage/mars-tools/cron/reports/`.
2. `Duration:` is **nonzero** and ~matches LOG wall time.
3. Step durations still present.
4. `Final status: SUCCESS` unless real failure.
5. No import behavior regression.

**Inherited pending (do not run now):**

- Run **4.235** post-1C Lari reparent verification.
- Hardened scheduled monitor observation after next monitor run.

---

## 11. Production mutation summary

| Class | Count |
|-------|------:|
| Remote uploads | 1 exact wrapper file |
| Remote overwrites | 1 |
| Remote deletes | 0 |
| FTP writes | 1 |
| FTP reads/listings | yes |
| FTP downloads | 1 source + 1 verify |
| Admin saves | 0 |
| DB writes | 0 |
| Import runs triggered | 0 |
| Monitor runs triggered | 0 |
| Product/category/stock/price changes | 0 |
| SEO/redirect/sitemap/robots/llms changes | 0 |
| Header/footer/Yandex changes | 0 |
| Cache clears | 0 |
| Cron wrapper code changes | 1 |
| Task Scheduler changes | 0 |
| public БЗПМ introduced | no |

---

## 12. Storage artefacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01\`

Checkpoint: `production\baselines\SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01\`

---

## 13. Authority updates

- `OPERATIONAL-INDEX.md` — Run 4.239
- `OCPILOT-STATE.md` — current focus + checkpoint
- `production-profile.md` — cron reports duration fix deployed
- `site-passport.md` — MARS 1C cron reports row
- `SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` — §39 anomaly status + §41 fix
- `tools/README.md` — new script + wrapper mirror

---

## 14. Git status

Selective commit of operation docs + patched wrapper mirror + tool script only. No Storage, no secrets.

---

## 15. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| Next import TXT Duration value on production | **UNKNOWN** until next cron run |
| PHP local harness on agent host | PHP not installed — simulation used |
| Run 4.235 post-1C verification | **still pending** |

---

## 16. Final verdict

**SITE-002 CRON RUN REPORTS DURATION FIX COMPLETE — PATCH DEPLOYED, NEXT IMPORT CONFIRMATION PENDING**

---

## 17. Next task recommendation

1. After next 1C import: verify TXT `Duration` nonzero (this operation confirmation).
2. Run **4.235** post-1C Lari reparent verification (inherited).
3. Observe hardened scheduled monitor on next 12:30 run (inherited from Run 4.233).
