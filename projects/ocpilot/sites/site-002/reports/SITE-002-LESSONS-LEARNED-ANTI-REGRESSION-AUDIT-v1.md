# SITE-002 LESSONS LEARNED / ANTI-REGRESSION AUDIT v1

**Site ID:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Audit date:** 2026-06-10  
**Mode:** Read-only analysis — no site changes, no deploy, no commit  
**Sources:** `projects/ocpilot/sites/site-002/reports/` (29 reports), `qa/`, `backups/`, `*-work/`  
**Evidence horizon:** Run 5 baseline (2026-06-09) through CATEGORY V2.3.1 (2026-06-09/10)

---

## 1. Executive Summary

За короткий цикл SITE-002 на TEST прошли **PDP hero redesign (failed W1A → rollback → W1A.2)**, **полный PDP rollback pre-W1A**, **SUPER_ATTS discovery**, **PDP V2→V4** (hero, commerce, content rebuild, documents), **Mobile Pass V1**, **Category Audit V1**, **Category V2** (view switcher → list card → compactness → subcategory chips V2.3/V2.3.1), **Font Awesome Pro**.

Главный вывод: **большинство регрессий — не «технические баги», а нарушение scope, shared blast radius и расхождение с live-source-of-truth**. Успешные проходы (W1A.2, Mobile Pass V1, V2.2 compactness, View Switcher CSS-only list) объединяет **явный scope lock, backup до deploy, изоляция селекторов и PDP V4 regression после category-правок**.

Критические anti-regression якоря:

| Якорь | Назначение |
|-------|------------|
| `SITE-002-STABLE-PDP-V4-2026-06-10` | Канонический PDP rollback |
| `SITE-002-STABLE-CATEGORY-V2.2-2026-06-10` | Канонический category rollback (до subcategory) |
| `*.failed-w1a.*` | Архив проваленного hero — не повторять паттерны |
| `*.pre-<pass>.bak` + deploy manifest | Точечный rollback каждого прохода |

**SAFE UNKNOWN:** текущий live после V2.3.1 без свежего STABLE-capture; FA Pro vendor bundle не в stable PDP folders; edge Twig-ветки (empty docs, Cases B/D) не live-проверены на всех SKU.

---

## 2. Главные выводы

### 2.1 Что работало

- **Rollback-дисциплина после W1A failure** — failed state сохранён (`producthero.twig.failed-w1a.*`), W1A.2 восстановил brand, round icons, buy box position.
- **Read-only discovery до writes** — W1B Hero Attribute Strategy, Category Audit V1 дали data-backed решения.
- **CSS-only passes с scope** — Mobile Pass V1, V2.2 compactness, View Switcher list mode (без второго Twig).
- **Stable snapshots** — PDP V2/V3/V4, Category V2 pre-switcher, Category V2.2 с SHA256 manifests.
- **Operator manual edits как source of truth** — stable PDP V4/V3 явно фиксируют operator-refined live state.

### 2.2 Что ломалось или откатывалось

- **Failed W1A** — scope creep: удалён бренд Assum, subtitle, dealer/B2B CTA, text action buttons, commercial-first mobile.
- **Content Visual Structure Pass** — сломанная структура `product-content__top` (70/30 + full-width specs); исправлено в Content Layout Fix.
- **Full PDP rollback pre-W1A** — потребовался byte-identical restore hero + tabs + CSS после W1B scroll sections.
- **Category V2.1** — нарушение плана «не трогать productcard.twig»; компенсировано global `display: none` + list-only show.

### 2.3 Системные риски (не закрыты полностью)

- **`style.css` и `main.js` — общий blast radius** PDP + category + search + wishlist/compare contexts.
- **`SUPER_ATTS` (12,13,15)** — 13/15 = 0% fill; ID 12 дублирует L/W/H; нельзя проектировать 8-cell hero без data check.
- **Shared partial `productcard.twig`** — search, related, wishlist, compare, category grid/list.
- **Credentials** — FTP в local deploy scripts; `config.php` с DB creds в stable backups.
- **Admin BLOCKED** на baseline — нет theme editor / modification UI verification.

