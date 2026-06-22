# ORCA Annotator Role Model v1

**Role model ID:** `orca-annotator-role-model`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## Purpose

Defines human and assisted roles in ORCA Semantic Intelligence annotation and adjudication. Clarifies authority boundaries. Not runtime. Not orchestration product.

---

## Authority hierarchy (annotation context)

1. **Operator** — policy, thresholds, overrides, release gates
2. **Approved annotation guideline** — procedure binding on all annotators
3. **Approved P0-B taxonomy and schema** — vocabulary and record shape
4. **Adjudicator** — resolves disagreement within guideline bounds
5. **Annotators** — produce labels under guideline
6. **Domain expert / PPC specialist** — advisory input; no automatic label authority
7. **LLM assistant** — structured evidence and alternatives only; no final authority

Aligns with ADR v1 authority model and operator decisions D1–D7.

---

## Roles

### Annotator

**Responsibility:** Makes first-pass labels using the approved annotation guideline and mandatory 10-step order.

**May:**
- Assign primary intent, signals, ambiguity, eligibility, risk, and review status per schema
- Request ABSTAIN when evidence is insufficient
- Cite phrase-specific rationale with supporting and opposing evidence

**May not:**
- Override protected-strata rules without adjudication
- Use service scope, frequency, or cluster membership as eligibility proof
- Assign final authority on policy exceptions
- See second annotator labels during independent pass

**Outputs:** Complete semantic record draft with decision trace and provenance.

---

### Second annotator

**Responsibility:** Labels independently **without seeing** the first annotator's decision (blind double annotation).

**May:**
- Apply the same guideline and checklist as first annotator
- Disagree with first annotator — triggers adjudication queue

**May not:**
- Access first-pass labels, rationale, or hints before own submission
- Collapse disagreement without adjudicator review when eligibility differs

**Outputs:** Independent semantic record for disagreement comparison.

---

### Domain expert

**Responsibility:** Clarifies terminology, product/module boundaries, regulatory context, and industry usage.

**May:**
- Explain what a phrase literally means in domain context
- Identify plausible interpretations (product vs module vs service noun)
- Flag when domain knowledge is insufficient → supports ABSTAIN route

**May not:**
- Automatically determine commercial eligibility
- Override PPC landing-fit or protected-intent rules
- Act as sole authority on ACCEPT without commercial evidence standard

**Outputs:** Advisory notes attached to adjudication or ABSTAIN queue; not a substitute for annotation record.

---

### PPC specialist

**Responsibility:** Assesses paid-search suitability, landing-page honesty, spend risk, and campaign-scope fit.

**May:**
- Evaluate landing compatibility (Step 7 of annotation order)
- Flag high spend-risk false positives (protected strata leakage)
- Advise on operator-seed policy for broad head terms

**May not:**
- Force ACCEPT from topical relevance alone
- Suppress ABSTAIN to inflate automation rate
- Determine primary intent without following annotation order

**Outputs:** Landing-fit assessment, spend-risk flags, PPC context for adjudication.

---

### Adjudicator

**Responsibility:** Resolves disagreement between annotators or between annotator and QA.

**May:**
- Issue binding eligibility decision within guideline bounds
- Request additional domain or PPC input
- Escalate to operator when policy threshold or seed exception required
- Preserve prior decisions in audit trail when overturning

**May not:**
- Change operator-approved D3 thresholds
- Approve benchmark gold labels without charter (P0-D)
- Implement classifier or runtime rules

**Outputs:** Adjudicated record with disagreement type, resolution rationale, and preserved prior labels.

See [`../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md`](../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md).

---

### Operator

**Responsibility:** Approves policy, thresholds, overrides, seed lists, and production release gates.

**May:**
- Approve or reject P0-C guideline and P0-D benchmark charter
- Authorize operator-seed ACCEPT with explicit tagging
- Override adjudication in documented exceptional cases
- Freeze or unfreeze Corvonero and campaign production per D2/D7

**May not:**
- Be bypassed for production authorization before P0-G threshold gate
- Delegate final production release to LLM or automated pipeline alone

**Outputs:** Operator approval records, override audit entries, gate status updates.

---

### LLM assistant

**Responsibility:** May provide structured evidence extraction, competing interpretations, and draft rationale **for human review**.

**May:**
- Suggest signals, ambiguity types, and decision-tree paths
- Summarize literal interpretation and likely next action
- Highlight protected-strata conflicts

**May not:**
- Act as final authority on ACCEPT / REJECT / ABSTAIN
- Validate its own output without human rubric (anti-pattern AP-12)
- Write generic template rationales that pass QA without human edit

**Outputs:** Structured suggestions marked `ASSISTANCE_ONLY`; human annotator or adjudicator retains label authority.

---

## Role interaction matrix

| Scenario | Primary actor | Support | Final authority |
|----------|---------------|---------|-----------------|
| First-pass annotation | Annotator | LLM assistant (optional) | Annotator |
| Double annotation | Second annotator | — | Adjudicator if disagree |
| Terminology dispute | Adjudicator | Domain expert | Adjudicator |
| Landing-fit dispute | Adjudicator | PPC specialist | Adjudicator |
| Policy exception | Operator | Adjudicator | Operator |
| Protected-strata conflict | Annotator → ABSTAIN | PPC specialist | Adjudicator / Operator |

---

## Related documents

- [`ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md`](ORCA-SEMANTIC-REVIEWER-CHECKLIST-v1.md)
- [`../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md`](../adjudication/ORCA-ANNOTATION-DISAGREEMENT-POLICY-v1.md)
- [`../quality/ORCA-ANNOTATOR-READINESS-PLAN-v1.md`](../quality/ORCA-ANNOTATOR-READINESS-PLAN-v1.md)
- [`../../../architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-AUTHORITY-MODEL-v1.md`](../../../architecture/semantic-intelligence/ORCA-SEMANTIC-INTELLIGENCE-AUTHORITY-MODEL-v1.md)
