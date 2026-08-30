# Server B Provisioning Intake v1

**Status:** **LIVE READ-ONLY INTAKE COMPLETE** — 2026-08-25  
**Wave:** MARS Server Ops Phase 3B  
**Planning locus:** `SERVER-B-PLANNING`  
**Final MCA / ATLAS asset ID:** **NOT ASSIGNED**  
**Overall verdict:** **PASS WITH RESIDUALS**

**Mode:** Strict read-only. No package install, no hardening, no DNS, no firewall mutation, no application build.

---

## 1. Intake gate

| Gate | Result |
|------|--------|
| Operator-approved provisioning | **YES** — AdminVPS Finland Micro (operator panel attestation) |
| Local access reference | **PRESENT** — `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md` |
| Required access fields | **PRESENT** (provider, hostname, public_ipv4, host, port, user, auth_type, password, domain, provisioned, initial_os) |
| Live SSH session | **ESTABLISHED** — password auth, **1** attempt, success |
| Server mutations | **NONE** (see safety assertion) |
| Server A operations | **NONE** |

---

## 2. Provisioning identity (operator + live)

| Field | Expected / operator panel | Live observed | Class |
|-------|---------------------------|---------------|-------|
| Provider | AdminVPS | AdminVPS (operator attestation; not re-checked in panel this wave) | **MATCH** (operator) / panel **NOT CHECKED** live |
| Location | Finland / Helsinki | **SAFE UNKNOWN** from OS alone (KVM guest) | **SAFE UNKNOWN** (live geo) |
| Plan | Micro | **NOT CHECKED** in provider panel this wave | **SAFE UNKNOWN** (live tariff) |
| Hostname / label | `metacode-cloud.com` | `metacode-cloud.com` | **MATCH** |
| Domain identity | `metacode-cloud.com` | hostname matches; DNS **not configured** this wave | **MATCH** (hostname) / DNS **NOT CHECKED** as production |
| OS | Ubuntu 24.04 LTS | Ubuntu 24.04 LTS | **MATCH** |
| Marketplace apps | not installed | docker / nginx / x-ui / xray **ABSENT** | **MATCH** (application stack) |
| BitNinja | not enabled | no BitNinja evidence in allowed checks | **SAFE UNKNOWN** / consistent with absent |
| Additional IPv4 | none | single IPv4 on eth0; no second public IPv4 observed | **MATCH** (observed) |
| Provider weekly backup | 1 free copy (operator) | **NOT CHECKED** live | **SAFE UNKNOWN** (live) |
| Traffic allowance | 10 TB (operator panel) | **NOT CHECKED** live | **SAFE UNKNOWN** (live) |
| Support access | disabled/prohibited unless changed | **NOT CHECKED** live | **SAFE UNKNOWN** |
| Recovery console | available (operator) | **NOT CHECKED** live — policy recorded | **SAFE UNKNOWN** (live availability) |

---

## 3. Access (sanitized)

| Field | Value |
|-------|-------|
| Method | SSH |
| User | `root` (temporary bootstrap) |
| Port | `22` |
| Auth type | `password` |
| Public IPv4 in Git | `<SERVER_B_IP>` |
| `secret_ref` | `local/infrastructure/SERVER-B-PLANNING/secrets.local.md` |
| Auth attempts used | 1 of max 2 |
| Session tooling | Python paramiko (same pattern as MCA-VPN-001 Phase 1B-1) |

**Note:** local `host` field currently holds a placeholder; intake used `public_ipv4`. Do not print credentials.

---

## 4. Safety assertion (Server B)

| Assertion | Result |
|-----------|--------|
| Server files created | **NONE** |
| Server files modified | **NONE** |
| Packages installed / upgraded | **NONE** |
| Users created | **NONE** |
| SSH config changed | **NONE** |
| Firewall changed | **NONE** |
| Services started / stopped / restarted / reloaded | **NONE** (read-only status queries only) |
| 3X-UI / Xray / Docker / nginx installed | **NONE** |
| Certificates created | **NONE** |
| DNS changed | **NONE** |
| Backups created | **NONE** |
| Provider settings changed | **NONE** |
| Reboot | **NONE** |

---

## 5. Live identity summary

| Field | Live | Class |
|-------|------|-------|
| Hostname | `metacode-cloud.com` | **MATCH** |
| OS | Ubuntu 24.04 LTS | **MATCH** |
| Kernel | `6.8.0-36-generic` | **PRESENT** |
| Arch | `x86_64` | **PRESENT** |
| Virtualization | KVM | **PRESENT** |
| Timezone | `Etc/UTC` | **PRESENT** |
| NTP service | active | **PRESENT** |
| Clock synchronized | **no** at intake | **CHANGED** vs ideal / residual |
| Uptime at intake | ~43 minutes | **PRESENT** |

Detail: [SERVER-B-CURRENT-PASSPORT-v1.md](SERVER-B-CURRENT-PASSPORT-v1.md), [SERVER-B-BOOTSTRAP-BASELINE-v1.md](SERVER-B-BOOTSTRAP-BASELINE-v1.md).

---

## 6. Resources vs expectation

