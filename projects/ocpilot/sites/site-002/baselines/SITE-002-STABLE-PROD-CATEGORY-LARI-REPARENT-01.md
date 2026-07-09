# SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01

**Issued:** 2026-07-09  
**Parent checkpoint:** [SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01.md](SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01.md)  
**Operation:** `SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01`  
**OCPilot run:** 4.235  
**Environment:** https://bzpm.ru/ (Production)

## Category hierarchy (after)

```
79 Нейтральное оборудование
→ 358 Шкафы и лари
  → 88 Лари
    → 140 Производственные лари
    → 141 Складские лари
  → 359 Шкафы кухонные
```

## Canonical URLs

| Page | URL |
|------|-----|
| Лари | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` |
| Складские лари | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/skladskie-lari` |
| Производственные лари | `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari/proizvodstvennye-lari` |

## Redirects (.htaccess)

- `/katalog/nejtralnoe-oborudovanie/lari` → nested `/shkafy-i-lari/lari` (301)
- `/katalog/nejtralnoe-oborudovanie/lari/*` → nested `/shkafy-i-lari/lari/*` (301)

## Production files touched

| Remote path | Role |
|-------------|------|
| `/public_html/.htaccess` | Old flat lari tree 301 |
| `/public_html/catalog/controller/startup/seo_url.php` | category_path normalize + rewrite |
| `/public_html/catalog/controller/startup/seo_pro.php` | `getPathByCategory` uses `category_path` |
| `/public_html/system/library/zpm/category_visibility.php` | `buildCategoryPathParam` + `product/katalog` links |
| `/public_html/catalog/controller/product/category.php` | Canonical/hub links via `buildCategoryPathParam` |

## Cache actions (scoped)

Cleared: `cache.category.seopath.*`, `cache.seo_pro.*`, `cache.cat-list-header.*`, `cache.product.seopath.*`

## Pending verification

**Post-1C import persistence** — next scheduled 1C import must be observed to confirm `parent_id` and `category_path` remain correct (1C does not update `parent_id` on existing categories per discovery; reparent is DB-authoritative until import behavior is re-verified).

## Report

[sites/site-002/reports/SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01.md](../reports/SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01.md)
