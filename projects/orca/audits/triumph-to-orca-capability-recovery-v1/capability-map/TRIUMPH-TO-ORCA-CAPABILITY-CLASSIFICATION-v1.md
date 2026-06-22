# Triumph-to-ORCA Capability Classification v1

**Machine-readable:** [`triumph-to-orca-capability-classification-v1.json`](triumph-to-orca-capability-classification-v1.json)

Primary classification per capability (exactly one):

| ID | Capability | Primary classification | Rationale |
|----|------------|------------------------|-----------|
| C-01 | Business-first intake | **PARTIALLY GENERALIZED** | Triumph freeze + Intelligence v0 intake; Corvonero v2 has intake |
| C-02 | Scenario-based demand design | **CHAT-LOCAL CAPABILITY** + **DOCUMENTED ONLY** in MARS | Doctrine captures intent; phrase curation not automated |
| C-03 | Operator scope lock | **EXISTS BUT NOT ENFORCED** | Contract + validator exist; clean-room pipeline skipped |
| C-04 | Protected seeds | **EXISTS BUT NOT INTEGRATED** | v7 recovery; not in clean-room admission |
| C-05 | One intent per group | **ALREADY EXISTS AND ENFORCED** (Triumph path only) | validation-cli SE-01 |
| C-06 | Commercial-intent blocklist | **ALREADY EXISTS AND ENFORCED** (Triumph path) | SE-03 + campaign negatives in JSON |
| C-07 | Narrow group validity | **EXISTS BUT NOT ENFORCED** | v6 violated; v7 fixed; clean-room N/A |
| C-08 | Ownership before negatives | **ALREADY EXISTS AND ENFORCED** (Triumph export) | Pipeline order in Triumph |
| C-09 | Negatives separate not manufacture | **ALREADY EXISTS AND ENFORCED** (Triumph) | cross-negative-matrix |
| C-10 | Landing alignment | **EXISTS BUT NOT INTEGRATED** | LRL documented; Corvonero semantic stage skipped LRL |
| C-11 | Semantic freeze | **PROJECT-SPECIFIC ONLY** (Triumph JSON SoT) | Pattern documented not universal runtime |
| C-12 | Pre-export validation 345 rules | **ALREADY EXISTS AND ENFORCED** (Triumph) | Human-triggered CLI |
| C-13 | Cross-negative mandatory | **ALREADY EXISTS AND ENFORCED** (Triumph) | Exporter gate |
| C-14 | QA cannot mutate scope | **DOCUMENTED ONLY** | Contract; repair history violates |
| C-15 | Classifier advisory only | **EXISTS BUT NOT ENFORCED** | Stated in contract; v4–v6 and clean-room violate |
| C-16 | Technical ≠ commercial validity | **EXISTS BUT NOT ENFORCED** until v7 | v6 false PASS |
| C-17 | Independent XLSX review | **MANUAL EXPECTATION** | Battle proven; not automated |
| C-18 | Operator launch gate | **DOCUMENTED ONLY** | approval-gates-contract |
| C-19 | ACCEPT requires commercial evidence | **DUPLICATED BY CURRENT P0 WORK** | Triumph had implicit operator curation; P0-C formalizes |
| C-20 | ABSTAIN | **NEWLY REQUIRED** (explicit) + **DUPLICATED BY P0** | Triumph used manual HOLD; no ABSTAIN terminal in tools |
| C-21 | Landing Readiness Layer | **EXISTS BUT NOT INTEGRATED** | Archive + index; not in Corvonero semantic pipeline |
| C-22 | Campaign Production Contract | **PARTIALLY GENERALIZED** | New 2026-06; overlaps Triumph freezes + SI admission |

## P0 layer classifications

| P0 artifact | Classification |
|-------------|----------------|
| P0-A SI architecture SI-01–17 | **FORMALIZATION** of fragmented Triumph + research practice |
| P0-B taxonomy/schema | **FORMALIZATION** + **NEWLY REQUIRED** machine record |
| P0-C annotation guideline | **STRENGTHENING** Triumph manual review → explicit ACCEPT/REJECT/ABSTAIN |
| P0-D benchmark charter | **NEWLY REQUIRED** for measurable admission — **not duplicate** of Triumph battle QA |

## Duplication watchlist

| New SI doc | Prior Triumph/ORCA doc | Verdict |
|------------|------------------------|---------|
| ORCA-SEMANTIC-ADMISSION-POLICY | generation-logic intent purity | Formalization — **operational diff:** needs runtime |
| ORCA-COMMERCIAL-EVIDENCE-STANDARD | SE-03 / operator phrase review | Strengthening — **not redundant** if enforced |
| ORCA-SEMANTIC-ANNOTATION-GUIDELINE | validation rules + operator judgment | Consolidation — **risk:** doc without pipeline read |
| Universal benchmark charter | Triumph 345 validation rules | **Different layer** — benchmark ≠ export validation |
