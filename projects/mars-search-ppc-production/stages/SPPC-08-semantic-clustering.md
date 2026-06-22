# SPPC-08 — Semantic Clustering

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-08-semantic-clustering.md`

---

## Stage ID

SPPC-08

## Name

Semantic Clustering

## Purpose

Group owned ACCEPT keywords into semantic clusters that will inform ad groups and message themes without collapsing distinct commercial meanings.

## Owning system

ORCA

## Participating systems

- ORCA Semantic Intelligence
- Operator (cluster merges/splits)

## Required inputs

- SPPC-07 ownership_bound token
- Ownership manifest
- Clustering policy version

## Optional inputs

- Operator theme preferences
- Negative seed hints (non-binding)

## Source-of-truth rules

- Cluster assignment per keyword is SoT for ad group candidacy.
- Clusters are scoped within service owner — no cross-service clusters without charter.
- Cluster IDs are stable for a given clustering policy version.

## Required processing

- Cluster keywords within each service owner partition.
- Enforce minimum and maximum cluster size policy.
- Label clusters with theme summary and representative queries.
- Flag singleton and mega-clusters for operator review.
- Emit cluster map for SPPC-14+.

## Required outputs

- Semantic cluster map (keyword ID → cluster ID)
- Cluster metadata: theme, service owner, tier histogram
- Review queue for edge clusters

## Prohibited outputs

- Campaign or ad group IDs
- Final negatives list
- Ad headlines

## Validation rules

- Every owned ACCEPT keyword in exactly one cluster per service partition.
- Cluster policy version documented.
- No cross-service cluster without waiver.

## Blocking conditions

- SPPC-07 incomplete
- Unclustered owned keywords
- Policy version missing

## Completion status

COMPLETE when cluster map committed and `clusters_locked` token issued.

## Evidence requirements

- Cluster map artifact
- Cluster statistics report
- Edge cluster review outcomes

## Next allowed stages

- SPPC-09
- SPPC-12

## Rollback / reopen behavior

Ownership or clustering policy change reopens SPPC-08; campaign architecture must wait.

## Responsible role

ORCA clustering operator

## Operator approval required

no — yes only for edge cluster merge/split decisions
