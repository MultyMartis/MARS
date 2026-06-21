# REPORT — SITE-002 STABLE CATEGORY V2.2 BASELINE

**Baseline name:** `SITE-002-STABLE-CATEGORY-V2.2-2026-06-10`
**Site:** SITE-002 (BZPM / ЗПМ TEST)
**Environment:** https://zpm.new-site.space/
**Captured at (UTC):** 2026-06-09T21:55:36.964406+00:00
**Mode:** Read-only — no FTP writes, no deploy, no rollback

---

## 1. Backup folder

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-category-v2.2-2026-06-10`

## 2. Included files

| Local name | Remote path | Size (bytes) |
|------------|-------------|--------------|
| `category.twig` | `catalog/view/theme/default/template/product/category.twig` | 4276 |
| `productcard.twig` | `catalog/view/theme/default/template/product/productcard.twig` | 5710 |
| `product_results.php` | `catalog/controller/product/product_results.php` | 6046 |
| `style.css` | `assets/css/style.css` | 273764 |
| `main.js` | `assets/js/main.js` | 183265 |

**Manifest:** `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-category-v2.2-2026-06-10\stable-category-v2.2-manifest.json`

## 3. SHA256 summary

| File | SHA256 |
|------|--------|
| `category.twig` | `b636ad2ee1047411a8e590a19db4b1e4e52bd7b5f09ced26a71765ac7ba4934e` |
| `productcard.twig` | `7f073b94ba22eee9fa237dccf8efb63c93666b1039c6af2c9b652bd6c97ce05e` |
| `product_results.php` | `64c46c39852f9711e22e2bf4f83d70f0055b66d8ed5223845df08567c91374f7` |
| `style.css` | `c2cdc2e4bebaba3f30ade2ee8a99e1a3c69171feba46ddbbfe2d468bb4193003` |
| `main.js` | `d69e586405008c26579d73857b7d2c2c08a590e39f53ff0b2a406f472cbced45` |

## 4. Стабильное состояние (Stable Category V2.2)

Зафиксировано live-состояние **после** CATEGORY V2.2 list-card compactness pass, **перед** работой над блоком «Подкатегории»:

- Category grid mode works.
- Category list mode works.
- View switcher grid/list works.
- Localstorage zpm_category_view works.
- List-card compactness pass applied.
- Primary specs in list mode work.
- Grid/mobile not broken.
- PDP V4 not affected.

**Included scope:** category PLP (grid + list), view switcher, list-card layout/commerce/compactness, primary specs in list mode.

**Out of scope / unchanged:** PDP V4 templates and assets not in this backup set.

## 5. Rollback instructions

Use when subcategory block work must be reverted to pre-subcategory stable V2.2 state.

1. Verify SHA256 of backup files match §3.
2. Upload each file from backup folder to matching remote path on FTP (`polygonws.beget.tech`):

   - `category.twig` → `catalog/view/theme/default/template/product/category.twig`
   - `productcard.twig` → `catalog/view/theme/default/template/product/productcard.twig`
   - `product_results.php` → `catalog/controller/product/product_results.php`
   - `style.css` → `assets/css/style.css`
   - `main.js` → `assets/js/main.js`

3. Clear Twig cache — delete contents of `system/storage/cache/template/`.
4. Hard-refresh browser (CSS/JS cache).
5. Verify category PLP:
   - Grid mode — card grid, commerce, no list-only compact layout.
   - List mode — compact list cards, primary specs visible, no overlap.
   - View switcher — Grid/List toggle; `localStorage` key `zpm_category_view` persists choice.
6. Verify mobile category layout (grid stack, no horizontal overflow).
7. Verify PDP V4 — hero, commerce, documents sidebar unchanged (SPKB SKU).

## 6. QA summary

Last verified pass before this baseline: **CATEGORY V2.2 LIST CARD COMPACTNESS** (2026-06-09).

Reference QA artifact:
`projects/ocpilot/sites/site-002/qa/category-v2.2-list-card-compactness/category-v2.2-list-card-compactness-qa-result.json`

| Area | Status at capture |
|------|-------------------|
| Grid mode (desktop + mobile) | PASS — card grid, commerce intact |
| List mode (desktop) | PASS — compact cards, primary specs, no overlap |
| View switcher | PASS — Grid/List toggle active |
| localStorage `zpm_category_view` | PASS — persists view choice |
| PDP V4 | PASS — not touched by category V2.2 passes |

Category probe URL: `https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-serii-premium/stoly-premium-600/`

## 7. Confirmation

**Stable Category V2.2 baseline successfully captured**

*Generated 2026-06-09T21:55:36.964406+00:00 — read-only capture; site unchanged.*
