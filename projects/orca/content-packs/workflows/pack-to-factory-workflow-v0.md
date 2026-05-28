# Content Pack → Website Factory Workflow v0

## Status

Human-operated cross-lane handoff. Aligns with [orca-factory-bridge-index-v0.md](../../intelligence/orca-factory-bridge-index-v0.md).

## Trigger

- Pack `artifact_state` ≥ `approved`
- Operator sets `approved_for_factory`
- MODE 1 semantic lock required for paid PPC routes

## Preconditions

| Check | Required |
|-------|----------|
| Pack approved | yes |
| `approved_for_factory` | yes — human recorded |
| `content_mode` | `MODE_1` |
| `semantic_lock` | `active` |
| PPC continuity filled | yes |
| SAFE UNKNOWN on launch blockers | resolved or explicitly accepted in approval file |

## Steps

| Step | Actor | Action |
|------|-------|--------|
| 1 | Operator | Generate handoff from [website-factory-handoff-template-v0.md](../templates/website-factory-handoff-template-v0.md) |
| 2 | Operator | Link `source_pack_id` + paths in handoff |
| 3 | Factory lane | Read handoff + [orca-website-factory-semantic-lock-v0.md](../../intelligence/orca-website-factory-semantic-lock-v0.md) |
| 4 | Factory lane | Implement in workspace — **presentation only** |
| 5 | Operator | PPC landing QA per [ppc-landing-qa-contract-v0.md](../../intelligence/ppc-landing-qa-contract-v0.md) |
| 6 | Operator | Set `approved_for_ads` when continuity verified |
| 7 | Operator | Commander import (separate CLI) if needed |
| 8 | Operator | `approved_for_launch` after URL + moderation checklist |

## Semantic lock enforcement

Factory **must not**:

- Rewrite H1, specs, denied tasks, FAQ answers, CTA hierarchy
- Add fleet framing, fake prices, invented reviews

Factory **may**:

- Layout, SCSS, responsive, imagery crop, `&nbsp;` typography

On violation → halt build; update pack version; re-handoff.

## Triumph reference path

| Artifact | Path |
|----------|------|
| Content pack example | [examples/triumph-manipulyator-5-tonn-pack-v0.md](../examples/triumph-manipulyator-5-tonn-pack-v0.md) |
| Existing handoff | `ppc/triumph-manipulator/handoff/triumph-manipulator-v5-page-01-manipulyator-5-tonn-handoff.md` |
| Workspace | `workspaces/triumph-manipulator-landing-v4/` |

## Outputs

| State | Meaning |
|-------|---------|
| `factory-ready` | Handoff issued; build authorized |
| Post-QA | `approved_for_ads` |

## Boundary

Handoff discipline only — not Factory implementation.
