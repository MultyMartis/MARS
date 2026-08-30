# Server B Base OS Security v1

**Status:** **COMPLETE** — 2026-08-25  
**Wave:** MARS Server Ops Phase 3D (baseline) · **Phase 3E reboot revalidation**  
**Verdict:** **PASS WITH RESIDUALS**  
**Planning locus:** `SERVER-B-PLANNING`  
**Not:** 3X-UI / Xray / VLESS / Reality / nginx / Docker / domain DNS / Server A / provider panel

---

## 1. Purpose

Bring clean Ubuntu 24.04 Server B to a secure, documented base-OS state before any VPN application stack.

Authorized: package updates, NTP/DNS diagnosis, UFW, fail2ban, AdminVPS port-policy reconciliation, SSH preservation, preparation for direct network validation.

---

## 2. Access safety (pre-mutation)

| Check | Result |
|-------|--------|
| User | `marsops` |
| Hostname | `metacode-cloud.com` |
| Auth | Ed25519 key-only |
| sudo | password-confirmed **PASS** |
| `ssh` service | active |
| Second independent key session (keepalive) | **PASS** before UFW enable |
| Root remote SSH | remains disabled |
| Managed SSH drop-in `00-mars-server-ops-hardening.conf` | **PRESERVED** (not undone) |

---

## 3. OS update

| Item | Result |
|------|--------|
| Repos resolve | **PASS** (`apt-get update`) |
| Simulation before upgrade | 369 upgraded / 0 newly installed / 0 to remove / 7 not upgraded |
| Operation | `DEBIAN_FRONTEND=noninteractive apt-get upgrade -y` |
| Packages upgraded | **369** |
| Packages newly installed (deps of this phase) | fail2ban stack (later step): `fail2ban`, `python3-pyasyncore`, `python3-pyinotify`, `whois` |
| Packages removed | **NONE** |
| dist-upgrade / do-release-upgrade / PPA | **NOT DONE** |
| Held packages | none (`apt-mark showhold` empty) |
| Kept back / phasing | `byobu` (phased); `fwupd`, `linux-generic`, `linux-headers-generic`, `linux-image-generic`, `sosreport`, `ubuntu-server-minimal` |
| Running kernel after upgrade | still `6.8.0-36-generic` (linux meta packages kept back) |
| `/var/run/reboot-required` | Phase 3D: **YES** (`libc6`, `apparmor`, `dbus`). Phase 3E reboot: **CLEARED** |
| Reboot executed | **YES** — Phase 3E single `sudo reboot` — [SERVER-B-CONTROLLED-REBOOT-v1.md](SERVER-B-CONTROLLED-REBOOT-v1.md) |

---

## 4. Time / DNS

See [SERVER-B-TIME-DNS-BASELINE-v1.md](SERVER-B-TIME-DNS-BASELINE-v1.md).

| Control | State |
|---------|-------|
| NTP service | active |
| Clock synchronized | **no** — residual (UDP/123 / provider policy) |
| DNS | working via SolusVM static `/etc/resolv.conf` |
| `systemd-resolved` | left disabled |

---

## 5. Firewall / fail2ban

| Control | Doc |
|---------|-----|
| UFW | [SERVER-B-FIREWALL-BASELINE-v1.md](SERVER-B-FIREWALL-BASELINE-v1.md) — **ACTIVE**, deny in / allow out, **22/tcp only** |
| fail2ban | [SERVER-B-FAIL2BAN-BASELINE-v1.md](SERVER-B-FAIL2BAN-BASELINE-v1.md) — **ACTIVE**, `sshd` jail |

---

## 6. SSH revalidation (post-security)

| Check | Result |
|-------|--------|
| Fresh `marsops` key SSH after UFW | **PASS** |
| sudo | **PASS** |
| `sshd -t` | **PASS** |
| Effective: PermitRootLogin | no |
| Effective: PasswordAuthentication | no |
| Effective: KbdInteractiveAuthentication | no |
| Effective: PubkeyAuthentication | yes |
| Effective: MaxAuthTries | 3 |
| Effective: Port | 22 |
| root + password (PreferredAuthentications=password) | **REJECTED** (`Permission denied (publickey)`) |
| `50-cloud-init.conf` still contains `PasswordAuthentication yes` | **PRESENT** — superseded by first-match `00-` file (**do not undo**) |

---

## 7. Public listeners

| Listener | Classification |
|----------|----------------|
| TCP 22 sshd | **EXPECTED** |
| UDP DHCP client :68 | local/system |
| 3X-UI / Xray / nginx / Docker VPN | **ABSENT** |

Transient UDP high port observed briefly during validation and cleared — not present at final `ss -tulpn` with process attribution.

---

## 8. Provider port policy

[SERVER-B-PROVIDER-PORT-POLICY-v1.md](SERVER-B-PROVIDER-PORT-POLICY-v1.md) — retrieved 2026-08-25 from AdminVPS KB. Finland outbound restrictions + global UDP 123 noted for NTP residual and future VPN port selection.

---

## 9. Direct network validation

Operator-assisted script:

`X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-DIRECT-NETWORK-TEST.ps1`

Gate document: [SERVER-B-DIRECT-NETWORK-GATE-v1.md](SERVER-B-DIRECT-NETWORK-GATE-v1.md)

**Not executed** from Cursor session (VPN/TUN may distort metrics / risk AI connectivity). Operator TUN-OFF result **not yet ingested**.

Classification:

- Pre-purchase FI1: **APPROVED** (historical)  
- Actual Server B direct route: **WAITING FOR OPERATOR TUN-OFF TEST**

---

## 10. Residuals

1. NTP not synchronized (provider UDP/123) — clock accuracy separately **ACCEPTABLE** (Phase 3E HTTPS Date cross-check).  
2. Reboot required (libc6/apparmor/dbus) — **CLEARED** in Phase 3E.  
3. Linux meta packages kept back — kernel still 6.8.0-36; 6.8.0-138 remains **SECURITY RELEVANT** residual.  
4. Direct TUN-OFF network retest pending operator.  
5. Final MCA asset ID pending.  
6. Domain DNS still unconfigured.

---

## 11. Application / domain / provider console

| Surface | State |
|---------|-------|
| 3X-UI / Xray / nginx / Docker | **ABSENT** |
| Domain DNS | registered / **UNCHANGED** |
| Provider console | **UNCHANGED** (emergency-only) |
| Server A | **UNTOUCHED** |

---

*Phase 3D base OS security · Phase 3E reboot revalidation · PASS WITH RESIDUALS · no secrets in Git.*
