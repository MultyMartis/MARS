# FP-0002 — Services V2 Program Responsive Differential v1

| Viewport | Desktop Figma | Mobile Figma `1:4880` | Runtime |
| -------- | ------------- | --------------------- | ------- |
| 320 | 2×2 grid | stack | stack |
| 390 | 2×2 | stack | stack |
| 768 | 2×2 | stack | stack |
| 1024 | breakpoint | stack | stack @ ≤1024 |
| 1025 | 2×2 | — | 2×2 |
| 1398 | 2×2 | — | 2×2 |
| Item descriptions | visible | hidden | hidden @ ≤1024 |
| Head link | «подробнее» | hidden | desktop only |
| Foot link | hidden | «подробнее о программе» | mobile only |
| CTA layout | 3-col band | stacked | stacked @ ≤1024 |
| Horizontal overflow | 0 | 0 | probe `overflowX: false` |

Screenshots captured at 1398 and 390 for all required regions.

**Verdict:** **RESPONSIVE_DIFFERENTIAL_DOCUMENTED**
