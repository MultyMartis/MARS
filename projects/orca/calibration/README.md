# ORCA Calibration Layer

**Status:** v0 — human-operated documentation  
**Purpose:** Close the loop between ORCA research, semantic packs, PPC continuity, Website Factory implementation, and operational review.

## What this is

- Calibration **findings** and **lessons** from real landing production
- Semantic drift taxonomy (productive vs destructive)
- Handoff gap signals for future packs
- Scaling rules derived from the first canonical case

## What this is NOT

- Runtime telemetry or analytics automation
- A/B testing engine or heatmap product
- AI optimization claims
- Governance enforcement

## Canonical case (v0)

| Case | Route / intent | Workspace |
|------|----------------|-----------|
| [triumph-manipulator/](triumph-manipulator/) | Master hot — «Аренда манипулятора в Краснодаре» (`grp_fc12_zakaz`) | `workspaces/triumph-manipulator-landing-v6/` (**canonical**; v5 = historical) |

## Entry points

| Doc | Role |
|-----|------|
| [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md) | Lane navigation |
| [orca-calibration-system-v0.md](orca-calibration-system-v0.md) | System definition |
| [semantic-drift-rules-v0.md](semantic-drift-rules-v0.md) | Drift classification |
| [calibration-review-method-v0.md](calibration-review-method-v0.md) | How operators run a calibration pass |
| [calibration-artifact-lifecycle-v0.md](calibration-artifact-lifecycle-v0.md) | Artifact states and paths |

## Related ORCA lanes

- Content packs: `projects/orca/content-packs/`
- Triumph PPC: `projects/orca/ppc/triumph-manipulator/`
- Factory bridge: `projects/orca/intelligence/orca-factory-bridge-index-v0.md`
- Semantic lock: `projects/orca/intelligence/orca-website-factory-semantic-lock-v0.md`
