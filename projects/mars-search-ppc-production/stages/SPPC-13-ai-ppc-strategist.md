# SPPC-13 — AI PPC Strategist

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-13-ai-ppc-strategist.md`

---

## Stage ID

SPPC-13

## Name

AI PPC Strategist

## Purpose

Produce a human-reviewed PPC strategy from the dated analytical pack. Strategy gates must pass before campaign production; jumping directly to Commander export is forbidden.

## Owning system

AI PPC Strategist

## Participating systems

- Operator
- ORCA
- Campaign Production (read-only)

## Required inputs

- SPPC-12 analytical_pack_dated token
- Dated analytical pack artifact
- Intake budget and KPI constraints

## Optional inputs

- Operator strategic priorities
- Brand positioning notes

## Source-of-truth rules

- Approved strategy document is SoT for campaign architecture intent.
- Strategy version binds to analytical pack version — no orphan strategies.
- Forbidden: Commander export or XLSX generation before strategy gates pass.

## Required processing

- Ingest dated analytical pack sections.
- Propose campaign topology, budget split, tier emphasis, and risk posture.
- Run strategy gates: pack freshness, admission completeness, negative conflict status, degraded SERP acknowledgment.
- Submit strategy for operator review.
- On approval, emit strategy authorization for SPPC-14.

## Required outputs

- PPC strategy document with version ID
- Strategy gate checklist (pass/fail per gate)
- Budget and tier emphasis recommendations
- Explicit non-goals and hold lists

## Prohibited outputs

- Commander XLSX or export bundles
- Keyword-level final bids without architecture stage
- Strategy referencing undated or pilot corpus
- Bypass of SPPC-14–19 production stages

## Validation rules

- All strategy gates documented PASS or waived with operator sign-off.
- Pack version ID matches SPPC-12 manifest.
- No export artifacts in strategist output directory.

## Blocking conditions

- SPPC-12 incomplete
- Any mandatory strategy gate FAIL without waiver
- Attempt to jump to SPPC-20
- Unresolved negative conflicts (from pack)

## Completion status

COMPLETE when strategy approved and `strategy_authorized` token issued.

## Evidence requirements

- Strategy document path
- Gate checklist artifact
- Operator approval timestamp

## Next allowed stages

- SPPC-14

## Rollback / reopen behavior

Pack refresh or intake change invalidates strategy; production stages halt.

## Responsible role

AI PPC Strategist operator; Operator approver

## Operator approval required

yes

## Charter notes

**Charter rule:** Strategy gates must pass before campaign production. **Forbidden:** direct jumps from strategist output to Commander export (SPPC-20). Production path is SPPC-14 → … → SPPC-19 → SPPC-20.
