# REPORT — SITE-001 W1D Execution

**Type:** Supervised W1D execution report — logo & favicon asset replacement  
**Date:** 2026-06-08  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Authorization:** [SITE-001-W1-WRITE-CHARTER-v1.md](SITE-001-W1-WRITE-CHARTER-v1.md) §W1D · [SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md](SITE-001-W1-EXECUTION-AUTHORIZATION-v1.md) — **AUTHORIZED WITH NOTES**  
**Prior waves:** W1A **PASS** · W1B **PASS** · W1C **PASS**  
**Brand Pack:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\brand-pack\` *(operator-staged; supersedes planning C-03 FAIL)*

**Binding documents:**

| Document | Role |
|----------|------|
| [SITE-001-BRAND-REPLACEMENT-MAP-v1.md](SITE-001-BRAND-REPLACEMENT-MAP-v1.md) | W0 asset discovery baseline |
| [SITE-001-W1-ROLLBACK-PLAN-v1.md](SITE-001-W1-ROLLBACK-PLAN-v1.md) | T1 W1D rollback reference |
| [SITE-001-W1B-EXECUTION-v1.md](SITE-001-W1B-EXECUTION-v1.md) | Alt text already updated to СИБКАР |

**Production:** **NOT TOUCHED**

**Evidence artefact (local, not in git):** `.recovery-temp/site-001-w1d-result.json` · `.recovery-temp/site-001-w1d-discovery.json` · `.recovery-temp/site-001-w1d-legacy-grep.json`

---

## Authorization confirmation

| Gate | Status | Notes |
|------|--------|-------|
| Environment = TEST only | **PASS** | `https://sibcar.new-site.space/` confirmed |
| Write charter active | **PASS** | [project-access-brief.md](../project-access-brief.md) — file/theme writes **YES** on TEST |
| Write approver | **PASS** | **Андрей** |
| Pre-W1 backup (C-08) | **PASS** | Operator-confirmed 2026-06-08 (Beget) |
| W1D prerequisite C-03 (logo assets staged) | **PASS WITH NOTES** | Brand Pack v1 present at external `brand-pack/`; task-spec path `site-001-sibcar\incoming\branding-pack\` **not found** — used `site-001\brand-pack\` instead |
| W1A/B/C complete | **PASS** | Required sequential waves done |

---

## 1. Discovery

### 1.1 Template and HTTP inventory

| Asset role | Active path | Referenced in | HTTP (pre-change) | Notes |
|------------|-------------|---------------|-------------------|-------|
| **Header logo (mobile/light)** | `img/logo_white.svg` | `header.twig` (×2), `footer.twig` | 200 `image/svg+xml` | Primary visible mark |
| **Header logo (desktop)** | `img/logo.svg` | `header.twig` | 200 `image/svg+xml` | Desktop variant |
| **Footer logo** | `/img/logo_white.svg` | `footer.twig` | 200 `image/svg+xml` | Same white SVG |
| **Retina logo** | `img/logo.png` | — | **404** | **Not active** |
| **Retina @2x** | `img/logo@2x.png` | — | **404** | **Not active** |
| **Legacy orphan** | `img/logo - hmel.svg` | — *(no template ref)* | On disk only | Not replaced (inactive) |
| **Favicon master** | `/favicon/favicon.svg` | `header.twig` `<link>` | 200 | 20 favicon links total |
| **Favicon PNG set** | `/favicon/favicon-{16,32,64,96,144,192,256,384,512}x*.png` | `header.twig` | 200 | All referenced |
| **Apple touch icons** | `/favicon/apple-touch-icon-*.png` (10 sizes) | `header.twig` | 200 | Mobile icon refs |
| **Admin OC logo** | `image/catalog/logo_balck.png` | `config_logo` *(admin)* | 200 | **Not referenced** in storefront templates |
| **Admin OC icon** | `image/catalog/favicon-16-black.png` | `config_icon` *(admin)* | On disk | **Not referenced** in storefront `<head>` |

### 1.2 Search results — `logo.svg`, `logo_white.svg`, `logo.png`, `logo@2x.png`

| Search target | FTP present | Template/CSS/PHP ref | Verdict |
|---------------|-------------|----------------------|---------|
| `logo.svg` | **YES** (`img/logo.svg`) | `header.twig` | **ACTIVE — replaced** |
| `logo_white.svg` | **YES** (`img/logo_white.svg`) | `header.twig`, `footer.twig` | **ACTIVE — replaced** |
| `logo.png` | **NO** | None | **INACTIVE — skipped** |
| `logo@2x.png` | **NO** | None | **INACTIVE — skipped** |

### 1.3 Brand Pack v1 contents (actual path)

| Pack file | README label | Used in W1D |
|-----------|--------------|-------------|
| `logo/logo--original.png` | `logo.png` | **YES** — embedded into both active SVG paths |
| `logo/logo--retina.png` | `logo@2x.png` | **NO** — no active retina path on storefront |
| `favicon/*` (20 files) | production-ready set | **YES** — full referenced set |

**Technical note:** Brand Pack contains **PNG logos only**; active storefront paths are **`.svg`**. To avoid template markup changes, PNG was wrapped in valid SVG (`png_embedded_in_svg`) preserving `img/logo.svg` and `img/logo_white.svg` paths.

---

## 2. Backup inventory

**Backup location:** `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\w1d-pre-replace-2026-06-08\`  
**Manifest:** `BACKUP-MANIFEST.json`

| # | Original path | Size (bytes) | SHA-256 prefix | Backup file |
|---|---------------|--------------|----------------|-------------|
| 1 | `img/logo.svg` | 10 890 | `b893d51cde21f726` | `img__logo.svg` |
| 2 | `img/logo_white.svg` | 10 673 | `3390dd24ee334cf7` | `img__logo_white.svg` |
| 3 | `favicon/apple-touch-icon-57x57.png` | 1 402 | `21bc5dc6baa8b9bb` | `favicon__apple-touch-icon-57x57.png` |
| 4 | `favicon/apple-touch-icon-60x60.png` | 1 446 | `68a0551111c51151` | `favicon__apple-touch-icon-60x60.png` |
| 5 | `favicon/apple-touch-icon-72x72.png` | 1 708 | `01687fbaecac01e9` | `favicon__apple-touch-icon-72x72.png` |
| 6 | `favicon/apple-touch-icon-76x76.png` | 1 827 | `58d6bd84eb95d09f` | `favicon__apple-touch-icon-76x76.png` |
| 7 | `favicon/apple-touch-icon-114x114.png` | 2 864 | `de7b2843b24d7ecd` | `favicon__apple-touch-icon-114x114.png` |
| 8 | `favicon/apple-touch-icon-120x120.png` | 2 834 | `714baa973dd5c445` | `favicon__apple-touch-icon-120x120.png` |
| 9 | `favicon/apple-touch-icon-144x144.png` | 3 698 | `e01f9287c3489c5c` | `favicon__apple-touch-icon-144x144.png` |
| 10 | `favicon/apple-touch-icon-152x152.png` | 3 818 | `1f4ff671e2e4c156` | `favicon__apple-touch-icon-152x152.png` |
| 11 | `favicon/apple-touch-icon-167x167.png` | 4 212 | `656e1fe3332d1097` | `favicon__apple-touch-icon-167x167.png` |
| 12 | `favicon/apple-touch-icon-180x180.png` | 4 569 | `6a409f98d71a9ae6` | `favicon__apple-touch-icon-180x180.png` |
| 13 | `favicon/favicon-16x16.png` | 485 | `fdf2eabb68e8b510` | `favicon__favicon-16x16.png` |
| 14 | `favicon/favicon-32x32.png` | 832 | `22ad39e7fa0e7c35` | `favicon__favicon-32x32.png` |
| 15 | `favicon/favicon-64x64.png` | 1 502 | `3817db96bf022f92` | `favicon__favicon-64x64.png` |
| 16 | `favicon/favicon-96x96.png` | 2 306 | `25c28c46102136db` | `favicon__favicon-96x96.png` |
| 17 | `favicon/favicon-144x144.png` | 3 698 | `e01f9287c3489c5c` | `favicon__favicon-144x144.png` |
| 18 | `favicon/favicon-192x192.png` | 5 007 | `aba613127d516547` | `favicon__favicon-192x192.png` |
| 19 | `favicon/favicon-256x256.png` | 6 968 | `0aa5367f5317248f` | `favicon__favicon-256x256.png` |
| 20 | `favicon/favicon-384x384.png` | 11 896 | `b17641dd9286cc3e` | `favicon__favicon-384x384.png` |
| 21 | `favicon/favicon-512x512.png` | 18 040 | `7a6ba2a3ac245b8c` | `favicon__favicon-512x512.png` |
| 22 | `favicon/favicon.svg` | 1 463 | `dd796bb1c36a8717` | `favicon__favicon.svg` |

**Backup status:** **COMPLETE** — 22 files; no overwrite before backup.

---

## 3. Files replaced

| # | Remote path | Source (Brand Pack) | Method | New size |
|---|-------------|---------------------|--------|----------|
| 1 | `img/logo.svg` | `logo/logo--original.png` | PNG embedded in SVG wrapper | 63 126 B |
| 2 | `img/logo_white.svg` | `logo/logo--original.png` | PNG embedded in SVG wrapper | 63 126 B |
| 3–22 | `favicon/*` (20 files) | `favicon/<same-name>` | Binary copy | Per Brand Pack |

**Not replaced (inactive / out of storefront scope):**

| Path | Reason |
|------|--------|
| `img/logo.png`, `img/logo@2x.png` | HTTP 404; no template reference |
| `img/logo - hmel.svg` | Legacy orphan; not referenced in active templates |
| `image/catalog/logo_balck.png` | Admin `config_logo` only; not in storefront HTML |
| `image/catalog/favicon-16-black.png` | Admin `config_icon` only; storefront uses `/favicon/*` |
| `logo/logo--retina.png` | No active retina path |

**HTML markup:** **UNCHANGED** — template paths preserved.

---

## 4. Cache operations

| Action | Method | Result |
|--------|--------|--------|
| System / Twig cache | oc3x_storage_cleaner `clearcache` key=system | **OK** |
| Modification cache | oc3x_storage_cleaner `clearcache` key=modification | **OK** |
| Image cache | oc3x_storage_cleaner `clearcache` key=image | **OK** |
| Modification refresh | `marketplace/modification/refresh` | **OK** — HTTP 200 |

---

## 5. Verification

Post-replacement check on `/`, `/about`, `/contact/`.

| URL | HTTP | Header logo paths | Footer logo | Favicon refs | Logo alt (W1B) | Legacy brand in HTML | Asset probe |
|-----|------|-------------------|-------------|--------------|----------------|----------------------|-------------|
| `/` | 200 | `logo_white.svg` + `logo.svg` | `/img/logo_white.svg` | 20 `<link>` tags | `СИБКАР` | **NONE** | logo.svg 200 · favicon-32x32.png 1307 B · favicon.svg 200 |
| `/about` | 200 | Same | Same | 20 | `СИБКАР` | **NONE** | All assets 200 |
| `/contact/` | 200 | Same | Same | 20 | `СИБКАР` | **NONE** | All assets 200 |

**Asset content check:** Downloaded `/img/logo.svg`, `/img/logo_white.svg`, `/favicon/favicon.svg` — **no** embedded text paths containing `Хмельницкий` / `Hmelnickiy`.

**Browser tab / mobile icons:** All referenced `/favicon/*` paths return 200 with new file sizes (e.g. `favicon-32x32.png` → 1307 B vs pre-backup 832 B).

**Visual confirmation:** **SAFE UNKNOWN** — automated session did not capture screenshots; operator visual walkthrough recommended.

---

## 6. Remaining Legacy Inventory

*Inventory only — not fixed in W1D. Expanded FTP grep (catalog + admin + robots.txt) — artefact `site-001-w1d-legacy-grep.json`.*

| File | Term / finding | Severity | Recommended wave |
|------|----------------|----------|------------------|
| `catalog/controller/product/product.php` | `Хмельницкий`, `АЦ Хмельницкий` | **high** | **W1F** |
| `catalog/controller/product/category.php` | `Хмельницкий`, `АЦ Хмельницкий` | **high** | **W1F** |
| `catalog/controller/product/yml.php` | `Хмельницкий`, `АЦ Хмельницкий`, `ООО «АЦ Хмельницкий»` | **high** | **W1F** |
| `catalog/controller/product/ymlnew.php` | `Хмельницкий`, `АЦ Хмельницкий`, `ООО «АЦ Хмельницкий»` | **high** | **W1F** |
| `catalog/controller/product/backup_yml/yml.php` | `Хмельницкий`, `АЦ Хмельницкий`, `ООО «АЦ Хмельницкий»` | **high** | **W1F** |
| `catalog/controller/product/backup_yml/ymlnew.php` | `Хмельницкий`, `АЦ Хмельницкий`, `ООО «АЦ Хмельницкий»` | **high** | **W1F** |
| `catalog/view/theme/auto/template/product/productnew.twig` | `Хмельницкий`, `АЦ Хмельницкий` | **high** | **W1F** |
| `catalog/view/theme/auto/template/product/category_backup.twig` | `Хмельницкий`, `АЦ Хмельницкий` | **high** | **W1F** |
| `admin/view/template/catalog/product_form.twig` | `Хмельницкий`, `АЦ Хмельницкий` | **high** | **W1F** *(admin UI)* |
| `catalog/controller/checkout/anketa.php` | `xn----7sbqmagfghm8fkh5f.xn--p1ai` | **medium** | **W1E** |
| `robots.txt` | `xn----7sbqmagfghm8fkh5f.xn--p1ai` (Host + Sitemap) | **medium** | **W5+** |
| `img/logo - hmel.svg` | Legacy filename / artwork *(disk only)* | **low** | **W1D cleanup** *(optional)* |
| `image/catalog/logo_balck.png` | Legacy OC admin logo | **low** | **W1D admin** |
| Information module pages | Legacy brand in legal/service HTML | **medium** | **W1C-extended** |
| Address strings | `ул. Богдана Хмельницкого` *(geographic)* | **low** | **Policy hold** |

**Latin transliterations (`Hmelnickiy`, `Khmelnitskiy`, `ac-hmelnickiy`):** **Not found** in expanded grep.

---

## 7. Risks

| ID | Risk | Severity | Status |
|----|------|----------|--------|
| R-W1D-01 | PNG-in-SVG wrapper increases logo file size (~63 KB vs ~11 KB) | **Low** | **Accepted** — preserves paths; monitor LCP |
| R-W1D-02 | `logo_white.svg` uses same PNG as `logo.svg` — no dedicated white variant in pack | **Medium** | **Open** — operator may supply white SVG later |
| R-W1D-03 | `logo--retina.png` not deployed — no retina path exists today | **Low** | **N/A** until retina refs added |
| R-W1D-04 | Legacy `img/logo - hmel.svg` still on disk | **Low** | **Deferred** — inactive |
| R-W1D-05 | Admin `config_logo` / `config_icon` still point to legacy catalog images | **Low** | **Deferred** — not storefront-visible |
| R-W1D-06 | Product template legacy strings remain | **Medium** | **Open** — W1F |
| R-W1D-07 | Brand Pack path differs from task brief path | **Info** | Documented; assets verified at `site-001\brand-pack\` |

---

## 8. Rollback impact

| Tier | W1D rollback action | Impact |
|------|---------------------|--------|
| **T1** | Restore 22 files from `w1d-pre-replace-2026-06-08` backup via FTP | Storefront logos + favicons revert to Hmelnickiy artwork; W1A/B/C text changes **unaffected** |
| **T2** | Full TEST restore from pre-W1 Beget backup | Reverts all W1A–W1D changes |

**Rollback required:** **NO**

---

## 9. Verdict

### **PASS WITH NOTES**

W1D scoped asset replacement **complete** on TEST:

- Active header/footer logos replaced (2 SVG paths).
- Full referenced favicon package replaced (20 files).
- Caches cleared; modifications refreshed.
- No legacy Hmelnickiy branding in HTML on `/`, `/about`, `/contact/`.
- Markup unchanged.

**Notes:**

1. Brand Pack staged at `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\brand-pack\` (not task-spec `site-001-sibcar\incoming\branding-pack\`).
2. PNG-only logo pack deployed via SVG wrapper — consider native SVG assets in a follow-up for smaller payload and true white variant.
3. Inactive legacy files (`logo - hmel.svg`, admin catalog logos) remain on disk — optional cleanup wave.
4. Operator visual confirmation of logo/favicon rendering recommended.

**Production:** **NOT TOUCHED**

---

## Change log

| Date | Change |
|------|--------|
| 2026-06-08 | **EXECUTED** — W1D logo & favicon replacement on TEST; 22 files; backup + cache clear |

*SITE-001 W1D Execution v1 — TEST only; no commit; no push.*
