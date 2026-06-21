# REPORT — SITE-002 STABLE PDP BASELINE

**Baseline name:** `SITE-002-STABLE-PDP-BASELINE-2026-06-09`
**Site:** SITE-002 (ЗПМ TEST)
**Environment:** https://zpm.new-site.space/
**Captured at (UTC):** 2026-06-09T07:28:41.017726+00:00
**Mode:** Read-only — no FTP writes, no deploy, no rollback performed

---

## 1. Backup folder

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baseline-2026-06-09`

## 2. Manifest path

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baseline-2026-06-09\stable-baseline-manifest.json`

## 3. Included files

| Remote path | Local copy | Size (bytes) |
|-------------|------------|--------------|
| `catalog/view/theme/default/template/product/producthero.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baseline-2026-06-09\catalog\view\theme\default\template\product\producthero.twig` | 9127 |
| `assets/css/style.css` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baseline-2026-06-09\assets\css\style.css` | 254122 |
| `catalog/controller/product/product.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baseline-2026-06-09\catalog\controller\product\product.php` | 30560 |
| `catalog/view/theme/default/template/common/header.twig` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baseline-2026-06-09\catalog\view\theme\default\template\common\header.twig` | 14322 |
| `config.php` | `C:\AI MARS\projects\ocpilot\sites\site-002\backups\stable-baseline-2026-06-09\config.php` | 1907 |

## 4. SHA256 summary

| File | SHA256 |
|------|--------|
| `catalog/view/theme/default/template/product/producthero.twig` | `92e74fd92329bd5451b6985820d5e60bce4b2233f9f3d549bb1f4edf9de840e9` |
| `assets/css/style.css` | `0a6e8d4e2035ba12a2095966213a6d5669260203a806efd62ab00c876c405ef6` |
| `catalog/controller/product/product.php` | `bc990f2a8dc0a27b565d903a081f361b58e5c7207b3f62ab5e7dc596f11e7f27` |
| `catalog/view/theme/default/template/common/header.twig` | `08b4de7cba99485a56457bb7c5452b8cb2a6dbf627997318377b02e0139d896b` |
| `config.php` | `d7c23de76416c4a837fd862dec532768d8f1bd7799b306fb68c686616e4d3626` |

## 5. Working state captured in this baseline

This checkpoint freezes the **current live TEST storefront** after operator-approved PDP work:

- **Hero 3-column DOM structure** — `product-hero__col--media`, `product-hero__col--info`, `product-hero__col--commerce` as direct grid children
- **Working SUPER_ATTS** — controller exposes `$data['super_atts']`; hero renders primary/additional spec blocks
- **Font Awesome Pro 5.15.4** — `header.twig` links `/assets/vendor/fontawesome-pro-5.15.4/css/all.min.css`
- **Operator manual edits** — all current live content in the five backed-up files
- **Current `producthero.twig` and `style.css`** — post hero-3col baseline rollback state

### Changes included in baseline (chronology)

| Work stream | Scope | Evidence |
|-------------|-------|----------|
| Wave 1A / 1A.2 | PDP hero rebuild, scroll sections | `reports/SITE-002-WAVE-1A-*` |
| Wave 1B / 1B.2 | Hero attributes, compactness | `reports/SITE-002-WAVE-1B*` |
| SUPER_ATTS fix | `product.php` + hero presentation | `superatts-work/` |
| Hero 3-column DOM fix | Twig + CSS grid columns | `hero-3col-work/hero-3col-dom-fix-*` |
| Hero 3-col baseline rollback | Reverted quick-props / post-change experiments | `hero-3col-work/hero-3col-baseline-rollback-result.json` |
| Font Awesome Pro install | Vendor bundle + `header.twig` | `fa-pro-work/fa-pro-install-result.json` |

**Not in this file backup (but part of live FA Pro state):**
`assets/vendor/fontawesome-pro-5.15.4/**` — installed on server; restore separately if rolling back FA Pro only.

## 6. Full rollback procedure

Use when future PDP work must be reverted to this checkpoint.

1. **Verify manifest** — confirm SHA256 of local backup files match §4 before upload.
2. **Upload each file** from the backup folder to the matching remote path on FTP (`polygonws.beget.tech`, account root = `public_html`):

   - `catalog/view/theme/default/template/product/producthero.twig` → `catalog/view/theme/default/template/product/producthero.twig`
   - `assets/css/style.css` → `assets/css/style.css`
   - `catalog/controller/product/product.php` → `catalog/controller/product/product.php`
   - `catalog/view/theme/default/template/common/header.twig` → `catalog/view/theme/default/template/common/header.twig`
   - `config.php` → `config.php`

3. **Clear Twig cache** — delete contents of `system/storage/cache/template/` on FTP.
4. **Verify live PDP** — e.g. SPKB SKU hero: 3 columns, SUPER_ATTS visible, cart/wishlist/compare OK.
5. **Verify Font Awesome** — home/catalog/PDP pages load FA Pro CSS (HTTP 200) and icons render.

**Security note:** `config.php` contains DB credentials — treat backup copies as sensitive; do not commit to public repos.

## 7. Confirmation

**Stable baseline successfully captured**

*Generated 2026-06-09T07:28:41.017726+00:00 — read-only capture; site unchanged.*
