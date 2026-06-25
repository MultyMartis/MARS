# ORCA Universal Benchmark Sampling Plan v1

**Plan ID:** `orca-universal-benchmark-sampling-plan`  
**Version:** v1  
**Date:** 2026-06-22  
**Status:** `PROPOSED — OPERATOR APPROVAL REQUIRED`  
**Machine reference:** [`orca-universal-benchmark-sampling-plan-v1.json`](orca-universal-benchmark-sampling-plan-v1.json)

---

## Purpose

Define **stratified quota sampling** across intent strata, domains, and difficulty for B0/B1/B2.

---

## Phase targets

| Phase | Phrases | Notes |
|-------|--------:|-------|
| B0 | 60–100 | Protocol qualification |
| B1 | 300–500 | Includes Corvonero pilot build |
| B2 | 1,200–2,000 | D5 universal target |

---

## Stratification

1. **Intent stratum** — target shares per [`../strata/ORCA-BENCHMARK-INTENT-STRATA-v1.md`](../strata/ORCA-BENCHMARK-INTENT-STRATA-v1.md)
2. **Domain** — min shares per [`../strata/ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md`](../strata/ORCA-BENCHMARK-DOMAIN-COVERAGE-v1.md)
3. **Difficulty** — shares per difficulty charter

Sampling method: **stratified quota** with documented shortfall backfill (operator waiver or adjacent stratum with audit).

---

## Corvonero pilot draw

- Size 300–500 within B1
- 100% double annotation
- Blind subset ≥ 100 drawn at allocation time — sealed before any model tuning

---

## Blind allocation

Universal blind pack: **300–400** phrases allocated at B2 planning; **never** included in dev/calibration exports.

---

## No rows in charter

This plan defines **quotas and procedure only**. Actual phrase lists are created post-approval in operational storage — not in this documentation package.
