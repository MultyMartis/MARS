# FP-0002 — Home Style Audit Final Recommendation v1

**Audit ID:** `home-style-baseline-01`  
**Authority:** `f5a9ecd7`  
**Date:** 2026-06-26

---

## A. Executive conclusion

**The Home page at operator baseline `f5a9ecd7` is a sufficient visual and component baseline for Services General planning**, with proven partial reuse already live on `uslugi.html`. The monolithic `style.scss` documents a stable container, color, typography, card, and responsive system. Gaps are **page-composition and inner-hero mapping**, not missing global tokens.

Home is **not** a complete pattern library name-wise (`.home-*` prefixes remain), but functionally it already feeds Services.

---

## B. Canonical factual rules (short list)

1. Container **1230px** max; gutters **30px** desktop, **15px** at ≤1024.  
2. Section vertical rhythm **50px** (`--pad-y`) on all breakpoints.  
3. Primary layout split **1024 / 1025** (CSS + JS).  
4. Body **Inter 300** @ 18/24; headings weight **400**; H2 **36/36**.  
5. Accent **rgb(179,38,30)**; page bg **rgba(218,229,240,0.7)**.  
6. Radius **30px** surfaces; buttons **pill** + CSS uppercase.  
7. Outline card family: **1px primary border**, transparent fill.  
8. Dark bands: primary text color bg + inverse type + optional bg image @ 10% opacity.  
9. Lead pattern: **5px left accent bar** (see `.rehub-universal-decor`).  
10. All SCSS in **`style.scss`**; behavior hooks via **`data-*`**.  
11. Buttons: **`.btn` / `.btn_dark` / `.btn--primary`**.  
12. Russian copy uses **`&nbsp;`** in HTML — preserve in reuse.

---

## C. Reusable sections (whole partials)

**Proven on Services (`uslugi.html`):**

- `home-rehabilitation-program.html`
- `home-founder-quote.html`
- `home-comfort.html`
- `home-faq.html`
- `home-final-form.html`

**High confidence for Services General mock:**

- `home-treatment-prevention.html` (category accordion)
- `hero-inner.html` (inner page hero — not yet on uslugi stub)

**Conditional:**

- `home-feature-grid.html`, `home-reviews.html`, `home-specialists.html`, `home-videos.html`

---

## D. Reusable patterns (internal — do not rename yet)

- Section head: H2 + uppercase “all” link + FA play icon  
- Lead accent bar (`.rehub-universal-decor` / section `__lead`)  
- Outline card + 3-col grid (feature-grid / recovery-intro cards)  
- Service link row (treatment `__service-item` grid)  
- Dark CTA band (requirements + final form)  
- Swiper + shared pagination bullets  
- Accordion (`data-accordion` single-open)  
- Fancybox gallery/video bindings  

---

## E. Home-only sections

- `.hero.hero--home` (full viewport home hero)  
- `.home-recovery-intro` (entire brand intro + 6 cards)  
- `.home-recovery-life` (stages + background narrative)  
- `.home-why-us` (until service-list coupling refactored)  
- Sequential photo bands as Home story (staff + landscape) unless mock requires  

---

## F. Classes not to rename

All `.home-*` BEM trees currently on Home and `uslugi.html`; `.hero*`, `.btn*`, `.container`, layout/modal classes; `.rehub-universal-decor`; `.block-whith-red-line` (typo preserved until operator renames).

---

## G. Safe extraction order

1. Services General **design-to-source mapping** (read-only plan)  
2. Add **inner hero** to Services page  
3. Add **treatment accordion** (or mock-equivalent) with new copy  
4. Reorder/extend `uslugi.html` to match mock — keep existing five partials  
5. Optional: alias lead bar on new sections only  
6. Optional: alias card grid if mock confirms  
7. **No** mass `.home-*` rename until Services page operator-approved  

---

## H. Risks

| Risk | Mitigation |
|------|------------|
| Over-abstraction | Reuse partials first; alias classes only with second proven use |
| Style duplication | Extend grouped SCSS selectors (already used for heads/pagination) |
| Selector collision | Do not introduce global short names without namespace |
| Home regression | No Home edits during Services build; test Home after each include |
| Source drift | Build from `f5a9ecd7` tag; resolve WIP typo/radius separately |
| Responsive mismatch | Verify recovery-life stages + program direction on mobile during planning |

---

## I. Gate recommendation

```text
READY_FOR_SERVICES_GENERAL_PLANNING
```

**Rationale:** Visual baseline documented; five Services partials already proven; PNG mock available; inner hero and accordion gaps are planning work, not baseline blockers.

---

## J. Exact next task

```text
Task:
FP-0002 V7 — Services General Page Design-to-Source Mapping and Build Plan

Required inputs:
- Spig_v1.2.fig (reference)
- 26.06.2026/Услуги общая PNG pair
- This audit pack (home-style-baseline-01)
- uslugi.html current stub @ f5a9ecd7

Source changes allowed:
NO (planning document only)

Expected outputs:
- Block-level PNG → partial mapping
- Reuse vs new-build decision per block
- Mobile override notes
- Implementation sequence (still no code until authorized)

Services implementation allowed:
NO
```

---

*End of final recommendation v1.*