---

## 3. Повторяющиеся ошибки

### 3.1 Ошибки Cursor / агента

| # | Паттерн | Пример из артефактов | Severity |
|---|---------|----------------------|----------|
| E-01 | **Scope creep** — добавление фич вне задачи | Failed W1A: dealer CTA, B2B row, удаление brand | Critical |
| E-02 | **Визуальные фантазии** — новые UI-паттерны без approval | Text wishlist/compare вместо round `btn-no-text` | High |
| E-03 | **Игнорирование shared CSS blast radius** | Category passes требовали PDP V4 regression — не всегда делалось до фикса процесса | High |
| E-04 | **Plan vs implementation drift** | View Switcher: план text «Сетка/Список» → deploy FA icons | Medium |
| E-05 | **Предположение о данных** | 8-cell fit grid при 4 dims на pilot SKU; SUPER_ATTS 13/15 empty | High |
| E-06 | **Структура до CSS / CSS без структуры** | Visual pass сломал layout → отдельный layout fix pass | High |
| E-07 | **Touch forbidden partial** | `productcard.twig` изменён в V2.1 despite Phase 1 «CSS-only list» | High |
| E-08 | **Неполная edge QA** | Cases B/D content matrix, empty docs branch — static only | Medium |
| E-09 | **Inventing hooks** | «Быстрый заказ» → `#zpmFbCallback` после SAFE UNKNOWN | Medium |
| E-10 | **Работа без live capture** | Operator manual edits в hero/docs не captured до stable snapshot | Medium |

### 3.2 Ошибки постановки задач

| # | Паттерн | Пример |
|---|---------|--------|
| T-01 | Задача «структурная», но без запрета на typography/color | Content passes меняли spacing, font-size без явного scope |
| T-02 | Нет explicit FORBIDDEN file list | W1A map есть scope lock; category V2.1 — productcard не в forbidden |
| T-03 | Нет baseline name в prompt | Mobile Pass явно ссылается на V4 SHA — хороший контрпример |
| T-04 | Pilot SKU не покрывает family | Стол СП-П-18/6 ≠ sink/tumba families; thermal/cold = 0 SKUs |
| T-05 | Backup как «operator action» без gate | Run 5 BLOCKED: backup unknown HIGH |

### 3.3 Где менялись стили без разрешения

| Pass | Что произошло | Доказательство |
|------|---------------|----------------|
| Failed W1A | Новые action button styles, dealer row, context band | W1A.2 comparison table |
| Content Visual Pass | `product-content__top` grid ratios, mobile order hacks | Content Layout Fix § «Removed product-content__top» |
| Category V2.1 | Typography tokens в `.p-card__primary-specs` | V2.1 commerce pass CSS scope |
| View Switcher | Pill buttons styling (planned text → FA icons) | View Switcher PASS §3 |

### 3.4 Где ломалась структура

| Incident | Broken | Fix |
|----------|--------|-----|
| Failed W1A | Buy box detached from 3-col row; brand removed | W1A.2 rebuild |
| W1B scroll sections | Tabs → sections (later full rollback) | PDP Full Rollback pre-W1A |
| Content Visual Pass | `product-content__top` 70/30 + specs below | Content Layout Fix: `product-content__main` 7fr/3fr |
| V2.1 productcard | New DOM block in shared partial | Global hide + list-only grid placement |

### 3.5 Где нужен был backup раньше

| Moment | Gap | Impact |
|--------|-----|--------|
| Run 5 / Wave 1 start | Backup status UNKNOWN, HIGH risk | Wave 1 readiness BLOCKED |
| Before failed W1A | Pre-w1a backups появились, но failed state archiving — урок для будущего | Rollback possible, но с потерей времени |
| Before operator manual edits | Stable captures post-factum | V4 delta mixes operator + agent passes |
| Before V2.3.1 | STABLE V2.3.1 not captured (optional per report) | Rollback only via `.pre-subcategory-polish-pass.bak` |

