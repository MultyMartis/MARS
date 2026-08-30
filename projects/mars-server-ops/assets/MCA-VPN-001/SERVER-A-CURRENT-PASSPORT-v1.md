# Server A Current Passport v1 — MCA-VPN-001

**Status:** **LIVE + SYSTEM SECURITY + PANEL EXPOSURE ACCEPTED + FINAL OPERATIONAL BACKUP 01** — intake 2026-08-25; hardening/panel 2026-08-30; preferred backup stamp `20260830T184024Z`  
**Authority:** Live observed state (intake) plus chartered hardening documented in [SECURITY-POSTURE-v1.md](SECURITY-POSTURE-v1.md), [PANEL-EXPOSURE report](../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md), [FINAL BACKUP report](../../reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md)  
**Not:** proof of bare-metal DR tested; nginx panel proxy not present

---

## Intake gate

| Gate | Result |
|------|--------|
| Phase 1B-1 read-only charter | Operator task issued 2026-08-25 |
| Local access reference | **PRESENT** — `local/infrastructure/MCA-VPN-001/secrets.local.md` |
| Live SSH session | **ESTABLISHED** (password auth, 1 attempt) |
| Verdict | **PASS WITH GAPS** |

Compare drift: [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md). Historical: [SERVER-A-LEGACY-PASSPORT-v1.md](SERVER-A-LEGACY-PASSPORT-v1.md).

---

## 1. Identity (live)

| Field | Live observed | Classification |
|-------|---------------|----------------|
| Asset ref | `MCA-VPN-001` | PRESENT |
| Provider | VEESP | **NOT CHECKED** — legacy only |
| Hostname | `wsp-cloud` | **MATCH** |
| Public domain | `wsp-cloud.com` (cert CN) | **MATCH** |
| Public IPv4 | `<SERVER_IP>` | **PRESENT** (redacted in Git) |
| OS | Ubuntu 22.04.5 LTS (Jammy) | **MATCH** |
| Kernel | 5.15.0-187-generic | **PRESENT** |
| Virtualization | KVM | **PRESENT** |
| Uptime at intake | ~7 days | **PRESENT** |
| Timezone | UTC, NTP active | **PRESENT** |
| Datacenter / tariff | — | **SAFE UNKNOWN** |

---

## 2. Resources (live)

| Resource | Live observed | Classification |
|----------|---------------|----------------|
| CPU | 1 vCPU — Intel Xeon Gold 6248 @ 2.50GHz | **MATCH** |
| RAM | 1.0 GiB total | **MATCH** |
| Swap | **`/swapfile` 1 GiB** (added 2026-08-30 hardening) | **CHANGED** vs intake |
| Disk | 20G root; ~46% used at hardening audit | **PRESENT** |
| Load (at intake) | 0.54, 0.26, 0.19 | **PRESENT** |

---

## 3. Network / listeners (live)

| Port | Process / role | Classification |
|------|----------------|----------------|
| 22/tcp | sshd | **PRESENT** |
| 5928/tcp | x-ui (panel HTTPS TLS-direct; ACCEPTED RESIDUAL) | **MATCH** |
| 2096/tcp | x-ui (subscription HTTPS; functional; UNUSED UNPROVEN dependency) | **PRESENT** |
| 8443/tcp | xray — inbound `MCA-Gate-TLS` (VLESS + TLS + RAW/TCP) | **PRESENT** |
| 46489/tcp | xray — inbound `MCA-Gate-Reality` (VLESS + Reality) | **PRESENT** |
| 8445/tcp | docker-proxy → MTProto container :443 | **PRESENT** |
| 127.0.0.1:11111, 62789 | xray internal | **PRESENT** |

IPv6: global address on eth0 — **PRESENT**.

---

## 4. Firewall (live)

| Layer | Live observed | Classification |
|-------|---------------|----------------|
| ufw | **active** (2026-08-30) — default deny in / allow out | **CHANGED** |
| Allowed public | 22, 8443, 46489, 5928 ACCEPTED RESIDUAL, 2096 sub residual, 8445 MTProto | **PRESENT** |
| nftables / iptables | Docker NAT/filter + UFW + fail2ban | **PRESENT** |
| Docker caveat | Do not claim UFW covers all Docker bypass | **RESIDUAL** |

