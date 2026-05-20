# Template Cleanup Safety Classification v1

## Status

Cleanup safety classification only. No cleanup was executed.

## Classification

| File | Classification | Reason |
|---|---|---|
| `operator-decisions/templates/operational-decision-template-v1.md` | KEEP AS-IS | Best current base template. It covers context, priority, evidence, uncertainty, action, defer, escalation, and risk. |
| `operator-decisions/templates/uncertainty-review-template-v1.md` | SAFE TO MERGE | No non-consolidation direct references found. Its useful fields can be preserved inside a consolidated template. |
| `operator-decisions/templates/tradeoff-review-template-v1.md` | SAFE TO MERGE | No non-consolidation direct references found. Its tradeoff fields can become optional fields in one template. |
| `operator-decisions/checklists/decision-quality-checklist-v1.md` | SAFE TO MERGE | No non-consolidation direct references found. Its checks can become a final checklist section. |
| `operator-decisions/checklists/low-evidence-checklist-v1.md` | NEEDS HUMAN REVIEW | Safety-critical. No active file references found, but operator dependency may exist outside docs. Preserve fully before archive. |
| `operator-decisions/checklists/escalation-checklist-v1.md` | NEEDS HUMAN REVIEW | Safety-critical. Escalation triggers and note fields must remain visible. Preserve fully before archive. |

## Archive Classification

No file is immediately classified as SAFE TO ARCHIVE LATER without replacement.

Archive-later candidates only after consolidated template approval:

- `uncertainty-review-template-v1.md`
- `tradeoff-review-template-v1.md`
- `decision-quality-checklist-v1.md`

Do not archive low-evidence or escalation checklists until a human confirms the consolidated template preserves their safety logic.

## Operator Safety Rule

KEEP AS-IS means no action until a replacement is approved. SAFE TO MERGE means merge content into a candidate first, not delete source. NEEDS HUMAN REVIEW means no archive or deletion without explicit approval.

## Boundary

This classification is not execution approval.
