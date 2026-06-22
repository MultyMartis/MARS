# Triumph-to-ORCA Recovery Decisions v1

**Machine-readable:** [`triumph-to-orca-recovery-decisions-v1.json`](triumph-to-orca-recovery-decisions-v1.json)  
**Status:** Recommendations only — **no implementation in this audit**

| Gap / asset | Decision | Rationale |
|-------------|----------|-----------|
| Triumph validation-cli (345 rules) | **REUSE** | Proven export gate — not admission gate |
| Triumph cross-negative-matrix | **REUSE** | Post-ownership negative pattern |
| Triumph JSON SoT pattern | **REUSE** | Architecture freeze + meaning layer |
| Triumph intent-groups / doctrine | **INTEGRATE** | Into P0-C examples + architecture freeze templates |
| Campaign Production Contract | **ENFORCE** | Exists; must run before semantic batch accept |
| Contract validator tool | **INTEGRATE** | Wire to admission + export; already tested |
| triumph-derived-orca-laws | **MERGE** | Into contract + SI invariants index — single registry |
| orca-production-contract-integration-plan | **EXTEND** | Execute planned wiring — not rewrite |
| P0-C annotation guideline | **ENFORCE** | Via admission module or human loop — not shelf |
| P0-B semantic record schema | **INTEGRATE** | Replace ad-hoc eligibility JSON shape |
| Clean-room regex pipeline | **DEPRECATE** | As admission authority — keep as diagnostic artifact only |
| Corvonero v1–v7 production semantic | **DO NOT DUPLICATE** | Historical anti-pattern only |
| P0-D benchmark charter | **INVESTIGATE FURTHER** | After integration stage — hold per audit |
| Bulk Wordstat → auto accept | **DO NOT DUPLICATE** | Triumph did opposite — architecture first |
| New classifier LLM layer | **DO NOT DUPLICATE** | Before contract + P0-C integration |
| MIG Wordstat corpus (Corvonero) | **REUSE** | Preserved corpus — valid SI-02 input |
| Landing Readiness Layer | **INTEGRATE** | Before Corvonero campaign export path |
| Chat-local phrase judgment | **INVESTIGATE FURTHER** | Capture via P0-C annotation on seed set |
| SI architecture ADR | **REUSE** | Target shape — do not rebuild |
| Duplicate invariant docs (P0-B vs campaign) | **MERGE** | Reduce operator confusion |
| Operator seed registry from MIG | **INTEGRATE** | ORCA-LAW-02 before expansion |
| ABSTAIN policy | **ENFORCE** | From P0-C — default for ambiguity |
| B0 benchmark rows | **DO NOT DUPLICATE** | Until admission consumer exists |
