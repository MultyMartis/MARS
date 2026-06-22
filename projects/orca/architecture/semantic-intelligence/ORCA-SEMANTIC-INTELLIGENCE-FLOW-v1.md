# ORCA Semantic Intelligence — Information Flow v1

**Flow ID:** `orca-semantic-intelligence-flow`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`

---

## High-level flow

```text
Operator Authority (SI-01)
        +
Market Evidence (SI-02)
        ↓
Immutable Source Corpus (SI-03)
        ↓
Normalization (SI-04)
        ↓
Query Understanding (SI-05)
        ↓
Hard Exclusion Screening (SI-06)
        ↓
Intent Classification (SI-07)
        ↓
Commercial Eligibility (SI-08)
   ↙        ↓        ↘
REJECT    ABSTAIN    ACCEPT
   ↓         ↓          ↓
Evidence  Human      Service
archive   Review     Mapping (SI-10)
(SI-03)   (SI-13)        ↓
             ↓      Cluster Discovery (SI-11)
          Decision        ↓
          (SI-09)   Negative Intelligence (SI-12)
                          ↓
                Semantic Core Review (SI-14)
                          ↓
                 APPROVED CORE
                          ↓
                Campaign Production (SI-15)
                          ↓
                 External Artifact QA (SI-16)
                          ↓
                       Draft export
                          ↓
                Post-Launch Proposals (SI-17)
