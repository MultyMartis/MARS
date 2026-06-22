# SPPC-21 — Dry Run and Operator Approval

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-21-dry-run-and-operator-approval.md`

---

## Stage ID

SPPC-21

## Name

Dry Run and Operator Approval

## Purpose

Operator reviews campaign readiness at the correct abstraction — campaigns, groups, strategy risks, and QA summary — not line-by-line approval of every keyword.

## Owning system

Operator

## Participating systems

- QA
- Campaign Production
- Commander Export

## Required inputs

- SPPC-20 export_transport_ready token
- Commander XLSX and export manifest
- SPPC-19 QA report
- SPPC-13 strategy document
- Dry-run checklist

## Optional inputs

- Spot-check keyword samples
- Simulated import preview screenshots

## Source-of-truth rules

- Operator approval record is SoT for authorization to import.
- Approval binds to export manifest checksum — different XLSX requires re-approval.
- Approval granularity: campaign/group/strategy level — not per-keyword unless escalated.

## Required processing

- Import dry-run or sandbox preview where platform allows.
- Review QA summary, tier emphasis, budget split, and negative conflict status.
- Spot-check representative groups — not full keyword enumeration.
- Record approve / hold / reject with rationale.
- On approve, emit import_authorized token for SPPC-22.

## Required outputs

- Operator approval record with checksum binding
- Dry-run checklist completed
- Hold or reject tickets if not approved

## Prohibited outputs

- Per-keyword mandatory sign-off grid as default gate
- Launch without explicit import_authorized
- Approval of different checksum than export manifest

## Validation rules

- Approval record references export manifest checksum.
- Dry-run checklist complete.
- Strategy and QA artifacts version-bound.

## Blocking conditions

- SPPC-20 incomplete
- Checksum mismatch vs approval record
- QA export_ready false
- Operator reject without remediation plan

## Completion status

COMPLETE when operator approves and `import_authorized` token issued.

## Evidence requirements

- Signed approval record
- Dry-run checklist artifact
- Checksum match audit

## Next allowed stages

- SPPC-22

## Rollback / reopen behavior

New export or production change revokes import_authorized; return to SPPC-19 or SPPC-20.

## Responsible role

Operator (account owner)

## Operator approval required

yes

## Charter notes

**Charter rule:** Operator approval at the **right abstraction** — campaigns, budget, risk summary, QA pass, representative spot checks. **Not** mandatory approval of every individual keyword.
