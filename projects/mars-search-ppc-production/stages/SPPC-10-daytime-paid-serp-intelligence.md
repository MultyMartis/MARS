# SPPC-10 — Daytime Paid SERP Intelligence

**Lifecycle:** MARS Search PPC Production v1
**Stage file:** `SPPC-10-daytime-paid-serp-intelligence.md`

---

## Stage ID

SPPC-10

## Name

Daytime Paid SERP Intelligence

## Purpose

Collect paid SERP snapshots during business hours via MIG PAID SERP BUSINESS HOURS mode to inform strategy, competitor cues, and ad format expectations. Degraded mode applies when collection is incomplete.

## Owning system

MIG (mode: PAID SERP BUSINESS HOURS)

## Participating systems

- ORCA (consumption)
- Operator (degraded mode acceptance)

## Required inputs

- SPPC-02 sources_registered token
- Target query sample from ACCEPT registry or strategist slice
- Business hours window definition (timezone, weekdays)
- SERP provider configuration reference

## Optional inputs

- SPPC-08 cluster representatives
- Competitor domain watchlist

## Source-of-truth rules

- Committed SERP snapshot pack is SoT for daytime paid landscape at capture time.
- Snapshots are time-stamped; stale SERP does not override fresh intake.
- Degraded mode flag is SoT when business-hours collection incomplete.

## Required processing

- Schedule captures within defined business hours window only.
- Record ad presence, formats, domains, and approximate positions.
- Tag queries missing SERP data or captured outside window.
- If coverage below threshold, emit degraded_mode manifest.
- Deliver SERP pack to SPPC-11 and SPPC-12 consumers.

## Required outputs

- Daytime paid SERP snapshot pack
- Coverage report: queries captured vs planned
- degraded_mode flag (true/false) with reason codes

## Prohibited outputs

- Campaign structure decisions
- Final bid recommendations
- SERP data presented as 24/7 representative without disclaimer

## Validation rules

- Capture timestamps fall within business hours window or flagged exception.
- Coverage metrics computed and attached.
- Degraded mode explicitly set when coverage incomplete.

## Blocking conditions

- SPPC-02 incomplete
- Zero captures without degraded mode declaration
- Business hours window undefined

## Completion status

COMPLETE when SERP pack committed and `serp_intelligence_ready` or `serp_degraded_mode` token issued.

## Evidence requirements

- SERP snapshot pack path
- Coverage and hours compliance report
- Degraded mode operator acknowledgment if applicable

## Next allowed stages

- SPPC-11
- SPPC-12

## Rollback / reopen behavior

Re-capture opens SPPC-10 only; analytical pack consumers must refresh bindings.

## Responsible role

MIG SERP operator

## Operator approval required

yes — when degraded_mode requires strategic acceptance

## Charter notes

**Charter rule:** Paid SERP collection runs in **business hours mode** only. If captures are missing or below coverage threshold, system enters **degraded mode** — downstream stages may proceed only with operator acknowledgment and degraded_mode flag on SPPC-12 pack.
