# Original vs Candidate Review v1

## Status

Usability comparison only.

This review does not approve replacement, archiving, merging, or cleanup of original ORCA templates and checklists.

## Compared Flows

### Original Flow

Multiple files used together:

- `operational-decision-template-v1.md`
- `uncertainty-review-template-v1.md`
- `tradeoff-review-template-v1.md`
- `decision-quality-checklist-v1.md`
- `low-evidence-checklist-v1.md`
- `escalation-checklist-v1.md`

### Candidate Flow

One additive file:

- `evidence-review-template-candidate-v1.md`

## Comparison Findings

### Operator Speed

Candidate is faster for small PPC reviews.

The original flow is slower because it requires switching between decision, uncertainty, tradeoff, quality, low-evidence, and escalation views. That makes sense for heavier review, but it is too much for a small landing or keyword issue.

Candidate risk: it can still become slow if every field is treated as mandatory.

### Readability

Candidate is easier to read as a single operator note.

Original files are individually clear, but the combined flow feels repetitive. The same discipline appears in multiple places: evidence, uncertainty, SAFE UNKNOWN, escalation, and fake-confidence boundaries.

Candidate risk: one long template can blur priority if sections are not short.

### Safety Visibility

Candidate preserves most safety signals:

- evidence strength
- confidence level
- SAFE UNKNOWN
- contradiction notes
- low-evidence guard
- escalation guard
- reversible or human-approved action check

Original flow has stronger safety separation because low-evidence and escalation are standalone checklists. That makes them harder to miss in serious cases.

### Escalation Visibility

Candidate makes escalation visible enough for routine reviews.

Original flow is stronger when escalation is central, because the standalone escalation checklist includes operator authority, spend, brand, policy, legal, operational capacity, decision fatigue, and action-vs-delay risk.

Candidate gap: escalation wording is shorter and may underrepresent policy, legal, spend, brand, and operator-authority triggers.

### SAFE UNKNOWN Visibility

Candidate keeps SAFE UNKNOWN visible in Evidence Summary, Uncertainty Review, Low-Evidence Guard, Final Operator Checklist, and escalation-style notes.

Original flow reinforces SAFE UNKNOWN through repetition across several documents. That repetition is annoying, but it is also protective.

Candidate is acceptable if SAFE UNKNOWN remains explicitly required, not implied.

### Review Fatigue

Candidate reduces review fatigue for small issues.

Original flow creates fatigue because operators must mentally stitch together several files. This can cause checklist skipping, especially under commercial time pressure.

Candidate risk: a long consolidated form can create a different fatigue pattern if it becomes a mini-methodology.

### Duplication Reduction

Candidate reduces duplication meaningfully.

Repeated lines across original files include:

- ORCA does not make business decisions.
- Evidence can be incomplete.
- Uncertainty is normal.
- Operator judgment matters.
- Avoid fake confidence.
- Escalation is healthy.

These are valuable boundaries, but repeated full phrasing slows practical review.

### Cognitive Load

Candidate lowers cognitive load for one-issue reviews because the operator follows one sequence.

Original flow lowers risk for complex decisions because each file gives a sharper lens. That is useful when evidence is weak but business impact is high.

## Practical Split

Use candidate only as an additive shortcut for small, bounded, human-operated reviews.

Keep original flow authoritative for:

- high-impact spend decisions
- legal or policy risk
- brand-risk decisions
- unresolved contradictions
- operator authority uncertainty
- decisions where action and delay both carry real risk

## Bottom Line

The candidate improves usability for routine PPC review notes.

It should not replace the original flow yet. It is faster, but the originals still have better safety separation for serious decisions.
