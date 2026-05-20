# Reference workspace QA flow v1 (Wave 4)

**Default entry (Wave 5):** [operational-qa-entry-v1.md](operational-qa-entry-v1.md) — use this file for the checklist body below.

**Status:** **documented** — **compact human** QA for `website-factory-reference-v1` or client workspaces cloned from it.  
**Not:** full Forge checklist catalog; **not** automated QA product.

**Target time:** ~15 minutes after `npm run build`.

---

## Setup

| Step | Command / action |
|------|------------------|
| Build | `npm run build` — record PASS/FAIL in REPORT |
| Open | `dist/index.html` — browser DevTools device toolbar |

---

## Viewport passes

### 375px (mobile)

- [ ] No horizontal scroll on `body` / `main`
- [ ] Hero H1 readable; CTA min-height ≥ 44px
- [ ] Pricing cards stack; featured tier order sensible
- [ ] Form fields single column; labels visible
- [ ] Sticky CTA: appears after scroll past hero; does not cover focused input

### 768px (tablet)

- [ ] Proof metrics grid — 3 col or graceful 1 col
- [ ] Pricing: 3 columns if space allows
- [ ] Contact: two-column or stacked without overlap

### Desktop (≥1024px)

- [ ] Container max-width centered
- [ ] CTA bands centered; no orphaned short lines
- [ ] Header sticky does not obscure hero H1 on load

---

## Interaction passes

| Area | Check |
|------|-------|
| **Modal** | Open from hero, pricing featured, sticky; ESC closes; body scroll restored |
| **Form** | Required validation; submit shows status; no double submit on rapid click |
| **Sticky** | Shows/hides on scroll; destroy demo does not leave ghost bar |
| **Links** | `tel:` / `mailto:` on contact block work |

---

## Replacement pass (if section work in session)

- [ ] `destroySection` before swap documented
- [ ] Post-swap modal CTA works
- [ ] Form re-binds once (`__wfFormBound` not duplicated) — see swap demo

---

## Overflow & layers

- [ ] No clipped focus rings
- [ ] Modal backdrop covers page; sticky **below** modal
- [ ] Hero overlay does not block CTA clicks (`pointer-events` on overlay only)

---

## z-index spot check

| Element | Below modal? |
|---------|----------------|
| Header | Yes |
| Sticky CTA | Yes |
| Hero overlay | N/A (inside section) |

---

## REPORT line

```text
Verification: reference QA flow v1 — 375/768/desktop spot-check PASS | partial | SAFE UNKNOWN (npm/build)
```

*Wave 4 — compact reference QA.*
