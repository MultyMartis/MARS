# SPPC-12 — Dated Analytical Pack

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-12-dated-analytical-pack.md`

---

## Stage ID

SPPC-12

## Name

Dated Analytical Pack

## Purpose

Assemble a single dated cross-system analytical pack that binds semantic, SERP, competitor, and tier signals for strategy — the mandatory input to AI PPC Strategist.

## Owning system

Cross-system (ORCA lead assembly)

## Participating systems

- MIG
- ORCA
- ORCA Semantic Intelligence
- Operator (pack approval)

## Required inputs

- SPPC-06 tiers_assigned token
- SPPC-08 clusters_locked token
- SPPC-09 negatives_ready token (or in-progress with flag)
- SPPC-10 serp_intelligence_ready or serp_degraded_mode token
- SPPC-11 competitor_audit_ready token

## Optional inputs

- Budget scenarios from operator
- Historical performance SAFE UNKNOWN declarations

## Source-of-truth rules

- Dated analytical pack with embedded as-of date is SoT for strategy session inputs.
- Pack sections are authoritative only at pack version — not live registry edits.
- degraded_mode from SPPC-10 must appear in pack metadata when active.

## Required processing

- Assemble required sections into versioned pack.
- Stamp as-of date and source artifact versions.
- Compute executive summary metrics.
- Flag stale or missing sections.
- Emit pack for SPPC-13.

## Required outputs

- Dated analytical pack document (markdown + machine-readable index)
- Pack manifest listing section sources and versions
- Executive summary metrics sheet

## Prohibited outputs

- Campaign architecture decisions
- Commander export files
- Strategy without dated pack reference

## Validation rules

- All required sections present or explicitly marked MISSING with waiver.
- As-of date and pack version unique.
- Source artifact versions match committed paths.

## Blocking conditions

- SPPC-06 or SPPC-08 incomplete
- SPPC-10 token missing entirely
- Pack assembled without date stamp

## Completion status

COMPLETE when pack committed and `analytical_pack_dated` token issued.

## Evidence requirements

- Committed pack path
- Manifest with section checklist
- Operator approval on degraded sections if applicable

## Next allowed stages

- SPPC-13

## Rollback / reopen behavior

Any source stage reopen forces new pack version; strategist must re-bind.

## Responsible role

ORCA assembly lead; Operator pack sign-off

## Operator approval required

yes — pack completeness and degraded SERP acknowledgment

## Charter notes

**Charter rule — required pack sections:**
1. **Pack metadata** — as-of date, version, intake binding, degraded_mode flags
2. **Demand summary** — corpus scale, admission distribution, tier histogram
3. **Service ownership map** — counts and conflicts resolved
4. **Semantic clusters** — cluster catalog with tier and service binding
5. **Negative intelligence summary** — conflict status, unresolved blockers
6. **Daytime paid SERP** — coverage, business hours compliance, degraded notes
7. **Competitor audit** — domain summaries and compliance flags
8. **Executive metrics** — T1–T5 counts, ACCEPT rate, ABSTAIN backlog, key risks
9. **Strategy input index** — pointers for SPPC-13 gates
