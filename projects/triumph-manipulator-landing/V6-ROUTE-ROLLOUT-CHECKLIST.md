# Triumph V6 Route Rollout Checklist

Use this checklist before every new rollout route.

## 1) Inputs

- [ ] ORCA semantic pack path is fixed for this route.
- [ ] Final website copy exists in the pack.
- [ ] Final website copy is explicitly separated from internal notes.

## 2) Create route

- [ ] Create `src/pages/{route}.html`.
- [ ] Copy canonical zakaz partials into `src/partials/sections/v5-ppc/{route}/`.
- [ ] Do not reuse existing scaffold partials from other target routes.

## 3) Page scope

- [ ] Set route `body[data-page-type]` correctly.
- [ ] Add route to required canonical CSS selector groups.
- [ ] Verify canonical CSS is applied to route sections.

## 4) Adapt content

- [ ] Hero.
- [ ] Specs.
- [ ] Tasks.
- [ ] Order steps.
- [ ] Pricing.
- [ ] FAQ.
- [ ] Contact form.
- [ ] CTA sources.

## 5) Forbidden checks

- [ ] No `.hero__notice`.
- [ ] No standalone `final-contact-cta` include.
- [ ] No ORCA/internal English operational wording in production copy.
- [ ] No changed fixed titles: `Что не перевозим`, `Частые вопросы`.
- [ ] Fixed-title verification normalizes HTML entities/nbsp: treat `Что не перевозим` and `Что не&nbsp;перевозим` as equivalent canonical forms (same principle for `Частые вопросы` if entity encoding appears).
- [ ] No duplicate `#contacts`.
- [ ] No mock form handlers.

## 6) Build checks

- [ ] `npm run build`.
- [ ] `dist/{route}.html` exists.
- [ ] `dist/index.html` still exists.

## 7) Marker checks

- [ ] `hero__cargo-action`.
- [ ] `machine-showcase__spec-panel`.
- [ ] `machine-transport--ops-grid`.
- [ ] `pricing-factors--system`.
- [ ] `order-steps--process`.
- [ ] `faq--split-cta`.
- [ ] `contact-cta--embedded`.

## 8) Visual QA

- [ ] 1440.
- [ ] 1280.
- [ ] 1025.
- [ ] 1024.
- [ ] 560.
- [ ] 390.

## 8A) ROUTE IMAGE QA

- [ ] Temporary baseline image allowed during rollout.
- [ ] Route-specific image required during image mapping pass.
- [ ] Verify `machine-showcase__media--index-baseline`.
- [ ] Verify alt text.
- [ ] Verify no stretched/cropped image behavior.

## 8B) POST-BUILD STRUCTURAL PARITY

- [ ] Compare route visually against canonical zakaz.
- [ ] Confirm no legacy layout drift.
- [ ] Confirm tasks cluster parity.
- [ ] Confirm proof-strip parity.
- [ ] Confirm FAQ/contact parity.

## 9) Calibration report

- [ ] What held.
- [ ] What broke.
- [ ] What was adapted.
- [ ] Whether rules need update.
