# EQVPS-MICRO-IP — Read-Only Live Intake

**Working reference:** `EQVPS-MICRO-IP` (neutral; **no** permanent MCA/ATLAS asset ID assigned)  
**Date:** 2026-08-27  
**Programme:** MARS Server Ops & VPS Forge  
**Mode:** Strict read-only live intake — evidence gathering only  
**Verdict:** **READY_WITH_RESIDUALS**  
**Remote mutations:** **0**

---

## 1. Task scope

Establish an exact pre-change baseline for the newly provisioned EQVPS Micro-IP VPS and determine readiness for a later controlled SSH bootstrap / hardening phase.

**Explicitly out of scope (not performed):**

- hardening; package install/update; SSH/firewall/hostname/password/user changes  
- reboot; DNS/PTR changes  
- Xray / 3X-UI / nginx / Docker / certificates / VPN / monitoring / agents / cron / systemd mutations  
- port scanning / broad network experiments from the VPS  

---

## 2. Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume `X:` label | **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| Staged changes | **empty** |
| Foreign WIP | **PRESERVED** (iseo-su / forge-wordpress / recovery-temp / etc. — untouched) |
| Commit / push | **NONE** |
| Programme index | [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) |
| Secret model | [SECRET-HANDLING-MODEL-v1.md](../../SECRET-HANDLING-MODEL-v1.md) |
| Prior pattern | Server B Phase 3B provisioning intake + MCA-VPN-001 Phase 1B-1 paramiko session |

---

## 3. Connection method (sanitized)

| Field | Value |
|-------|-------|
| Method class | SSH password auth (temporary bootstrap) |
| Tooling | Python **paramiko** (same class as MCA-VPN-001 / Server B intake) |
| User | `root` |
| Port | `22` |
| Auth attempts | **1** (success) |
| `secret_ref` | `local/infrastructure/EQVPS-MICRO-IP/secrets.local.md` |
| Credentials in Git | **NONE** |
| Credentials in REPORT | **NONE** |
| Temporary credential files | **NONE** created |
| Host key policy | first-connect AutoAdd (session-only; not written to Git) |

Raw observational capture (local-only, gitignored):  
`X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\intake-raw-2026-08-27\readonly-evidence.txt`

---

## 4. Operator-provided direct-network gate (pre-task)

**Class: OPERATOR-PROVIDED** (not re-run as VPS-side proof in this phase)

| Item | Operator evidence |
|------|-------------------|
| Path | VPN/TUN **OFF**, physical Ethernet / Goodline |
| ICMP | 20/20, 0% loss |
| RTT | ~61–64 ms (avg ~61 ms) |
| traceroute | reached assigned VPS; path visibly traversed **Hetzner Helsinki** infrastructure |
| TCP/22 direct | **PASS** |
| Dedicated public IPv4 | **YES** (operator + live guest match) |

---

## 5. Provider control-panel observations (operator screenshots)

**Class: PROVIDER-PANEL CLAIM / OPERATOR-PROVIDED** — verified from guest where noted.

| Panel claim | Guest verification |
|-------------|-------------------|
| Product EQVPS Micro-IP | Operator attestation |
| 2 vCPU | **CONFIRMED** — `nproc`/`lscpu` = 2 |
| 2 GB RAM | **CONFIRMED** — ~1.9 GiB MemTotal |
| 25 GB NVMe | **CONFIRMED** — `sda` 25G |
| Dedicated public IPv4 | **CONFIRMED** — `eth0` holds `95.216.126.173/28` |
| Ubuntu 24.04 | **CONFIRMED** — Ubuntu 24.04.4 LTS |
| SSH port 22 | **CONFIRMED** — listener + `sshd -T` |
| Inbound all ports on public IPv4 | **PROVIDER-PANEL CLAIM** — not port-tested this phase |
| Full outbound Internet | **OBSERVED** functional DNS (`getent`); broad egress matrix **not** chartered |
| Console / root password reset / OS reinstall / PTR | **OPERATOR-PROVIDED** panel surfaces — not mutated |
| PTR resembles `clients.your-server.de` | **SAFE UNKNOWN** live (no PTR query chartered) |
| Panel hostname `metacode-cloud` | **CONFIRMED** guest hostname |

---

## 6. Command / evidence summary

Sequential read-only remote sections via `exec_command`:

