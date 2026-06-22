# ORCA Semantic Reviewer Checklist v1

**Checklist ID:** `orca-semantic-reviewer-checklist`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-semantic-reviewer-checklist-v1.json`](orca-semantic-reviewer-checklist-v1.json)

---

## Purpose

Pre-submit and QA checklist for human reviewers of ORCA Semantic Intelligence annotation records. Applies to first-pass annotators, second annotators, adjudicators, and QA reviewers. Not runtime. Not classifier.

---

## When to use

- Before submitting any annotation record for review
- During double-annotation QA sampling
- During adjudication of disagreement cases
- During annotator certification error analysis (future)

---

## Mandatory checklist items

Complete **all** items before marking a record `READY_FOR_REVIEW` or equivalent workflow status.

| ID | Question | Failure action |
|----|----------|----------------|
| RC-01 | Did I interpret the phrase **literally** — without imagined business context or desired paid outcome? | Revise literal interpretation; do not proceed |
| RC-02 | Did I identify the **likely next user action** (hire, buy, learn, DIY, navigate, etc.)? | Complete Step 2 of annotation order |
| RC-03 | Did I **separate topic from intent** — topical relevance ≠ commercial eligibility? | Re-assess primary intent before eligibility |
| RC-04 | Did I consider the **strongest non-commercial interpretation** (career, education, DIY, regulatory, navigational, free/download)? | Apply protected non-commercial standard |
| RC-05 | Did I **distinguish service from product** (buy module vs hire specialist)? | Apply product-vs-service adjudication |
| RC-06 | Did I **distinguish provider from career** (customer seeking service vs job seeker / employer hiring)? | Apply protected non-commercial standard |
| RC-07 | Did I **distinguish provider from DIY** (paid specialist vs self-service how-to)? | Apply problem-query or DIY rules |
| RC-08 | Can an **honest service landing page** directly satisfy this query without changing its meaning? | If no → REJECT or ABSTAIN, not ACCEPT |
| RC-09 | Did I **avoid using service scope as proof of demand** (scope presence ≠ eligibility)? | Remove scope-based reasoning from rationale |
| RC-10 | Is **ABSTAIN required** — unresolved ambiguity, conflicting signals, or insufficient evidence? | Assign ABSTAIN with unresolved question |
| RC-11 | Is the rationale **phrase-specific** — not generic template text? | Rewrite per phrase-specific rationale standard |
| RC-12 | Are **provenance and versions** present (guideline version, annotator ID, timestamp)? | Complete audit fields before submit |

---

## Extended QA checks (reviewer / adjudicator)

| ID | Question | Applies to |
|----|----------|------------|
| RC-13 | Did the annotator follow the **10-step mandatory annotation order** without skipping? | QA reviewer |
| RC-14 | Are **signals** recorded with positive and negative evidence separated? | QA reviewer |
| RC-15 | Was **commercial eligibility assigned only after** intent, ambiguity, and landing checks? | QA reviewer |
| RC-16 | Does the **decision trace** link evidence to final ACCEPT / REJECT / ABSTAIN? | QA reviewer |
| RC-17 | Is **service candidate** status distinct from eligibility (CANDIDATE_ONLY pre-ACCEPT)? | QA reviewer |
| RC-18 | Are **protected strata** handled conservatively when signals conflict? | QA reviewer |
| RC-19 | Was **ABSTAIN** used appropriately — not as lazy annotation or hidden ACCEPT? | QA reviewer |
| RC-20 | Does the record validate against **semantic record schema v1** (shape only)? | QA reviewer |

---

## Anti-pattern quick scan

If any of the following are detected, **block submission** until corrected:

- Service-term presence treated as automatic ACCEPT
- Topic match treated as commercial intent
- Error/problem treated as provider intent without explicit support signal
- Model confidence or cluster membership treated as evidence
- Copied or generic rationale
- Semantic decision deferred to export or campaign grouping

See [`../examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md`](../examples/ORCA-SEMANTIC-ANNOTATION-ANTI-PATTERNS-v1.md).

---

## Related documents

- [`../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md`](../guidelines/ORCA-SEMANTIC-ANNOTATION-GUIDELINE-v1.md)
- [`ORCA-ANNOTATOR-ROLE-MODEL-v1.md`](ORCA-ANNOTATOR-ROLE-MODEL-v1.md)
- [`../quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md`](../quality/ORCA-ANNOTATION-QUALITY-GATES-v1.md)
