# SPPC-09 — Negative Keyword Intelligence

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-09-negative-keyword-intelligence.md`

---

## Stage ID

SPPC-09

## Name

Negative Keyword Intelligence

## Purpose

Produce negative keyword intelligence after admission and ownership are complete. Cross-route negative conflicts block Commander export until resolved.

## Owning system

ORCA

## Participating systems

- MIG (SERP context)
- Validators
- Operator (conflict resolution)

## Required inputs

- SPPC-05 admission_complete token
- SPPC-07 ownership_bound token
- SPPC-08 clusters_locked token (recommended)
- Cross-negative rules pack version
- REJECT keyword set from admission

## Optional inputs

- Competitor brand lists
- Operator negative seeds
- SPPC-10 SERP intelligence (when available)

## Source-of-truth rules

- Negative matrix is SoT for what must not co-serve across routes.
- Negatives must not be finalized before admission and ownership — no pre-admission negative authority.
- Unresolved cross-route conflicts are hard blockers for SPPC-20 export.

## Required processing

- Generate campaign-level, group-level, and cross-route negatives from REJECT rows and rules.
- Build cross-negative conflict matrix across service owners and clusters.
- Flag conflicts where a positive in route A is negated incorrectly in route B.
- Require operator resolution for unresolved conflicts.
- Emit negative intelligence pack for SPPC-15 and SPPC-19.

## Required outputs

- Negative keyword intelligence pack
- Cross-negative conflict matrix with resolution status
- Rules pack version binding

## Prohibited outputs

- Negatives computed before SPPC-05 admission
- Export-ready XLSX
- Silent suppression of conflict rows

## Validation rules

- Admission and ownership tokens present in processing log.
- Conflict matrix built; zero unresolved conflicts for export path.
- Every negative traces to rule ID or REJECT admission row.

## Blocking conditions

- SPPC-05 or SPPC-07 incomplete
- Unresolved cross-negative conflicts
- Negatives generated on pre-admission snapshot

## Completion status

COMPLETE when negative pack committed, conflicts resolved or waived, and `negatives_ready` token issued.

## Evidence requirements

- Negative intelligence pack artifact
- Conflict matrix with resolution audit
- REPORT confirming post-admission/ownership ordering

## Next allowed stages

- SPPC-15
- SPPC-19
- SPPC-20

## Rollback / reopen behavior

Admission, ownership, or cluster change forces negative regeneration; export blocked until re-validated.

## Responsible role

ORCA negative intelligence operator

## Operator approval required

yes — required for conflict resolution and waivers

## Charter notes

**Charter rule:** Negative intelligence runs **after** commercial intent admission (SPPC-05) and service/meaning ownership (SPPC-07). Unresolved cross-route negative **conflicts block Commander export** (SPPC-20).
