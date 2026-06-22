# SPPC-14 — Campaign Architecture

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-14-campaign-architecture.md`

---

## Stage ID

SPPC-14

## Name

Campaign Architecture

## Purpose

Translate authorized strategy into campaign topology: campaigns, directions, and group shells aligned to clusters and service owners.

## Owning system

Campaign Production

## Participating systems

- ORCA (cluster binding)
- QA (structure review)

## Required inputs

- SPPC-13 strategy_authorized token
- Approved strategy document
- SPPC-08 cluster map
- SPPC-07 ownership manifest

## Optional inputs

- Platform-specific naming conventions
- Historical campaign naming

## Source-of-truth rules

- Campaign architecture artifact is SoT for structural IDs.
- Architecture must trace to strategy version and cluster map version.
- No keyword or ad content at this stage — structure only.

## Required processing

- Define campaigns aligned to strategy budget split.
- Map clusters to ad group shells within service partitions.
- Assign directional labels and platform metadata.
- Validate structure against strategy non-goals.
- Emit architecture manifest for SPPC-15.

## Required outputs

- Campaign architecture manifest (campaign / direction / group shells)
- Cluster-to-group mapping table
- Architecture validation report

## Prohibited outputs

- Populated keyword rows
- Ad copy
- Bids or budgets as final values
- XLSX export

## Validation rules

- Every in-scope cluster maps to exactly one group shell or documented split.
- Strategy version bound.
- No orphan group shells.

## Blocking conditions

- SPPC-13 incomplete
- Cluster map version mismatch
- Strategy non-goals violated

## Completion status

COMPLETE when architecture committed and `architecture_locked` token issued.

## Evidence requirements

- Architecture manifest path
- Mapping validation report

## Next allowed stages

- SPPC-15

## Rollback / reopen behavior

Strategy or cluster change reopens architecture; downstream distribution cleared.

## Responsible role

Campaign Production architect

## Operator approval required

no