| Section | Status |
|---------|--------|
| A Identity / OS | **CHECKED** |
| B CPU / memory / swap | **CHECKED** |
| C Storage | **CHECKED** |
| D Network / DNS stubs | **CHECKED** |
| E Listeners / services | **CHECKED** |
| F SSH effective config | **CHECKED** |
| G Firewall | **CHECKED** |
| H fail2ban | **CHECKED** (absent) |
| I Packages / reboot flag | **CHECKED** (no `apt update`) |
| J DNS / time / NTP | **CHECKED** |
| K Application stack probes | **CHECKED** |
| L Provider / cloud agents | **CHECKED** |
| M Users / keys metadata | **CHECKED** |
| N Bounded logs | **CHECKED** |

Forbidden mutation commands (`apt update/upgrade/install`, firewall changes, sshd reload, etc.) were **not** used.

---

## 7. Factual intake results

### 7.1 Server identity — CONFIRMED

| Field | Live |
|-------|------|
| Hostname | `metacode-cloud` |
| OS | Ubuntu 24.04.4 LTS (Noble) |
| Kernel (running) | `6.8.0-124-generic` |
| Arch | `x86_64` |
| Virtualization | **KVM** (`systemd-detect-virt`, `hostnamectl`) |
| Hardware vendor | QEMU |
| Boot / uptime at intake | boot `2026-08-27 14:24:39` UTC; ~35 min uptime |
| Timezone | `Etc/UTC` |
| Working asset ID | `EQVPS-MICRO-IP` only (no MCA ID invented) |

### 7.2 Resources — CONFIRMED

| Resource | Live | vs panel |
|----------|------|----------|
| vCPU | 2 (AMD Ryzen 5 3600 presented to guest) | **MATCH** |
| RAM | 1.9 GiB total; ~1.5 GiB available | **MATCH** (~2 GB) |
| Swap | **none** (`SwapTotal: 0`) | **OBSERVED** |
| Disk | `sda` 25G; root `/dev/sda1` ext4 ~24G (~2.3G used / ~21G avail) | **MATCH** |
| Boot | `/boot` ext4 on `sda16`; EFI vfat `sda15` | **PRESENT** |
| LVM volumes | no PV/VG/LV in use (tools may exist; empty `pvs`/`vgs`/`lvs`) | **ABSENT** volumes |
| Extra disk | `sr0` 4M iso9660 (cloud-init NoCloud seed) | **OBSERVED** |
| Unexpected data disk | **none** | — |

### 7.3 Network — CONFIRMED / OBSERVED

| Item | Live |
|------|------|
| Interface | `eth0` UP, MTU 1500 |
| Public IPv4 | `95.216.126.173/28` on eth0 (static route proto) |
| Gateway | `95.216.126.161` |
| Global IPv6 | **none** on eth0 (link-local only) |
| DNS stub | `/etc/resolv.conf` → `/run/systemd/resolve/stub-resolv.conf`; `nameserver 127.0.0.53` |
| systemd-resolved | **enabled** + **active** |
| Uplink resolvers | `185.12.64.2`, `185.12.64.1`, `2a01:4ff:ff00::add:1` (**OBSERVED**; Hetzner-associated DNS ranges — not a corporate-ownership claim) |
| DNS functional test | `getent hosts example.com` / `google.com` **PASS** (AAAA answers) |
| Public egress IP identity | Guest configured address = `95.216.126.173`; external echo IP **SAFE UNKNOWN** (no unauthorized external IP echo) |

**Listeners (TCP/UDP attributed):**

| Socket | Process |
|--------|---------|
| `0.0.0.0:22`, `[::]:22` | `sshd` (+ systemd socket activation) |
| `127.0.0.53:53`, `127.0.0.54:53` (tcp/udp) | `systemd-resolved` |

No unexpected web/VPN/panel listeners observed.

### 7.4 SSH baseline — CONFIRMED (bootstrap-open)

| Directive (`sshd -T`) | Effective |
|------------------------|-----------|
| Port | `22` |
| ListenAddress | `0.0.0.0:22`, `[::]:22` |
| PermitRootLogin | **yes** |
| PasswordAuthentication | **yes** |
| PubkeyAuthentication | yes |
| KbdInteractiveAuthentication | no |
| AuthenticationMethods | any |
| UsePAM | yes |
| MaxAuthTries | 6 |
| X11Forwarding | **yes** |
| AllowUsers / DenyUsers | **not set** |

