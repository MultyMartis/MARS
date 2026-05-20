# Repeated Boundary Review v1

## Status

Boundary compression plan only. No source files were rewritten.

## Scope

Reviewed repeated boilerplate boundary patterns in the evidence/confidence/contradictions/operator-decisions family, with special attention to templates and checklists.

## Repeated Boundary Patterns

| Boundary pattern | Where it repeats | Keep repeated? | Compression recommendation |
|---|---|---|---|
| "ORCA does not make business decisions." | Operator decision README, rules, templates, checklists, boundaries. | Yes, but less often. | Keep in operator-facing entrypoint and key template; remove from every small checklist later only with approval. |
| "Not automation / telemetry / runtime / autonomous decision-making." | Most boundary sections across target family. | Yes, in core docs. | Use one compact shared boundary paragraph later. |
| "Evidence can be incomplete / contextual." | Evidence, confidence, contradiction, operator decision docs. | Yes. | Keep in evidence core and operator template; avoid repeating in every checklist. |
| "Human review is mandatory." | Evidence validation, confidence, contradictions, decisions. | Yes. | Keep in core evidence discipline and escalation/decision rules. |
| "SAFE UNKNOWN is valid." | Evidence, confidence, contradictions, decisions, templates. | Yes. | Keep in every operator-facing template field; avoid long repeated explanation. |
| "Reject fake confidence / unsupported strategic certainty." | Confidence, contradictions, operator decisions, checklists. | Yes. | Keep concise in boundary reference and low-evidence rules. |
| "Examples are fictional." | Mostly examples outside this narrow template/checklist scope. | Contextual. | Keep repeated in examples; not relevant to target templates/checklists. |

## What Can Stay Repeated

Keep repetition where it protects operators:

- source files that may be read independently;
- primary operator-facing template;
- escalation and low-evidence safety material;
- any file where autonomous decision risk is easy to misread.

## Excessive Repetition

Likely excessive:

- each small checklist repeating the full non-automation disclaimer;
- each small template repeating near-identical business-decision disclaimers;
- repeated "fake confidence" paragraphs where a single line is enough;
- repeated boundary text that is longer than the actual operator instruction.

## Shared Compact Reference Candidate

Future compact boundary could say:

```text
ORCA evidence and decision docs are human-supervised review aids. They do not automate decisions, prove market truth, run telemetry, or replace operator judgment. Use SAFE UNKNOWN when evidence is incomplete.
```

Do not apply this yet. It is a candidate only.

## Boundary

This plan does not rewrite existing boundary sections. It identifies future compression opportunities only.
