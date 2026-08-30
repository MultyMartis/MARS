# EQVPS-MICRO-IP — Controlled Reboot + Direct Port Gate

**Date:** 2026-08-27  
**Wave:** MARS Server Ops — EQVPS-MICRO-IP (Server B Phase 3E / 3E2 pattern adapted)  
**Operator access:** `marsops` @ dedicated public IPv4 `:22` (Ed25519 dedicated key)  
**Verdict:** **PASS_WITH_RESIDUALS**

**Not in this wave:** Xray / 3X-UI / nginx / Docker / certbot; DNS/PTR; swap; GPT/partition changes; cloud-init edits; open-vm-tools removal; SSH port change; second reboot; package install/update/upgrade/remove; persistent 443/8443 opening.

**Raw evidence (gitignored):** `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\reboot-port-gate-raw-2026-08-27\`

**Precedent:** [SERVER-B-CONTROLLED-REBOOT-v1.md](../SERVER-B-PLANNING/SERVER-B-CONTROLLED-REBOOT-v1.md), [SERVER-B-DIRECT-NETWORK-GATE-v1.md](../SERVER-B-PLANNING/SERVER-B-DIRECT-NETWORK-GATE-v1.md), [SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md](../SERVER-B-PLANNING/SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md) — safety model reused; diagnostic method adapted (Python temp listeners, **not** ssh.socket/443).

**Prior EQVPS waves:** [read-only intake](./EQVPS-MICRO-IP-read-only-intake-2026-08-27.md), [SSH bootstrap](./EQVPS-MICRO-IP-controlled-ssh-bootstrap-2026-08-27.md), [base OS security + firewall](./EQVPS-MICRO-IP-base-os-security-firewall-2026-08-27.md).

---

## 1. Scope summary

| Phase | Action | Result |
|-------|--------|--------|
| A | Pre-reboot lockout snapshot + gates | **PASS** |
| B | Exactly one `sudo reboot` + SSH recovery poll | **PASS** |
| C | Post-reboot `marsops` + sudo | **PASS** |
| D | Kernel activation `6.8.0-138-generic` | **PASS** (`KERNEL_ACTIVATION=PASS`) |
| E | SSH / UFW / fail2ban persistence | **PASS** |
| F | DNS / NTP / general state | **PASS** |
| G–J | Bounded direct gate TCP/22 + 443 + 8443 (TUN OFF) | **PASS** (all three) |
| K | Remove temp listeners + temp UFW rules | **PASS** |
| L | Fresh independent post-cleanup validation | **PASS** |

---

## 2. Controlled reboot

| Item | Value |
|------|-------|
| Exact reboot count | **1** |
| Method | `sudo reboot` (normal controlled; not provider force/reset) |
| Pre-reboot remote time | `2026-08-27T16:29:05Z` |
| Pre-reboot kernel | `6.8.0-124-generic` |
| Pre-reboot uptime | ~2h04m |
| Reboot issued (operator local) | `2026-08-27T23:29:07+07:00` |
| Boot time (`uptime -s`) | `2026-08-27 16:29:14` UTC |
| TCP/22 available again | ~15 s after issue (first poll) |
| Fresh authenticated SSH | ~29 s after issue (`2026-08-27T23:29:36+07:00`) |
| Provider web console | **NOT INVOKED** (documented emergency path only) |
| Second reboot | **NOT PERFORMED** |

---

## 3. Kernel activation

| Item | Value |
|------|-------|
| Before | `6.8.0-124-generic` |
| After | `6.8.0-138-generic` |
| **KERNEL_ACTIVATION** | **PASS** |
| `/var/run/reboot-required` after reboot | **NO** (cleared) |
| Bounded package query | `dpkg-query -W` for `linux-image-*` / `linux-generic*` / `linux-base` only — **no** bare `dpkg -l` |

Installed images observed post-reboot include both `linux-image-6.8.0-124-generic` and `linux-image-6.8.0-138-generic`; running kernel is **138**.

---

## 4. Persistence

### SSH

| Check | Result |
|-------|--------|
| `sshd -t` | **PASS** (exit 0) |
| Effective hardening | `permitrootlogin no`; `passwordauthentication no`; `kbdinteractiveauthentication no`; `pubkeyauthentication yes`; `maxauthtries 3`; `x11forwarding no`; `port 22` |
| Listener | TCP/22 (`sshd` / systemd socket activation) |
| `marsops` key login | **PASS** (fresh independent sessions) |
| sudo (`marsops` → root) | **PASS** |

### UFW

| Check | Result |
|-------|--------|
| Post-reboot baseline | **active**; default deny incoming / allow outgoing |
| Baseline inbound allow | **22/tcp only** (`# MARS SSH`, IPv4 + IPv6) |
| During diagnostics (temporary) | 22 + 443 + 8443 |
| After cleanup | **22/tcp only** restored |

### fail2ban

| Check | Result |
|-------|--------|
| Service | **active** |
| Jail | `sshd` **active** |
| Banned during wave | 0 (failed counters may increment from automation noise) |

### DNS / NTP

| Check | Result |
|-------|--------|
| DNS (`getent hosts example.com` / `google.com`) | **functional** |
| `resolvectl` | eth0 DNS servers present |
| `timedatectl` | System clock synchronized: **yes**; NTP service: **active** |
| `systemd-timesyncd` | active; contacted Ubuntu NTP |

---

## 5. Direct Goodline gate (TUN OFF)

