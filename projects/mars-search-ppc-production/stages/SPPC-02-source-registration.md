# SPPC-02 — Source Registration

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-02-source-registration.md`

---

## Stage ID

SPPC-02

## Name

Source Registration

## Purpose

Register and fingerprint every external data source MIG will consume: Wordstat exports, site crawls, SERP providers, competitor feeds, and operator-supplied files. No ingestion without registered provenance.

## Owning system

MIG

## Participating systems

- ATLAS (scope binding)
- Operator

## Required inputs

- SPPC-01 intake_approved token
- Source file manifests with checksums
- Acquisition timestamps and method (export, API, crawl)
- Geography and language metadata per source

## Optional inputs

- Provider credentials reference (not secrets in repo)
- Prior MIG research pack pointers
- Throttling or rate-limit notes

## Source-of-truth rules

- MIG source registry is SoT for what was ingested and when.
- Unregistered files must not enter semantic or campaign pipelines.
- Checksum mismatch triggers re-registration, not silent overwrite.

## Required processing

- Register each source with ID, type, geography, and acquisition time.
- Compute and store checksums for all registered blobs.
- Bind sources to intake version from SPPC-01.
- Emit source registration manifest for SPPC-03.

## Required outputs

- MIG source registration manifest (JSON)
- Per-source metadata records with checksums
- Source-to-intake version binding record

## Prohibited outputs

- Semantic classifications
- Normalized keyword registry
- Campaign or ad artifacts

## Validation rules

- Every file slated for corpus intake appears in registry.
- Checksums reproducible on re-read.
- Geography and language align with intake scope.

## Blocking conditions

- SPPC-01 not complete
- Unregistered source referenced in downstream job
- Checksum failure without operator resolution

## Completion status

COMPLETE when manifest is committed and `sources_registered` token issued.

## Evidence requirements

- Committed source registration manifest
- Checksum audit log or inline hashes
- REPORT line listing source count and types

## Next allowed stages

- SPPC-03

## Rollback / reopen behavior

Adding or replacing sources reopens SPPC-02 and downstream semantic stages. Prior corpus artifacts marked stale until re-intake.

## Responsible role

MIG operator / research lead

## Operator approval required

no
