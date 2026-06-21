# REPORT — SITE-002 STABLE CATEGORY V2 PRE-VIEW-SWITCHER BASELINE

**Baseline name:** `SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER`
**Site:** SITE-002 (ЗПМ TEST)
**Environment:** https://zpm.new-site.space/
**Captured at (UTC):** 2026-06-09T20:54:41.463205+00:00
**Mode:** Read-only — no FTP writes, no deploy

---

## 1. Backup folder

`C:\AI MARS\projects\ocpilot\sites\site-002\backups\SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER`

## 2. Included files

| Local name | Remote path | Size (bytes) |
|------------|-------------|--------------|
| `category.twig` | `catalog/view/theme/default/template/product/category.twig` | 3245 |
| `style.css` | `assets/css/style.css` | 268329 |
| `main.js` | `assets/js/main.js` | 181055 |

**Manifest:** `C:\AI MARS\projects\ocpilot\sites\site-002\backups\SITE-002-STABLE-CATEGORY-V2-PRE-VIEW-SWITCHER\stable-category-v2-pre-view-switcher-manifest.json`

## 3. SHA256 summary

| File | SHA256 |
|------|--------|
| `category.twig` | `49bb0e98efee49b0ee91aa35a972afee5ab912dc34cd4dbb01e6e676b317235c` |
| `style.css` | `9ae7ac39174394fee130a177c09179bd00df9eb47fe099bda5267922e27d95a1` |
| `main.js` | `548c3a3e94d400c52a525ca76bca92a453789bd8a3ca97b1ffc82b2ed1eeb19f` |

## 4. Rollback instructions

Use when CATEGORY V2 view switcher work must be reverted to pre-pass state.

1. Verify SHA256 of backup files match §3.
2. Upload each file from backup folder to matching remote path on FTP (`polygonws.beget.tech`):

   - `category.twig` → `catalog/view/theme/default/template/product/category.twig`
   - `style.css` → `assets/css/style.css`
   - `main.js` → `assets/js/main.js`

3. Clear Twig cache — delete contents of `system/storage/cache/template/`.
4. Verify category PLP — grid layout unchanged, no view switcher in topbar.
5. Verify PDP V4 — hero, commerce, documents sidebar unchanged.

## 5. Confirmation

**Stable CATEGORY V2 pre-view-switcher baseline successfully captured**

*Generated 2026-06-09T20:54:41.463205+00:00 — read-only capture; site unchanged.*
