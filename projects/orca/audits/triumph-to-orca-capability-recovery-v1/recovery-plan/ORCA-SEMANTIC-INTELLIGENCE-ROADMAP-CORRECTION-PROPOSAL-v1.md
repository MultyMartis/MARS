# ORCA Semantic Intelligence — Roadmap Correction Proposal v1

## Questions answered

| Question | Answer |
|----------|--------|
| Should P0-D be approved unchanged? | **No** — hold until integration/enforcement stage defined |
| Should it be amended? | **Yes** — add prerequisite: contract + P0-C admission consumer PASS on pilot slice |
| Should B0 start next? | **No** — blocked until integration stage |
| Is contract-integration stage required before B0? | **Yes** — evidence: clean-room registered contract but did not read it |
| Must Triumph evidence be added to P0-C examples? | **Recommended** — not blocking integration |
| Must Campaign Production Contract change? | **Minor merge** with P0-B invariants — not rewrite |
| Which components need runtime enforcement? | Admission (P0-C), contract validator at semantic gate, seed protection, architecture freeze order |
| Which documents should merge? | Campaign invariants ↔ P0-B record invariants; laws ↔ contract index |
| Shortest safe path back to Corvonero? | Integration stage → pilot annotation on MIG subset → contract PASS → then P0-D/B0 → semantic rerun on preserved corpus only |

---

## Option A — Continue current roadmap

Proceed: approve P0-D → B0 → classifier → Corvonero rerun.

| Pros | Cons |
|------|------|
| Momentum on SI documentation | **Repeats failure mode** — docs without pipeline consumption |
| Benchmark before build | Measures nonexistent admission runtime |

**Evidence against:** Corvonero clean-room had P0-A–C **approved or proposed** yet pipeline used regex — same class of gap.

---

## Option B — Insert integration/enforcement stage (recommended)

Insert **P0-I (Integration)** between P0-C and P0-D:

1. Wire `validate-campaign-production-contract.mjs` to semantic admission boundary  
2. Implement admission consumer using P0-B record + P0-C decision semantics (rules-first acceptable)  
3. Architecture freeze gate before bulk corpus processing  
4. Operator seed protection from MIG handoff  
5. Re-run **pilot slice only** (e.g. 200 phrases) — not full 2370  
6. Document PASS/FAIL with evidence  

Then: amend P0-D with integration prerequisites → operator approve P0-D → B0.

| Pros | Cons |
|------|------|
| Closes proven knowledge→execution gap | Delays benchmark calendar |
| Reuses Triumph + contract investment | Requires focused implementation (bounded) |
| Corvonero corpus preserved | Operator time for pilot review |

---

## Option C — Merge/reduce duplicated specification layers

Merge invariant registries and authority docs; single admission handbook referencing Triumph SE + P0-C.

| Pros | Cons |
|------|------|
| Less operator fatigue | Does not alone fix enforcement |
| Clearer ownership | Merge work parallel to integration |

**Best as adjunct to Option B**, not replacement.

---

## Option D — Hybrid correction

**P0-I integration** (Option B) + **selective merge** (Option C) + **P0-D amended** with:

- Prerequisite gate: integration PASS on pilot slice  
- Triumph + Corvonero failure examples in benchmark strata  
- Corvonero pilot charter unchanged in size but **blocked** until integration PASS  

---

## Recommendation: **Option D (Hybrid)**

**Evidence:**

1. Triumph success was **export-path enforcement** + **human architecture freeze**, not SI docs alone (`TRIUMPH-SEARCH-RK-STABLE-STATE-v1.md`).  
2. Corvonero clean-room **listed** contract AUTH-03 but script **did not load** it (consumption audit).  
3. P0-C **approved** (`78b0557`) — **implementation not started** per README.  
4. P0-D measures admission quality — **meaningless** without admission consumer (duplication audit).  
5. Contract validator **exists and passes tests** — shortest path is **INTEGRATE** not **REBUILD**.

**P0-D status:** `PROPOSED — ON HOLD` until P0-I completes.

**Corvonero:** remains **FROZEN** until operator sign-off on integrated admission pilot.
