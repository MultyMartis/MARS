# SITE-002 — STABLE LIVE — M9.13 About Redesign 02

**Status:** **ACTIVE** on TEST — `/about` page authority  
**URL:** https://zpm.new-site.space/about  
**Date:** 2026-06-29  
**Report:** [SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md](../reports/SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md)

## Authority policy

| Rule | Value |
|------|--------|
| **About page** | M9.13 redesign + polish pass v1 — **ACTIVE on TEST** |
| **Visual / UX baseline (site-wide)** | Operator Manual Polish 01 + Local Fonts 01 **preserved** |
| **Font delivery** | Local Fonts 01 — **unchanged** |
| **Supersedes (About only)** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` · legacy pre-M9.13 About on live |
| **Site checkpoint** | Extends `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` — About domain update only |

## Live artifact hashes (post-deploy)

| Artifact | SHA256 | Bytes |
|----------|--------|-------|
| `catalog/view/theme/default/template/information/about.twig` | `2e1fdf5d3fda58f7eb0a4c42a40de6d4f26d904cc0a7b7829a758ada2a1b8dfc` | 19585 |
| `catalog/controller/information/about.php` | `e598e6eba95d7b864b01e1f6ee0cddfeacf3e5705f20b541a33ac3c3df62e29f` | 1864 |
| `assets/css/style.css` | `a7773bc32ea9a0745d14d28d17748e2591e48917dc56db4bdef14d6be45fad0f` | 421855 |
| `assets/img/about-page-img.jpg` | `9732ce40aed0ba90d3cba7872b8bde0dba00d651ab4dd4050614e4ed158ddfe6` | 2585275 |
| `assets/img/about-logistics.jpg` | `b97dcfaa20f61a8bc583efcc558d8bf74003bd216bb90be0121cb800e728bfc6` | 2301124 |

Deploy manifest: [restore-v2-manifest.json](../reports/m9.13-restore-v2-work/restore-v2-manifest.json)

## Pre-deploy backups

| Remote | Backup |
|--------|--------|
| `about.twig` | [catalog__view__theme__default__template__information__about.twig.pre-site-002-about-restore-v2.bak](../backups/catalog__view__theme__default__template__information__about.twig.pre-site-002-about-restore-v2.bak) |
| `about.php` | [catalog__controller__information__about.php.pre-site-002-about-restore-v2.bak](../backups/catalog__controller__information__about.php.pre-site-002-about-restore-v2.bak) |
| `style.css` | [style.css.pre-site-002-about-restore-v2.bak](../backups/style.css.pre-site-002-about-restore-v2.bak) |
| `about-page-img.jpg` | [assets__img__about-page-img.jpg.pre-site-002-about-restore-v2.bak](../backups/assets__img__about-page-img.jpg.pre-site-002-about-restore-v2.bak) |

## Rollback

```text
py reports/m9.13-restore-v2-work/m913-about-rollback-restore-v2.py
```

Returns to legacy About + Local Fonts 01 CSS (pre-restore-v2 state).
