# FP-0002 V9-03B — Button Hover Audit v1

**Phase:** V9-03B  
**Date:** 2026-07-02  
**Scope:** `src/scss/style.scss`, V9 motion block

## Summary

Operator correction: remove button lift/transform on hover; retain calm ~0.3s color transitions only.

## Affected selectors (corrected)

| Selector | Source | Previous behavior | Decision | Final behavior |
|----------|--------|-------------------|----------|----------------|
| `.btn` (hover block) | `style.scss` ~9194–9209 | `translateY(-1px)` on hover; `translateY(0)` on active; transform in transition | **Remove transform** | Color/border/box-shadow only via `var(--motion-base)` |
| `.btn:hover` (base) | `style.scss` ~606–610 | Color/border only | Keep | Unchanged |
| `.btn_dark:hover` | ~619 | Color/border only | Keep | Unchanged |
| `.btn--primary:hover` | ~632–637 | Color/border only | Keep | Unchanged |
| `.btn:active` | ~644–646 | `opacity: 0.92` | Keep | No movement |
| `.btn:focus-visible` | ~639–642 | Outline ring | Keep | Keyboard visible |
| `.btn:disabled` | ~648–653 | No pointer, opacity 0.5 | Keep | No animation |

## Non-button hover transforms (retained)

| Selector | Behavior | Decision |
|----------|----------|----------|
| `.blog-archive-card:hover` | `translateY(-3px)` | Retained — card, not button |
| `.review-archive-card:hover` | `translateY(-3px)` | Retained |
| `.home-articles__card:hover` | `translateY(-3px)` | Retained |
| `.blog-archive-card__image` scale | `scale(1.02)` on card hover | Retained — image inside card |

## Button-like controls verified (no transform added)

- `.founder-quote__cta` — color only
- `.final-form__submit` — inherits `.btn`
- `.modal-consultation__submit` — inherits `.btn`
- `.hero__button` — layout only
- Header/offcanvas CTAs — `.btn` system

## Reduced motion

`prefers-reduced-motion: reduce` — `.btn:hover` transform already forced to `none` in reduced-motion block; lift rules removed at source.
