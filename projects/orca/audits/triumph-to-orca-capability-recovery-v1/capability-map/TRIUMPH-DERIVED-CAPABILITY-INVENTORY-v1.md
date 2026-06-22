# Triumph-Derived Capability Inventory v1

**Machine-readable:** [`triumph-derived-capability-inventory-v1.json`](triumph-derived-capability-inventory-v1.json)

| ID | Capability | Source evidence | First appearance | Owner | Doc? | Impl? | Integrated? | Enforced? | Validated? | Consumer | Failure if absent |
|----|------------|-----------------|------------------|-------|------|-------|-------------|-----------|------------|----------|-------------------|
| C-01 | Business-first intake before keywords | Route freeze before JSON | 2026-05-28 freeze | ORCA | Yes | Partial | Corvonero v2 intake only | No | Battle only | Triumph export | Scope creep |
| C-02 | Scenario-based demand design | intent-groups-v1.md tiers | Triumph research | ORCA | Yes | Manual | Triumph only | No | Operator | JSON phrases | Volume-first garbage |
| C-03 | Operator-approved service scope lock | ORCA-LAW-01; route freeze | 2026-05-28 | Operator | Yes | JSON freezes | v7 recovery | Partial (v7 contract) | v7 audit | Contract validator | Service deletion |
| C-04 | Protected commercial seeds | ORCA-LAW-02; is_primary | JSON instance | Operator | Yes | Triumph JSON | v7 recovery package | Partial | v7 audit | Contract INV-SEED | Seed loss (v6) |
| C-05 | One intent per group | ORCA-LAW-03; SE-01 | validation rules | ORCA | Yes | validation-cli | Triumph | Partial | 345 rules | Groups | Budget bleed |
| C-06 | Commercial-intent review (employment/edu block) | ORCA-LAW-06; SE-03 | semantic-validation | ORCA | Yes | validation-cli | Triumph | Partial | Battle | Negatives | Info leakage |
| C-07 | Narrow group validity | ORCA-LAW-04/05 | intent-groups; GROUP-FIDELITY | ORCA | Yes | Partial | v7 fix | Partial | v7 | Contract | False HOLD |
| C-08 | Semantic ownership before negatives | ORCA-LAW-08 | cross-negative order | ORCA | Yes | cross-negative-matrix | Triumph | Partial | Battle | Export | Collisions |
| C-09 | Negatives separate neighbors not manufacture groups | ORCA-LAW-09 | CROSS-NEGATIVE-RULES | ORCA | Yes | JS matrix | Triumph | Partial | Battle | Groups | Artificial arch |
| C-10 | Landing alignment ad/group/URL | ORCA-LAW-10; LM-* | landing continuity | ORCA | Yes | validation-cli | Triumph | Partial | URL sync | LRL | QS/conversion risk |
| C-11 | Semantic freeze before export | JSON SoT + freezes | battle stable | ORCA | Yes | JSON instance | Triumph | Manual | Battle | Export | Drift |
| C-12 | Pre-export validation gate (345 rules) | validation-cli | Triumph tools | ORCA | Yes | CLI | Triumph | Human-trigger | Battle | Export | Transport errors |
| C-13 | Cross-negative mandatory pre-export | TRIUMPH-D03 | exporter v1.4 | ORCA | Yes | Script | Triumph | Partial | Battle | Commander | Sibling competition |
| C-14 | QA cannot mutate scope | ORCA-LAW-11 | lessons learned | ORCA | Yes | Contract | Planned | No | v6 counterexample | Repair pkgs | Scope loss |
| C-15 | Classifier advisory only | ORCA-LAW-13 | contract authority order | ORCA | Yes | Contract text | Not in clean-room | No | v4 failure | Classifier | Template admission |
| C-16 | Technical PASS ≠ commercial validity | ORCA-LAW-15 | lessons; v6 | ORCA | Yes | Contract | v7 gate | Partial | v7 | Operator | False confidence |
| C-17 | Independent XLSX/Commander review | ORCA-LAW-14 | GROUP-FIDELITY-QA | ORCA | Yes | Human process | Triumph | Manual | Battle | Launch | Hidden defects |
| C-18 | Operator review before launch | approval-gates-contract | Intelligence v0 | ORCA | Yes | Docs | Triumph | Manual | Battle | Operator | Auto-launch |
| C-19 | ACCEPT requires commercial evidence | SI admission policy; P0-C | 2026-06 SI docs | ORCA SI | Yes | **No** | **No** | **No** | **No** | Future classifier | Corvonero 1892 failure |
| C-20 | ABSTAIN under ambiguity | P0-C ABSTAIN standard | 2026-06 | ORCA SI | Yes | **No** | **No** | **No** | **No** | Annotation | Auto-accept |
| C-21 | Landing Readiness Layer | lessons learned → LRL | 2026-05-30 | ORCA | Yes | Docs | Partial | No | SAFE UNKNOWN | PPC export | Ad↔landing gap |
| C-22 | Campaign Production Contract | triumph-derived laws | 2026-06-22 | ORCA | Yes | Validator tool | v7 only | Partial | Tests | Export gate | Authority defects |

**Legend:** Documented / Implemented / Integrated / Enforced are **independent** dimensions.
