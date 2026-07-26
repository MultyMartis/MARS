# METALLKA — Backup / Rollback Model v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B (PARTIAL panel UI)  
**Date:** 2026-07-26

```text
Do not create or restore backups in this phase.
```

---

## Classifications

| Question | Answer |
|----------|--------|
| **BACKUP AVAILABLE** | **YES** (operator attestation + programme intake) |
| **RESTORE AVAILABLE** | **YES** (operator attestation) |
| **RESTORE PROCEDURE UNDERSTOOD** | **PARTIAL** — hosting-native Beget backup/restore confirmed as capability; exact retention/UI not inspected (panel credentials incomplete in local secrets) |

---

## Model

| Item | Status |
|------|--------|
| Mechanism | Beget hosting-native backup |
| File backup | AVAILABLE (operator) |
| DB backup | AVAILABLE (operator) |
| Retention visible | **SAFE UNKNOWN** (panel not opened) |
| Restore scope | Hosting restore UI exists (operator) — exact file vs full account **PARTIAL** |
| Emergency restore owner | Operator / hosting account holder |
| Operator can restore independently? | **YES** (operator-confirmed capability) |
| Plugin directory rollback | Feasible via hosting restore or manual file replace from backup — **not tested** |
| Exact-file rollback | Feasible in principle via SFTP/SSH from backup — **not tested** |
| Plugin backup plugins | No dedicated Updraft etc. found |

---

## Gate implication

Mutation gates still require fresh backup proof per programme rules. Gate A discovery did **not** create a backup.

---

*Backup / Rollback Model v1.*
