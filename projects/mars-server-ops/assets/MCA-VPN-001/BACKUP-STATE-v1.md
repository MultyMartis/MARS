# Backup State v1 — MCA-VPN-001

**Status:** **PREFERRED CURRENT FINAL OPERATIONAL BACKUP VERIFIED 2026-08-30** (`veesp-final-operational-20260830T184024Z`) — remote+local twin; SHA match. Captures post–3.7.0 upgrade, credential rotation, KEY-ONLY SSH, UFW, fail2ban, swap, journald, and ACCEPTED panel residuals (`:5928` / `:2096`). Older twins remain **historical rollback points** (not deleted). Bare-metal NOT EXERCISED.  
**Critical:** Historical `mca-gate-full-*` archives are **NOT** full-server backups. Application/x-ui archives must restore **matching** binary+DB pairs after the 3.7.0 schema migration. Older stamps may restore pre-UFW / pre-KEY-ONLY / older 3X-UI/Xray / pre-rotation credentials.

**Evidence:** [../../reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md](../../reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md) · [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md) · [../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md) · [../../reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md)

---

## 0final. Preferred current final operational backup (POST FULL HARDENING BASELINE)

| Field | Value |
|-------|-------|
| Archive | `veesp-final-operational-20260830T184024Z.tgz` |
| Stamp | `20260830T184024Z` |
| Remote | `/root/mars-backups/veesp-final-operational-20260830T184024Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-final-operational-20260830T184024Z.tgz` |
| Size | **81065422** bytes (**77.310011** MiB / **0.075498** GiB) |
| SHA-256 | `b15631b7d1519fbd8364b73541fbf6e240f5e1032b0b44ef49fc34725bc80cec` |
| Remote/local | **MATCH** |
| Members | **333** |
| Live stack at capture | KEY-ONLY SSH (`marsops` + root recovery); UFW **active**; fail2ban; swap **1 GiB**; journald `SystemMaxUse=300M`; 3X-UI **3.7.0**; Xray **26.7.28**; VLESS+TLS+RAW `:8443` (8 clients); Reality `:46489` (1); panel `:5928` PUBLIC TLS-DIRECT ACCEPTED RESIDUAL; `:2096` PUBLIC UNUSED UNPROVEN; nginx ABSENT; reboot-required flag present (**not** rebooted) |
| Use | **Preferred** restore baseline for current accepted VEESP operational state |
| Bare-metal restore | **NOT YET EXERCISED** |

---

## 0sec. Historical post–system-security snapshot (SUPERSEDED as preferred)

| Field | Value |
|-------|-------|
| Archive | `veesp-post-system-hardening-20260830T163612Z.tgz` |
| Stamp | `20260830T163612Z` |
| Remote | `/root/mars-backups/veesp-post-system-hardening-20260830T163612Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-post-system-hardening-20260830T163612Z.tgz` |
| Size | **81048677** bytes |
| SHA-256 | `1857afff8dbc087540b252394438115a9babb1b42c212c03137c4d41e7d920d7` |
| Remote/local | **MATCH** |
| Live stack at capture | KEY-ONLY SSH (`marsops` + root recovery); UFW **active**; fail2ban sshd; swap **1 GiB**; journald cap; 3X-UI **3.7.0**; Xray **26.7.28**; VLESS+TLS+RAW `:8443`; panel `:5928`/`:2096` PUBLIC TEMPORARY |
| Use | Historical rollback twin — prefer `20260830T184024Z` for current baseline |
| Bare-metal restore | **NOT YET EXERCISED** |

### 0sec-pre. Pre-hardening rollback twin

| Field | Value |
|-------|-------|
| Archive | `veesp-pre-system-hardening-20260830T162532Z.tgz` |
| Stamp | `20260830T162532Z` |
| Remote | `/root/mars-backups/veesp-pre-system-hardening-20260830T162532Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-pre-system-hardening-20260830T162532Z.tgz` |
| Size | **81015066** bytes |
| SHA-256 | `ec201264ef9ef0062ec19fa67c3c7bb56c6522b803c6ed1842c77e6ef497b7a7` |
| Remote/local | **MATCH** |
| Live stack at capture | Password SSH still enabled; UFW inactive; pre-`marsops` account model |
| Use | Rollback of SSH/firewall wave only if post-hardening path fails |

---

## 0. Preferred current x-ui snapshot (POST-UPGRADE 3.7.0)

