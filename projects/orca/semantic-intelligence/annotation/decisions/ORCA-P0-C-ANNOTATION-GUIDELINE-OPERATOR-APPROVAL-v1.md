# ORCA P0-C — Annotation Guideline Operator Approval v1

**Record ID:** `orca-p0-c-annotation-guideline-operator-approval`  
**Version:** v1  
**Date:** 2026-06-22  
**Authority:** Human operator — MARS ORCA governance  
**Machine reference:** [`orca-p0-c-annotation-guideline-operator-approval-v1.json`](orca-p0-c-annotation-guideline-operator-approval-v1.json)

---

## Purpose

Formal record of operator approval for P0-C ORCA Semantic Annotation Guideline v1, and authorization of P0-D Universal Benchmark Charter work.

---

## C1 — Guideline status

**Decision:** `APPROVED — IMPLEMENTATION NOT STARTED`

The annotation handbook, standards, decision trees, example library, anti-pattern library, reviewer checklist, annotator role model, disagreement policy, quality gates, and annotator readiness plan are approved as specification authority. No annotator certification, benchmark labels, classifier, or runtime implementation is authorized by this approval.

---

## C2 — Annotation order

**Approved mandatory order:**

1. literal interpretation;
2. likely next user action;
3. signal extraction;
4. primary and secondary intent;
5. competing interpretations;
6. provider-hire likelihood;
7. landing compatibility;
8. ACCEPT / REJECT / ABSTAIN;
9. risk and review requirement;
10. decision trace.

---

## C3 — ABSTAIN governance

**Decision:** Approved as mandatory safety outcome for unresolved ambiguity.

ABSTAIN is a valid terminal annotation outcome when evidence is insufficient, competing interpretations remain unresolved, or protected-intent risk requires conservative routing. ABSTAIN is not lazy annotation or a substitute for adjudication when disagreement exists.

---

## C4 — Example-library authority

**Decision:** Training illustrations only.

The example library and anti-pattern library are **not**:

- benchmark labels;
- gold truth;
- automatic production authority.

Promotion to gold requires independent re-annotation, adjudication, and benchmark freeze per future P0-D charter.

---

## C5 — Double annotation direction

**Decision:** Authorized for benchmark design.

Independent double annotation is approved as the benchmark annotation model direction. Exact operational SLA, sample rates, and long-term percentage remain to be defined in P0-D.

---

## C6 — Numerical quality thresholds

**Operator-approved (D3):**

- Commercial Precision on auto-accept >= 0.95;
- protected-strata FPR <= 0.01 per protected class.

**All other numerical thresholds:**

`PROPOSED — BENCHMARK VALIDATION REQUIRED`

---

## C7 — P0-D authorization

**Decision:** `AUTHORIZED`

Operator authorizes drafting of P0-D — ORCA Universal Semantic Benchmark Charter v1. P0-D requires separate operator approval before B0 qualification execution, Corvonero pilot selection, or baseline implementation.

---

## Related documents

- [`ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md`](ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md)
- [`../README.md`](../README.md)
- [`../../decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md`](../../decisions/ORCA-P0-B-TAXONOMY-AND-SCHEMA-OPERATOR-APPROVAL-v1.md)
