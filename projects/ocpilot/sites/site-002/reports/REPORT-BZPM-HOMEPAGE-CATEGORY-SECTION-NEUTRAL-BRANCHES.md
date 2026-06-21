# REPORT — BZPM HOMEPAGE CATEGORY SECTION NEUTRAL BRANCHES

**Дата:** 2026-06-15  
**Среда:** TEST only — https://zpm.new-site.space/  
**Authority:** SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI · live capture pre-deploy  
**Режим:** deploy на TEST · **NO COMMIT** · **NO PUSH** · **NO PRODUCTION**

---

## 1. Root cause

После M7.1 Launch Mode блок категорий на главной (`catalog/controller/common/home.php`) брал данные из кэша `cat-list-header` и пропускал их через `CategoryVisibility::filterRootCategories()`.

`filterRootCategories()` предназначен для **root-level** навигации (megamenu, footer, `/katalog` roots) и в Launch Mode оставляет только категорию **79 — «Нейтральное оборудование»**.

После M9.5/M9.7C hub и megamenu уже показывают **5 живых веток** (`getNeutralHubBranchIds()` → 301, 80, 322, 207, 326) с runtime-фильтром `getTotalProducts() > 0`, но homepage **не была переведена** на эту логику и осталась на старом root-only пути.

**Twig не виноват:** `sections/catalogsections.twig` корректно рендерит массив `$data['categories']`; проблема только в источнике данных контроллера.

---

## 2. Safety check (pre-change)

| Проверка | Результат |
|----------|-----------|
| Live FTP capture `home.php` + `category_visibility.php` | ✅ `backups/pre-m9.7e-live__*` |
| Homepage до фикса | **1 карточка** — «Нейтральное оборудование» → `/katalog/nejtralnoe-oborudovanie` |
| `filterRootCategories()` на homepage | ✅ использовался — root cause подтверждён |
| `getNeutralHubBranchIds()` в `category_visibility.php` | ✅ уже есть (301, 80, 322, 207, 326) |
| Hub / megamenu / Twig / CSS карточек | **не трогались** |
| БД | **не требовалась** |
| Ручные правки оператора (CSS/Twig) | **не откатывались** |

---

## 3. Files modified (live TEST)

| Файл | Изменение |
|------|-----------|
| `catalog/controller/common/home.php` | В Launch Mode: `buildHomepageCategoryCards($this)` вместо `filterRootCategories(unserialize($catlist))` |
| `system/library/zpm/category_visibility.php` | Новый метод `buildHomepageCategoryCards()` — reuse `getNeutralHubBranchIds()` + count filter + `img` 300×300 |

**Repo patch (local):**

- `projects/ocpilot/sites/site-002/m9.7e-homepage-neutral-branches-work/patch/catalog/controller/common/home.php`
- `projects/ocpilot/sites/site-002/m9.7e-homepage-neutral-branches-work/patch/system/library/zpm/category_visibility.php`

**Не изменялись:** `catalogsections.twig`, megamenu, hub, M9 profiles, header/footer/katalog controllers, БД, CSS.

---

## 4. Before / After

### Before (live pre-deploy)

- Homepage category section: **1** карточка  
  - «Нейтральное оборудование»  
  - img: `/image/catalog/Category-image/nejtralnoe-oborudovanie-2.webp`  
  - href: `/katalog/nejtralnoe-oborudovanie`

### After (live post-deploy)

- Homepage category section: **5** карточек (vetки neutral hub)  
- Root «Нейтральное оборудование» **отсутствует** в блоке  
- Изображения: WebP 300×300 из `image/catalog/Category-image/` (cache resize)  
- Порядок: commercial priority list M9.5 (301 → 80 → 322 → 207 → 326)

---

## 5. Final homepage category list

| ID | Название | href | image |
|----|----------|------|-------|
| 301 | Столы | `/katalog/nejtralnoe-oborudovanie/stoly` | `.../stoly-300x300.webp` |
| 80 | Моечные ванны | `/katalog/nejtralnoe-oborudovanie/moechnye-vanny` | `.../moechnye-vanny-300x300.webp` |
| 322 | Подтоварники и подставки | `/katalog/nejtralnoe-oborudovanie/podtovarniki-i-podstavki` | `.../podtovarniki-i-podstavki-300x300.webp` |
| 207 | Зонты вытяжные | `/katalog/nejtralnoe-oborudovanie/zonty-vytyazhnye` | `.../zonty-vytyazhnye-300x300.webp` |
| 326 | Тележки сервировочные | `/katalog/nejtralnoe-oborudovanie/telezhki-servirovochnye` | `.../telezhki-servirovochnye-300x300.webp` |

Набор **идентичен** hub `/katalog/nejtralnoe-oborudovanie` (имена, ссылки, изображения).

---

## 6. QA results

**Script:** `m9.7e-homepage-neutral-branches-work/m9.7e-qa.py`  
**Evidence:** `m9.7e-homepage-neutral-branches-work/qa/m9.7e-qa-result.json`  
**Summary:** **13 PASS / 0 FAIL / 0 WARN**

| Check | Result |
|-------|--------|
| `/` HTTP 200, no PHP errors | PASS |
| Homepage 5 cards, correct set & order | PASS |
| No root «Нейтральное оборудование» card | PASS |
| No forbidden empty branches | PASS |
| No placeholder images | PASS |
| `/katalog` HTTP 200 | PASS |
| `/katalog/nejtralnoe-oborudovanie` hub 5 cards | PASS |
| `/stoly/`, `/moechnye-vanny/` HTTP 200 | PASS |
| Megamenu neutral: 5 tiles, no zero-count | PASS |

---

## 7. Rollback procedure

1. **Point rollback (preferred):** восстановить live из pre-deploy backup:
   - `m9.7e-homepage-neutral-branches-work/backups/pre-deploy-20260614-224916__catalog__controller__common__home.php`
   - `m9.7e-homepage-neutral-branches-work/backups/pre-deploy-20260614-224916__system__library__zpm__category_visibility.php`
2. Upload на TEST FTP (`polygonws.beget.tech`, public_html) поверх текущих файлов.
3. Очистить `system/storage/cache/template/` (Twig cache).
4. Verify: homepage снова показывает **1** карточку «Нейтральное оборудование».

**Deploy manifest:** `m9.7e-homepage-neutral-branches-work/backups/m9.7e-deploy-20260614-224916.json`

---

## 8. Git status

**Commit / push:** не выполнялись (по заданию).

**Новые локальные артефакты задачи:**

- `projects/ocpilot/sites/site-002/m9.7e-homepage-neutral-branches-work/` (patch, deploy, QA, backups)
- `projects/ocpilot/sites/site-002/reports/REPORT-BZPM-HOMEPAGE-CATEGORY-SECTION-NEUTRAL-BRANCHES.md`

---

## UNKNOWN / SECURITY

- **UNKNOWN:** нет — live QA PASS на всех проверенных URL.
- **SECURITY RISK:** deploy script содержит FTP credentials (как в prior M9.7C work); не коммитить credentials в repo.
