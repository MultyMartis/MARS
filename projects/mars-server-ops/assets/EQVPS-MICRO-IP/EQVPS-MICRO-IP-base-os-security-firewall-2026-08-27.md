# EQVPS-MICRO-IP — Base OS Security + Firewall Hardening

**Date:** 2026-08-27  
**Wave:** MARS Server Ops — EQVPS-MICRO-IP Phase (Server B Phase 3D pattern)  
**Operator access:** `marsops` @ `95.216.126.173:22` (Ed25519 dedicated key)  
**Verdict:** **PASS_WITH_RESIDUALS**

**Not in this wave:** reboot, SSH port change, DNS/PTR/hostname change, swap, GPT repair, cloud-init edits, open-vm-tools removal, application stack, non-22 port openings, diagnostic 443 listeners.

**Raw evidence (gitignored):** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\base-security-raw-2026-08-27\`

**Precedent:** [SERVER-B-BASE-OS-SECURITY-v1.md](../SERVER-B-PLANNING/SERVER-B-BASE-OS-SECURITY-v1.md), [SERVER-B-FIREWALL-BASELINE-v1.md](../SERVER-B-PLANNING/SERVER-B-FIREWALL-BASELINE-v1.md), [SERVER-B-FAIL2BAN-BASELINE-v1.md](../SERVER-B-PLANNING/SERVER-B-FAIL2BAN-BASELINE-v1.md)

---

## 1. Scope summary

| Phase | Action | Result |
|-------|--------|--------|
| A | Pre-change baseline + SSH hardening validation | **PASS** |
| B | `apt-get update` + normal `apt-get upgrade -y` | **PASS** (0 upgraded; 2 phased kept-back) |
| C | fail2ban install + MARS sshd jail | **PASS** |
| D | UFW deny-in / allow-out + SSH/22 only + fresh session test | **PASS** |
| E | unattended-upgrades observation | **PASS** (Ubuntu default preserved) |
| F | DNS / NTP post-check | **PASS** |
| G | Post-change security validation | **PASS** |

**Reboot:** **NOT performed** (deferred by charter).

---

## 2. Package maintenance

| Item | Value |
|------|-------|
| `apt-get update` | **PASS** |
| `apt-get upgrade -y` (normal only) | **PASS** |
| Packages upgraded this wave | **0** |
| Packages newly installed (this wave) | fail2ban stack from prior partial run in same session (`fail2ban`, deps); upgrade wave itself: **0** |
| Package removals | **0** (required zero — confirmed) |
| Kept back (phasing) | `libproc2-0`, `procps` |
| `/var/run/reboot-required` | **present** (pre-existing + unchanged by this wave) |
| Reboot-required packages | `libc6`, `linux-image-6.8.0-138-generic`, `linux-base` |
| Running kernel (unchanged) | `6.8.0-124-generic` |
| Installed newer kernel image (not running) | `linux-image-6.8.0-138-generic` |

---

## 3. UFW

| Item | Value |
|------|-------|
| Status | **active** (enabled on startup) |
| Default incoming | **deny** |
| Default outgoing | **allow** |
| Routed | disabled |
| Inbound allow rules | **22/tcp** `# MARS SSH` (IPv4 + IPv6 rule present) |
| Application ports | **NOT opened** (80, 443, 8443, 5928, 2096, etc.) |

**Activation safety**

| Step | Result |
|------|--------|
| SSH listening on TCP/22 before enable | **PASS** |
| Rule added before enable | **PASS** |
| `ufw --force enable` | **PASS** |
| Independent fresh SSH session (`marsops` + dedicated key) | **PASS** |
| `sudo whoami` → `root` on fresh session | **PASS** |

---

## 4. fail2ban

| Item | Value |
|------|-------|
| Package | `fail2ban` 1.0.2-3ubuntu0.1 (Ubuntu noble) |
| Service | **active** |
| Managed config | `/etc/fail2ban/jail.d/00-mars-server-ops-ssh.conf` |
| Jail | `sshd` only |
| Backend | `systemd` |
| Policy | `maxretry=5`, `findtime=10m`, `bantime=1h` (Server B baseline) |
| `fail2ban-client -t` | **OK** |
| Currently banned | 0 |
| Intentional ban test | **NOT PERFORMED** (charter forbids) |

---

## 5. SSH preservation

Effective `sshd -T` after changes:

| Setting | Expected | Observed |
|---------|----------|----------|
| port | 22 | **22** |
| permitrootlogin | no | **no** |
| passwordauthentication | no | **no** |
| kbdinteractiveauthentication | no | **no** |
| pubkeyauthentication | yes | **yes** |
| maxauthtries | 3 | **3** |
| x11forwarding | no | **no** |

