# ORCA Visual Semantics Layer v0

**Status:** v0 — human-calibrated operational UX semantics (documentation only)  
**First evidence case:** Triumph Manipulator v5 — master hot (`grp_fc12_zakaz`, `/`)  
**Not:** design system, Figma tokens, CSS, runtime personalization, autonomous UX AI, CRO analytics

## Problem statement

ORCA already produces **semantic content** (PPC intent, landing structure, CTA logic, trust positioning). Triumph v5 calibration proved:

> **Semantic content ≠ visual implementation priorities.**

Website Factory had to **infer** hero zoning, proof weight, compactness, CTA dominance, mobile priority, and trust modes manually. This layer formalizes that inference so ORCA can emit **visual semantic intent** alongside copy.

## Relationship to other ORCA layers

| Layer | Role |
|-------|------|
| PPC / blueprints | What to say |
| Content packs (vNext) | Structured section copy |
| **Visual semantics (this)** | How Factory should **prioritize, zone, and weight** elements |
| Website Factory | HTML/SCSS implementation |
| Calibration (`projects/orca/calibration/triumph-manipulator/`) | Raw evidence — **not** duplicated here; distilled in `triumph-calibration/` |

## Entry points

| Doc | Use when |
|-----|----------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Navigation |
| [orca-visual-semantics-system-v0.md](orca-visual-semantics-system-v0.md) | System overview + canonical fields |
| [contracts/website-factory-visual-contract-v0.md](contracts/website-factory-visual-contract-v0.md) | Factory handoff requirements |
| [examples/triumph-zakaz-hero-visual-semantics-v1.md](examples/triumph-zakaz-hero-visual-semantics-v1.md) | First canonical example |

## Evidence discipline

All v0 claims trace to:

- `projects/orca/calibration/triumph-manipulator/` (2026-05-28 loop)
- As-built references cite workspace paths **read-only** — this layer does not modify workspaces

**SAFE UNKNOWN** where device QA, analytics, or SLA proof are absent.

## Versioning

- **v0** — field definitions, Triumph calibration distillate, Factory contract
- **v1 (planned)** — content-pack field binding — see `next-evolution/`
