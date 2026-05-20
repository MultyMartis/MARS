# Low-Risk Cleanup Candidates v1

## Status

Candidate list only. No cleanup was executed.

## Allowed Candidate Types

Only low-risk candidates are included:

- duplicate templates;
- duplicate checklists;
- repeated boilerplate review structures;
- repeated boundary boilerplate.

Core evidence, confidence, contradiction, and operator-decision logic are excluded from this list.

## Lowest-Risk Candidates

| Candidate | Type | Why low risk | Required safeguard |
|---|---|---|---|
| `operator-decisions/templates/uncertainty-review-template-v1.md` | Duplicate template | Its fields overlap strongly with `operational-decision-template-v1.md`. | Preserve known/unknown, weak evidence, contradictions, dangerous assumptions, SAFE UNKNOWN. |
| `operator-decisions/templates/tradeoff-review-template-v1.md` | Duplicate template | Its fields can become optional tradeoff fields inside one template. | Preserve risk of action, risk of delay, and review stop point. |
| `operator-decisions/checklists/decision-quality-checklist-v1.md` | Duplicate checklist | Can become final checklist section in one evidence review template. | Preserve action/evidence match, assumptions labeled, weak evidence warning. |
| repeated Status sections in templates/checklists | Boilerplate | Most say manual, not automation, not approval. | Keep one concise disclaimer in consolidated template. |
| repeated Boundary sections in templates/checklists | Boilerplate | Boundary text repeats similar fake-confidence and autonomous-decision warnings. | Keep operator-visible boundary once; do not remove safety meaning. |

## Needs Human Review Before Cleanup

| Candidate | Why review is needed |
|---|---|
| `operator-decisions/checklists/low-evidence-checklist-v1.md` | Safety-critical; should not disappear unless fully preserved in consolidated template. |
| `operator-decisions/checklists/escalation-checklist-v1.md` | Safety-critical; escalation triggers must remain visible. |
| `operator-decisions/templates/operational-decision-template-v1.md` | Likely base template; should be kept unless replacement is approved. |

## Not Low-Risk In This Pass

Do not include:

- `evidence/evidence-discipline-model-v1.md`;
- `evidence/evidence-strength-model-v1.md`;
- `confidence/*`;
- `contradictions/*`;
- `operator-decisions/*rules*.md`;
- `operator-decisions/operator-decision-model-v1.md`;
- any semantic, landing, heuristic, workflow, or contract docs.

## Safe First Cleanup Shape

If execution is later approved, safest first action is not deletion. It is:

- create one consolidated template candidate;
- compare against all existing templates/checklists;
- confirm no safety field is lost;
- then decide archive-only versus redirect versus deletion.

## Boundary

This candidate list is not permission to archive or delete files.
