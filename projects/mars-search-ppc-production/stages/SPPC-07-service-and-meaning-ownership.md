# SPPC-07 — Service and Meaning Ownership

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-07-service-and-meaning-ownership.md`

---

## Stage ID

SPPC-07

## Name

Service and Meaning Ownership

## Purpose

Bind each ACCEPT keyword to an owned service line, landing meaning, and offer surface so downstream clustering and ads do not invent product semantics.

## Owning system

ORCA

## Participating systems

- ATLAS (scope)
- Operator (ownership disputes)
- Website Factory (landing inventory)

## Required inputs

- SPPC-06 tiers_assigned token
- Tier-augmented ACCEPT registry
- Service catalog from intake
- Landing / offer inventory or SAFE UNKNOWN manifest

## Optional inputs

- Site intelligence pack
- Cross-sell rules

## Source-of-truth rules

- Service ownership field per keyword is SoT for meaning routing.
- Unowned ACCEPT keywords block clustering and campaign production.
- Landing URL assignments are provisional until SPPC-17 alignment.

## Required processing

- Map each ACCEPT keyword to exactly one primary service owner.
- Attach meaning tags: intent class, offer type, geo modifier handling.
- Flag conflicts: keyword maps to multiple services or none.
- Emit ownership manifest for SPPC-08.

## Required outputs

- Service ownership manifest keyed by keyword ID
- Conflict report with resolution status
- Provisional landing pointers where known

## Prohibited outputs

- Final ad copy
- Cluster IDs without ownership
- Invented services not in catalog

## Validation rules

- 100% ACCEPT rows have primary service owner or documented conflict in queue.
- No keyword with two primary owners without split rule.
- Service catalog version bound.

## Blocking conditions

- SPPC-06 incomplete
- Unresolved ownership conflicts above threshold
- Service catalog missing

## Completion status

COMPLETE when ownership manifest committed and `ownership_bound` token issued.

## Evidence requirements

- Ownership manifest artifact
- Conflict resolution log
- Service catalog version reference

## Next allowed stages

- SPPC-08
- SPPC-09

## Rollback / reopen behavior

Service catalog or intake change reopens ownership; clusters and negatives invalidated.

## Responsible role

ORCA meaning architect; Operator for conflict resolution

## Operator approval required

yes — when ownership conflicts reach human queue
