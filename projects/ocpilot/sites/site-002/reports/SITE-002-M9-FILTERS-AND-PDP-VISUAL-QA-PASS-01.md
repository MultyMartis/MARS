# SITE-002-M9-FILTERS-AND-PDP-VISUAL-QA-PASS-01

**Date:** 2026-09-07  
**Site:** SITE-002 / ЗПМ Production (`https://bzpm.ru/`)  
**Mode:** Visual QA + public HTTP smoke only  
**Final verdict:** `SITE-002 M9 FILTERS AND PDP VISUAL QA PASS COMPLETE — OPERATOR REVIEW PACKAGE READY`

## 1. Scope

Combined visual QA after completed M9/PDP waves:

| Wave | Operation |
|------|-----------|
| `[86]` Стеллажи M9 | `SITE-002-PROD-M9-STELLAZHI-PROFILE-86-01` |
| `[86]` Стеллажи PDP hero | `SITE-002-PROD-PDP-HERO-SPECS-STELLAZHI-86-01` |
| `[301]` Столы M9 refresh | `SITE-002-PROD-M9-STOLY-PROFILE-301-REFRESH-01` |
| `[331]` Полки M9 | `SITE-002-PROD-M9-POLKI-PROFILE-331-01` |
| `[186]` Хлебопекарное M9 | `SITE-002-PROD-M9-HLEBOPEKARNOE-PROFILE-186-01` |

Allowed: HTTP GET, Playwright screenshots, safe public filter click/reset, local evidence/report files.  
Forbidden: production mutation (DB/FTP/deploy/cache/import/profile/PDP/template writes).

## 2. Production safety boundary

Evidence: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-M9-FILTERS-AND-PDP-VISUAL-QA-PASS-01\`

| Flag | Value |
|------|-------|
| `db_write_allowed` | false |
| `ftp_write_allowed` | false |
| `deploy_allowed` | false |
| `import_run_allowed` | false |
| `cache_clear_allowed` | false |
| `profile_write_allowed` | false |
| `pdp_specs_write_allowed` | false |
| `screenshot_capture_allowed` | true |

`regression/mutation-summary.csv`: only `http_get_public`, `browser_screenshot`, `filter_click_reset_public` = True. No write/deploy actions performed.

## 3. Pages checked

### PLP

- Стеллажи, Столы, Полки, Миксеры, Тестомесы, Моечные ванны (regression)
- Catalog root, Upakovochnoe, Posuda, Zapchasti (expect 404)

### PDP samples

| Family | URL |
|--------|-----|
| Стеллажи | `https://bzpm.ru/nejtralnoe-oborudovanie/stellazhi/stellazh-dlya-defrostacii-stpd-p-10-6-1000h600h1800` |
| Столы | `https://bzpm.ru/nejtralnoe-oborudovanie/stoly/stol-dlya-sbora-othodov-spso-s-10-6-1000h600h850` |
| Полки | `https://bzpm.ru/nejtralnoe-oborudovanie/polki-nastennye-i-nastolnye/polka-zakrytaya-pzk-p-10-4-1000h400h600` |
| Миксеры | `https://bzpm.ru/hlebopekarnoe-oborudovanie/miksery-planetarnye/mikser-universalnyy-b5` |
| Тестомесы | `https://bzpm.ru/hlebopekarnoe-oborudovanie/testomesy/testomes-sh-20` |

Polki PDP sample was corrected mid-pass (initial listing-like URL lacked hero/chars).

## 4. Filter QA results

HTML sidebar expectation checks (`filter-click-tests/sidebar-expectation-checks.md`):

- **Стеллажи:** Поиск, dims, конструкция полки, нагрузка, ножки; no prominent Стандарт — PASS shape
- **Столы:** material / конструкция полки / борт; `Тип опоры` under secondary — PASS
- **Полки:** конструкция полки / материал / конструкция / нагрузка — PASS
- **Миксеры / Тестомесы:** Объем, Мощность, Напряжение PRIMARY; material not primary — PASS
- **Моечные ванны:** 200, sidebar present (regression smoke)

