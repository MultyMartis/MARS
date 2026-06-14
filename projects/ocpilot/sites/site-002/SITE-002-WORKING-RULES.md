# SITE-002 — Working Rules (ЗПМ / BZPM)

**Environment:** TEST — https://zpm.new-site.space/  
**Full audit:** [reports/SITE-002-LESSONS-LEARNED-ANTI-REGRESSION-AUDIT-v1.md](reports/SITE-002-LESSONS-LEARNED-ANTI-REGRESSION-AUDIT-v1.md)  
**Updated:** 2026-06-14

---

## DO

- **Capture live first** — если оператор правил на FTP, сделать FTP read + SHA256 до любых правок агента.
- **Operator manual live edits are source-of-truth** — после ручных правок оператора live на хостинге считается каноном; старые work-копии и repo STABLE-папки **не** использовать как текущее состояние без свежего live-capture.
- **Before any next change, capture only the specific live files that will be touched** — не полный сайт; только файлы из scope следующей задачи.
- **Do not rely on old work copies after manual edits** — `*-work/`, `backups/stable-*` до manual pass, `.pre-*.bak` от прошлых волн.
- **Name baseline** в каждой задаче (PDP V4, Category V2.2, или `.pre-<pass>.bak`).
- **Backup before deploy** — `backups/*.pre-<pass>.bak` + deploy manifest JSON.
- **Document DOM/data chain** — controller → twig → CSS → JS hooks **до** правок.
- **Scope lock** — explicit ALLOWED + FORBIDDEN files в prompt.
- **Isolate category CSS** — только `.page--category`; list-only — `.category--view-list` + `@media (min-width: 1025px)`.
- **PDP V4 regression** после любого category или shared CSS/JS/Twig pass.
- **Clear Twig cache** — `system/storage/cache/template/` после deploy.
- **Preserve hooks** — `data-cart-add`, `data-fav-toggle`, `data-compare-toggle`, `data-fancybox`, `docs-list` + `download` + `href`.
- **Archive failed states** — `*.failed-*` backups, не только pre-pass.
- **Mark SAFE UNKNOWN** — если ветка Twig/SKU не live-проверена.
- **Report + QA screenshots** в `reports/` и `qa/`; git commit только по запросу оператора.

---

## DO NOT

- **Не трогать `productcard.twig`** без отдельного разрешения оператора.
- **Не менять shared partials** (`productcard`, `header`, `relproducts`) без анализа всех мест использования.
- **Не менять стили**, если задача только структурная (Twig/HTML).
- **Не менять font-size / color / typography** без явного разрешения.
- **Не добавлять новые визуальные паттерны** (dealer CTA, B2B row, text action buttons, новые секции).
- **Не удалять** Assum brand, subtitle mechanism, round wishlist/compare icons.
- **Не трогать** `config.php`, DB, OCMOD без отдельного charter.
- **Не коммитить** deploy scripts с FTP credentials.
- **Не деплоить** без rollback section в отчёте.
- **Не claim PASS** для empty docs, pagination AJAX, Cases B/D без live SKU.
- **Не проектировать 8-cell hero** без проверки fill rate (`SUPER_ATTS` 13/15 = 0%).
- **Не возвращать** сломанный `product-content__top` 70/30 layout.

---

## Backup rules

| When | What |
|------|------|
| Any FTP write | Live FTP → `backups/*.pre-<pass-name>.bak` |
| Wave complete | STABLE folder + `stable-*-manifest.json` + report |
| Failed pass | `*.failed-<pass>.*` before rollback |
| Operator manual edit | Immediate live capture → update stable |

**Rollback tiers:**

1. **Point** — `*.pre-<pass>.bak` (last pass only)
2. **STABLE** — full checkpoint folder (see below)
3. **Emergency PDP** — `stable-pdp-v4-2026-06-10/`

**Always:** manifest with SHA256; byte-verify before upload on rollback.

---

## QA rules

### Minimum every deploy

1. Pre-deploy backup exists  
2. Twig cache cleared  
3. No PHP/Twig errors  
4. Rollback path documented  

### PDP (SPKB-18/7-ВЛ5)

Hero 3-col · SUPER_ATTS/FA icons · commerce + service cards · cart/qty/fav/compare · gallery · lower block no tabs · documents sidebar · mobile overflow 768/390/360

### Category (Столы ПРЕМИУМ-600)

Grid @1920/1440/1280 · list @≥1025 · view switcher + localStorage · switcher hidden ≤1024 · card commerce hooks · **PDP V4 regression**

### If `productcard.twig` changed

Search · wishlist · compare · related — **0 visible** `.p-card__primary-specs` outside list mode

### Gaps → SAFE UNKNOWN

Fancybox click · cart click · `pagination__more` · empty docs live SKU · multi-image thumbs

---

## Shared component danger list

| File | Blast radius | Rule |
|------|--------------|------|
| `productcard.twig` | Category, search, wishlist, compare, related | **RESTRICTED** — separate approval |
| `style.css` | Entire storefront (PDP + category + …) | Scope selectors; PDP regression mandatory |
| `main.js` | Filters, sort, view switcher, subcat, cart | Test filter AJAX after changes |
| `producthero.twig` | All PDPs | Hero passes only |
| `producttabs.twig` | PDP lower block | Structure + docs contract |
| `category.twig` | PLP + subcats | Category passes only |
| `product_results.php` | Card data in listings | Changes `primary_specs` etc. |
| `header.twig` | FA Pro CSS link | FA/install passes only |
| `config.php` | DB credentials | **Never edit** without charter; sensitive in backups |

---

## Current stable baselines

| Name | Path / type | Use for rollback |
|------|-------------|------------------|
| **Live manual compact ★** | [baselines/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14.md) — metadata only | **Active checkpoint** — rollback via Beget global backup + operator live state |
| PDP V4 (historical) | `backups/stable-pdp-v4-2026-06-10/` | Pre-manual-edit PDP — may not match live |
| PDP V3 | `backups/stable-pdp-v3-2026-06-10/` | Pre-documents-final |
| PDP V2 | `backups/stable-pdp-v2-2026-06-09/` | Hero + commerce + **tabs** |
| Category V2.2 (historical) | `backups/stable-category-v2.2-2026-06-10/` | Pre-manual-edit category — may not match live |
| Category pre-switcher | `backups/SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER/` | No view switcher |
| Pre-W1A hero | `backups/producthero.twig.pre-w1a.bak` | Original 50/50 hero |
| Failed W1A (do not restore) | `backups/producthero.twig.failed-w1a.*` | Audit reference only |

**Post-manual-edit live:** canonical truth = hosting + Beget global backup. Repo file baselines are **historical** unless refreshed by targeted live-capture.

**FA Pro vendor:** `assets/vendor/fontawesome-pro-5.15.4/**` — not in stable PDP folders; restore separately.

---

## Reference SKUs (TEST)

| Context | SKU / category |
|---------|----------------|
| PDP + docs | SPKB-18/7-ВЛ5 (tumba) |
| PDP dims pilot | СП-П-18/6 (стол) |
| Category leaf | Столы ПРЕМИУМ-600 |
| Subcategories | `/stoly-serii-premium/` parent |

---

## Security

- Credentials: `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\` only  
- FTP host: `polygonws.beget.tech` — CWD `/` = public_html  
- `config.php` in backups = **sensitive**  
- No credentials in repo / reports / commits

---

*Operational quick-ref. See full audit for evidence and stage-by-stage lessons.*
