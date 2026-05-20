# Merge Family Role Map v1

## Status

Controlled merge mapping only. No files are merged, deleted, archived, moved, or rewritten.

## Scope

Target family only:

- `projects/orca/evidence/**`
- `projects/orca/confidence/**`
- `projects/orca/contradictions/**`
- `projects/orca/operator-decisions/**`

## Reality Principle

ORCA must stay usable. Simplicity is strategic, but compression has risks. Evidence discipline must survive any future merge.

## Role Map

| Layer | Actual operational purpose | Unique value | Duplicated value | Maintenance burden | Operator burden | Abstraction risk |
|---|---|---|---|---:|---:|---:|
| `evidence` | Records, qualifies, traces, and validates PPC research evidence. | Strongest source of truth for evidence fields, source reliability, traceability, human validation, and evidence strength. | Confidence, contradiction, freshness, volatility, SAFE UNKNOWN, and human review logic overlap with all other target layers. | Medium | Medium | Low |
| `confidence` | Defines how reliability increases, decreases, decays, and updates over time. | Explicit confidence lifecycle: update reasons, decay, repeatability, pattern reliability, downgrade rules. | Evidence strength levels and contradiction penalties duplicate `evidence` and `contradictions`. | Medium | Medium | Medium |
| `contradictions` | Preserves conflicting observations and prevents false generalization. | Strongest source for conflict types, resolution status, bounded contradictions, and volatility conflict handling. | Confidence caps, evidence context, SAFE UNKNOWN, volatility, and human review duplicate `evidence` and `confidence`. | Medium | Medium | Medium |
| `operator-decisions` | Turns evidence, uncertainty, contradiction, and confidence into human operator action, defer, stop, or escalate. | Strongest operator-facing action layer: priorities, tradeoffs, escalation, fatigue, low-evidence decision rules. | Evidence weighting, uncertainty, confidence reduction, contradiction impact, and SAFE UNKNOWN duplicate previous layers. | High | High | Medium |

## Layer-Level Findings

### `evidence`

- Keep as the core record discipline.
- It should own evidence fields, source reliability, traceability, freshness, strength, and human validation.
- It should not become a decision layer.

### `confidence`

- Keep only the parts that explain lifecycle: increase, decrease, decay, repeatability, and update reasons.
- Its level definitions can likely be folded into evidence strength or a short appendix.
- Risk: if kept separate, operators may treat evidence strength and confidence as two competing scores.

### `contradictions`

- Keep as a focused conflict-handling appendix or submodule.
- It should preserve contradiction types and resolution status.
- It should not duplicate general evidence fields in every file.

### `operator-decisions`

- Keep operator-facing decision and escalation rules.
- Compress evidence and uncertainty explanations into references to the evidence core.
- It should answer: act, defer, stop, or escalate.

## Main Role Separation

- `evidence`: what was observed and how reliable the record is.
- `confidence`: how reliability changes over time.
- `contradictions`: what conflicts with what and how it limits conclusions.
- `operator-decisions`: what the human operator does next.

## Boundary

This map does not create a new layer. It prepares a future compression decision.
