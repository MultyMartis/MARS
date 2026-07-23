# ISEO-SU HYBRID SOURCE-OF-TRUTH MATRIX v1

**Programme:** ISEO-SU-SITE-OPS  
**Task:** PHASE 2B  
**Date:** 2026-07-24  

| surface | production runtime location | current editor/owner | possible source | confirmed source | deployment method | drift risk | future MARS method | classification |
|---------|------------------------------|----------------------|-----------------|------------------|-------------------|------------|--------------------|----------------|
| Homepage `/` | WP page + `iseoblog/page-home.php` | Operator / freelancers via WP file or SFTP | Also `home.html` | **WP template `page-home.php` for `/`** | SFTP / WP theme file edit | **High** vs `home.html` | SFTP scoped file OR WPilot only if content moved to WP fields | SHARED_BUT_WORDPRESS_RENDERED |
| Marketing HTML pages | `public_html/*.html`, `services/`, `cases/` | SFTP / direct file | Unknown local build | **Production files** | SFTP upload | Medium–High | SFTP / future mirror | STATIC_FILE_OWNED |
| Shared CSS/JS | `css/`, `js/`, `libs/` | SFTP | Unknown build pipeline | **Production asset dirs** | SFTP | High (global blast radius) | SFTP with strong HITL | SHARED_BUT_STATIC_RENDERED |
| Blog posts | WP DB + theme templates | WP Admin | — | **WordPress** | WP Admin / future WPilot | Medium | WPilot (after gate) | WORDPRESS_OWNED |
| Blog chrome | `iseoblog` header/footer/template-parts | SFTP theme files | — | **Theme files** | SFTP | Medium | SFTP scoped / WPilot for content only | WORDPRESS_OWNED |
| Tariff cards | HTML + `js/common.js` + theme `content-tarifs-*` | Mixed | Dual | **Mixed — URL-dependent** | SFTP | **High** | Map URL then single-channel edit | SHARED |
| SEO calculator | `js/common.js` + `calc__FORM.php` + theme calc parts | Mixed | Dual | **Mixed — URL-dependent** | SFTP | **High** | Protect; chartered SFTP only | SHARED |
| Form/mail handlers | `*__FORM.php` (+ copies) | SFTP | — | **Production PHP handlers** | SFTP | High (lead loss) | Protect; never casual edit | STATIC_FILE_OWNED |
| Offers / commercial proposals | CPT `offer`, `/offers`, `single-offer.php` | WP Admin + theme | Candidate for “web-KP” | **WordPress CPT/theme** (tool name unconfirmed) | WP / SFTP theme | Medium | WPilot for CPT content after gate | WORDPRESS_OWNED / SAFE_UNKNOWN tool label |
| Report Hub | `report-hub/*.html` | SFTP | Sibling product | **Production report-hub files** | SFTP | Medium | Separate programme boundary | EXTERNAL_TOOL |
| Plugins | `wp-content/plugins` | WP Admin | Vendor | **Plugin dirs + WP** | WP Admin updates (not in this task) | Medium | HOLD updates unless chartered | WORDPRESS_OWNED |
| Core | `wp-admin`, `wp-includes` | Hosting/WP | WordPress.org | **Core trees** | Core updates HOLD | High if touched | Never casual | WORDPRESS_OWNED |
| Routing | `.htaccess` | SFTP | — | **Docroot `.htaccess`** | SFTP | Critical | Protect | SHARED infrastructure |
| Canonical Git/build outside prod | Not found on server | SAFE UNKNOWN | Local machine / other repo | **SAFE UNKNOWN** | — | High if assumed | Resolve U-022 before sync fantasies | SAFE_UNKNOWN |

---

*Hybrid SoT matrix v1 · 2026-07-24.*
