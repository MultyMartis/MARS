# SPPC-05 — Commercial Intent Admission

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-05-commercial-intent-admission.md`

---

## Stage ID

SPPC-05

## Name

Commercial Intent Admission

## Purpose

Decide commercial fitness of each normalized keyword using ORCA Semantic Intelligence with mandatory ACCEPT, REJECT, or ABSTAIN outcomes. Regex or rule-only shortcuts are not final authority.

## Owning system

ORCA Semantic Intelligence

## Participating systems

- Operator (ABSTAIN resolution)
- MIG (context)
- Validators

## Required inputs

- SPPC-04 registry_normalized token
- Canonical keyword registry
- Admission policy pack version
- Business intake scope boundaries from SPPC-01

## Optional inputs

- Legacy commercial labels for disagreement audit
- Protected class definitions
- Operator pre-notes on edge cases

## Source-of-truth rules

- Admission decision per keyword is SoT in registry extension — one of ACCEPT, REJECT, ABSTAIN only.
- Semantic Intelligence model/policy pack is authoritative; regex filters may pre-sort but never finalize.
- ABSTAIN rows require escalation ladder resolution before export paths.

## Required processing

- Run Semantic Intelligence admission scorer per registry row.
- Assign ACCEPT, REJECT, or ABSTAIN with confidence and rationale code.
- Route ABSTAIN to escalation ladder: auto-retry → operator queue → policy amendment.
- Block ACCEPT for rows failing protected-class or scope gates.
- Emit admission ledger for SPPC-06.

## Required outputs

- Admission ledger with ACCEPT / REJECT / ABSTAIN per keyword ID
- Escalation queue for ABSTAIN rows
- Policy pack version and model run metadata
- Disagreement audit vs legacy labels (if provided)

## Prohibited outputs

- Binary pass/fail without ABSTAIN path
- Regex-only final decisions
- Silent promotion of ABSTAIN to ACCEPT
- Campaign keywords without admission status

## Validation rules

- 100% registry rows have exactly one of ACCEPT, REJECT, ABSTAIN.
- No ACCEPT without scope and protected-class check.
- Escalation ladder documented for every ABSTAIN.
- Policy pack version matches committed artifact.

## Blocking conditions

- SPPC-04 incomplete
- Any row missing admission decision
- ABSTAIN backlog above operator SLA without waiver
- Regex marked as sole authority in processing log

## Completion status

COMPLETE when admission ledger committed, ABSTAIN queue routed, and `admission_complete` token issued.

## Evidence requirements

- Admission ledger artifact
- Escalation queue export
- REPORT with ACCEPT/REJECT/ABSTAIN distribution

## Next allowed stages

- SPPC-06

## Rollback / reopen behavior

Policy pack or intake scope change reopens admission; prior ACCEPT rows re-scored.

## Responsible role

ORCA Semantic Intelligence operator; Operator for ABSTAIN resolution

## Operator approval required

yes — required when ABSTAIN escalation reaches human queue

## Charter notes

**Charter rule:** ACCEPT / REJECT / ABSTAIN only. Escalation ladder: (1) auto-retry with alternate context, (2) operator review queue, (3) policy amendment charter. Regex and heuristics may assist routing but are **not** final admission authority.
