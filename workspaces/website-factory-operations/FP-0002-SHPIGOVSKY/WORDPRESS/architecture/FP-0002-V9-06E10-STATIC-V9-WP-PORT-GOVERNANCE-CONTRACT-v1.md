# FP-0002 V9-06E10 Static V9 WP Port Governance Contract v1

**Status:** PROPOSED — mandatory for all future FP-0002 WordPress port tasks  
**Evidence JSON:** `validation/v9-06e10-full-backup-wp-port-root-cause-audit/static-v9-wp-port-governance-contract.json`

## 1. Primary authority

Static V9 HTML under `workspaces/fp-0002-shpigovsky-v9/src/` and rendered `dist/` is the **primary layout authority** for every V9-backed route. WordPress theme partials are **derivatives**, not co-equal design sources.

## 2. Direct section-stack parity

For V9-backed pages, porting means **one section stack per page** matching static HTML order, classes, and inner markup — not "V9-compatible" semantic reconstruction from ACF/CPT/helpers.

## 3. Pre-repair section map

No repair task may begin without a committed **static-to-WP section map** listing: order, static partial, WP partial, content class, gap, action.

## 4. Screenshot gate

No layout/visual task may claim **PASS** without side-by-side static V9 vs WP runtime screenshots for every route in scope.

## 5. DOM probes are diagnostic only

Section-class probes, HTTP 200 smoke, and marker checks are **supporting evidence only**. They cannot override failed visual parity.

## 6. No extra blocks

WP output must not contain sections/blocks absent from static V9 unless explicitly tagged **DEMO** or **OPERATOR_APPROVED** in the task charter and content inventory.

## 7. No missing blocks

Every static V9 section must appear on WP unless explicitly **DEFERRED** with operator sign-off.

## 8. Content classification

Each content field must be exactly one of:

| Class | Meaning |
|-------|---------|
| EXACT_V9 | Must match static HTML copy byte-for-byte (modulo WP entities) |
| DEMO | Fixture/lorem present in static V9 — show in inventory |
| OPERATOR_REAL_CONTENT | Operator-provided production copy |
| DEFERRED | Not in scope this wave |

Mixed or mutated text paths are forbidden.

## 9. Pre-V9 partial risk

Any partial classified **OLD_PRE_V9_PARTIAL** or **SEMANTIC_RECONSTRUCTION** is **HIGH RISK** on V9-backed routes and requires explicit charter admission.

## 10. Post-repair inventory

Every repair wave must update **final content/demo inventory** JSON and architecture doc before PASS.

## Stop tokens

- `STOP — NO STATIC SECTION MAP`
- `STOP — PROBE-ONLY VALIDATION`
- `STOP — SEMANTIC REBUILD WITHOUT CHARTER`
