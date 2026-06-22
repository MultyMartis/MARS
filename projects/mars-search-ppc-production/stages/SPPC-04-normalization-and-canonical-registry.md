# SPPC-04 — Normalization and Canonical Registry

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-04-normalization-and-canonical-registry.md`

---

## Stage ID

SPPC-04

## Name

Normalization and Canonical Registry

## Purpose

Normalize raw corpus rows into a canonical keyword registry with stable IDs, deduplicated surface forms, and traceable lineage to source rows.

## Owning system

ORCA

## Participating systems

- MIG (source lineage)
- Operator (anomaly review)

## Required inputs

- SPPC-03 corpus_intake_complete token
- Full semantic corpus artifact
- Normalization ruleset version

## Optional inputs

- Legacy registry for merge-only comparison
- Operator synonym overrides

## Source-of-truth rules

- ORCA canonical keyword registry is SoT for normalized demand entities.
- Every registry row must trace to one or more corpus source rows.
- Normalization ruleset version is frozen per registry generation.

## Required processing

- Apply normalization: casing, whitespace, punctuation, locale rules.
- Deduplicate surface forms; assign stable canonical IDs.
- Preserve lineage pointers to corpus and source registry.
- Flag anomalies (encoding, empty, ultra-short) to quarantine.
- Emit registry manifest for SPPC-05.

## Required outputs

- Canonical keyword registry (JSON)
- Normalization report: dedupe stats, quarantine count
- Ruleset version binding record

## Prohibited outputs

- Commercial intent decisions (ACCEPT/REJECT)
- Campaign structure
- Tier assignments

## Validation rules

- Registry row count ≤ corpus unique forms; lineage complete.
- No orphan registry rows without corpus pointer.
- Ruleset version documented.

## Blocking conditions

- SPPC-03 incomplete
- Lineage gaps above threshold
- Ruleset version missing

## Completion status

COMPLETE when registry committed and `registry_normalized` token issued.

## Evidence requirements

- Committed registry artifact
- Normalization report with counts
- Lineage spot-check sample

## Next allowed stages

- SPPC-05

## Rollback / reopen behavior

Ruleset change or corpus reopen forces registry regeneration; downstream admission invalidated.

## Responsible role

ORCA semantic pipeline operator

## Operator approval required

no
