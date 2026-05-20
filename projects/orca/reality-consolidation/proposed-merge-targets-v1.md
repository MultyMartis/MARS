# Proposed Merge Targets v1

## Status

Merge proposal only. Do not merge, delete, archive, move, or rewrite files from this document alone.

## Goal

Reduce duplication and maintenance cost while preserving evidence discipline, uncertainty handling, contradiction handling, confidence handling, and operator decisions.

## What Could Become One Layer

### Candidate Layer: Evidence And Decision Discipline

Could consolidate:

- `evidence`
- selected `confidence`
- selected `contradictions`
- selected `operator-decisions`

Purpose:

- record evidence;
- qualify evidence;
- handle uncertainty;
- preserve contradictions;
- decide whether to act, stop, defer, or escalate.

Risk:

- this could become too broad if not aggressively scoped.

## What Should Remain Separate

### Operator-Facing Decision Rules

Keep separate or clearly visible:

- `operator-decisions/operator-decision-model-v1.md`
- `operator-decisions/decision-priority-rules-v1.md`
- `operator-decisions/escalation-rules-v1.md`
- `operator-decisions/low-evidence-decision-rules-v1.md`

Reason:

- operators need action guidance without reading evidence theory.

### Core Evidence Record

Keep separate or as the first section of the merged layer:

- `evidence/evidence-discipline-model-v1.md`
- `evidence/evidence-strength-model-v1.md`
- `evidence/source-reliability-rules-v1.md`
- `evidence/observation-traceability-rules-v1.md`

Reason:

- evidence discipline is the base. If it weakens, the whole system becomes fake confidence.

## What Should Become Appendices Or Reference Docs

### Confidence Appendix

Candidate appendix:

- `confidence/confidence-governance-model-v1.md`
- `confidence/confidence-update-rules-v1.md`
- `confidence/evidence-decay-rules-v1.md`
- `confidence/repeatability-model-v1.md`
- `confidence/pattern-reliability-scoring-v1.md`

Keep as reference for:

- confidence increase;
- confidence decrease;
- decay;
- repeatability;
- reliability changes over time.

### Contradiction Appendix

Candidate appendix:

- `contradictions/contradiction-tracking-model-v1.md`
- `contradictions/conflicting-observation-rules-v1.md`
- `contradictions/unstable-pattern-handling-v1.md`
- `contradictions/market-volatility-rules-v1.md`

Keep as reference for:

- conflict types;
- resolution status;
- bounded contradictions;
- volatility handling.

### Templates And Checklists

Candidate appendix or compression:

- `operator-decisions/templates/*`
- `operator-decisions/checklists/*`

Reason:

- useful for operators, but likely duplicative.
- one compact decision template may be enough.

## What Should Be Archived Later

Do not archive now. Later candidates if duplication remains:

- duplicate confidence level definitions after a unified evidence/confidence scale exists;
- redundant low-evidence rules repeated in both evidence and operator decisions;
- templates that only restate evidence, uncertainty, action, escalation, and SAFE UNKNOWN;
- scoring-like files if they imply precision beyond the evidence.

## What Should Remain Operator-Facing

Operator-facing minimal set should include:

- evidence summary;
- evidence strength;
- uncertainty and contradiction status;
- practical decision;
- escalation condition;
- SAFE UNKNOWN.

Likely files to keep operator-visible:

- `operator-decisions/operator-decision-model-v1.md`
- `operator-decisions/practical-decision-rules-v1.md`
- `operator-decisions/escalation-rules-v1.md`
- one compact decision template.

## Merge Target Recommendation

Recommended future structure:

- `evidence-and-reality/` as the core evidence, confidence, contradiction, and uncertainty discipline.
- `operator-decision/` as the compact operator-facing action layer.

This is a merge target concept only, not a new layer request.

## Boundary

No current ORCA file should be deleted or merged until a separate task approves exact file-level actions.
