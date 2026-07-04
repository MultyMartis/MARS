# FP-0002 V9-06D.4 RERUN Rewrite Flush Status v1

## Default policy

Rewrite flush is **NOT PERFORMED** in V9-06D.4.

## Observation

| Path | Generated permalink | HTTP |
|---|---|---:|
| `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | MATCH (Service 74) | **404** |

All other authorized visual QA URLs returned HTTP 200.

## Classification

`REWRITE_FLUSH_MICRO_GATE_REQUIRED`

## Why not flushed in D.4

Operator authorization for this task explicitly excludes rewrite flush by default. Flush is allowed only when:

1. DB checkpoint exists
2. object/ACF writes passed
3. dry-run identifies only `rewrite_rules` option update
4. operator authorization explicitly includes rewrite flush

Condition 4 is **not** met.

## Recommended next action

`REWRITE_FLUSH_MICRO_GATE` — separate operator-authorized micro-gate to flush rewrite rules for Service CPT routes, then re-check Service 74 HTTP status.

## Follow-on (2026-07-04)

REWRITE-FLUSH-MICRO-GATE executed: soft flush PASS; Service 74 still HTTP 404 → `FLUSH_NOT_SUFFICIENT`. See `FP-0002-REWRITE-FLUSH-MICRO-GATE-RESULT-v1.md`.
