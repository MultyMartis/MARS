# FP-0002 V8 O-Centre Accessibility Charter v1

**Date:** 2026-06-29

---

## Page-level

| Rule | O-Centre plan |
|---|---|
| One H1 | Single H1 in `services-inner-hero-v2` title (`OC-B01`) |
| `lang` | `ru` on `<html>` (layout default) |
| Main landmark | `<main>` wrapping page blocks (match services template) |

---

## Heading hierarchy

| Region | Levels |
|---|---|
| Hero | H1 (title) + eyebrow as `<p>` |
| Narrative bands | H2 per section; H3 in program items / steps |
| Program | H2 + H3 item titles |
| Specialists / Reviews / FAQ | H2 section headings |
| No skipped levels | H1 → H2 → H3 within each region |

---

## Landmarks and section labels

| Block | Element | `aria-labelledby` / label |
|---|---|---|
| Hero | `<section aria-labelledby="…titleId">` | title id param |
| Comfort | `aria-labelledby="comfort-heading"` | param |
| Specialists | `aria-labelledby="specialists-heading"` | param |
| Reviews | region label in partial | reuse |
| FAQ | `aria-labelledby="faq-heading"` | param |
| Staff/clinic bleed | `aria-label` if decorative band used | not staff-photo default |

---

## Images

| Type | Alt policy |
|---|---|
| Hero background | `alt=""` decorative (current inner-hero pattern) |
| Comfort gallery | `alt=""` if decorative; upgrade if semantic |
| Category gallery thumbs | Caption as visible text; alt empty unless semantic |
| Founder photo | Name in adjacent text — alt from founder partial |
| Specialist portraits | Names in card text — alt from partial |

---

## Gallery / Fancybox

| Item | Policy |
|---|---|
| Comfort tiles | Link text from `href` image; ensure keyboard focusable `<a>` |
| Fancybox group | `data-fancybox="comfort"` — single group per page |
| Captions | Fancybox caption from visible `figcaption` if wired |

---

## Buttons and links

| Control | Semantics |
|---|---|
| Hero CTA | `<button type="button">` + `data-modal-open` |
| Program CTA | Same modal pattern with `data-modal-source` unique per band |
| Subnav | `<a href="#…">` to section ids — must match heading ids |
| Phone links | `tel:` in CTA band where present |

---

## Forms

No dedicated About form on inventory — modal consultation only (`data-lead-form` in modal, not page).

---

## IDs

| Strategy | Rule |
|---|---|
| Page-scoped ids | Prefix: `o-centre-*` or block-specific (`who-we-treat-heading`) |
| Duplicate prevention | Run page-wide DOM gate after implementation |
| Accordion | Unique panel ids per FAQ instance |
| Swiper | No id on slides; pagination bullets decorative |

---

## ARIA

| Pattern | Model |
|---|---|
| Accordion | `aria-expanded`, `aria-controls` on FAQ buttons (existing `faq.html`) |
| Modal | Existing `modal-consultation` hooks |
| Subnav | `<nav aria-label="Разделы страницы">` — extend internal-page-nav label for About |

---

## Keyboard / motion

| Item | Plan |
|---|---|
| Accordion | Enter/Space on headers |
| Modal | Focus trap in existing modal |
| Swiper | Arrow keys via Swiper defaults |
| `prefers-reduced-motion` | Respect global SCSS / Swiper reduced motion |

---

## Result

**PASS_WITH_KNOWN_GAPS** — subnav `aria-label` and comfort `href="#"` need implementation fixes; BLK-036–038 heading ids pending partial design.
