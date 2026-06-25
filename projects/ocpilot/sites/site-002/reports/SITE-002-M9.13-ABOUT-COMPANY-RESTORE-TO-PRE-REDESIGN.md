# REPORT — M9.13 ABOUT COMPANY RESTORE TO PRE-REDESIGN

**Project:** SITE-002 (BZPM / ЗПМ)  
**URL (TEST):** https://zpm.new-site.space/about  
**Authority:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`  
**Mode:** RESTORE ONLY (operator rejected M9.13 redesign/polish)  
**Date:** 2026-06-23  
**Commit:** NO · **Push:** NO

---

## 1. Restore source

| Tier | Source | Used |
|------|--------|------|
| **Primary** | Point rollback `backups/*.pre-m9.13-about-redesign.bak` | ✓ |
| **Image fallback** | `backups/about-page-img.jpg.pre-m9.13-about-polish-v1.bak` | ✓ (see note) |
| **Beget full backup** | Not used | — |

**Restore script:** `reports/m9.13-restore-work/m913-about-restore-to-pre-redesign.py`  
**Manifest:** `reports/m9.13-restore-work/restore-manifest.json`

### Note — `about-page-img.jpg`

Expected file `about-page-img.jpg.pre-m9.13-about-redesign.bak` **does not exist** — M9.13 redesign did not replace the image file (only referenced it in Twig). The polish pass later replaced the hero JPEG. Restored from `about-page-img.jpg.pre-m9.13-about-polish-v1.bak`, which captures the **same bytes** that were on live immediately before redesign (276 765 bytes, SHA256 below).

---

## 2. Files restored

| Remote path | Backup source | Post-restore SHA256 | Bytes |
|-------------|---------------|---------------------|-------|
| `catalog/view/theme/default/template/information/about.twig` | `backups/about.twig.pre-m9.13-about-redesign.bak` | `998321d3b3ea0a119b0aa688d9c6ebbcdc31431ced75110450026d24458202f8` | 3443 |
| `catalog/controller/information/about.php` | `backups/about.php.pre-m9.13-about-redesign.bak` | `77ac5ea35be5863f5c729c996743a8f8cd18af3e9afca328d4dcde7585b5fa8a` | 1687 |
| `assets/css/style.css` | `backups/style.css.pre-m9.13-about-redesign.bak` | `6f91745218bfd7a455ebd3c23a28745d3c6ee60e8a26814c0ee5efc4723249cd` | 299 779 |
| `assets/img/about-page-img.jpg` | `backups/about-page-img.jpg.pre-m9.13-about-polish-v1.bak` *(fallback)* | `138d682e4e3b0acc214c9ac24d31fe1c5110653809da9f6c35028966293230e3` | 276 765 |

**Pre-restore live capture** (M9.13 redesign + polish state): `reports/m9.13-restore-work/pre-restore-capture/`

| File | Pre-restore SHA256 |
|------|-------------------|
| `about.twig` | `2e1fdf5d3fda58f7eb0a4c42a40de6d4f26d904cc0a7b7829a758ada2a1b8dfc` |
| `about.php` | `e598e6eba95d7b864b01e1f6ee0cddfeacf3e5705f20b541a33ac3c3df62e29f` |
| `style.css` | `fbf5aaadf69b20c8d8d2bba91770158d0a8588a077f512dc61f6cc73d8a7e251` |
| `about-page-img.jpg` | `9732ce40aed0ba90d3cba7872b8bde0dba00d651ab4dd4050614e4ed158ddfe6` |
| `about-logistics.jpg` | `b97dcfaa20f61a8bc583efcc558d8bf74003bd216bb90be0121cb800e728bfc6` |

---

## 3. Files removed

| Remote path | Action | Reason |
|-------------|--------|--------|
| `assets/img/about-logistics.jpg` | **Deleted** from live FTP | Introduced by M9.13 polish only; not referenced in pre-redesign page |

Pre-delete capture: `reports/m9.13-restore-work/pre-restore-capture/about-logistics.jpg`

---

## 4. SHA verification

Cross-check against M9.13 redesign deploy manifest (`reports/m9.13-work/deploy-manifest.json` **pre_sha256** values):

| File | Redesign pre-deploy SHA | Restored SHA | Match |
|------|-------------------------|--------------|-------|
| `about.twig` | `998321d3…02f8` | `998321d3…02f8` | ✓ |
| `about.php` | `77ac5ea3…5fa8a` | `77ac5ea3…5fa8a` | ✓ |
| `style.css` | `6f917452…249cd` | `6f917452…249cd` | ✓ |

Twig cache clear attempted (`system/storage/cache/template/`); FTP listing returned empty (no stale entries or no list permission).

---

## 5. QA results

### Automated HTML (post-restore)

| Check | Result |
|-------|--------|
| HTTP 200 | ✓ |
| Old structure: `about-page--main-wrap` | ✓ |
| Old video block: `about-page-video` | ✓ |
| Old geo image: `geo-web.png` | ✓ |
| Old partials: cert slider / dealer form refs | ✓ |
| No `zpm-about-hero` | ✓ |
| No `zpm-about-company` | ✓ |
| No `zpm-about-advantages` | ✓ |
| No `zpm-about-certs` | ✓ |
| No `zpm-about-geo` | ✓ |
| No `zpm-about-cta` | ✓ |
| No `about-logistics.jpg` in HTML | ✓ |
| **all_pass** | ✓ |

**Post-restore HTML capture:** `reports/m9.13-restore-work/qa-about-restored.html`

### Playwright (desktop 1440 + mobile 390)

| Check | Result |
|-------|--------|
| HTTP status | 200 / 200 |
| Console errors | **0** |
| Horizontal overflow | none (sw ≤ cw) |
| Breadcrumbs present | ✓ |
| Header present (`zpm-header` / global chrome) | ✓ |
| Footer present (`zpm-footer`) | ✓ |
| Old video block visible | ✓ |
| No M9.13 hero namespace | ✓ |

**QA JSON:** `qa/m9.13-about-restore-screenshots/restore-qa-results.json`

### Scope compliance (untouched)

Catalog, PDP, filters, contacts, Commercial Trust block, header, footer, breadcrumbs, 1C/import, product files, global settings — **not modified** in this pass (About route files + one polish-only image only).

---

## 6. Screenshots

| Viewport | File |
|----------|------|
| Desktop 1440 full | `qa/m9.13-about-restore-screenshots/desktop-1440-full.png` |
| Mobile 390 full | `qa/m9.13-about-restore-screenshots/mobile-390-full.png` |

---

## 7. Rollback notes

| Direction | Action |
|-----------|--------|
| **Re-apply M9.13 redesign** | Deploy from `reports/m9.13-work/` via `m913-about-deploy.py` |
| **Re-apply polish only** | Deploy from `reports/m9.13-polish-work/` via `m913-about-polish-deploy.py` |
| **Re-restore pre-redesign** | Re-run `reports/m9.13-restore-work/m913-about-restore-to-pre-redesign.py` |

Pre-restore M9.13 state preserved locally in `reports/m9.13-restore-work/pre-restore-capture/` (not re-deployed).

**UNKNOWN:** Twig cache clear returned empty file list — if stale render appears, operator manual clear on Beget may be required.

---

## 8. Git status

No commit. No push.

Untracked artifacts from this restore pass:

- `reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md` *(this report)*
- `reports/m9.13-restore-work/` *(script, manifest, pre-restore capture, QA HTML)*
- `qa/m9.13-about-restore-screenshots/` *(screenshots + QA JSON)*

Prior M9.13 work dirs remain untracked from earlier passes (`m9.13-work/`, `m9.13-polish-work/`, related reports/backups).

---

**Outcome:** Live TEST `/about` restored to pre-M9.13 redesign structure. M9.13 sections removed. Polish-only logistics image removed. Operator decision (reject redesign) applied.
