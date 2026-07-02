# FP-0002 — Services V1 Differential Audit v1

**Date:** 2026-06-26  
**Sources:** A) `Spig_v1.2.fig` visible anatomy · B) PNG 26.06.2026 · C) V1 @ `641295e1` (`uslugi.html`)

| Component | Figma/PNG target | Current V1 | Difference | Severity | Root cause |
| --------- | ---------------- | ---------- | ---------- | -------- | ---------- |
| Inner Hero shell | Banner 1400×628 + overlay | `hero-inner.html` + gradient polish | CTA column split vs in-banner CTA | STRUCTURAL_MISMATCH | wrong component boundary |
| Inner Hero content | Left overlay panel 582px | Panel present, copy matches | DOM/actions split | MINOR_POLISH | reuse of generic inner hero |
| Breadcrumbs | `1:1363` under hero | Absent | Missing trail | MISSING_COMPONENT | missing node during decomposition |
| Page submenu | `1:1367` 6 tabs | Absent | Missing category shortcuts | MISSING_COMPONENT | incorrect reuse assumption |
| Category 1 | Full editorial + gallery | Implemented | Decor/geometry partial | PARTIAL_MATCH | wrong responsive inference |
| Category 2 | 6 items + gallery + bodies | Names only | Missing descriptions | CONTENT gap (documented SAFE_UNKNOWN) | content extraction policy |
| Category 3 | Compact, no gallery | `--compact --no-gallery` | Close | MATCH / PARTIAL | — |
| Category 4 | Compact genotyping | `--compact`, empty leads | Lead missing | PARTIAL_MATCH | Figma lorem exclusion |
| Program | 2×2 image grid | Home vertical layout | Grid wrong | STRUCTURAL_MISMATCH | layout reuse without audit |
| Founder | `1:1649` | `home-founder-quote.html` | Near match | MATCH | — |
| Comfort | Gallery mosaic | `home-comfort.html` | Visual gap documented in polish reviews | MINOR_POLISH | capture vs geometry |
| Mid-page CTA | `1:1715` dark strip | Not dedicated partial | Merged/missing as section | MISSING_COMPONENT | missing node during decomposition |
| FAQ | `1:1720` | `home-faq.html` | Near match | MATCH | — |
| Final form | Before footer | `home-final-form.html` | Near match | MATCH | — |
| Recovery intro `1:1374` | Not on PNG | Not in V1 | N/A | N/A | hidden frame — exclude |
| Footer | `1:1747` | `footer.html` | Match | MATCH | — |

## Aggregate severity

| Severity | Count |
| -------- | ----: |
| MATCH | 4 |
| MINOR_POLISH | 2 |
| STRUCTURAL_MISMATCH | 3 |
| MISSING_COMPONENT | 3 |
| PARTIAL_MATCH | 4 |

## Primary root causes

1. **incorrect reuse assumption** — page built from home partial inventory before target anatomy
2. **missing node during decomposition** — breadcrumbs, tabs, mid-CTA not extracted
3. **wrong component boundary** — hero-inner treated as complete inner page hero
4. **layout reuse without audit** — program section

## REPAIR_V1 feasibility

**Not recommended.** Adding breadcrumbs/tabs/program layout to V1 would produce a hybrid DOM inconsistent with Figma hero architecture and increase regression risk on `uslugi.html` fallback.
