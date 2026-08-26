# SAFE-UNKNOWN-v1

## Rule

Incomplete provenance → `SAFE_UNKNOWN`. Do not delete, spam-mark, process, archive destructively, change category, or hide from production.

## Inventory

Approximately **12–13** CLEAN rows classified SAFE_UNKNOWN (name heuristics such as `test` / `Synth*` **without** `SYNTHETIC_TEST` / `lead_synth_` / `msg_synth_` corroboration).

## Disposition

- **Not mutated** by cleanup scripts.
- Production selectors (`isTest` in reminder + patched `group_open`) may still **exclude** name-heuristic test-like rows from actionable queues — that is selector hygiene, not destructive cleanup.
- Human review list retained in private local forensic; no PII in Git.

## Counters

| Metric | Value |
|--------|------:|
| SAFE_UNKNOWN mutated by cleanup | **0** |
| PRODUCTION_REAL mutated by cleanup | **0** |
