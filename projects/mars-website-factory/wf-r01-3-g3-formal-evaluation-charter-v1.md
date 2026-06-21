# WF-R01.3 Gate G3 Formal Evaluation Charter v1

**Subprogram lane:** WF-R01.3 — Reference Implementation Expansion  
**Gate ID:** **G3**  
**Version:** v1  
**Date:** 2026-06-22  
**Mode:** normative gate evaluation contract — **documentation and evaluation procedure only**

**Honesty boundary:** This charter **authorizes and defines** formal Gate G3 evaluation procedure, criteria, evidence baseline, and decision semantics for **this evaluation pass**. **Charter acceptance does not constitute Gate G3 PASS, G3 CLOSED, operator sign-off, or remediation execution.**

---

## 1. Status

| Field | Value |
|-------|-------|
| **Status** | **ACCEPTED FOR THIS EVALUATION PASS** |
| **Charter decision** | Combined evaluation contract + evaluation artefact per G2 precedent |
| **Gate state after charter** | **EVIDENCE ASSEMBLED · READY FOR FORMAL EVALUATION · NOT EVALUATED · NOT PASSED · NOT CLOSED** |
| **Implementation state** | **NOT AUTHORIZED** by this charter alone |
| **Coverage impact** | **None** — metrics frozen at G3-E snapshot |

---

## 2. Gate Identity

| Field | Value |
|-------|-------|
| **Gate ID** | **G3** |
| **Canonical name** | **ECOMMERCE + CORPORATE reference slice** |
| **Formal evaluation name** | **WF-R01.3 G3-F — Formal Gate Evaluation** |
| **Parent programme** | **WF-R01.3** — Reference Implementation Expansion |
| **Delivery subprogramme** | **WF-R01.3.5** — Corporate & Commerce Reference Slices |
| **Predecessor gate** | **G2 — CLOSED** · **PASS WITH NON-BLOCKING DEBT** |
| **Successor gate** | **G4 — Full Core reference** (RPC 32/32 + full Core SC) |
| **Entry requirement** | G3-E evidence pack **READY FOR FORMAL EVALUATION** |
| **Evaluation owner** | Technical evaluation in Cursor pass (G3-F) |
| **Human decision owner** | Operator — **named steward SAFE UNKNOWN** |
| **Closure boundary** | Only after accepted operator decision on evaluation artefact |

---

## 3. Authority

| Document | Path | Role |
|----------|------|------|
| G3 evidence pack | [wf-r01-3-g3-evidence-pack-v1.md](wf-r01-3-g3-evidence-pack-v1.md) | **Primary evidence baseline** · criteria G3-C01–G3-C18 |
| G3-E assembly report | [wf-r01-3-g3-evidence-assembly-v1.md](../../reports/wf-r01-3-g3-evidence-assembly-v1.md) | Assembly verification |
| WF-R01.3.5 charter | [wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md](wf-r01-3-5-corporate-commerce-reference-slices-charter-v1.md) | G3 Readiness Contract §30 · substitution · G3/G4 split |
| W6-G3R reconciliation | [wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md](wf-r01-3-5-w6-g3r-g3-readiness-reconciliation-v1.md) | Criteria extraction · gap matrix |
| W7-CD evidence | [wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md](wf-r01-3-5-w7-cd-corporate-slice-blueprint-evidence-v1.md) | Corporate/ecommerce slice evidence |
| W6-D · W6-B reports | [reports](../../reports/) | Commerce utility · block RPC evidence |
| Coverage Model | [wf-r01-3-1-coverage-model-charter-v1.md](wf-r01-3-1-coverage-model-charter-v1.md) | Five dimensions · G0–G4 gates |
| Program design | [wf-r01-3-reference-expansion-program-design-v1.md](../../reports/wf-r01-3-reference-expansion-program-design-v1.md) | G3 gate definition |
| G2 evaluation precedent | [wf-r01-3-g2-formal-gate-pass-charter-v1.md](wf-r01-3-g2-formal-gate-pass-charter-v1.md) · [wf-r01-3-g2-formal-evaluation-decision-v1.md](wf-r01-3-g2-formal-evaluation-decision-v1.md) | **Procedural precedent only** — criteria not auto-transferred |

**Authority hierarchy for G3 criteria:** G3 evidence pack §9 **>** WF-R01.3.5 charter §30 **>** W6-G3R **>** Coverage Model G3 gate table.

---

## 4. Purpose

Execute evidence-based formal evaluation of Gate G3 after G3-E evidence assembly complete. Publish G3-F formal evaluation decision. Recommend technical Gate decision. Prepare operator decision record without granting human PASS or closure.

**G3 confirms (on PASS):**

- RPC ≥ 29/32 with W6 binding partials CART · CHECKOUT · PAYMENT
- ECOMMERCE utility scaffolds and staging chain evidence
- CORPORATE pilot minimum with documented substitution policy
- Five-dimension snapshot reconciliation without unauthorized accrual
- Operator-reviewed formal gate REPORT

**G3 does not confirm:**

```text
production readiness
full RPC 32/32
RSC 11/11
ECOMMERCE PC accrual
DELIVERY implementation
dedicated FEATURES / REVIEWS / MAP partials
Template-Art completion
Website Factory production-ready
automatic G4 start
automatic Pilot Readiness start
```

