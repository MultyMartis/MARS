# ORCA Semantic Annotation Guideline Decision v1

**Decision ID:** `orca-semantic-annotation-guideline-decision`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `APPROVED — IMPLEMENTATION NOT STARTED`  
**Machine reference:** [`orca-semantic-annotation-guideline-decision-v1.json`](orca-semantic-annotation-guideline-decision-v1.json)

---

## Decision summary

Proposed P0-C **implementation-neutral** human annotation and adjudication guideline package for ORCA Semantic Intelligence v1. Binds annotators to P0-B taxonomy and schema. Not runtime. Not classifier. Not benchmark.

---

## Selected annotation process

| Area | Selection |
|------|-----------|
| Unit of annotation | Single search phrase (query string) per semantic record |
| Mandatory order | 10-step sequence: literal → goal → signals → intent → ambiguity → provider-hire → landing → eligibility → risk → trace |
| Terminal outputs | ACCEPT / REJECT / ABSTAIN only — no direct service mapping or campaign grouping |
| Evidence model | Strong/weak commercial signals; evidence ≠ auto-trigger |
| Protected strata | Career, education, DIY, regulatory, navigational, free/download — conservative defaults |
| Problem queries | Three interpretations (paid specialist / DIY / insufficient evidence) |
| Short head terms | Evidence or operator seed required; frequency ≠ intent |
| ABSTAIN governance | Mandatory when ambiguity unresolved; not lazy annotation |
| Rationale | Phrase-specific six-element rubric; generic templates prohibited |
| Double annotation | Blind second pass; adjudication on eligibility disagreement |

---

## Selected reviewer roles

Per [`../reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md`](../reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md):

- Annotator, Second annotator, Domain expert, PPC specialist, Adjudicator, Operator, LLM assistant (assistance only)

---

## Decision order

Commercial eligibility (Step 8) is assigned **only after** literal interpretation, user goal, signals, primary/secondary intent, ambiguity assessment, provider-hire likelihood, and landing compatibility checks. No step may be skipped.

---

## Evidence standard

[`../guidelines/ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md`](../guidelines/ORCA-COMMERCIAL-EVIDENCE-STANDARD-v1.md) — strong explicit provider-facing signals required for ACCEPT path; weak contextual signals may route to ABSTAIN.

---

## ABSTAIN governance

[`../guidelines/ORCA-ABSTAIN-STANDARD-v1.md`](../guidelines/ORCA-ABSTAIN-STANDARD-v1.md) — mandatory ABSTAIN conditions; requires unresolved question, competing interpretations, missing evidence, review route, and risk level.

Aligns with operator decision D4 (explicit ABSTAIN mandatory on insufficient evidence).

---

## Example library role

Training illustrations in [`../examples/`](../examples/) — **not** gold benchmark labels. Old Corvonero labels forbidden as annotation truth. Minimum class coverage per validation V-11.

---

## Disagreement policy

[`../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md`](../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md) — seven disagreement types; mandatory adjudication triggers; operator escalation rules; benchmark metadata schema for P0-D.

---

## Quality gate approach

[`../quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md`](../quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md) — ten proposed annotation metrics; D3 thresholds (commercial precision ≥ 0.95, protected FPR ≤ 0.01) operator-approved; all other numerics PROPOSED — BENCHMARK CHARTER REQUIRED.

---

## Unresolved decisions (defer to P0-D and later)

| ID | Topic | Notes |
|----|-------|-------|
| U-C01 | Qualification set phrases and pass threshold | Annotator readiness Step 3–4 |
| U-C02 | Double-annotation sample rate | P0-D benchmark charter |
| U-C03 | Annotator agreement κ target | P0-D charter |
| U-C04 | Operator seed list governance | VALIDATED_OPERATOR_SEED workflow |
| U-C05 | Automated rationale repetition validator | Post-guideline tooling |
| U-C06 | Adjudication SLA timing | Operational capacity |
| U-C07 | LLM prompt boundary document | Evidence-only vs label authority |

---

## Consequences

1. **P0-B taxonomy and schema** remain canonical vocabulary — guideline does not extend enums without new gate.
2. **Benchmark** remains NOT STARTED until P0-C operator approval and P0-D charter.
3. **Corvonero** remains FROZEN — no relabel from this package.
4. **Campaign production** remains BLOCKED per D7.
5. **Classifier and runtime** remain NOT STARTED.
6. **Training examples** must not be promoted to gold without adjudication and charter freeze.

---

## Next gate

**P0-D Universal Benchmark Charter** — operator approval required before B0 qualification, Corvonero pilot selection, or baseline implementation.

---

## Approval record

| Role | Name | Date | Status |
|------|------|------|--------|
| Operator | Approved | 2026-06-22 | APPROVED — IMPLEMENTATION NOT STARTED (C1–C7) |
| P0-B authority | Approved | 2026-06-22 | APPROVED — CHECKPOINTED |
| P0-C package | This decision | 2026-06-22 | APPROVED — IMPLEMENTATION NOT STARTED |
| P0-C operator approval | [`ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md`](ORCA-P0-C-ANNOTATION-GUIDELINE-OPERATOR-APPROVAL-v1.md) | 2026-06-22 | APPROVED |

---

## Related documents

- [`../README.md`](../README.md)
- [`../validation/ORCA-ANNOTATION-GUIDELINE-VALIDATION-v1.md`](../validation/ORCA-ANNOTATION-GUIDELINE-VALIDATION-v1.md)
- [`../../decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md`](../../decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md)
