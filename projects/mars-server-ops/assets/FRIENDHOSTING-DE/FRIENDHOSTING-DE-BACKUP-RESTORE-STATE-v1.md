# FRIENDHOSTING-DE — Backup / restore state v1

**inventory_ref:** FRIENDHOSTING-DE  
**Status:** **CANONICAL** freeze record  
**Critical distinction:**

```text
BACKUP VERIFIED  ≠  FULL DISASTER RESTORE TESTED
```

---

## 1. Latest dual-wave operational backup (current preferred twin)

| Field | Value |
|-------|-------|
| Archive name | `friendhosting-operational-20260830T132309Z.tgz` |
| Stamp | `20260830T132309Z` |
| Remote path | `/root/mars-backups/friendhosting-operational-20260830T132309Z.tgz` |
| Local path | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-operational-20260830T132309Z.tgz` |
| Size | **80743234** bytes |
| SHA-256 | `a434c1fdd178c3df133b74b503e8298b150a6640727c15d89aee341b9bf6e617` |
| Remote/local | **MATCH** |
| Readability | **PASS** |
| Restore procedure | **CONFIRMED** |
| Bare-metal restore | **NOT YET EXERCISED** |

Report: [../../reports/MARS-SERVER-OPS-DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01.md](../../reports/MARS-SERVER-OPS-DUAL-LOCAL-BACKUP-FRIENDHOSTING-VEESP-01.md)  
Procedure: [../../runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md](../../runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md)

---

## 2. Prior final operational freeze (retained)

| Field | Value |
|-------|-------|
| Archive name | `friendhosting-final-operational-20260830T125003Z.tgz` |
| Stamp | `20260830T125003Z` |
| Remote path | `/root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz` |
| Local path | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-final-operational-20260830T125003Z.tgz` |
| Size | **80746687** bytes |
| SHA-256 | `1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2` |
| Remote/local | **MATCH** |
| Restore procedure | **CONFIRMED** |
| Bare-metal restore | **NOT YET EXERCISED** |

Report: [../../reports/MARS-SERVER-OPS-FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01.md](../../reports/MARS-SERVER-OPS-FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01.md)

Prefer **`20260830T132309Z`** for current accepted state unless a charter names the earlier freeze.

---

## 3. What “BACKUP VERIFIED” means

- Archive exists remote + local  
- Hashes match  
- Tar list/readable  
- Written restore steps exist and were reviewed against archive contents  

---

## 4. What “FULL DISASTER RESTORE TESTED” would require

Separate charter to:

- restore onto clean OS (or equivalent destructive drill);  
- re-prove SSH / nginx / ACME / 3X-UI / Xray / six clients;  
- file evidence under Storage/evidence;  

Until then: **NOT YET EXERCISED**.

---

## 5. Historical archives

Prior P2 / P3 / P3.1 backups remain historical checkpoints. Dual-wave local directory currently holds **10** `.tgz` archives (no cleanup in DUAL-LOCAL-BACKUP-01).

---

## 6. Programme model

[../../BACKUP-RESTORE-MODEL-v1.md](../../BACKUP-RESTORE-MODEL-v1.md)

---

*Backup/restore state v1 · updated 2026-08-30 (dual local wave).*
