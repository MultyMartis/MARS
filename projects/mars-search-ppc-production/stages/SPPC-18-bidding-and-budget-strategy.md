# SPPC-18 — Bidding and Budget Strategy

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-18-bidding-and-budget-strategy.md`

---

## Stage ID

SPPC-18

## Name

Bidding and Budget Strategy

## Purpose

Define bidding approach and budget allocation per campaign with explicit manual vs automated branch selection and tier-weighted emphasis.

## Owning system

Campaign Production

## Participating systems

- Operator
- AI PPC Strategist (budget alignment)

## Required inputs

- SPPC-13 strategy_authorized token
- SPPC-14 architecture_locked token
- SPPC-06 tier assignments
- Intake budget envelope

## Optional inputs

- Platform automated bidding eligibility
- Historical CPC SAFE UNKNOWN notes

## Source-of-truth rules

- Bidding strategy artifact is SoT for bid mode and budget splits.
- Branch selection (manual vs automated) must be explicit per campaign.
- Placeholder bids in export are not final — operator calibrates in platform unless automated branch authorized.

## Required processing

- Allocate budget across campaigns per strategy.
- Select manual or automated bidding branch per campaign with rationale.
- Apply tier weights to initial bid guidance.
- Document calibration expectations for manual branch.
- Emit bidding manifest for SPPC-19 and SPPC-20.

## Required outputs

- Bidding and budget strategy manifest
- Manual vs automated branch declaration per campaign
- Initial bid guidance table (placeholders allowed for manual)

## Prohibited outputs

- Silent default to automated without declaration
- Budget exceeding intake envelope without waiver
- Final live bids presented as committed without operator calibration note

## Validation rules

- Every campaign has branch selection and budget line.
- Total budget ≤ intake envelope or waiver on record.
- Tier weights documented.

## Blocking conditions

- SPPC-13 or SPPC-14 incomplete
- Missing branch selection
- Budget overrun without waiver

## Completion status

COMPLETE when bidding manifest committed and `bidding_strategy_locked` token issued.

## Evidence requirements

- Bidding manifest path
- Branch selection audit
- Budget sum reconciliation

## Next allowed stages

- SPPC-19
- SPPC-20

## Rollback / reopen behavior

Strategy or budget envelope change reopens bidding; export waits for re-lock.

## Responsible role

Campaign Production budget lead; Operator for envelope waivers

## Operator approval required

yes — automated branch and budget envelope exceptions

## Charter notes

**Charter rule:** Explicit **manual vs automated** branch per campaign. Manual branch expects operator calibration post-import; automated branch requires platform eligibility and operator authorization.
