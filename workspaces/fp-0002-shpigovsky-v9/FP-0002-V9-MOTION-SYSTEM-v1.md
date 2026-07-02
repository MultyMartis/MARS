# FP-0002 V9 — Motion System v1

**Phase:** V9-03A  
**Scope:** Canonical static frontend motion contract for Forge reproduction

## CSS tokens (`:root` in `src/scss/style.scss`)

| Token | Value | Use |
|-------|-------|-----|
| `--motion-fast` | `0.2s` | Rare fast micro-states |
| `--motion-base` | `0.3s` | Hover, focus, UI panels |
| `--motion-reveal` | `0.7s` | Scroll reveal |
| `--motion-preloader` | `0.45s` | Preloader fade |
| `--ease-standard` | `cubic-bezier(0.4, 0, 0.2, 1)` | Default |
| `--ease-emphasized` | `cubic-bezier(0.2, 0, 0, 1)` | Reveal transform |
| `--reveal-distance` | `20px` | Reveal travel |
| `--reveal-stagger-step` | `80ms` | Group stagger increment |

Legacy aliases preserved: `--transition-base` maps to motion base.

## Reveal data contract

| Attribute | Role |
|-----------|------|
| `data-reveal` | Element enters with opacity + translateY when intersecting |
| `data-reveal-group` | Parent; children with `data-reveal` receive capped stagger |
| `data-reveal-delay` | Reserved; not required in V9-03A (stagger via group) |

### JS classes

- `html.js-enabled` — set in head (JS active)
- `html.js-reveal-ready` — set before hidden reveal state applies
- `.is-revealed` — applied once when visible

### No-JS safety

Without `js-reveal-ready`, `[data-reveal]` elements remain visible (no hiding CSS).

### Fail-safe

`initRevealAnimations` reveals all targets after 8s if observer fails.

## Preloader contract

| Hook | Purpose |
|------|---------|
| `data-preloader` | Root overlay |
| `data-preloader-line` | Progress line width |
| `html.is-preloader-active` | Visible + scroll lock |
| `sessionStorage fp0002_preloader_session` | Once per session |

## Reduced motion

`@media (prefers-reduced-motion: reduce)` disables reveal transform, hover lifts, preloader/modal/offcanvas transitions.

## Restraint by page type

- **Home / services / O-Centre:** section `data-reveal` on major blocks; card groups staggered.
- **Blog article:** no body-section reveals; related block only.
- **Legal:** single document container reveal.
- **Hero / above-fold:** no reveal on hero.

## JS initializers (`src/js/main.js`)

- `initPreloader()` — IIFE at file top
- `initRevealAnimations()` — IIFE after preloader
