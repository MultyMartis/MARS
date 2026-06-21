# REPORT — CATEGORY V2.1 LIST CARD COMMERCE PASS

**Site:** SITE-002 (BZPM / ЗПМ TEST)  
**Environment:** https://zpm.new-site.space/  
**Baseline:** SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER + CATEGORY V2 VIEW SWITCHER PASS  
**Deployed at (UTC):** 2026-06-09T21:17:05Z

---

## 1. Backup paths

Pre-change live captures (FTP read-only):

| File | Backup path |
|------|-------------|
| `product_results.php` | `projects/ocpilot/sites/site-002/backups/product_results.php.pre-list-card-commerce-pass.bak` |
| `productcard.twig` | `projects/ocpilot/sites/site-002/backups/productcard.twig.pre-list-card-commerce-pass.bak` |
| `style.css` | `projects/ocpilot/sites/site-002/backups/style.css.pre-list-card-commerce-pass.bak` |

Deploy manifest: `projects/ocpilot/sites/site-002/backups/category-v2.1-list-card-commerce-deploy-manifest-20260609-211705.json`

---

## 2. Changed files

| Local work copy | Remote path |
|-----------------|-------------|
| `category-v2.1-list-card-commerce-work/product_results.php` | `catalog/controller/product/product_results.php` |
| `category-v2.1-list-card-commerce-work/productcard.twig` | `catalog/view/theme/default/template/product/productcard.twig` |
| `category-v2.1-list-card-commerce-work/style.css` | `assets/css/style.css` |

Supporting (not deployed): deploy script, QA script under `category-v2.1-list-card-commerce-work/`.

---

## 3. PHP changes

In `product_results.php`, before `$card` assembly:

- Build `$primary_specs = []` from standard `$result` fields only (no SQL, no SUPER_ATTS).
- **Длина, мм** → `intval($result['length'])` if `> 0`
- **Ширина, мм** → `intval($result['width'])` if `> 0`
- **Высота, мм** → `intval($result['height'])` if `> 0`
- **Масса, кг** → `round((float)$result['weight'], 2)` if `> 0`
- Pass `'primary_specs' => $primary_specs` into `$card`; all existing keys preserved.

---

## 4. Twig changes

In `productcard.twig`, inside `.p-card__body` after status block:

```twig
{% if primary_specs %}
  <dl class="p-card__primary-specs">
    {% for spec in primary_specs %}
      <div class="p-card__primary-spec">
        <dt>{{ spec.name }}</dt>
        <dd>{{ spec.text }}</dd>
      </div>
    {% endfor %}
  </dl>
{% endif %}
```

Cart, qty, wishlist, compare, price, title, article, status — unchanged.

---

## 5. CSS scope

**Global (safe default):**

```css
.p-card__primary-specs { display: none; }
```

**List-view only** (`@media (min-width: 1025px)`):

- `.page--category .category--view-list .p-card__primary-specs` → `display: grid`, row 4 / column 2
- Compact 4-column grid using `--border-color`, `--main-light-color`, `--radius-main`, `--pad-gap*`, `--mini-Font-size`, `--large-Font-size`
- `.p-card` grid rows extended to 4 for specs row
- No changes outside `.page--category .category--view-list`

---

## 6. QA grid / list

**Category GRID (desktop 1920–1280):** specs in DOM but `display: none` — PASS  
**Category LIST (desktop 1920–1280):**

| Check | Result |
|-------|--------|
| Specs visible (`display: grid`) | PASS |
| 4 values (Длина/Ширина/Высота/Масса) | PASS (sample: 1800 / 600 / 850 / 36.5) |
| Photo width 200px | PASS |
| Cart / qty / wishlist / compare / подробнее | PASS |
| Horizontal overflow | PASS (none) |

**1024×768 note:** list CSS applies from `min-width: 1025px` (pre-existing view-switcher breakpoint). At 1024px list class may be set via JS but layout remains grid — expected, not introduced by this pass.

QA JSON: `projects/ocpilot/sites/site-002/qa/category-v2.1-list-card-commerce/category-v2.1-list-card-commerce-qa-result.json`

---

## 7. Shared contexts regression

| Context | Cards | Visible specs blocks | Pass |
|---------|-------|----------------------|------|
| Search | yes | 0 | PASS |
| Wishlist | yes | 0 | PASS |
| Compare | 0 | 0 | PASS |

---

## 8. PDP V4 regression

URL: SPKB-18-7-VL5 SKU  
Hero 3 cols, commerce card, content, documents, related — PASS  
Related carousel: 0 visible `.p-card__primary-specs` — PASS

Screenshot: `qa/category-v2.1-list-card-commerce/pdp-v4-regression-1920.png`

---

## 9. Screenshots

**Grid:** `qa/category-v2.1-list-card-commerce/category-grid-{1920,1440,1366,1280,1024}.png`  
**List:** `qa/category-v2.1-list-card-commerce/category-list-{1920,1440,1366,1280,1024}.png`  
**Mobile grid:** `qa/category-v2.1-list-card-commerce/category-mobile-grid-{768,576,390,375,360}.png`

Mobile: specs hidden on all tested viewports — PASS

---

## 10. Rollback procedure

1. Upload backup files from §1 to FTP:
   - `product_results.php.pre-list-card-commerce-pass.bak` → `catalog/controller/product/product_results.php`
   - `productcard.twig.pre-list-card-commerce-pass.bak` → `catalog/view/theme/default/template/product/productcard.twig`
   - `style.css.pre-list-card-commerce-pass.bak` → `assets/css/style.css`
2. Clear `system/storage/cache/template/` on FTP.
3. Verify category list mode — specs block absent.
4. Verify category grid unchanged.
5. Verify PDP V4 regression on SPKB SKU.

---

## 11. Git status

Work artifacts under `projects/ocpilot/sites/site-002/` (backups, work dir, QA, report).  
**Commit:** NO  
**Push:** NO

---

**Pass complete:** list-view category cards show compact primary dimensions/mass; grid, mobile, shared contexts, and PDP V4 unchanged.
