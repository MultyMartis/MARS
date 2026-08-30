# Live Intake Checklist v1 — MCA-VPN-001

**Purpose:** Read-only evidence collection for **Phase 1B-1**  
**Status:** TEMPLATE — **NOT EXECUTION AUTHORIZATION**  
**Default mode:** READ-ONLY discovery only

---

## Intake rules

1. **No mutation** during discovery unless separate change charter exists.  
2. Capture **sanitized** outputs — secrets to local/Storage only per [SECRET-HANDLING-MODEL-v1.md](../../SECRET-HANDLING-MODEL-v1.md).  
3. Populate [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md) from evidence.  
4. Produce REPORT artifact with evidence refs — not raw secret dumps in Git.

---

## Read-only evidence classes

| Class | Examples | Notes |
|-------|----------|-------|
| **Provider panel metadata** | Plan name, region, IP (may stay local), billing status | Screenshot or sanitized export |
| **OS / kernel** | `hostnamectl`, `uname -a` | READ-ONLY |
| **Resources** | `lscpu`, `free -h`, `df -h` | READ-ONLY |
| **Package inventory** | `dpkg -l` or inventory script output | Sanitize before Git |
| **Services** | `systemctl list-units`, enabled/running | READ-ONLY |
| **Listeners** | `ss -tulpn` | READ-ONLY |
| **Network / routes** | `ip addr`, `ip route` | READ-ONLY |
| **Firewall** | `ufw status`, `nft list ruleset` (read-only) | LIVE VERIFY |
| **SSH effective settings** | `sshd -T` (sanitized) | No secrets in Git |
| **fail2ban** | `systemctl status fail2ban`, jail list | READ-ONLY |
| **Docker** | `docker ps -a`, `systemctl status docker` | READ-ONLY |
| **nginx** | `nginx -v`, `systemctl status nginx`, package query | Confirm absence or presence |
| **3X-UI version** | `x-ui version` / panel about / inventory | READ-ONLY |
| **Xray version** | `x-ui log`, binary `-version` if available | READ-ONLY |
| **Sanitized x-ui settings** | `x-ui settings` — redact secrets | Local store for full output |
| **Inbound/outbound topology** | 3X-UI panel read-only export | No UUIDs/keys in Git |
| **Certificates** | `certbot certificates` or openssl dates — **not private keys** | Metadata only |
| **Certificate expiry** | notAfter dates | READ-ONLY |
| **Renewal timer/cron** | `systemctl list-timers`, crontab -l (root) | READ-ONLY |
| **Backups** | List `/root/MCA/backups/**`, sizes, dates | No archive contents in Git |
| **Archive manifests** | `tar -tf` listing (sanitized) | READ-ONLY |
| **Checksums** | SHA256 if files exist | Record in REPORT |
| **MCA tree** | `find /root/MCA` | READ-ONLY |
| **Monitoring** | cron, external probes if any | SAFE UNKNOWN until seen |
| **Disk use trends** | `df -h`, large files | READ-ONLY |
| **Recent relevant logs** | `x-ui log`, journal snippets — sanitized | No secrets |

---

## Explicitly PROHIBITED during intake

Unless separate **change charter** with operator approval:

| Prohibited action | Reason |
|-------------------|--------|
| x-ui DB `UPDATE` / `DELETE` | HIGH — production config |
| `systemctl restart` / `stop` x-ui | HIGH — VPN interruption |
| Service stop/disable (any critical) | Incident 3 lesson |
| Firewall mutation | Exposure risk |
| SSH config mutation | Lockout risk |
| Certificate renewal / replacement | Identity change |
| DNS mutation | Routing impact |
| Client deletion/addition in panel | Production impact |
| Package upgrade / dist-upgrade | Runtime change |
| `reboot` | Availability impact |

---

## Post-intake deliverables

| Deliverable | Location |
|-------------|----------|
| Updated reconciliation matrix | [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md) |
| Intake REPORT | `projects/mars-server-ops/reports/` (when chartered) |
| Secret-bearing raw exports | Local / `X:\AI MARS STORAGE\mars-server-ops\` per policy |
| Operator review checkpoint | Before any Server B research/build |

---

## Related documents

- [KNOWN-GOOD-PROCEDURES-v1.md](KNOWN-GOOD-PROCEDURES-v1.md)
- [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md) — READ-ONLY FIRST

---

*Live Intake Checklist v1 · read-only · no authorization to mutate.*
