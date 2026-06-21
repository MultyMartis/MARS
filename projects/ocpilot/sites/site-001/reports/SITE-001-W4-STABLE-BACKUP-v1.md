# SITE-001 W4 Stable Backup v1

**Type:** Stable checkpoint report — pre-W4.1  
**Date:** 2026-06-09  
**Site:** SITE-001 — Автосалон СИБКАР  
**Environment:** **TEST only** — `https://sibcar.new-site.space/`  
**Backup ID:** `pre-w4-1-stable-20260609-1506`

---

## Summary

Stable incremental backup created per OCPilot discipline **before** W4.1 Header & Hero Authority write. Captures accepted W4 + W3UX-C1 + W3ATMOSPHERE TEST state.

---

## Backup location

```
C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\pre-w4-1-stable-20260609-1506\
├── BACKUP-MANIFEST.md
├── catalog__view__theme__auto__template__common__header.twig
├── catalog__view__theme__auto__template__common__footer.twig
├── catalog__view__theme__auto__template__product__product.twig
├── css__main.css
└── css__media.css
```

---

## Files backed up

| Remote path | Bytes | Lines |
|-------------|-------|-------|
| `catalog/view/theme/auto/template/common/header.twig` | 11,653 | 343 |
| `catalog/view/theme/auto/template/common/footer.twig` | 20,078 | 410 |
| `catalog/view/theme/auto/template/product/product.twig` | 37,330 | 931 |
| `css/main.css` | 140,066 | 8,217 |
| `css/media.css` | 35,060 | 2,402 |

---

## Live CSS sizes (pre-W4.1)

| File | Bytes | Lines |
|------|-------|-------|
| `css/main.css` | 140,066 | 8,217 |
| `css/media.css` | 35,060 | 2,402 |

---

## Active wave markers (pre-W4.1)

| Marker | Present |
|--------|---------|
| W3UX-C1 Used Catalog Card Density | **YES** |
| W3ATMOSPHERE-01 Global Atmosphere Refresh | **YES** |
| W4 Used PDP Structural Visual Slice | **YES** |
| W4.1 Header & Hero Authority | **NO** |

---

## Rollback

**T1:** Restore all 5 files from `pre-w4-1-stable-20260609-1506` via FTP STOR + cache clear.  
**footer.twig:** included in backup; restore only if modified during W4.1 (W4.1 did **not** modify footer).

---

## Evidence

| Artifact | Path |
|----------|------|
| Manifest | External storage `BACKUP-MANIFEST.md` |
| Result JSON | `.recovery-temp/site-001-w4-1-result.json` |
| Execute script | `.recovery-temp/site-001-w4-1-execute.py` |

---

## Status

**DONE** — stable checkpoint **ACTIVE** as W4.1 rollback baseline.

*SITE-001 W4 Stable Backup v1 — TEST only; no production; no commit.*
