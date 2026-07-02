# FP-0002 V9-04 Asset and Media Migration v1

**Date:** 2026-07-02

| Category | Destination |
|----------|-------------|
| Logo, UI SVG icons | Theme static `assets/images/` |
| Decorative patterns | Theme static |
| Hero/gallery editorial photos | Media Library |
| Blog inline images | Media Library in post content |
| Service photos | Media Library via ACF image fields |
| Fonts | Theme `assets/fonts/` (compiled from `src/fonts/`) |
| CSS/JS bundles | Theme `assets/css|js/` from build pipeline |
| Fancybox/Swiper | Bundled in main.js/CSS or vendor copies |

## Rules

- Do not upload every icon to Media Library.
- Preserve alt text from V9 markup.
- WebP where already emitted in dist; retain originals for editor upload.
