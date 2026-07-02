# FP-0002 V8 O-Centre Hero Asset Decision v1

## Decision

**`EXPORT_CANONICAL`**

## Evidence

| Field | Value |
|---|---|
| Figma node | `1:2226` «image 13030403» |
| Figma frame size | 1400×628 (display crop) |
| Zip image hash (hex) | `c96ae5052d14489981804509c79bb86e1bb6eae1` |
| Exported evidence | `STORAGE/.../evidence/o-centre-hero-fig-c96ae505.jpg` |
| Evidence SHA-256 | `446930d62914c036de9027d421cb28c1bee39fef2672d9e63f239da108e7a527` |
| Production output | `src/img/content/o-centre/o-centre-hero.webp` |
| Output dimensions | 1890×1260 |
| Output SHA-256 | `3e9d45fee8d59c8ab3550d20d2310b4d834e87eecb8b9506ea92e972bea407c7` |
| Desktop/mobile | Same image reference (single hero fill) |
| Overlay | Hero text overlay per design (not part of asset) |

## Existing candidate comparison

| Candidate | SHA-256 | Exact match |
|---|---|---:|
| `services-hero.webp` | `f4fcac4135e2d7155327eb6c6b785ad8e651f4497f9fbdc608b443d0bed586e08` | **No** |
| Historical home hero | `52431f99…` (prior audit) | **No** |

## Crop / focal point

Implementation should use CSS object-fit/position to achieve 1400×628 visible crop as in Figma frame `1:2226`; source file is larger than frame (1890×1260).

## Alt policy

Decorative background with contextual hero copy in foreground — alt may be empty if copy carries meaning; confirm at implementation accessibility review.

## Result

Hero asset **resolved and approved** for commit. Not substitutable with `services-hero.webp`.

Compare JSON: `STORAGE/.../temp/FP-0002-V8-OCENTRE-HERO-COMPARE.json`
