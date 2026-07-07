# SITE-002-STABLE-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01

**Site:** SITE-002 (ЗПМ / bzpm.ru)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-08  
**Operation:** `SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01` (OCPilot Run **4.221**)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-NEW-SECTIONS-ENTRYPOINTS-02`

---

## Summary

Category entrypoints on megamenu, homepage, and neutral hub display in **Russian A→Я** order by visible category name. Membership (11 branch IDs), images, and URLs unchanged.

| Field | Value |
|-------|--------|
| Branch IDs (membership) | `322,331,301,326,354,358,207,80,86,88,360` |
| Display sort | **А → Я** by `name` |
| Code files patched | **2** (`category_visibility.php`, `category.php`) |
| Images / admin / DB | **0 changes** |
| PDP extra-info (4.218) | **preserved** |
| Forbidden public **БЗПМ** | **0** |

---

## Remote paths changed

| Path | Role |
|------|------|
| `/public_html/system/library/zpm/category_visibility.php` | Sort helper + homepage + megamenu children |
| `/public_html/catalog/controller/product/category.php` | Neutral hub `hub_categories` sort |

---

## Rollback

Re-upload from:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01\source-before\`

Manifest: `rollback/remote-before-manifest.json`

---

## Report

[sites/site-002/reports/SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01.md](../reports/SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01.md)
