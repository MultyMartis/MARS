# ORCA Full-Corpus Semantic Capability Audit v1

**Date:** 2026-06-23  
**JSON:** [ORCA-FULL-CORPUS-SEMANTIC-CAPABILITY-AUDIT-v1.json](./ORCA-FULL-CORPUS-SEMANTIC-CAPABILITY-AUDIT-v1.json)

## Summary

| Layer | Status |
|-------|--------|
| Enforcement core (P0-I) | **OPERATIONAL** |
| Semantic candidate generation | **RULES ONLY** — deterministic assessor |
| Live LLM/model | **MISSING / NOT VALIDATED** |
| Full-corpus production runner | **IMPLEMENTED (Wave 3)** |
| Corvonero production semantic | **FROZEN** |

## Eight audit answers

1. **What makes the semantic decision?** `deterministic-assessor.mjs` (wraps pilot regex engine) → reassessment → adjudication → invariants.
2. **Real assessor vs rules?** Rules only in-repo; no executable LLM provider.
3. **Runtime contracts consumed?** 17 contracts via P0-I contract loader (taxonomy, schema, invariants, admission policy, annotation guideline).
4. **Auto-generated fields?** phrase_id, tri-state decision, likelihoods, tier, ownership, cluster_id, review routing, pack checksums.
5. **Full-corpus scale outputs?** Scale test 500/500 reconciled; no approved client corpus production run.
6. **Why 70 ABSTAIN from 200 in P0-I?** 67% `TOPIC_ONLY_INSUFFICIENT_EVIDENCE`, 27% `PROBLEM_QUERY_AMBIGUITY` — conservative mode by design.
7. **Dominant uncertainty families?** Topic-only 1С relevance; problem/support queries; career/DIY/product ambiguity.
8. **Reuse vs replace?** Reuse enforcement shell + corpus; replace pilot assessor and Corvonero v1 decisions; build live model + benchmark.
