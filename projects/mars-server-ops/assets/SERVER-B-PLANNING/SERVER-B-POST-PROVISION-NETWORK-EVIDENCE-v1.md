# Server B Post-Provision Network Evidence v1

**Status:** **RECORDED** — 2026-08-25 · Phase 3E gate still open  
**Wave:** MARS Server Ops Phase 3B (metrics) · **Phase 3E (direct gate pending)**  
**Target:** newly provisioned Server B (`SERVER-B-PLANNING`)  
**Public IPv4 in Git:** `<SERVER_B_IP>`  
**Not:** throughput benchmark, iperf run, DNS cutover, or provider-panel mutation

---

## 1. Scope

Workstation → **actual** Server B public IPv4 validation after provisioning.

Pre-purchase FI1 iperf evidence (~87–92 Mbit/s) remains historical and is **not** repeated here.

**iperf against Server B:** **DEFERRED** (no temporary server install allowed in Phase 3B).

---

## 2. Live host network (read-only SSH)

| Check | Result | Class |
|-------|--------|-------|
| Interface | `eth0` UP (altnames `enp0s3` / `ens3`) | **PRESENT** |
| IPv4 | `<SERVER_B_IP>/24` DHCP metric 100 | **PRESENT** |
| IPv6 | link-local only on eth0; lo `::1` | **PRESENT** / no global IPv6 |
| Default route | DHCP default via provider gateway on eth0 | **PRESENT** |
| Extra routes | host routes toward `1.1.1.1` and `8.8.8.8` via gateway (DHCP) | **PRESENT** |
| `ss -tulpn` | TCP `*:22` sshd; UDP DHCP `:68` | **PRESENT** |
| Unexpected app listeners | none observed | **MATCH** (clean baseline) |
| `resolvectl status` | exit non-zero; empty capture; `systemd-resolved.service` disabled in unit list | **SAFE UNKNOWN** (resolver detail) |

---

## 3. Workstation tests (Windows)

Commands (sanitized):

```text
ping <SERVER_B_IP> -n 20
tracert <SERVER_B_IP>
Test-NetConnection <SERVER_B_IP> -Port 22
```

### 3.1 Ping

| Metric | Value |
|--------|-------|
| Sent | 20 |
| Received | 20 |
| Lost | 0 (0%) |
| min | 0 ms |
| avg | 0 ms |
| max | 6 ms |
| TTL observed | 64 |

### 3.2 Traceroute

| Observation | Value |
|-------------|-------|
| Hops to destination | **1** (destination answered as hop 1) |
| Hop-1 RTT samples | &lt;1 ms |

### 3.3 TCP/22

| Check | Result |
|-------|--------|
| `Test-NetConnection` TcpTestSucceeded | **True** |
| `Test-NetConnection` PingSucceeded | **False** (inconsistent with `ping.exe` success) |
| Live SSH session | **True** (paramiko auth success) |

---

## 4. Classification

| Item | Class |
|------|-------|
| Host reachable for SSH | **PASS** |
| TCP/22 from workstation | **PASS** |
| ICMP reachability | **PASS** via `ping.exe` / **CHANGED** signal vs TNC PingSucceeded=False |
| Path realism vs Finland expectation | **NOT ACCEPTED as direct-route proof** — see §4.1 |
| Throughput | **NOT CHECKED** (iperf deferred) |
| DNS for `metacode-cloud.com` | **NOT CHECKED** / intentionally not mutated |

### 4.1 POST-PROVISION DIRECT NETWORK VALIDATION — RETEST REQUIRED WITH TUN OFF

Phase 3B workstation metrics (**0–6 ms**, **1-hop traceroute**) must **not** be treated as valid proof of direct Russia → Finland latency.

Operator context (Phase 3C correction): the current Xray/V2Ray **TUN** workflow had been re-enabled after pre-purchase testing. Post-provision low RTT / single-hop observations are therefore **likely TUN/VPN-distorted**.

| Decision | State |
|----------|-------|
| Accept Phase 3B 0–6 ms / 1-hop as direct-route proof | **NO** |
| Direct retest with operator TUN **OFF** | **WAITING FOR OPERATOR** — Phase 3E. Script not executed from Cursor (connectivity / TUN-distortion risk). |

Operator script:

`X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-DIRECT-NETWORK-TEST.ps1`

Gate: [SERVER-B-DIRECT-NETWORK-GATE-v1.md](SERVER-B-DIRECT-NETWORK-GATE-v1.md)

```text
PowerShell -ExecutionPolicy Bypass -File "X:\AI MARS\projects\mars-server-ops\assets\SERVER-B-PLANNING\SERVER-B-DIRECT-NETWORK-TEST.ps1" -ServerIp "<SERVER_B_IP>"
```

```text
PRE-PURCHASE FI1 = APPROVED
ACTUAL SERVER B DIRECT ROUTE = WAITING FOR OPERATOR TUN-OFF TEST
```

---

## 5. Relation to pre-purchase evidence

| Evidence | Role |
|----------|------|
| [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md) | Pre-purchase FI1 / provider network case — **PASS** |
| This document | Post-assign IP validation — SSH/TCP gate **PASS**; **direct latency proof pending TUN OFF retest** |

---

## 6. Provider port policy

Live retrieval (Phase 3D): [SERVER-B-PROVIDER-PORT-POLICY-v1.md](SERVER-B-PROVIDER-PORT-POLICY-v1.md)

Source: https://my.adminvps.ru/knowledgebase/561/zablokirovannye-porty-na-usluge-vps.html (2026-08-25)

Historical caution: do not select TCP 8444 without live confirmation. Current page does **not** list 8444 as blocked — still re-verify before VPN port assignment.

---

*Post-provision network evidence · Phase 3B record + Phase 3E TUN-OFF gate pending · IP sanitized as &lt;SERVER_B_IP&gt;.*
