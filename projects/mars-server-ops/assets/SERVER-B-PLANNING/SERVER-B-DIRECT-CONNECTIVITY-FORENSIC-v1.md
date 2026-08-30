# Server B Direct Connectivity Forensic v1 — Phase 3E2 / closed 3E3

**Status:** **CLOSED** — 2026-08-26  
**Wave:** MARS Server Ops Phase **3E2** (deploy) → **3E3** (operator FAIL + cleanup)  
**Verdict:** dual direct FAIL (TCP/22 + TCP/443); temporary SSH/443 **REMOVED**; current assigned IP **REJECTED** for direct entry  
**Public IPv4 in Git:** `<SERVER_B_IP>`  
**Final verdict:** [SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md](SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md)  
**Not:** application stack, VPN deploy, DNS change, Server A work, permanent SSH port migration

---

## 1. Purpose

Distinguish why the operator **direct ISP path with TUN OFF** cannot reach the assigned Server B IP on TCP/22 / ICMP / TCP/443, while Server B remains **alive** via the operator’s existing VPN-mediated SSH path.

Primary hypotheses (still unresolved):

| ID | Hypothesis |
|----|------------|
| **A** | Operator ISP/path specifically filters **TCP/22** and/or **ICMP** (and possibly 443) |
| **B** | Operator ISP/path cannot reach this particular AdminVPS IP/subnet |
| **C** | Other route/provider filtering |

**Root cause owner after Phase 3E3:** **SAFE UNKNOWN**

---

## 2. Direct TUN-OFF failure evidence (operator-observed)

| Check | Result |
|-------|--------|
| Active adapter | Physical Ethernet only |
| Active TUN / Wintun / TAP | **NONE** |
| `ping` | **FAILED** |
| traceroute | Entered ISP/private network; **did not reach destination** |
| `Test-NetConnection` TCP/22 | **FALSE** |
| `Test-NetConnection` TCP/443 | **FALSE** (final operator evidence) |

---

## 3. Why the VPS is not classified failed

| Fact | State |
|------|-------|
| Server B SSH via existing VPN path | **WORKS** (`marsops` + Ed25519) |
| Controlled reboot survival (Phase 3E) | **PASS** |
| `sshd` active on 22 | **YES** |
| Temporary SSH/443 via known-working path (3E2) | **PASS** |
| UFW allows TCP/22 | **YES** |
| fail2ban active (sshd) | **YES** |
| Application stack | **ABSENT** |

**Classification:**

```text
ACTUAL SERVER B DIRECT NETWORK GATE = FAILED (CURRENT ASSIGNED IP)
SERVER B HOST HEALTH = PASS
ROOT CAUSE OWNER = SAFE UNKNOWN
VPS / PROVIDER PRODUCT = NOT CLASSIFIED FAILED
```

---

## 4. Provider TCP/443 policy check

Source: [SERVER-B-PROVIDER-PORT-POLICY-v1.md](SERVER-B-PROVIDER-PORT-POLICY-v1.md) (AdminVPS KB 2026-08-25).

| Port | Listed as provider-blocked for Finland VPS? |
|------|-----------------------------------------------|
| TCP/443 inbound | **NO** |
| TCP/22 outbound (Finland) | YES (outbound only — not relevant to inbound SSH) |

Temporary SSH/443 was **authorized** for forensic use in 3E2.

---

## 5. Temporary SSH/443 diagnostic (historical) + 3E3 cleanup

### Deployed in Phase 3E2

| Path | Role |
|------|------|
| `/etc/ssh/sshd_config.d/00-mars-server-ops-hardening.conf` | **PRESERVED** — auth + `Port 22` |
| `/etc/ssh/sshd_config.d/01-mars-server-ops-direct-connectivity-test.conf` | Temporary `Port 443` |
| `/etc/systemd/system/ssh.socket.d/01-mars-server-ops-direct-connectivity-test.conf` | Temporary `ListenStream` 443 |

Validation via known-working path: SSH/22 **PASS**; SSH/443 **PASS**.

### Removed in Phase 3E3

| Item | State |
|------|-------|
| Temporary sshd drop-in | **REMOVED** |
| Temporary ssh.socket drop-in | **REMOVED** |
| UFW `443/tcp` TEMP rule | **REMOVED** |
| Listeners after cleanup | **22 only** |
| Hardening drop-in | **PRESERVED** |

---

## 6. Temporary UFW (final)

| Rule | Comment | State |
|------|---------|-------|
| 22/tcp ALLOW | MARS SSH | **PRESERVED** |
| 443/tcp ALLOW | MARS TEMP SSH DIRECT TEST | **REMOVED** |
| Default incoming | deny | **PRESERVED** |
| Default outgoing | allow | **PRESERVED** |

---

## 7. Application stack

| Component | State |
|-----------|-------|
| 3X-UI / Xray / VLESS / Reality / WS | **ABSENT** |
| nginx / Docker / TLS certs | **ABSENT** |
| DNS mutation | **NONE** |

---

## 8. Interpretation matrix (applied)

| TCP/443 direct | TCP/22 direct | Classification |
|----------------|---------------|----------------|
| **FALSE** | **FALSE** | DIRECT CURRENT-ISP REACHABILITY TO ASSIGNED SERVER B IP/SUBNET = **FAILED** — hard blocker for this Server B as operator direct VPN entry until resolved. |

---

## 9. Server mutations

**Phase 3E2:** temporary SSH/443 + UFW 443 allow.  
**Phase 3E3:** remove those only; sudo password rotation (precaution); docs + support pack.

**Server A:** **NONE**

---

## 10. Root cause state

```text
ROOT CAUSE OWNER = SAFE UNKNOWN
CURRENT ASSIGNED IP = REJECTED FOR DIRECT OPERATOR ENTRY
ADMINVPS FINLAND PROVIDER = NOT REJECTED
NEXT = OPERATOR → ADMINVPS NETWORK/ROUTING SUPPORT CASE
```

---

*Direct connectivity forensic · Phase 3E2 deploy + 3E3 close · temp SSH/443 removed · IP sanitized as &lt;SERVER_B_IP&gt; · no secrets in Git.*
