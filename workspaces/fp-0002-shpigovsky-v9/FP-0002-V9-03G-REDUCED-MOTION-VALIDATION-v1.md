# FP-0002 V9-03G Reduced Motion Validation v1

**Phase:** V9-03G

## Scroll-to-top reduced-motion contract

| Behavior | Normal motion | Reduced motion |
|----------|---------------|----------------|
| Scroll on click | `behavior: 'smooth'` | `behavior: 'auto'` |
| Show/hide transition | opacity/visibility fade (~0.3s) | suppressed via `@media (prefers-reduced-motion: reduce)` on `.scroll-to-top` |
| Button presence | retained | retained |
| Threshold logic | 500px | 500px (unchanged) |

## JS detection

```javascript
window.matchMedia('(prefers-reduced-motion: reduce)')
```

Used in `initScrollToTop` click handler.

## Protected systems (unchanged)

| System | Reduced-motion handling |
|--------|-------------------------|
| Modal (V9-03F) | existing block — transitions disabled |
| Section reveal (V9-03B) | immediate reveal fallback |
| Fancybox | existing reduced-motion overrides |
| Button hover | no transform lift (color only) |

## Operator check

Enable OS reduced motion → verify instant scroll-to-top on click and minimal show/hide motion.
