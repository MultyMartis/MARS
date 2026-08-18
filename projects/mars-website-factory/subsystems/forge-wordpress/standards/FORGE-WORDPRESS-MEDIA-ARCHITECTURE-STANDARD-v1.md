# Forge WordPress — Media architecture standard v1

**ID:** FW-S-38  
**Status:** ACTIVE — CANONICAL DEFAULT  
**Date:** 2026-08-18  
**Evidence:** FP-0002 attachment IDs in ACF; galleries/Fancybox; local video caution; operator media in Library

---

## 1. Ownership

| Concern | Owner |
|---------|--------|
| Media Library objects | WordPress attachments (IDs) |
| Featured / portrait SoT | native featured image **or** one named ACF image — not both competing |
| Content images | editor / ACF image fields resolving IDs |
| Decorative theme chrome | theme assets (not client-editable unless designed) |

**Avoid absolute host URLs** in content when dynamic attachment resolution (`wp_get_attachment_image`, ACF image array/ID) is available. Hardcoded `https://staging…/wp-content/uploads/…` is a migration defect.

Preserve originals in uploads; do not overwrite masters with compressed derivatives.

---

## 2. Image sizes policy

Register **custom sizes only** when a layout actually needs them. Do not send huge originals to card contexts.

| Category | Typical use | Notes |
|----------|-------------|-------|
| thumbnail / card | lists, hubs, search | crop or soft proportional — per design |
| portrait | people/staff | often 3:4; match featured-image contract |
| hero | home/service heroes | large but capped; srcset |
| content | in-article | `content_width` aligned |
| gallery | Fancybox/source + thumb | two sizes, not original twice |

**Pixel dimensions remain design-dependent.** Categories are canonical; numbers belong in the project DESIGN-SYSTEM-MAP / IMPLEMENTATION-SPEC.

Use `srcset`/`sizes` via `wp_get_attachment_image`. Enable WebP/AVIF **only** through the chosen image-optimization owner ([PERFORMANCE-BASELINE](FORGE-WORDPRESS-PERFORMANCE-BASELINE-v1.md)) — not a second plugin.

Always output width/height or aspect-ratio to limit CLS. Lazy-load below-the-fold; **not** LCP hero if it delays paint.

Alt: required for informative images; empty alt for decorative.

---

## 3. SVG policy

| Rule | |
|------|--|
| SVG in Media Library | only through a **controlled** allowlist (capability + sanitization) |
| Untrusted SVG | treat as executable — default **deny** for client editors |
| Icon vs content image | icons: sprite or inline in theme; photos: raster |
| Inline SVG in templates | theme-owned; not pasted by editors into WYSIWYG |
| Sanitization | if upload allowed, sanitize; never `file_get_contents` into unescaped output |

---

## 4. Gallery

One gallery component owner (markup + CSS + Fancybox or equivalent). Group `data-fancybox` consistently. Do not mix a second lightbox.

---

## 5. Video policy

| Decision | Guidance |
|----------|----------|
| Local MP4 vs embed | Embed (YouTube/Vimeo/etc.) unless the brief requires owned file, autoplay background, or offline |
| Local file | no giant assets without explicit reason + poster |
| Poster | required for local/hero video |
| preload | `metadata` or `none` — not `auto` on mobile-heavy pages |
| autoplay | muted + `playsinline`; never unsound autoplay |
| mobile bandwidth | prefer embed or short muted loop; measure |
| fallback | poster + link if video fails |
| broken media | QA must include 404 poster/src |

---

*FW-S-38 v1.*
