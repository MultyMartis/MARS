# Post-cutover rollback design (PG-compatible)

## Forbidden

Do **not** treat Sheets-based `Operational.dev` as a valid rollback after PostgreSQL becomes SoT and new PG-only mutations exist.

## Strategy

1. Prefer rollback to a previous **PG-compatible** candidate/release registered in `mars_core.workflow_releases` (same data contract family).
2. Today there is only one PG-compatible Operational candidate (`Operational.v3.dev`). Therefore, before cutover wave:
   - either pin a frozen export/hash of v3 as `rollback-copy` release metadata, **or**
   - keep a dedicated inactive `Operational.v3.rollback` clone of the accepted export (still INACTIVE until needed).
3. Immediate post-cutover rollback window: reversion of n8n active flag to the pinned PG-compatible release **before** divergent PG-only writes, OR controlled compensating jobs if writes already happened.
4. Sheets remains projection-only after cutover — not rollback SoT.

## Pre-cutover resolution required

Create/register a PG-compatible rollback pin of the accepted v3 export hash before activating live Gmail on v3.
