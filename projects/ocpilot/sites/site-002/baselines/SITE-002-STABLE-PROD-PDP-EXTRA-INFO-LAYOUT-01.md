# SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01

**Site:** SITE-002 (ЗПМ / bzpm.ru)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01` (OCPilot Run 4.218)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`

---

## Summary

PDP attribute **«Дополнительные сведения»** is extracted in `product.php` for display only and rendered as `product-content__extra-info` after `product-content__specs-toggle-wrap` in `producttabs.twig`. Spec table no longer contains the long prose row.

| Field | Value |
|-------|--------|
| Remote files patched | **3** (`product.php`, `producttabs.twig`, `assets/css/style.css`) |
| DB / admin / product data changes | **0** |
| Meta generator | **preserved** |
| Example PDP verification | extra info **out of table**, separate block **after toggle** |
| Forbidden public **БЗПМ** | **0** |
| Sitemap URL count | **1377** (unchanged) |

---

## Patched files

| Remote path | Role |
|-------------|------|
| `/public_html/catalog/controller/product/product.php` | `$data['extra_info_attribute']` display extraction |
| `/public_html/catalog/view/theme/default/template/product/producttabs.twig` | Extra-info block markup |
| `/public_html/assets/css/style.css` | Scoped `.product-content__extra-info` styles |

---

## Rollback

Re-upload from:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01\source-before\`

Manifest: `rollback/remote-before-manifest.json`

---

## Report

[sites/site-002/reports/SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01.md](../reports/SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01.md)
