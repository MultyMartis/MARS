# FP-0002 V9-03G Fixed Controls Audit v1

**Phase:** V9-03G  
**Date:** 2026-07-02

## Fixed viewport controls inventory

| Control | Selector / hook | Position | z-index | Desktop offset | Mobile offset | Notes |
|---------|-----------------|----------|---------|----------------|---------------|-------|
| Consultation modal | `.modal-consultation`, `[data-modal="consultation"]` | fixed inset 0 | **1200** | centered overlay | full viewport | Highest product layer |
| Modal overlay | `.modal-consultation__overlay` | absolute inset 0 | (within modal) | — | — | Captures background clicks |
| Off-canvas menu | `.offcanvas`, `[data-offcanvas]` | fixed inset 0 | **1000** | full viewport | full viewport | Below modal |
| Page overlay (legacy) | `.page_overlay` | fixed inset 0 | **100** | — | — | Low legacy layer |
| Sticky/fixed header | `.site-header` | static/sticky per breakpoint | section-local | — | mobile bar | Not a floating action |
| Fancybox gallery | `.fancybox__container` | fixed (plugin) | plugin high | — | — | Above scroll-to-top |
| **Scroll-to-top (new)** | `.scroll-to-top`, `[data-scroll-to-top]` | fixed bottom-right | **900** | 15px right/bottom + safe-area | 10px right/bottom + safe-area | Below modal/offcanvas |

## Stacking relationship

```
modal-consultation (1200)
  └── overlay + dialog
offcanvas (1000)
fancybox (plugin — above 900)
scroll-to-top (900)  ← new
page_overlay (100)
page content
```

## Collision assessment

| Risk | Mitigation |
|------|------------|
| Scroll-to-top above modal | z-index 900 < 1200; modal overlay intercepts clicks |
| Scroll-to-top above offcanvas | z-index 900 < 1000 |
| Footer link overlap | Fixed bottom-right with 15px/10px inset; compact 48px/44px control |
| Modal close control overlap | Modal centered; scroll-to-top corner-positioned |
| Gallery overlap | Fancybox owns overlay layer above 900 |

## Placement decision

- Shared partial: `src/partials/components/scroll-to-top.html`
- Included once via `footer.html` after `.site-page-shell` closes
- Outside modal DOM (`global-consultation-modal.html` unchanged)
- Exactly one emission per route (via shared footer include)

## Modal runtime protection

- No changes to modal HTML, SCSS block 10b, or modal JS (`bindModalSystem` / Triumph runtime)
- Scroll-to-top does not use `is-modal-scroll-locked` or modal helpers
