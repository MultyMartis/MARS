# SPPC-15 — Keyword and Negative Distribution

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-15-keyword-and-negative-distribution.md`

---

## Stage ID

SPPC-15

## Name

Keyword and Negative Distribution

## Purpose

Distribute ACCEPT keywords and negative intelligence into architecture group shells with match types and cross-route negatives attached.

## Owning system

Campaign Production

## Participating systems

- ORCA
- Validators

## Required inputs

- SPPC-14 architecture_locked token
- SPPC-09 negatives_ready token
- Architecture manifest
- Tier-augmented ACCEPT registry
- Negative intelligence pack

## Optional inputs

- Match type policy overrides
- Operator hold list from strategy

## Source-of-truth rules

- Distribution ledger is SoT for which keyword lives in which group with which match type.
- Negatives must match SPPC-09 pack version or newer resolved version.
- No keyword distribution without architecture binding.

## Required processing

- Place ACCEPT keywords into group shells per cluster map.
- Apply match type policy by tier and strategy.
- Attach group and campaign negatives from intelligence pack.
- Validate no positive/negative self-conflicts at group level.
- Emit distribution ledger for SPPC-16.

## Required outputs

- Keyword distribution ledger
- Negative attachment manifest
- Distribution validation report

## Prohibited outputs

- Ad copy
- Final bid values
- Export XLSX
- Keywords in groups without architecture ID

## Validation rules

- No ACCEPT keyword unassigned unless on strategy hold list.
- Negative pack version ≥ SPPC-09 committed version.
- No unresolved cross-route conflicts.

## Blocking conditions

- SPPC-14 or SPPC-09 incomplete
- Cross-negative conflicts unresolved
- Architecture token missing

## Completion status

COMPLETE when ledger committed and `distribution_complete` token issued.

## Evidence requirements

- Distribution ledger path
- Validation report
- Negative version binding

## Next allowed stages

- SPPC-16
- SPPC-19

## Rollback / reopen behavior

Architecture, negatives, or admission reopen forces redistribution.

## Responsible role

Campaign Production keyword lead

## Operator approval required

no
