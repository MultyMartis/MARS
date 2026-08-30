# Live Intake Evidence v1 — MCA-VPN-001

**Intake session:** 2026-08-25  
**Mode:** Ultra-safe read-only (chartered)  
**Operator asset:** Server A — production VPN (`MCA-VPN-001`)  
**Outcome:** **PASS WITH GAPS** — read-only live collection completed; operator review required before mutation

---

## 1. Session preflight (local — completed)

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| X: volume label | **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Staged changes | **empty** |
| Foreign WIP | Present elsewhere in repo — **not staged, not touched** |
| Legacy asset docs read | YES — full MCA-VPN-001 pack + programme charter |

---

## 2. Access reference (local — success)

| Expected reference | Result |
|--------------------|--------|
| `X:\AI MARS\local\infrastructure\MCA-VPN-001\secrets.local.md` | **PRESENT** (local-only; not in Git) |
| Required SSH fields (`host`, `port`, `user`, `auth_type`) | **COMPLETE** |
| Auth method used | **password** (1 attempt; success) |
| Private key path in secrets | Referenced but key file not found locally — not used |

**Programme rule applied:** credentials never printed, echoed, or committed.

---

## 3. SSH session

| Observation | Classification |
|-------------|----------------|
| SSH authentication | **SUCCESS** (single controlled session) |
| Session method | Python paramiko (OpenSSH/sshpass unavailable on operator workstation) |
| Authentication attempts | **1** (within charter limit of 2) |
| Server-side mutation from session | **NONE** |

**Public IP:** captured during intake; represented as `<SERVER_IP>` in all Git documentation.

---

## 4. Collection passes — execution status

All passes executed **sequentially** (low-load rule). Raw operator-side capture was used for evidence synthesis only — **not committed to Git**.

| Pass | Topic | Status |
|------|-------|--------|
| 1 | Server identity | **CHECKED** |
| 2 | Resources | **CHECKED** |
| 3 | Network / listeners | **CHECKED** |
| 4 | Firewall | **CHECKED** |
| 5 | SSH effective config | **CHECKED** |
| 6 | Services | **CHECKED** |
| 7 | 3X-UI | **CHECKED** (semver gap — see gaps) |
| 8 | SQLite | **CHECKED** (read-only; no dump) |
| 9 | Xray | **CHECKED** |
| 10 | nginx | **CHECKED** — not installed |
| 11 | Docker | **CHECKED** — MTProto container only |
| 12 | TLS / certificates | **CHECKED** (metadata only) |
| 13 | Backups | **CHECKED** (listing/stat; no extract) |
| 14 | MCA inventory tree | **CHECKED** |
| 15 | MTProto | **CHECKED** (metadata only) |
| Logs | Bounded journal tail (x-ui unit) | **CHECKED** |

---

## 5. Key live findings (sanitized summary)

| Area | Live fact | Notes |
|------|-----------|-------|
| Hostname | `wsp-cloud` | MATCH legacy |
| OS | Ubuntu 22.04.5 LTS, kernel 5.15.0-187-generic | MATCH legacy |
| Uptime at intake | ~7 days (2026-08-24 20:13 UTC) | — |
| CPU / RAM / disk | 1 vCPU; 1.0 GiB RAM; 20G disk 42% used | MATCH legacy sizing |
| Listeners | 22, 5928, 2096, 8443, 46489, 8445 (+ xray localhost) | See passport |
| ufw | **inactive** | PRESENT (new evidence) |
| fail2ban | **active** on SSH | PRESENT |
| SSH | root login + password auth **enabled** | SECURITY RISK signal |
| x-ui service | active, enabled | MATCH |
| Xray | **26.6.22** | MATCH legacy |
| 3X-UI semver | **NOT OBTAINED** via CLI | SAFE UNKNOWN |
| Inbounds | 2 — VLESS TLS/WS (8443), VLESS Reality (46489) | MATCH direction |
| nginx | **not installed** | MATCH legacy absence |
| Docker | MTProto proxy container on 8445 | CHANGED (new live evidence) |
| `/etc/letsencrypt` | **absent** | CHANGED vs legacy |
| Certs | `/root/cert/wsp-cloud.com/` LE cert, expires **2026-11-11** | PRESENT |
| MCA tree | `/root/MCA/` present with backups | MATCH |
| VPN backup | `/root/MCA/backups/vpn/3xui_full_backup.tar.gz` ~65.5 MB | CHANGED location vs `/root/` |
| Server backup archive | `mca-gate-full-2026-06-27-1845.tar.gz` ~79.6 MB | PRESENT |
| webBasePath | **PRESENT** in DB (value redacted) | Legacy match **SAFE UNKNOWN** |

---

## 6. Gaps and not checked

| Item | Classification |
|------|----------------|
| 3X-UI exact semver | **SAFE UNKNOWN** — `x-ui version` shows menu only; binary mtime 2026-06-25 |
| webBasePath vs legacy `<3XUI_PANEL_PATH>` | **SAFE UNKNOWN** — value not compared in Git |
| Provider tariff / datacenter | **NOT CHECKED** |
| Backup archive contents (`tar -tf`) | **NOT CHECKED** this session |
| Backup checksum verification | **NOT CHECKED** |
| TCP Vision on Reality inbound | **SAFE UNKNOWN** — stream_settings show Reality yes, Vision no |
| Full DR restore test | **NOT TESTED** (unchanged) |
| `/root/MCA/inventory/xui-db.sql` | **NOT OPENED** (secret-bearing) |

---

## 7. Server safety attestation (mandatory)

| Mutation class | Result |
|----------------|--------|
| Server files created | **NONE** |
| Server files modified | **NONE** |
| Packages changed | **NONE** |
| Services restarted | **NONE** |
| Services reloaded | **NONE** |
| Services stopped | **NONE** |
| Services started | **NONE** |
| Firewall changed | **NONE** |
| SSH changed | **NONE** |
| x-ui changed | **NONE** |
| Xray changed | **NONE** |
| SQLite writes | **NONE** |
| Certificates changed | **NONE** |
| Backups created | **NONE** |
| Archives extracted | **NONE** |
| Docker changed | **NONE** |
| DNS changed | **NONE** |
| Reboot | **NONE** |

---

## 8. Related documents

- [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md) — populated live columns  
- [SERVER-A-CURRENT-PASSPORT-v1.md](SERVER-A-CURRENT-PASSPORT-v1.md) — live passport  
- [LIVE-INTAKE-CHECKLIST-v1.md](LIVE-INTAKE-CHECKLIST-v1.md)

---

*Live Intake Evidence v1 · read-only intake 2026-08-25 · zero server mutations.*
