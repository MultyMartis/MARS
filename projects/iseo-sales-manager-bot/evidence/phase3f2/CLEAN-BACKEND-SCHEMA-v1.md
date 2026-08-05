# CLEAN BACKEND SCHEMA v1 — Phase 3F.2

## Source of truth

The full target `lead_clean_v2` column list is documented in [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md) §3 (Identity/timestamps, Client, Request/attribution, Processing, Quality, Reply, Duplicate, Manager lifecycle, Diagnostics). This file records Phase 3F.2-specific schema observations only — it does not restate the full column list.

## Columns relevant to this phase

| Column | Role in Phase 3F.2 |
|---|---|
| `manager_status` | Tri-state (`pending`/`processed`/`spam`) authoritative lifecycle field — target of the reconciliation write, see [EVGENIY-LIFECYCLE-RECONCILIATION-v1.md](EVGENIY-LIFECYCLE-RECONCILIATION-v1.md) |
| `telegram_action_token` | Callback-resolution token; confirmed present in the schema mapping but observed empty (`stored_len=0`) on Клиент A's row at callback time, and non-empty on only 9/106 CLEAN rows overall — see [CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md](CALLBACK-NOT-FOUND-ROOT-CAUSE-v1.md) |
| `parser_version` | Observed schema/mapping lag: live Parse ran `sm-parser-v3.3`, CLEAN write reflected `sm-parser-v3.2` — known anomaly, not fixed in this pass |
| `message_format`/`message_format_version` | Same lag pattern: live Format ran `sm-msg-v2.4`, CLEAN write reflected `sm-msg-v2.2` |
| `is_probable_test` | Read by `isProbableTest()` in `implementation/runtime-libs/pending-leads-lib.mjs`; drives the [TEST-DATA-SEPARATION-v1.md](TEST-DATA-SEPARATION-v1.md) split |
| `received_at` (identity/timestamp group) | Preserved as Gmail `internalDate` through reconciliation — never overwritten by a later processing step |

## Known anomaly (not a Phase 3F.2 fix target)

`parser_version` and `message_format`/`message_format_version` on the CLEAN row can lag one minor version behind the live node output at the moment of append (observed once, on Клиент A's row). This is recorded here as a **known anomaly** for future triage — Phase 3F.2 scope was the callback-token defect only; this mapping lag is explicitly **not** repaired in this pass.

## Status

| Item | Status |
|---|---|
| `telegram_action_token` presence in schema mapping | **CONFIRMED** (column exists, mapping exists) |
| `telegram_action_token` populated at append time for new rows | **PARTIAL** — deterministic Lead Processor contract calls for pre-append population (see [CALLBACK-LOOKUP-REPAIR-v1.md](CALLBACK-LOOKUP-REPAIR-v1.md)); live coverage across all intake paths not independently re-verified in this pass |
| `parser_version`/`message_format` mapping-lag anomaly | **SAFE UNKNOWN** root cause; **not fixed** |

*Related: [LEAD-EVENT-HISTORY-v1.md](LEAD-EVENT-HISTORY-v1.md), [architecture/LEAD-DATA-MODEL-v1.md](../../architecture/LEAD-DATA-MODEL-v1.md).*
