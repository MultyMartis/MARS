# OLYA-INTEGRITY-AFTER-RESTORE-v1

## MOD_B access

- **Final state:** active (E67145502141) @ mod-b-restore.json

## Lead inventory (post-restore baseline @ 11:40:02Z)

- Total leads in MOD_B actor events: **14**
- pending: **1** (hash12 bd9c7ee3f398 — production; not used in tests)
- spam: **13**

## Integrity assessment

- No evidence of lead deletion or status mutation on Olya production lead during isolation window.
- Pre-revoke dedicated baseline overwritten; **SAFE UNKNOWN** for bit-exact pre/post lead hash diff.
- Post-restore capture shows stable production-like inventory with MOD_B active.

## Olya real leads baseline (post-restore): **14**
