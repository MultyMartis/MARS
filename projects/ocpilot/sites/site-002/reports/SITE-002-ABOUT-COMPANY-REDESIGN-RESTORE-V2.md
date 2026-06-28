# REPORT — SITE-002 ABOUT COMPANY REDESIGN RESTORE

**Project:** SITE-002 (BZPM / ЗПМ)  
**URL (TEST):** https://zpm.new-site.space/about  
**Prior authority:** `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`  
**New authority:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`  
**Mode:** Re-activation of saved M9.13 implementation — **not** recovery, **not** redesign  
**Date:** 2026-06-29  
**Pre-work git:** `50b1f0bc` (CHECKPOINT-PRE-ABOUT-RESTORE-V2)  
**Post-work git:** pending final commit

---

## 1. Pre-flight

| Check | Result |
|-------|--------|
| HEAD (pre-work) | `51d41f25` — `feat(site-002): local Inter fonts migration on TEST` |
| Branch | `mars/canonical-post-recovery` |
| Prior checkpoint | `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` |
| Git pre-marker | [CHECKPOINT-PRE-ABOUT-RESTORE-V2.md](m9.13-restore-v2-work/CHECKPOINT-PRE-ABOUT-RESTORE-V2.md) @ `50b1f0bc` |
| Authority verification | **PASS** — all M9.13 work copies present |

---

## 2. Authority source (implementation restored from)

| Artifact | Source path | SHA256 |
|----------|-------------|--------|
| `about.twig` | `reports/m9.13-work/about.twig` (polish-inclusive) | `2e1fdf5d3fda58f7eb0a4c42a40de6d4f26d904cc0a7b7829a758ada2a1b8dfc` |
| `about.php` | `reports/m9.13-work/about.php` | `e598e6eba95d7b864b01e1f6ee0cddfeacf3e5705f20b541a33ac3c3df62e29f` |
| M9.13 CSS block | `reports/m9.13-work/m9.13-about-page.css` | `3d7313a747fa1854a129a63a7377f40b180b0f3c415621cf907795e072d42453` |
| Hero image | `reports/m9.13-polish-work/assets/img/about-page-img.jpg` | `9732ce40aed0ba90d3cba7872b8bde0dba00d651ab4dd4050614e4ed158ddfe6` |
| Logistics image | `reports/m9.13-polish-work/assets/img/about-logistics.jpg` | `b97dcfaa20f61a8bc583efcc558d8bf74003bd216bb90be0121cb800e728bfc6` |

**Reports (design authority):**

- [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md)
- [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md)

**NOT used:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` live state · pre-redesign legacy About · Pass 1 / 1.1 / 1.2 as About source.

---

## 3. Files restored (deployed to TEST)

| Remote path | Action | Post SHA256 | Bytes |
|-------------|--------|-------------|-------|
| `catalog/view/theme/default/template/information/about.twig` | Replaced with M9.13 polish twig | `2e1fdf5d…` | 19585 |
| `catalog/controller/information/about.php` | Replaced with M9.13 controller (SEO meta) | `e598e6eb…` | 1864 |
| `assets/css/style.css` | **Merged** — M9.13 block appended to live operator CSS | `a7773bc3…` | 421855 |
| `assets/img/about-page-img.jpg` | Replaced with polish hero photo | `9732ce40…` | 2585275 |
| `assets/img/about-logistics.jpg` | Uploaded (was absent after prior restore) | `b97dcfaa…` | 2301124 |

**Untouched (per scope):** Delivery · Payment · Warranty · Dealers · Custom · Catalog · PDP · Home · Commercial Trust · `main.js` · `header.twig`

---

## 4. Merge — operator changes preserved

| File | Merge strategy | Operator canon preserved |
|------|----------------|--------------------------|
| `style.css` | Download live (Local Fonts 01 + Operator Manual Polish 01) → append/replace `zpm-about-page*` block only | **YES** — full operator CSS retained; only M9.13 About namespace added (~6942 bytes) |
| `about.twig` | Full replace — pre-restore was legacy layout (3443 bytes); no operator delta on About twig since restoration | N/A — legacy twig had no post-polish operator edits |
| `about.php` | Full replace — M9.13 SEO meta controller | N/A — pre-restore matched pre-M9.13 controller |
| Images | Polish authority assets deployed | Hero replaced; logistics re-added |

**Pre-restore live `style.css` SHA256:** `78c6e13b17632e8f8638515af5141c8a79c432ff45e215e75d56c5b3430635d7` (Local Fonts 01 authority — unchanged except appended About block)

---

## 5. Old files no longer active on live