| Resource | Expected | Live | Class |
|----------|----------|------|-------|
| vCPU | 2 | 2 — AMD EPYC (KVM) | **MATCH** |
| RAM | ~4 GB | 3.8 GiB | **MATCH** |
| Disk | ~30 GB NVMe | 30G `/dev/vda1` ext root | **MATCH** |
| Swap | not specified | 512M `/swapfile` | **PRESENT** (not blocking) |
| Free space | — | ~26G avail on `/` | **PRESENT** |

---

## 7. Network / listeners

| Item | Live | Class |
|------|------|-------|
| Public IPv4 on eth0 | `<SERVER_B_IP>/24` (DHCP) | **PRESENT** |
| IPv6 | link-local only on eth0 (no global IPv6 observed) | **PRESENT** / no global |
| Default route | via provider gateway on eth0 | **PRESENT** |
| Listening TCP | `*:22` sshd only | **PRESENT** |
| Listening UDP | DHCP client `:68` | **PRESENT** |
| 3X-UI / Xray / nginx / Docker listeners | **ABSENT** | **MATCH** (clean host) |
| `resolvectl status` | failed (systemd-resolved disabled) | **SAFE UNKNOWN** DNS detail |

Evidence: [SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md](SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md).

---

## 8. Firewall / SSH bootstrap

| Layer | Live | Class |
|-------|------|-------|
| ufw | inactive | **PRESENT** |
| nft ruleset | empty / none listed | **PRESENT** |
| iptables / ip6tables | default ACCEPT policies | **PRESENT** |
| fail2ban | unit **ABSENT** | **ABSENT** |
| sshd PermitRootLogin | yes | **PRESENT** (bootstrap) |
| sshd PasswordAuthentication | yes | **PRESENT** (bootstrap) |
| Internet password guessing | failed root attempts observed in `systemctl status ssh` | **PRESENT** — residual risk |

---

## 9. Software baseline

| Component | State |
|-----------|-------|
| docker | **ABSENT** |
| nginx | **ABSENT** |
| x-ui | **ABSENT** |
| xray | **ABSENT** |
| fail2ban | **ABSENT** |
| atop | **PRESENT** (enabled unit — provider/image residual) |
| snapd | **PRESENT** (Ubuntu default) |
| cloud-init | **PRESENT** (typical VPS) |

---

## 10. Provider port restriction

```text
PORT POLICY — MUST BE VERIFIED BEFORE VPN PORT ASSIGNMENT
```

Provider knowledge-base reference (operator-observed):  
https://my.adminvps.ru/knowledgebase/561/zablokirovannye-porty-na-usluge-vps.html

Exact blocked-port list: **NOT hard-coded** in this intake (no authoritative in-repo evidence dump of the current page).

Planning caution retained: **TCP 8444 must not be selected** unless current provider evidence explicitly confirms it is usable.

---

## 11. Provider console policy

AdminVPS web/VNC/recovery console is **NOT** the normal MARS operating path.

Normal path: **MARS/Cursor → SSH → Server B**.

Provider panel reserved for emergency console, password recovery, power/reboot recovery, rescue mode, provider backup restore, infrastructure-level troubleshooting.

---

## 12. Asset state

```text
PROVISIONED — FINAL ASSET REGISTRATION PENDING
```

Locus remains `SERVER-B-PLANNING`. **No** MCA/ATLAS ID invented.

---

## 13. Residuals (non-blocking for Phase 3C charter)

1. Root + password SSH bootstrap exposed to internet brute-force attempts.  
2. Clock not yet synchronized (`timedatectl`: synchronized=no) while NTP service active.  
3. No host firewall / fail2ban.  
4. Workstation ICMP RTT anomalously low / single-hop traceroute — see network evidence residual.  
5. `resolvectl` unavailable; DNS resolver detail incomplete from allowed commands.  
6. `atop` enabled unexpectedly relative to “marketplace not installed” narrative.  
7. Final inventory / MCA asset ID not assigned.  
8. DNS for `metacode-cloud.com` not configured (by design this wave).  
9. Local secrets `host` field is placeholder (IP lives in `public_ipv4`).

---

## 14. Recommended next step

**PHASE 3C — SERVER B SECURE SSH BOOTSTRAP** (separate charter):

- dedicated operator sudo user  
- MARS-controlled Ed25519 key in local-only secret contour  
- install public key; verify second session + sudo  
- confirm provider emergency console remains available  
- only then disable direct root/password SSH as approved  

**No 3X-UI / Xray / DNS / firewall productization in Phase 3C.**

---

## 15. Related documents

- [SERVER-B-CURRENT-PASSPORT-v1.md](SERVER-B-CURRENT-PASSPORT-v1.md)  
- [SERVER-B-BOOTSTRAP-BASELINE-v1.md](SERVER-B-BOOTSTRAP-BASELINE-v1.md)  
- [SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md](SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md)  
- [../../SECRET-HANDLING-MODEL-v1.md](../../SECRET-HANDLING-MODEL-v1.md)  

---

*Phase 3B · read-only provisioning intake · 2026-08-25 · PASS WITH RESIDUALS.*
