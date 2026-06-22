# ORCA Annotation Guideline Validation v1

**Validation ID:** `orca-annotation-guideline-validation`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `APPROVED — DOCUMENTATION VALIDATION`  
**Machine reference:** [`orca-annotation-guideline-validation-v1.json`](orca-annotation-guideline-validation-v1.json)

---

## Purpose

Documentation validation plan for P0-C ORCA Semantic Annotation Guideline package. Validates guideline completeness against P0-B taxonomy, mandatory annotation order, and task Part 25 criteria. **Not** classifier benchmark. **Not** runtime proof.

---

## Validation checks (Part 25)

| ID | Criterion | Method | Expected |
|----|-----------|--------|----------|
| V-01 | All approved taxonomy values represented | Crosswalk guideline + standards ↔ P0-B taxonomy JSON | No orphan vocabulary; intent/signal/ambiguity/eligibility/risk/review enums referenced |
| V-02 | Annotation order explicit | Review handbook Section + guideline Part 7 | 10-step mandatory sequence documented; no step skippable |
| V-03 | ACCEPT/REJECT/ABSTAIN rules distinct | Compare ACCEPT, REJECT, ABSTAIN standards | Non-overlapping terminal rules; seven ACCEPT requirements; REJECT triggers separate |
| V-04 | Problem queries do not auto-accept | Review problem-query adjudication standard | Problem signal alone ≠ ACCEPT; I1/I2/I3 interpretations |
| V-05 | Topic match does not auto-accept | Review commercial evidence + anti-patterns | Evidence ≠ auto-trigger; topic ≠ intent |
| V-06 | Product/service distinction exists | Review product-vs-service adjudication | Product-only REJECT path; integration may ACCEPT; ambiguity → ABSTAIN |
| V-07 | Career/provider distinction exists | Review protected non-commercial standard | Career seeker vs customer; employee hiring ≠ service demand |
| V-08 | DIY/provider distinction exists | Review problem + protected standards | How-to / DIY vs paid specialist; unresolved → ABSTAIN |
| V-09 | Short-head policy exists | Review short-head adjudication standard | Generic nouns, roles, modules, regulatory names; frequency ≠ intent |
| V-10 | ABSTAIN routes exist | Review ABSTAIN standard + decision trees | Mandatory ABSTAIN conditions; unresolved question required |
| V-11 | Examples cover all required classes | Inventory example library | ≥20 ACCEPT, ≥20 REJECT, ≥20 ABSTAIN; problem, product/service, career/provider, short-head, counterexamples |
| V-12 | Rationales phrase-specific | Review rationale standard + checklist RC-11 | Six required elements; prohibited generic templates listed |
| V-13 | No benchmark created | Directory scan annotation locus | No gold benchmark rows; no `benchmark/` dataset |
| V-14 | No Corvonero corpus relabelled | Directory scan + manifest | No full corpus labels; training illustrations only |
| V-15 | No classifier/runtime implemented | Directory scan | No classifier code, runtime, or production semantic pipeline in P0-C scope |

---

## Execution procedure

1. **Taxonomy crosswalk** — Link each P0-B taxonomy JSON to handbook sections and standards.
2. **Order audit** — Verify 10 steps appear in handbook, decision trees, and reviewer checklist.
3. **Terminal rule audit** — Confirm every decision-tree subtree ends in ACCEPT, REJECT, or ABSTAIN only.
4. **Example inventory** — Count examples per class in example library JSON manifest.
5. **Negative scope scan** — Confirm no benchmark rows, Corvonero relabels, or classifier artifacts.
6. **Operator review** — P0-C package approved as `APPROVED — IMPLEMENTATION NOT STARTED` (C1–C7).

---

## Out of scope (P0-C validation)

- Inter-annotator agreement measurement
- Classifier accuracy on blind test
- Live campaign validation
- AJV runtime validator execution (deferred per B6)
- Gold label adjudication

---

## Results summary

Machine-readable check manifest in JSON counterpart. Package approved by operator 2026-06-22 (C1–C7). Benchmark charter (P0-D) authorized but not started.

---

## Related documents

- [`../decisions/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md`](../decisions/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-DECISION-v1.md)
- [`../../validation/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-VALIDATION-v1.md`](../../validation/ORCA-SEMANTIC-TAXONOMY-AND-SCHEMA-VALIDATION-v1.md)
- [`../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md)
