# ISEO-SU PAGE-TO-SOURCE MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Date:** 2026-07-24  
**Companion matrix:** [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)

Maps each major route to WP object, template, root file, includes, assets, handlers, and edit method.

| Route | WP object | Template | Root / primary file | Includes / parts | Assets | Handlers | Edit method |
|-------|-----------|----------|---------------------|------------------|--------|----------|-------------|
| `/` | page 1732 `glavnaya` | `page-home.php` | theme `page-home.php` | none (monolithic) | `css/*`, `libs/*`, `js/common.js`, `img/` | via common.js → FORM.php | SFTP theme file (not editor) |
| `/home.html` | — | — | `home.html` | none observed | same family | same | SFTP file (parallel) |
| `/blog` | page 1730 | `page-blog.php` | theme `page-blog.php` | header/footer/topbar | theme enqueues + `js/common.js` | chrome forms | theme + posts separately |
| `/blog/{slug}.html` | post | `single.php` | theme `single.php` | header; ACF fields | theme + uploads | — | WP Admin + ACF «Записи» |
| `/blog/category/*` | category | `archive.php` / hierarchy | theme | header/footer | theme | — | WP taxonomy / posts |
| `/tariff-calc` | page 1734 | `page-tariffcalc.php` | theme page + `template-parts/tarif-calc.php` | `include_once` tarif-calc | theme + common.js | `calc__FORM.php`, `tariff_*__FORM.php` | ACF calculator groups + theme part |
| `/offers` | page 1377 | default `page.php` → `content-page` | theme `page.php` | `template-parts/content-page.php` | theme | — | WP page; related CPT admin |
| `/offer/{slug}` (private) | CPT `offer` | `single-offer.php` | theme `single-offer.php` | header; ACF | theme | — | WP offer + ACF «Предложения» |
| `/services.html` | — | — | `services.html` | none | css/js/libs | forms via JS | SFTP |
| `/services/seo.html` etc. | — | — | matching path | none / local | css/js | often `services/.../*__FORM.php` | SFTP exact path |
| `/cases.html` | — | — | `cases.html` | — | css/js | forms | SFTP |
| `/cases/*.html` | — | — | `cases/*.html` | — | css/js | forms | SFTP |
| `/contacts.html` | — | — | `contacts.html` | — | css/js | callback/page | SFTP |
| `/about.html` | — | — | `about.html` | — | css/js | forms | SFTP |
| `/reviews.html` | — | — | `reviews.html` | — | css/js | `review__FORM.php` | SFTP |
| `/partners.html` | — | — | `partners.html` | — | css/js | `partners__FORM.php` | SFTP |
| `/bonuses.html` | — | — | `bonuses.html` | — | css/js | `bonus__FORM.php` | SFTP |
| `/career.html` | — | — | `career.html` | — | css/js | `career__FORM.php` | SFTP |
| `/guarantees.html` | — | — | `guarantees.html` | — | css/js | — | SFTP |
| legal pages | — | — | matching `*.html` | — | css | — | SFTP |
| `/report-hub/` | — | — | `report-hub/*` | app-local | local | — | sibling programme |
| `/varvara-new.php` | — | — | `varvara-new.php` | — | — | — | SFTP chartered |
| `/sitemap-static.xml` | — | — | `sitemap-static.xml` | — | — | — | SFTP |
| `/sitemap.xml` | Yoast index | — | generated + includes static | — | — | — | Yoast + static file |

---

*Page-to-source map v1 · 2026-07-24.*
