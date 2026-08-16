# ASSET-CONDITION MAP — PROD-P11

| Asset / behavior | Before (P08/P09) | After (P11) |
|------------------|------------------|-------------|
| Specialist profile CSS | `is_page()` + hub child | `shpigovsky_is_specialist_singular()` → `is_singular('specialist')` (+ legacy child safety) |
| Fancybox certificates | same page/hub-child gate | same singular specialist gate |
| Template render | Generic Content page template + content-page branch | `single-specialist.php` forced; leftover `_wp_page_template` cleared |
| Cards / hub listing | page children of `#1030` | `post_type=specialist` ordered by `menu_order` (empty-CPT rollback fallback) |
| Smart Search group Специалисты | page children under hub | CPT `specialist` (page fallback only if CPT empty) |
| Sitemap specialists provider | page children | CPT IDs; unset from core posts provider to avoid duplicates |