### 3.6 Где нужно было читать DOM/цепочку данных

| Area | Gap | Lesson |
|------|-----|--------|
| SUPER_ATTS | Assumed 8 cells; live = 4 dims from `oc_product` | Read `product.php` + DB fill rates first |
| Category filter AJAX | Cards = pre-rendered HTML; `updateProducts()` replaces grid | Document before JS changes |
| `pagination__more[data-next]` | Click behavior SAFE UNKNOWN | Probe before assuming infinite scroll |
| CTA hooks | «Быстрый заказ» dedicated modal unknown | Map `#zpmFbCallback` / `#zpmFbQuestion` first |
| Breadcrumbs → series context | Heuristic `breadcrumbs[n-2]` fragile | W1A.2 R-01 High |

### 3.7 Shared partials — зафиксированные риски

| File | Contexts | Incident |
|------|----------|----------|
| `productcard.twig` | Category grid/list, search, wishlist, compare, related | V2.1 changed despite plan |
| `style.css` | Entire storefront | Every category pass → PDP regression |
| `main.js` | Filters, sort, view switcher, subcat IIFE | V2.3+ touches |
| `producthero.twig` | All PDPs | Failed W1A, multiple stable baselines |
| `producttabs.twig` | PDP lower block | Tabs→sections→rebuild→documents chain |
| `header.twig` | FA Pro CSS link | Stable PDP bundles |

---

## 4. Анти-ошибочные правила (общие)

1. **Live-source-of-truth** — если оператор правил руками на FTP, сначала **capture live** (FTP read + SHA256), потом работать от snapshot.
2. **Backup before any write** — FTP pull → `*.pre-<pass>.bak` + deploy manifest JSON; deploy без rollback section запрещён.
3. **Scope lock в каждой задаче** — explicit ALLOWED paths + FORBIDDEN paths (см. §6–§10).
4. **No scope creep** — не добавлять dealer CTA, B2B rows, новые кнопки, новые секции без explicit approval.
5. **No visual invention** — не менять font-size, color, typography, border-radius, shadows без explicit approval.
6. **Structural task ≠ style task** — если задача только Twig/structure, CSS diff должен быть minimal/none.
7. **DOM/data chain first** — controller → twig variables → CSS selectors → JS hooks documented BEFORE edits.
8. **Shared file rule** — touch `productcard.twig`, `style.css`, `main.js` → mandatory regression matrix (§12).
9. **Failed state archive** — сохранять `*.failed-*`, не только pre-pass backups.
10. **SAFE UNKNOWN honesty** — не claim PASS для untested branches (empty docs, pagination, missing SKUs).
11. **PDP V4 regression** — mandatory после любого category CSS/JS/Twig pass.
12. **Twig cache** — clear `system/storage/cache/template/` после deploy.
13. **Не коммитить** deploy scripts с FTP credentials.

---

## 5. Правила для PDP

### 5.1 Scope

| Allowed (typical pass) | Forbidden (unless explicit charter) |
|------------------------|-------------------------------------|
| `producthero.twig` (hero-only pass) | `config.php`, DB, OCMOD |
| `producttabs.twig` (content pass) | `catalog/controller/product/product.php` (unless SUPER_ATTS work chartered) |
| `style.css` (scoped PDP blocks) | `category.twig`, `productcard.twig` |
| `header.twig` (FA Pro only) | Mass controller/model edits |

### 5.2 Hero-specific

- **Сохранять:** Assum brand (`product-hero__brand`), round wishlist/compare (`btn-no-text`), subtitle mechanism (conditional hide placeholder only).
- **Не добавлять:** dealer CTA, B2B preview row, text action buttons, commercial-first mobile order (gallery must stay early per W1A.2).
- **SUPER_ATTS:** не расширять IDs 12/13/15 без CMS fill; pilot часто показывает **4 dims** (L/W/H/weight), не 8 cells.
- **3-column DOM:** `product-hero__col--media`, `--info`, `--commerce` — не ломать без rebuild plan.

### 5.3 Lower block (V4 frozen)

