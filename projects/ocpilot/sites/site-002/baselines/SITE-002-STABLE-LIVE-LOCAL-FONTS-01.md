# SITE-002 — STABLE LIVE — Local Fonts 01

**Status:** **ACTIVE** on TEST — font delivery authority for SITE-002  
**URL:** https://zpm.new-site.space/  
**Date:** 2026-06-29  
**Report:** [SITE-002-LOCAL-FONTS-MIGRATION.md](../reports/SITE-002-LOCAL-FONTS-MIGRATION.md)

## Authority policy

| Rule | Value |
|------|--------|
| **Visual / UX baseline** | Preserved from `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` — no typography/layout/CSS design changes |
| **Font delivery** | **100% local** — no Google Fonts, no CDN font CSS, no external `@font-face` |
| **Supersedes** | Operator Manual Polish 01 for `@font-face`, preload, and font file inventory only |

## Live artifact hashes (post-deploy)

| Artifact | SHA256 | Bytes |
|----------|--------|-------|
| `assets/css/style.css` | `78c6e13b17632e8f8638515af5141c8a79c432ff45e215e75d56c5b3430635d7` | 414913 |
| `assets/css/style.min.css` | `559283779628ccff246d4a913ff5feab21540485a7da4a8d274417614fb43df9` | 76956 |
| `catalog/view/theme/default/template/common/header.twig` | `25e77e036aec73d58bda40b493da3502c73db04e6753d222cac6eeb8db9a71da` | 15158 |
| `assets/fonts/Inter-Bold.woff2` | `6f56409fd3d64bb85f7d070bce20749db2d66b6d63cec586cc22d1c761be2491` | 24356 |
| `assets/fonts/Inter-ExtraBold.woff2` | `a7d0a50f15d389cad679238466bdb5fc9787aa0715719064ce25abaff042820d` | 24400 |

Deploy manifest: [deploy-manifest.json](../reports/local-fonts-work/deploy-manifest.json)

## Pre-deploy backups

| Remote | Backup |
|--------|--------|
| `assets/css/style.css` | [style.css.pre-site-002-local-fonts-01.bak](../backups/style.css.pre-site-002-local-fonts-01.bak) |
| `assets/css/style.min.css` | [style.min.css.pre-site-002-local-fonts-01.bak](../backups/style.min.css.pre-site-002-local-fonts-01.bak) |
| `header.twig` | [catalog__view__theme__default__template__common__header.twig.pre-site-002-local-fonts-01.bak](../backups/catalog__view__theme__default__template__common__header.twig.pre-site-002-local-fonts-01.bak) |

## Rollback

1. Restore `.pre-site-002-local-fonts-01.bak` files via FTP  
2. Delete `Inter-Bold.woff2` and `Inter-ExtraBold.woff2` if rolling back fully  
3. Clear OpenCart Twig template cache if header restored
