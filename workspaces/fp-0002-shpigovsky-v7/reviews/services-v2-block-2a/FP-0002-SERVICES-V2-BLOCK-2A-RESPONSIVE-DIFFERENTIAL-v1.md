# FP-0002 — Services V2 Block 2A Responsive Differential v1

**Date:** 2026-06-26

| Viewport | Check | Result |
| -------- | ----- | ------ |
| 320 | implied via 390 base | no overflow at 390 |
| 390 | full page | overflow false (373/390) |
| 430 | inherits ≤1024 mobile rules | pass |
| 768 | ≤1024 stack | pass |
| 1024 | breakpoint edge | mobile rules active |
| 1025 | desktop grid gallery | pass |
| 1280 | container width | pass |
| 1398 | reference desktop | overflow false (1381/1398) |
| 1440 | decor crop | pass |
| 1920 | decor absolute | pass |

## Mobile differential (vs desktop)

| Area | Mobile behavior |
| ---- | --------------- |
| Head | marker + copy row preserved; tighter gap |
| Lead | full width, red bar retained |
| Service head | column stack; leader hidden |
| Gallery | single column, 220px height |
| CTA | full width max 334px |
| Decor | reduced opacity/size |

## Overflow

Horizontal overflow at 390 and 1398: **0**
