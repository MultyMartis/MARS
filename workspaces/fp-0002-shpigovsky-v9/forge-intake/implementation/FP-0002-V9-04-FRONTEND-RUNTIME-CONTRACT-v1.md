# FP-0002 V9-04 Frontend Runtime Contract v1

**Date:** 2026-07-02

## Compiled assets (stable hashes)

| Asset | Path | SHA-256 |
|-------|------|---------|
| CSS | `dist/assets/css/style.css` | F89FCB86A678C5FB4D4A94DB2E423095A23564B6C3BE19D7E39CF5AF0D30ABDE |
| JS | `dist/assets/js/main.js` | 19518C4BF86FBDA4FD5128D67EF00CBF7A2BDC6000A571B65D75BFA6AF27DB8A |

## Behaviors

| Feature | Status |
|---------|--------|
| Section reveal `[data-reveal]` | enabled |
| Button hover | color/border/shadow only |
| Modal | Triumph-derived V9-03F |
| Gallery Fancybox 5 | enabled |
| Offcanvas | `data-offcanvas` |
| Accordions | per-section |
| Scroll-to-top | V9-03G |
| Preloader | **absent** |
| Global page-load fade | **absent** |

## Enqueue

Theme owns compiled CSS/JS; version via theme version or filemtime; defer in footer; respect `prefers-reduced-motion`.

## Admin bar

Test fixed controls and scroll-to-top offset when logged in.