---

## 5. SSH effective policy (live)

| Field | Live observed | Classification |
|-------|---------------|----------------|
| port | 22 | **MATCH** |
| operational account | **`marsops`** key-only + sudo | **CHANGED** |
| permitrootlogin | **without-password** (key recovery retained) | **CHANGED** |
| passwordauthentication | **no** | **CHANGED** |
| pubkeyauthentication | yes | **PRESENT** |
| Key material | LOCAL ONLY (`local/infrastructure/MCA-VPN-001/ssh/`) | **PRESENT** |

---

## 6. Security services (live)

| Service | Live observed | Classification |
|---------|---------------|----------------|
| fail2ban | active, enabled | **PRESENT** |
| ssh | active, enabled | **PRESENT** |

---

## 7. 3X-UI (live)

| Item | Live observed | Classification |
|------|---------------|----------------|
| Service status | active (running), enabled | **MATCH** |
| Binary path | `/usr/local/x-ui/x-ui` | **PRESENT** |
| Version (semver) | **3.7.0** (`/usr/local/x-ui/x-ui -v`) | **MATCH** (upgraded 2026-08-30 from 3.4.1) |
| Panel port | 5928 | **MATCH** |
| Panel protocol | HTTPS (cert paths under `/root/cert/wsp-cloud.com/`) | **MATCH** |
| webBasePath | **NON_DEFAULT** — value **redacted** / LOCAL SECRET ONLY | **PRESENT** |
| Subscription port listener | 2096 (x-ui subscription HTTPS functional; dependency **UNUSED UNPROVEN**) | **PRESENT** |

**Post-intake operational notes (2026-08-30):**  
- Admin credential rotation — **PASS** (LOCAL SECRET ONLY).  
- Official 3X-UI upgrade **3.4.1 → 3.7.0** — **PASS**; DB migration occurred; panel path/port/TLS preserved; clients unchanged (**9**).  
- **System security hardening 01** — **PASS** server-side: KEY-ONLY SSH; UFW active; fail2ban; swap; journald cap. Report: [MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md).  
- **Panel exposure hardening 01** — **PASS WITH RESIDUALS**: `:5928` ACCEPTED RESIDUAL (TLS-direct OPTION C); `:2096` left PUBLIC (UNUSED UNPROVEN); nginx migration DEFERRED; VPN mutations **0**. Report: [MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md).  
- **Final full operational backup 01** — **PASS**: preferred stamp `veesp-final-operational-20260830T184024Z`; SHA match remote/local; restore procedure CONFIRMED; bare-metal NOT EXERCISED. Report: [MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md](../../reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md).  
- Prior reports: [MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md), [MARS-SERVER-OPS-VEESP-3XUI-UPGRADE-PANEL-EXPOSURE-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-3XUI-UPGRADE-PANEL-EXPOSURE-HARDENING-01.md).

---

## 8. Xray / VPN runtime (live)

| Item | Live observed | Classification |
|------|---------------|----------------|
| Xray version | **26.7.28** | **MATCH** (managed replace during 3X-UI upgrade; was 26.6.22) |
| Binary | `/usr/local/x-ui/bin/xray-linux-amd64` | **PRESENT** |
| Inbound count | **2** (both VLESS, enabled) | **PRESENT** |
| VLESS TLS RAW inbound | id 1, port **8443**, remark `MCA-Gate-TLS`, clients **8** | **MATCH** |
| Reality inbound | id 3, port 46489, remark `MCA-Gate-Reality`, clients **1** | **MATCH** |
| Vision | Not detected in stream_settings flags | **SAFE UNKNOWN** |
| nginx in VPN path | not installed | **MATCH** (absence) |

**Transport truth:** inbound `:8443` is **VLESS + TLS + RAW/TCP**. Do not treat any historical WS wording as current architecture.

---

## 9. nginx (live)

| Item | Live observed | Classification |
|------|---------------|----------------|
| Installed | **no** | **MATCH** |
| Running | **no** | **MATCH** |
| In VPN path | **not proven / not involved** | **MATCH** |

---

## 10. Docker (live)

