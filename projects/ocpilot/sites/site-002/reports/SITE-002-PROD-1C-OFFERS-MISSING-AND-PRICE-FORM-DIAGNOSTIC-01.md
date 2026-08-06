# REPORT — SITE-002 1C Offers Missing and Price Form Diagnostic 01

**Operation:** `SITE-002-PROD-1C-OFFERS-MISSING-AND-PRICE-FORM-DIAGNOSTIC-01`  
**OCPilot run:** **4.320**  
**Date:** 2026-08-06  
**Production:** https://bzpm.ru/  
**Verdict:** `SITE-002 OFFERS AND PRICE FORM DIAGNOSTIC COMPLETE — PRICE FORM FIXED, IMPORT ATTENTION`

## 1. Scope

Diagnostic of missing 1C `offers` exchange file vs continuing imports, plus diagnose/fix public «Запросить/Получить прайс-лист» form. No manual import, no category/product/baseline changes. Isolated JS fix allowed if root cause clear.

## 2. Operator request

- 1C specialist not responding; operator sees import present, offers absent (historical pattern: 1C did not upload offers; old file deleted outside site/operator).
- Despite missing offers, check what happened with updates/imports.
- Form «Запросить прайс-лист» (also «Получить прайс-лист» on home) does not send with correct input.

## 3. Client Ops boundary

Client Ops / n8n / Telegram / MetaBOT **not** touched.

## 4. Preflight

- Volume `X:` label **AI WS**
- Authority worktree initially on `site-002-git-authority-realign-after-wave-e` @ `812d1515` (behind origin); foreign WIP left untouched
- Clean commit worktree: `repo-site002-4320` branch `site-002-offers-price-form-4320` from `origin/mars/canonical-post-recovery`
- Prior forensic commit `45d6db18` is ancestor of origin

## 5. Reports read / current state

- Baseline 1879 still authoritative
- 4.319 placement forensic still valid for targets Посуда/Холодильное/Упаковочное
- Form stack: anketa + CSRF + reCAPTCHA + empty-lead guard; recipients admin-managed

## 6. Latest import / log healthcheck

| Field | Value |
|-------|-------|
| Latest TXT | `mars_1c_import_2026-08-06_080005.txt` |
| Run ID | `mars-20260806-080001-8a1a9b1e` |
| Final status | **SUCCESS** |
| Catalog | PASS · `import0_1.xml` · 4.28s |
| Offers | PASS · **(none listed)** · 0.04s |
| Classification | `LATEST_IMPORT_SUCCESS_IMPORT_ONLY` |

Daily natural imports exist for 2026-07-31 … 2026-08-06.

## 7. Exchange files forensic

| File | Present |
|------|---------|
| `import.xml` / `offers.xml` (bare) | **No** |
| `import0_1.xml` | **Yes** (~11.2 MB, MDTM 2026-08-05 17:04:18) |
| `offers0_1.xml` / any `offers0_*.xml` | **No** |

Classification: **`OFFERS_ABSENT_CURRENT`**  
Operator is correct in substance (offers missing); canonical filenames are numbered `import0_1` / `offers0_*`, not bare `import.xml`/`offers.xml`.

## 8. Offers impact forensic

- Offers importer: `glob(.../offers0_*.xml)` → empty list → no price/qty updates; step still PASS
- Does **not** set product `status=0`
- Practical impact: **stale prices/stock** until offers return; catalog XML can still update products/categories

## 9. DB read-only import impact check

- Recipients: `info@bzpm.ru,client.leads@polygon-ws.ru` (restored)
- Category **364** Посуда: **6 products, all status=0**; prices non-zero; `date_modified` 2026-07-27
- Category **95** Холодильное: **0 products**
- ~1639 products `date_modified >= 2026-08-06` (catalog wave today)
- Disabled total products: 8 / 1647

## 10. Sitemap / monitor state

- Sitemap count **1879** · delta **0** · `SITEMAP_MATCHES_BASELINE_1879`
- Monitor `2026-08-06_13-04-53`: `HYGIENE_REVIEW_REQUIRED` (10 added / 10 removed, 10 false-positive suppressed, onboarding 0) · baseline unchanged

## 11. Public import smoke

- Home /katalog 200
- `posuda-i-inventar` empty PLP copy present; category-364 PDPs **404** (disabled)
- No PHP fatal in sampled pages

## 12. Price form inventory

