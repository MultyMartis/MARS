# Corvonero — Knowledge-to-Execution Failure Analysis v1

Tests possible causes against repository evidence.

| # | Possible cause | Verdict | Evidence |
|---|----------------|---------|----------|
| 1 | Knowledge existed only in chat | **PARTIALLY CONFIRMED** | Triumph phrase curation likely chat-local; **but** freezes, JSON, validation-cli **are** in MARS |
| 2 | Knowledge existed only in project reports | **PARTIALLY CONFIRMED** | Laws/contract written 2026-06-22 **after** Corvonero failures; clean-room ran same day — integration lag |
| 3 | Wrong system owned the rule | **CONFIRMED** | Regex pipeline owned admission; contract owned export-only validator |
| 4 | Pipeline never consumed the contract | **CONFIRMED** | `run-clean-room-semantic-pipeline-v1.mjs` — no contract import; consumption audit |
| 5 | Validator checked structure not semantics | **CONFIRMED** | `semantic-core-integrity-validation-v1.json` counts; integration plan table |
| 6 | Semantic judgement delegated to weak rules/LLM | **CONFIRMED** | `classifyIntent` regex; v4 template classifier in historical branch |
| 7 | No benchmark | **CONFIRMED** | P0-D not approved; no gold rows |
| 8 | No gold labels | **CONFIRMED** | No annotated admission set for Corvonero |
| 9 | No ABSTAIN | **CONFIRMED** | P0-C ABSTAIN not implemented; bulk ELIGIBLE |
| 10 | Campaign/output schema drove admission | **NOT SUPPORTED** for clean-room | Admission driven by eligibility JSON not Commander schema |
| 11 | Authority order incomplete | **CONFIRMED** | Manifest lists contract; script ignores authority order |
| 12 | Operator review occurred too late | **CONFIRMED** | Workbook after 1892 accepts; report § operator review |
| 13 | Old labels contaminated new runs | **NOT SUPPORTED** for clean-room | Clean-room forbade v1–v7 semantic reuse; corpus-only restart |
| 14 | Files existed but not registered | **NOT SUPPORTED** | Contract registered AUTH-03 — **registered but not read** |
| 15 | Registered artifacts had no enforcement mechanism | **CONFIRMED** | Integration plan: "not delivered: full pipeline refactor" |

## Primary failure chain (evidence-backed)

```text
Wordstat corpus (2399 rows)
  → regex intent + service regex eligibility (no contract, no P0-C)
  → ~1892 auto-ACCEPT equivalents
  → career/education/DIY/informational blur in commercial bucket
  → post-hoc gate FAILED
  → operator D2 freeze
```

## Why Triumph knowledge did not control Corvonero

1. **Different admission posture:** Triumph never ran bulk corpus admission.
2. **Triumph enforcement is export-path tools**, not universal semantic admission runtime.
3. **Contract captured Triumph laws June 2026** — **after** Corvonero v1–v6 pain but **before** integration into clean-room script.
4. **P0 SI approved** — **documentation only**; clean-room pipeline not updated to SI-07 admission policy.
5. **Operator seeds in MIG** informed Wordstat expansion but **not** protected-seed gate in pipeline (ORCA-LAW-02).

## Corvonero career/education/DIY specific

Regex `CAREER`, `EDU`, `DIY` arrays **exist** in pipeline — they exclude **some** phrases. Failure mode: phrases matching `1с` context get `COMMERCIAL SERVICE` with `review: true` but eligibility still promotes to `ELIGIBLE COMMERCIAL` when `services.length > 0`. Product/configuration queries mapped to services without hire-intent proof.

**Evidence:** `run-clean-room-semantic-pipeline-v1.mjs` lines 65–139.
