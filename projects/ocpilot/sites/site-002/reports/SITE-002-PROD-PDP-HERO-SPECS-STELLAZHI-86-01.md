# REPORT — SITE-002-PROD-PDP-HERO-SPECS-STELLAZHI-86-01

Time: 2026-09-06T19:15:52+00:00

## 1. Scope

Bounded PDP `.product-hero__specs` family shortlist for category branch `[86] Стеллажи`.  
Lower «Характеристики» unchanged. No PLP/M9/filter/DB writes.

## 2. Operator decision

After M9 filter profile visual PASS, configure curated hero specs on shelving PDPs.  
Operator sample: `https://bzpm.ru/nejtralnoe-oborudovanie/stellazhi/stellazh-dlya-defrostacii-stpd-p-10-6-1000h600h1800`.

## 3. Production safety boundary

- DB writes: **forbidden** (0)
- Deploy allowlist: resolver NEW + `product.php` PATCH only
- Filter files / Twig / config SUPER_ATTS: **not changed**
- Full characteristics table logic: **not changed**

## 4. Source architecture

- Template: `producthero.twig` → `.product-hero__specs` from `super_atts`
- Controller: `catalog/controller/product/product.php` builds dims then appends attr IDs
- NEW: `system/library/zpm/product_hero_specs_resolver.php`
- Detection: `path` leaf under 86 **or** product via `product_to_category` + `category_path.path_id=86`
- Fallback: global `SUPER_ATTS`

## 5. DB/sample attribute analysis

Samples under path_id=86: **40**

Hero append IDs: `[21, 114, 122, 26, 33]`  
(Конструкция, Количество полок, Макс. нагрузка на полку, Ножки, Тип опоры)

Coverage CSV: Storage `db-readonly/category-86-hero-spec-coverage.csv`

## 6. PDP before

| label | status | hero | pairs |
|-------|--------|------|-------|
| operator_screenshot | 200 | 7 | Длина, мм=1000 | Ширина, мм=600 | Высота, мм=1800 | Масса, кг=48.1 | Конструкция=разборная | Ножки=уголок 40х40 (нержаве |
| shelving_1 | 200 | 7 | Длина, мм=800 | Ширина, мм=600 | Высота, мм=1800 | Масса, кг=26.8 | Конструкция=разборная | Ножки=уголок 40х40 (оцинкова |
| shelving_2 | 200 | 7 | Длина, мм=1000 | Ширина, мм=600 | Высота, мм=1800 | Масса, кг=31.3 | Конструкция=разборная | Ножки=уголок 40х40 (оцинков |

## 7. Spec plan

See Storage `spec-plan/spec-plan.md`. Final append list `[21, 114, 122, 26, 33]` after L/W/H/weight.

## 8. Backup / rollback

- Live `product.php` backed up under `file-backups/live-before/`
- Rollback plan: `rollback/rollback-plan.md`

## 9. Deploy

- product_hero_specs_resolver.php: match=True
- product.php: match=True

## 10. Cache

Cleared template/cache files under production `storage/cache` (see `cache/cache-action-summary.md`).

## 11. PDP after

| label | status | hero | polki | nagruzka | support_in_chars | bzpm | php |
|-------|--------|------|-------|----------|------------------|------|-----|
| operator_screenshot | 200 | 8 | False | True | False | False | False |
| shelving_1 | 200 | 9 | True | True | False | False | False |
| shelving_2 | 200 | 9 | True | True | False | False | False |

## 12. Regression

| label | family | status | hero | bzpm | php |
|-------|--------|--------|------|------|-----|
| stoly | 301 | 200 | 9 | False | False |
| moechnye | 80 | 200 | 10 | False | False |
| dz260_upakovka | non-neutral | 200 | 0 | False | False |

## 13. OPERATOR CHECK — ПРОВЕРИТЬ КАРТОЧКУ ТОВАРА СЕЙЧАС

**Открыть:**

https://bzpm.ru/nejtralnoe-oborudovanie/stellazhi/stellazh-dlya-defrostacii-stpd-p-10-6-1000h600h1800

Также:  
https://bzpm.ru/stellazh-proizvodstvennyy-stpp-s-8-6-800h600h1800
https://bzpm.ru/stellazh-proizvodstvennyy-stpp-s-10-6-1000h600h1800

**Верх `.product-hero__specs`:** Длина → Ширина → Высота → Масса → Конструкция → Количество полок → Макс. нагрузка на полку → Ножки → Тип опоры (только если значения есть).

**Низ «Характеристики»:** полный список; «Регулируемость опоры…» не должна пропасть.

Подробнее: Storage `operator-check/operator-manual-check-instructions.md`.

## 14. Storage artifacts

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PDP-HERO-SPECS-STELLAZHI-86-01\`

## 15. Git status

Branch `mars/canonical-post-recovery` has foreign unpushed commits / WIP.  
**Docs commit skipped** (unsafe selective scope). Report may be uncommitted.

## 16. SAFE UNKNOWN / blockers

- Exact Twig split visual polish: operator visual check
- Whether every shelving SKU has attrs 114/122: coverage CSV (skip empty rows by design)

## 17. Final verdict

**SITE-002 PDP HERO SPECS STELLAZHI 86 COMPLETE — OPERATOR VISUAL CHECK REQUIRED**

## 18. Next recommendation

Operator visual check on 3 shelving PDPs; if FAIL → rollback `product.php` + optional delete resolver; if PASS → optional docs commit of this report only.
