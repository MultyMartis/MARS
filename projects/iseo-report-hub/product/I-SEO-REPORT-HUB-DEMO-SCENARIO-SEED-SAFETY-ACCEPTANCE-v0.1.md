# I-SEO Report Hub — Demo Scenario Seed Safety / Acceptance v0.1

**Status:** safety + acceptance gate for seed design and next implementation  
**Date:** 2026-08-21  
**Wave:** Demo User and Scenario Seed Charter 01

---

## 1. Safety requirements (mandatory)

| Rule | Requirement |
|------|-------------|
| Backup | mysqldump (or approved equivalent) **before** any DB mutation |
| Local-only | DB `iseo_report_hub_dev` @ `127.0.0.1`; `APP_ENV=local`; flag `--confirm-local-demo-seed` |
| No production | No writes to host DB; no deploy |
| No host upload | No FTP/SFTP/panel upload to `reports.i-seo.su` from Cursor/MARS |
| No PDF/export/share | No create/regenerate/revoke for demo or Demo Client in seed/fill unless later charter |
| No report 1/5 mutation | Preserve show-ready + empty draft baselines |
| No secrets in docs | No password hashes, share tokens, session cookies, `.env` values |
| Password `test` | Local/demo only — rotate/disable before production |
| Foreign WIP | Preserve; exact-path commits only |
| Marker cleanup | Exact IDs + `MARS_DEMO_PROVERKA_20260821` only |

Operator will manually take site files and DB from Laragon when ready — MARS documents paths only:

- Runtime: `X:\MARS-Localhost\sites\php\projects\iseo-report-hub`
- Source: `X:\AI MARS\projects\iseo-report-hub\app-source`
- DB: `iseo_report_hub_dev`
- PHP: **8.3**

---

## 2. Rollback requirements

1. Keep pre-seed backup until operator accepts demo.  
2. On failure: restore backup; do not improvise partial deletes.  
3. Optional `--cleanup` only after status shows marker IDs and only those IDs.  
4. After cleanup, confirm Demo Client counts restored/unchanged.

---

## 3. Acceptance criteria

### 3.1 After Seed Implementation 01

| # | Criterion |
|---|-----------|
| A1 | User `Тест Проверочнов` / `test@reports.i-seo.local` / role `seo_specialist` / active |
| A2 | Login works locally with password `test` |
| A3 | Client/project/site `ПРОВЕРКА.рa` visible (display literal preserved) |
| A4 | Two periods: July finalized (or agreed closed status), August active |
| A5 | Two monthlies: July full + closed status; August in progress |
| A6 | Realistic work entries (≥10 July, ≥8 August baseline) |
| A7 | Report blocks present for both months |
| A8 | Evidence `demo-proverka-ids.json` written |
| A9 | Report 1/5 unchanged; exports/shares/PDF baseline preserved |
| A10 | Zero export/share/PDF rows for new demo monthlies |

### 3.2 After Browser Fill Pass 01

| # | Criterion |
|---|-----------|
| B1 | Content enriched via UI where possible |
| B2 | Field help `?` visible on key forms |
| B3 | July client preview credible for training |
| B4 | August preview honest in-progress |
| B5 | UI issues logged or none |
| B6 | Still no PDF/export/share mutation |

### 3.3 Pre-hosting (later)

| # | Criterion |
|---|-----------|
| C1 | Demo useful for SEO team training |
| C2 | Weak demo password not shipped live |
| C3 | Upload only after explicit operator command |

---

## 4. Charter wave acceptance (this docs wave)

| # | Criterion | Status |
|---|-----------|--------|
| D1 | Current state audit written | Required |
| D2 | User seed spec written | Required |
| D3 | Scenario data spec written | Required |
| D4 | Content pack written | Required |
| D5 | Seed implementation plan written | Required |
| D6 | Browser fill follow-up written | Required |
| D7 | Safety/acceptance written | This doc |
| D8 | Closeout report + OPERATIONAL-INDEX update | Required |
| D9 | No code/runtime/DB mutation in charter | Required |
| D10 | Exact-path docs commit; no push | Required |

---

## 5. Stop conditions (implementation)

- Wrong DB / host / missing backup / missing confirm flag  
- Attempt to mutate report 1/5  
- Export/share rows already exist for target demo monthlies unexpectedly  
- Unknown user email collision  
- Volume/workspace mismatch  

Emit STOP tokens per MARS guardrails and abort.
