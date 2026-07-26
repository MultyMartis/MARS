# METALLKA — Cache Map v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26

```text
Do not purge.
```

---

## Actual layers

| Layer | Present? | Owner | Notes |
|-------|----------|-------|-------|
| Page cache plugin (WP Rocket / LSCache / etc.) | **NO** dedicated active page-cache plugin | — | |
| `advanced-cache.php` | **NO** | — | |
| `object-cache.php` | **NO** | — | |
| Redis / Memcached drop-in | **Not evidenced** | — | |
| Fast Velocity Minify | Plugin **inactive**; dirs `wp-content/cache/fvm` remain | PLUGIN (inactive) | Leftover cache files |
| Clearfy | **Active** HTML/asset optimization options | PLUGIN | Includes HTML optimize flags |
| Clearfy / WMAC cache dirs | `wp-content/cache/wmac/{js,css}` | PLUGIN | |
| The7 generated CSS | `wp-content/uploads/the7-css/` | THE7 | Dynamic CSS cache options exist (`the7_dynamic_css_cache`, etc.) |
| WPBakery generated assets | `wp-content/uploads/js_composer/` | WPBAKERY | |
| Hosting / nginx cache | **PARTIAL** — nginx front present; no explicit cache headers proving edge cache | HOSTING | No Cloudflare |
| CDN | **Not evidenced** | — | |
| OPcache | **SAFE UNKNOWN** (not inspected via panel) | — | |
| Browser / robots Cache-Control | `robots.txt` `max-age=604800` | HTTP | |

---

## Ownership summary

Primary active optimization owner: **Clearfy**.  
Theme CSS regeneration owner: **The7**.  
No Redis object cache. No `advanced-cache` drop-in.

---

*Cache Map v1.*
