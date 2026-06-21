# REPORT — BZPM M9.7C IMAGE DEPLOY + MEGAMENU CLEANUP

**Режим:** TEST only — https://zpm.new-site.space/  
**Authority:** SITE-002-STABLE-M9-COMPLETE-20260615 · REPORT-BZPM-M9.7B-CATEGORY-IMAGE-GENERATION.md  
**Production:** не затронут  
**Commit / push:** не выполнялись

---

## 1. Root cause — empty categories in megamenu

**Классификация: D) mixed source (controller data + category query)**

| Слой | Файл | Поведение до фикса | Доказательство |
|------|------|-------------------|----------------|
| **C) Category query** | `catalog/controller/product/katalog.php` | Кэш `cat-list-header` строится через `getCategories()` **без** фильтра `getTotalProducts() > 0` для `children` | Baseline lines 64–74: все дочерние категории cat 79 попадают в кэш |
| **B) Controller data** | `catalog/controller/common/header.php` | Читает кэш, применяет только `filterRootCategories()` (Launch Mode на **корнях**), **не** фильтрует `children` | Baseline line 165: `filterRootCategories(unserialize($catlist))` |
| **A) Twig** | `catalog/view/theme/default/template/common/megamenu.twig` | Рендерит **все** `mainc.children` без условий | Lines 47–64: `{% for c in mainc.children %}` |
| **Эталон (правильно)** | `catalog/controller/product/category.php` | Hub mode **уже** скрывает ветки с `totalsub <= 0` | Lines 189–193 |

**Live до фикса (2026-06-14):** 12 плиток в neutral megamenu — 5 с товарами + 7 с `0 шт.` (Стеллажи, Полки, Подтоварники, Тележки, Шкафы, Лари, Столы производственные).  
**Evidence:** `m9.7c-image-megamenu-work/m9.7c-live-probe.py` · `.recovery-temp/m9.7a-hub-live.html`

**Почему hub был чище megamenu:** hub использует `getNeutralHubBranchIds()` + runtime count filter; megamenu — полный DB subtree из кэша.

---

## 2. Files modified

### Deployed to TEST (FTP)

| Remote path | Действие |
|-------------|----------|
| `system/library/zpm/category_visibility.php` | **modified** — `prepareMegamenuCategories()` |
| `catalog/controller/common/header.php` | **modified** — runtime enrich + filter перед megamenu |
| `catalog/controller/product/katalog.php` | **modified** — filter при build cache + `prepareMegamenuCategories()` |

### Local worktree (patch + tooling)

| Path | Действие |
|------|----------|
| `projects/ocpilot/sites/site-002/m9.7c-image-megamenu-work/patch/...` | patch sources |
| `projects/ocpilot/sites/site-002/m9.7c-image-megamenu-work/m9.7c-deploy.py` | deploy script |
| `projects/ocpilot/sites/site-002/m9.7c-image-megamenu-work/m9.7c-qa.py` | QA script |
| `projects/ocpilot/sites/site-002/m9.7c-image-megamenu-work/m9.7c-live-probe.py` | pre-fix probe |
| `projects/ocpilot/sites/site-002/m9.7c-image-megamenu-work/backups/m9.7c-deploy-20260614-215218.json` | deploy manifest |
| `projects/ocpilot/sites/site-002/m9.7c-image-megamenu-work/qa/m9.7c-qa-result.json` | QA evidence |
| `projects/ocpilot/sites/site-002/reports/REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md` | этот отчёт |

**Pre-deploy backups (live rollback copies):**  
`m9.7c-image-megamenu-work/backups/pre-m9.7c-*`

---

## 3. Images deployed

| Файл | Canvas | Size | SHA256 (prefix) | Remote |
|------|--------|-----:|-----------------|--------|
| `stoly.webp` | 1800×1200 | 65 KB | `1c8804f5…` | `image/catalog/Category-image/stoly.webp` |
| `moechnye-vanny.webp` | 1800×1200 | 83 KB | `d2bc204a…` | `image/catalog/Category-image/moechnye-vanny.webp` |
| `podtovarniki-i-podstavki.webp` | 1800×1200 | 59 KB | `7ad714d1…` | `image/catalog/Category-image/podtovarniki-i-podstavki.webp` |
| `zonty-vytyazhnye.webp` | 1800×1200 | 113 KB | `453eb18a…` | `image/catalog/Category-image/zonty-vytyazhnye.webp` |
| `telezhki-servirovochnye.webp` | 1800×1200 | 107 KB | `8ed52705…` | `image/catalog/Category-image/telezhki-servirovochnye.webp` |