---

## 5. Scope

- Gate identity confirmation
- Criteria freeze G3-C01–G3-C18 from evidence pack
- G3-E evidence-pack integrity verification
- Five-dimension coverage reconciliation (no accrual)
- RC · RPC · RSC · SC · PC evaluation
- Corporate pilot · ecommerce staging · substitution waiver evaluation
- Blueprint-instance evaluation
- Build evidence verification (G3-E baseline)
- Debt classification (blocking vs non-blocking vs G4-only)
- Technical Gate decision recommendation
- Operator decision record template (unfilled)

---

## 6. Out of Scope

- Human operator sign-off
- Gate CLOSED state
- WF-R01.3.5 subprogram completion
- G4 implementation start
- Pilot Readiness package
- Pilot project workspace
- Implementation mutation
- Registry / Coverage Model / metric accrual changes
- Production readiness claims

---

## 7. Evidence Baseline

**Canonical input:** [wf-r01-3-g3-evidence-pack-v1.md](wf-r01-3-g3-evidence-pack-v1.md) v1 · published 2026-06-21 · G3-E **COMPLETE WITH RECORDED DEBT**.

**Coverage freeze at evaluation open:**

```text
RC  = 32/32
RPC = 29/32
RSC = 7/11
SC  = LANDING PASS · CATALOG PASS · PROMO PASS
      CORPORATE pilot evidence assembled with substitution debt
      ECOMMERCE staging evidence assembled
PC  = 1/1 LANDING · 1/1 CATALOG corridor · 1/1 PROMO corridor
      ECOMMERCE not accrued
```

---

## 8. Criteria Source

Extract **G3-C01–G3-C18** from evidence pack §9. **No additions or deletions** without explicit authority conflict resolution.

**Allowed per-criterion results:**

```text
PASS
PASS WITH NON-BLOCKING DEBT
CONDITIONAL
FAIL
NOT APPLICABLE
G4-ONLY
SAFE UNKNOWN
```

---

## 9. Decision Vocabulary

| Decision | Meaning |
|----------|---------|
| **PASS RECOMMENDED** | All mandatory criteria PASS; zero mandatory FAIL |
| **PASS WITH NON-BLOCKING DEBT RECOMMENDED** | Mandatory criteria met; recorded debt does not block G3 floor |
| **CONDITIONAL PASS — REMEDIATION REQUIRED** | Gate pass requires named remediation before operator approval |
| **FAIL — BLOCKING EVIDENCE GAPS** | One or more mandatory criteria FAIL |
| **EVALUATION BLOCKED BY AUTHORITY** | Irreconcilable authority conflict — stop |

**Mandatory FAIL > 0** → **PASS RECOMMENDED forbidden**.

---

## 10. Debt Classification

| Class | G3 effect |
|-------|-----------|
| **Non-blocking debt** | May carry forward with operator approval |
| **G4-only debt** | Not evaluated as G3 blocker unless authority conflict |
| **Blocking gap** | Mandatory criterion FAIL — blocks PASS recommendation |
| **Substitution waiver** | Requires explicit G3-F decision per charter §30 |

---

## 11. Operator Boundary

- Cursor / technical pass publishes **recommendation only**
- Operator records decision in evaluation artefact §26
- **Named steward:** **SAFE UNKNOWN** unless canonical authority names one
- Cursor **must not** write operator decision · date · identity

---

## 12. Closure Boundary

Gate G3 **CLOSED** only after:

1. G3-F evaluation **PUBLISHED**
2. Operator decision **RECORDED** (APPROVE or APPROVE WITH RECORDED NON-BLOCKING DEBT)
3. Separate closure task updates roadmap · OPERATIONAL-INDEX

**This charter + evaluation do not close the gate.**

---

## 13. Remediation Boundary

Remediation packages (implementation waves · coverage accrual · dedicated partials) are **separate authorized tasks**. G3-F evaluation **does not execute** remediation unless technical decision is **CONDITIONAL PASS — REMEDIATION REQUIRED**.

---

## 14. Formal Evaluation Procedure

1. Duplicate evaluation check — stop if accepted G3 evaluation exists
2. Git / state freeze — record branch · HEAD · exclude foreign WIP
3. Evidence inventory — G3-E pack + bound wave reports
4. Criterion-by-criterion audit — G3-C01–G3-C18
5. Five-dimension reconciliation — no accrual
6. Substitution · corporate · ecommerce · PC · blueprint evaluation
7. Debt classification
8. Technical Gate decision — single outcome from §9 vocabulary
9. Operator decision record — template only
10. Roadmap / index sync — **EVALUATED · NOT CLOSED**
11. Selective Git checkpoint

---

## 15. Post-G3 Eligibility (informational)

After operator approval, **separate human lifecycle decision** required among:

- Operator Gate closure task
- Pilot Readiness decision
- G4 continuation
- Stable pause

**G4:** NOT STARTED by this charter. **Pilot Readiness:** NOT STARTED by this charter.

---

*Combined evaluation contract — accepted for WF-R01.3 G3-F evaluation pass · v1 · 2026-06-22*