| Field | Value |
|-------|-------|
| Archive | `veesp-xui-postupgrade-20260830T155842Z.tgz` |
| Stamp | `20260830T155842Z` |
| Remote | `/root/mars-backups/veesp-xui-postupgrade-20260830T155842Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-xui-postupgrade-20260830T155842Z.tgz` |
| Size | **80876064** bytes |
| SHA-256 | `97ee0394a308f827b9798d748c86f740ec8b2501a0c60712c7927913db5389d0` |
| Remote/local | **MATCH** |
| Live stack at capture | 3X-UI **3.7.0**; Xray **26.7.28**; VLESS+TLS+RAW `:8443`; rotated admin DB; PUBLIC TLS-DIRECT panel `:5928`; nginx ABSENT |
| Use | Preferred restore for **current** panel/VPN application state after upgrade |
| Bare-metal restore | **NOT YET EXERCISED** |

---

## 0pre. Pre-upgrade rollback twin (3.4.1)

| Field | Value |
|-------|-------|
| Archive | `veesp-xui-preupgrade-20260830T154548Z.tgz` |
| Stamp | `20260830T154548Z` |
| Remote | `/root/mars-backups/veesp-xui-preupgrade-20260830T154548Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-xui-preupgrade-20260830T154548Z.tgz` |
| Size | **83815970** bytes |
| SHA-256 | `ae78f5ef548bdbcea0677c259d949698ae66941a5ebe8b95f3b6e9e11b5aac5b` |
| Remote/local | **MATCH** |
| Live stack at capture | 3X-UI **3.4.1**; Xray **26.6.22**; rotated admin credentials already in DB |
| Compatibility | Restore **matching** `/usr/local/x-ui` + `/etc/x-ui` from **this** archive only — do not mix with post-upgrade DB |

---

## 0ops. Broader operational backup (DUAL-LOCAL-BACKUP-01)

| Field | Value |
|-------|-------|
| Archive | `veesp-operational-20260830T132309Z.tgz` |
| Stamp | `20260830T132309Z` |
| Remote | `/root/mars-backups/veesp-operational-20260830T132309Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-operational-20260830T132309Z.tgz` |
| Size | **83967532** bytes |
| SHA-256 | `d10b67cb1b8a9e0beb4a131a583eee1af56cb153e4513d1e599f6e8bba9112c8` |
| Remote/local | **MATCH** |
| Live stack at capture | VLESS + TLS + RAW/TCP `:8443`; Xray **26.6.22**; Ubuntu 22.04.5; nginx ABSENT; certs under `/root/cert/wsp-cloud.com/` |
| Restore procedure | **CONFIRMED** — [../../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md) |
| Classification | Scoped **operational** VPN/panel/TLS/SSH/security inventory — **not** full filesystem |

Restoring this stamp after 2026-08-30 **reverts** to Xray 26.6.22-era binaries **and** **pre-rotation** panel credentials.

---

## 0a. Scoped pre-credential snapshot (ADMIN ACCESS HARDENING 01)

Taken immediately before 3X-UI username/password rotation.

| Field | Value |
|-------|-------|
| Archive | `veesp-xui-precred-20260830T141517Z.tgz` |
| Stamp | `20260830T141517Z` |
| Remote | `/root/mars-backups/veesp-xui-precred-20260830T141517Z.tgz` |
| Local twin | `X:\AI MARS\local\infrastructure\MCA-VPN-001\backups\veesp-xui-precred-20260830T141517Z.tgz` |
| Size | **516851** bytes |
| SHA-256 | `ce6134f4b7eed075571323a2d7cbfede0bc192967b81464929ab11c27463c3b3` |
| Remote/local | **MATCH** |
| Scope | `/etc/x-ui/` (includes `x-ui.db`) — **not** a full operational backup |
| Use | Credential/panel-DB rollback only |
| Related wave | [../../reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md) |

Live panel credentials: **LOCAL SECRET ONLY** (`X:\AI MARS\local\infrastructure\MCA-VPN-001\secrets.local.md`).

---

## 1. Backup classification key

| Class | Meaning |
|-------|---------|
| **A — Historical early archive** | Pre-incident / long-lived `3xui_full_backup.tar.gz` |
| **B — Post-recovery VPN/app archive** | ~`mca-gate-full-2026-06-27-1845.tar.gz` |
| **Full server backup** | Entire Ubuntu filesystem — **NOT CONFIRMED** |

---

## 2. Archive A — Historical `3xui_full_backup.tar.gz`

| Field | Value |
|-------|-------|
| **Name** | `3xui_full_backup.tar.gz` |
| **Status** | CONFIRMED HISTORICAL — existed; intentionally preserved |
| **Forensic value** | Proved absence of `/usr/local/x-ui/web` in working-era backup — disproved false panel hypothesis |
| **Final location (after migration)** | **`/root/MCA/backups/vpn/3xui_full_backup.tar.gz`** — **LIVE PRESENT** (~65.5 MB, mtime 2026-06-27) |
| **Legacy root path** | `/root/3xui_full_backup.tar.gz` — **LIVE ABSENT** (migrated) |
| **Scope** | VPN/3X-UI related — treat as **application backup**, not bare metal |

