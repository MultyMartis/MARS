# ORCA Annotator Readiness Plan v1

**Plan ID:** `orca-annotator-readiness-plan`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Defines a **future** six-step certification process for annotators before they may label benchmark gold rows. Human-operated training plan — not automated certification engine. **No qualification answers are created in this task.**

---

## Scope

- Applies to: trained annotators, second annotators, and adjudicator candidates
- Does not apply to: operator policy approval, LLM assistant configuration, classifier training
- Prerequisite: P0-C guideline operator approval; P0-D benchmark charter for gold-label eligibility

---

## Six-step certification process

### Step 1 — Read taxonomy and guideline

**Activity:** Complete required reading in order per annotation README and handbook Section 4.

**Includes:**
- P0-B taxonomy documents (primary intent, user goal, signal, ambiguity, eligibility, risk, review status)
- Semantic record schema and invariants
- Full annotation guideline (20 sections)
- Commercial evidence, protected non-commercial, problem, product-vs-service, short-head, ACCEPT/REJECT/ABSTAIN, and rationale standards

**Completion criterion:** Annotator attests reading complete; supervisor confirms via checklist sign-off.

**Not in this task:** Automated reading tracking.

---

### Step 2 — Review example library

**Activity:** Study training illustrations in the example library.

**Includes:**
- Minimum coverage areas: clear ACCEPT, clear REJECT, ABSTAIN, problem queries, product-vs-service, career-vs-provider, short-head, difficult counterexamples
- Anti-pattern library review (16 anti-patterns)

**Completion criterion:** Annotator completes guided review session; identifies common wrong decisions in sample set.

**Not in this task:** Example library answers as certification key.

---

### Step 3 — Complete qualification set

**Activity:** Independently annotate a **fixed qualification phrase set** defined in future P0-D charter annex.

**Includes:**
- Blind annotation without peer labels
- Mandatory 10-step order and reviewer checklist
- Phrase-specific rationale for every record

**Completion criterion:** All records submitted with complete schema fields.

**Not in this task:** Qualification phrase set, qualification answers, or scoring rubric numerics.

---

### Step 4 — Compare with adjudicated answers

**Activity:** Compare qualification-set labels against **adjudicated reference answers** prepared by certification lead.

**Includes:**
- Eligibility match rate
- Intent match on disputed cases
- Rationale quality review

**Completion criterion:** Meets charter-defined agreement threshold (PROPOSED — BENCHMARK CHARTER REQUIRED).

**Not in this task:** Adjudicated answer key files.

---

### Step 5 — Pass error analysis

**Activity:** Structured review of every mismatch from Step 4.

**Includes:**
- Classify error type (intent, eligibility, signal, anti-pattern)
- Written correction plan per error
- Re-annotation of failed phrases if required

**Completion criterion:** Certification lead confirms error patterns are understood and not systematic.

**Not in this task:** Error analysis tooling or automated feedback.

---

### Step 6 — Become eligible to annotate benchmark

**Activity:** Operator or certification lead grants **benchmark annotation eligibility**.

**Includes:**
- Record in annotator registry (future)
- Guideline version binding
- Double-annotation pairing assignment

**Completion criterion:** Eligibility recorded; annotator may label **dev split** benchmark rows per P0-D charter. Gold freeze requires separate adjudication pass.

**Not in this task:** Annotator registry implementation; benchmark row assignment.

---

## Explicit exclusions (this task)

- No qualification answer keys
- No certification exam conduct
- No numerical pass/fail thresholds (deferred to P0-D)
- No benchmark rows created
- No automated certification pipeline

---

## Related documents

- [`../reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md`](../reviewer-tools/ORCA-ANNOTATOR-ROLE-MODEL-v1.md)
- [`../reviewer-tools/ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md`](../reviewer-tools/ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md)
- [`ORCA-ANNOTATION-QUALITY-GATES-v1.md`](ORCA-ANNOTATION-QUALITY-GATES-v1.md)
- [`../examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md`](../examples/ORCA-ANNOTATION-EXAMPLE-LIBRARY-v1.md)
