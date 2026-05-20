# Production hardening rules v1 (Wave 5)

**Status:** **documented** — **edge-case survivability** for Gulp + vanilla Factory workspaces.  
**Not:** runtime monitoring, **not** automated enforcement, **not** governance expansion.

**Applies to:** client workspaces, reference, post-migration legacy.

---

## When to run

- Before **freeze** (Standard+).  
- After section **replacement** or foundation touch.  
- During [adoption-validation-flow-v1.md](adoption-validation-flow-v1.md).

Record gaps as **HARDENING FINDINGS** in REPORT (max 8 bullets).

---

## z-index collisions

| Rule | Fix pattern |
|------|-------------|
| Sections must not use literal `z-index: 999` | Use `_layers.scss` tokens only |
| Sticky CTA below modal | `$z-sticky-cta` < `$z-modal-backdrop` |
| Hero overlay does not block clicks | `pointer-events: none` on decorative overlay |
| Dropdowns in header | `$z-dropdown` — not above modal |

**Spot check:** open modal with sticky visible — sticky must not cover modal.

---

## Modal stacking

- One modal stack owner: `WfModal` / `js/core/modal.js`.  
- `data-modal-open` on `button[type=button]` — not nested forms.  
- ESC closes top modal; body scroll lock released.  
- Do not open second modal without closing first (HITL if product requires stack).

---

## Sticky edge cases

- Sticky CTA: register `sticky-cta` module; `destroy` removes bar + listeners.  
- iOS Safari: test `position: sticky` with address bar show/hide — **SAFE UNKNOWN** if not tested.  
- Sticky header + in-page anchor: hash scroll not hidden under header (padding-top on target or scroll-margin).

---

## Overflow edge cases

- `body { overflow-x: hidden }` is not a substitute for fixing wide children.  
- Cards/grids: `min-width: 0` on flex/grid children.  
- Modal open: verify no double scrollbar (body lock).  
- Long unbroken strings: `overflow-wrap: anywhere` on user content regions.

---

## Observer / resize cleanup

- Prefer `WfLifecycle.onResize` with returned `off` in `destroy`.  
- `IntersectionObserver` / `ResizeObserver`: disconnect in module `destroy`.  
- No new anonymous `window.addEventListener('resize')` in section files without teardown.

---

## Replacement cleanup

Per [section-survivability-implementation-v1.md](foundation-systems/section-survivability-implementation-v1.md):

1. `destroySection(root)` before DOM removal.  
2. Swap partial HTML; keep `data-section` + `data-block-id`.  
3. `initSection(root)` once — no duplicate `__wf*Bound` flags.  
4. Re-test modal + form bind on replaced section.

---

## Body-lock conflicts

- Only modal (or documented drawer) may set `document.body` overflow lock.  
- If mobile menu adds lock — must release when menu closes; never stack with modal lock.  
- After modal close: `overflow` restored (manual check on 375px).

---

## Form double-submit

- `form` module: disable submit during async; re-enable on error.  
- Rapid double-click: one in-flight request.  
- After `replaceSectionContent`: single bind — verify in DevTools or console flag.

---

## Mobile viewport quirks

- `viewport` meta present on all page entries.  
- `100vh` hero: prefer `min-height` + content-driven height where iOS bar breaks layout.  
- Touch targets ≥ 44px on primary CTAs (reference QA).  
- `:hover` styles must not be required for affordance on touch.

---

## REPORT line

```text
HARDENING: z-index/modal/sticky/overflow/cleanup — PASS | partial (list) | SAFE UNKNOWN (untested: iOS)
```

*Wave 5 — production edge-case prevention.*