| Item | Value |
|------|-------|
| TUN state during gate | **OFF** — `xray_tun` **Disabled** for tests |
| Physical interface | **Ethernet** (Realtek PCIe GbE) |
| Source address | `192.168.0.193` |
| Target | EQVPS dedicated public IPv4 (from local secret contour; not repeated here as a credential) |
| ping `-n 20` | **PASS** — 20/20, **0%** loss, ~61 ms average (61–66 ms) |
| traceroute | **PASS** — completes to target (~13 hops; Helsinki/Hetzner path visible) |
| TCP/22 | **PASS** — `TcpTestSucceeded=True`, InterfaceAlias=`Ethernet` |
| TCP/443 | **PASS** — `TcpTestSucceeded=True`, InterfaceAlias=`Ethernet` |
| TCP/8443 | **PASS** — `TcpTestSucceeded=True`, InterfaceAlias=`Ethernet` |

### Independent classifications

| Gate | Classification |
|------|----------------|
| **DIRECT_22** | **PASS** |
| **DIRECT_443** | **PASS** |
| **DIRECT_8443** | **PASS** |

**Note:** An earlier recovery poll briefly observed `InterfaceAlias=xray_tun` while TUN was still up. That observation was **invalidated** for gate classification. Gate tests were re-run only after TUN disable and Ethernet path confirmation.

**Local workstation residual:** re-enabling `xray_tun` after tests required elevated rights and **was not restored** by this wave (`Status: Disabled`). Operator may re-enable locally. **Not** a server residual.

---

## 6. Diagnostic implementation

| Item | Value |
|------|-------|
| Method | Temporary **Python 3** TCP accept/close listeners (base image `Python 3.12.3`) |
| Path | `/tmp/mars-eqvps-port-gate/` |
| Ports | **443**, **8443** only |
| Process model | `nohup python3 ... &` under sudo; PIDs recorded |
| Persistent systemd / cron | **NONE** |
| SSH / ssh.socket mutation | **NONE** (TCP/22 untouched) |
| Temporary UFW | `443/tcp` `# MARS TEMP DIRECT GATE 443`; `8443/tcp` `# MARS TEMP DIRECT GATE 8443` |
| Packages installed for test | **NONE** |

Evidence tooling discipline: no bare `dpkg -l`; `PAGER=cat` / `--no-pager` where applicable; bounded non-interactive SSH evidence collection.

---

## 7. Cleanup

| Item | Result |
|------|--------|
| Listener PIDs terminated | **YES** (2263, 2264) |
| `/tmp/mars-eqvps-port-gate/` removed | **YES** |
| Temporary UFW 443/8443 removed | **YES** (IPv4 + IPv6) |
| Final UFW | **22/tcp only** |
| Final public listeners | **SSH TCP/22 only** (+ local systemd-resolved) |
| Residual listeners on 443/8443 | **NONE** |
| Residual mars systemd units | **NONE** |

---

## 8. Residuals

| Residual | Notes |
|----------|-------|
| No swap | Acceptable; not created this wave |
| Prior GPT / cloud-init / open-vm-tools notes | Carried from earlier EQVPS waves; **not** mutated |
| Application stack absent | Expected |
| Phased/kept-back packages (historical) | Not re-audited as mutation target; no apt this wave |
| Operator `xray_tun` left Disabled | Local workstation; needs elevated re-enable |

---

## 9. Explicit non-mutations

| Area | Status |
|------|--------|
| Package maintenance (`apt` update/upgrade/install/remove/autoremove) | **NOT PERFORMED** |
| Swap | **NOT CREATED** |
| GPT / partitions | **NOT MODIFIED** |
| cloud-init | **NOT MODIFIED** |
| open-vm-tools | **NOT REMOVED** |
| DNS / PTR | **NOT CHANGED** |
| Hostname | **UNCHANGED** (`metacode-cloud`) |
| SSH port | **22 unchanged** |
| Applications (Xray/3X-UI/nginx/Docker/certbot/etc.) | **NOT DEPLOYED** |
| Second reboot | **NOT PERFORMED** |
| ssh.socket / SSH listen on 443/8443 | **NOT USED** |

---

## 10. Remote mutations (exact classes)

1. Exactly one controlled `sudo reboot`.  
2. Temporary privileged Python listeners on TCP/443 and TCP/8443 under `/tmp/mars-eqvps-port-gate/`.  
3. Temporary UFW allow rules for 443/tcp and 8443/tcp (with MARS TEMP comments).  
4. Mandatory cleanup: kill listeners, remove temp directory, delete temporary UFW rules.

No other remote mutation classes.

---

## 11. Classification rationale

**PASS_WITH_RESIDUALS** — all charter success criteria for reboot, persistence, kernel activation, cleanup, and independent DIRECT_22 / DIRECT_443 / DIRECT_8443 **PASS** results were met. Residuals are non-blocking (no swap; prior known host residuals; local TUN adapter left disabled).

---

## 12. Recommended next phase (do not execute)

Given **DIRECT_443=PASS** and **DIRECT_8443=PASS** on this owned dedicated IPv4 from operator Goodline with TUN OFF:

**Next controlled phase:** chartered **TLS / Xray-compatible ingress design + deploy wave** preferring **TCP/443** as primary public entry (with **8443** as documented alternate), still without opening persistent firewall rules until that wave’s explicit allowlist step. Include certificate strategy, process isolation, and UFW allow-only-after-listener-ready safety — Server B architecture freeze constraints apply by analogy.

Do **not** treat this report as authorization to deploy Xray/3X-UI/nginx.

---

*EQVPS-MICRO-IP controlled reboot + direct port gate · 2026-08-27 · PASS_WITH_RESIDUALS · no secrets in Git.*
