# Evidence Family Cleanup Order v1

## Status

Planning only. Do not execute cleanup from this document without explicit approval.

## Cleanup Principle

Start with the safest duplication. Do not touch core evidence or contradiction models until operator-facing paths and safety rules are protected.

## Safest Cleanup Order

### 1. Duplicate Templates And Checklists

Target:

- `operator-decisions/templates/operational-decision-template-v1.md`
- `operator-decisions/templates/uncertainty-review-template-v1.md`
- `operator-decisions/templates/tradeoff-review-template-v1.md`
- `operator-decisions/checklists/decision-quality-checklist-v1.md`
- `operator-decisions/checklists/low-evidence-checklist-v1.md`
- `operator-decisions/checklists/escalation-checklist-v1.md`

Why first:

- they overlap heavily;
- they are easiest to compare;
- one future `evidence-review-template-v1.md` can preserve the useful fields.

Stop if:

- the combined template becomes longer than the originals in practice;
- escalation or low-evidence safety fields disappear;
- operator cannot use the template in one short review.

### 2. Repeated Boundary Text

Target:

- repeated "not automation / not telemetry / not runtime";
- repeated "ORCA does not make business decisions";
- repeated "human review is mandatory";
- repeated pseudo-intelligence rejection.

Why second:

- boundary repetition has low unique value but high maintenance cost.

Stop if:

- source-specific boundaries are lost;
- rejection of autonomous decisions becomes unclear;
- SAFE UNKNOWN language disappears.

### 3. Repeated Confidence Explanations

Target:

- `confidence/confidence-governance-model-v1.md`
- `confidence/confidence-update-rules-v1.md`
- `confidence/evidence-decay-rules-v1.md`
- `confidence/repeatability-model-v1.md`
- `confidence/pattern-reliability-scoring-v1.md`
- confidence sections duplicated in `evidence/evidence-strength-model-v1.md`.

Why third:

- confidence logic is useful but duplicated;
- one practical reliability scale may reduce operator confusion.

Stop if:

- evidence strength and confidence become vague;
- decay or downgrade rules are removed;
- scoring language implies false precision.

### 4. Repeated Evidence Quality Logic

Target:

- `evidence/evidence-strength-model-v1.md`
- `evidence/source-reliability-rules-v1.md`
- `evidence/observation-traceability-rules-v1.md`
- overlapping logic in `operator-decisions/evidence-weighting-rules-v1.md`.

Why fourth:

- evidence quality is central and should be compressed only after confidence scale is clear.

Stop if:

- source, timestamp, region, niche, device, reviewer, or SAFE UNKNOWN fields are lost;
- observation and interpretation are no longer separated;
- synthetic output warning is removed.

### 5. Contradiction Handling Overlap

Target:

- `contradictions/contradiction-tracking-model-v1.md`
- `contradictions/conflicting-observation-rules-v1.md`
- `contradictions/unstable-pattern-handling-v1.md`
- `contradictions/market-volatility-rules-v1.md`
- overlapping contradiction references in confidence and operator decisions.

Why fifth:

- contradictions are safety-critical and should not be compressed early.

Stop if:

- contradiction states are removed;
- conflicts become generic uncertainty;
- volatility and unstable-pattern limits disappear;
- confidence caps are no longer visible.

### 6. Operator-Decision Overlap

Target:

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

Why sixth:

- operator path must remain clear after evidence/confidence/contradiction rules are stabilized.

Stop if:

- act / stop / defer / escalate decisions are unclear;
- escalation rules are hidden;
- low-evidence limits are weakened;
- operator-facing file becomes theory-heavy.

### 7. Only Then Consider Archiving

Candidate:

- `confidence/pattern-reliability-scoring-v1.md`
- duplicate old templates/checklists after the consolidated template is approved;
- redirect READMEs only after folder policy is approved.

Stop if:

- operator has not approved archive-only versus delete;
- old folder redirect policy is undecided;
- any original doc must be preserved unchanged.

## Global Stop Conditions

Stop the cleanup plan before execution if:

- `projects/orca/evidence-core/` is not approved;
- the operator wants archive-only cleanup;
- original folders must remain canonical;
- any target source file is actively used by another ORCA path;
- evidence discipline becomes less explicit;
- contradiction handling becomes a footnote;
- templates become less usable;
- cleanup creates a new methodology layer.

## Boundary

This order is a safety plan. It is not permission to change source files.
