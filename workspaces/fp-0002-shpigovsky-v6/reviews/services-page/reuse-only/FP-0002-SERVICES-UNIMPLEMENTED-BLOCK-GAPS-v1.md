# FP-0002 Services Unimplemented Block Gaps v1

**Date:** 2026-06-23  
**Page:** `src/pages/uslugi.html` (reuse-only mode)  
**Authority:** Hard gate from `FP-0002-SERVICES-EXACT-REUSE-MATRIX-v1.md`

## Gaps

| Position | Mockup block | Why not reused | Required next task |
| -------- | ------------ | -------------- | ------------------ |
| 2 | Service Hero | NO_MATCH vs `hero.html` — mockup requires breadcrumbs, eyebrow, body copy, overlay-in-image composition; home hero is site-name H1 without breadcrumbs | Implement as **new block** only after operator approves dedicated DOM spec OR an existing partial reaches EXACT_100/SAME_DOM |
| 3 | Зависимости и пристрастия | NO_MATCH vs `home-treatment-prevention.html` — mockup uses indexed section + topic articles + 3 image cards + CTA; home uses accordion with link list only in panel 1 | One-block implementation from approved mockup; **no approximate reuse** |
| 4 | Психическое здоровье | NO_MATCH — home accordion panel 2 is empty; mockup needs full section with cards and topics | One-block implementation after operator charter |
| 5 | Расстройства пищевого поведения | NO_MATCH — home accordion panel 3 empty; mockup layout is standalone section | One-block implementation after operator charter |

## Currently implemented on `/uslugi/` (reuse-only)

| Position | Block | Partial |
| -------- | ----- | ------- |
| 1 | Header | `partials/layout/header.html` |
| 6 | Program | `partials/sections/home-rehabilitation-program.html` |
| 7 | Founder quote | `partials/sections/home-founder-quote.html` |
| 8 | Comfort | `partials/sections/home-comfort.html` |
| 9 | FAQ | `partials/sections/home-faq.html` |
| 10 | Final form | `partials/sections/home-final-form.html` |
| 11 | Footer | `partials/layout/footer.html` |
| — | Modal | `partials/components/modal-consultation.html` |

**Visual incompleteness is intentional and correct** until gaps 2–5 pass hard gate.
