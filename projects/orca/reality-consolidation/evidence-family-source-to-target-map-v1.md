# Evidence Family Source-To-Target Map v1

## Status

Planning only. No file movement, merge, archive, deletion, or rewrite is authorized.

## Proposed Target Folder

Target concept only:

- `projects/orca/evidence-core/`

Do not create this folder yet.

## Source-To-Target Map

| Current file | Proposed future destination | Action type | Notes |
|---|---|---|---|
| `projects/orca/evidence/evidence-discipline-model-v1.md` | `evidence-core/evidence-discipline-core-v1.md` | merge into proposed target file | Core source. Preserve evidence fields and observation/interpretation split. |
| `projects/orca/evidence/evidence-strength-model-v1.md` | `evidence-core/evidence-strength-and-confidence-v1.md` | merge into proposed target file | Merge with confidence scale; avoid competing reliability terms. |
| `projects/orca/evidence/observation-traceability-rules-v1.md` | `evidence-core/evidence-discipline-core-v1.md` | merge into proposed target file | Preserve trace fields and unsupported pattern controls. |
| `projects/orca/evidence/source-reliability-rules-v1.md` | `evidence-core/evidence-discipline-core-v1.md` | merge into proposed target file | Preserve source classes, especially synthetic output warning. |
| `projects/orca/evidence/human-validation-rules-v1.md` | `evidence-core/evidence-discipline-core-v1.md` | merge into proposed target file | Preserve validation triggers and outcomes. |
| `projects/orca/confidence/confidence-governance-model-v1.md` | `evidence-core/evidence-strength-and-confidence-v1.md` | convert into appendix content | Preserve confidence lifecycle; compress level duplication. |
| `projects/orca/confidence/confidence-update-rules-v1.md` | `evidence-core/evidence-strength-and-confidence-v1.md` | convert into appendix content | Preserve update reasons and downgrade triggers. |
| `projects/orca/confidence/repeatability-model-v1.md` | `evidence-core/evidence-strength-and-confidence-v1.md` | convert into appendix content | Compress repeatability classes into reliability section. |
| `projects/orca/confidence/evidence-decay-rules-v1.md` | `evidence-core/evidence-strength-and-confidence-v1.md` | convert into appendix content | Preserve freshness states and decay triggers. |
| `projects/orca/confidence/pattern-reliability-scoring-v1.md` | `evidence-core/evidence-strength-and-confidence-v1.md` or archive | needs human decision | Scoring language has false-precision risk. Keep only caution/penalty content if approved. |
| `projects/orca/contradictions/contradiction-tracking-model-v1.md` | `evidence-core/contradiction-handling-v1.md` | merge into proposed target file | Core source. Preserve contradiction states. |
| `projects/orca/contradictions/conflicting-observation-rules-v1.md` | `evidence-core/contradiction-handling-v1.md` | merge into proposed target file | Preserve conflict handling and forbidden handling. |
| `projects/orca/contradictions/unstable-pattern-handling-v1.md` | `evidence-core/contradiction-handling-v1.md` | convert into appendix content | Preserve unstable pattern warnings. |
| `projects/orca/contradictions/market-volatility-rules-v1.md` | `evidence-core/contradiction-handling-v1.md` | convert into appendix content | Preserve volatility levels and confidence effects. |
| `projects/orca/operator-decisions/README.md` | `evidence-core/README.md` or redirect README | needs human decision | Depends on whether old folder remains as redirect. |
| `projects/orca/operator-decisions/operator-decision-model-v1.md` | `evidence-core/operator-decision-rules-v1.md` | merge into proposed target file | Core operator-facing source. |
| `projects/orca/operator-decisions/decision-priority-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | merge into proposed target file | Keep high-impact priority test. |
| `projects/orca/operator-decisions/uncertainty-handling-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | merge into proposed target file | Preserve weak evidence, stop, and escalation triggers. |
| `projects/orca/operator-decisions/evidence-weighting-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | merge into proposed target file | Compress into action rules; avoid second evidence scale. |
| `projects/orca/operator-decisions/practical-decision-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | merge into proposed target file | Keep practical tests and anti-theory guardrails. |
| `projects/orca/operator-decisions/low-evidence-decision-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | merge into proposed target file | Core safety content. Preserve forbidden low-evidence decisions. |
| `projects/orca/operator-decisions/operational-tradeoff-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | convert into appendix content | Keep short tradeoff section only. |
| `projects/orca/operator-decisions/decision-fatigue-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | convert into appendix content | Keep fatigue stop rules as safety note. |
| `projects/orca/operator-decisions/escalation-rules-v1.md` | `evidence-core/operator-decision-rules-v1.md` | merge into proposed target file | Core source. Preserve escalation triggers and note fields. |
| `projects/orca/operator-decisions/operator-decision-boundaries-v1.md` | `evidence-core/README.md` and `operator-decision-rules-v1.md` | merge into proposed target file | Preserve boundary once; remove repetition later only with approval. |
| `projects/orca/operator-decisions/templates/operational-decision-template-v1.md` | `evidence-core/evidence-review-template-v1.md` | convert into template | Best base template. |
| `projects/orca/operator-decisions/templates/uncertainty-review-template-v1.md` | `evidence-core/evidence-review-template-v1.md` | convert into template | Fold known/unknown, assumptions, SAFE UNKNOWN fields into one template. |
| `projects/orca/operator-decisions/templates/tradeoff-review-template-v1.md` | `evidence-core/evidence-review-template-v1.md` | convert into template | Add optional tradeoff fields only. |
| `projects/orca/operator-decisions/checklists/decision-quality-checklist-v1.md` | `evidence-core/evidence-review-template-v1.md` | convert into template | Convert to final checklist section. |
| `projects/orca/operator-decisions/checklists/low-evidence-checklist-v1.md` | `evidence-core/evidence-review-template-v1.md` | convert into template | Preserve low-evidence safety questions. |
| `projects/orca/operator-decisions/checklists/escalation-checklist-v1.md` | `evidence-core/evidence-review-template-v1.md` | convert into template | Preserve escalation note fields. |

## Current Files That May Remain As-Is Temporarily

Until the operator approves target folder and redirect policy, all original files should remain as-is.

## Archive Candidates

No archive action now. Candidate only:

- `projects/orca/confidence/pattern-reliability-scoring-v1.md`

Reason:

- it has the highest false-precision risk and duplicates evidence strength/confidence concepts.

## Boundary

This map is a plan, not an execution instruction.
