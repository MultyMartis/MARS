# Interaction & motion discipline v2

**Status:** production motion law. **Not** motion design philosophy or animation library.

**Pairs with:** [token-system-v2.md](token-system-v2.md) timing tokens, [interaction-intent-governance.md](../interaction-intent-governance.md) (Tier 3 QA vocabulary).

---

## 1. Allowed animation categories

| Category | Example | Max duration |
|----------|---------|--------------|
| **State feedback** | button hover, focus ring | `$duration-fast` (150ms) |
| **Disclosure** | accordion height, tab fade | `$duration-base` (250ms) |
| **Overlay** | modal backdrop fade | `$duration-base` |
| **Micro affordance** | icon chevron rotate | `$duration-fast` |
| **Sticky reveal** | CTA bar slide-in | `$duration-base` |

Use CSS `transition` on transform/opacity/box-shadow — not layout properties (`width`, `height`, `top`) except accordion with `grid`/`max-height` pattern.

---

## 2. Forbidden motion patterns

- Parallax scroll tied to `scroll` without reduced-motion guard.
- Auto-playing carousels without pause control.
- Infinite marquee text on conversion pages.
- Bounce/elastic easing on primary CTA.
- Page-enter animations blocking first paint.
- Multiple simultaneous scroll-triggered reveals.
- Blur filters animating on large areas (mobile GPU cost).

---

## 3. Duration & easing posture

```scss
// from token-system-v2
transition: opacity $duration-base $ease-standard,
            transform $duration-base $ease-standard;
```

| Use | Easing |
|-----|--------|
| Enter / open | `$ease-out` |
| Exit / close | `$ease-standard` |
| Hover | `$ease-standard` |

**Cap:** no interaction chain > 400ms total perceived delay.

---

## 4. Mobile degradation

Below `$bp-md`:

- Disable parallax and scroll-linked transforms.
- Replace slide-in sticky CTA with instant show/hide (`opacity` only).
- Reduce shadow transitions (paint cost).

```scss
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

## 5. Performance boundaries

- Animate only `transform` and `opacity` when possible.
- No `transition: all`.
- Max 3 concurrent animated elements per viewport.
- Sliders: use `scroll-snap` before heavy JS animation.

---

## 6. Scroll animation restraint

**Default:** no scroll-jacking. If handoff requires reveal-on-scroll:

- One shot per element (`IntersectionObserver` once).
- Unobserve after reveal in `destroy` path.
- No cumulative delay chains (stagger max 50ms × 3 items).

---

## 7. Overlay motion rules

- Backdrop: opacity only.
- Dialog: opacity + `translateY(8px)` → `0` — no scale bounce.
- Close faster than open (150ms vs 250ms optional).

---

## 8. Interaction hierarchy

When multiple handlers compete:

1. Modal open/close (blocks background)
2. Form submit lock
3. Accordion/tabs inside modal
4. Slider drag
5. Hover effects

Lower priority handlers must not fire while modal open (use `body.is-modal-open` guard in delegated click handler).

---

## 9. CTA interaction

- One clear `:focus-visible` style site-wide (token-driven).
- Hover must not remove contrast.
- Loading state: text change or spinner — no width collapse.

*Wave 2 — interaction/motion discipline.*
