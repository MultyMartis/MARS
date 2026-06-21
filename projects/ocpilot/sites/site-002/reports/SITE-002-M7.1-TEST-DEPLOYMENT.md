# REPORT — BZPM M7.1 TEST Deployment

**Project:** BZPM / SITE-002  
**Environment:** https://zpm.new-site.space/ (TEST only)  
**Deploy UTC:** 2026-06-14 17:36:22  
**Operator approval:** M7.1 confirmed · TEST deploy authorized  
**Commit / push / production:** **NOT performed**

---

## Deploy summary

| Item | Result |
|------|--------|
| Files deployed | **10** (1 created + 9 modified) |
| Target | TEST FTP (`polygonws.beget.tech`) |
| Twig cache | **cleared recursively** — 72 entries removed under `system/storage/cache/template/` |
| Deploy manifest | `m7.1-launch-mode-work/backups/m7.1-launch-mode-deploy-20260614-173622.json` |
| QA artifact | `qa/m7.1-launch-mode/m7.1-launch-mode-qa-result.json` |

---

## Pre-deploy breadcrumb audit

Проверка цепочек **до** заливки (live TEST):

| Page type | URL | «Каталог» crumb | Chain |
|-----------|-----|-----------------|-------|
| **PLP leaf** | `/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/` | **Да** → `/katalog` | Главная → **Каталог** → Нейтральное оборудование → Столы → … → current |
| **PLP parent** | `/katalog/nejtralnoe-oborudovanie/stoly/` | **Да** → `/katalog` | Главная → **Каталог** → Нейтральное оборудование → current |
| **PDP** | SP-P-18/6 sample | **Нет** | Главная → Нейтральное оборудование → … → product (pre-existing) |

**Вывод pre-deploy:** замена `href` у «Каталог» затрагивает только `category.php` (PLP / nested PLP). PDP не содержит отдельного crumb «Каталог» — регрессия маловероятна.

---

## Post-deploy breadcrumb verification

| Page type | «Каталог» href (post) | Chain intact |
|-----------|----------------------|--------------|
| **PLP leaf** | `/katalog/nejtralnoe-oborudovanie` | **Да** — все промежуточные категории сохранены |
| **Nested parent** (`/stoly/`) | `/katalog/nejtralnoe-oborudovanie` | **Да** |
| **PDP** | (нет crumb «Каталог») | **Да** — цепочка категорий без изменений |

**Post-deploy PLP chain (leaf):**

1. Главная → `/`
2. **Каталог → `/katalog/nejtralnoe-oborudovanie`** *(изменено с `/katalog`)*
3. Нейтральное оборудование → `/katalog/nejtralnoe-oborudovanie`
4. Столы → … → current leaf

**Примечание:** «Каталог» и «Нейтральное оборудование» ведут на один hub — ожидаемо в Launch Mode, навигация не ломается.

---

## QA checklist results (14/14 PASS)

| ID | Check | Status |
|----|-------|--------|
| QA-01 | `/katalog` → 200, no redirect | **PASS** |
| QA-02 | `/katalog` → exactly **1** root card | **PASS** |
| QA-03 | `/katalog/nejtralnoe-oborudovanie` → 200 | **PASS** |
| QA-04 | Leaf PLP → 200 | **PASS** |
| QA-05 | Sample PDP → 200 | **PASS** |
| QA-06 | Megamenu → single neutral root | **PASS** |
| QA-07 | Footer → neutral only (+ custom equipment) | **PASS** |
| QA-08 | Mobile «Каталог» → neutral | **PASS** |
| QA-09 | Megamenu «Открыть страницу каталога» → neutral | **PASS** |
| QA-10 | PLP breadcrumb «Каталог» → neutral | **PASS** |
| QA-11 | Nested category breadcrumb «Каталог» → neutral | **PASS** |
| QA-12 | PDP breadcrumb chain intact (no Catalog level) | **PASS** |
| QA-13 | No meta refresh on `/katalog` | **PASS** |
| QA-14 | Hidden root direct URL → 200, no redirect | **PASS** |

