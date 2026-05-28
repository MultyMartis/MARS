# Research → Content Pack Workflow v0

## Status

Human-operated workflow. **Not** automated pipeline.

## Trigger

- New PPC route or intent tier approved in strategy
- New capability / use-case page needed
- Major repositioning after research review

## Prerequisites

- ORCA project exists under `projects/orca/projects/<id>/`
- Research artifacts graded per [evidence-classification-system-v0.md](../../evidence/evidence-classification-system-v0.md)

## Steps

| Step | Action | Output |
|------|--------|--------|
| 1 | Define **one** landing object (route + intent tier) | Scope note in session |
| 2 | Collect inputs (see [content-pack-system-v0.md](../content-pack-system-v0.md)) | Source list |
| 3 | Copy [landing-content-pack-template-v0.md](../templates/landing-content-pack-template-v0.md) | Pack file `draft` |
| 4 | Fill sections 01–10 from blueprints / handoff / research | Section contracts |
| 5 | Set `ppc_continuity` from campaign instance JSON | Locked ad fields |
| 6 | Mark **SAFE UNKNOWN** for unverified NAP, rates, URLs | `safe_unknowns[]` |
| 7 | Set positioning locks (single machine, denied tasks, etc.) | `positioning_locks[]` |
| 8 | Run [operator-review-flow-v0.md](operator-review-flow-v0.md) | `reviewed` |
| 9 | Operator approves pack | `approved` + gates as needed |

## STOP rules

- Three findings already block launch-critical claims → stop research expansion
- Evidence weak → **SAFE UNKNOWN**, do not invent
- Do not open Commander exporter until pack aligns with group semantics

## Outputs

| State | Deliverable |
|-------|-------------|
| `approved` | Pack ready for DOCX export or Factory handoff |
| `MODE_1` eligible | `content_mode: MODE_1` + `semantic_lock: active` after factory gate |

## Related

- [../export-pipeline-v0.md](../export-pipeline-v0.md)
- Triumph blueprint: `ppc/triumph-manipulator/landing-pages/05-capability-5-ton.md`

## Boundary

Operator checklist only.
