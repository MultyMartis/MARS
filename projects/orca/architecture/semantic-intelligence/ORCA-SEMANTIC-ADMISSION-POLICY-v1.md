# ORCA Semantic Intelligence — Admission Policy v1

**Policy ID:** `orca-semantic-admission-policy`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Layer:** SI-08 Commercial Eligibility (+ SI-09 adjudication for ABSTAIN)

---

## Outcomes

Commercial eligibility produces **exactly three** outcomes:

| Outcome | Meaning |
|---------|---------|
| `ACCEPT` | Phrase may enter service mapping and downstream semantic core candidacy |
| `REJECT` | Phrase excluded from commercial core; archived with evidence |
| `ABSTAIN` | Insufficient support for ACCEPT or confident REJECT; routed to adjudication |

**ABSTAIN is not failure.** It is a controlled safety state per operator decision D4.

---

## ACCEPT requirements

All must be satisfied for auto-ACCEPT (human override follows separate audit path):

1. **Supported probable paid-service intent** — primary or co-primary intent aligns with operator hire_service or approved commercial module offer.
2. **Honest service-side landing answer** — a landing page can answer the query without reinterpretation or bait-and-switch.
3. **No dominant protected non-commercial intent** — career, educational, DIY/how-to, regulatory, navigational not primary.
4. **Sufficient confidence** — meets risk-mode threshold; in CONSERVATIVE mode, highest bar applies.
5. **No unresolved ownership-critical ambiguity** — service mapping conflict does not block admission decision itself, but product/service conflict must be resolved or ABSTAIN.

**Prohibited ACCEPT triggers:**

- Service term presence alone.
- Topical relevance to business category alone.
- High search volume alone.
- Competitor bidding on phrase alone.
- Lexical similarity to known ACCEPT phrase alone.

---

## REJECT criteria

Use `REJECT` when:

1. Primary intent is clearly non-commercial for operator's service offer.
2. Phrase is educational, career, DIY, regulatory, navigational, irrelevant, or malformed (and not eligible for ABSTAIN exception).
3. Product/module intent incompatible with service-only offer.
4. Landing would require reinterpretation of query meaning.
5. SI-06 hard exclusion applies with sufficient confidence and no registered exception.
6. Operator scope explicitly prohibits the query class.

REJECT records require: primary intent, rule/model evidence, rejection class, version binding.

---

## ABSTAIN — mandatory conditions

ABSTAIN is **mandatory** when:

1. Multiple plausible intents remain after SI-07.
2. Short query lacks provider signal (e.g. single-word or fragment).
3. Problem query may indicate DIY or paid support equally.
4. Service versus product intent unresolved.
5. Model/rule disagreement exists.
6. Confidence below risk-mode threshold.
7. Protected-strata signals conflict with commercial signals.
8. High-risk ACCEPT in CONSERVATIVE mode without secondary confirmation.

ABSTAIN routes to SI-09 → SI-13. Resolution may yield ACCEPT or REJECT with human audit.

---

## Risk modes

### CONSERVATIVE

**For:** new accounts, limited budgets, no conversion history, expensive B2B leads.

| Parameter | Setting |
|-----------|---------|
| ACCEPT confidence threshold | Highest |
| ABSTAIN queue | Largest |
| Protected-strata handling | Strictest — lean REJECT or ABSTAIN |
| Auto-ACCEPT | Minimal — prefer human confirmation on edge cases |

**Corvonero initial mode:** `CONSERVATIVE`

### BALANCED

**For:** established campaigns, moderate data, active operator review.

| Parameter | Setting |
|-----------|---------|
| ACCEPT confidence threshold | Moderate |
| ABSTAIN queue | Moderate |
| Protected-strata handling | Standard D3 FPR caps |
| Auto-ACCEPT | Allowed when P0-G thresholds met |

### EXPLORATORY

**For:** isolated experiments, dedicated budgets, explicit controlled-test governance.

| Parameter | Setting |
|-----------|---------|
| ACCEPT confidence threshold | Lower within experiment charter only |
| ABSTAIN queue | Smaller within experiment scope |
| Scope | Isolated budget/campaign — **must not weaken approved core silently** |
| Governance | Explicit experiment charter required |

---

## Topical relevance rule

**Topical relevance ≠ commercial intent.**

A phrase may be topically relevant to operator services and still receive REJECT or ABSTAIN. SI-08 must evaluate likely next user action and landing compatibility — not category overlap alone.

---

## Protected strata

Classes (per D3): career, educational, DIY/how-to, regulatory, navigational.

| Mode | Default on conflict |
|------|---------------------|
| CONSERVATIVE | REJECT or ABSTAIN — never auto-ACCEPT |
| BALANCED | ABSTAIN unless strong hire signal |
| EXPLORATORY | Per experiment charter — core still protected |

FPR cap on auto-ACCEPT into protected classes: **≤ 0.01** per class (D3).

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-admission-policy-v1.json` |
| Quality gates | `ORCA-SEMANTIC-INTELLIGENCE-QUALITY-GATES-v1.md` |
| Operator D3/D4 | `research/.../decisions/` |