Evidence: `projects/ocpilot/sites/site-002/qa/m7.1-launch-mode/m7.1-launch-mode-qa-result.json`

---

## URL verification matrix

| URL | HTTP | Redirect | Launch Mode expectation | Result |
|-----|------|----------|-------------------------|--------|
| https://zpm.new-site.space/ | 200 | no | Home megamenu/footer/mobile filtered | **OK** |
| https://zpm.new-site.space/katalog | 200 | no | 1× neutral card | **OK** |
| https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie | 200 | no | Neutral hub | **OK** |
| https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/ | 200 | no | Nested PLP + breadcrumb | **OK** |
| https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/ | 200 | no | Leaf PLP + filters/cards | **OK** |
| https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/stol-proizvodstvennyy-sp-p-18-6-1800h600h850 | 200 | no | PDP V5.1 unaffected | **OK** |
| https://zpm.new-site.space/katalog/teplovoe-oborudovanie | 200 | no | Hidden root still accessible (no nav links) | **OK** |

---

## Files deployed (TEST)

| Remote path | SHA256 |
|-------------|--------|
| `system/library/zpm/category_visibility.php` | `a17fd7ee66448962f5290da151668163c2a5ac60af0348a8c47e183c9a8a59a4` |
| `catalog/controller/product/katalog.php` | `f91b9a894c55fa50d689de39df6ef44ec5d4e4180f66ae462069695c2ae9cc0e` |
| `catalog/controller/product/category.php` | `71ae2e3676cbcc4a53d982e8a2922601530a760ccf809b9980055d820e1ecef6` |
| `catalog/controller/common/header.php` | `804548a608a1579eeacc92ded17bcf27b8966ec244fff53f4446ba1ab08e4bc2` |
| `catalog/controller/common/footer.php` | `1d4b15cb9fd96a7cc792d6c3b3a43c15b01924535a6517d2af8a7a42cd19a7c5` |
| `catalog/controller/common/home.php` | `8bdf16d6ee30078d541518bfc23fd39683f2676cf6cc44a1413440fa47d16a00` |
| `catalog/view/theme/default/template/common/megamenu.twig` | *(see deploy manifest)* |
| `catalog/view/theme/default/template/common/footer.twig` | *(see deploy manifest)* |
| `catalog/view/theme/default/template/sections/catalogsections.twig` | *(see deploy manifest)* |
| `catalog/view/theme/default/template/sections/offcanvasmenu.twig` | *(see deploy manifest)* |

Full hashes: `m7.1-launch-mode-work/backups/m7.1-launch-mode-deploy-20260614-173622.json`

---

## Rollback (TEST)

1. Restore from `m7.1-launch-mode-work/backups/*.pre-m7.1-launch-mode.bak`
2. Delete `system/library/zpm/category_visibility.php`
3. Clear `system/storage/cache/template/` (recursive)
4. Verify 9 cards on `/katalog`, 9 megamenu tabs, breadcrumb «Каталог» → `/katalog`

---

## Risks / notes

| Note | Detail |
|------|--------|
| Hidden roots | Direct URLs still 200 — by design (M7.1 scope); not linked from nav |
| PDP breadcrumbs | No «Каталог» level — unchanged from pre-M7.1 |
| PLP redundancy | «Каталог» and «Нейтральное оборудование» both → neutral hub — acceptable |
| Production | **Not deployed** — TEST only |

---

## Git status

```
?? projects/ocpilot/sites/site-002/m7.1-launch-mode-work/
?? projects/ocpilot/sites/site-002/qa/m7.1-launch-mode/
?? projects/ocpilot/sites/site-002/reports/SITE-002-M7.1-LAUNCH-MODE-IMPLEMENTATION.md
?? projects/ocpilot/sites/site-002/reports/SITE-002-M7.1-TEST-DEPLOYMENT.md
```

**Commit:** NO · **Push:** NO · **Production deploy:** NO

---

## Operator sign-off

M7.1 Launch Mode **live on TEST**. Рекомендуется визуальная проверка megamenu / footer / mobile в браузере, затем решение о production (отдельный charter).