No PHP warnings / no public `БЗПМ` on checked PLPs.

## 5. Click/reset tests

All four leaf PLPs: PASS render after click + reset; no PHP / no `БЗПМ`.

| Page | Clicked | Cards | Notes |
|------|---------|-------|-------|
| Стеллажи | `in_stock=1` | 15→15→15 | reset via reload |
| Столы | `in_stock=1` | 15→15→15 | reset via reload |
| Полки | `in_stock=1` | 15→15→15 | reset via reload |
| Миксеры | `in_stock=1` | 5→5→5 | reset via reload |

**SAFE UNKNOWN (soft):** automation clicked stock checkbox, not a PRIMARY attribute checkbox. Listing stability and absence of warnings verified; PRIMARY attribute AJAX not proven end-to-end.

## 6. PDP QA results

All five PDPs: HTTP 200, `.product-hero__specs` present, lower `Характеристики` present, no PHP warnings, no public `БЗПМ`. Price/cart/image areas not obviously broken in smoke.

Shelving PDP hero specs remain active; lower characteristics table preserved.

## 7. Screenshots

Folder:  
`...\SITE-002-M9-FILTERS-AND-PDP-VISUAL-QA-PASS-01\screenshots\`

Files `01`–`14` captured (PLP filters, PDPs, system pages). See `screenshots/README.md`.

**Note:** `07-pdp-stellazhi-hero-specs.png` is a small clip (~3.5 KB) of a sparse hero box (`SCREENSHOT_CLIP_SMALL`) — usable for presence, not rich visual review. Prefer `01` PLP + live URL for Web-GPT if needed.

## 8. Regression

- `/zapchasti` → **404**
- `/upakovochnoe-oborudovanie` → **200**, DZ-260 hint present
- `/posuda-i-inventar`, `/katalog/` → **200**
- Expected M9 filter sidebars visible on 86/301/331/188/189 leaves
- No production mutation

## 9. Operator review package

`operator-review/operator-review-package.md`

**Send to Web-GPT first:** `01`–`06` PLP filters, then `08`–`11` PDP heroes, then `07` (small), then `12`–`14` system if needed.

## 10. Storage artifacts

```
.../SITE-002-M9-FILTERS-AND-PDP-VISUAL-QA-PASS-01/
  preflight/  public-smoke/  filter-click-tests/  pdp-checks/
  screenshots/  regression/  operator-review/  git/  reports/  logs/  manifests/
```

Key: `manifests/operation.json`, `public-smoke/public-smoke.csv`, `pdp-checks/pdp-checks.csv`, `filter-click-tests/*`, `screenshots/README.md`.

## 11. Git status

- Branch: `mars/canonical-post-recovery`
- Volume: `AI WS` / workspace `X:\AI MARS`
- Large **foreign WIP** present (ISEO / client-ops / etc.) — not touched
- ~278 unpushed commits vs `origin/mars/canonical-post-recovery`
- **Phase 9 docs commit skipped** (`STOP — UNPUSHED COMMITS PRESENT` + foreign WIP). Report left uncommitted.

## 12. SAFE UNKNOWN / blockers

| Item | Status |
|------|--------|
| PRIMARY attribute click (not stock) | SAFE UNKNOWN — soft |
| Stellazhi PDP screenshot density | SCREENSHOT_CLIP_SMALL — soft |
| Blockers | none |

## 13. Final verdict

**`SITE-002 M9 FILTERS AND PDP VISUAL QA PASS COMPLETE — OPERATOR REVIEW PACKAGE READY`**

## 14. Next recommendation

After operator/Web-GPT visual sign-off: pick next M9 family profile or PDP hero-specs wave per catalog priority plan; do not mutate production from this QA package.
