# Server B Direct Network Gate v1

**Status:** **CLOSED — CURRENT ASSIGNED IP REJECTED FOR DIRECT ENTRY** — 2026-08-26  
**Wave:** MARS Server Ops Phase 3E / **3E3**  
**Verdict:** **REJECTED** for direct operator VPN entry on current assigned IP/subnet/ISP path  
**Planning locus:** `SERVER-B-PLANNING`  
**Public IPv4 in Git:** `<SERVER_B_IP>`  
**Final verdict:** [SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md](SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md)  
**Support pack:** [SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md](SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md)  
**Related forensic:** [SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md](SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md)  
**Not:** iperf3 server install, VPN port assignment, DNS cutover, or application stack

---

## 1. Purpose

Issue an **ACCEPT / REJECT** verdict for the **actual assigned** Server B IPv4 over the operator ISP path with:

- v2rayN / Xray **TUN = OFF**
- Windows system proxy that would intercept PowerShell ICMP/TCP tests **OFF**

Cursor **must not** disable the operator VPN automatically.

---

## 2. Why this gate exists

Phase 3B workstation metrics (0–6 ms, 1-hop traceroute) are **not** accepted as direct Russia → Finland proof. They were likely TUN-distorted. See [SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md](SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md).

Pre-purchase FI1 evidence remains **reference only** ([SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md)):

| Pre-purchase FI1 | Value |
|------------------|-------|
| Ping average | approximately **71 ms** |
| Packet loss | **0%** |
| iperf | approximately **87–92 Mbit/s** |
| Physical Ethernet | **100 Mbps** |
| Classification | **APPROVED** (pre-purchase network) |

The assigned VM may use a different subnet/path. Do **not** require identical RTT.

---

## 3. Operator-observed direct failure (final)

With TUN OFF / physical Ethernet / no active TUN/Wintun/TAP:

| Check | Result |
|-------|--------|
| ping | **FAILED** |
| traceroute | ISP/private path; **destination not reached** |
| `Test-NetConnection` TCP/22 | **FALSE** |
| `Test-NetConnection` TCP/443 | **FALSE** |

Server B itself remains **alive** via alternate (VPN-mediated) SSH path. **Do not** classify the VPS or entire AdminVPS Finland product as failed.  
**Root cause owner:** **SAFE UNKNOWN**.

---

## 4. Final gate state (Phase 3E3)

| Item | State |
|------|-------|
| Pre-purchase FI1 network | **APPROVED** |
| Actual assigned IP direct path | **FAILED** |
| TCP/22 direct | **FAILED** |
| TCP/443 direct | **FAILED** |
| Ping direct | **FAILED** |
| Direct VPN entry readiness | **REJECTED** for current assigned IP until routing/IP resolved |
| Temporary SSH/443 | **REMOVED** (Phase 3E3) |
| Host health (alternate path) | **PASS** |
| AdminVPS Finland provider | **NOT REJECTED** |
| Root cause owner | **SAFE UNKNOWN** |

```text
PRE-PURCHASE FI1 NETWORK = APPROVED
ACTUAL ASSIGNED SERVER B IP = DIRECT OPERATOR ISP PATH FAILED
TCP/22 direct = FAILED
TCP/443 direct = FAILED
PING direct = FAILED
DIRECT VPN ENTRY READINESS = REJECTED FOR CURRENT ASSIGNED IP UNTIL ROUTING/IP ISSUE RESOLVED
```

---

## 5. Acceptance matrix (applied)

| TCP/443 direct | TCP/22 direct | Gate implication |
|----------------|---------------|------------------|
| FALSE | FALSE | Direct ISP reachability to assigned IP/subnet **FAILED** — hard blocker for application stack on this IP |

Exact filter/route attribution without evidence: **forbidden**.

---

## 6. Provider escalation

Operator action: use [SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md](SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md).

Acceptable resolutions: route/filter fix · IPv4 replace · Finland subnet/DC migrate · else reopen shortlist.

**Do not** start Phase 4A until a new TUN-OFF direct retest **PASS**.

---

## 7. Provider port policy

[SERVER-B-PROVIDER-PORT-POLICY-v1.md](SERVER-B-PROVIDER-PORT-POLICY-v1.md) — TCP/443 **not** documented as provider-blocked. Temporary SSH/443 was forensic only and is **gone**.

---

*Direct network gate · Phase 3E3 · current assigned IP rejected for direct entry · provider not rejected · IP sanitized as &lt;SERVER_B_IP&gt;.*
