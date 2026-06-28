# FP-0002 — Services General Final Build Plan v1

**Planning ID:** `services-general-01`  
**Date:** 2026-06-26  
**Gate document:** consolidates all `services-general-01/` planning artifacts

---

## A. Executive conclusion

**Services General Pass 1 implementation may begin** after operator source checkpoint is committed. Planning identifies proven reuse for 5 existing partials, one parameterized hero, and one new category-hub pattern (×4 instances). Asset exports and categories 2–4 copy are **SAFE_UNKNOWN** but **do not block** Phase 1–2 (shell + hero + section reorder).

---

## B. Target page order

1. Header  
2. Inner hero — «Лечение и профилактика»  
3. Category hub — Зависимости и пристрастия  
4. Category hub — Психическое здоровье  
5. Category hub — Расстройства пищевого поведения  
6. Category hub — Генотипирование  
7. Program directions (`home-rehabilitation-program`)  
8. Founder quote (`home-founder-quote`, variant A)  
9. Comfort gallery (`home-comfort`)  
10. FAQ (`home-faq`)  
11. Final form (`home-final-form`)  
12. Footer  
13. Modal (consultation)

*Optional mid-page CTA band — defer until operator confirms on PNG.*

---

## C. Exact reuse

- `home-rehabilitation-program.html`
- `home-founder-quote.html` (variant A)
- `home-comfort.html`
- `home-faq.html`
- `home-final-form.html`
- `layout/header.html`, `layout/footer.html`, `modal-consultation.html`

---

## D. Parameterized reuse

| Partial | Parameters |
|---------|------------|
| `hero-inner.html` | `heroImage`, `heroWidth`, `heroHeight`, `heroTagline`, `heroTitle` |
| `home-rehabilitation-program.html` | `programHeading` |
| `home-founder-quote.html` | `modalSource`, `founderQuoteModifierClass` |
| `home-final-form.html` | `leadSource` |
| `home-faq.html` | *(future)* `faqHeading` |

---

## E. Pattern reuse

- Service list rows — structure from `.home-treatment-prevention__service-*`  
- Section head + «all link» — from program/comfort head  
- Lead accent — `.rehub-universal-decor` / `.block-whith-red-line` where mock shows red bar  
- Dark CTA band — pattern from `.home-rehabilitation-requirements__cta-band` if confirmed  
- Buttons — `.btn.btn_dark.btn--primary`

---

## F. New unique blocks

- **Services category hub** — expanded category section with 3-image gallery (×4)  
- **Services hero assembly** — new include wiring only (partial exists)

---

## G. Files plan

| File/path | Action | Reason | Home impact |
| --------- | ------ | ------ | ----------- |
| `src/pages/uslugi.html` | Modify | Correct section order; add hero + hubs | None if Home untouched |
| `src/partials/sections/services-category-hub.html` | Create | New category block | None |
| `src/scss/style.scss` | Append scoped rules | Hero already exists; hub + page scope | **Risk** — must not alter Home selectors |
| `src/partials/sections/home-*.html` | **Do not modify** Pass 1 | Reuse via includes | Protected |
| `src/pages/index.html` | **Do not modify** | Home protected | — |
| `src/js/main.js` | **No change expected** | Existing hooks sufficient | — |
| `foundation/FP-0002-V7-OPERATIONAL-STATUS.md` | Update status | Planning complete | — |

---

## H. Asset plan

Export from Figma / INCOMING before final QA:

- 1× Services hero interior  
- 12× category gallery images (3 per category × 4)  
- 1× optional watermark graphic  

Reuse existing program, founder, comfort assets.

---

## I. Responsive plan

- Desktop ≥1025: container 1230, gutters 30px, category gallery 3-col  
- ≤1024: gutters 15px, hero auto height, gallery 1-col, founder stack  
- ≤390: verify type scale and messenger/header rules (site-wide)  
- Mobile PNG order authoritative

---

## J. Universalization plan

**None in Pass 1.** Do not create global/shared section classes until second page needs them. Keep `.home-*` on Home; use `.services-category-hub*` on Services.

---

## K. Protected Home boundaries

- `src/pages/index.html` — no edits  
- All Home partials — no structural edits  
- `.home-founder-quote--variant-b` rules — operator-canonical (including photo `border-radius`)  
- `.home-recovery-intro` heading typo fix — operator-canonical  
- No mass rename; no search/replace on `.home-*`

---

## L. Build/QA plan

Widths: **1440, 1230, 1024, 767, 390, 320**  
Checks: section order, hero inner height, category gallery, Fancybox on comfort, FAQ accordion, form submit UI, header active state  
Compare: PNG desktop + mobile side-by-side  
Home smoke: `index.html` unchanged render vs operator baseline

---

## M. Rollback strategy

1. Git revert Services-only commits  
2. Or restore ZIP `FP-0002-V7-OPERATOR-DELTA-BEFORE-SERVICES-PLANNING-01-SOURCE.zip`  
3. Rollback boundary: anything after operator checkpoint commit affecting `uslugi.html`, new partials, Services SCSS block

---

## N. Operator decisions

| # | Decision | Blocking? | Default if deferred |
|---|----------|-----------|---------------------|
| 1 | Program H2: keep current param vs PNG title | No | Keep current param |
| 2 | Comfort H2: «приватность» vs «анонимность» | No | Keep source string Pass 1 |
| 3 | FAQ H2: «Нас часто спрашивают» vs «ОТВЕТЫ НА ВОПРОСЫ» | No | Keep source Pass 1 |
| 4 | Mid-page CTA band — include or omit | No | Omit Pass 1 |
| 5 | Category 2–4 service lists — content source | Partial | Empty/minimal until Figma text export |
| 6 | Asset export batch — before or during implementation | No | Parallel with Phase 3 |

---

## O. Gate recommendation

```text
READY_FOR_SERVICES_GENERAL_IMPLEMENTATION_WITH_SAFE_UNKNOWNS
```

SAFE_UNKNOWNs listed in §N do not block Phase 1–2.

---

## P. Exact next task

```text
FP-0002 V7 — Services General Page Implementation Pass 1
```

**Scope:** Phase 1–2 only — `uslugi.html` shell, inner hero, correct reuse section order.  
**Out of scope:** Category hub partial, asset exports, Home changes, universalization.

---

*End of final build plan v1.*
