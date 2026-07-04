# FP-0002 Rewrite Flush Rollback Plan v1

**Gate:** REWRITE-FLUSH-MICRO-GATE  
**Date:** 2026-07-04  
**Rollback status:** READY (not executed)

## Checkpoint

`X:\MARS-Localhost\backups\wordpress\projects\shpigovsky\rewrite-flush-micro-gate-pre-20260704-174923\`

| Artifact | Path |
|---|---|
| DB dump | `database\mars_wp_fp0002-rewrite-flush-micro-gate-pre.sql` |
| Rewrite baseline | `rewrite-baseline\rewrite-rules-baseline.json` |
| Object baseline | `wordpress-state\object-content-baseline-summary.json` |
| Instructions | `rollback\ROLLBACK-INSTRUCTIONS.md` |

## Pre-flush hashes (restore targets)

| Item | Value |
|---|---|
| `rewrite_rules` hash | `c3e9cb3746da51c81226e4b8e517004c6a0ca0a5eb73a6ea5225c2a8af1aa110` |
| Pages | 23 |
| Services | 15 |
| Posts | 1 (pre-existing) |
| Menus | 3 |

## Post-flush hashes (current)

| Item | Value |
|---|---|
| `rewrite_rules` hash | `bf3926c71b7b134708fa052f782c911dcc931dd61b1964a49b034d5b546c3a12` |

## Restore procedure

1. Stop writes to the local FP-0002 runtime.
2. Restore only local DB `mars_wp_fp0002` from the checkpoint SQL dump.
3. Re-validate rewrite_rules hash and seeded object combined hashes.
4. Confirm Pages=23, Services=15, menus unchanged, Service 74 HTTP matches pre-flush baseline (404).

## Expected rollback route behavior

Same as pre-flush: six D.4 QA URLs HTTP 200; Service 74 HTTP 404; generated permalinks unchanged.

## Why rollback was not executed

Flush completed safely with no scope drift. Service 74 remaining 404 is classified `FLUSH_NOT_SUFFICIENT`, not flush-induced breakage of previously working routes.
