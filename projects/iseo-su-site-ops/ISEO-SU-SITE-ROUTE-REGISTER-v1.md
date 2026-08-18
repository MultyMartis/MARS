# ISEO-SU SITE ROUTE REGISTER v1

**Programme:** ISEO-SU-SITE-OPS  
**Status:** SUPERSEDES practical use of [ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md](ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md) for classification work  
**Authority detail:** [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)  
**Updated:** 2026-07-24 architecture knowledge capture  

Historical public route register remains immutable evidence; this register uses the new classification vocabulary.

| ID | Path | Class | Conf | Notes |
|----|------|-------|------|-------|
| SR-001 | `/` | WORDPRESS_TEMPLATE_STATIC_LIKE | HIGH | page 1732 + `page-home.php` |
| SR-002 | `/home.html` | LEGACY_OR_PARALLEL | HIGH | drift twin |
| SR-003 | `/blog` | WORDPRESS_TEMPLATE_STATIC_LIKE | HIGH | page 1730 + `page-blog.php` |
| SR-004 | `/blog.html` | LEGACY_OR_PARALLEL | HIGH | not live blog |
| SR-005 | `/blog/{slug}.html` | WORDPRESS_CONTENT | HIGH | permalink pattern |
| SR-006 | `/blog/category/{slug}` | WORDPRESS_CONTENT | HIGH | categories live |
| SR-007 | `/tariff-calc` | HYBRID_COMPOSITE | HIGH | ACF + theme + JS + handlers |
| SR-008 | `/offers` | WORDPRESS_CONTENT | HIGH | offers / web-KP candidate entry |
| SR-009 | `/offer/*` | WORDPRESS_CONTENT | MEDIUM | private CPT singles; robots disallow |
| SR-010 | `/web-kp/` `/kp/` | SAFE_UNKNOWN | HIGH | 404; naming only |
| SR-011 | `/services.html` | STATIC_HARDCODED | HIGH | intermittent 500 observed once |
| SR-012 | `/services/**` | STATIC_HARDCODED | HIGH | sitemap-static inventory |
| SR-013 | `/cases.html` `/cases/**` | STATIC_HARDCODED | MEDIUM | |
| SR-014 | `/contacts.html` | STATIC_HARDCODED | HIGH | |
| SR-015 | `/about.html` | STATIC_HARDCODED | HIGH | |
| SR-016 | root marketing HTML set | STATIC_HARDCODED | HIGH | reviews/partners/bonuses/career/guarantees/legal |
| SR-017 | `/report-hub/` | EXTERNAL_SIBLING | HIGH | sibling product |
| SR-018 | `/varvara-new.php` | STATIC_HARDCODED | MEDIUM | VVR-Searcher |
| SR-019 | `/sitemap.xml` | HYBRID_COMPOSITE | HIGH | Yoast index + static |
| SR-020 | `/sitemap-static.xml` | STATIC_HARDCODED | HIGH | 71 URLs |
| SR-021 | `/robots.txt` | STATIC_HARDCODED | HIGH | |
| SR-022 | `www` host | REDIRECT_OR_ALIAS | HIGH | → apex https |

---

*Site route register v1 · 2026-07-24.*
