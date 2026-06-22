# MARS Search PPC Production Lifecycle v1

**Status:** `APPROVED — IMPLEMENTATION AUTHORIZED` (W1-D1, 2026-06-22)  
**Date:** 2026-06-22  
**Platform:** Yandex Direct — Search campaigns only  
**Canonical locus:** `projects/mars-search-ppc-production/`

---

## Operator decision (binding when approved)

MARS must **not** advance to strategy, campaign production, or Commander Export until mandatory prior stages complete with registered artifacts.

When required inputs are missing:

1. Stop transition  
2. Set status `BLOCKED`  
3. List missing inputs  
4. Name owning system/role  
5. Do not substitute assumptions  
6. Do not fabricate completed results  

---

## Mandatory lifecycle (23 stages)

| ID | Stage | Owner |
|----|-------|-------|
| SPPC-01 | Business Intake and Operator Authority | ATLAS |
| SPPC-02 | Source Registration | MIG |
| SPPC-03 | Full Semantic Corpus Intake | MIG / ORCA intake |
| SPPC-04 | Normalization and Canonical Registry | ORCA |
| SPPC-05 | Commercial Intent Admission | ORCA Semantic Intelligence |
| SPPC-06 | Demand Priority Segmentation (T1–T5) | ORCA Semantic Intelligence |
| SPPC-07 | Service and Meaning Ownership | ORCA Semantic Intelligence |
| SPPC-08 | Semantic Clustering | ORCA Semantic Intelligence |
| SPPC-09 | Negative Keyword Intelligence | ORCA Semantic Intelligence |
| SPPC-10 | Daytime Paid SERP Intelligence | MIG (`PAID SERP — BUSINESS HOURS`) |
| SPPC-11 | Competitor Advertising Audit | MIG |
| SPPC-12 | Dated Analytical Pack | Cross-system |
| SPPC-13 | AI PPC Strategist | AI PPC Strategist |
| SPPC-14 | Campaign Architecture | Campaign Production |
| SPPC-15 | Keyword and Negative Distribution | Campaign Production |
| SPPC-16 | Ad Production | Campaign Production |
| SPPC-17 | Landing and Offer Alignment | QA |
| SPPC-18 | Bidding and Budget Strategy | Campaign Production |
| SPPC-19 | Campaign QA | QA / Validators |
| SPPC-20 | Commander Export | Commander Export (transport only) |
| SPPC-21 | Dry Run and Operator Approval | Operator |
| SPPC-22 | Import and Launch | Operator / Platform |
| SPPC-23 | Post-Launch Learning | Post-Launch Learning |

Stage contracts: [stages/README.md](stages/README.md)

---

## System responsibility map

```text
ATLAS / Project Registry
→ project identity, business relationships, registered entities

MIG
→ evidence collection, source registration, Wordstat, SERP, market groundtruth

ORCA Semantic Intelligence
→ interpretation, commercial admission, prioritization, service ownership,
  clustering, negative intelligence

AI PPC Strategist
→ strategy from completed dated analytical evidence

Campaign Production
→ campaigns, groups, keywords, negatives, ads, URLs, UTM, bid configuration

QA / Validators
→ semantic, structural, PPC, landing, export, readiness checks

Commander Export
→ transport-only import artifacts

Post-Launch Learning
→ search-term evidence, performance evidence, governed proposals
```

---

## Core principles

### Full corpus (SPPC-03)

Process the **complete provided corpus**. Never substitute:

- 200-row P0-I pilot  
- convenient manual subset  
- highest-frequency-only slice  
- pre-filtered “already commercial” phrases  

Subsets allowed only for technical validation, benchmark, controlled pilot, diagnostics — **never** confused with production corpus processing.

### Commercial admission (SPPC-05)

Authoritative outcomes: `ACCEPT` | `REJECT` | `ABSTAIN`.

ABSTAIN escalation ladder:

```text
primary assessor
→ independent automated reassessment
→ automated adjudication / evidence enrichment
→ only unresolved policy/domain conflicts to human review
```

