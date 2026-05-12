# Frontend QA — Triumph Manipulator Landing (v0)

**Method:** Manual QA narrative aligned with [qa-validation-model.md](../../qa-validation-model.md) frontend lane **intent** — **no** automated Lighthouse run claimed.

---

## 1. Layout

- Section spacing matches handoff rhythm; no accidental overlap of **sticky_cta** with footer CTAs.
- **Grid:** tile heights consistent where copy length varies (clamp or min-height policy).

---

## 2. Responsive

- No horizontal scroll at 375px except intentional tables (**none** planned).
- Touch targets **≥44px** where feasible for primary actions.

---

## 3. CTA

- Primary button same component variant in hero, final, sticky.
- **tel:** links include meaningful `aria-label` if icon-only (**decision** in build).

---

## 4. Accessibility

- **H1** single; heading levels not skipped.
- **FAQ:** keyboard open/close; focus trap **avoid** unless modal (prefer native `details`).
- Form: labels associated with inputs; errors announced (aria-live region **recommended**).

---

## 5. Trust consistency

- Claims in **cases** captions match visible image context.
- **trust_block** logos have alt text or `aria-hidden` if decorative per policy.

---

## 6. Mobile

- Virtual keyboard does not hide active input (scroll-into-view check).
- Sticky does not obscure focused form field.

---

## 7. Semantic structure

- `main`, `header`, `footer` landmarks.
- **FAQ** content visible in DOM for SEO (not JS-only injection).

---

## 8. Verdict (simulated)

**Pass with notes** — pending real build, real content, and legal review of claims.

---

*Frontend QA v0 — reference execution only*
