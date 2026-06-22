# SPPC-06 — Demand Priority Segmentation T1–T5

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-06-demand-priority-segmentation-t1-t5.md`

---

## Stage ID

SPPC-06

## Name

Demand Priority Segmentation T1–T5

## Purpose

Assign demand priority tiers T1 through T5 to ACCEPT-admitted keywords to drive budget, bid, and production sequencing without conflating tier with campaign structure.

## Owning system

ORCA

## Participating systems

- ORCA Semantic Intelligence
- Operator (tier dispute resolution)

## Required inputs

- SPPC-05 admission_complete token
- Admission ledger (ACCEPT rows only)
- Tiering rubric version
- Business intake KPI and budget signals

## Optional inputs

- Historical conversion proxies
- Seasonal weighting notes

## Source-of-truth rules

- Tier field on ACCEPT rows is SoT for demand priority.
- Each ACCEPT row carries exactly one tier T1–T5.
- REJECT and ABSTAIN rows carry no tier.

## Required processing

- Score ACCEPT rows against tiering rubric.
- Assign T1 (highest priority) through T5 (lowest priority).
- Document tie-break rules and manual overrides.
- Emit tier distribution report for SPPC-07.

## Required outputs

- Tier-augmented registry subset for ACCEPT rows
- Tier definitions binding document (embedded in contract)
- Distribution report: counts per tier

## Prohibited outputs

- Campaign or ad group assignments
- Bid values
- Keywords without tier on ACCEPT rows

## Validation rules

- Every ACCEPT row has exactly one tier T1–T5.
- Tier definitions match rubric version.
- No REJECT/ABSTAIN rows tiered.

## Blocking conditions

- SPPC-05 incomplete
- ACCEPT row missing tier
- Rubric version mismatch

## Completion status

COMPLETE when tier assignments committed and `tiers_assigned` token issued.

## Evidence requirements

- Tier-augmented artifact
- Distribution report
- Override log if any manual tier changes

## Next allowed stages

- SPPC-07

## Rollback / reopen behavior

Rubric or admission reopen invalidates tiers; re-segment from SPPC-05 or SPPC-06 as scoped.

## Responsible role

ORCA demand analyst

## Operator approval required

no — yes only on documented tier dispute overrides

## Charter notes

**Charter rule — tier definitions:**
| Tier | Definition | Typical use |
|------|------------|-------------|
| **T1** | Core money intent — highest commercial fit, direct service match, operator-mandated must-win queries | Priority budget, first production wave, tight QA |
| **T2** | Strong commercial intent — clear buyer signal, minor ambiguity | Full production, standard bids |
| **T3** | Moderate intent — commercial but broader or comparative | Production with efficiency guardrails |
| **T4** | Exploratory intent — plausible demand, weaker conversion signal | Limited groups, test budgets |
| **T5** | Long-tail / reservoir — admitted but deprioritized; may be paused pre-launch | Hold or minimal presence unless strategy elevates |
