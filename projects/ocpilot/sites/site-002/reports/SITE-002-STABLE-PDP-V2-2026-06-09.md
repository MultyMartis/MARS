# REPORT — SITE-002 STABLE PDP V2 BASELINE

**Baseline name:** `SITE-002-STABLE-PDP-V2-2026-06-09`
**Site:** SITE-002 (ЗПМ TEST)
**Environment:** https://zpm.new-site.space/
**Captured at (UTC):** 2026-06-09T09:18:19.079377+00:00
**Mode:** Read-only — no FTP writes, no deploy, no rollback performed

---

## 1. Backup folder

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09`

## 2. Included files

| Remote path | Local copy | Size (bytes) |
|-------------|------------|--------------|
| `catalog/view/theme/default/template/product/producthero.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09\catalog\view\theme\default\template\product\producthero.twig` | 12030 |
| `catalog/view/theme/default/template/product/producttabs.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09\catalog\view\theme\default\template\product\producttabs.twig` | 3305 |
| `catalog/view/theme/default/template/common/header.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09\catalog\view\theme\default\template\common\header.twig` | 14322 |
| `catalog/controller/product/product.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09\catalog\controller\product\product.php` | 30560 |
| `assets/css/style.css` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09\assets\css\style.css` | 257141 |
| `config.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09\config.php` | 1907 |

**Manifest:** `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-pdp-v2-2026-06-09\stable-pdp-v2-manifest.json`

## 3. SHA256 summary

| File | SHA256 |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | `a6624a9fd9597ffce4d85cf89ad6c0bd3dbde0f4672e7d1d68ba55635fc510c0` |
| `catalog/view/theme/default/template/product/producttabs.twig` | `4cfcec354486e6c8d9f8322bc0e071b465b1fda42c618f835a84e80171586110` |
| `catalog/view/theme/default/template/common/header.twig` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` |
| `catalog/controller/product/product.php` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` |
| `assets/css/style.css` | `6a985fda511934c9a4f9761a99f841c7a759c5abe33cba72a4c5453fe3a24c61` |
| `config.php` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` |

## 4. Stable state definition

This checkpoint freezes the **current live TEST storefront** before work on the lower block «Описание / Характеристики / Документы»:

- **Product hero 3-column DOM** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce` as direct grid children
- **SUPER_ATTS working** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks
- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`
- **Primary specs with distinct FA icons (captured from live `producthero.twig`):**
  - Длина → `fad fa-arrows-alt-h`
  - Ширина → `fad fa-arrows-alt-v`
  - Высота → `fad fa-arrow-to-top`
  - Масса → `far fa-weight-hanging`
- **Right column commerce card** — `product-hero__commerce-card` with header «Стоимость:», price, stock, cart/qty, wishlist/compare
- **Right column service card** — `product-hero__service-card` with «Быстрый заказ» / «Задать вопрос» hooks
- **Operator manual edits** in live `producthero.twig` and `style.css`
- **Cart / qty / wishlist / compare** functional
- **Gallery / Fancybox** functional
- **`producttabs.twig`** — current live lower tabs template (baseline for upcoming tab-block work)

### Prior baselines

Supersedes hero/commerce slice of `SITE-002-STABLE-HERO-FA-ICONS-2026-06-09` and `SITE-002-STABLE-PDP-BASELINE-2026-06-09` for full PDP V2 rollback including commerce card and `producttabs.twig`.

**Not in this file backup (but part of live FA Pro state):**
`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro vendor bundle only.

## 5. Rollback instructions

Use when future PDP work (including lower tabs) must be reverted to this PDP V2 checkpoint.

1. **Verify manifest** — confirm SHA256 of local backup files match §3 before upload.
2. **Upload each file** from the backup folder to the matching remote path on FTP (`polygonws.beget.tech`, account root = `public_html`):

   - `catalog/view/theme/default/template/product/producthero.twig` → `catalog/view/theme/default/template/product/producthero.twig`
   - `catalog/view/theme/default/template/product/producttabs.twig` → `catalog/view/theme/default/template/product/producttabs.twig`
   - `catalog/view/theme/default/template/common/header.twig` → `catalog/view/theme/default/template/common/header.twig`
   - `catalog/controller/product/product.php` → `catalog/controller/product/product.php`
   - `assets/css/style.css` → `assets/css/style.css`
   - `config.php` → `config.php`

3. **Clear Twig cache** — delete contents of `system/storage/cache/template/` on FTP.
4. **Verify live PDP** — SPKB SKU: 3-column hero, SUPER_ATTS, commerce + service cards, distinct FA icons.
5. **Verify commerce** — cart, qty, wishlist, compare functional.
6. **Verify gallery** — Fancybox opens on hero media.
7. **Verify lower tabs** — Описание / Характеристики / Документы render from restored `producttabs.twig`.
8. **Verify Font Awesome** — FA Pro CSS loads (HTTP 200) and icons render.

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
| producttabs.twig baseline captured | PASS |

**Primary spec icon mapping (captured from live `producthero.twig`):**

| Attribute | Icon class |
|-----------|------------|
| Длина | `fad fa-arrows-alt-h` |
| Ширина | `fad fa-arrows-alt-v` |
| Высота | `fad fa-arrow-to-top` |
| Масса | `far fa-weight-hanging` |

**Delta vs `SITE-002-STABLE-HERO-FA-ICONS-2026-06-09`:**

| File | Prior | Current | Delta |
|------|-------|---------|-------|
| `producthero.twig` | 9734 B | 12030 B | +2296 B (commerce + service cards) |
| `style.css` | 254448 B | 257141 B | +2693 B (commerce card styles) |
| `producttabs.twig` | — | 3305 B | **new in baseline** |
| `header.twig`, `product.php`, `config.php` | unchanged SHA256 | — | — |

**Evidence:**

- `commerce-card-work/commerce-card-result.json`
- `fa-icon-work/primary-fa-icon-switch-result.json`
- `reports/SITE-002-PRODUCT-HERO-COMMERCE-CARD.md`

## 7. Confirmation

**Stable PDP V2 baseline successfully captured**

*Generated 2026-06-09T09:18:19.079377+00:00 — read-only capture; site unchanged.*
