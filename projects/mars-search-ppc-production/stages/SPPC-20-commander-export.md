# SPPC-20 — Commander Export

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-20-commander-export.md`

---

## Stage ID

SPPC-20

## Name

Commander Export

## Purpose

Generate Yandex Direct Commander transport XLSX from validated production artifacts. Export is transport-only — no semantic or strategic decisions at this stage.

## Owning system

Commander Export

## Participating systems

- Campaign Production (source artifacts)
- Validators (pre-export gate)

## Required inputs

- SPPC-19 qa_passed token with export_ready true
- Architecture, distribution, ad, alignment, and bidding manifests
- Commander template version
- Exporter tool version

## Optional inputs

- Operator spot-check sample size

## Source-of-truth rules

- Production JSON/manifests remain SoT for meaning; XLSX is disposable transport snapshot.
- Exporter maps fields — it does not invent keywords, negatives, or copy.
- Template version and exporter version must be recorded on every export.

## Required processing

- Verify SPPC-19 export_ready and SPPC-09 conflict-free status.
- Run exporter CLI against bound artifact bundle.
- Run transport validation (duplicates, sheet split, hygiene).
- Stamp export manifest with versions and checksum.
- Hand off XLSX to SPPC-21 — no launch.

## Required outputs

- Commander XLSX transport file
- Export manifest: template version, exporter version, checksum
- Transport validation log

## Prohibited outputs

- Semantic reclassification or tier changes
- New keywords or ads not in production manifests
- Launch or budget activation
- Export without qa_passed token
- Strategic decisions embedded in exporter run

## Validation rules

- qa_passed and export_ready true.
- Transport validation PASS.
- Checksum recorded; row counts reconcile with manifests.
- Export log explicitly marks transport-only role.

## Blocking conditions

- SPPC-19 incomplete or export_ready false
- SPPC-09 unresolved conflicts
- Transport validation FAIL
- Attempt to export from undated strategy or pilot corpus

## Completion status

COMPLETE when XLSX and export manifest committed and `export_transport_ready` token issued.

## Evidence requirements

- XLSX path (gitignored acceptable) + export manifest in repo
- Transport validation log
- Exporter and template version IDs

## Next allowed stages

- SPPC-21

## Rollback / reopen behavior

Any production artifact change invalidates export; regenerate from SPPC-19.

## Responsible role

Commander Export operator

## Operator approval required

no

## Charter notes

**Charter rule:** Commander Export is **transport only**. It maps validated manifests to XLSX — no admission decisions, no strategy changes, no negative invention. Meaning SoT remains ORCA production artifacts.
