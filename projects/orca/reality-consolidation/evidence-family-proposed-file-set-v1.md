# Evidence Family Proposed File Set v1

## Status

Planning only. Do not create `projects/orca/evidence-core/` from this document without explicit approval.

## Proposed Future Structure

```text
projects/orca/evidence-core/
  README.md
  evidence-discipline-core-v1.md
  evidence-strength-and-confidence-v1.md
  contradiction-handling-v1.md
  operator-decision-rules-v1.md
  evidence-review-template-v1.md
```

## Purpose

Create the smallest future file set that preserves:

- evidence discipline;
- confidence handling;
- contradiction handling;
- uncertainty handling;
- operator decision rules;
- practical review template.

## Proposed Files

### `README.md`

Purpose:

- explain the consolidated family;
- point operators to the minimal path;
- state that this is human-supervised documentation, not automation.

Source mapping:

- `operator-decisions/README.md`
- boundary summaries from all target families
- selected framing from merge-map documents

### `evidence-discipline-core-v1.md`

Purpose:

- own evidence record fields;
- preserve source, timestamp, region, niche, device, reviewer, traceability, source reliability, human validation, and SAFE UNKNOWN;
- separate observation from interpretation.

Source mapping:

- `evidence/evidence-discipline-model-v1.md`
- `evidence/observation-traceability-rules-v1.md`
- `evidence/source-reliability-rules-v1.md`
- `evidence/human-validation-rules-v1.md`

### `evidence-strength-and-confidence-v1.md`

Purpose:

- define one practical reliability scale;
- explain confidence increase, decrease, decay, repeatability, and freshness;
- avoid competing scores.

Source mapping:

- `evidence/evidence-strength-model-v1.md`
- `confidence/confidence-governance-model-v1.md`
- `confidence/confidence-update-rules-v1.md`
- `confidence/evidence-decay-rules-v1.md`
- `confidence/repeatability-model-v1.md`
- selected caution from `confidence/pattern-reliability-scoring-v1.md`

### `contradiction-handling-v1.md`

Purpose:

- preserve conflicting observations;
- define contradiction states;
- handle unstable patterns and volatility;
- prevent forced agreement.

Source mapping:

- `contradictions/contradiction-tracking-model-v1.md`
- `contradictions/conflicting-observation-rules-v1.md`
- `contradictions/unstable-pattern-handling-v1.md`
- `contradictions/market-volatility-rules-v1.md`

### `operator-decision-rules-v1.md`

Purpose:

- convert evidence state into action, stop, defer, revise, or escalate;
- preserve high-impact risk priority;
- keep low-evidence and escalation safety visible.

Source mapping:

- `operator-decisions/operator-decision-model-v1.md`
- `operator-decisions/decision-priority-rules-v1.md`
- `operator-decisions/uncertainty-handling-rules-v1.md`
- `operator-decisions/evidence-weighting-rules-v1.md`
- `operator-decisions/practical-decision-rules-v1.md`
- `operator-decisions/low-evidence-decision-rules-v1.md`
- `operator-decisions/operational-tradeoff-rules-v1.md`
- `operator-decisions/decision-fatigue-rules-v1.md`
- `operator-decisions/escalation-rules-v1.md`
- `operator-decisions/operator-decision-boundaries-v1.md`

### `evidence-review-template-v1.md`

Purpose:

- replace multiple overlapping operator templates/checklists with one practical operator note.

Source mapping:

- `operator-decisions/templates/operational-decision-template-v1.md`
- `operator-decisions/templates/uncertainty-review-template-v1.md`
- `operator-decisions/templates/tradeoff-review-template-v1.md`
- `operator-decisions/checklists/decision-quality-checklist-v1.md`
- `operator-decisions/checklists/low-evidence-checklist-v1.md`
- `operator-decisions/checklists/escalation-checklist-v1.md`

Minimum fields:

- reviewer:
- date:
- review area:
- evidence source:
- evidence strength / confidence:
- contradiction:
- uncertainty:
- decision:
- escalation:
- SAFE UNKNOWN:

## What This File Set Avoids

- four overlapping folders for one evidence-to-decision path;
- competing evidence strength and confidence scoring systems;
- multiple templates asking for the same fields;
- repeated boundary paragraphs in every file;
- pseudo-precision from scoring-like language.

## Boundary

This proposal does not create the target folder or modify source documents.
