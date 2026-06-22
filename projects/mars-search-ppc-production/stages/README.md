# MARS Search PPC Production — Stage Contracts Index

**Generated:** 2026-06-22  
**Generator:** `tools/generate-stage-contracts.mjs`  
**Count:** 23 stages (SPPC-01 … SPPC-23)

---

## Purpose

This index lists canonical stage contracts for the MARS Search PPC Production lifecycle. Each contract defines inputs, outputs, validation, blocking conditions, and handoff tokens for human-operated production.

**Honesty boundary:** These contracts describe documented production discipline — not automated orchestration unless future tooling explicitly implements it.

---

## Stage map

| # | Contract | Name | Owning system | Operator approval |
|---|----------|------|---------------|-------------------|
| 01 | [SPPC-01](./SPPC-01-business-intake.md) | Business Intake and Operator Authority | ATLAS | yes |
| 02 | [SPPC-02](./SPPC-02-source-registration.md) | Source Registration | MIG | no |
| 03 | [SPPC-03](./SPPC-03-full-semantic-corpus-intake.md) | Full Semantic Corpus Intake | MIG / ORCA (joint) | yes — witness sign-off that full corpus, not pilot, was ingested |
| 04 | [SPPC-04](./SPPC-04-normalization-and-canonical-registry.md) | Normalization and Canonical Registry | ORCA | no |
| 05 | [SPPC-05](./SPPC-05-commercial-intent-admission.md) | Commercial Intent Admission | ORCA Semantic Intelligence | yes — required when ABSTAIN escalation reaches human queue |
| 06 | [SPPC-06](./SPPC-06-demand-priority-segmentation-t1-t5.md) | Demand Priority Segmentation T1–T5 | ORCA | no — yes only on documented tier dispute overrides |
| 07 | [SPPC-07](./SPPC-07-service-and-meaning-ownership.md) | Service and Meaning Ownership | ORCA | yes — when ownership conflicts reach human queue |
| 08 | [SPPC-08](./SPPC-08-semantic-clustering.md) | Semantic Clustering | ORCA | no — yes only for edge cluster merge/split decisions |
| 09 | [SPPC-09](./SPPC-09-negative-keyword-intelligence.md) | Negative Keyword Intelligence | ORCA | yes — required for conflict resolution and waivers |
| 10 | [SPPC-10](./SPPC-10-daytime-paid-serp-intelligence.md) | Daytime Paid SERP Intelligence | MIG (mode: PAID SERP BUSINESS HOURS) | yes — when degraded_mode requires strategic acceptance |
| 11 | [SPPC-11](./SPPC-11-competitor-advertising-audit.md) | Competitor Advertising Audit | MIG | no |
| 12 | [SPPC-12](./SPPC-12-dated-analytical-pack.md) | Dated Analytical Pack | Cross-system (ORCA lead assembly) | yes — pack completeness and degraded SERP acknowledgment |
| 13 | [SPPC-13](./SPPC-13-ai-ppc-strategist.md) | AI PPC Strategist | AI PPC Strategist | yes |
| 14 | [SPPC-14](./SPPC-14-campaign-architecture.md) | Campaign Architecture | Campaign Production | no |
| 15 | [SPPC-15](./SPPC-15-keyword-and-negative-distribution.md) | Keyword and Negative Distribution | Campaign Production | no |
| 16 | [SPPC-16](./SPPC-16-ad-production.md) | Ad Production | Campaign Production | no — yes for compliance waivers only |
| 17 | [SPPC-17](./SPPC-17-landing-and-offer-alignment.md) | Landing and Offer Alignment | QA / Campaign Production | yes — for offer mismatch waivers |
| 18 | [SPPC-18](./SPPC-18-bidding-and-budget-strategy.md) | Bidding and Budget Strategy | Campaign Production | yes — automated branch and budget envelope exceptions |
| 19 | [SPPC-19](./SPPC-19-campaign-qa.md) | Campaign QA | QA / Validators | yes — for mandatory rule waivers |
| 20 | [SPPC-20](./SPPC-20-commander-export.md) | Commander Export | Commander Export | no |
| 21 | [SPPC-21](./SPPC-21-dry-run-and-operator-approval.md) | Dry Run and Operator Approval | Operator | yes |
| 22 | [SPPC-22](./SPPC-22-import-and-launch.md) | Import and Launch | Operator / Platform | yes |
| 23 | [SPPC-23](./SPPC-23-post-launch-learning.md) | Post-Launch Learning | Post-Launch Learning | yes — for reopen recommendations and new cycle charters |

---

## Canonical flow (summary)

```text
01 Business Intake (ATLAS)
 → 02 Source Registration (MIG)
 → 03 Full Semantic Corpus Intake (MIG/ORCA)
 → 04 Normalization (ORCA)
 → 05 Commercial Intent Admission (ORCA Semantic Intelligence)
 → 06 Demand Priority T1–T5 (ORCA)
 → 07 Service and Meaning Ownership (ORCA)
 → 08 Semantic Clustering (ORCA)
 → 09 Negative Keyword Intelligence (ORCA)
 → 10 Daytime Paid SERP (MIG)
 → 11 Competitor Audit (MIG)
 → 12 Dated Analytical Pack (cross-system)
 → 13 AI PPC Strategist
 → 14 Campaign Architecture
 → 15 Keyword and Negative Distribution
 → 16 Ad Production
 → 17 Landing and Offer Alignment
 → 18 Bidding and Budget Strategy
 → 19 Campaign QA
 → 20 Commander Export (transport only)
 → 21 Dry Run and Operator Approval
 → 22 Import and Launch
 → 23 Post-Launch Learning
```

---

## Charter-highlighted rules

| Stage | Rule |
|-------|------|
| SPPC-03 | Full corpus intake — no 200-row pilot substitution |
| SPPC-05 | ACCEPT / REJECT / ABSTAIN; escalation ladder; no regex as final authority |
| SPPC-06 | T1–T5 tier definitions binding |
| SPPC-09 | Negatives after admission and ownership; conflicts block export |
| SPPC-10 | Paid SERP business hours; degraded mode if incomplete |
| SPPC-12 | Dated analytical pack required sections |
| SPPC-13 | Strategy gates; forbidden jump to Commander |
| SPPC-20 | Transport-only export |
| SPPC-21 | Operator approval at campaign/strategy abstraction |

---

## Regeneration

```bash
node tools/generate-stage-contracts.mjs
```
