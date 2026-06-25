# FP-0002 V7 — Final Polish Difference Audit

**Date:** 2026-06-24  
**Authority:** operator-canonical V7 + visible `Spig_v1.2.fig` content

## Summary counts

| Classification | Count |
| -------------- | ----: |
| OPERATOR_CANONICAL | 28 |
| TOKEN_MISMATCH | 0 |
| FIGMA_MISMATCH | 1 |
| RESPONSIVE_DEFECT | 0 |
| LEGACY_CSS | 1 |
| DUPLICATE_RULE | 0 |
| MEASURED_EXCEPTION | 0 |
| SAFE_UNKNOWN | 2 |

## Section audits

| Section | Property | Current value | Figma value | Existing token | Difference | Action |
| ------- | -------- | ------------: | ----------: | -------------- | ---------: | ------ |
| Gallery | caption position | `absolute` overlay | below image in 400px card (372px image + caption) | N/A | overlay vs normal flow | CORRECT |
| Gallery | caption color | `--color-text-inverse` | primary text below image | `--color-text-primary` | inverse on image | CORRECT |
| Gallery | caption DOM | `<p>` in `<div>` | image + caption sibling | `<figure>` + `<figcaption>` | semantics | CORRECT |
| Gallery | image→caption gap | 0 (overlay) | ~28px card remainder | `--pad-gap-tight` (10px) | spacing | CORRECT |
| Hero | all geometry | operator values | FIG reference | mixed tokens | operator-authored | KEEP |
| Recovery intro | copy/layout | operator values | FIG text nodes | N/A | verified Phase 3A | KEEP |
| Recovery life | mobile columns | 1 col ≤1024 | no dedicated mobile frame | N/A | RESPONSIVE_DERIVED | KEEP |
| Founder quote | SVG mark | 70×55 SVG | vector `1:1217` | N/A | Phase 3B verified | KEEP |
| Section rhythm | `main > section` padding | `var(--pad-y)` | 50px sections | `--pad-y` | Phase 4A complete | KEEP |
| Head | meta/OG paths | implemented | N/A | N/A | marketing copy TBD | KEEP |
| Services unique blocks | presence | absent | hub cards exist | N/A | out of scope | KEEP |
| Gallery (mobile) | caption placement | RESPONSIVE_DERIVED | SAFE UNKNOWN mobile subtree | N/A | desktop evidence applied | KEEP_WITH_EVIDENCE |
| Mobile gallery frame | dedicated frame | N/A | not isolated in extract | N/A | insufficient proof | DO_NOT_CHANGE |

## Legacy CSS removed

| Selector/property | Usage | Classification | Action |
| ----------------- | ----- | -------------- | ------ |
| `.home-gallery__caption` `position:absolute` + inverse overlay stack | replaced by normal flow | LEGACY_CSS | REMOVED_AFTER_USAGE_PROOF |
| `.home-gallery__slide` `position:relative` | only served overlay caption | LEGACY_CSS | REMOVED_AFTER_USAGE_PROOF |

## Polish actions taken

1. Gallery caption moved to static flow below image (`figure` / `figcaption`).
2. No other sections modified — operator-canonical values preserved.