```

---

## Layer specifications

### SI-01 — Operator Authority

**Owns:** business scope, audience, geography, commercial constraints, confirmed facts, prohibited claims, budget/risk mode.  
**Cannot:** generate final keyword decisions automatically.  
**Inputs:** operator intake, service scope registry.  
**Outputs:** versioned operator scope manifest bound to project.

### SI-02 — Market Evidence

**Owns:** Wordstat, keyword tools, SERP evidence, search-term evidence, external demand signals.  
**Cannot:** declare a phrase commercially eligible.  
**Inputs:** MIG exports, tool pulls, SERP snapshots.  
**Outputs:** evidence packs with source log.

### SI-03 — Source Corpus

**Owns:** immutable raw phrases, provenance, source snapshots, frequency evidence.  
**Cannot:** normalize away meaning; create semantic decisions.  
**Inputs:** SI-02 evidence bindings.  
**Outputs:** raw phrase ledger with provenance IDs.

### SI-04 — Normalization

**Owns:** deterministic cleanup, deduplication, operators, morphology-safe normalization, stable query IDs.  
**Cannot:** rewrite malformed queries into invented commercial formulations.  
**Inputs:** SI-03 raw corpus.  
**Outputs:** normalized phrase records with `query_id`.

### SI-05 — Query Understanding

**Owns structured extraction:** entity, action, object, problem, desired outcome, modifiers, provider signal, product/module signal, DIY signal, career signal, educational signal, regulatory signal, navigation signal, geography.  
**Cannot:** produce final ACCEPT alone.  
**Inputs:** SI-04 normalized records, SI-01 scope.  
**Outputs:** feature object per phrase.

### SI-06 — Hard Exclusion Screening

**Owns:** high-confidence exclusion classes — clear employment, clear education, explicit free download, login/navigation, obvious irrelevant noise, malformed spam.  
**Must support:** exceptions, versioned rules, regression anchors, conflict detection.  
**Cannot:** classify ambiguous problem queries as commercial.  
**Inputs:** SI-05 features.  
**Outputs:** `EXCLUDED` | `PASS_TO_INTENT` with rule ID and confidence.

### SI-07 — Intent Classification

**Produces:** primary intent, secondary intent, confidence, competing interpretations.  
**Required taxonomy (minimum):** hire_service, buy_product_or_module, technical_support, troubleshoot_self, DIY/how-to, informational, educational, career/employment, regulatory, navigational, documentation, download, ambiguous, irrelevant, malformed.  
**Inputs:** SI-05, SI-06 pass records.  
**Outputs:** intent classification record.

### SI-08 — Commercial Eligibility

**Produces exactly:** `ACCEPT` | `REJECT` | `ABSTAIN`.  
**Uses:** literal interpretation, likely next user action, provider-hire likelihood, landing compatibility, alternative intent, cost-sensitive policy (risk mode).  
**Cannot:** infer ACCEPT merely because a service term is present.  
**Inputs:** SI-07, SI-01 scope, risk mode.  
**Outputs:** eligibility decision with confidence and evidence.

### SI-09 — Semantic Adjudication

**Handles:** ABSTAIN, high-risk ACCEPT, model/rule disagreements, protected strata, short ambiguous queries, problem queries, product-versus-service conflicts.  
**May use:** human reviewer, structured LLM assistance, retrieved examples, benchmark evidence.  
**Final authority:** human/operator per governance.  
**Inputs:** SI-08 ABSTAIN and escalated ACCEPT/REJECT.  
**Outputs:** resolved decision or escalated queue item.

### SI-10 — Service Mapping

**Runs only for:** commercially approved phrases (post-ACCEPT adjudication).  
**Produces:** primary service ownership, secondary candidate, conflict, mapping confidence, operator override.  
**Cannot:** change commercial eligibility.  
**Inputs:** ACCEPT records, SI-01 service scope.  
**Outputs:** ownership mapping record.

### SI-11 — Cluster Discovery

**Produces:** candidate clusters by shared user task, landing compatibility, service ownership, commercial promise, semantic distinction.  
**Cannot:** create campaign groups; merge different primary intents due to lexical similarity.  
**Inputs:** SI-10 mappings, SI-07 intents.  
**Outputs:** cluster candidate sets.

### SI-12 — Negative Intelligence

**Runs after:** ownership and cluster proposals.  
**Separates:** semantic exclusions, global negative candidates, campaign negative candidates, cluster separation candidates, exact exclusions, collision risks.  
**Cannot:** rescue bad base phrases through long inline negatives.  
**Inputs:** SI-10, SI-11, SI-01 prohibited claims.  
**Outputs:** negative candidate registry.

### SI-13 — Human Review

**Owns queues:** ABSTAIN, protected strata, high-risk ACCEPT, conflicts, random ACCEPT audit, random REJECT audit, model disagreement, blind evaluation.  
**Inputs:** escalations from SI-08, SI-09, SI-10, SI-11.  
**Outputs:** adjudicated decisions with reviewer audit trail.

### SI-14 — Semantic Core Authority

**Creates:** the only approved semantic authority artifact.  
**States:** `DRAFT` → `IN REVIEW` → `APPROVED` | `REJECTED` | `SUPERSEDED`.  
**Only `APPROVED` unlocks SI-15.**  
**Inputs:** resolved phrase records from SI-08 through SI-12.  
**Outputs:** versioned Semantic Core artifact.

### SI-15 — Campaign Production Handoff

**Consumes:** approved Semantic Core.  
**Cannot:** add phrases, restore rejected, alter intent, eligibility, or ownership without Semantic Core gate return.  
**Inputs:** SI-14 APPROVED core.  
**Outputs:** campaign architecture dataset (non-export).

### SI-16 — External Artifact QA

**Validates:** semantic authority, campaign dataset, XLSX, Commander import, review workbook parity.  
**Cannot:** silently repair semantics during export.  
**Inputs:** SI-14, SI-15 outputs, export artifacts.  
**Outputs:** pass/fail QA report.

### SI-17 — Post-Launch Learning

**Consumes:** search terms, clicks, spend, conversions, negative candidates, new demand.  
**Produces:** proposals only.  
**Cannot:** mutate approved Semantic Core without versioned review cycle.  
**Inputs:** platform performance data.  
**Outputs:** proposal queue for operator gate.

---

## State machine — phrase lifecycle

| State | Description | Next states |
|-------|-------------|-------------|
| `RAW` | In SI-03 corpus | `NORMALIZED` |
| `NORMALIZED` | SI-04 complete | `UNDERSTOOD` |
| `UNDERSTOOD` | SI-05 complete | `SCREENED` |
| `SCREENED` | SI-06 complete | `INTENT_CLASSIFIED` or `HARD_EXCLUDED` |
| `HARD_EXCLUDED` | SI-06 high-confidence | `REJECTED` (terminal for admission) |
| `INTENT_CLASSIFIED` | SI-07 complete | `ELIGIBILITY_PENDING` |
| `ELIGIBILITY_PENDING` | SI-08 processing | `ACCEPTED` \| `REJECTED` \| `ABSTAINED` |
| `ABSTAINED` | SI-08 ABSTAIN | `IN_ADJUDICATION` |
| `IN_ADJUDICATION` | SI-09/SI-13 | `ACCEPTED` \| `REJECTED` |
| `ACCEPTED` | Commercially eligible | `MAPPED` |
| `MAPPED` | SI-10 complete | `CLUSTER_CANDIDATE` |
| `CLUSTER_CANDIDATE` | SI-11 assigned | `NEGATIVES_DERIVED` |
| `NEGATIVES_DERIVED` | SI-12 complete | `CORE_DRAFT` |
| `REJECTED` | Non-commercial or failed adjudication | `EVIDENCE_ARCHIVED` |
| `CORE_DRAFT` | In SI-14 draft | `IN_REVIEW` |
| `IN_REVIEW` | Operator review | `APPROVED` \| `REJECTED` \| `SUPERSEDED` |
| `APPROVED` | In approved core | `CAMPAIGN_CONSUMED` |
| `CAMPAIGN_CONSUMED` | SI-15 handoff | `EXPORT_QA` |
| `EXPORT_QA` | SI-16 validation | `EXPORT_READY` or `QA_FAILED` |

---

## Prohibited shortcuts

| Shortcut | Why prohibited |
|----------|----------------|
| SI-02 → SI-08 ACCEPT | Market evidence ≠ commercial intent |
| SI-05 topical match → ACCEPT | Topic ≠ hire intent |
| SI-06 ambiguous → REJECT without adjudication | May suppress valid commercial problem queries |
| SI-11 before SI-08 ACCEPT | Clusters before eligibility |
| SI-12 before SI-10 | Negatives before ownership |
| SI-15 phrase addition | Contaminates approved core |
| SI-16 semantic repair on export fail | Hides authority drift |
| SI-17 → SI-14 without gate | Post-launch leakage |
| Skip SI-14 APPROVED → Commander | D7 violation |

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-flow-v1.json` |
| Authority model | `ORCA-SEMANTIC-INTELLIGENCE-AUTHORITY-MODEL-v1.md` |
| Admission policy | `ORCA-SEMANTIC-ADMISSION-POLICY-v1.md` |
