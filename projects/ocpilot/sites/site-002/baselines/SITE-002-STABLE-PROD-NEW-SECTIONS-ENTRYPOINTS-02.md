# SITE-002-STABLE-PROD-NEW-SECTIONS-ENTRYPOINTS-02

**Site:** SITE-002 (ЗПМ / bzpm.ru)  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Issued:** 2026-07-07  
**Operation:** `SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02` (OCPilot Run **4.220**)  
**Parent checkpoint:** `SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01`

---

## Summary

Homepage and neutral-hub category tiles extended from **9 → 11** with Лари (88) and Кондитерский инвентарь (360). Composer-only white-background WebP images deployed; `category_visibility.php` whitelist updated.

| Field | Value |
|-------|--------|
| Branch IDs | `322,331,301,326,354,358,207,80,86,88,360` |
| New images | `lari.webp`, `konditerskiy-inventar.webp` (+ cache 300×300) |
| Admin image saves | **2** (IDs 88, 360) |
| Code files patched | **1** (`category_visibility.php`) |
| Image generation | **COMPOSER_ONLY_NO_API** |
| PDP extra-info (4.218) | **preserved** |
| Forbidden public **БЗПМ** | **0** |

---

## Remote paths changed

| Path | Role |
|------|------|
| `/public_html/image/catalog/Category-image/lari.webp` | Master tile image |
| `/public_html/image/catalog/Category-image/konditerskiy-inventar.webp` | Master tile image |
| `/public_html/image/cache/catalog/Category-image/lari-300x300.webp` | Cache derivative |
| `/public_html/image/cache/catalog/Category-image/konditerskiy-inventar-300x300.webp` | Cache derivative |
| `/public_html/system/library/zpm/category_visibility.php` | Branch whitelist |

---

## Rollback

Re-upload from:

`X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\deployments\SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02\source-before\`

Manifest: `rollback/remote-before-manifest.json`

---

## Report

[sites/site-002/reports/SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02.md](../reports/SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02.md)
