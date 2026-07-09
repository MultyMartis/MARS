# SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01

**Issued:** 2026-07-09  
**Parent checkpoint:** [SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01.md](SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01.md)  
**Operation:** `SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01`  
**OCPilot run:** 4.236  
**Environment:** https://bzpm.ru/ (Production)

## Parent Category Tiles whitelist (after)

**Terminology:** Parent Category Tiles / Витрина родительских категорий

```
$neutral_hub_branch_ids = array(322, 331, 301, 326, 354, 358, 207, 80, 86, 360);
```

- **Removed from parent tiles:** **88** Лари  
- **Kept:** **358** Шкафы и лари  
- **Tile count:** homepage + neutral hub = **10** `zpm-cat-card` (was 11)

## Category hierarchy (unchanged from Run 4.235)

```
79 Нейтральное оборудование
→ 358 Шкафы и лари
  → 88 Лари (child category page active)
```

## Surfaces verified

| Surface | Лари standalone tile | Шкафы и лари tile |
|---------|---------------------|-------------------|
| Homepage | absent | present |
| Neutral hub | absent | present |
| `/katalog` megamenu | absent | present |
| `/shkafy-i-lari` children | **present** (child card) | hub page |

## Production file touched

| Remote path | Change |
|-------------|--------|
| `/public_html/system/library/zpm/category_visibility.php` | Removed **88** from `$neutral_hub_branch_ids` |

## Unchanged from parent checkpoint

- Nested URL `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari` — **200**
- Old flat `/lari` — **301** to nested
- DB `parent_id`, `category_path`, SEO keywords, redirects, sitemap policy

## Pending (inherited)

Post-1C import verification for Run 4.235 reparent persistence.

## Report

[sites/site-002/reports/SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md](../reports/SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md)