**Валидация:** WebP valid (PIL), H=1200, источник M9.7B `image/catalog/Category-image/`.

**Resize на storefront:** OpenCart генерирует `image/cache/catalog/Category-image/{slug}-300x300.webp` — подтверждено в QA.

---

## 4. DB records updated

`oc_category.image` (TEST `polygonws_zpm`):

| category_id | Категория | image (после) | rows affected |
|---:|---|---|--:|
| 301 | Столы | `catalog/Category-image/stoly.webp` | 1 |
| 80 | Моечные ванны | `catalog/Category-image/moechnye-vanny.webp` | 1 |
| 322 | Подтоварники и подставки | `catalog/Category-image/podtovarniki-i-podstavki.webp` | 1 |
| 207 | Зонты вытяжные | `catalog/Category-image/zonty-vytyazhnye.webp` | 1 |
| 326 | Тележки сервировочные | `catalog/Category-image/telezhki-servirovochnye.webp` | 1 |

**До:** все 5 полей `image` пустые (baseline `oc_category.json`).  
**Evidence:** `backups/m9.7c-deploy-20260614-215218.json` → `db_updates`

---

## 5. Before / after — megamenu neutral children

### Before (12 tiles)

Подтоварники и подставки (11), Столы (419), Тележки сервировочные (3), Зонты вытяжные (23), Моечные ванны (152), **Столы производственные (0)**, **Стеллажи (0)**, **Полки (0)**, **Подтоварники (0)**, **Шкафы (0)**, **Тележки (0)**, **Лари (0)** — все с `placeholder-300x300.png`.

### After (5 tiles)

Подтоварники и подставки (11), Столы (419), Тележки сервировочные (3), Зонты вытяжные (23), Моечные ванны (152) — реальные WebP thumbs, **0 zero-count**.

---

## 6. QA results

**Summary:** 17 PASS · 0 FAIL  
**Evidence:** `m9.7c-image-megamenu-work/qa/m9.7c-qa-result.json`

| Check | Result |
|-------|--------|
| HOME `/` | PASS HTTP 200, no PHP warnings |
| `/katalog` | PASS |
| `/katalog/nejtralnoe-oborudovanie` hub | PASS — 5 cards, real images |
| Branch PLPs 301/80/322/207/326 | PASS HTTP 200 |
| Reference PDPs (table + sink) | PASS HTTP 200 |
| Megamenu — 5 tiles only | PASS |
| Megamenu — no zero-count | PASS |
| Megamenu — no forbidden empty cats | PASS |
| Megamenu + hub — no placeholders | PASS |

**Hub card images (after):** все 5 → `image/cache/catalog/Category-image/*-300x300.webp`

---

## 7. Rollback procedure

1. **PHP:** восстановить из `m9.7c-image-megamenu-work/backups/pre-m9.7c-*` → upload на TEST:
   - `category_visibility.php`
   - `header.php`
   - `katalog.php`
2. **DB (optional — только если откат изображений нужен):**
   ```sql
   UPDATE oc_category SET image = '' WHERE category_id IN (301,80,322,207,326);
   ```
3. **Images (optional):** удалить 5 новых WebP из `image/catalog/Category-image/` на TEST (не трогать эталонные root images).
4. **Cache:** очистить `system/storage/cache/` (`cache.cat-list-header*`), `system/storage/cache/template/`, соответствующие `image/cache/catalog/Category-image/*-300x300.webp`.
5. **Baseline reference:** `SITE-002-STABLE-M9-COMPLETE-20260615/files/`

---

## 8. Risks

| Risk | Level | Note |
|------|-------|------|
| Stale `cat-list-header` cache | Low | Фикс применяет runtime filter в `header.php`; rebuild cache в `katalog.php` тоже фильтрует |
| Image cache lag | Low | Первый hit регенерирует thumb; QA подтвердил корректные URL |
| Direct URL access to hidden cats | None (by design) | Категории остаются в DB; скрытие только в megamenu/katalog cache |
| Production drift | None | Production не трогали |

---

## 9. Git status

Локальные изменения: patch/work scripts, report, M9.7B images в `image/catalog/Category-image/` — **untracked/uncommitted**.  
**No commit · no push** (policy).

---

## UNKNOWN / SECURITY RISK

**UNKNOWN:** точный механизм появления `count` у children в **старом** serialized cache (до фикса) — вероятно legacy enrichment при первичном build; не блокирует fix (runtime recount в `prepareMegamenuCategories`).

**SECURITY RISK:** нет. FTP/DB credentials — existing project ops pattern; не коммитились.

---

## Stop

M9.7C complete on TEST. Awaiting operator visual HITL on 300×300 image quality if required.
