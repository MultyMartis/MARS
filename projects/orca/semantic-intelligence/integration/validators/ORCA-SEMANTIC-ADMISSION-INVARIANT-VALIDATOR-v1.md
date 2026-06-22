# ORCA Semantic Admission Invariant Validator v1

**Validator ID:** `orca-semantic-admission-invariant-validator-v1`  
**Machine-readable:** [`orca-semantic-admission-invariant-validator-v1.json`](orca-semantic-admission-invariant-validator-v1.json)

---

## Purpose

Blocking post-decision validator enforcing P0-I minimum invariant set. Schema validation alone is insufficient.

---

## Severity model

| Severity | Behavior |
|----------|----------|
| `FATAL` | Halt pipeline run |
| `BLOCKING` | Record rejected from admission pass; counted in pilot metrics |
| `WARNING` | Logged; human review route |

---

## P0-I minimum blocking rules

| # | Rule | Error code | Severity |
|---|------|------------|----------|
| 1 | ACCEPT based only on topical/service match | `SI-INV-001` | BLOCKING |
| 2 | ACCEPT without positive commercial evidence | `SI-INV-002` | BLOCKING |
| 3 | ACCEPT with unresolved HIGH ambiguity | `SI-INV-003` | BLOCKING |
| 4 | ACCEPT with unresolved provider-vs-DIY conflict | `SI-INV-004` | BLOCKING |
| 5 | ACCEPT with unresolved career-vs-provider conflict | `SI-INV-005` | BLOCKING |
| 6 | ACCEPT with unresolved product-vs-service conflict | `SI-INV-006` | BLOCKING |
| 7 | Missing provenance for automated decision | `SI-INV-007` | BLOCKING |
| 8 | Missing taxonomy/schema/guideline versions | `SI-INV-008` | FATAL |
| 9 | Final service ownership before ACCEPT | `SI-INV-009` | BLOCKING |
| 10 | cluster/campaign/export fields in admission output | `SI-INV-010` | BLOCKING |
| 11 | Numeric narrative placeholders in interpretation | `SI-INV-011` | BLOCKING |
| 12 | Silent rewriting of malformed phrases | `SI-INV-012` | BLOCKING |
| 13 | Missing ABSTAIN route when required by policy | `SI-INV-013` | BLOCKING |
| 14 | Semantic mutation during export channel | `SI-INV-014` | BLOCKING |
| 15 | Required contract not loaded | `SI-INV-015` | FATAL |

Maps to invariants 1–20 in `orca-semantic-record-invariants-v1.json` with P0-I subset flagged `p0_i_blocking: true`.

---

## Validator output

Per record:

```json
{
  "query_id": "...",
  "validator_version": "v1",
  "pass": false,
  "violations": [{"code": "SI-INV-002", "severity": "BLOCKING", "invariant_id": 2}]
}
```

Run-level: `blocked_count`, `fatal_count`, `pass_rate` (informational only — not D3 quality proof).
