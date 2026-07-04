# FP-0002 V9-06D.6 Runtime Delivery / Rollback Plan v1

**Date:** 2026-07-04
**Planning only** — no delivery in D.6

## Gates (later implementation)

1. Source implementation complete for the wave
2. PHP lint on changed PHP
3. Static validation / source manifest
4. Runtime checkpoint (files; DB if content/options writes)
5. Dry-run runtime delivery (ADDITIVE_ONLY, fail-closed)
6. Runtime source hash matching
7. Visual smoke (desktop/mobile) — no pixel-perfect claim

## Rollback

| Layer | Method |
|---|---|
| Source | git revert of theme/plugin commit(s) for the wave |
| Runtime files | restore pre-delivery runtime backup for owned theme/plugin paths only |
| DB | restore DB dump only if that wave performed DB writes |

## Forbidden

- Broad delete/copy/mirror
- Plugin install/update/delete
- Unattended ACF PRO updates
- Mixing path-ownership cleanup with delivery

## Result

COMPLETE
