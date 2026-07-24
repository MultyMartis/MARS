# ISEO-SU STATIC / WORDPRESS BOUNDARY MAP v1

**Programme:** ISEO-SU-SITE-OPS  
**Origin:** PHASE 2B  
**Updated:** 2026-07-24 architecture knowledge capture  

Legacy vocabulary (2B) remains in historical notes. **Operational classification** now uses:

`STATIC_HARDCODED` · `WORDPRESS_CONTENT` · `WORDPRESS_TEMPLATE_STATIC_LIKE` · `HYBRID_COMPOSITE` · `REDIRECT_OR_ALIAS` · `LEGACY_OR_PARALLEL` · `SAFE_UNKNOWN` · `EXTERNAL_SIBLING`

Canonical table: [ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md](ISEO-SU-CANONICAL-ROUTE-OWNERSHIP-MATRIX-v1.md)  
Knowledge base: [ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md](ISEO-SU-PRODUCTION-ARCHITECTURE-KNOWLEDGE-BASE-v1.md)

---

## Boundary summary

| Zone | Boundary |
|------|----------|
| Physical `.html` / handlers | Static/PHP file wins when present |
| Missing path | WordPress rewrite |
| Homepage `/` | WP route + hardcoded template (static-like) |
| `home.html` / `blog.html` | Parallel only |
| Blog posts | WordPress content + ACF |
| `/tariff-calc` | Hybrid (WP+ACF+JS+handlers) |
| `/offers` + CPT `offer` | WordPress commercial proposals |
| Shared `css/` `js/` | Shared; consumed by both sides |
| `report-hub/` | Sibling external surface |

## Ownership rules of thumb

1. If a physical file exists at the request path → static/PHP file wins (Apache + WP `!-f`).
2. If no file/dir → WordPress front controller.
3. `.html` may execute PHP — do not assume “pure static”.
4. Do not edit theme chrome assuming it updates all marketing HTML (and vice versa).
5. Do not call every PHP-rendered page “WordPress content” — check template vs editor vs ACF.

---

*Boundary map v1 · updated architecture capture 2026-07-24.*
