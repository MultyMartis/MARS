# Server B Phase 3E Final Network Verdict v1

**Status:** **CLOSED FOR DIRECT ENTRY ON CURRENT ASSIGNED IP** — 2026-08-26  
**Wave:** MARS Server Ops Phase **3E3**  
**Planning locus:** `SERVER-B-PLANNING`  
**Public IPv4 in Git:** `<SERVER_B_IP>`  
**Related:** [SERVER-B-DIRECT-NETWORK-GATE-v1.md](SERVER-B-DIRECT-NETWORK-GATE-v1.md) · [SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md](SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md) · [SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md](SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md)  
**Not:** VPN stack, DNS, TLS, 3X-UI, Xray, provider auto-ticket send, Server A work

---

## 1. Final recorded verdict

```text
PRE-PURCHASE FI1 NETWORK:
APPROVED

ACTUAL ASSIGNED SERVER B IP:
DIRECT OPERATOR ISP PATH FAILED

TCP/22 direct:
FAILED

TCP/443 direct:
FAILED

PING direct:
FAILED

DIRECT VPN ENTRY READINESS:
REJECTED FOR CURRENT ASSIGNED IP UNTIL ROUTING/IP ISSUE RESOLVED

SERVER B HOST HEALTH:
PASS

ROOT CAUSE OWNER:
SAFE UNKNOWN
```

Do **not** claim the failure owner is operator ISP, upstream transit, AdminVPS subnet routing, filtering, or geo/network policy without evidence.

Do **not** classify the entire AdminVPS Finland product/provider as failed. Failure scope is:

**current assigned IP / subnet / current operator ISP path** — until further evidence.

---

## 2. Operator final evidence (TUN OFF)

| Check | Result |
|-------|--------|
| Active adapter | Physical Ethernet only |
| Active TUN / Wintun / TAP | **NONE** |
| ping | **FAILED** |
| traceroute | Did **not** reach destination (prior evidence) |
| TCP/22 direct | **FALSE** |
| TCP/443 direct | **FALSE** |

---

## 3. Concurrent host facts (PASS)

| Fact | State |
|------|-------|
| Server B alive | **YES** |
| SSH via operator existing VPN path | **WORKS** (`marsops` + Ed25519) |
| SSH/22 via known-working path | **PASS** |
| Temporary SSH/443 via known-working path (Phase 3E2) | **PASS** (then removed in 3E3) |
| UFW / fail2ban / security baseline | **HEALTHY** |
| Application stack | **ABSENT** |

---

## 4. Phase 3E3 closure actions (summary)

| Action | Result |
|--------|--------|
| Remove temp SSH/443 drop-ins | **DONE** |
| Remove UFW temp 443 allow | **DONE** |
| Preserve SSH/22 + hardening | **DONE** |
| Rotate `marsops` sudo (precaution) | **DONE** — verified |
| Provider support pack | **CREATED** (operator send only) |

---

## 5. AdminVPS / IP decision state

| Subject | State |
|---------|-------|
| AdminVPS Finland provider | **NOT REJECTED** |
| Current assigned Server B IP | **REJECTED FOR DIRECT OPERATOR ENTRY** |

### Next acceptable resolutions

| ID | Resolution |
|----|------------|
| **A** | Provider fixes routing/filtering and direct retest **PASS** |
| **B** | Provider changes public IPv4 and direct retest **PASS** |
| **C** | Provider migrates to another Finland subnet/DC path and direct retest **PASS** |
| **D** | If provider cannot resolve — reopen provider shortlist |

**Do not** automatically order another VPS.  
**Do not** automatically delete this VPS.

---

## 6. Residuals (unchanged this phase)

| Residual | State |
|----------|-------|
| linux-generic / image / headers **6.8.0-138** kept back | **PRESERVED** (priority = network/provider) |
| NTP synchronization flag | **RESIDUAL**; clock accuracy **ACCEPTABLE** |
| Final MCA asset ID | **NOT ASSIGNED** |

---

## 7. Forbidden until direct gate PASS

3X-UI · Xray · VLESS · Reality · WebSocket · TLS certificate · nginx · Docker · MTProto · DNS A/AAAA for this IP · Phase 4A

---

## 8. Next step

```text
OPERATOR → ADMINVPS SUPPORT NETWORK/ROUTING CASE
Then: provider response → IP replace or route fix → repeat TUN-OFF direct test
Only after PASS → Phase 4A
```

---

*Phase 3E final network verdict · current assigned IP rejected for direct entry · provider not rejected · no secrets in Git.*
