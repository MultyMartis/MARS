# Server B Controlled Reboot v1

**Status:** **COMPLETE** — 2026-08-25  
**Wave:** MARS Server Ops Phase 3E  
**Verdict:** **PASS**  
**Planning locus:** `SERVER-B-PLANNING`  
**Not:** kernel meta-package upgrade, NTP architecture change, DNS mutation, 3X-UI / Xray / nginx / Docker, or Server A work

---

## 1. Purpose

Apply the single Ubuntu package-update reboot deferred from Phase 3D (`libc6` / `apparmor` / `dbus`) and prove MARS `marsops` key SSH, sudo, and host security services survive reboot.

---

## 2. Authorization checklist (pre-reboot)

| Check | Result |
|-------|--------|
| `marsops` Ed25519 key local | **YES** — `local/infrastructure/SERVER-B-PLANNING/ssh/marsops_ed25519` |
| sudo credential local | **YES** — local secret contour |
| Provider recovery console | **DOCUMENTED fallback** — not live-opened this wave |
| Server A | **UNTOUCHED** |
| Production traffic on Server B | **NONE** (application stack absent) |
| Application stack | **ABSENT** |
| Reboot method | one `sudo reboot` (not provider power-cycle) |
| Multiple reboot commands | **NOT ISSUED** |

---

## 3. Pre-reboot access safety

| Check | Result |
|-------|--------|
| Session A `whoami` | `marsops` |
| Session B `whoami` | `marsops` |
| Hostname | `metacode-cloud.com` |
| sudo (both sessions) | **PASS** (`uid=0`) |
| `ssh` / `ssh.socket` | active |
| UFW | active |
| fail2ban | active |
| sshd jail | active |
| Root remote SSH | not used |
| SSH config mutation | **NONE** |

Access was stable. Reboot proceeded.

---

## 4. Pre-reboot snapshot

| Field | Value |
|-------|-------|
| Kernel | `6.8.0-36-generic` |
| OS | Ubuntu 24.04.4 LTS |
| Uptime | ~1h56m |
| `/var/run/reboot-required` | **YES** — pkgs: `libc6`, `apparmor`, `dbus` |
| Public TCP listener | 22/tcp (`sshd`) |
| DHCP client | UDP/68 (`systemd-networkd`) |

Effective `sshd -T` (unchanged intent):

| Directive | Value |
|-----------|-------|
| `Port` | 22 |
| `PermitRootLogin` | no |
| `PasswordAuthentication` | no |
| `KbdInteractiveAuthentication` | no |
| `PubkeyAuthentication` | yes |
| `MaxAuthTries` | 3 |
| `sshd -t` | **PASS** |

---

## 5. Reboot execution

| Item | Value |
|------|-------|
| Command | `sudo reboot` (single) |
| Operator | `marsops` |
| Provider panel power-cycle | **NOT USED** |
| First conservative wait | ~25 s |
| SSH recovery | **PASS** — ~32 s after reboot issue |
| Boot time (`uptime -s`) | `2026-08-25 16:15:34` UTC |
| Retry window consumed | well under 5 minutes |
| Provider console | **NOT INVOKED** |

---

## 6. Post-reboot access gate

| Check | Result |
|-------|--------|
| Fresh session A | `marsops` / `metacode-cloud.com` / sudo **PASS** |
| Independent session B | `marsops` / `metacode-cloud.com` / sudo **PASS** |
| `sshd -T` expected directives | **MATCH** |
| `sshd -t` | **PASS** |
| Password SSH `root` | **REJECTED** (`BadAuthenticationType`; allowed: `publickey`) |
| Password SSH `marsops` | **REJECTED** (`BadAuthenticationType`; allowed: `publickey`) |

Ubuntu 24.04 socket activation: `ssh.socket` **enabled + active**; `ssh.service` unit-file may show `disabled` while `sshd` is running. This is expected generator behaviour, not an SSH outage.

---

## 7. Post-reboot security services

| Control | Result |
|---------|--------|
| SSH | **active** |
| UFW | **active** — deny in / allow out; **22/tcp only** |
| fail2ban | **active** |
| sshd jail | **active** (0 banned) |
| Firewall loosened | **NO** |
| VPN/application ports opened | **NO** |

---

## 8. Kernel / package state after reboot

| Item | Result |
|------|--------|
| Running kernel | still `6.8.0-36-generic` |
| Newer kernel active? | **NO** — linux meta packages remain kept back |
| `/var/run/reboot-required` | **CLEARED** (`REBOOT_REQUIRED_NO`) |

Remaining `apt` upgradable (not installed this phase):

| Package | Pocket | Class |
|---------|--------|-------|
| `linux-generic` / `linux-image-generic` / `linux-headers-generic` 6.8.0-138 | noble-updates + **noble-security** | **SECURITY RELEVANT** — kept back / not auto-installed |
| `byobu` | noble-updates | **PHASED / NORMAL** |
| `fwupd` | noble-updates | **PHASED / NORMAL** |
| `sosreport` | noble-updates | **PHASED / NORMAL** |
| `ubuntu-server-minimal` | noble-updates | **PHASED / NORMAL** |

---

## 9. Explicit non-actions

| Surface | State |
|---------|-------|
| SSH hardening drop-in | **PRESERVED** |
| UFW / fail2ban policy | **UNCHANGED** |
| Kernel meta install | **NOT DONE** |
| chrony / ntpd install | **NOT DONE** |
| timesyncd restart loop | **NOT DONE** |
| 3X-UI / Xray / nginx / Docker | **ABSENT** |
| DNS / TLS | **NONE** |
| Server A | **UNTOUCHED** |
| Provider panel | **UNTOUCHED** |

---

*Phase 3E controlled reboot · PASS · no secrets in Git.*
