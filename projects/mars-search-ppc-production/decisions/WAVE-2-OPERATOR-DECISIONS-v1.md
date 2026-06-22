# Wave 2 Operator Decisions — MIG Evidence Production Core v1

**Date:** 2026-06-23  
**Decision set:** `wave-2-operator-decisions-v1`

## Status summary

| Wave / subject | Status |
|----------------|--------|
| Wave 1 | `OPERATIONAL WITH DOCUMENTED PLATFORM BOUNDARY` |
| Wave 1.2 | `APPROVED — READY FOR CHECKPOINT` |
| Wave 2 | `IMPLEMENTATION AUTHORIZED` |
| Corvonero | `FROZEN` |

## W2-D1 — Wave 1

`OPERATIONAL WITH DOCUMENTED PLATFORM BOUNDARY`

Lifecycle gate, execution receipts, legacy lockdown, and bypass suites are green. Missing Paid SERP and Strategist runtimes correctly block downstream progress.

## W2-D2 — Wave 1.2 checkpoint

Authorized after selective verification of legacy entry-point lockdown scope.

## W2-D3 — Wave 2

`MIG EVIDENCE PRODUCTION CORE — AUTHORIZED`

Wave 2 implementation may proceed. Operator review required before operational approval. Do not self-grant `OPERATIONAL`.

## W2-D4 — Paid SERP

Canonical mode: **`PAID SERP — BUSINESS HOURS`**

Paid advertising evidence must include: local date, exact local time, timezone, weekday, region, device, query, advertising block observations, interruption/CAPTCHA status.

## W2-D5 — Business-hours policy

Business hours are project/region-aware. No universal fixed interval may be invented. Each project must define timezone, intended advertiser-active interval, collection windows, and exception policy.

## W2-D6 — Evidence honesty

No visible ad block means explicit evidence states (`NO ADS OBSERVED`, `COLLECTION DEGRADED`, `CAPTCHA / INTERRUPTION`) — not market conclusions or silent success.

## W2-D7 — Corvonero

Remain frozen. Read-only compatibility audit permitted; no new search collection authorized.
