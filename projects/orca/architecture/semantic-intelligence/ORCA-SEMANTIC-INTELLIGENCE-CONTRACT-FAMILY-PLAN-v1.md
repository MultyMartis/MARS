# ORCA Semantic Intelligence — Contract Family Plan v1

**Plan ID:** `orca-semantic-intelligence-contract-family`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** All contracts `PLANNED` — not implemented in this task

---

## Purpose

Define the future contract family for ORCA Semantic Intelligence v1. Full field schemas deferred to P0-B and subsequent contract drafting gates.

---

## Contract registry

### 1. Semantic Source Contract

| Field | Value |
|-------|-------|
| Purpose | Immutable raw phrase ingestion with provenance |
| Producer | SI-02, SI-03 |
| Consumer | SI-04 Normalization |
| Required fields | `phrase_id`, `raw_text`, `source_id`, `snapshot_version`, `frequency`, `captured_at` |
| Invariants | No intent labels at ingest; provenance immutable |
| Gate | Corpus freeze before normalization run |
| Status | **PLANNED** |

### 2. Query Understanding Contract

| Field | Value |
|-------|-------|
| Purpose | Structured feature object per normalized phrase |
| Producer | SI-05 |
| Consumer | SI-06, SI-07 |
| Required fields | `query_id`, `entity`, `action`, `object`, `modifiers`, signal flags, `extractor_version` |
| Invariants | Features are proposals — not eligibility decisions |
| Gate | P0-B schema freeze |
| Status | **PLANNED** |

### 3. Intent Classification Contract

| Field | Value |
|-------|-------|
| Purpose | Primary/secondary intent with confidence |
| Producer | SI-07 |
| Consumer | SI-08, SI-09 |
| Required fields | `query_id`, `primary_intent`, `secondary_intent`, `confidence`, `competing_interpretations`, `classifier_version` |
| Invariants | Taxonomy version bound; `ambiguous` valid outcome |
| Gate | P0-B taxonomy freeze |
| Status | **PLANNED** |

### 4. Commercial Eligibility Contract

| Field | Value |
|-------|-------|
| Purpose | ACCEPT / REJECT / ABSTAIN gate output |
| Producer | SI-08 |
| Consumer | SI-09, SI-10, SI-13 |
| Required fields | `query_id`, `outcome`, `confidence`, `risk_mode`, `evidence_refs`, `policy_version` |
| Invariants | Exactly one of ACCEPT/REJECT/ABSTAIN; topical relevance alone insufficient |
| Gate | P0-G threshold pass for auto-ACCEPT |
| Status | **PLANNED** |

### 5. Abstention and Human Review Contract

| Field | Value |
|-------|-------|
| Purpose | Queue items and adjudication outcomes |
| Producer | SI-08, SI-09, SI-13 |
| Consumer | SI-14 Semantic Core |
| Required fields | `queue_id`, `query_id`, `queue_type`, `reviewer_id`, `resolution`, `rationale`, `guideline_version` |
| Invariants | ABSTAIN resolution requires human or operator audit |
| Gate | P0-C guideline approval |
| Status | **PLANNED** |

### 6. Service Ownership Contract

| Field | Value |
|-------|-------|
| Purpose | Primary service mapping for ACCEPT phrases |
| Producer | SI-10 |
| Consumer | SI-11, SI-12 |
| Required fields | `query_id`, `primary_service`, `secondary_candidate`, `conflict_flag`, `mapping_confidence`, `scope_version` |
| Invariants | Runs only post-ACCEPT; cannot alter eligibility |
| Gate | Operator scope version bound |
| Status | **PLANNED** |

### 7. Cluster Candidate Contract

| Field | Value |
|-------|-------|
| Purpose | Task-based cluster proposals |
| Producer | SI-11 |
| Consumer | SI-12, SI-14, SI-15 |
| Required fields | `cluster_id`, `member_query_ids`, `task_label`, `landing_compatibility`, `primary_intent_homogeneity` |
| Invariants | No merge of conflicting primary intents |
| Gate | Post ownership assignment |
| Status | **PLANNED** |

### 8. Negative Intelligence Contract

| Field | Value |
|-------|-------|
| Purpose | Derived negative candidates by class |
| Producer | SI-12 |
| Consumer | SI-14, SI-15 |
| Required fields | `negative_id`, `query_id`, `negative_class`, `scope`, `collision_risk`, `derivation_version` |
| Invariants | Post ownership; cannot rescue bad base phrases |
| Gate | Post cluster proposal |
| Status | **PLANNED** |

### 9. Semantic Core Authority Contract

| Field | Value |
|-------|-------|
| Purpose | Canonical approved semantic artifact |
| Producer | SI-14 |
| Consumer | SI-15, SI-16 |
| Required fields | `core_id`, `version`, `state`, `phrase_records[]`, `approver_id`, `approved_at` |
| Invariants | Only APPROVED unlocks campaign production |
| Gate | P0-H operator sign-off |
| Status | **PLANNED** |

### 10. Campaign Handoff Contract

| Field | Value |
|-------|-------|
| Purpose | Campaign production consumption of approved core |
| Producer | SI-15 |
| Consumer | SI-16, Campaign Production Contract v1 |
| Required fields | `handoff_id`, `core_version`, `campaign_dataset_ref`, `immutable_semantic_hash` |
| Invariants | No semantic mutation; compatible with ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1 |
| Gate | APPROVED core only |
| Status | **PLANNED** |

### 11. External Artifact Parity Contract

| Field | Value |
|-------|-------|
| Purpose | Export/Commander parity validation |
| Producer | SI-16 |
| Consumer | Operator, export pipeline |
| Required fields | `qa_id`, `core_hash`, `export_hash`, `field_diffs[]`, `validator_version` |
| Invariants | Fail closed; no silent semantic repair |
| Gate | Pre-Commander handoff |
| Status | **PLANNED** |

### 12. Post-Launch Learning Contract

| Field | Value |
|-------|-------|
| Purpose | Performance-fed proposal queue |
| Producer | SI-17 |
| Consumer | Operator gate for core versioning |
| Required fields | `proposal_id`, `source_term`, `proposal_type`, `evidence`, `target_core_version` |
| Invariants | Proposals only — no direct core mutation |
| Gate | Operator review for adoption |
| Status | **PLANNED** |

---

## Cross-reference

| Artifact | Path |
|----------|------|
| JSON record | `orca-semantic-intelligence-contract-family-plan-v1.json` |
| Campaign Production Contract | `projects/orca/contracts/ORCA-CAMPAIGN-PRODUCTION-CONTRACT-v1.md` |
