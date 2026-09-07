# REPORT — SITE-002-PROD-PDP-HERO-SPECS-HLEBOPEKARNOE-186-01

**Final verdict:** `SITE-002 PDP HERO SPECS HLEBOPEKARNOE 186 COMPLETE — OPERATOR VISUAL CHECK REQUIRED`

**Date:** 2026-09-07T08:30:22+00:00  
**Site:** SITE-002 / https://bzpm.ru/  
**Target:** category `[186]` — Хлебопекарное оборудование (children `[188]`/`[189]`)  
**Operation:** `SITE-002-PROD-PDP-HERO-SPECS-HLEBOPEKARNOE-186-01`

---

## 1. Scope

Additive family-specific PDP hero specs for bakery products under root `[186]`, reusing existing `ProductHeroSpecsResolver` architecture introduced for `[86] Стеллажи`.

## 2. Operator decision

Operator reviewed combined visual QA for M9/PDP work. Remaining gap: bakery mixer/testomes PDP hero showed mostly dimensions/mass; bakery-specific attrs missing from upper `.product-hero__specs`. Bounded production wave approved.

## 3. Production safety boundary

| Gate | Value |
|------|--------|
| DB writes | **0** (SELECT only) |
| Product/category/SEO/import/baseline | **0** |
| M9 profile / global_hidden / SUPER_ATTS | **unchanged** |
| FTP deploy | Exact resolver file only |
| product.php | **not redeployed** (already wired) |
| Cleanup/delete | **0** |

## 4. Docs / architecture read

See Storage `docs-read/docs-read.csv` and `preflight/current-pdp-hero-architecture.md`.

Architecture: Twig `super_atts` ← product.php dimensions + `ProductHeroSpecsResolver` family IDs; fallback SUPER_ATTS; `[86]` protected.

## 5. `[186]` PDP before state

See `pdp-before/pdp-before.csv`.

- mixer_188: status=200 hero_names=`Длина, мм | Ширина, мм | Высота, мм | Масса, кг` bakery_hits=0
- testomes_189: status=200 hero_names=`Длина, мм | Ширина, мм | Высота, мм | Масса, кг` bakery_hits=0
- stellazhi_86_regression: status=200 hero_names=`Длина, мм | Ширина, мм | Высота, мм | Масса, кг | Конструкция | Максимальная распределенная нагрузка на полку (кг) | Ножки | Тип опоры` bakery_hits=0

## 6. Attribute inventory

- Products CSV: `db-readonly/category-186-pdp-products.csv`
- Attrs CSV: `db-readonly/category-186-pdp-attributes-by-product.csv`
- Candidate analysis: `attribute-analysis/pdp-hero-candidate-attrs-186.md`

Preferred samples:

- Mixer: {'product_id': '4714', 'category_id': '188', 'name': 'Миксер универсальный  В30', 'public_url': 'https://bzpm.ru/hlebopekarnoe-oborudovanie/miksery-planetarnye/mikser-universalnyy-v30', 'bakery_attr_count': 5, 'bakery_attr_ids': '127,129,130,134,135'}
- Testomes: {'product_id': '4692', 'category_id': '189', 'name': 'Тестомес ТТ-D25D', 'public_url': 'https://bzpm.ru/hlebopekarnoe-oborudovanie/testomesy/testomes-tt-d25d', 'bakery_attr_count': 7, 'bakery_attr_ids': '127,128,130,132,134,135,137'}

## 7. Hero specs decision

Shared `[186]` order after L/W/H/mass:

`127, 135, 134, 130, 129, 128, 132, 137`

Empty skipped; duplicates skipped; lower Характеристики preserved.

## 8. Files changed

| File | Action |
|------|--------|
| `/public_html/system/library/zpm/product_hero_specs_resolver.php` | PATCH additive `[186]` |
| `catalog/controller/product/product.php` | NO CHANGE |
| Twig / M9 / config | NO CHANGE |

## 9. Backup / rollback

- Backups: `file-backups/live-before/`
- Inventory: `file-backups/file-backup-inventory.csv`
- Plan: `rollback/rollback-plan.md`
- Resolver SHA256 before: `452ebf1ee480854ac91b75acd807b158e22468dd6b74ba157529ce7dccbe4657`

## 10. Deploy

See `deploy/deploy-summary.md` — resolver upload verify match=True expected.

## 11. Cache

Narrow OpenCart `storage/cache` top-level cache file clear — `cache/cache-action-summary.md`.

## 12. Public after

- mixer_188: status=200 hero_names=`Длина, мм | Ширина, мм | Высота, мм | Масса, кг | Объем | Мощность, кВт | Напряжение | Количество скоростей | Загрузка сухого продукта` bakery_hits=5
- testomes_189: status=200 hero_names=`Длина, мм | Ширина, мм | Высота, мм | Масса, кг | Объем | Мощность, кВт | Напряжение | Количество скоростей | Загрузка теста | Скорость об/мин | Реверс` bakery_hits=7
- stellazhi_86_regression: status=200 hero_names=`Длина, мм | Ширина, мм | Высота, мм | Масса, кг | Конструкция | Максимальная распределенная нагрузка на полку (кг) | Ножки | Тип опоры` bakery_hits=0

## 13. Screenshots

Folder: Storage `screenshots/` — status in `screenshot-status.txt` (SAFE UNKNOWN acceptable if capture tool missing).

## 14. Regression

- Shelving OK: True
- PLP/katalog OK: True
- Details: `regression/regression-summary.md`

## 15. OPERATOR CHECK — ПРОВЕРИТЬ PDP ХЛЕБОПЕКАРНОГО

See Storage `operator-check/operator-check.md`.

- Mixer URL: https://bzpm.ru/hlebopekarnoe-oborudovanie/miksery-planetarnye/mikser-universalnyy-v30
- Testomes URL: https://bzpm.ru/hlebopekarnoe-oborudovanie/testomesy/testomes-tt-d25d
- Shelving URL: https://bzpm.ru/nejtralnoe-oborudovanie/stellazhi/stellazh-dlya-defrostacii-stpd-p-10-6-1000h600h1800

FAIL if: 500/blank, broken price/cart/image, missing Характеристики, broken `[86]` hero, empty/dupe rows, БЗПМ, PHP warnings.

## 16. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PDP-HERO-SPECS-HLEBOPEKARNOE-186-01\`

## 17. Git status

Default: **no commit** (unpushed commits + foreign WIP). Optional selective commit of this report only if operator requests.

## 18. SAFE UNKNOWN / blockers

- Screenshot automation may be SAFE UNKNOWN if Playwright unavailable.
- Do not confuse `[186]` with old `[368]` under technological tree.

## 19. Final verdict

`SITE-002 PDP HERO SPECS HLEBOPEKARNOE 186 COMPLETE — OPERATOR VISUAL CHECK REQUIRED`

## 20. Next recommendation

Operator visual check of mixer/testomes hero screenshots; if PASS, continue next family PDP hero wave only by explicit charter.
