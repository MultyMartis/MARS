# SPPC-16 — Ad Production

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-16-ad-production.md`

---

## Stage ID

SPPC-16

## Name

Ad Production

## Purpose

Produce compliant ad copy variants per group shell following strategy tone, intake compliance, and platform format limits.

## Owning system

Campaign Production

## Participating systems

- QA (copy compliance)
- Operator (brand voice)

## Required inputs

- SPPC-15 distribution_complete token
- Distribution ledger
- Intake compliance and brand rules
- Strategy tone and offer guidance

## Optional inputs

- Approved copy templates
- A/B variant count policy

## Source-of-truth rules

- Ad copy artifact is SoT for headlines, descriptions, and display paths.
- Copy must reference group IDs from distribution ledger.
- Compliance rules from intake override creative preference.

## Required processing

- Draft ads per group with required format fields.
- Run compliance lint against intake prohibitions.
- Ensure uniqueness constraints per platform rules.
- Attach final URLs as provisional pending SPPC-17.
- Emit ad copy pack for SPPC-17 and SPPC-19.

## Required outputs

- Ad copy pack keyed by group ID
- Compliance lint report
- Provisional URL map

## Prohibited outputs

- Non-compliant claims from competitor audit
- Export XLSX
- Ads without group binding

## Validation rules

- Every active group has ≥1 compliant ad variant.
- Compliance lint PASS or waived with operator sign-off.
- Character limits satisfied per platform spec.

## Blocking conditions

- SPPC-15 incomplete
- Compliance lint FAIL without waiver
- Missing ads for in-scope groups

## Completion status

COMPLETE when ad pack committed and `ads_produced` token issued.

## Evidence requirements

- Ad copy pack path
- Compliance lint artifact

## Next allowed stages

- SPPC-17
- SPPC-19

## Rollback / reopen behavior

Distribution or compliance rule change reopens ad production for affected groups.

## Responsible role

Campaign Production copy lead

## Operator approval required

no — yes for compliance waivers only
