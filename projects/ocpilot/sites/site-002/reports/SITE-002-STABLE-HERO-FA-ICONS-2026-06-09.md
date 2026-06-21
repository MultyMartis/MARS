# REPORT — SITE-002 STABLE HERO FA ICONS BASELINE

**Baseline name:** `SITE-002-STABLE-HERO-FA-ICONS-2026-06-09`
**Site:** SITE-002 (ЗПМ TEST)
**Environment:** https://zpm.new-site.space/
**Captured at (UTC):** 2026-06-09T08:00:35.433771+00:00
**Mode:** Read-only — no FTP writes, no deploy, no rollback performed

---

## 1. Backup folder

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-hero-fa-icons-2026-06-09`

## 2. Included files

| Remote path | Local copy | Size (bytes) |
|-------------|------------|--------------|
| `catalog/view/theme/default/template/product/producthero.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-hero-fa-icons-2026-06-09\catalog\view\theme\default\template\product\producthero.twig` | 9734 |
| `assets/css/style.css` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-hero-fa-icons-2026-06-09\assets\css\style.css` | 254448 |
| `catalog/controller/product/product.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-hero-fa-icons-2026-06-09\catalog\controller\product\product.php` | 30560 |
| `catalog/view/theme/default/template/common/header.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-hero-fa-icons-2026-06-09\catalog\view\theme\default\template\common\header.twig` | 14322 |
| `config.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-hero-fa-icons-2026-06-09\config.php` | 1907 |

**Manifest:** `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-hero-fa-icons-2026-06-09\stable-hero-fa-icons-manifest.json`

## 3. SHA256 summary

| File | SHA256 |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | `e4c05f4937a3eda76b93b672384d65314d887367db0108750c2202f97186827e` |
| `assets/css/style.css` | `029e0d3500269542f6230954c54addf7bdb4974666e3f5c9d38d0864fbb622aa` |
| `catalog/controller/product/product.php` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` |
| `catalog/view/theme/default/template/common/header.twig` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` |
| `config.php` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` |

## 4. Stable state definition

This checkpoint freezes the **current live TEST storefront** after operator manual edits and successful primary-spec FA icon switch:

- **Product hero 3-column DOM** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce` as direct grid children
- **SUPER_ATTS working** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks
- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`
- **Primary specs with distinct FA icons (operator-refined live mapping):**
  - Длина → `fad fa-arrows-alt-h`
  - Ширина → `fad fa-arrows-alt-v`
  - Высота → `fad fa-arrow-to-top`
  - Масса → `far fa-weight-hanging`
- **Operator manual edits** in live `producthero.twig` and `style.css`
- **Commerce block intact** — cart, qty, wishlist, compare
- **Gallery / Fancybox intact**

### Prior baseline superseded for hero FA state

Replaces hero/icon slice of `SITE-002-STABLE-PDP-BASELINE-2026-06-09` for post-FA-icon-switch rollback. Prior baseline remains valid for pre-icon-switch restore.

**Not in this file backup (but part of live FA Pro state):**
`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro vendor bundle only.

## 5. Rollback instructions

Use when future PDP work must be reverted to this FA-icons-stable checkpoint.

1. **Verify manifest** — confirm SHA256 of local backup files match §3 before upload.
2. **Upload each file** from the backup folder to the matching remote path on FTP (`polygonws.beget.tech`, account root = `public_html`):

   - `catalog/view/theme/default/template/product/producthero.twig` → `catalog/view/theme/default/template/product/producthero.twig`
   - `assets/css/style.css` → `assets/css/style.css`
   - `catalog/controller/product/product.php` → `catalog/controller/product/product.php`
   - `catalog/view/theme/default/template/common/header.twig` → `catalog/view/theme/default/template/common/header.twig`
   - `config.php` → `config.php`

3. **Clear Twig cache** — delete contents of `system/storage/cache/template/` on FTP.
4. **Verify live PDP** — SPKB SKU hero: 3 columns, SUPER_ATTS visible, distinct FA icons per primary spec.
5. **Verify commerce** — cart, qty, wishlist, compare functional.
6. **Verify gallery** — Fancybox opens on hero media.
7. **Verify Font Awesome** — FA Pro CSS loads (HTTP 200) and icons render.

**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.

## 6. QA summary

**Reference URL:** https://zpm.new-site.space/katalog/nejtralnoe-oborudovanie/stoly/stoly-tumby-serii-premium/stoly-tumby-s-odnoy-celnotyanutoy-vannoy/stol-tumba-spkb-18-7-vl5-1800h700h850

| Check | Status |
|-------|--------|
| Hero 3-column DOM | PASS (prior waves + operator edits) |
| SUPER_ATTS | PASS |
| Font Awesome Pro | PASS |
| Primary spec icons (4 distinct) | PASS |
| Cart / qty / wishlist / compare | PASS |
| Gallery / Fancybox | PASS |

**Primary spec icon mapping (captured from live `producthero.twig`):**

| Attribute | Icon class |
|-----------|------------|
| Длина | `fad fa-arrows-alt-h` |
| Ширина | `fad fa-arrows-alt-v` |
| Высота | `fad fa-arrow-to-top` |
| Масса | `far fa-weight-hanging` |

**Delta vs prior stable PDP baseline:** `producthero.twig` +607 bytes (9734 vs 9127); `style.css` +326 bytes (254448 vs 254122) — operator manual edits post FA-icon switch.

**Prior deploy evidence:** `fa-icon-work/primary-fa-icon-switch-result.json` (pre-operator icon refinement)

Screenshots: `qa/primary-fa-icon-switch/spkb-18-7-vl5-hero-desktop.png`, `spkb-18-7-vl5-hero-mobile.png`

## 7. Confirmation

**Stable hero FA icons baseline successfully captured**

*Generated 2026-06-09T08:00:35.433771+00:00 — read-only capture; site unchanged.*
