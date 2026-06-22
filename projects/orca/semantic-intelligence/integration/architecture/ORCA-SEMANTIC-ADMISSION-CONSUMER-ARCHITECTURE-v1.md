# ORCA Semantic Admission Consumer Architecture v1

**Doc ID:** `orca-semantic-admission-consumer-architecture-v1`  
**Date:** 2026-06-22  
**Status:** `PROPOSED — P0-I`

---

## Overview

P0-I replaces manifest-only registration with a **consumer graph** at the admission boundary (SI-07 / SI-08). Each consumer owns load, version check, application, blocking behavior, and audit trace for one contract family.

```text
                    ┌─────────────────────────┐
                    │  Contract Loader (I-01) │
                    │  reads loading manifest │
                    └───────────┬─────────────┘
                                │
        ┌───────────────────────┼───────────────────────┐
        ▼                       ▼                       ▼
┌───────────────┐     ┌─────────────────┐     ┌─────────────────┐
│ Taxonomy      │     │ Schema          │     │ Annotation      │
│ Consumer      │     │ Consumer        │     │ Policy Consumer │
└───────┬───────┘     └────────┬────────┘     └────────┬────────┘
        │                      │                         │
        └──────────────────────┼─────────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Admission           │
                    │ Orchestrator (I-03) │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                      ▼
┌───────────────┐     ┌─────────────────┐   ┌─────────────────┐
│ Invariant     │     │ Risk Mode       │   │ Operator Scope  │
│ Consumer      │     │ Consumer        │   │ Consumer        │
└───────┬───────┘     └────────┬────────┘   └────────┬────────┘
        │                      │                     │
        └──────────────────────┼─────────────────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Version Authority   │
                    │ Consumer            │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Invariant Validator │
                    │ (I-04) BLOCKING     │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Human Review Router │
                    │ (I-05)              │
                    └──────────┬──────────┘
                               ▼
                    ┌─────────────────────┐
                    │ Contract Consumption│
                    │ Report (I-07)     │
                    └─────────────────────┘
```

---

## Consumer responsibilities

| Consumer | Contract family | Blocks pipeline |
|----------|-----------------|-----------------|
| Taxonomy | P0-B controlled vocabularies | Yes — enum validation |
| Semantic record schema | P0-B JSON Schema | Yes — shape validation |
| Annotation policy | P0-C decision semantics | Yes — decision rules |
| Invariant | P0-B invariants registry | Yes — post-decision |
| Risk mode | P0-A admission policy | Yes — threshold gates |
| Operator scope | Project business scope | Yes — scope prohibition |
| Version authority | ADR authority model | Yes — version mismatch |

---

## Orchestration rules

1. **Load order** is defined in contract loading manifest — not ad hoc.
2. **No consumer may skip version check** for required contracts.
3. **Semantic record generator (I-02)** must populate all required schema fields before invariant validation.
4. **Legacy regex adapter (I-06)** runs in parallel diagnostic channel only — never overrides ACCEPT/REJECT/ABSTAIN.
5. **Contract-consumption report (I-07)** must list every required contract with `loaded`, `version_matched`, `fields_consumed`.

---

## Failure modes (global)

| Condition | Error code | Severity |
|-----------|------------|----------|
| Required contract not loaded | `BLOCKED — REQUIRED SEMANTIC CONTRACT NOT LOADED` | FATAL |
| Version mismatch | `BLOCKED — SEMANTIC CONTRACT VERSION MISMATCH` | FATAL |
| Schema validation fail | `SI-VAL-001` | BLOCKING |
| Invariant violation | `SI-INV-*` | BLOCKING |
| Unregistered contract referenced | `SI-REG-001` | WARNING → FATAL if required |

---

## Integration classification

After pilot run, each contract entry receives status:

- `INTEGRATED` — all five I6 criteria met
- `REGISTERED — NOT INTEGRATED` — manifest only
- `LOADED — NOT CONSUMED` — read but not applied
- `DEPRECATED` — legacy regex authority (must not be INTEGRATED for admission)
