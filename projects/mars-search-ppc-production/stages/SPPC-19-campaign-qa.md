# SPPC-19 — Campaign QA

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-19-campaign-qa.md`

---

## Stage ID

SPPC-19

## Name

Campaign QA

## Purpose

Run validators across architecture, keywords, negatives, ads, landing alignment, and bidding before any Commander export. QA failure blocks SPPC-20.

## Owning system

QA / Validators

## Participating systems

- Campaign Production
- ORCA
- Operator

## Required inputs

- SPPC-15 distribution_complete token
- SPPC-16 ads_produced token
- SPPC-17 landing_aligned token
- SPPC-18 bidding_strategy_locked token
- SPPC-09 negatives_ready token
- Validator ruleset version

## Optional inputs

- Spot-check query list from operator
- Prior QA failure remediations

## Source-of-truth rules

- QA report with pass/fail per rule is SoT for export eligibility.
- Validators assist humans — failures require remediation or operator waiver.
- No export when mandatory rules fail.

## Required processing

- Run structural validation against architecture manifest.
- Validate keyword/negative consistency and cross-route matrix.
- Lint ads for compliance and format.
- Verify URL alignment and tracking.
- Check bidding manifest completeness.
- Emit QA report with export_ready boolean.

## Required outputs

- Campaign QA report (rule-level pass/fail)
- export_ready flag
- Remediation ticket list for failures

## Prohibited outputs

- Commander XLSX (reserved for SPPC-20)
- Launch authorization
- QA pass without evidence logs

## Validation rules

- All mandatory validator rules executed.
- export_ready true only when zero mandatory failures or waivers documented.
- Artifact versions match production ledger.

## Blocking conditions

- Any upstream production token missing
- Mandatory QA rule FAIL
- Unresolved negative conflicts
- export_ready false

## Completion status

COMPLETE when QA report committed with export_ready true and `qa_passed` token issued.

## Evidence requirements

- QA report path
- Validator ruleset version
- Waiver log if applicable

## Next allowed stages

- SPPC-20

## Rollback / reopen behavior

Any production artifact change reopens QA; export_ready revoked.

## Responsible role

QA validator operator

## Operator approval required

yes — for mandatory rule waivers