- **No tab UI** — static sections: description, specifications, documents sidebar.
- **Preserve:** `docs-list` type class, `href`, `download`, `docs-list__download`, empty-state `product-content__docs-empty`.
- **Hooks:** `#zpmFbQuestion`, `#zpmFbCallback` — document before CTA label changes.
- **Не возвращать** `product-content__top` 70/30 pattern (proven broken in visual pass).

### 5.4 Mobile Pass pattern

- **CSS-only** append at end of `style.css`.
- **Baseline SHA** = PDP V4 (`084c402a…` for pre-mobile-pass backup).
- Desktop rules untouched.

### 5.5 PDP rollback reference

**Primary:** `backups/stable-pdp-v4-2026-06-10/` + manifest SHA256.  
**Note:** FA Pro vendor `assets/vendor/fontawesome-pro-5.15.4/**` — restore separately.

---

## 6. Правила для Category

### 6.1 Scope isolation

```css
/* Mandatory pattern */
.page--category { /* category-only rules */ }
.page--category .category--view-list { /* list-only, desktop */ }
@media (min-width: 1025px) { /* list mode layout */ }
```

- Switcher **hidden ≤1024**; strip `category--view-list` on mobile.
- List mode = **CSS reorder only** unless operator approves second Twig partial.

### 6.2 View switcher

- `localStorage` key: `zpm_category_view` (`grid`|`list`).
- Inline FOUC guard after `<section class="category">`.
- After filter AJAX: verify `updateProducts()` preserves view class.

### 6.3 List card / specs (V2.1+)

- `primary_specs` from `product_results.php` — standard `oc_product` fields only (length/width/height/weight).
- **Prefer:** CSS-only specs display; **if** `productcard.twig` must change → explicit approval + shared context regression.
- Global: `.p-card__primary-specs { display: none; }` — list-only show.

### 6.4 Subcategory chips (V2.3 / V2.3.1)

- Collapse max 2 lines; toggle «Показать все подкатегории».
- V2.3.1 = polish only (icons, chevron, labels) — logic frozen from V2.3.
- Leaf category: block empty OK.

### 6.5 Category rollback reference

**Primary:** `backups/stable-category-v2.2-2026-06-10/` (pre-subcategory).  
**Pre-switcher:** `backups/SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER/`.  
**V2.3.1 point rollback:** `*.pre-subcategory-polish-pass.bak`.

---

## 7. Правила для shared components

### 7.1 `productcard.twig` — RESTRICTED

**Default: DO NOT TOUCH without separate operator approval.**

If approved:

1. Document all include contexts (category, search, wishlist, compare, related/Swiper).
2. Regression matrix: grid mode specs hidden; list mode specs visible; search/wishlist/compare/related = **0 visible** `.p-card__primary-specs`.
3. Preserve: `data-cart-add`, `data-qty-*`, `data-fav-toggle`, `data-compare-toggle`, price, status, article.

### 7.2 `producthero.twig` — PDP-critical

- Hero-only passes may touch; category passes must NOT.
- Compare against stable PDP V4 SHA before deploy.

### 7.3 `producttabs.twig` — PDP lower block

- Structure passes require backup + SPKB SKU QA.
- Do not reintroduce tab UI without explicit charter.

### 7.4 `category.twig`

- Category passes OK; verify PDP unaffected.
- Subcategory block scoped to `.page--category`.

### 7.5 `filterssidebar.twig`

- Out of scope for V2 passes but coupled to filter AJAX — note in task if filters break.

### 7.6 `relproducts.twig`

- Swiper cards must NOT receive list-mode primary specs styles.

---

## 8. Правила для CSS

1. **Scope selectors** — `.page--category`, `.category--view-list`, `.product-hero`, `.product-content` — never global leaky rules.
2. **No unauthorized typography** — do not change `--mini-Font-size`, `--large-Font-size`, font-family, color tokens unless task explicitly allows.
3. **Reuse design system** — `--main-dark-color`, `--border-color`, `--radius-main`, `--pad-gap*`.
4. **Structural-only task** — CSS diff should be zero or scoped to layout (grid/flex/order/display) without aesthetic changes.
5. **Append mobile blocks** at end of `style.css` with comment banner (`SITE-002 — PDP MOBILE PASS V1` pattern).
6. **No `transition: all`** on interactive elements (align with starter progressive enhancement rules).
7. **After any `style.css` change** — PDP V4 + category QA viewports.

