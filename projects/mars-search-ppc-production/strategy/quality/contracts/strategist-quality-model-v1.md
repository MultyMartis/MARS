# Strategist Quality Model v1 — Wave 4.1

**Status:** `AUTHORIZED — EVALUATION ONLY`  
**Authority:** Operator decisions W4.1-D4; schema-valid output is **not** proof of good strategy.

## Categories

Each category defines: quality criterion, critical defects, warnings, machine-checkable invariants, expert-judgement fields, evidence requirements.

### 1. Evidence grounding

| Field | Definition |
|-------|------------|
| **Criterion** | Every strategic claim traces to pack evidence or marked assumption |
| **Critical** | Invented competitor fact; diagnostic evidence as production authority |
| **Warning** | Thin evidence citation; assumption not labeled |
| **Invariants** | `evidence_refs_exist`, `no_fabricated_observed_facts` |
| **Expert** | Citation relevance, freshness interpretation |
| **Evidence** | `evidence_inventory`, `statements`, authority matrix |

### 2. Objective correctness

| Field | Definition |
|-------|------------|
| **Criterion** | Strategic objective matches business model and conversion path |
| **Critical** | Lead-gen objective on e-commerce direct-sale model without operator decision |
| **Warning** | Secondary conversion omitted when pack lists it |
| **Invariants** | `objective_matches_business_authority` |
| **Expert** | Multi-objective trade-off |
| **Evidence** | `business_authority`, `service_ownership` |

### 3. Demand-tier policy

| Field | Definition |
|-------|------------|
| **Criterion** | T1–T5 activation follows pack tiers and operator launch mode |
| **Critical** | T5 merged with T1; rejected tier activated |
| **Warning** | T3/T4 launched without staged gate |
| **Invariants** | `t5_isolated`, `rejected_phrases_not_activated`, `tier_policy_respected` |
| **Expert** | Tier prioritization under budget pressure |
| **Evidence** | `demand_tier_registry`, `tier_distribution` |

### 4. Campaign architecture coherence

| Field | Definition |
|-------|------------|
| **Criterion** | Campaigns split by real service/demand/geo differences; implementable in Yandex Direct |
| **Critical** | Incompatible landings mixed; artificial fragmentation without rationale |
| **Warning** | Over-segmentation; under-segmentation of distinct services |
| **Invariants** | `campaign_has_landing_or_blocker`, `cluster_has_owner` |
| **Expert** | Segmentation rationale, Direct feasibility |
| **Evidence** | `semantic_clusters`, `service_ownership`, `landing_inventory` |

### 5. Keyword ownership preservation

| Field | Definition |
|-------|------------|
| **Criterion** | Clusters map to approved services; no orphan activation |
| **Critical** | Unassigned cluster activated |
| **Warning** | Cross-service phrase leakage |
| **Invariants** | `cluster_has_owner`, `no_unassigned_activation` |
| **Expert** | Ownership ambiguity resolution |
| **Evidence** | `service_ownership_registry`, `semantic_cluster_registry` |

### 6. Negative strategy safety

| Field | Definition |
|-------|------------|
| **Criterion** | Negative conflicts surfaced; rejected phrases not activated |
| **Critical** | Negative conflict ignored; high-frequency rejected phrase activated |
| **Warning** | Incomplete global negatives |
| **Invariants** | `negative_conflicts_not_ignored`, `rejected_phrases_not_activated` |
| **Expert** | Negative scope vs reach trade-off |
| **Evidence** | `negative_intelligence_pack` |

### 7. Landing alignment

| Field | Definition |
|-------|------------|
| **Criterion** | Active clusters have matching landing; geo/CTA aligned |
| **Critical** | Campaign without landing and without explicit blocker |
| **Warning** | Mobile/technical gap not noted |
| **Invariants** | `campaign_has_landing_or_blocker`, `landing_matches_service` |
| **Expert** | Multi-landing selection |
| **Evidence** | `landing_inventory`, alignment results |

### 8. Offer alignment

| Field | Definition |
|-------|------------|
| **Criterion** | Ad promise supported by offer inventory |
| **Critical** | Offer claim contradicts pack |
| **Warning** | Weak CTA-offer linkage |
| **Invariants** | `offer_refs_from_inventory` |
| **Expert** | Offer positioning |
| **Evidence** | `offer_inventory` |

### 9. Bidding maturity fit

| Field | Definition |
|-------|------------|
| **Criterion** | Bidding family matches tracking, conversions, operator constraints |
| **Critical** | Auto conversion bidding without tracking/goals/data |
| **Warning** | Manual bidding without operating policy |
| **Invariants** | `no_auto_bidding_without_conversions`, `tracking_blocks_auto` |
| **Expert** | Hybrid staged transition gates |
| **Evidence** | `measurement_requirements`, conversion history |

### 10. Budget honesty

| Field | Definition |
|-------|------------|
| **Criterion** | Unknown budget not invented; allocation marked as scenario when numeric |
| **Critical** | Invented monthly budget as client authority |
| **Warning** | Missing `BUDGET DECISION REQUIRED` |
| **Invariants** | `no_invented_budget`, `budget_decision_when_unknown` |
| **Expert** | Allocation rationale |
| **Evidence** | `business_authority.monthly_budget` |

### 11. Measurement readiness

| Field | Definition |
|-------|------------|
| **Criterion** | Tracking gaps block corresponding bidding activation |
| **Critical** | Production activation with tracking gap hidden |
| **Warning** | Goals listed but not validated |
| **Invariants** | `tracking_gap_blocks_bidding` |
| **Expert** | Goal hierarchy |
| **Evidence** | measurement contract, operator tracking status |

### 12. Blocker preservation

| Field | Definition |
|-------|------------|
| **Criterion** | Pack blockers appear in strategy; no false production claim |
| **Critical** | Missing Paid SERP hidden; critical blocker omitted |
| **Warning** | Excessive provisional blocking |
| **Invariants** | `blockers_preserved`, `provisional_not_production` |
| **Expert** | Blocker remediation accuracy |
| **Evidence** | `pack.blockers`, `pack_readiness` |

### 13. Provisional/production distinction

| Field | Definition |
|-------|------------|
| **Criterion** | Provisional pack → provisional strategy only |
| **Critical** | Provisional marked production-ready |
| **Warning** | Ambiguous status language |
| **Invariants** | `provisional_not_production` |
| **Expert** | Degradation path clarity |
| **Evidence** | `pack_readiness` |

### 14. Operator-decision clarity

| Field | Definition |
|-------|------------|
| **Criterion** | Explicit, compact list of operator decisions required |
| **Critical** | Hidden policy decisions in narrative |
| **Warning** | Operator overload (>8 decisions without grouping) |
| **Invariants** | `operator_decisions_explicit` |
| **Expert** | Decision prioritization |
| **Evidence** | `operator_decisions_required` |

### 15. Internal consistency

| Field | Definition |
|-------|------------|
| **Criterion** | Objective, tiers, campaigns, bidding, budget align |
| **Critical** | Contradictory tier and campaign mapping |
| **Warning** | Narrative vs structured field mismatch |
| **Invariants** | `output_reconciliation` |
| **Expert** | Cross-section coherence |
| **Evidence** | Full strategy object |

## Quality gates

**Critical (must be zero):** fabricated production facts, invented budget authority, hidden critical blockers, rejected demand activation, campaign without landing/blocker, provisional marked production.

**Target:** schema-valid rate 1.0; evidence-link validity ≥0.99; critical invariant pass rate 1.0; material stability contradiction ≤0.05.
