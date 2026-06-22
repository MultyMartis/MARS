# ORCA Semantic Intelligence — Authority Model v1

**Model ID:** `orca-semantic-intelligence-authority-model`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**ADR:** `ORCA-SEMANTIC-INTELLIGENCE-ADR-v1.md`

---

## Principle

Lower authority layers **cannot override** higher layers. Semantic decisions flow down the pipeline; appeals flow up through adjudication and human review — never sideways from export or campaign production into core semantics.

---

## Authority hierarchy (strict order)

| Rank | Authority source | Layer / artifact | Can override |
|------|------------------|------------------|--------------|
| 1 | Explicit operator decisions | D1–D7; future versioned decisions | All below |
| 2 | Approved business scope | SI-01 operator intake; service scope registry | Layers 3–12 |
| 3 | Approved Semantic Core | SI-14 state `APPROVED` | Layers 4–12 for bound phrases |
| 4 | Approved annotation guideline | Future P0-C | Model outputs; clustering suggestions |
| 5 | Benchmark / gold labels | Future P0-D/E | Model calibration targets |
| 6 | Versioned deterministic rules | SI-06 hard exclusions | Model on narrow exclusion classes only |
| 7 | Calibrated model output | SI-07, SI-08 (advisory until P0-G) | Nothing above; subject to ABSTAIN |
| 8 | LLM-assisted adjudication | SI-09 structured assistance | Nothing above; human final |
| 9 | Clustering suggestions | SI-11 candidates | Eligibility; ownership; core |
| 10 | Campaign production | SI-15 | Semantic fields |
| 11 | Export formatting | SI-16 XLSX/Commander transport | Semantic fields |
| 12 | Post-launch proposals | SI-17 | Approved core without new gate |

---

## Layer authority matrix

| Layer | Authority level | Final decision owner |
|-------|-----------------|----------------------|
| SI-01 Operator Authority | **POLICY** | Operator |
| SI-02 Market Evidence | **EVIDENCE** | None — input only |
| SI-03 Source Corpus | **IMMUTABLE RECORD** | None — preservation only |
| SI-04 Normalization | **DETERMINISTIC TRANSFORM** | Rule version owner |
| SI-05 Query Understanding | **FEATURE EXTRACTION** | None — structured features |
| SI-06 Hard Exclusion | **HIGH-CONFIDENCE RULE** | Rule set version |
| SI-07 Intent Classification | **ADVISORY** | None until benchmark-gated |
| SI-08 Commercial Eligibility | **GATE OUTPUT** | Produces ACCEPT/REJECT/ABSTAIN — ABSTAIN escalates |
| SI-09 Semantic Adjudication | **ESCALATION** | Human/operator on unresolved |
| SI-10 Service Mapping | **OWNERSHIP PROPOSAL** | Operator override available |
| SI-11 Cluster Discovery | **SUGGESTION** | Human review before core |
| SI-12 Negative Intelligence | **DERIVED** | Cannot alter eligibility |
| SI-13 Human Review | **ADJUDICATION** | Human reviewer + operator sign-off |
| SI-14 Semantic Core | **CANONICAL SEMANTIC AUTHORITY** | Operator approval |
| SI-15 Campaign Production | **CONSUMER** | None on semantics |
| SI-16 External Artifact QA | **VALIDATOR** | None — fail closed |
| SI-17 Post-Launch Learning | **PROPOSAL** | Operator gate for adoption |

---

## Override rules

### Permitted

- Operator override on SI-10 service ownership with audit trail.
- Human adjudication in SI-09/SI-13 resolving ABSTAIN to ACCEPT or REJECT.
- Operator supersede of Semantic Core version with new review cycle.
- SI-06 exception registry for narrowly defined rule conflicts.

### Prohibited

- Campaign production changing intent, eligibility, or ownership.
- Export layer silently repairing semantic mismatches.
- Model output auto-ACCEPT without threshold gate pass (P0-G).
- Clustering merging phrases with different primary commercial intents.
- Post-launch search terms auto-adding phrases to approved core.
- Diagnostic Corvonero v1 decisions promoted to authority.

---

## Conflict resolution

1. **Rule vs model disagreement** → ABSTAIN → SI-09 → SI-13 if unresolved.
2. **Protected strata vs commercial signal** → default REJECT or ABSTAIN per CONSERVATIVE mode; never auto-ACCEPT.
3. **Service mapping conflict** → ABSTAIN on ownership-critical ambiguity; block cluster assignment.
4. **Export vs core mismatch** → SI-16 fail; return to core or export fix without semantic change.

---

## Version binding

Each decision record binds to: `operator_scope_version`, `rule_set_version`, `model_version` (if any), `guideline_version`, `core_version`. Missing binding → decision invalid for production handoff.

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-authority-model-v1.json` |
| Flow | `ORCA-SEMANTIC-INTELLIGENCE-FLOW-v1.md` |
| Admission policy | `ORCA-SEMANTIC-ADMISSION-POLICY-v1.md` |
