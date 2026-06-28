# SITE-002 — Stable Live PDP Body Category Classes Checkpoint

**Baseline name:** `SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01`  
**Site:** SITE-002 (ЗПМ / BZPM)  
**Environment:** TEST — https://zpm.new-site.space/  
**Registered at:** 2026-06-29  
**Mode:** PDP `<body>` category classes — controller only  
**Status:** **ACTIVE / PASS**

---

## 1. Authority state

**Checkpoint:** `SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01`

**Parent authority:** All prior SITE-002 stable checkpoints retained (Home Commercial Trust, About, Local Fonts, Corporate Intro, etc.)

**Scope:** Product pages only — additive body classes for future CSS; **no visual change**.

---

## 2. Live surface

| Item | Value |
|------|--------|
| Remote file | `catalog/controller/product/product.php` |
| Base classes | `page page--product` |
| Category classes | `category-root-{id}` · `category-parent-{id}` |
| Data source | OpenCart `path` query parameter on product route |

### Verified samples (2026-06-29)

| PDP | body class |
|-----|------------|
| Neutral → moechnye-vanny bath | `page page--product category-root-79 category-parent-80` |
| Neutral → stoly table | `page page--product category-root-79 category-parent-301` |

---

## 3. SHA256

| State | SHA256 | Bytes |
|-------|--------|-------|
| Pre-deploy | `e3eccfc0d0361d3f46ab3a122b4de599af4e0d1dbb22db9de8fc6d874435320a` | 30 566 |
| Post-deploy | `df015d3ed96af041ae570a2156508df2f8ba533f9bfbe27b3053f03a8586812e` | 31 409 |

Manifest: [reports/pdp-body-category-classes-work/deploy-manifest.json](../reports/pdp-body-category-classes-work/deploy-manifest.json)

---

## 4. Rollback

| Item | Path |
|------|------|
| Script | [site-002-pdp-body-category-classes-rollback.py](../reports/pdp-body-category-classes-work/site-002-pdp-body-category-classes-rollback.py) |
| Backup | `backups/catalog__controller__product__product.php.pre-pdp-body-category-classes.bak` |

---

## 5. Report

[reports/SITE-002-PDP-BODY-CATEGORY-CLASSES.md](../reports/SITE-002-PDP-BODY-CATEGORY-CLASSES.md)