---

## 9. Правила для Twig

1. **Read live twig first** — FTP capture before edit; operator manual diffs are truth.
2. **Preserve hooks** — `data-*` attributes, `aria-*`, existing class names used by JS.
3. **Conditional blocks** — keep `{% if %}` logic for empty description, documents, images.
4. **No invented variables** — use only controller-provided data; document fallbacks.
5. **Include chain** — `product.twig` → `producthero` + `producttabs` + `relproducts`; do not add wrapper files without plan.
6. **docs-list contract** — type class on link, `download` attribute, valid `href`.
7. **One partial rule** — list view via CSS on same `productcard.twig`, not duplicate partial unless approved.

---

## 10. Правила для JS

1. **`main.js` is shared** — category view module, filters, sort, subcat IIFE; PDP gallery/cart may share globals.
2. **Prefer data-* hooks** — `data-category-view`, `data-category-view-mode`, `data-cart-add`, etc.
3. **Filter AJAX** — test `updateProducts()` after changes; cards re-render from server HTML.
4. **localStorage** — `zpm_category_view`; handle `resize` + desktop guard `matchMedia('(min-width: 1025px)')`.
5. **No inline scripts in Twig** except documented FOUC guard pattern in `category.twig`.
6. **Verify execution path** before patching — script loaded, selectors match, no silent `import()` failures.
7. **`pagination__more`** — SAFE UNKNOWN until probed; do not assume behavior.

---

## 11. Правила для backups

### 11.1 When to backup

| Trigger | Action |
|---------|--------|
| Any FTP write | Pre-deploy `.pre-<pass>.bak` from **live** FTP |
| Multi-file wave start | STABLE snapshot folder + manifest + report |
| Failed implementation | Archive `*.failed-<pass>.*` before rollback |
| Operator manual edit detected | Capture live immediately → update stable baseline |
| Before rollback | Document which backup tier (pre-pass vs stable vs pre-w1a) |

### 11.2 Naming convention (observed)

- `*.pre-<pass-name>.bak` — point-in-time pre-deploy
- `*.failed-w1a.*` — failed implementation archive
- `stable-pdp-v{N}-YYYY-MM-DD/` — frozen checkpoint folder
- `*-deploy-manifest-YYYYMMDD-HHMMSS.json` — SHA256 evidence

### 11.3 Stable baselines registry

| Name | Path | Use |
|------|------|-----|
| PDP V4 ★ | `backups/stable-pdp-v4-2026-06-10/` | Canonical PDP rollback |
| PDP V3 | `backups/stable-pdp-v3-2026-06-10/` | Pre-documents-final |
| PDP V2 | `backups/stable-pdp-v2-2026-06-09/` | Hero + commerce + tabs |
| Hero FA icons | `backups/stable-hero-fa-icons-2026-06-09/` | Post FA switch, pre-commerce |
| Category V2.2 ★ | `backups/stable-category-v2.2-2026-06-10/` | Pre-subcategory |
| Category pre-switcher | `backups/SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER/` | No view switcher |
| Pre-W1A hero | `backups/producthero.twig.pre-w1a.bak` | Original 50/50 hero |

### 11.4 Gaps to close

- STABLE CATEGORY V2.3.1 — not captured (recommended after next operator approval).
- FA Pro vendor bundle — not in stable PDP folders.
- Run 5 era — no pre-work backup (lesson learned).

---

## 12. Правила для QA

### 12.1 Every deploy (minimum)

- [ ] Pre-deploy backup + manifest SHA256
- [ ] Twig cache cleared
- [ ] PHP/Twig errors absent on TEST
- [ ] Rollback path documented in report
- [ ] Changed files list + git status NO COMMIT

