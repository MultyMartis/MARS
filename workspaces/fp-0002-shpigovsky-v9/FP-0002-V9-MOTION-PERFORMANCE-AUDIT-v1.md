# FP-0002 V9 — Motion Performance Audit v1

**Phase:** V9-03A

| Metric | Value |
|--------|-------|
| CSS size | ~570 KB (compiled, incl. FA) |
| JS size | ~38 KB |
| New dependencies | None |
| Animated properties | Primarily `opacity`, `transform` |
| Scroll handlers | None added |
| Observer | Single `IntersectionObserver`, unobserve after reveal |
| Global `will-change` | Not added |
| `transition: all` | Removed from `.reviews__card` (pre-existing) |

**Result:** PASS — no heavy library; observer count bounded by `[data-reveal]` elements.
