# Forge WordPress — Backup / Rollback Standard v1

**ID:** FW-RB-03  
**Status:** ACTIVE  
**Date:** 2026-08-18  
**Class:** C  
**Evidence:** FP-0002 Layer B exact-file vs P14 full backup

---

## When exact-file backup is enough

Frequent UI/code waves with **operator-confirmed** recent full backup; small allowlist; DB object changes limited and snapshotted (post IDs, options keys).

Operator override “full backup not required this wave” is **wave-local**, not a policy change.

---

## When full files + DB backup is mandatory

- Major migration / re-import  
- Production baseline freeze  
- Final cutover / NS switch  
- Destructive DB operation  
- Unknown-risk schema changes  

Replace the “last complete dump” after content freeze before NS (P17-FU02 lesson).

Critical clarification:

- an old full backup is a **rollback artifact**, not automatic proof of current editorial truth;
- after editors keep working in production, full DB rollback requires impact review of content loss;
- when the issue is technical (SMTP, indexing, one option group, one plugin file), restore the smallest required scope instead of reverting the whole live DB.

---

## Rollback manifest format

```markdown
# Rollback manifest
Wave:
Host:
Layer-A (operator full): path / confirmed Y/N
Layer-B files: STORAGE path
DB objects: STORAGE path / IDs
Restore order: files then objects (or reverse — document)
Forbidden: git reset, restore of unrelated WIP
```

---

*FW-RB-03 v1.1 — clarifies rollback artifact vs current editorial truth.*
