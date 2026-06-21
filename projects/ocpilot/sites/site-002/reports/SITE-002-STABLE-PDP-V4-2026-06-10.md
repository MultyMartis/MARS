# REPORT — SITE-002 STABLE PDP V4 BASELINE

**Baseline name:** `SITE-002-STABLE-PDP-V4-2026-06-10`
**Site:** SITE-002 (ЗПМ TEST)
**Environment:** https://zpm.new-site.space/
**Captured at (UTC):** 2026-06-09T19:56:33.279606+00:00
**Mode:** Read-only — no FTP writes, no deploy, no rollback performed

---

## 1. Backup folder

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10`

## 2. Included files

| Remote path | Local copy | Size (bytes) |
|-------------|------------|--------------|
| `catalog/view/theme/default/template/product/producthero.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10\catalog\view\theme\default\template\product\producthero.twig` | 12067 |
| `catalog/view/theme/default/template/product/producttabs.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10\catalog\view\theme\default\template\product\producttabs.twig` | 4582 |
| `catalog/view/theme/default/template/common/header.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10\catalog\view\theme\default\template\common\header.twig` | 14322 |
| `catalog/controller/product/product.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10\catalog\controller\product\product.php` | 30560 |
| `assets/css/style.css` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10\assets\css\style.css` | 263979 |
| `config.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10\config.php` | 1907 |

**Manifest:** `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v4-2026-06-10\stable-pdp-v4-manifest.json`

## 3. SHA256 summary

| File | SHA256 |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | `ea1226986460fdbe2ae7a1f6c653f225ef49f515d519ffbd1ee45da036c86b69` |
| `catalog/view/theme/default/template/product/producttabs.twig` | `a2e1d402d9f595bf21a16be73cc381c9c12964588030b1b9deb08253d1b66f6b` |
| `catalog/view/theme/default/template/common/header.twig` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` |
| `catalog/controller/product/product.php` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` |
| `assets/css/style.css` | `084c402af786bd817c46657d56dcc085cf7706174db3e62dd6638d2a111c83b2` |
| `config.php` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` |

## 4. Delta vs PDP V3

Comparison against `SITE-002-STABLE-PDP-V3-2026-06-10` (`stable-pdp-v3-manifest.json`):

| File | V3 SHA256 | V4 SHA256 | Changed |
|------|-----------|-----------|---------|
| `catalog/view/theme/default/template/product/producthero.twig` | `ea1226986460fdbe2ae7a1f6c653f225ef49f515d519ffbd1ee45da036c86b69` | `ea1226986460fdbe2ae7a1f6c653f225ef49f515d519ffbd1ee45da036c86b69` | no |
| `catalog/view/theme/default/template/product/producttabs.twig` | `86419148b5d10e75dd361de26e8e51a717c4db1f38769c1cfe0049bf5b661d2b` | `a2e1d402d9f595bf21a16be73cc381c9c12964588030b1b9deb08253d1b66f6b` | yes |
| `catalog/view/theme/default/template/common/header.twig` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` | no |
| `catalog/controller/product/product.php` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` | no |
| `assets/css/style.css` | `21761371479795f75f98985c551cf3dd0f78abd348672d22409795ab1b68ccde` | `084c402af786bd817c46657d56dcc085cf7706174db3e62dd6638d2a111c83b2` | yes |
| `config.php` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` | no |

**V4 delta summary:**

- **`producttabs.twig`** — operator manual edits + documents final pass: sidebar always visible, compact doc rows, mini-CTA, empty-state branch
- **`style.css`** — operator manual edits + documents final pass CSS: compact `.docs-list` row layout, file-type icons, docs note/empty states
- **Unchanged vs V3:** `catalog/view/theme/default/template/product/producthero.twig`, `catalog/view/theme/default/template/common/header.twig`, `catalog/controller/product/product.php`, `config.php`

## 5. Stable state definition

This checkpoint freezes the **current live TEST storefront** after operator manual edits in `producttabs.twig` and `style.css`, plus the documents final pass:

### Hero / commerce (inherited from V3)

