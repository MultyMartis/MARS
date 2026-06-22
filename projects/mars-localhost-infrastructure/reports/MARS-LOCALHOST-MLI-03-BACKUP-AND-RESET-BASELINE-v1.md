# MARS Localhost MLI-03 — Backup and Reset Baseline v1

**Document type:** Backup and reset baseline validation  
**Version:** v1  
**Date:** 2026-06-23  
**Stage:** MLI-03  
**Git baseline:** commit `4621388` on `mars/post-cycle8-live-tests`

---

## Target

| Field | Value |
|-------|-------|
| Site | `fws-0001` |
| Site path | `D:\MARS-Localhost\sites\wordpress\synthetic\fws-0001` |
| Backup root | `D:\MARS-Localhost\backups\wordpress\synthetic\fws-0001\` |

---

## Baseline snapshot

| Field | Value |
|-------|-------|
| Snapshot id | `baseline-001` |
| Full path | `D:\MARS-Localhost\backups\wordpress\synthetic\fws-0001\baseline-001` |
| Created during | MLI-03 WordPress profile provisioning |

---

## Validation results

| Check | Result |
|-------|--------|
| Baseline backup directory created | **PROVEN** |
| Backup contains site + DB artefacts | **WITH LIMITATIONS** — path exists; contents not re-inventoried in this report pass |
| Restore drill executed | **NOT PROVEN** — restore not executed in this validation pass |
| Reset procedure documented | **WITH LIMITATIONS** — directory standard defines layout; operator reset runbook not executed here |

---

## Assessment

**PROVEN WITH LIMITATIONS**

- A named baseline snapshot (`baseline-001`) exists at the standard backup path.
- **Backup creation** is proven; **restore/reset execution** is not proven in MLI-03 this pass.

---

## Secrets

Backup archives may contain database dumps with credentials. Paths are documented; **no passwords** in this report. Handle per [MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md](../MARS-LOCALHOST-MYSQL-LOCAL-CREDENTIALS-POLICY-v1.md).

---

## Related

- [MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md](../MARS-LOCALHOST-DIRECTORY-STANDARD-v1.md)
- [MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md](../MARS-LOCALHOST-RUNTIME-MANIFEST-CONTRACT-v1.md)

---

*Backup and reset baseline report v1 — MLI-03.*
