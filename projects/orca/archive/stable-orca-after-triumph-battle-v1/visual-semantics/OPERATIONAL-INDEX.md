# OPERATIONAL-INDEX — ORCA Visual Semantics

**Lane:** B · ORCA Visual Semantics Layer v0  
**Updated:** 2026-05-28

## Start here

1. [README.md](README.md)
2. [orca-visual-semantics-system-v0.md](orca-visual-semantics-system-v0.md)
3. [examples/triumph-zakaz-hero-visual-semantics-v1.md](examples/triumph-zakaz-hero-visual-semantics-v1.md)

## Core system

| File | Purpose |
|------|---------|
| [orca-visual-semantics-system-v0.md](orca-visual-semantics-system-v0.md) | System definition + 15 canonical fields |
| [visual-semantics-principles-v0.md](visual-semantics-principles-v0.md) | Operating principles |
| [semantic-to-visual-translation-v0.md](semantic-to-visual-translation-v0.md) | ORCA copy → visual intent mapping |
| [frontend-priority-model-v0.md](frontend-priority-model-v0.md) | P0–P4 section + element priority |
| [semantic-density-rules-v0.md](semantic-density-rules-v0.md) | Overload warnings |
| [trust-mode-system-v0.md](trust-mode-system-v0.md) | social / operational / hybrid |
| [hero-hierarchy-model-v0.md](hero-hierarchy-model-v0.md) | Hero zones + evolution |
| [mobile-criticality-rules-v0.md](mobile-criticality-rules-v0.md) | Mobile-first implementation hints |

## Schemas

| File | Field(s) |
|------|----------|
| [schemas/visual-semantics-schema-v0.md](schemas/visual-semantics-schema-v0.md) | Master bundle |
| [schemas/hero-priority-schema-v0.md](schemas/hero-priority-schema-v0.md) | `hero_priority`, `hero_layout_mode` |
| [schemas/trust-mode-schema-v0.md](schemas/trust-mode-schema-v0.md) | `trust_mode`, `proof_*` |
| [schemas/cta-priority-schema-v0.md](schemas/cta-priority-schema-v0.md) | `cta_priority`, `cta_weight` |
| [schemas/compactness-schema-v0.md](schemas/compactness-schema-v0.md) | `compactness_level` |
| [schemas/visual-density-schema-v0.md](schemas/visual-density-schema-v0.md) | `visual_density`, `visual_noise_risk` |

## Triumph calibration (distilled)

| File | Source calibration doc |
|------|------------------------|
| [triumph-calibration/README.md](triumph-calibration/README.md) | Loop index |
| [triumph-calibration/hero-evolution-findings-v1.md](triumph-calibration/hero-evolution-findings-v1.md) | `ux-observations/hero-evolution-v1.md` |
| [triumph-calibration/productive-drift-findings-v1.md](triumph-calibration/productive-drift-findings-v1.md) | drift-analysis + orca-vs-frontend |
| [triumph-calibration/destructive-drift-findings-v1.md](triumph-calibration/destructive-drift-findings-v1.md) | D1, D2, continuity gaps |
| [triumph-calibration/trust-evolution-findings-v1.md](triumph-calibration/trust-evolution-findings-v1.md) | `trust-block-analysis-v1.md` |
| [triumph-calibration/visual-density-findings-v1.md](triumph-calibration/visual-density-findings-v1.md) | `visual-density-observations-v1.md` |
| [triumph-calibration/mobile-risk-findings-v1.md](triumph-calibration/mobile-risk-findings-v1.md) | `mobile-risk-observations-v1.md` |
| [triumph-calibration/hero-zoning-findings-v1.md](triumph-calibration/hero-zoning-findings-v1.md) | `current-hero-analysis-v1.md` |
| [triumph-calibration/ppc-to-hero-alignment-findings-v1.md](triumph-calibration/ppc-to-hero-alignment-findings-v1.md) | `ppc-continuity-analysis-v1.md` |

## Contracts (Factory bridge)

| File | Audience |
|------|----------|
| [contracts/website-factory-visual-contract-v0.md](contracts/website-factory-visual-contract-v0.md) | Website Factory |
| [contracts/visual-semantic-lock-rules-v0.md](contracts/visual-semantic-lock-rules-v0.md) | Lock + drift classes |
| [contracts/frontend-priority-contract-v0.md](contracts/frontend-priority-contract-v0.md) | Section priority |
| [contracts/hero-implementation-contract-v0.md](contracts/hero-implementation-contract-v0.md) | Hero partial contract |

## Examples

| File | Case |
|------|------|
| [examples/triumph-zakaz-hero-visual-semantics-v1.md](examples/triumph-zakaz-hero-visual-semantics-v1.md) | Master hot hero (canonical) |
| [examples/trust-mode-examples-v0.md](examples/trust-mode-examples-v0.md) | Trust modes |
| [examples/compactness-examples-v0.md](examples/compactness-examples-v0.md) | Compactness tiers |
| [examples/mobile-priority-examples-v0.md](examples/mobile-priority-examples-v0.md) | Mobile critical |

## Next evolution

| File | Target |
|------|--------|
| [next-evolution/visual-semantic-fields-for-content-pack-v1.md](next-evolution/visual-semantic-fields-for-content-pack-v1.md) | Pack YAML binding |
| [next-evolution/hero-v2-operational-rules-v1.md](next-evolution/hero-v2-operational-rules-v1.md) | H2-1…H2-6 from calibration |
| [next-evolution/frontend-hint-system-v1.md](next-evolution/frontend-hint-system-v1.md) | Implementation hints |
| [next-evolution/scaling-rules-for-11-pages-v2.md](next-evolution/scaling-rules-for-11-pages-v2.md) | Sibling routes |

## Upstream evidence (read-only)

- `projects/orca/calibration/triumph-manipulator/`
- `projects/orca/ppc/triumph-manipulator/landing-pages/01-master-hot-general.md`

## Out of scope (v0)

- Design tokens / Figma
- CSS / partial edits
- governance/*, mars-runtime/*, exporter-cli, validation-cli
- Workspace modifications
