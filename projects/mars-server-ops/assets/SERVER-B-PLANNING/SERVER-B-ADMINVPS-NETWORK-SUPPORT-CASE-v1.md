# Server B — AdminVPS Network Support Case Pack v1

**Status:** **OPERATOR READY — DO NOT AUTO-SEND** — 2026-08-26  
**Wave:** MARS Server Ops Phase **3E3**  
**Audience:** Operator copy/paste to AdminVPS support  
**Public IPv4 in Git:** `<SERVER_B_IP>` (fill from local secrets when sending)  
**Not:** automatic ticket submission · destructive reinstall request · Server A work

---

## 1. How to use

1. Replace `<SERVER_B_IP>` with the assigned public IPv4 from local secrets.  
2. Optionally fill `<OPERATOR_PUBLIC_IP>` / `<OPERATOR_ASN>` if known; otherwise ask support to request/capture source from their side.  
3. Paste the **sanitized summary** below into AdminVPS support.  
4. Preserve the current VM until an operator decision after provider response.

---

## 2. Sanitized summary (copy/paste)

```text
Subject: Finland VPS — assigned IPv4 not reachable from operator ISP (direct path)

Service: AdminVPS Finland VPS (Helsinki / FI1 preferred network context).

Issue:
The VPS itself is alive and fully reachable for management over an alternate VPN-mediated path.
Direct connectivity from the operator’s ISP path (TUN/proxy off; physical Ethernet only) fails.

Observed from operator workstation (direct / TUN OFF):
- ICMP ping to assigned public IPv4: FAIL
- TCP/22 to assigned public IPv4: FAIL
- TCP/443 to assigned public IPv4: FAIL (temporary diagnostic SSH listener was confirmed working via the alternate VPN path, then removed)
- Traceroute: does not reach the destination

Host-side checks (via working alternate path):
- SSH on TCP/22 works (key-only operator user)
- Temporary SSH on TCP/443 also worked via the alternate path during diagnosis
- Host firewall allows SSH; security baseline healthy
- Guest OS: Ubuntu 24.04; hostname present; no application VPN stack installed yet

Please check:
1) Routing / filtering / reachability for the assigned IPv4 and its subnet toward the operator ISP/AS path
2) Whether any provider-side filter would drop ICMP and TCP/22+TCP/443 from external consumer ISPs
3) Whether you can correct routing/filtering so direct reachability is restored

If routing cannot be corrected, please advise whether you can:
- replace the assigned public IPv4, and/or
- migrate the VM to another Finland subnet / DC path

Constraints:
- Do not perform a destructive reinstall unless we explicitly request it later
- Please preserve the current VM until we confirm next steps

Operator source identity (if needed):
- Operator public source IP: <OPERATOR_PUBLIC_IP>   [UNKNOWN in MARS docs — fill or capture server-side]
- Operator ASN / ISP: <OPERATOR_ASN>                 [UNKNOWN in MARS docs — fill or capture server-side]
- Assigned VPS IPv4: <SERVER_B_IP>
```

---

## 3. Evidence notes (internal; not required in ticket)

| Item | State |
|------|-------|
| Pre-purchase FI1 network | **APPROVED** (reference) |
| Actual assigned IP direct path | **FAILED** |
| Host health via alternate path | **PASS** |
| Root cause owner | **SAFE UNKNOWN** |
| Temporary SSH/443 | Deployed Phase 3E2; **removed** Phase 3E3 |
| Application stack | **ABSENT** |
| DNS | **Unchanged** |

Full verdict: [SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md](SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md)

---

## 4. Provider decision framing (internal)

| Subject | State |
|---------|-------|
| AdminVPS Finland provider | **NOT REJECTED** |
| Current assigned IP | **REJECTED FOR DIRECT OPERATOR ENTRY** |

Acceptable outcomes: route/filter fix · IPv4 replace · Finland subnet/DC migrate · else reopen shortlist.

---

*AdminVPS network support case pack · operator send only · no secrets in Git.*