Human review is a **bounded exception**, not the default production engine.

### Demand tiers (SPPC-06)

| Tier | Definition |
|------|------------|
| **T1** | Direct high-intent commercial demand |
| **T2** | Commercial problem demand |
| **T3** | Extended service demand |
| **T4** | Additional adjacent demand |
| **T5** | Experimental demand |

Frequency alone must not determine tier.

### Paid SERP (SPPC-10)

Mandatory MIG mode: `PAID SERP — BUSINESS HOURS`.

If business-hours paid SERP evidence is missing for primary directions, AI strategy reports:

```text
BLOCKED OR DEGRADED — PAID COMPETITIVE EVIDENCE MISSING
```

Continue only under explicitly approved degraded-evidence mode ([architecture/DEGRADED-EVIDENCE-MODE-v1.md](architecture/DEGRADED-EVIDENCE-MODE-v1.md)).

### Commander Export (SPPC-20)

Transport-only. Must not admit phrases, change semantics, move keywords, modify negatives, invent structure, rewrite strategy, or mutate URLs without registered correction.

### Operator approval (SPPC-21)

Approval at campaign/strategy abstraction — **not** every keyword. Phrase-level review reserved for policy conflicts, sampled QA, critical disagreements, explicit operator request.

---

## Machine-readable contract

- Contract: [contracts/mars-search-ppc-lifecycle-contract-v1.json](contracts/mars-search-ppc-lifecycle-contract-v1.json)  
- Schema: [schemas/mars-search-ppc-lifecycle-contract-v1.schema.json](schemas/mars-search-ppc-lifecycle-contract-v1.schema.json)  
- Project manifest: [state/project-ppc-state-manifest-template-v1.json](state/project-ppc-state-manifest-template-v1.json)  
- Validator: [validators/validate-search-ppc-lifecycle.mjs](validators/validate-search-ppc-lifecycle.mjs)

---

## Lifecycle statuses

`NOT STARTED` | `IN PROGRESS` | `BLOCKED` | `READY FOR REVIEW` | `APPROVED` | `COMPLETED` | `COMPLETED WITH APPROVED DEGRADATION` | `SUPERSEDED` | `FAILED` | `FROZEN`

Completion requires **registered artifacts** — a report claiming completion is insufficient.

---

## Execution contracts

- Web-GPT: [web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md](web-gpt/WEB-GPT-SEARCH-PPC-EXECUTION-CONTRACT-v1.md)  
- Cursor: [cursor/CURSOR-SEARCH-PPC-TASK-STARTER-v1.md](cursor/CURSOR-SEARCH-PPC-TASK-STARTER-v1.md)

---

## Related audits

- Gap audit: [reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md](reports/MARS-SEARCH-PPC-LIFECYCLE-GAP-AUDIT-v1.md)  
- Bypass audit: [reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md](reports/MARS-SEARCH-PPC-BYPASS-FAILURE-AUDIT-v1.md)  
- Repair roadmap: [roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md](roadmap/MARS-SEARCH-PPC-LIFECYCLE-REPAIR-ROADMAP-v1.md)

---

## P0-I pilot boundary

ORCA P0-I 200-phrase integration pilot: **TECHNICAL INTEGRATION EVIDENCE ONLY** — see [ORCA-P0-I-PILOT-RECLASSIFICATION-DECISION-v1](../orca/semantic-intelligence/integration/decisions/ORCA-P0-I-PILOT-RECLASSIFICATION-DECISION-v1.md).

---

## Corvonero

**FROZEN PENDING SEARCH PPC PRODUCTION LIFECYCLE IMPLEMENTATION AND GAP CLOSURE**

---

## Operator approval gate

```text
PROPOSED — OPERATOR APPROVAL REQUIRED
```

Decision record: [decisions/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1.md](decisions/MARS-SEARCH-PPC-PRODUCTION-LIFECYCLE-OPERATOR-DECISION-v1.md)