---

## 3. Archive B — `mca-gate-full-2026-06-27-1845.tar.gz` (approximate)

### Creation context

Created **after** successful panel recovery from known-good state.

**Sanitized creation pattern (historical):**

```text
tar ... /usr/local/x-ui /etc/xray /etc/x-ui /etc/letsencrypt /root/cert
```

### Confirmed scope (contents)

| Path | In scope |
|------|----------|
| `/usr/local/x-ui` | YES |
| `/etc/xray` | YES |
| `/etc/x-ui` | YES |
| `/etc/letsencrypt` | YES (historical archive scope) | **LIVE ABSENT on filesystem** — cert material under `/root/cert/` only |
| `/root/cert` | YES |

### Observed size

~**80 MB** (historical observation) — **LIVE:** ~**79.6 MB** at `/root/MCA/backups/server/mca-gate-full-2026-06-27-1845.tar.gz` (**PRESENT**)

---

## 4. PROMINENT CLASSIFICATION

```text
NOT A FULL SERVER BACKUP
```

Despite filename and placement under `/root/MCA/backups/server/`, this archive:

- Does **not** prove backup of full Ubuntu filesystem
- Does **not** prove packages, users, firewall, systemd, networking, cron, or OS-level state
- Must **not** be treated as bare-server or disaster-recovery-complete archive based on name or directory alone

**Archive filename/location does not prove backup scope.**

---

## 5. MCA backup layout (legacy)

```
/root/MCA/
├── backups/
│   ├── vpn/          ← 3xui_full_backup.tar.gz migrated here
│   └── server/       ← mca-gate-full-* moved here (semantic mismatch)
├── docs/
├── inventory/
├── recovery/
└── scripts/
```

**Semantic problem:** `mca-gate-full-*.tar.gz` under `backups/server/` suggests "server backup" but contents are VPN/application paths only.

### Other backup-related paths

| Path | Role |
|------|------|
| `/root/mca-backups/` | Former location — SUPERSEDED by `/root/MCA/` |
| `/root/backup_3xui/` | Historical unpacked/working backup |
| `/root/xui-repair-backup/` | Temporary repair backup — deletion approved | **LIVE ABSENT** |

---

## 6. Local / off-server copy state

| Item | Legacy assessment |
|------|-------------------|
| WinSCP/SFTP download planned | CONFIRMED HISTORICAL |
| Local copy likely exists | MEDIUM confidence — workflow indicates intent |
| Checksum-confirmed current local copy | **NOT PROVEN** |
| SHA256 workflow | Discussed — **NOT PROVEN implemented** |
| Backup encryption | **NOT PROVEN** |

---

## 7. Full server backup — discussed but not proven

A true filesystem-wide archive was **discussed** (excluding `/proc`, `/sys`, etc.) but **no successful creation/verification** appears in accessible history.

**FULL SERVER BACKUP = NOT CONFIRMED**

---

## 8. Future requirements (Server Ops policy — not claimed as existing)

Per programme backup discipline:

| Requirement | Current on Server A (2026-08-30) |
|-------------|----------------------------------|
| Manifest | Present inside `veesp-operational-20260830T132309Z` (operational) |
| Explicit scope documentation | Yes — dual-wave report + restore runbook |
| Timestamp in filename | Yes |
| Checksum (SHA256) | **VERIFIED** remote+local for `20260830T132309Z` |
| Sensitivity classification | Secret-bearing — local-only twins |
| Off-server copy | **VERIFIED** local twin under `MCA-VPN-001\backups` |
| Restore strategy | **CONFIRMED** written procedure |
| Restore test (bare-metal) | **NOT TESTED** |

Historical Class A/B archives: checksum/off-server verification remains as previously documented (not re-proven in this wave).

---

## 9. Secret-bearing backup artifacts

Treat as **SECRET-BEARING** — never commit to Git:

- `/etc/x-ui/x-ui.db`
- `/root/MCA/inventory/xui-db.sql`
- Certificate private keys under `/etc/letsencrypt`, `/root/cert`
- All `.tar.gz` VPN backup archives

---

## Related documents

- [RECOVERY-STATE-v1.md](RECOVERY-STATE-v1.md)
- [FILESYSTEM-MAP-v1.md](FILESYSTEM-MAP-v1.md)
- [BACKUP-RESTORE-MODEL-v1.md](../../BACKUP-RESTORE-MODEL-v1.md)

---

*Backup State v1 · current operational twin `20260830T132309Z` · historical Class A/B notes retained · mca-gate-full is NOT full-server backup.*
