# Evidence Family File Inventory v1

## Status

Planning only. No source files were deleted, moved, merged, rewritten, archived, staged, or committed.

## Scope

Reviewed only:

- `projects/orca/evidence/**`
- `projects/orca/confidence/**`
- `projects/orca/contradictions/**`
- `projects/orca/operator-decisions/**`
- approved merge-map documents in `projects/orca/reality-consolidation/`

## Inventory

| Path | Current role | Unique value | Duplicated value | Likely future status | Cleanup risk |
|---|---|---|---|---|---|
| `projects/orca/evidence/evidence-discipline-model-v1.md` | Core evidence record discipline. | Defines evidence fields and separation of observation, interpretation, confidence, impact, contradiction, and SAFE UNKNOWN. | Repeats confidence, contradiction, human review, freshness, and no-runtime boundary logic. | KEEP CORE | High: losing this weakens all evidence discipline. |
| `projects/orca/evidence/evidence-strength-model-v1.md` | Evidence strength classification. | Defines weak/moderate/strong/very strong support and penalties. | Overlaps confidence levels, reliability scoring, repeatability, decay, contradiction penalties. | MERGE INTO CORE | Medium: scale confusion if merged carelessly. |
| `projects/orca/evidence/observation-traceability-rules-v1.md` | Observation traceability rules. | Preserves observation IDs, evidence links, source type, context, status, and contradictions. | Repeats evidence context and confidence update traceability. | MERGE INTO CORE | High: traceability is easy to over-compress. |
| `projects/orca/evidence/source-reliability-rules-v1.md` | Source quality discipline. | Distinguishes direct observation, case evidence, client input, secondary reference, synthetic output, SAFE UNKNOWN. | Overlaps evidence strength and confidence penalties. | MERGE INTO CORE | Medium: synthetic-output warning must survive. |
| `projects/orca/evidence/human-validation-rules-v1.md` | Human validation requirements. | Defines when validation is required and possible validation outcomes. | Repeats boundary and human review language across all layers. | MERGE INTO CORE | Medium: avoid deleting validation gates as boilerplate. |
| `projects/orca/confidence/confidence-governance-model-v1.md` | Confidence levels and governance. | Defines LOW/MEDIUM/HIGH/VERY HIGH and increase/decrease rules. | Duplicates evidence strength levels and pattern reliability bands. | APPENDIX | Medium: operators may confuse confidence with evidence strength. |
| `projects/orca/confidence/confidence-update-rules-v1.md` | Confidence update protocol. | Captures previous/new confidence, update reason, new evidence, contradictions, volatility, age. | Overlaps traceability, decay, contradiction handling. | APPENDIX | Medium: useful nuance can be lost during compression. |
| `projects/orca/confidence/repeatability-model-v1.md` | Repeatability classes. | Defines isolated, same-query, cross-query, cross-case, cross-region, cross-source, historical evidence. | Overlaps evidence strength and reliability scoring. | APPENDIX | Low: can be compacted into strength/confidence file. |
| `projects/orca/confidence/evidence-decay-rules-v1.md` | Freshness and decay rules. | Defines current/recent/stale/expired/unknown and decay triggers. | Overlaps confidence update, evidence freshness, volatility, contradictions. | APPENDIX | Medium: stale evidence rules are safety-critical. |
| `projects/orca/confidence/pattern-reliability-scoring-v1.md` | Pattern reliability score aid. | Combines evidence strength, confidence, repeatability, penalties, contradictions, regional/seasonal scope. | Heavily duplicates evidence strength and confidence governance. | ARCHIVE CANDIDATE | High: scoring language may imply false precision. |
| `projects/orca/contradictions/contradiction-tracking-model-v1.md` | Contradiction record model. | Defines contradiction types, required fields, and resolution status. | Repeats evidence context, confidence impact, human review. | KEEP CORE | High: contradiction states must survive. |
| `projects/orca/contradictions/conflicting-observation-rules-v1.md` | Conflict handling rules. | Gives practical rules for preserving both sides and capping confidence. | Overlaps contradiction model and confidence downgrade rules. | MERGE INTO CORE | Medium: conflict examples are useful but compressible. |
| `projects/orca/contradictions/unstable-pattern-handling-v1.md` | Unstable pattern controls. | Prevents unstable findings from becoming rules. | Overlaps confidence, volatility, decay, repeatability. | APPENDIX | Medium: instability guardrails matter. |
| `projects/orca/contradictions/market-volatility-rules-v1.md` | Volatility rules. | Defines volatility sources, levels, and confidence effects. | Overlaps evidence decay, unstable patterns, confidence governance. | APPENDIX | Medium: volatility is important but can be referenced. |
| `projects/orca/operator-decisions/README.md` | Operator decision layer index. | Clear operator-facing purpose and document list. | Repeats boundary and decision discipline. | NEEDS HUMAN REVIEW | Low: future redirect README may replace it. |
| `projects/orca/operator-decisions/operator-decision-model-v1.md` | Decision model. | Defines decision priorities and inputs. | Duplicates evidence strength, contradiction level, uncertainty, escalation references. | KEEP CORE | High: primary operator-facing entrypoint. |
| `projects/orca/operator-decisions/decision-priority-rules-v1.md` | Priority rules. | Keeps high-impact PPC risks first. | Overlaps practical decision and checklist logic. | MERGE INTO CORE | Low: easily folded into decision rules. |
| `projects/orca/operator-decisions/uncertainty-handling-rules-v1.md` | Weak evidence, stop, escalation rules. | Directly tells operator when evidence is weak, when to stop, when to escalate. | Overlaps low-evidence rules, escalation rules, confidence/contradiction penalties. | MERGE INTO CORE | Medium: stop/escalate guidance must remain visible. |
| `projects/orca/operator-decisions/evidence-weighting-rules-v1.md` | Evidence weighting for decisions. | Translates stronger/weaker evidence into act/escalate/stop choices. | Overlaps evidence strength and low-evidence rules. | MERGE INTO CORE | Medium: avoid duplicating a second evidence scale. |
| `projects/orca/operator-decisions/practical-decision-rules-v1.md` | Practical action rules. | Keeps decisions commercially relevant and anti-theory. | Overlaps decision priority and tradeoff rules. | MERGE INTO CORE | Low: high operator value, low unique structure. |
| `projects/orca/operator-decisions/low-evidence-decision-rules-v1.md` | Low-evidence action limits. | Defines allowed low-evidence decisions and forbidden high-risk decisions. | Overlaps uncertainty handling and low-evidence checklist. | KEEP CORE | High: protects against fake confidence. |
| `projects/orca/operator-decisions/operational-tradeoff-rules-v1.md` | Tradeoff framing. | Captures speed/depth, segmentation/simplicity, evidence/action speed. | Overlaps practical decision rules and tradeoff template. | APPENDIX | Low: useful but not core for every review. |
| `projects/orca/operator-decisions/decision-fatigue-rules-v1.md` | Fatigue controls. | Prevents tired operators from over-acting on weak evidence. | Overlaps minimalism/fast-review concepts outside target family and escalation rules. | APPENDIX | Low: useful as safety appendix. |
| `projects/orca/operator-decisions/escalation-rules-v1.md` | Escalation rules. | Defines exact escalation triggers and escalation note fields. | Overlaps uncertainty handling and escalation checklist. | KEEP CORE | High: operator safety depends on visible escalation. |
| `projects/orca/operator-decisions/operator-decision-boundaries-v1.md` | Boundary document. | Explicitly rejects autonomous decision-making and strategic certainty. | Repeats boundary language from README and many files. | MERGE INTO CORE | Low: preserve key boundary, remove repetition later. |
| `projects/orca/operator-decisions/templates/operational-decision-template-v1.md` | General decision template. | Practical fields for evidence, uncertainty, action, defer, escalate, risk. | Overlaps uncertainty/tradeoff templates and checklists. | TEMPLATE | Medium: likely best base for single future template. |
| `projects/orca/operator-decisions/templates/uncertainty-review-template-v1.md` | Uncertainty template. | Focuses on known/unknown, weak evidence, contradictions, dangerous assumptions. | Overlaps operational decision template and low-evidence checklist. | TEMPLATE | Low: merge into one template. |
| `projects/orca/operator-decisions/templates/tradeoff-review-template-v1.md` | Tradeoff template. | Captures tradeoff, supporting/delay evidence, risk accepted, stop point. | Overlaps operational decision template and tradeoff rules. | TEMPLATE | Low: convert to optional fields. |
| `projects/orca/operator-decisions/checklists/decision-quality-checklist-v1.md` | Decision quality checklist. | Quick final check for evidence, uncertainty, contradictions, escalation. | Overlaps operator decision model and operational template. | TEMPLATE | Low: merge into one review template/checklist. |
| `projects/orca/operator-decisions/checklists/low-evidence-checklist-v1.md` | Low-evidence checklist. | Practical check for incomplete source, thin sample, assumptions, contradiction, reversibility. | Overlaps low-evidence rules and uncertainty template. | TEMPLATE | Medium: preserve low-evidence safety. |
| `projects/orca/operator-decisions/checklists/escalation-checklist-v1.md` | Escalation checklist. | Practical escalation triggers and note fields. | Overlaps escalation rules and decision template. | TEMPLATE | Medium: preserve escalation note fields. |

## File-Level Summary

- KEEP CORE: evidence discipline, contradiction tracking, operator decision model, low-evidence decision rules, escalation rules.
- MERGE INTO CORE: evidence strength, traceability, source reliability, human validation, most operator decision rules.
- APPENDIX: confidence lifecycle, repeatability, decay, unstable patterns, volatility, tradeoffs, fatigue.
- TEMPLATE: operator templates and checklists should become one compact evidence review template.
- ARCHIVE CANDIDATE: pattern reliability scoring only after human approval.
- NEEDS HUMAN REVIEW: current `operator-decisions/README.md` because future redirect policy is undecided.

## Boundary

This inventory is not permission to delete, archive, or modify source files.
