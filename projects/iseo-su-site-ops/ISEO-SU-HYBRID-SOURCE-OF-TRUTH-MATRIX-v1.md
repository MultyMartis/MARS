# ISEO-SU HYBRID SOURCE-OF-TRUTH MATRIX v1

**Programme:** ISEO-SU-SITE-OPS  
**Origin:** PHASE 2B  
**Updated:** 2026-07-24 architecture knowledge capture  

Detail maps: [ISEO-SU-PAGE-TO-SOURCE-MAP-v1.md](ISEO-SU-PAGE-TO-SOURCE-MAP-v1.md) · [ISEO-SU-TASK-ROUTING-GUIDE-v1.md](ISEO-SU-TASK-ROUTING-GUIDE-v1.md)

| surface | production runtime location | current editor/owner | confirmed source | deployment method | drift risk | future MARS method | classification |
|---------|------------------------------|----------------------|------------------|-------------------|------------|--------------------|----------------|
| Homepage `/` | WP page + `page-home.php` | SFTP theme | **`page-home.php`** | SFTP theme | High vs `home.html` | SFTP theme scoped | WORDPRESS_TEMPLATE_STATIC_LIKE |
| `home.html` | docroot file | SFTP | parallel file | SFTP | High | avoid / sync deliberately | LEGACY_OR_PARALLEL |
| Marketing HTML | `*.html`, `services/`, `cases/` | SFTP | production files | SFTP | Medium–High | SFTP | STATIC_HARDCODED |
| Shared CSS/JS | `css/`, `js/`, `libs/` | SFTP | production assets | SFTP | **High** | SFTP + HITL | SHARED |
| Blog posts | WP DB + `single.php` + ACF «Записи» | WP Admin | WordPress | WP Admin | Medium | WPilot only if later chartered for post_content | WORDPRESS_CONTENT |
| Blog hub `/blog` | `page-blog.php` | SFTP theme | theme template | SFTP | Medium | SFTP theme | WORDPRESS_TEMPLATE_STATIC_LIKE |
| Blog chrome | theme header/footer/parts | SFTP | theme parts | SFTP | Medium | SFTP | WORDPRESS |
| Tariff calculator page | `/tariff-calc` + ACF + `tarif-calc.php` + JS + handlers | Mixed | **Hybrid layers** | WP ACF + SFTP | **High** | map layer first | HYBRID_COMPOSITE |
| Tariff cards on HTML | markup + common.js + FORM.php | SFTP | static+JS+handlers | SFTP | High | protect | HYBRID on static pages |
| Form/mail handlers | `*__FORM.php` (+ copies) | SFTP | production PHP | SFTP | High | protect | STATIC_HARDCODED handlers |
| Offers / web-KP candidate | `/offers` + CPT `offer` + ACF «Предложения» | WP Admin | WP CPT/ACF/theme | WP / SFTP theme | Medium | WP Admin; private | WORDPRESS_CONTENT |
| Report Hub | `report-hub/` | SFTP | sibling files | SFTP | Medium | separate programme | EXTERNAL_SIBLING |
| Plugins/core | wp-content / core | WP Admin | vendor+WP | HOLD updates | Medium | charter only | WORDPRESS |
| Routing | `.htaccess` | SFTP | docroot htaccess | SFTP | Critical | protect | infrastructure |
| Offline Git/build SoT | not on server | SAFE UNKNOWN | U-022 | — | High if assumed | resolve before sync | SAFE_UNKNOWN |

---

*Hybrid SoT matrix v1 · updated 2026-07-24.*
