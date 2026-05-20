# Safe Cleanup Template Review v1

## Status

Low-risk cleanup review only. No source templates, checklists, core docs, folders, or operational logic were changed.

## Scope

Reviewed templates and checklists inside the target family:

- `projects/orca/evidence/**`
- `projects/orca/confidence/**`
- `projects/orca/contradictions/**`
- `projects/orca/operator-decisions/**`

Actual template/checklist files found only in:

- `projects/orca/operator-decisions/templates/`
- `projects/orca/operator-decisions/checklists/`

## Template Findings

| File | Finding | Classification | Reason |
|---|---|---|---|
| `operator-decisions/templates/operational-decision-template-v1.md` | Broadest and most practical base template. | KEEP | Covers context, priority, evidence, uncertainty, action, defer, escalation, risk. |
| `operator-decisions/templates/uncertainty-review-template-v1.md` | Near-duplicate focused on known/unknown and handling decision. | MERGE LATER | Useful fields can be folded into the operational decision template. |
| `operator-decisions/templates/tradeoff-review-template-v1.md` | Specialized tradeoff note with evidence and decision fields. | MERGE LATER | Useful as optional section, not separate default template. |

## Checklist Findings

| File | Finding | Classification | Reason |
|---|---|---|---|
| `operator-decisions/checklists/decision-quality-checklist-v1.md` | Compact final quality check. | MERGE LATER | Can become a final checklist section in one template. |
| `operator-decisions/checklists/low-evidence-checklist-v1.md` | Safety-critical low-evidence checks. | NEEDS HUMAN REVIEW | Should be preserved, but likely folded into one evidence review template. |
| `operator-decisions/checklists/escalation-checklist-v1.md` | Safety-critical escalation triggers and note fields. | NEEDS HUMAN REVIEW | Should remain visible until a combined template proves usable. |

## Duplicate Structures

Repeated structures:

- Status disclaimer;
- Context fields;
- evidence source;
- weak evidence / uncertainty;
- contradictions;
- assumptions;
- SAFE UNKNOWN;
- decision/action;
- escalate;
- repeated boundary text.

## Duplicate Checklist Logic

Repeated checklist logic:

- weak evidence should reduce confidence;
- contradictions reduce confidence;
- assumptions must be labeled;
- escalation is needed for high-impact incomplete evidence;
- ORCA does not make business decisions;
- reject fake confidence and unsupported strategic certainty.

## Low-Risk Consolidation Direction

Future single template candidate:

- start from `operational-decision-template-v1.md`;
- add known/unknown and dangerous assumptions from `uncertainty-review-template-v1.md`;
- add optional tradeoff fields from `tradeoff-review-template-v1.md`;
- add final decision quality checks;
- preserve low-evidence and escalation safety checks.

## Boundary

This review identifies duplication. It does not approve deletion, archiving, or merge execution.
