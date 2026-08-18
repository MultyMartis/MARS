# Forge WordPress — Performance baseline v1

**ID:** FW-S-39  
**Status:** ACTIVE — OPERATIONS STANDARD  
**Date:** 2026-08-18  
**Does not:** require a specific PageSpeed score as a fake DoD.

**Rule:** Measure first. Do not optimize blindly. Do not install several plugins for the same concern.

---

## 1. Pre-launch checklist (inspect)

| Inspect | Ask |
|---------|-----|
| Page weight | HTML+CSS+JS+images+fonts+video on Home + one heavy inner page |
| Image dimensions | displayed size vs file; cards not using originals |
| Font loading | subset/WOFF2; `font-display`; no duplicate families |
| CSS/JS payload | unused vendor (full Swiper on pages without sliders?) |
| Render blocking | critical CSS optional; do not invent a second optimizer |
| Unused libraries | Fancybox/jQuery extra copies |
| Excessive DOM | accidental repeater explosion |
| Third-party scripts | analytics/chat — empty-safe; no double inject |
| Layout shift | images/fonts/embeds |
| Large video | [MEDIA](FORGE-WORDPRESS-MEDIA-ARCHITECTURE-STANDARD-v1.md) |
| Cache headers | host/CDN; not `no-store` on static assets in production |

Record numbers in the QA matrix. Fix the largest proven cost, not a blog-post ritual.

---

## 2. Performance ownership (one owner each)

| Concern | Typical owner | Collision |
|---------|---------------|-----------|
| Page cache | one host or one plugin | Autoptimize + WP Rocket + host cache + Cloudflare Polish fighting |
| Object cache | host Redis/none | two object-cache.php drops |
| Minification | same as page-cache plugin **or** build pipeline — **one** | |
| CDN | DNS/host | |
| Image optimization | one (host WebP **or** plugin **or** build) | |
| Browser caching | host/CDN headers | |

Default: **host cache + build-minified theme assets**. Extra optimization plugins need a WAD and a collision row in the plugin register.

---

## 3. Cache / generated-asset cutover purge

Domain or environment changes require an **exact purge**:

1. Page cache (plugin + host panel)  
2. Object cache if used  
3. Transients that store absolute URLs  
4. Generated CSS/JS (optimizer “used CSS”, critical CSS)  
5. Optimization plugin caches  
6. CDN purge  
7. Rewrite flush (`flush_rewrite_rules` / permalinks save)  
8. Browser cache note for operators (hard refresh is not a substitute for 1–6)  

Then smoke Home, one CPT, sitemap, Admin.

Tie this into [LAUNCH SOP](../runbooks/FORGE-WORDPRESS-PRE-CUTOVER-AND-LAUNCH-SOP-v1.md) after `home`/`siteurl` migrate.

---

*FW-S-39 v1.*
