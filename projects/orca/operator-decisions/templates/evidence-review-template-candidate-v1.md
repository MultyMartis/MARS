# Evidence Review Template Candidate v1

## Status

Candidate only.

This file is additive. It is not an approved replacement for existing ORCA operator-decision templates or checklists.

Original templates and checklists remain authoritative until explicit human approval:

- `operational-decision-template-v1.md`
- `uncertainty-review-template-v1.md`
- `tradeoff-review-template-v1.md`
- `decision-quality-checklist-v1.md`
- `low-evidence-checklist-v1.md`
- `escalation-checklist-v1.md`

Do not use this candidate as the sole source for safety-critical reviews yet.

Use one short line per field unless risk requires more.

## Review Identity

- review ID:
- date:
- reviewer:
- project / niche:
- region:
- campaign / ad group / landing reference:

## Evidence Summary

- observed issue:
- evidence source:
- evidence strength: weak / moderate / strong / very strong / SAFE_UNKNOWN
- confidence level: low / medium / high / very high / SAFE_UNKNOWN
- freshness: current / recent / stale / expired / unknown
- volatility: low / medium / high / unknown
- region/device context:

## Uncertainty Review

- what is known:
- what is unknown:
- SAFE UNKNOWN:
- assumptions:
- weak evidence:
- contradiction notes:

## Tradeoff Review, If Relevant

- speed vs evidence quality:
- simplicity vs segmentation:
- trust / pricing / landing clarity:
- operator effort vs expected value:

## Decision Proposal

- recommended action:
- action type: proceed / revise / defer / stop / escalate / collect more evidence / reject
- expected benefit:
- risk if wrong:
- fallback action:
- human approval required: yes / no / SAFE_UNKNOWN
- final outcome: proceed / defer / escalate / collect more evidence / reject

## Low-Evidence Guard

- Do not convert weak evidence into strong conclusions.
- Do not overblock search terms from one weak or narrow observation.
- Do not infer true root cause without evidence.
- Do not treat one SERP, one session, or one landing review as market truth.
- Use SAFE UNKNOWN when evidence is missing, stale, unstable, contradicted, or too narrow.

## Escalation Guard

Escalate when any of the following apply:

- spend, budget, or brand risk;
- policy or legal/compliance risk;
- landing mismatch risk;
- weak evidence with high impact;
- contradiction unresolved;
- operator uncertainty;
- operator authority insufficient;
- decision fatigue visible;
- business capacity unknown.

## Final Operator Checklist

- Evidence source is named.
- Evidence strength and confidence are not overstated.
- SAFE UNKNOWN is recorded where needed.
- Contradictions are visible.
- Low-evidence limits are respected.
- Escalation triggers were checked.
- Recommended action is reversible or human-approved.
