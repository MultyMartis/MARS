# Known Good Procedures v1 — MCA-VPN-001

**Status:** HISTORICAL PROCEDURE CATALOG — **NOT EXECUTION AUTHORIZATION**  
**Rule:** Historical command success does **not** authorize future execution without scoped charter + operator approval.

Risk labels reference [CHANGE-RISK-MODEL-v1.md](../../CHANGE-RISK-MODEL-v1.md) → MARS Survivability authoritative classes.

---

## READ-ONLY (historical — intake/discovery)

| Command / action | Purpose | Risk |
|------------------|---------|------|
| `hostnamectl` | OS identity | READ-ONLY |
| `uname -a` | Kernel/build | READ-ONLY |
| `lscpu` | CPU info | READ-ONLY |
| `free -h` | Memory | READ-ONLY |
| `df -h` | Disk use | READ-ONLY |
| `ip addr` | Interfaces | READ-ONLY |
| `ip route` | Routing | READ-ONLY |
| `ss -tulpn` | Listeners | READ-ONLY |
| `ss -tlnp \| grep :22` | SSH listener check | READ-ONLY |
| `x-ui log` | 3X-UI logs (pager: Shift+G for end) | READ-ONLY |
| `x-ui settings` | Sanitized panel settings | READ-ONLY |
| `sqlite3 /etc/x-ui/x-ui.db ".tables"` | DB structure | READ-ONLY |
| `sqlite3 /etc/x-ui/x-ui.db ".schema settings"` | Settings schema | READ-ONLY |
| `tar -tf <BACKUP_FILE>` | Inspect archive contents | READ-ONLY |
| `find /root/MCA \| sort` | MCA tree listing | READ-ONLY |

---

## LOW / MEDIUM (historical helpers)

| Command / action | Purpose | Risk |
|------------------|---------|------|
| `sed -i 's/\r$//' /root/MCA/scripts/inventory.sh` | Fix CRLF on script | LOW — mutates one file |
| `bash /root/MCA/scripts/inventory.sh` | Generate inventory bundle | MEDIUM — reads system; writes files including secret-bearing dump |

**Warning:** Inventory script produced `xui-db.sql` — **SECRET-BEARING** output.

---

## HIGH (service/config impact)

| Command / action | Purpose | Risk |
|------------------|---------|------|
| `systemctl restart x-ui` | Reload 3X-UI/Xray after config change | HIGH — **service interruption**; Incident 3 context |
| Direct SQLite `UPDATE` on `settings` | Panel port/path repair | HIGH — DB mutation; backup DB first |
| Certificate replacement | TLS identity change | HIGH |
| Firewall modifications | Exposure change | HIGH |
| Network configuration changes | Connectivity change | HIGH |
| `reboot` | Full node restart | HIGH |

---

## DESTRUCTIVE (forbidden without explicit destructive charter)

| Command / action | Risk |
|------------------|------|
| `rm -rf ...` | DESTRUCTIVE |
| Restore archive over live production filesystem | DESTRUCTIVE |
| SQLite DELETE / destructive schema change | DESTRUCTIVE |
| `systemctl stop x-ui` / `disable` during diagnostics | DESTRUCTIVE on single-path VPN |
| Firewall flush / reset | DESTRUCTIVE |
| Service removals | DESTRUCTIVE |

---

## Backup procedure (proven VPN/application scope only)

**Sanitized historical pattern:**

```text
tar -czpf <BACKUP_FILE> /usr/local/x-ui /etc/xray /etc/x-ui /etc/letsencrypt /root/cert
```

**Classification:** Application/VPN backup — **NOT full-server backup**.

Inspect before trust:

```text
tar -tf <BACKUP_FILE> | head -30
```

---

## Panel recovery pattern (historical — HIGH RISK)

Conceptual steps only — **do not embed secret values:**

1. Backup `/etc/x-ui/x-ui.db` first  
2. Read `settings` keys (`webPort`, `webBasePath`)  
3. Restore known-good values from authority (local secret store)  
4. `systemctl restart x-ui`  
5. Verify panel in browser — do not expose path in Git reports  

Known-good historical port: **5928**. Base path: `<3XUI_PANEL_PATH>`.

---

## Execution disclaimer

```text
This catalog documents what worked historically.
It does NOT grant standing authorization.
Every live operation requires:
  - scoped charter
  - risk classification
  - backup/checkpoint where applicable
  - operator approval
  - READ-ONLY FIRST on production VPN
```

---

## Related documents

- [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md)
- [LIVE-INTAKE-CHECKLIST-v1.md](LIVE-INTAKE-CHECKLIST-v1.md)

---

*Known Good Procedures v1 · catalog only · not authorization.*
