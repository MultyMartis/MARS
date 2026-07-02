# FP-0002 V9-04 Scroll-to-Top Contract v1

**Date:** 2026-07-02

| Rule | Value |
|------|-------|
| Placement | Global template-part once per page (footer include) |
| Selector | `[data-scroll-to-top]` |
| Visible when | `scrollY > 500` |
| Hidden when | `scrollY <= 500` |
| Position | Fixed bottom-right |
| z-index | **900** (below offcanvas 1000, modal 1200) |
| Click | smooth scroll; `prefers-reduced-motion` → immediate |
| Modal interaction | Must not conflict with scroll lock |
| Admin bar | Verify offset in WP QA |

Authority: `src/partials/components/scroll-to-top.html`, `src/js/main.js` init block V9-03G.
