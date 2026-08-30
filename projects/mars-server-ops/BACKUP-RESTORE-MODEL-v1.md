# MARS Server Ops — Backup & Restore Model v1

**Status:** **documented** programme discipline  
**Not:** automated backup product, scheduled job engine, or proof that backups exist on any server

---

## 1. Purpose

Adapt reusable MARS patterns for **generic server operations**:

- [MARS Survivability](../mars-survivability/OPERATIONAL-INDEX.md) — snapshot manifest, rollback advisor  
- [MLI](../mars-localhost-infrastructure/OPERATIONAL-INDEX.md) — runtime vs brain separation, recovery scripts as human-invoked  
- [Forge WordPress Backup/Rollback](../mars-website-factory/subsystems/forge-wordpress/runbooks/FORGE-WORDPRESS-BACKUP-ROLLBACK-STANDARD-v1.md) — exact-file vs full backup, rollback manifest  
- [OCPilot Storage](../ocpilot/external-storage-registry.md) — bulk artifact placement  

**Phase 1A:** model only — **no backup commands**, no live backups.

---

## 2. Programme rule (Server Ops)

> **A backup is not considered operationally complete until a restore strategy exists.**

Where practical, restoration should be **tested** and evidence filed under Storage `restore-tests\`.

**Scope honesty:** This is a **Server Ops programme rule** derived from existing Survivability rollback discipline and Forge rollback lessons — **not** claimed as a new global MARS governance mandate unless separately chartered.

### 2.1 Required backup properties (completeness gate)

A backup entry is **incomplete** unless the following are recorded (or explicitly marked SAFE UNKNOWN with owner):

| Property | Requirement |
|----------|-------------|
| **Exact source** | Server/inventory_ref + paths/services covered |
| **Timestamp** | UTC preferred |
| **Location** | Storage / local / provider snapshot path (not Git for secret-bearing) |
| **Hash/checksum** | Where practical (`sha256` or equivalent) |
| **Readability** | Operator can open/list artifacts without undocumented tooling |
| **Restore procedure** | Written steps before relying on the backup |
| **Rollback boundary** | What will / will not be overwritten |
| **Post-restore validation** | How PASS is declared after restore |

VPN/FriendHosting lesson: pre-hardening backup waves must satisfy this gate **before** further production mutation.

### 2.2 BACKUP VERIFIED vs FULL DISASTER RESTORE TESTED

| Label | Means | Does **not** mean |
|-------|-------|-------------------|
| **BACKUP VERIFIED** | Archive exists (remote/local as required), hash/readability PASS, restore **procedure** written/confirmed | Bare-metal or destructive restore was executed |
| **FULL DISASTER RESTORE TESTED** | Chartered restore onto clean/damaged host with post-restore validation evidence | Ordinary backup creation alone |

FriendHosting final operational backup (`20260830T125003Z`): **BACKUP VERIFIED** · bare-metal restore **NOT YET EXERCISED**.  
Canonical pointer: [assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-BACKUP-RESTORE-STATE-v1.md](assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-BACKUP-RESTORE-STATE-v1.md).

---

## 3. Backup classes

| Class | Description | Typical artifacts |
|-------|-------------|-------------------|
| **A — Config** | Service configs, compose files, proxy vhost | Redacted or full in Storage `configs/` |
| **B — Service data** | Application files, non-DB state | Archive in `backups/` |
| **C — Database dump** | PostgreSQL/MySQL logical dump | `backups/` with manifest |
| **D — Docker volume** | Named volumes, bind mounts (bounded) | Volume export |
| **E — Certificates** | TLS certs/keys | Storage or local — **keys never Git** |
| **F — VPN / 3X-UI** | Panel export, Xray config | Storage — sanitize client secrets |
| **G — Pre-change checkpoint** | Baseline before MEDIUM+ change | `baselines/` |
| **H — Off-server copy** | Operator-controlled second location | **SAFE UNKNOWN** policy per operator |

---

## 4. Backup manifest (template)

Store alongside backup in Storage (Git may hold sanitized copy or pointer):

```markdown
# Backup manifest — Server Ops
manifest_id:
inventory_ref:
passport_ref:
charter_id:
created:
operator:
backup_class: A|B|C|D|E|F|G
source_server:
artifacts:
  - path:
    sha256: (optional)
    sensitivity: public|internal|secret
retention_until:
restore_procedure_ref:
restore_tested: yes|no|planned
notes:
```

---

## 5. Pre-change checkpoint expectation

Before **MEDIUM RISK** or higher external change:

1. Select backup class(es) appropriate to blast radius.  
2. Create manifest.  
3. Store artifacts under [STORAGE-MODEL-v1.md](STORAGE-MODEL-v1.md) paths.  
4. Document restore steps **before** executing change.  
5. Record checkpoint id in implementation charter and REPORT.

Aligns with Survivability snapshot requirement for MEDIUM+ repo work; external server work uses Storage baselines analogously.

---

## 6. Rollback artifact vs current truth

From Forge lesson (adapted):

- An old full backup is a **rollback artifact**, not proof of current production truth.  
- After continued production use, full restore may cause **content loss** — scope restore narrowly when issue is technical (one service, one DB, one config file).  
- Document **restore order** (files before DB or reverse) in charter.

---

## 7. Restore procedure (generic)

| Step | Action |
|------|--------|
| 1 | **STOP** active change; confirm charter rollback section |
| 2 | Identify manifest + baseline |
| 3 | Verify backup integrity (size, date, test hash if used) |
| 4 | Execute restore on scoped resources only |
| 5 | Validate service health per passport healthcheck |
| 6 | File evidence in `restore-tests/` or REPORT |
| 7 | Update passport `last_verified` / backup status |

**No automated restore by agents** unless future explicit tooling charter says otherwise.

---

## 8. Restore validation

After restore:

- Service responds on expected surface  
- Database connectivity (app user)  
- Reverse proxy route  
- VPN client smoke (if applicable) — operator-led  
- Document **residual UNKNOWN** if not fully verified  

---

## 9. Encryption & sensitivity

| Topic | Stance |
|-------|--------|
| **Encryption at rest** | Operator/provider responsibility — **SAFE UNKNOWN** for uniform policy |
| **Secrets in backups** | Treat dumps and config backups as **secret-bearing** — Storage + access control |
| **Git** | Manifest **pointers** only — not dump files |

---

## 10. Retention

**Not fixed globally.** Charter or operator policy defines:

- `retention_until` in manifest  
- Archive move to `archive\`  
- No agent-initiated delete without destructive charter  

---

## 11. Evidence

| Event | Evidence location |
|-------|-------------------|
| Backup taken | Storage `backups/` or `baselines/` + manifest |
| Restore drill | Storage `restore-tests/` + REPORT |
| Failed backup | REPORT + halt |

---

## 12. Related documents

- [STORAGE-MODEL-v1.md](STORAGE-MODEL-v1.md)  
- [CHANGE-RISK-MODEL-v1.md](CHANGE-RISK-MODEL-v1.md)  
- [SERVER-OPS-CHARTER-v1.md](SERVER-OPS-CHARTER-v1.md)  
- [projects/mars-survivability/protocols/snapshot-manifest-standard-v1.md](../mars-survivability/protocols/snapshot-manifest-standard-v1.md)  

---

*Backup & Restore Model v1 · Phase 1A · no live backups.*
