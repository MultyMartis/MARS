# ORCA Annotation Disagreement Policy v1

**Policy ID:** `orca-annotation-disagreement-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-annotation-disagreement-policy-v1.json`](orca-annotation-disagreement-policy-v1.json)

---

## Purpose

Defines how annotator disagreement is classified, adjudicated, escalated, and preserved as benchmark metadata. Human-operated protocol — not automated orchestration.

---

## Disagreement types

| Type ID | Name | Description | Typical trigger |
|---------|------|-------------|-----------------|
| DGT-01 | Intent disagreement | Different primary or secondary intent assignment | Competing interpretations after Step 4 |
| DGT-02 | Eligibility disagreement | ACCEPT vs REJECT vs ABSTAIN differ | After Step 8 |
| DGT-03 | Signal disagreement | Different signal types, strength, or evidence spans | Step 3 extraction |
| DGT-04 | Ambiguity disagreement | Different ambiguity type or severity | Step 5 assessment |
| DGT-05 | Service-candidate disagreement | Different candidate service mapping pre-ACCEPT | Step 13 handling |
| DGT-06 | Risk disagreement | Different risk level or review requirement | Step 9 |
| DGT-07 | Rationale-quality disagreement | Same eligibility but insufficient or generic rationale | QA rubric failure |

Multiple types may apply to one case. Record **all** applicable types in adjudication metadata.

---

## What requires adjudication

**Mandatory adjudication** when:

- Two independent annotators disagree on **eligibility** (ACCEPT / REJECT / ABSTAIN)
- Eligibility differs and at least one label is **ACCEPT**
- Either annotator assigned **protected-strata** primary intent and the other assigned commercial path
- QA flags **rationale-quality** failure on ACCEPT or borderline ABSTAIN
- **Service-candidate** mapping conflicts on an ACCEPT-bound record
- Annotator and automated schema validator disagree on required fields (shape only — not classifier)

**May proceed without adjudication** when:

- Disagreement is **cosmetic** (wording of rationale) and eligibility, intent, and risk match — QA may reconcile copy
- **Mechanical reconciliation** applies (see below)

---

## Mechanical reconciliation (no adjudicator)

Allowed only when eligibility and primary intent **already match**:

| Field | Rule |
|-------|------|
| Secondary intent | Keep more conservative (non-commercial preferred) |
| Signal strength | Keep weaker strength when spans overlap |
| Ambiguity severity | Keep higher severity |
| Risk level | Keep max(dimension) per risk taxonomy |
| Rationale wording | Merge phrase-specific elements; reject generic templates |

If mechanical reconciliation would **change eligibility or primary intent** → full adjudication required.

---

## Adjudication procedure

1. **Freeze** both annotator records; preserve originals unchanged
2. **Classify** disagreement type(s)
3. **Re-run** mandatory checklist (RC-01–RC-12) on disputed phrase
4. **Consult** domain expert or PPC specialist if terminology or landing-fit is disputed
5. **Issue** adjudicated record with:
   - Final eligibility and intent
   - Disagreement type(s)
   - Resolution rationale (phrase-specific)
   - Reference to guideline section applied
6. **Route** to operator if escalation triggers apply

---

## Prior decision preservation

- Original annotator records are **immutable** after submission
- Adjudicated record references `prior_annotation_ids[]`
- Overturns must state **which prior label was rejected** and **why**
- Operator overrides reference adjudication ID when overturning adjudicator

---

## Override authority

| Actor | May override | May not override |
|-------|--------------|------------------|
| Adjudicator | Annotator labels within guideline | D3 thresholds; operator seed policy |
| Operator | Adjudicator; policy exceptions | ADR v1 admission outputs (ACCEPT/REJECT/ABSTAIN only) |
| LLM assistant | — | Any human label |

---

## Operator escalation (mandatory)

Escalate to operator when:

- Adjudicator cannot resolve within guideline without **new policy**
- **Operator-seed ACCEPT** is proposed for a phrase lacking Wordstat-proven demand
- Disagreement involves **protected-strata ACCEPT** on auto-admit path
- Repeated disagreement on same ambiguity class exceeds charter threshold (future P0-D)
- **Benchmark gold label** candidacy is disputed (P0-D onward only)

Escalation record must include: phrase, disagreement types, annotator IDs, adjudicator notes, recommended operator action.

---

## Benchmark metadata

Disagreement cases feed benchmark design (P0-D charter). For each adjudicated case, capture:

| Metadata field | Purpose |
|----------------|---------|
| `disagreement_types[]` | Stratify benchmark by failure mode |
| `protected_strata_involved` | Per-class FPR analysis (D3) |
| `adjudication_outcome` | Gold label source = adjudicated |
| `prior_labels[]` | Inter-annotator agreement metrics |
| `resolution_time` | Operational load tracking |
| `escalated_to_operator` | Policy gap detection |
| `ambiguity_class` | Ambiguity recall evaluation |
| `guideline_section_cited` | Guideline gap detection |

**This task does not create benchmark rows.** Metadata schema is defined for future P0-D/E use.

---

## Related documents

- [`../reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md`](../reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md)
- [`../quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md`](../quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md)
- [`../guidelines/ORCA-ABSTAIN-STANDARD-v1.md`](../guidelines/ORCA-ABSTAIN-STANDARD-v1.md)