### 12.2 PDP QA (SPKB-18/7-ВЛ5 minimum)

- [ ] Hero 3-col DOM + SUPER_ATTS / primary specs + FA Pro icons
- [ ] Commerce card «Стоимость:» + service card hooks
- [ ] Cart, qty, wishlist, compare functional (DOM hooks present)
- [ ] Gallery / `data-fancybox="product"`
- [ ] Lower block: no tabs; description + specs; documents sidebar
- [ ] `docs-list` links: type class, `download`, `href`
- [ ] `product-help` + `rel-products`
- [ ] Mobile 768/390/360: no horizontal overflow; 2×2 primary specs

### 12.3 Category QA (Столы ПРЕМИУМ-600 + parent with subcats)

- [ ] Grid cols @1920/1440/1280
- [ ] List mode @≥1025: photo 200px (V2.2: 160px compact), specs row, no overlap
- [ ] View switcher + localStorage persist after reload
- [ ] Switcher hidden ≤1024
- [ ] Cart/qty/wishlist/compare on card
- [ ] Filter button present
- [ ] **PDP V4 regression** (mandatory)
- [ ] If `productcard.twig` touched: search/wishlist/compare/related — 0 visible primary specs

### 12.4 Subcategory (V2.3+)

- [ ] Many subcats: collapsed, expand/collapse, no overflow
- [ ] Few subcats: toggle hidden
- [ ] PDP: no subcat block

### 12.5 Automation gaps (mark SAFE UNKNOWN if not run)

- Interactive Fancybox / cart click
- `pagination__more` AJAX
- Empty documents live SKU
- Content Cases B/D live URLs
- Multi-image gallery thumbs SKU

### 12.6 Reference QA artifacts

- `qa/category-v2-view-switcher/category-v2-view-switcher-qa-result.json`
- `qa/category-v2.1-list-card-commerce/`
- `qa/category-v2.2-list-card-compactness/`
- `qa/category-v2.3-subcategory-chips/`
- `qa/category-v2.3.1-subcategory-polish/`
- `qa/category-audit-v1/`
- `qa/mobile-pass-v1/` (screenshots)
- `qa/rollback-pre-w1a/`

---

## 13. Security rules

1. **No credentials in repo** — FTP/DB passwords only in `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\` or operator password manager.
2. **Do not commit** `*-deploy.py`, `*-rollback.py` without credential scrubbing.
3. **`config.php` in stable backups** contains DB credentials — treat as **sensitive**; do not push to public repos.
4. **FTP effective root** — login PWD `/` = `public_html`; secrets doc path `/zpm.new-site.space/public_html/` → 550 error (BASELINE-v1).
5. **No `config.php` exposure** in reports, chat, or commits.
6. **Admin BLOCKED** on baseline — do not attempt brute force; request operator session.
7. **TEST `display_errors`** noted in baseline — low operational leak; do not worsen.
8. **Deploy scripts** — reference external secrets only in documentation.

---

## 14. Cursor prompt rules

### 14.1 Mandatory preamble (copy into every SITE-002 task)

```
SITE-002 (ЗПМ) OCPilot pass

BASELINE: <name> + SHA256 of files to touch
ENV: https://zpm.new-site.space/ (TEST only)
MODE: <read-only | deploy>

ALLOWED FILES:
- <exact remote paths>

FORBIDDEN (do not touch):
- productcard.twig (unless this task explicitly approves)
- config.php, DB, OCMOD
- <other paths outside scope>

DOM/DATA CHAIN (document before edit):
- Controller → twig vars → CSS selectors → JS hooks

