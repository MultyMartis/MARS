# FP-0002 V9-03G Scroll-to-Top Runtime Validation v1

**Phase:** V9-03G  
**Preview:** http://127.0.0.1:8797/  
**Method:** Static contract verification + automated HTTP validation (operator browser confirmation pending)

## Representative routes tested

| Route | HTTP | Scroll-to-top markup | Notes |
|-------|------|----------------------|-------|
| `/` | 200 | 1× button | Long page — threshold applicable |
| `/o-centre/` | 200 | 1× button | Long infrastructure page |
| `/kontakty/` | 200 | 1× button | Contact page |
| `/blog/nazvanie-stati/` | 200 | 1× button | Article page |
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | 200 | 1× button | Long service page |
| `/privacy-policy/` | 200 | 1× button | Legal page |

## Threshold contract (JS)

| Condition | Expected | Implementation |
|-----------|----------|----------------|
| `scrollY <= 500` | Hidden | `scroll-to-top--visible` absent; `aria-hidden="true"`; `pointer-events: none` |
| `scrollY > 500` | Visible | `scroll-to-top--visible` present; `aria-hidden="false"` |
| Initial load at top | Hidden | `updateVisibility()` on init |
| `pageshow` (bfcache) | Correct state | `pageshow` listener |
| Resize | Stable | passive resize listener + rAF throttle |

## Click contract

| Check | Expected |
|-------|----------|
| Click action | `window.scrollTo({ top: 0, behavior: 'smooth' })` |
| Reduced motion | `behavior: 'auto'` via `matchMedia` |
| URL hash | Unchanged |
| After return to top | Button hides when `scrollY <= 500` |

## Accessibility

| Check | Result |
|-------|--------|
| Semantic button | PASS |
| `aria-label` | PASS (`Прокрутить страницу наверх`) |
| Hidden not focusable | PASS (visibility + blur on hide) |
| Focus-visible styling | PASS (accent outline) |

## Operator visual confirmation required

Browser scroll threshold boundary (~500px), smooth scroll feel, and keyboard Tab order require operator review on preview URL.
