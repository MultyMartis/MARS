# FP-0002 V7 Visual Baseline — Pre-Final Polish Stable

**Release:** `FP-0002-V7-PRE-FINAL-POLISH-OPERATOR-STABLE-01`  
**Captured:** 2026-06-24

## Pages

| Page | Dist path | Status |
|------|-----------|--------|
| Home | `dist/index.html` | PRESENT |
| Services | `dist/uslugi.html` | PRESENT |

## Responsive overflow baseline (pre-polish)

| Viewport | Home overflow | Services overflow |
| -------- | -------------: | ----------------: |
| 320 | 0 | 0 |
| 390 | 0 | 0 |
| 768 | 0 | 0 |
| 1024 | 0 | 0 |
| 1025 | 0 | 0 |
| 1398 | 0 | 0 |

## Known visual characteristics at freeze

| Surface | Note |
|---------|------|
| Gallery captions | Overlay on image (`position: absolute`) — **known defect** |
| Recovery life mobile | Single-column stack — RESPONSIVE_DERIVED, not exact mobile Figma |
| Section vertical rhythm | `main > section` uses `var(--pad-y)` after Phase 4A |
| Head SEO copy | Technically complete; marketing review pending |
| Favicon / OG | Paths valid; visual review pending |
| Services unique blocks | Not implemented (intentional REUSE_ONLY) |

## Functional baseline

```text
Gallery Swiper = 1
Reviews Swiper = 1
Specialists Swiper = 1
Comfort Fancybox = ACTIVE
FAQ = ACTIVE
Modal = ACTIVE
Final form = PRESENT
```

## Reference captures (prior phases)

- `reviews/package-001/spacing-cleanup/implementation/`
- `reviews/package-001/recovery-life/implementation/`
- `reviews/package-001/content-corrections/implementation/`
