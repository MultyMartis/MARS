# Merge Duplication Matrix v1

## Status

Controlled duplication matrix only. No source files changed.

## Scope

This matrix covers only `evidence`, `confidence`, `contradictions`, and `operator-decisions`.

## Matrix

| Duplicated concept | `evidence` | `confidence` | `contradictions` | `operator-decisions` | Compression note |
|---|---|---|---|---|---|
| Evidence quality | Core evidence discipline, strength, source reliability | Used to raise/lower confidence | Used to preserve conflicting evidence | Used to weight decisions | Keep source in `evidence`; reference elsewhere. |
| Confidence level | Evidence record includes confidence and strength | Owns LOW/MEDIUM/HIGH/VERY HIGH and updates | Applies confidence caps | Uses confidence indirectly through low-evidence rules | Merge level definitions or clearly separate strength vs confidence. |
| Weak evidence | WEAK strength and SAFE UNKNOWN | LOW confidence and insufficient evidence handling | Open or unresolved conflicts | Low-evidence decision rules | One shared weak-evidence rule should feed decisions. |
| Freshness and decay | Evidence freshness and stale penalties | Evidence decay and update rules | Stale vs current conflict | Escalate/defer if evidence is incomplete | Keep decay as confidence appendix; avoid repeat in every decision doc. |
| Volatility | SERP and market volatility reduce strength | Volatility reduces confidence | Volatility can make contradictions unstable | Volatility can trigger escalation | One volatility rule should be referenced by all. |
| Human review | Required before use | Required before confidence updates | Required before resolution | Required for business decisions | Keep as shared boundary language, not repeated heavily. |
| SAFE UNKNOWN | Evidence record field | Missing context handling | Resolution status option | Decision output and uncertainty field | Keep one definition; reuse everywhere. |
| Source context | Timestamp, region, niche, device | Scope in updates | Required in conflict tracking | Evidence source in templates | Standardize one minimal context field set. |
| Contradiction impact | Evidence record links contradictions | Contradictions reduce confidence | Core contradiction model | Contradictions reduce decision confidence | Contradiction logic should live in `contradictions`; decision layer should reference. |
| Escalation | Human validation before strategic use | Not primary | Human review before resolution | Core escalation rules | Keep escalation in `operator-decisions`. |

## Duplicated Review Logic

| Review logic | Duplication pattern | Proposed owner |
|---|---|---|
| Record evidence before interpretation | Appears as evidence discipline and decision discipline. | `evidence` |
| Downgrade weak or stale evidence | Appears in evidence strength, confidence update, and low-evidence decisions. | `confidence` appendix under evidence core |
| Preserve contradictions | Appears in evidence, contradictions, confidence, and decisions. | `contradictions` |
| Stop when evidence is weak and low impact | Appears in operator decisions and evidence caution rules. | `operator-decisions` |
| Escalate high-impact uncertainty | Appears in operator decisions and human validation rules. | `operator-decisions` |

## Duplicated Uncertainty Logic

| Uncertainty condition | Repeated in | Compression direction |
|---|---|---|
| Missing region, niche, timestamp, or device | `evidence`, `confidence`, `contradictions` | Standardize as minimal evidence context. |
| Incomplete source data | `evidence`, `operator-decisions` | Evidence records it; decisions act on it. |
| Contradictions unresolved | all four layers | Contradictions own state; confidence and decisions reference impact. |
| Assumptions driving conclusion | `evidence`, `operator-decisions` | Keep in decision checklist, referenced from evidence discipline. |

## Duplicated Confidence Logic

| Confidence logic | Repeated in | Compression direction |
|---|---|---|
| LOW/WEAK evidence | `evidence-strength-model`, `confidence-governance-model`, `low-evidence-decision-rules` | Use one low-evidence definition. |
| Increase requires repeated comparable evidence | `evidence-strength-model`, `confidence-governance-model`, `confidence-update-rules` | Keep once in confidence lifecycle appendix. |
| Decrease for stale, volatile, missing context | `evidence`, `confidence`, `contradictions` | Keep once in confidence lifecycle appendix. |
| Contradictions cap confidence | `confidence`, `contradictions`, `operator-decisions` | Contradiction impact should be a shared rule. |

## Duplicated Contradiction Handling

| Contradiction handling | Repeated in | Compression direction |
|---|---|---|
| Do not delete conflicting evidence | `evidence`, `contradictions` | Keep in contradiction appendix. |
| Preserve region/niche/device/timestamp | `evidence`, `contradictions`, `confidence` | Use standard evidence context fields. |
| Bound instead of forcing resolution | `contradictions`, `confidence` | Keep in contradiction appendix. |
| Use SAFE UNKNOWN when unresolved | all four layers | Shared SAFE UNKNOWN definition. |

## Duplicated Operational Guidance

| Guidance | Repeated in | Compression direction |
|---|---|---|
| ORCA does not make business decisions | `operator-decisions`, evidence boundaries, confidence boundaries | Keep as shared boundary. |
| Not automation / telemetry / runtime | all target families | Replace repeated paragraphs with short standard boundary later. |
| Escalation is healthy | `operator-decisions`, human validation | Keep in operator-facing layer. |
| Simplicity beats theoretical perfection | `operator-decisions`, consolidation docs | Keep in operator-facing layer. |

## Boundary

This matrix identifies duplication. It does not authorize pruning by itself.