- **Product hero 3-column DOM** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce`
- **SUPER_ATTS working** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks
- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`
- **Primary specs with distinct FA icons** — operator-refined live mapping in `producthero.twig`
- **Right column commerce card** — `product-hero__commerce-card` with header «Стоимость:», price, stock, cart/qty, wishlist/compare
- **Right column service card** — `product-hero__service-card` with «Быстрый заказ» / «Задать вопрос» hooks
- **Cart / qty / wishlist / compare** functional
- **Gallery / Fancybox** functional

### Lower block — product-content (V4 delta vs V3)

- **No tab UI** — Описание / Характеристики / Документы as static sections
- **`product-content__grid--with-side`** — sidebar always rendered
- **Description + specs** in left column (`product-content__main`)
- **Documents sidebar** always visible with `<h2>Документы</h2>`
- **Compact doc row** — `docs-list__file-main`, `docs-list__file-title`, `docs-list__file-type`, `docs-list__download` with `fal fa-download`
- **Mini-CTA** — `product-content__docs-note` with link to `#zpmFbQuestion`
- **Empty state** — `product-content__docs-empty` with «Запросить документы» → `#zpmFbQuestion` when no documents
- **`docs-list` logic preserved** — type class, `href`, `download`, file-type icons
- **Related products + product-help** below content grid

### Prior baselines

Supersedes `SITE-002-STABLE-PDP-V3-2026-06-10` for full PDP rollback including hero, commerce, content layout, and documents final pass.

**Not in this file backup (but part of live FA Pro state):**
`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro vendor bundle only.

## 6. Rollback instructions

Use when future PDP work must be reverted to this PDP V4 checkpoint.

1. **Verify manifest** — confirm SHA256 of local backup files match §3 before upload.
2. **Upload each file** from the backup folder to the matching remote path on FTP (`polygonws.beget.tech`, account root = `public_html`):

   - `catalog/view/theme/default/template/product/producthero.twig` → `catalog/view/theme/default/template/product/producthero.twig`
   - `catalog/view/theme/default/template/product/producttabs.twig` → `catalog/view/theme/default/template/product/producttabs.twig`
   - `catalog/view/theme/default/template/common/header.twig` → `catalog/view/theme/default/template/common/header.twig`
   - `catalog/controller/product/product.php` → `catalog/controller/product/product.php`
   - `assets/css/style.css` → `assets/css/style.css`
   - `config.php` → `config.php`

3. **Clear Twig cache** — delete contents of `system/storage/cache/template/` on FTP.
4. **Verify live PDP (SPKB SKU)** — 3-column hero, SUPER_ATTS, commerce + service cards, distinct FA icons.
5. **Verify commerce** — cart, qty, wishlist, compare functional.
6. **Verify gallery** — Fancybox opens on hero media.
7. **Verify lower block** — white `product-content`, description+specs left, documents sidebar right, no tabs.
8. **Verify documents** — compact doc rows, mini-CTA, `docs-list__link` with type class, `download`, valid `href`.
9. **Verify empty docs branch** — `product-content__docs-empty` CTA when no documents (static twig check if no live SKU).
10. **Verify product-help + related** — visible below content grid.
11. **Verify Font Awesome** — FA Pro CSS loads (HTTP 200) and icons render.

**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.

## 7. QA summary

**Reference URL:** https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850

| Check | Status |
|-------|--------|
| Hero 3-column DOM | PASS |
| SUPER_ATTS | PASS |
| Font Awesome Pro | PASS |
| Primary spec icons (distinct) | PASS |
| Commerce card «Стоимость:» | PASS |
| Service card (right column) | PASS |
| Cart / qty / wishlist / compare | PASS |
| Gallery / Fancybox | PASS |
| product-content layout (no tabs) | PASS |
| Description + specs left column | PASS |
| Documents sidebar always visible | PASS |
| Compact doc row + mini-CTA | PASS |
| docs-list / file-type logic | PASS |
| product-help + related products | PASS |

**Evidence:**

- `documents-final-pass-work/documents-final-pass-qa-result.json`
- `content-layout-fix-work/content-layout-fix-qa-result.json`
- `content-visual-pass-work/content-visual-pass-qa-result.json`
- `content-rebuild-work/content-rebuild-qa-result.json`
- `commerce-card-work/commerce-card-result.json`
- `fa-icon-work/primary-fa-icon-switch-result.json`

## 8. Confirmation

**Stable PDP V4 baseline successfully captured**

*Generated 2026-06-09T19:56:33.279606+00:00 — read-only capture; site unchanged.*
