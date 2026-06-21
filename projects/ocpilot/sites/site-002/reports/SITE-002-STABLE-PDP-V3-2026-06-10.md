# REPORT — SITE-002 STABLE PDP V3 BASELINE

**Baseline name:** `SITE-002-STABLE-PDP-V3-2026-06-10`
**Site:** SITE-002 (ЗПМ TEST)
**Environment:** https://zpm.new-site.space/
**Captured at (UTC):** 2026-06-09T18:55:55.323352+00:00
**Mode:** Read-only — no FTP writes, no deploy, no rollback performed

---

## 1. Backup folder

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10`

## 2. Included files

| Remote path | Local copy | Size (bytes) |
|-------------|------------|--------------|
| `catalog/view/theme/default/template/product/producthero.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10\catalog\view\theme\default\template\product\producthero.twig` | 12067 |
| `catalog/view/theme/default/template/product/producttabs.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10\catalog\view\theme\default\template\product\producttabs.twig` | 3335 |
| `catalog/view/theme/default/template/common/header.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10\catalog\view\theme\default\template\common\header.twig` | 14322 |
| `catalog/controller/product/product.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10\catalog\controller\product\product.php` | 30560 |
| `assets/css/style.css` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10\assets\css\style.css` | 262069 |
| `config.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10\config.php` | 1907 |

**Manifest:** `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v3-2026-06-10\stable-pdp-v3-manifest.json`

## 3. SHA256 summary

| File | SHA256 |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | `ea1226986460fdbe2ae7a1f6c653f225ef49f515d519ffbd1ee45da036c86b69` |
| `catalog/view/theme/default/template/product/producttabs.twig` | `86419148b5d10e75dd361de26e8e51a717c4db1f38769c1cfe0049bf5b661d2b` |
| `catalog/view/theme/default/template/common/header.twig` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` |
| `catalog/controller/product/product.php` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` |
| `assets/css/style.css` | `21761371479795f75f98985c551cf3dd0f78abd348672d22409795ab1b68ccde` |
| `config.php` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` |

## 4. Stable state definition

This checkpoint freezes the **current live TEST storefront** after operator manual edits and PDP lower-block work (content rebuild, visual structure pass, layout fix):

### Hero / commerce (from PDP V2, unchanged scope)

- **Product hero 3-column DOM** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce` as direct grid children
- **SUPER_ATTS working** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks
- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`
- **Primary specs with distinct FA icons** — operator-refined live mapping in `producthero.twig`
- **Right column commerce card** — `product-hero__commerce-card` with header «Стоимость:», price, stock, cart/qty, wishlist/compare
- **Right column service card** — `product-hero__service-card` with «Быстрый заказ» / «Задать вопрос» hooks
- **Cart / qty / wishlist / compare** functional
- **Gallery / Fancybox** functional

### Lower block — product-content layout (V3 delta vs V2)

- **No tab UI** — Описание / Характеристики / Документы rendered as static sections (not JS tabs)
- **`product-content__grid`** — desktop 7fr/3fr when documents present (`--with-side`)
- **`product-content__main`** — left column: description (if present) + specifications
- **`product-content__side`** — right sidebar: documents with horizontal doc cards
- **White section background** on `.product-content`; light background only on `.product-help`
- **`docs-list` logic preserved** — `docs-list__link`, type class (`pdf`, `word`, …), `download`, `href`, file icons
- **Related products + product-help** visible below content grid

### Prior baselines

Supersedes `SITE-002-STABLE-PDP-V2-2026-06-09` for full PDP rollback including hero, commerce, and lower content layout.

**Not in this file backup (but part of live FA Pro state):**
`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro vendor bundle only.

## 5. Rollback instructions

Use when future PDP work must be reverted to this PDP V3 checkpoint.

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
8. **Verify documents** — `docs-list__link pdf` with `download` and valid `href`.
9. **Verify product-help + related** — visible below content grid.
10. **Verify Font Awesome** — FA Pro CSS loads (HTTP 200) and icons render.

**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.

## 6. QA summary

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
| Documents right sidebar | PASS |
| docs-list / file-type logic | PASS |
| product-help + related products | PASS |

**Delta vs `SITE-002-STABLE-PDP-V2-2026-06-09` (SHA256):**

| File | V2 SHA256 | V3 SHA256 | Changed |
|------|-----------|-----------|---------|
| `catalog/view/theme/default/template/product/producthero.twig` | `a6624a9fd9597ffce4d85cf89ad6c0bd3dbde0f4672e7d1d68ba55635fc510c0` | `ea1226986460fdbe2ae7a1f6c653f225ef49f515d519ffbd1ee45da036c86b69` | yes |
| `catalog/view/theme/default/template/product/producttabs.twig` | `4cfcec354486e6c8d9f8322bc0e071b465b1fda42c618f835a84e80171586110` | `86419148b5d10e75dd361de26e8e51a717c4db1f38769c1cfe0049bf5b661d2b` | yes |
| `catalog/view/theme/default/template/common/header.twig` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` | no |
| `catalog/controller/product/product.php` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` | no |
| `assets/css/style.css` | `6a985fda511934c9a4f9761a99f841c7a759c5abe33cba72a4c5453fe3a24c61` | `21761371479795f75f98985c551cf3dd0f78abd348672d22409795ab1b68ccde` | yes |
| `config.php` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` | no |

**Evidence:**

- `content-layout-fix-work/content-layout-fix-qa-result.json`
- `content-visual-pass-work/content-visual-pass-qa-result.json`
- `content-rebuild-work/content-rebuild-qa-result.json`
- `commerce-card-work/commerce-card-result.json`
- `fa-icon-work/primary-fa-icon-switch-result.json`

## 7. Confirmation

**Stable PDP V3 baseline successfully captured**

*Generated 2026-06-09T18:55:55.323352+00:00 — read-only capture; site unchanged.*
