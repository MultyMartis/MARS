# FINAL SOAK PRODUCTION COUNTERS T0 v1

Sanitized. No customer PII.

## Baseline at final soak start (accepted)

| Counter | Value |
|---|---:|
| received | 1 |
| pending | 0 |
| processed | 1 |
| spam | 0 |
| Last processed production lead | 05.08.2026 17:22 МСК (PROD_LEAD_1) |

## Observed after T+0 (execution-ledger evidence)

| Alias | Ingest МСК | Delivery | Lifecycle note |
|---|---|---|---|
| PROD_LEAD_1 | historical | historical 3-recipient | processed @ 17:22 05.08 — baseline |
| PROD_LEAD_2 | 06.08.2026 16:26 | **3** cards; MOD_C revoked | status not re-read from Sheets this checkpoint (SAFE UNKNOWN exact pending/processed) |
| PROD_LEAD_3 | 06.08.2026 16:56 | **4** cards incl. reactivated MOD_C | callback action **spam** (two Admin callback execs) |

## Derived production counters (best-effort)

| Counter | Value | Notes |
|---|---:|---|
| production leads received (epoch cumulative, inferred) | ≥3 | baseline 1 + 2 post-T0 ingestions |
| production leads pending | SAFE UNKNOWN | requires Sheets `/stats` or LEADS read; no post-T0 command packet |
| production leads processed | ≥1 | PROD_LEAD_1; PROD_LEAD_2 unknown |
| production leads spam | ≥1 | PROD_LEAD_3 |
| production leads lost | 0 | both post-T0 ingestions completed Ops success path |
| production leads duplicated | 0 | duplicate class `new` on both ingestions |
| synthetic/probable_test in observed ingest path | 0 | |

## CONFIG runtime stamps (not authoritative lifecycle)

Ops wrote `last_production_processed_at=2026-08-06T13:56:47.466Z` (= **06.08.2026 16:56:47 МСК**) on PROD_LEAD_3 delivery success. This **diverges** from baseline PROD_LEAD_1 17:22 display expectation and is recorded as a watch/status-cache concern under STOP.

## Delivery opportunity note

Genuine production delivery opportunities **did** occur after T+0 (not manufactured).