Version: OpenSSH_9.6p1 Ubuntu-3ubuntu13.18.

Drop-ins present:

- `/etc/ssh/sshd_config.d/00-eqvps-permitroot.conf` — `PermitRootLogin yes`, `PasswordAuthentication yes`  
- `/etc/ssh/sshd_config.d/60-cloudimg-settings.conf` — `PasswordAuthentication yes`  

`/root/.ssh/authorized_keys`: **empty** (0 bytes).

### 7.5 Firewall / fail2ban

| Control | State | Class |
|---------|-------|-------|
| UFW package/unit | unit **enabled**; **status inactive** | **CONFIRMED** |
| nft ruleset | empty | **OBSERVED** |
| iptables / ip6tables | default ACCEPT policies only | **CONFIRMED** |
| fail2ban | **not installed** (no unit, no package) | **CONFIRMED ABSENT** |

### 7.6 DNS / time / NTP

| Item | State |
|------|-------|
| Clock synchronized | **yes** |
| NTP service | **active** (`systemd-timesyncd`) |
| Peer contacted | `ntp.ubuntu.com` (`185.125.190.57:123`) |
| chrony | absent |
| Absolute clock accuracy vs external reference | **SAFE UNKNOWN** (sync state confirmed; independent accuracy measurement not performed) |

### 7.7 Application stack — ABSENT (bounded)

Binary / dpkg / unit / path / process probes for:  
x-ui, xray, nginx, apache2, docker, containerd, podman, caddy, certbot, n8n, PostgreSQL, MySQL/MariaDB, WireGuard, OpenVPN, Shadowsocks, Hysteria, sing-box — **ABSENT**.

letsencrypt / `/var/www` paths — **ABSENT**.

### 7.8 Provider / cloud agents — OBSERVED

| Component | State |
|-----------|-------|
| cloud-init | installed; status **done** / **degraded done** (deprecated `user` string warnings; `errors: []`) |
| DataSource | NoCloud seed `/dev/sr0` |
| qemu-guest-agent | **PRESENT** + **active** |
| EQVPS-named guest tooling beyond SSH drop-in | **not observed** as packages |
| Hetzner-named guest packages | **not observed** |
| Monitoring agents (telegraf/datadog/zabbix/…) | **not observed** |
| open-vm-tools unit enabled | **OBSERVED** (Ubuntu image residual on KVM guest; not treated as VMware hypervisor proof) |

### 7.9 Users / login baseline

| Item | State |
|------|-------|
| Human users (UID ≥1000 excl. nobody) | **none** |
| sudo group members | **empty** |
| root account | present; password set (`passwd -S` → `P`); expiry never |
| Authorized keys | empty file only |

Journal note (pre-intake / early life): `chpasswd` password change for root at `2026-08-27 14:37:50` via qemu-ga path — **OBSERVED** historical event consistent with provider/console password set; **not** performed by this intake session.

### 7.10 Logs / failed units (bounded)

| Item | State |
|------|-------|
| `systemctl --failed` | **0** failed units |
| GPT warnings at boot | Primary/alt GPT header not at end of disk (`7340031 != 52428799`) — **RESIDUAL** |
| cloud-init recoverable | deprecation warnings only |

---

## 8. Residuals

1. **reboot-required: YES** — packages include `linux-image-6.8.0-138-generic` while running `6.8.0-124-generic`; also `libc6`, `linux-base`.  
2. Cached `apt list --upgradable` shows at least `procps` / `libproc2-0` pending (indexes **not** refreshed this phase — residual completeness **SAFE UNKNOWN**).  
3. No swap configured.  
4. GPT geometry warning (likely post-image disk size vs partition table).  
5. UFW installed/enabled unit but inactive; host packet filter effectively open.  
6. fail2ban absent.  
7. SSH bootstrap-open: root + password + X11Forwarding yes + MaxAuthTries 6.  
8. cloud-init **degraded done** (deprecated user key).  
9. `open-vm-tools` enabled on KVM image.  
10. Permanent MCA asset ID **not assigned**.  
11. Provider PTR / panel inbound-all-ports claim **not** live-validated beyond SSH/22.

---

## 9. Security risks