| Artifact | Status |
|----------|--------|
| Legacy `about.twig` (`about-page--main-wrap`, video, cert slider, dealer form) | **Superseded** — backed up |
| Legacy `about.php` (pre-M9.13 partial loads) | **Superseded** — backed up |
| Pre-restore hero JPEG (276765 bytes) | **Superseded** — backed up |
| `style.css` without `zpm-about-*` block | **Superseded** for About rendering — operator CSS otherwise retained in merged file |

Legacy `.about-page-*` CSS rules remain in `style.css` as orphaned selectors — harmless; not removed to avoid touching operator CSS.

---

## 6. Backups (FTP pre-deploy)

Suffix: `.pre-site-002-about-restore-v2.bak`

| Backup file | SHA256 | Bytes |
|-------------|--------|-------|
| `catalog__view__theme__default__template__information__about.twig.pre-site-002-about-restore-v2.bak` | `998321d3b3ea0a119b0aa688d9c6ebbcdc31431ced75110450026d24458202f8` | 3443 |
| `catalog__controller__information__about.php.pre-site-002-about-restore-v2.bak` | `77ac5ea35be5863f5c729c996743a8f8cd18af3e9afca328d4dcde7585b5fa8a` | 1687 |
| `style.css.pre-site-002-about-restore-v2.bak` | `78c6e13b17632e8f8638515af5141c8a79c432ff45e215e75d56c5b3430635d7` | 414913 |
| `assets__img__about-page-img.jpg.pre-site-002-about-restore-v2.bak` | `138d682e4e3b0acc214c9ac24d31fe1c5110653809da9f6c35028966293230e3` | 276765 |

Manifest: [m9.13-restore-v2-work/restore-v2-manifest.json](m9.13-restore-v2-work/restore-v2-manifest.json)  
SHA256 index: [m9.13-restore-v2-work/restore-v2-sha256.json](m9.13-restore-v2-work/restore-v2-sha256.json)

---

## 7. QA

### Automated HTML (post-deploy)

| Check | Pass |
|-------|------|
| HTTP 200 | ✓ |
| Breadcrumbs present | ✓ |
| `zpm-about-page` namespace | ✓ |
| All 6 M9.13 sections | ✓ |
| Hero trust row + FAD icons | ✓ |
| Logistics photo | ✓ |
| Fancybox cert | ✓ |
| CTA form `dialog=7` | ✓ |
| No legacy video / slider / dealer blocks | ✓ |
| **all_pass** | ✓ |

Capture: [m9.13-restore-v2-work/qa-about-redesign-v2.html](m9.13-restore-v2-work/qa-about-redesign-v2.html)

### Playwright (desktop / tablet / mobile)

| Check | Desktop 1440 | Tablet 1024 | Mobile 390 |
|-------|--------------|-------------|------------|
| Console errors | 0 | 0 | 0 |
| Horizontal overflow | ✓ | ✓ | ✓ |
| Full-page + section screenshots | ✓ | ✓ | ✓ |

Screenshots: `qa/m9.13-about-redesign-v2-screenshots/`  
Manifest: [qa/m9.13-about-redesign-v2-screenshots/screenshot-manifest.json](../qa/m9.13-about-redesign-v2-screenshots/screenshot-manifest.json)

**Manual HITL pending:** form submit smoke test · operator visual sign-off @ 1440 / 1024 / 390

---

## 8. Rollback

### Point rollback (restore pre-restore-v2 state)

```text
py reports/m9.13-restore-v2-work/m913-about-rollback-restore-v2.py
```

Restores all four `.pre-site-002-about-restore-v2.bak` files to FTP. Returns About to legacy pre-M9.13 layout with Local Fonts 01 CSS intact.

### Full disaster rollback

Beget full backup + current live TEST + file-level pass backups.

---

## 9. Git

| Item | Value |
|------|--------|
| Pre-work commit | `50b1f0bc` — CHECKPOINT-PRE-ABOUT-RESTORE-V2 |
| Deploy script | `reports/m9.13-restore-v2-work/m913-about-restore-redesign-v2.py` |
| Rollback script | `reports/m9.13-restore-v2-work/m913-about-rollback-restore-v2.py` |
| Screenshot script | `reports/m9.13-restore-v2-work/m913-about-restore-v2-screenshots.py` |

---

## 10. Checkpoint

**Registered:** `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`  
Baseline: [baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md)  
Registration: [SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-REDESIGN-02.md](SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-REDESIGN-02.md)

Supersedes `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` for `/about` page domain only. Local Fonts 01 font delivery authority **carried forward**.

---

## 11. Final verdict

**READY FOR HITL REVIEW**

M9.13 About Company redesign + polish pass v1 re-activated on TEST from saved work copies. Operator Manual Polish 01 + Local Fonts 01 CSS preserved via merge. No scope expansion. No redesign. Automated QA **PASS**. Operator visual and form HITL **PENDING**.