- Home commercial-trust section classes: `zpm-commercial-trust zpm-dealers` + `data-dealers`
- Form title: **«Получить прайс-лист»** · hidden `dialog=7` · fields name/phone/email/message/agree
- Also dialog=3 «Узнать цену» (product price question) — different surface
- Handler route: `checkout/anketa` via dealer isolated handler in `main.js`

## 13. Price form reproduction

- Direct anketa POST (CSRF+reCAPTCHA+fields): **200** `ok:true`
- UI submit with filled fields: **400** empty-lead message
- Network capture: FormData after loading disable contained **only** CSRF + reCAPTCHA

## 14. Price form backend diagnostic

Root cause: `zpmFormSetLoading(form, true)` disables all inputs **before** `new FormData(form)`. Disabled controls are omitted from FormData → empty-lead guard fires.  
Classification before fix: `PRICE_FORM_EMPTY_LEAD_GUARD_FALSE_POSITIVE` secondary to `PRICE_FORM_JS_ERROR` / loading-order bug (reported as frontend validation/empty payload).

## 15. Fix decision gate

**`PRICE_FORM_FIX_APPROVED_ISOLATED`** — reorder FormData before disable in 3 sites (dealer / fancybox / corp CTA).

## 16. Implementation if approved

- Patched production `public_html/assets/js/main.js`
- Repo mirror: `projects/ocpilot/sites/site-002/tools/main_js_price_form_formdata_loading_fix.js`
- Backup: `backups/main.js.ftp-before`
- FTP verify SHA match after STOR

## 17. Post-fix tests / form regression

| Test | Result |
|------|--------|
| Home price-list UI | 200 ok |
| About price-list UI | 200 ok |
| Callback direct | 200 ok |
| Product question direct | 200 ok |
| Dealers/dialog7 direct | 200 ok |
| Empty/service-only guard | 400 |
| JS marker present | yes |
| ALL_PASS | **true** |

## 18. Regression / mutation summary

See `regression/mutation-summary.csv`. Forbidden surfaces untouched.

## 19. Docs update

OPERATIONAL-INDEX run **4.320**, OCPILOT-STATE, production-profile, site-passport, knowledge map, tools README.

## 20. Decision

- Import: `IMPORT_OFFERS_MISSING_ATTENTION`
- Products: `PRODUCT_VISIBILITY_ATTENTION`
- Price form: `PRICE_FORM_FIXED`
- Final: **`SITE-002 OFFERS AND PRICE FORM DIAGNOSTIC COMPLETE — PRICE FORM FIXED, IMPORT ATTENTION`**

## 21. Production mutation summary

| Item | Count |
|------|------:|
| production DB writes | 0 |
| production FTP writes | 1 |
| source/code changes | 1 (`main.js`) |
| template changes | 0 |
| JS changes | 1 |
| cache clear | 0 |
| OCMOD refresh | 0 |
| import runs | 0 |
| scheduler changes | 0 |
| monitor baseline changes | 0 |
| category/product changes | 0 |
| redirect / `.htaccess` | 0 |
| importer/mapping changes | 0 |
| Client Ops / n8n / Telegram | 0 |
| dirty main changes | 0 |
| docs/report changes | yes |

## 22. Git/worktree summary

- Commit worktree: `X:\AI MARS STORAGE\git-sync-e01\repo-site002-4320`
- Branch: `site-002-offers-price-form-4320` → push `origin/mars/canonical-post-recovery`
- Dirty main / prior authority WIP: out of scope

## 23. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-1C-OFFERS-MISSING-AND-PRICE-FORM-DIAGNOSTIC-01\`

## 24. SAFE UNKNOWN / blockers

- Exact 1C-side reason offers were not uploaded: **SAFE UNKNOWN** (needs 1C specialist)
- Whether any archived offers file existed then deleted by exchange automation: **SAFE UNKNOWN** (no archive hits found)
- Monitor 10/10 URL churn detail not fully re-triaged beyond summary JSON (hygiene review already open)

## 25. Final verdict

**`SITE-002 OFFERS AND PRICE FORM DIAGNOSTIC COMPLETE — PRICE FORM FIXED, IMPORT ATTENTION`**

## 26. Next recommendation

1. Ask 1C to upload current `offers0_1.xml` (or `offers0_*.xml`) to `1c_incoming/webdata/` before next morning import.
2. After offers appear, confirm next natural import lists offers inputs and non-trivial offers duration; spot-check prices.
3. Separate charter still needed for category placement (Посуда 364 / Холодильное 95 / Упаковочное) — unchanged from 4.319.
4. Optional: monitor hygiene review for `2026-08-06_13-04-53` URL swap list (no baseline change).