| Risk | Class |
|------|-------|
| Direct Internet exposure of **root password SSH** on port 22 with empty authorized_keys | **SECURITY RISK** (expected temporary bootstrap; must not remain) |
| Host firewall inactive (ACCEPT defaults) while provider claims all inbound ports open | **SECURITY RISK** / **PROVIDER-PANEL CLAIM** interaction |
| No fail2ban / intrusion throttling | **SECURITY RISK** (baseline gap) |
| X11Forwarding enabled on server SSH | **SECURITY RISK** (low urgency vs root password; still harden later) |
| Pending reboot after kernel/libc package state | **RESIDUAL** (operational; schedule in controlled phase) |

---

## 10. SAFE UNKNOWN

- Exact contractual ownership / rack location beyond guest + operator path evidence  
- Live PTR/rDNS value  
- True “all inbound ports open” matrix (443 and others) — deferred diagnostic phase  
- Full pending-update set without `apt update`  
- Absolute NTP accuracy vs external calibrated source  
- Whether `open-vm-tools` is intentionally required by provider  
- Provider console availability at incident time (panel feature attested; not exercised)  

---

## 11. Classification summary

| # | Area | Result |
|---|------|--------|
| 1 | Server identity | **CONFIRMED** `metacode-cloud` / Ubuntu 24.04.4 / KVM |
| 2 | Provider / infra | EQVPS Micro-IP (**OPERATOR**); path/DNS consistent with Hetzner HEL infra (**OBSERVED**, not ownership claim) |
| 3 | OS baseline | Clean cloud Ubuntu; cloud-init degraded warnings |
| 4 | Resource baseline | 2 vCPU / ~2 GB / 25G — **MATCH** panel |
| 5 | Network baseline | Dedicated IPv4 on eth0; SSH:22 only public listener; DNS OK |
| 6 | SSH baseline | Bootstrap-open root+password |
| 7 | Firewall baseline | UFW inactive; nft empty; iptables ACCEPT |
| 8 | fail2ban | Absent |
| 9 | DNS baseline | systemd-resolved stub + Hetzner-range uplink resolvers |
| 10 | Time / NTP | Synchronized via timesyncd |
| 11 | Application stack | Target apps **ABSENT** |
| 12 | Update / reboot | reboot-required **YES**; indexes not refreshed |
| 13 | Recovery surface | Provider console / password reset / reinstall / PTR (**OPERATOR-PROVIDED**); Git holds no live recovery secrets |
| 14 | Security risks | Root password SSH + open host filter |
| 15 | SAFE UNKNOWN | See §10 |
| 16 | Readiness | **READY_WITH_RESIDUALS** |

---

## 12. Remote mutations assertion

```text
REMOTE_MUTATIONS = 0
```

Backed by charter + session: observational `exec_command` only; no package/user/SSH/firewall/DNS/service/state changes; no reboot.

---

## 13. Files created / changed locally

| Path | Role |
|------|------|
| `X:\AI MARS\projects\mars-server-ops\assets\EQVPS-MICRO-IP\EQVPS-MICRO-IP-read-only-intake-2026-08-27.md` | **This Git-safe report** (created) |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\intake-raw-2026-08-27\readonly-evidence.txt` | Raw evidence (local-only; **not** for Git) |
| `X:\AI MARS\local\infrastructure\EQVPS-MICRO-IP\secrets.local.md` | Unchanged secret contour |

Temporary intake helper script removed after run. No secrets copied into Git paths.

---

## 14. Git status (session)

| Item | Value |
|------|-------|
| Branch | `mars/canonical-post-recovery` |
| Before | Foreign WIP present; staged empty; this asset path absent |
| After | Same foreign WIP preserved; **untracked** report under `assets/EQVPS-MICRO-IP/` expected |
| Staged | **none** (task) |
| Commit | **NONE** |

---

## 15. Verdict and next phase

**Verdict:** `READY_WITH_RESIDUALS`

**Reasons:** SSH live access works; OS/resources match panel; application stack clean; DNS/NTP healthy; operator direct TCP/22 already PASS. Residuals (open root password SSH, inactive UFW, no fail2ban, reboot-required, GPT warning, no swap) are expected for a fresh bootstrap and do **not** block a controlled next phase — they **define** it.

**Exact next recommended phase (do not execute now):**

> Controlled SSH bootstrap for `EQVPS-MICRO-IP`: create dedicated `marsops` account + Ed25519 key + sudo; dual-session validation; then disable root SSH and password authentication; leave UFW/fail2ban/reboot/selected-port gate for subsequent chartered phases (Server B Phase 3C→3D pattern).

---

*End of read-only intake evidence — 2026-08-27.*
