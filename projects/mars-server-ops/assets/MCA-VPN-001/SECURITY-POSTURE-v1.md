# Security Posture v1 — MCA-VPN-001 (VEESP)

**Status:** **SYSTEM SECURITY HARDENING 01 APPLIED** + **PANEL EXPOSURE HARDENING 01 DECISION** (2026-08-30)  
**Not:** claim that panel/subscription ports are closed, or that Docker published ports are fully mediated by UFW.  
**Reports:** [../../reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md) · [../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md)

---

## 1. Administration path

| Item | Value |
|------|-------|
| Independent admin egress | FriendHosting **`92.42.99.126`** |
| VEESP used as control plane egress | **NO** (required gate) |
| FriendHosting mutation in this wave | **0** |

---

## 2. SSH model

| Item | Value |
|------|-------|
| Port | **22** (unchanged — no theatre port move) |
| Operational account | **`marsops`** (sudo group; password-confirmed sudo, not NOPASSWD) |
| Operational login | **key-only** (ed25519; local secret contour) |
| Root remote login | **`PermitRootLogin without-password`** (key recovery retained) |
| PasswordAuthentication | **no** |
| KbdInteractiveAuthentication | **no** |
| PubkeyAuthentication | **yes** |
| Drop-in | `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` |
| Private keys | **LOCAL ONLY** under `X:\AI MARS\local\infrastructure\MCA-VPN-001\ssh\` — never Git |

---

## 3. Host firewall (UFW)

| Item | Value |
|------|-------|
| UFW | **active** |
| Default | deny incoming / allow outgoing / deny routed |
| Intended public allows | **22**, **8443** (VLESS TLS RAW), **46489** (Reality), **5928** (panel ACCEPTED RESIDUAL), **2096** (sub residual; UNUSED UNPROVEN), **8445** (MTProto docker-proxy) |
| `:80`/`:443` | **not** opened (nginx ABSENT; host `:443` unused; nginx migration DEFERRED) |

**Rollback:** `ufw --force disable` from an already-open recovery session.

---

## 4. Docker / iptables caveat

| Item | Value |
|------|-------|
| Docker | present; MTProto published via **docker-proxy** `:8445` |
| Claim | Do **not** assert “UFW ACTIVE = all Docker ports protected” |
| Classification | **RESIDUAL** — Docker NAT/FORWARD interaction remains a documentation caveat |

---

## 5. fail2ban / swap / logging

| Item | Value |
|------|-------|
| fail2ban | **active**; **sshd** jail loaded (port 22); `3x-ipl` may coexist |
| Swap | **`/swapfile` 1 GiB**; mode `600`; fstab persisted |
| journald | drop-in **`SystemMaxUse=300M`** / **`RuntimeMaxUse=100M`** |

---

## 6. Panel exposure residual (PANEL EXPOSURE HARDENING 01)

| Port | State |
|------|-------|
| `:5928` | **ACCEPTED RESIDUAL** — PUBLIC TLS-direct 3X-UI admin (OPTION C) |
| `:2096` | **PUBLIC** — subscription HTTPS functional; device dependency **UNUSED UNPROVEN** (left open) |
| nginx | **ABSENT**; host `:443` unused; nginx migration **DEFERRED** |

**Report:** [../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md](../../reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md)

---

## 7. Update / reboot posture

| Item | Value |
|------|-------|
| Pending apt upgrades | present (recorded; **not** broadly installed in this wave) |
| Reboot required | **YES** (`/var/run/reboot-required`) — **reboot NOT performed** |

---

## 8. Related

- [SERVER-A-CURRENT-PASSPORT-v1.md](SERVER-A-CURRENT-PASSPORT-v1.md)  
- [BACKUP-STATE-v1.md](BACKUP-STATE-v1.md)  
- [../../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md](../../runbooks/VEESP-MCA-VPN-001-OPERATIONAL-RESTORE-v1.md)

---

*Security posture · MCA-VPN-001 · 2026-08-30 · no secrets.*
