# Template Reference Inventory v1

## Status

Reference safety scan only. No source docs were modified, renamed, merged, archived, or deleted.

## Scope

Scanned references to only these files:

- `projects/orca/operator-decisions/templates/operational-decision-template-v1.md`
- `projects/orca/operator-decisions/templates/uncertainty-review-template-v1.md`
- `projects/orca/operator-decisions/templates/tradeoff-review-template-v1.md`
- `projects/orca/operator-decisions/checklists/decision-quality-checklist-v1.md`
- `projects/orca/operator-decisions/checklists/low-evidence-checklist-v1.md`
- `projects/orca/operator-decisions/checklists/escalation-checklist-v1.md`

## Inventory

| Target file | Direct references | Indirect references | Likely operator dependency | Likely workflow dependency | Risk level |
|---|---|---|---|---|---|
| `operational-decision-template-v1.md` | Referenced in `reality-consolidation` planning docs only. | Decision model and evidence weighting concepts support the same fields. | Medium: likely best base template if an operator uses the folder directly. | Low: no active workflow reference found. | MEDIUM |
| `uncertainty-review-template-v1.md` | Referenced in `reality-consolidation` planning docs only. | Uncertainty handling and low-evidence rules cover the same logic. | Low to medium: useful for uncertainty-heavy reviews, but duplicative. | Low: no active workflow reference found. | LOW |
| `tradeoff-review-template-v1.md` | Referenced in `reality-consolidation` planning docs only. | Operational tradeoff rules cover the same logic. | Low: specialized optional template. | Low: no active workflow reference found. | LOW |
| `decision-quality-checklist-v1.md` | Referenced in `reality-consolidation` planning docs only. | Decision priority, practical decision, and evidence weighting rules cover the same checks. | Low to medium: useful as final sanity check. | Low: no active workflow reference found. | LOW |
| `low-evidence-checklist-v1.md` | Referenced in `reality-consolidation` planning docs only. | Low-evidence decision rules and uncertainty handling rules are safety-critical sources. | Medium: checklist may be a practical operator guardrail. | Low: no active workflow reference found. | MEDIUM |
| `escalation-checklist-v1.md` | Referenced in `reality-consolidation` planning docs only. | Escalation rules and uncertainty handling rules are safety-critical sources. | Medium: checklist may be a practical operator guardrail. | Low: no active workflow reference found. | MEDIUM |

## Direct Reference Finding

No direct references were found from non-consolidation ORCA workflow docs during this scan. Current direct references are planning references inside `projects/orca/reality-consolidation/`.

## Indirect Dependency Finding

Even without direct file references, low-evidence and escalation logic are safety-critical. They should be preserved in any future consolidated template.

## SAFE UNKNOWN

Actual human usage is unknown. Operators may use these files directly without a markdown reference from another file.

## Boundary

This inventory does not authorize cleanup execution.
