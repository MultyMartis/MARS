# Forge WordPress — Slider / Carousel Standard v1

**ID:** FW-S-16  
**Status:** ACTIVE — PRODUCTION PROVEN WITH CAVEATS  
**Date:** 2026-08-18  
**Class:** A / F / H  
**Evidence:** FP-0002 P08 mobile nav; P13 trackpad / Swiper mousewheel

---

## 1. Input matrix

| Input | Expected |
|-------|----------|
| Mouse drag | Horizontal slide where designed |
| Touch | Horizontal swipe; vertical page scroll preserved |
| Trackpad | Horizontal gesture slides; **vertical** scroll not captured (`forceToAxis`, `releaseOnEdges` on Swiper mousewheel) |
| Keyboard | If dots/arrows exist, focusable; Hero may be autoplay-only per design |
| Reduced motion | Autoplay off or minimized |

---

## 2. Responsive chrome

| Viewport | Non-Hero | Hero |
|----------|----------|------|
| ≤767 | Prev/next (often left-aligned); dots optional/hidden | Follow design; often **exclude** generic prev/next helper |
| ≥768 | Dots; prev/next hidden unless design says otherwise | Independent |

Mark Hero with a dedicated data hook so shared slider-nav helpers **do not** attach.

---

## 3. Ownership

- **Swiper** owns sliding. Do not add `scrollBy` on the same axis (Factory anti-pattern).
- One init path; selectors via `data-*`.
- Physical device QA required for touch + iOS + MacBook trackpad ([REAL-DEVICE-QA](FORGE-WORDPRESS-REAL-DEVICE-QA-STANDARD-v1.md)).

---

*FW-S-16 v1.*
