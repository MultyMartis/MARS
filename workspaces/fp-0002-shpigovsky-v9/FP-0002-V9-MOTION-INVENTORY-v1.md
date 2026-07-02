# FP-0002 V9 — Motion Inventory v1

**Phase:** V9-03A

## Interactive — HOVER_REQUIRED / FOCUS_REQUIRED

| Component | Hover | Focus |
|-----------|-------|-------|
| `.btn` | color/bg/border, translateY(-1px) | `:focus-visible` outline |
| `.site-header__nav-link` | existing color | existing |
| `.site-footer__legal-link` | color | outline |
| Cards (blog, review, home-articles, related) | lift -3px, image scale 1.02 | link focus inherited |
| Modal close | bg | outline |
| Offcanvas controls | existing | existing |
| Accordion toggles | icon rotate (existing) | button focus |
| Form fields | border (existing) | visible focus |

## Reveal — REVEAL_SECTION

Major `<section data-reveal>` in partials (51 sections); hero excluded.

## Reveal — REVEAL_GROUP

| Group | Container |
|-------|-----------|
| Blog archive cards | `.blog-archive__grid` |
| Reviews archive | `.reviews-archive__list` |
| Home articles | `.home-articles__grid` |

## NO_ANIMATION / RESTRAINED

| Area | Policy |
|------|--------|
| Hero | NO_ANIMATION |
| Blog article body | NO_ANIMATION |
| Blog conclusion/sources | NO_ANIMATION |
| Legal H2 blocks | Single container reveal only |
| Modal hidden content | NO_ANIMATION until open |
| Accordion hidden panels | opacity fade only |

## EXISTING_ANIMATION_PRESERVE

- Swiper carousels
- Fancybox
- Accordion `aria-expanded` + `hidden` semantics

## REDUCED_MOTION_DISABLE

All reveal transforms, stagger, card hover lifts, preloader line animation.
