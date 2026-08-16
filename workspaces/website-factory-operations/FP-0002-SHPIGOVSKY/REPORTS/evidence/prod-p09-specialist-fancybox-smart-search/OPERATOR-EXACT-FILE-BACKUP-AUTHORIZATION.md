# PROD-P09 — Operator Backup Authorization (Exact-File Rollback Mode)

**Date:** 2026-08-14  
**Wave:** FP-0002 PROD-P09 Specialist Fancybox + Smart Search  
**Scope lock:** this wave only — do **not** generalize to unrelated future waves.

## Operator decision (explicit)

```text
FULL BEGET FILES + DB BACKUP NOT REQUIRED FOR PROD-P09
```

```text
P09 OPERATOR AUTHORIZATION — EXACT-FILE LOCAL ROLLBACK SNAPSHOTS USED INSTEAD OF FULL BEGET LAYER A
```

```text
P09 EXACT-FILE ROLLBACK MODE AUTHORIZED BY OPERATOR
```

## Policy applied

| Item | Value |
|------|--------|
| Full Beget Layer A (files + DB) required for this wave | **NO** |
| Exact-file production-before download + SHA-256 | **YES (mandatory)** |
| Snapshot root | `X:\AI MARS STORAGE\deployment-packs\fp-0002\prod-p09-layer-b-pre\` |
| DB / Admin / ACF mutations expected | **0** |
| If unexpected DB/ACF needed | **STOP** (do not broaden authorization) |

## Rollback method

Restore only affected file(s) from `prod-p09-layer-b-pre\` via exact SFTP put.  
Do **not** restore full site/DB for P09 regressions.
