# Reference workspace QA flow v1 (Wave 4)

**Default entry (Wave 5):** [operational-qa-entry-v1.md](operational-qa-entry-v1.md) — routes here for the checklist body.

**Status:** **documented** — **complete** compact human QA for `website-factory-reference-v1` or client workspaces cloned from it. **Not** a legacy stub; **not** full Forge checklist catalog; **not** automated QA product.

**Target time:** ~15 minutes after `npm run build`.

---

## Setup

| Step | Command / action |
|------|------------------|
| Build | `npm run build` — record PASS/FAIL in REPORT |
| Open | `dist/index.html` — browser DevTools device toolbar |

---

## RU commercial landings (mandatory)

When the landing primary locale is **Russian** (commercial Factory landing):

1. Run **[ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md)** at all required widths: **320 / 375 / 390 / 420 / 760 / 1180 / 1320 / 1440**.
2. Apply typography/overflow rules from **[russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md)** — no mid-word splits; no forbidden break CSS on UI.
3. Record in REPORT:

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
```

Generic viewport passes below are **supplementary** (interaction/layout); they **do not** replace the RU preset.

---

## Viewport passes (supplementary — interaction & layout)

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
- [ ] CTA bands centered; short-line widows acceptable at **word boundaries** — do **not** fix with `nowrap`, `&nbsp;` chains, or word-breaking CSS (see RU typography authority when locale is RU)
- [ ] Header sticky does not obscure hero H1 on load

**For RU commercial landings use:** [ru-landing-qa-preset-v1.md](ru-landing-qa-preset-v1.md) for authoritative typography QA widths.

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

Overflow fixes on RU landings **must** follow [russian-no-word-splitting-typography-v1.md](russian-no-word-splitting-typography-v1.md). Prefer layout/grid and `min-width: 0` before any word-breaking CSS.

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

## REPORT lines

Generic line — **supplementary generic responsive validation only** (not gating for RU commercial):

```text
Verification: reference QA flow v1 — 375/768/desktop spot-check PASS | partial | SAFE UNKNOWN (npm/build)
```

For **Russian commercial landings**, also include ( **required for QA PASS** ):

```text
RU TYPOGRAPHY / NO WORD-SPLITTING — PASS | partial (list) | FAIL | SAFE UNKNOWN (widths not tested)
```

*Wave 4 checklist body — stabilized Wave 5 with RU preset authority.*