| Check | Result |
|-------|--------|
| `sshd -t` | **PASS** |
| marsops key login | **PASS** |
| sudo (password) | **PASS** |

Hardening drop-in from prior wave: `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` — **unchanged**.

---

## 6. DNS / time

### DNS

| Check | Result |
|-------|--------|
| `/etc/resolv.conf` | stub → `/run/systemd/resolve/stub-resolv.conf` |
| `resolvectl status` | eth0 DNS `185.12.64.2`, `185.12.64.1` |
| `getent hosts example.com` | **PASS** |
| `getent hosts google.com` | **PASS** |
| DNS mutation this wave | **NONE** |

### NTP / clock

| Check | Result |
|-------|--------|
| `timedatectl` — synchronized | **yes** |
| NTP service | **active** (`systemd-timesyncd`) |
| Time server | `ntp.ubuntu.com` (185.125.190.57) |
| NTP mutation this wave | **NONE** |

---

## 7. Resource state

| Item | Value |
|------|-------|
| Hostname | `metacode-cloud` (**unchanged**) |
| RAM | ~1.9 GiB |
| Swap | **none** |
| Root disk | `/dev/sda1` ext4 24G (~10% used) |
| Listeners (public) | **22/tcp** only (plus local systemd-resolved stubs) |

---

## 8. Application stack absence

| Package / binary probe | Result |
|----------------------|--------|
| nginx, xray, docker.io, certbot | **absent** |
| `nginx`, `xray`, `docker`, `certbot` in PATH | **absent** |

No unintended application deployment detected.

---

## 9. unattended-upgrades (observation only)

| Item | Value |
|------|-------|
| Package | **installed** (`unattended-upgrades` 2.9.1+nmu4ubuntu1) |
| Service | **active (running)** |
| `/etc/apt/apt.conf.d/20auto-upgrades` | present — periodic update + unattended upgrade enabled |
| `/etc/apt/apt.conf.d/50unattended-upgrades` | present — Ubuntu default origins |
| Policy rewrite this wave | **NONE** (preserve Ubuntu defaults per charter) |

---

## 10. Residuals (expected / unchanged)

| Residual | Classification |
|----------|----------------|
| `/var/run/reboot-required` | **EXPECTED** — kernel/libc pending; reboot deferred to next phase |
| Running kernel `6.8.0-124` vs installed `6.8.0-138` | **EXPECTED** until controlled reboot |
| No swap | **EXPECTED** — out of scope |
| GPT header warning (from intake) | **EXPECTED** — not remediated |
| cloud-init deprecated user-key warning | **EXPECTED** — not remediated |
| open-vm-tools on KVM | **EXPECTED** — not removed |
| Phased kept-back packages (`libproc2-0`, `procps`) | **EXPECTED** — Ubuntu phasing |
| Non-22 ingress / direct network gate | **NOT TESTED** — next phase |
| fail2ban `Total failed: 4` (historical journal matches) | **INFORMATIONAL** — no bans applied |

---

## 11. Explicit non-mutations

| Item | Status |
|------|--------|
| Reboot | **NOT performed** |
| Swap creation | **NOT performed** |
| GPT / partition repair | **NOT performed** |
| cloud-init | **NOT modified** |
| open-vm-tools | **NOT removed/disabled** |
| DNS / PTR / hostname | **NOT modified** |
| Application stack | **NOT deployed** |
| Ports 80/443/8443/5928/2096 | **NOT opened** |
| SSH port change | **NOT performed** |
| Root/password SSH re-enable | **NOT performed** |

---

## 12. Remote mutation classes

1. **APT:** index refresh; normal upgrade (no removals).  
2. **Packages installed:** `fail2ban` (+ dependencies from Ubuntu repo).  
3. **fail2ban:** drop-in jail config at `/etc/fail2ban/jail.d/00-mars-server-ops-ssh.conf`; service enabled.  
4. **UFW:** default policies set; `22/tcp` allow with comment `MARS SSH`; firewall enabled.  
5. **No changes** to SSH hardening drop-in, DNS, NTP, hostname, cloud-init, disk, swap, or application layer.

---

## 13. Git / evidence

| Item | Value |
|------|-------|
| Branch | `mars/canonical-post-recovery` |
| Commit | **NONE** (not authorized) |
| Git-safe artefact | this file |
| Local raw logs | `base-security-evidence.txt`, `base-security-evidence.json` under gitignored local path |

---

## 14. Recommended next phase

**Controlled reboot + persistence validation + direct network port gate** — execute reboot to activate `6.8.0-138-generic`, confirm SSH/UFW/fail2ban/DNS/NTP survive reboot, then bounded direct-network ingress test for non-22 ports per MARS Server B Phase 3E pattern. **Do not** open application ports until chartered.

---

*EQVPS-MICRO-IP base OS security + firewall · 2026-08-27 · no secrets.*
