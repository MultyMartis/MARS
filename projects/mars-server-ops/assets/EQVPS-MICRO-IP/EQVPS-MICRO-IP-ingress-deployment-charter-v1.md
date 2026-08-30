# EQVPS-MICRO-IP — Ingress Deployment Charter v1

**Status:** **CHARTER ONLY — NOT EXECUTED**  
**Date:** 2026-08-27  
**Depends on:** [EQVPS-MICRO-IP-dns-binding-ingress-architecture-2026-08-27.md](./EQVPS-MICRO-IP-dns-binding-ingress-architecture-2026-08-27.md)  
**Verdict prerequisite:** architecture wave **READY_FOR_INGRESS_DEPLOYMENT**  
**Target host:** EQVPS Micro-IP · `metacode-cloud` · `95.216.126.173` · Ubuntu 24.04.4 LTS  
**Domain:** `metacode-cloud.com` (Beget; A already bound — **do not** mutate DNS unless cert strategy requires DNS-01 TXT)

**Explicit authorization required before any step below runs.** This document alone is **not** permission to install software.

---

## 0. Hard stops (carry forward)

Do **not** unless this charter is operator-approved and then only as written:

- Touch Server A (MCA-VPN-001)  
- Touch AdminVPS Server B  
- Change Beget A/AAAA/MX/SPF/autoconfig/autodiscover (except temporary DNS-01 TXT if that path is chosen)  
- Change PTR/rDNS  
- Change hostname  
- Open panel/subscription publicly  
- Install nginx / Docker / unrelated stacks  
- `git add .` / commit without separate authorization  

---

## 1. Exact software to install

| Component | Strategy |
|-----------|----------|
| **3X-UI** | Official current **stable** release — **re-verify version on install day** (do not hard-code stale semver from docs) |
| **Xray** | Version **bundled / recommended** by that 3X-UI release |
| **certbot** or 3X-UI ACME helper | Only if needed for LE cert; prefer **DNS-01**; if HTTP-01, certbot standalone on :80 time-boxed |
| **nginx** | **NOT installed** in this charter |
| **Docker** | **NOT installed** in this charter |

Install method: native 3X-UI installer / systemd path consistent with MARS Server Ops practice (not marketplace preinstall images).

Record exact versions in evidence after install.

---

## 2. Primary transport

| Field | Value |
|-------|-------|
| Protocol | **VLESS** |
| Security | **REALITY** |
| Flow | **Vision** if supported by install-time Xray; otherwise document gap |
| Port | **TCP/443** |
| Public bind | `0.0.0.0:443` (and IPv6 only if intentionally enabled) |
| REALITY `dest` / `serverNames` | **External camouflage** — **not** `metacode-cloud.com` |
| Keys / shortIds | **New** — independent from Server A; store only in local secrets / Storage secret contour |

---

## 3. Fallback transport

| Field | Value |
|-------|-------|
| Protocol | **VLESS** |
| Security | **TLS** (real certificate) |
| Network | **XHTTP** (preferred) |
| Port | **TCP/8443** |
| Certificate | LE for `metacode-cloud.com` (+ optional `www` SAN) |
| SNI | `metacode-cloud.com` |

### Compatibility gate

If operator clients (v2rayN / v2rayNG / etc.) fail XHTTP import or tunnel:

1. Document failure evidence.  
2. Switch fallback inbound to **VLESS + TLS + WebSocket** on **8443** (Server A–proven family).  
3. Do **not** run conflicting dual TLS inbounds on the same port without an explicit redesign charter.

---

## 4. Exact ports (end-state)

| Port | Action |
|------|--------|
| 22/tcp | Keep UFW allow (SSH) |
| 443/tcp | UFW allow **after** Reality inbound listening |
| 8443/tcp | UFW allow **after** TLS inbound + cert ready |
| 80/tcp | Temporary allow **only** for HTTP-01; remove immediately after cert success |
| Panel | `127.0.0.1:<chosen>` — **no UFW publish** |
| Subscription | `127.0.0.1:<chosen>` — **no UFW publish** initially |

---

## 5. Exact domain usage

| Use | Value |
|-----|-------|
| Cert CN/SAN | `metacode-cloud.com` (± `www`) |
| TLS fallback SNI | `metacode-cloud.com` |
| Ops reference | apex A → `95.216.126.173` (already true) |
| Reality camouflage | **External** targets only |
| New DNS records this charter | **None** unless DNS-01 TXT required (temporary) |

---

## 6. Exact UFW changes (sequence)

1. Confirm baseline: default deny in / allow out; **22/tcp only**.  
2. If HTTP-01: `allow 80/tcp` with comment `MARS TEMP ACME HTTP-01` → issue cert → **delete** rule.  
3. Confirm Reality listens on 443 → `allow 443/tcp` comment `MARS VLESS REALITY`.  
4. Confirm TLS+XHTTP listens on 8443 → `allow 8443/tcp` comment `MARS VLESS TLS XHTTP`.  
5. Verify `ufw status verbose` — no panel/subscription ports.  
6. Never leave temp 80 open overnight.

