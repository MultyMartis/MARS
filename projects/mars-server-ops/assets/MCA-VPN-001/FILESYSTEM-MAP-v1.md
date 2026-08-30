# Filesystem Map v1 — MCA-VPN-001

**Status:** **LIVE RECONCILIATION 2026-08-25** — live verification column populated from read-only intake  
**Purpose:** Known paths, sensitivity, and backup relevance

**Evidence:** [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md)

---

## Path catalog

| Path | Purpose | Legacy state | Backup relevance | Secret sensitivity | Live verification (2026-08-25) |
|------|---------|--------------|------------------|-------------------|-------------------------------|
| `/usr/local/x-ui` | 3X-UI runtime / binaries / Xray assets | CONFIRMED | YES | Possible adjacency | **PRESENT** |
| `/usr/local/x-ui/x-ui` | 3X-UI binary | CONFIRMED | YES | Low direct | **PRESENT** (mtime 2026-06-25) |
| `/usr/local/x-ui/bin` | Xray/runtime binaries | CONFIRMED | Useful | Possible config adjacency | **PRESENT** |
| `/etc/x-ui` | 3X-UI persistent data | CONFIRMED | YES | **YES** | **PRESENT** |
| `/etc/x-ui/x-ui.db` | Main SQLite DB | CONFIRMED | **CRITICAL** | **SECRET-BEARING** | **PRESENT** — read-only `.tables` / settings only |
| `/etc/xray` | Xray-related configuration | CONFIRMED | YES | **YES possible** | **PRESENT** |
| `/etc/letsencrypt` | Let's Encrypt certificates/state | CONFIRMED | YES | **YES** (private keys) | **ABSENT** — **CHANGED** |
| `/root/cert` | Certificate material | CONFIRMED | YES | **YES** | **PRESENT** — LE cert expires 2026-11-11 |
| `/root/MCA` | MCA operational structure | CONFIRMED | YES | Mixed | **PRESENT** |
| `/root/MCA/backups/vpn` | VPN backups directory | CONFIRMED | YES / off-server | **YES** | **PRESENT** — `3xui_full_backup.tar.gz` ~65.5 MB |
| `/root/MCA/backups/server` | Intended server backup area | CONFIRMED dir | YES | **YES** | **PRESENT** — `mca-gate-full-2026-06-27-1845.tar.gz` ~79.6 MB |
| `/root/MCA/docs` | On-server documentation | CONFIRMED | YES | Normally no | **PRESENT** |
| `/root/MCA/inventory` | Machine inventory outputs | CONFIRMED | YES | May contain secrets | **PRESENT** — `xui-db.sql` **NOT OPENED** |
| `/root/MCA/inventory/xui-db.sql` | SQLite dump | CONFIRMED | **CRITICAL** | **SECRET-BEARING** | **PRESENT** — contents **NOT OPENED** |
| `/root/MCA/scripts` | Helper scripts | CONFIRMED | YES | Review | **PRESENT** |
| `/root/MCA/secrets` | Intended secret documentation area | PLANNED/likely | YES encrypted/off-server | **YES** | **NOT CHECKED** |
| `/root/mca-backups` | Former backup location | SUPERSEDED | Historical | **YES** | **NOT CHECKED** |
| `/root/3xui_full_backup.tar.gz` | Historical backup before move | CONFIRMED HISTORICAL | Critical historical | **SECRET-BEARING** | **ABSENT** — migrated to MCA path |
| `/root/backup_3xui` | Historical unpacked/working backup | CONFIRMED HISTORICAL | Potentially | **YES** | **NOT CHECKED** |
| `/root/xui-repair-backup` | Temporary repair backup | Deletion approved | No after replacement | **YES** | **ABSENT** |
| `/root/docker_list.txt` | Historical inventory artifact | CONFIRMED HISTORICAL | Optional | Low | **NOT CHECKED** |
| `/root/mtproto_backup.json` | MTProto-related backup artifact | CONFIRMED HISTORICAL | Unknown | Likely **YES** | **PRESENT** — metadata only; contents **NOT OPENED** |

---

## Sensitivity summary

### SECRET-BEARING (never in Git)

- `/etc/x-ui/x-ui.db`
- `/root/MCA/inventory/xui-db.sql`
- Certificate private key material under `/root/cert` (and historical `/etc/letsencrypt` if restored from archive)
- VPN backup archives (`*.tar.gz`)
- `/root/MCA/secrets/` if populated
- `/root/mtproto_backup.json` — treat as secret-bearing; do not open in Git workflows

### Forensic / semantic notes

1. **`/usr/local/x-ui/web`** — absence was **normal** in historical working backup; not root cause of panel 404.  
2. **`backups/server/`** placement of `mca-gate-full-*` is **misleading** — not proof of full-server scope.  
3. **`/etc/letsencrypt` absent on live FS** — certificates appear to live under `/root/cert/wsp-cloud.com/`; archive may still contain historical letsencrypt tree.

---

## Related documents

- [BACKUP-STATE-v1.md](BACKUP-STATE-v1.md)
- [RECOVERY-STATE-v1.md](RECOVERY-STATE-v1.md)
- [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md)

---

*Filesystem Map v1 · live verification 2026-08-25 · secret paths not opened.*