BACKUP:
- Capture live FTP → backups/*.pre-<pass>.bak
- Deploy manifest with SHA256
- Rollback section in report

QA:
- PDP: SPKB SKU + viewports
- Category: PREMIUM-600 + PDP V4 regression
- Mark SAFE UNKNOWN for untested branches

OUTPUT:
- Report in projects/ocpilot/sites/site-002/reports/
- NO commit, NO push unless operator requests
```

### 14.2 Task-type additions

| Task type | Extra rules |
|-----------|-------------|
| PDP hero | Preserve brand, round icons, subtitle mechanism; no dealer/B2B |
| PDP content | No `product-content__top`; preserve docs-list contract |
| Category CSS | `.page--category` scope only; PDP V4 regression mandatory |
| Category Twig | Test filter AJAX + view switcher persist |
| Read-only audit | NO FTP writes; evidence to `qa/` |
| Rollback | Byte-verify against manifest; 10-point functional checklist |

### 14.3 Anti-patterns to flag in review

- Removing Assum brand or subtitle entirely
- Text buttons replacing round wishlist/compare
- Changing `productcard.twig` in «CSS-only» task
- Global CSS without `.page--category` guard
- Claiming 8-cell hero without SKU proof
- Deploy without `.pre-<pass>.bak`
- Committing deploy scripts

---

## 15. Чеклист перед любым изменением

- [ ] **Baseline named** — e.g. `SITE-002-STABLE-PDP-V4-2026-06-10` or `STABLE-CATEGORY-V2.2`
- [ ] **Operator approval** for write operations (access brief charter)
- [ ] **Live capture** if operator edited manually since last stable
- [ ] **DOM/data chain documented** — controller, twig, CSS, JS
- [ ] **Scope written** — ALLOWED + FORBIDDEN file lists
- [ ] **Shared partial check** — if touching productcard/style/main.js → regression matrix planned
- [ ] **Backup plan** — `.pre-<pass>.bak` + stable snapshot if multi-file wave
- [ ] **Rollback bytes identified** — which .bak or stable folder
- [ ] **Pilot SKUs chosen** — PDP: SPKB; Category: PREMIUM-600; family coverage checked
- [ ] **SUPER_ATTS/data reality checked** — no assumed 8 cells or empty attribute IDs
- [ ] **No style changes** if task is structural-only
- [ ] **Credentials** — deploy script local only, not for commit

---

## 16. Чеклист после любого изменения

- [ ] **Deploy manifest** saved with SHA256
- [ ] **Twig cache cleared** on FTP
- [ ] **Automated QA** run (or gaps marked SAFE UNKNOWN)
- [ ] **Screenshots** to `qa/<pass-name>/`
- [ ] **Report** written in `reports/`
- [ ] **PDP V4 regression** — if category or shared CSS/JS touched
- [ ] **Shared contexts** — if productcard touched: search/wishlist/compare/related checked
- [ ] **Rollback tested** or rollback procedure documented
- [ ] **Changed files list** in report
- [ ] **Git status** — NO commit unless operator requests
- [ ] **SECURITY NOTE** — no credentials in committed artifacts
- [ ] **STABLE snapshot** — if pass completes a wave (recommend for operator sign-off)

---

## 17. Рекомендации для внедрения в MARS/OCPilot docs

### 17.1 Site-level (SITE-002)

| Action | Target | Priority |
|--------|--------|----------|
| Adopt `SITE-002-WORKING-RULES.md` as operator quick-ref | `projects/ocpilot/sites/site-002/` | High |
| Capture **STABLE CATEGORY V2.3.1** after operator sign-off | `backups/stable-category-v2.3.1-*/` | High |
| Add FA Pro vendor to stable backup checklist | PDP stable capture scripts | Medium |
| Create missing **CATEGORY V2.3 report** retroactively from manifest + QA | `reports/` | Low |
| Update `site-passport.md` status from AWAITING INTAKE → EXECUTION | passport | Medium |

### 17.2 OCPilot program docs (proposed)

| Doc | Content |
|-----|---------|
| `projects/ocpilot/templates/site-pass-working-rules-template.md` | DO/DO NOT, backup, QA, shared danger list |
| `projects/ocpilot/templates/site-pass-cursor-preamble.md` | §14.1 block for all site passes |
| `projects/ocpilot/templates/site-stable-baseline-spec.md` | Naming, manifest, SHA256, rollback report format |
| `projects/ocpilot/templates/shared-partial-regression-matrix.md` | productcard, style.css, main.js contexts |
| Update `project-access-brief` template | Backup confirmed = gate before writes |

### 17.3 MARS governance cross-links

- Align with `governance/operational-survivability.md` — human-operated backup discipline.
- Align with `governance/execution-contracts-overview.md` — task envelope with ALLOWED/FORBIDDEN.
- Align with `governance/reality-audit-framework.md` — SAFE UNKNOWN for untested branches.
- **Not** claiming automated enforcement — documentation patterns only.

### 17.4 Process improvements from SITE-001 learnings parallel

SITE-001 has `RESTORE-POINT-REGISTRY`, write charters, rollback plans — SITE-002 should adopt analogous:

- **Restore point registry** entry per STABLE snapshot
- **Write charter** per multi-file wave (category V2 was implicit, not chartered)
- **Explicit visual impact decision** before CSS typography changes

---

## Appendix A — Stage index (evidence map)

| Stage | Report(s) | Key lesson |
|-------|-----------|------------|
| Baseline Run 5 | `SITE-002-BASELINE-v1.md` | Backup unknown BLOCKED; Admin BLOCKED; FTP root quirk |
| W1A failed → W1A.2 | `SITE-002-WAVE-1A.2-ROLLBACK-AND-REBUILD-v1.md` | Scope creep; failed archive; scope lock works |
| W1A map | `SITE-002-WAVE-1A-IMPLEMENTATION-MAP-v1.md` | SUPER_ATTS ≠ 8 cells; scope lock defined |
| W1B scroll | `SITE-002-WAVE-1B-PDP-SCROLL-SECTIONS-v1.md` | Tabs→sections; super_atts reuse |
| W1B attributes | `SITE-002-WAVE-1B-HERO-ATTRIBUTE-STRATEGY-v1.md` | SUPER_ATTS 12/13/15 data reality |
| Full rollback | `SITE-002-PDP-FULL-ROLLBACK-PRE-W1A-v1.md` | Byte-identical restore; backup tier rationale |
| FA Pro + Hero | `SITE-002-STABLE-HERO-FA-ICONS-2026-06-09.md` | Operator manual = truth |
| PDP V2/V3/V4 | `SITE-002-STABLE-PDP-V*-*.md` | Progressive stable checkpoints |
| Content rebuild/visual/layout/docs | `SITE-002-PDP-CONTENT-*.md` | Structure before CSS; layout fix recovery |
| Mobile Pass V1 | `SITE-002-PDP-MOBILE-PASS-V1.md` | CSS-only append; V4 SHA rollback |
| Category Audit V1 | `SITE-002-CATEGORY-AUDIT-V1.md` | Read-only; PLP lags PDP V4 |
| View Switcher | `SITE-002-CATEGORY-V2-VIEW-SWITCHER-PASS.md` | CSS-only list; localStorage |
| V2.1 commerce/layout | `SITE-002-CATEGORY-V2.1-*.md` | productcard + PHP; shared partial risk |
| V2.2 compactness | `SITE-002-CATEGORY-V2.2-LIST-CARD-COMPACTNESS-PASS.md` | CSS-only; STABLE V2.2 |
| V2.3 chips | manifest + QA only | Collapse/toggle pattern |
| V2.3.1 polish | `SITE-002-CATEGORY-V2.3.1-SUBCATEGORY-POLISH-PASS.md` | Polish only; STABLE optional |

---

## Appendix B — Reference URLs (TEST)

| Purpose | URL pattern |
|---------|-------------|
| PDP QA (tumba + docs) | `/katalog/.../stol-tumba-spkb-18-7-vl5-1800h700h850` |
| PDP pilot (стол dims) | `/katalog/.../stol-proizvodstvennyy-sp-p-18-6-1800h600h850` |
| Category leaf | `/katalog/.../stoly-premium-600/` |
| Category parent (subcats) | `/katalog/.../stoly-serii-premium/` |

---

*Audit v1 — documentation only. No live changes performed. Evidence from repo artifacts as of 2026-06-10.*