---

## 7. Certificate strategy

| Item | Decision |
|------|----------|
| Required | **YES** before enabling 8443 TLS fallback |
| Preferred challenge | **DNS-01** at Beget (TXT `_acme-challenge`) |
| Alternate | **HTTP-01** on :80 time-boxed **before** Reality binds 443 |
| Avoid | TLS-ALPN-01 on 443 after Reality is live |
| Renewal | Document mechanism (timer/cron/3X-UI) in evidence; test renew dry-run where safe |
| Private keys | Local + Storage only — **never Git** |

---

## 8. Panel access model

| Item | Decision |
|------|----------|
| Bind | `127.0.0.1` |
| Auth | Strong unique password; random `webBasePath` |
| Access | SSH tunnel only |
| TLS for panel | Optional local self-signed or reuse host cert on localhost — operator choice; **not** public |
| fail2ban | Keep sshd jail; do not expose panel to need HTTP jail yet |

---

## 9. Subscription model

| Phase | Model |
|-------|-------|
| Initial | Export profiles from panel / serve subscription via SSH tunnel |
| Later (separate charter) | Optional public TLS subscription on neutral path — not this charter |

Client strategy: **manual** profile switch — Profile EQVPS-REALITY / Profile EQVPS-TLS-XHTTP; Server A profiles **unchanged**.

---

## 10. Pre-change backup (mandatory before install)

1. Provider snapshot if available (confirm EQVPS feature — SAFE UNKNOWN until checked).  
2. Capture: sshd effective config, UFW numbered status, fail2ban status, `dpkg-query -W` bounded list, `ss -lntup`, hostname, IP, kernel.  
3. Write manifest (backup class G) under Storage with restore steps **before** apt/installer runs.  
4. After 3X-UI install + before opening 443/8443: backup 3X-UI DB, Xray config, certs, unit files (classes F/E/A).

---

## 11. Rollback strategy

| Trigger | Action |
|---------|--------|
| Install failure | Stop installer; restore packages/state from checkpoint; keep UFW 22-only |
| Bad inbound | Disable inbound in panel; reload; keep SSH |
| Public exposure mistake | UFW delete 443/8443/80; confirm listeners; rotate any leaked panel path/password |
| Total stack failure | Stop `x-ui`; UFW 22-only; restore DB/config backup; if needed provider snapshot under DR charter |
| Operator connectivity | Fall back to **Server A** profiles (untouched) |

---

## 12. Validation tests (acceptance)

Execute from operator Goodline with **TUN OFF** unless a test explicitly requires TUN ON.

| # | Test | Pass criteria |
|---|------|---------------|
| 1 | Local listener | `ss` shows 443 + 8443 owned by xray/x-ui as designed; panel on 127.0.0.1 only |
| 2 | UFW | Allows exactly 22 + 443 + 8443 (and not 80 after ACME) |
| 3 | Direct TCP 443 | `TcpTestSucceeded=True` on Ethernet |
| 4 | Direct TCP 8443 | Same |
| 5 | DNS | apex/www still `95.216.126.173` (auth + recursive spot-check) |
| 6 | TLS | `openssl s_client` / equivalent to `:8443` shows expected cert for `metacode-cloud.com` |
| 7 | Client import | Reality profile imports; XHTTP (or WS fallback) imports |
| 8 | Client tunnel Reality | Browse / IP check shows EQVPS egress |
| 9 | Client tunnel fallback | Same via 8443 profile |
| 10 | IP/ASN exit | Confirms EQVPS/Helsinki path — not Server A |
| 11 | Latency/speed sanity | Not broken vs baseline RTT (~60 ms class); no hard SLA |
| 12 | TUN ON smoke | Optional secondary; document adapter used |
| 13 | Panel | Reachable **only** via SSH tunnel; **not** from public Internet |
| 14 | Cleanup | No temp ACME listeners; no `/tmp` diagnostic servers; no temp UFW comments left |

---

## 13. Closeout criteria

Wave may close **PASS** only when:

- Primary Reality on 443 works for operator client  
- Fallback TLS+XHTTP (or approved WS alternate) on 8443 works  
- Panel not public  
- UFW minimal allowlist documented  
- Versions + backup manifests filed  
- REPORT written under `assets/EQVPS-MICRO-IP/`  
- Server A untouched  
- No unauthorized DNS permanent changes  

---

## 14. Suggested execution order

1. Preflight (MARS X-volume, branch, foreign WIP preserve).  
2. Pre-install backup + provider snapshot check.  
3. Certificate via DNS-01 (preferred) **or** time-boxed HTTP-01.  
4. Install 3X-UI + bundled Xray; lock panel to localhost.  
5. Configure Reality :443.  
6. Configure TLS+XHTTP :8443 with cert.  
7. UFW allow 443 then 8443.  
8. Client validation matrix.  
9. Post-install secret backup to Storage.  
10. REPORT + residual list.  

**Do not execute this charter in the DNS/architecture wave.**

---

*Ingress Deployment Charter v1 · EQVPS-MICRO-IP · not executed.*