| Item | Live observed | Classification |
|------|---------------|----------------|
| Docker daemon | active, enabled — v29.1.3 | **PRESENT** |
| Containers | `mtproto` — `telegrammessenger/proxy:latest`, up 7 days, host 8445→443 | **PRESENT** |
| VPN path involvement | **not proven** — separate MTProto service | **PRESENT** |

---

## 11. TLS / certificates (live)

| Item | Live observed | Classification |
|------|---------------|----------------|
| `/etc/letsencrypt` | **absent** | **CHANGED** |
| Active cert path | `/root/cert/wsp-cloud.com/fullchain.pem` + privkey | **PRESENT** |
| Domain | wsp-cloud.com | **MATCH** |
| Issuer | Let's Encrypt (YE2) | **PRESENT** |
| Validity | 2026-08-13 → **2026-11-11** | **PRESENT** |
| certbot timers | none observed | **PRESENT** |
| Renewal mechanism | **SAFE UNKNOWN** | — |

---

## 12. Backups (live)

| Item | Live observed | Classification |
|------|---------------|----------------|
| **Preferred final operational** | `veesp-final-operational-20260830T184024Z.tgz` — remote `/root/mars-backups/` + local twin; SHA **MATCH**; **81065422** B | **PRESENT** (2026-08-30) |
| Historical post-hardening / pre-hardening / post-upgrade / pre-upgrade / operational / pre-cred | retained under `/root/mars-backups/` + local `MCA-VPN-001\backups` | **PRESENT** — historical rollback only |
| `/root/MCA/backups/vpn/3xui_full_backup.tar.gz` | ~65.5 MB | **PRESENT** (historical Class A) |
| `/root/MCA/backups/server/mca-gate-full-2026-06-27-1845.tar.gz` | ~79.6 MB | **PRESENT** (NOT full-server) |
| Bare-metal DR | **NOT YET EXERCISED** | — |
| Detail | [BACKUP-STATE-v1.md](BACKUP-STATE-v1.md) · restore [VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md) | — |

---

## 13. MCA tree (live)

| Path | Live observed | Classification |
|------|---------------|----------------|
| `/root/MCA/` | backups, docs, inventory, recovery, scripts, secrets | **MATCH** |
| `/root/MCA/inventory/` | machine inventory outputs (incl. xui-db.sql — not opened) | **PRESENT** |
| `/root/mtproto_backup.json` | exists, 7392 bytes, mtime 2026-04-17 | **PRESENT** (contents not read) |

---

## 14. Monitoring (live)

| Item | Live observed | Classification |
|------|---------------|----------------|
| Dedicated monitoring service | not identified | **SAFE UNKNOWN** |
| fail2ban | active on SSH | **PRESENT** |
| MTProto | Docker container running | **PRESENT** |

---

## 15. Legacy vs live summary

| Area | Verdict |
|------|---------|
| Core identity (hostname, OS, sizing) | **MATCH** |
| Xray version | **MATCH** |
| Panel port 5928 | **MATCH** |
| nginx absent from VPN path | **MATCH** |
| `/etc/letsencrypt` | **CHANGED** (absent live) |
| Backup root path for 3xui archive | **CHANGED** |
| Docker + MTProto on VPN host | **PRESENT** (new live evidence) |
| WebSocket on TLS inbound | **CHANGED** vs legacy Server A topology doc |
| 3X-UI semver | **MATCH** (**3.7.0**) |
| Full DR | **NOT TESTED** (unchanged) |

---

## 16. Related documents

- [SERVER-A-LEGACY-PASSPORT-v1.md](SERVER-A-LEGACY-PASSPORT-v1.md)  
- [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md)  
- [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md)  
- [BACKUP-STATE-v1.md](BACKUP-STATE-v1.md)  
- [SECURITY-POSTURE-v1.md](SECURITY-POSTURE-v1.md)  
- Credential rotation closeout: [../../reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md)

---

*Server A Current Passport v1 · live intake 2026-08-25 · admin rotation + 3X-UI 3.7.0 + system security hardening 2026-08-30 · transport truth `:8443` = VLESS TLS RAW · panel exposure residual NEXT WAVE.*
