# Minimal Template Consolidation Candidate v1

## Status

Candidate only. Do not create the actual template from this document without approval.

## Safety Finding

No non-consolidation direct references were found for the six target template/checklist files. A consolidation candidate is safe to propose, but not safe to execute until human usage is confirmed.

## Candidate Template Shape

Proposed future file:

- `projects/orca/evidence-core/evidence-review-template-v1.md`

Do not create it yet.

## Fields

```text
# Evidence Review Template v1

## Status

Manual evidence and decision note. Not approval, automation, telemetry, or autonomous decision-making.

## Context

- reviewer:
- date:
- campaign or review area:
- decision needed:
- evidence source:

## Evidence

- strongest evidence:
- weak evidence:
- what is known:
- what is unknown:
- contradictions:
- assumptions:
- SAFE_UNKNOWN:

## Priority

- high-impact risk:
- semantic cleanliness:
- landing clarity:
- trust alignment:
- mobile usability:
- operational simplicity:
- realistic review scope:

## Tradeoff

- speed vs depth:
- evidence quality vs action speed:
- operational realism vs theory:
- risk of action:
- risk of delay:

## Decision

- action:
- defer:
- verify:
- stop review:
- escalate:
- reason:

## Safety Checklist

- action matches evidence:
- assumptions are labeled:
- weak evidence cannot support major action:
- contradictions reduce confidence:
- SAFE_UNKNOWN is recorded:
- escalation needed:
- recommended human owner:
```

## Source Fields Preserved

From `operational-decision-template-v1.md`:

- context;
- decision priority;
- strongest and weak evidence;
- contradictions;
- assumptions;
- action/defer/escalate;
- risk of action and delay.

From `uncertainty-review-template-v1.md`:

- what is known;
- what is unknown;
- dangerous assumptions;
- stop, verify, reversible action.

From `tradeoff-review-template-v1.md`:

- speed vs depth;
- evidence quality vs action speed;
- operational realism vs theory;
- risk accepted / risk framing.

From `decision-quality-checklist-v1.md`:

- action matches evidence;
- assumptions labeled;
- weak evidence warning;
- practicality check.

From `low-evidence-checklist-v1.md`:

- incomplete source;
- thin sample;
- isolated observation;
- assumptions doing the work;
- hard-to-reverse action warning;
- mark SAFE UNKNOWN.

From `escalation-checklist-v1.md`:

- high-impact risk;
- incomplete evidence;
- contradictions reduce confidence;
- dangerous assumptions;
- operator authority insufficient;
- recommended human owner.

## Preserved Escalation Logic

Escalation must remain visible when:

- high-impact risk exists;
- evidence is incomplete;
- contradictions reduce confidence;
- assumptions are dangerous;
- spend, brand, policy, legal, or operational capacity is affected;
- operator authority is insufficient;
- action risk and delay risk both matter.

## Preserved SAFE UNKNOWN Handling

SAFE UNKNOWN must remain:

- a required field;
- acceptable when evidence is incomplete;
- visible before action;
- not treated as failure or incompleteness to hide.

## Boundary

This is a candidate shape only. It does not replace any existing template or checklist.
