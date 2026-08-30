# Server B Firewall Baseline v1

**Status:** **ACTIVE** — updated Phase **3E3** 2026-08-26  
**Wave:** MARS Server Ops Phase 3D (+ 3E2 temp 443; **3E3 cleanup**)  
**Tool:** UFW (Ubuntu package `ufw` 0.36.2-6)  
**Not:** application/VPN port openings, provider panel firewall, or Server A changes

---

## 1. Policy target

| Direction | Policy |
|-----------|--------|
| Default incoming | **deny** |
| Default outgoing | **allow** |
| Routed | disabled |

### Public inbound allowlist (final Phase 3E3)

| Port | Proto | Comment | State |
|------|-------|---------|-------|
| 22 | tcp | MARS SSH | **ALLOW** |
| 443 | tcp | MARS TEMP SSH DIRECT TEST | **REMOVED** (Phase 3E3) |

**Not opened for application:** 80, 3X-UI panel, Reality, WebSocket, subscription, or other VPN ports.

---

## 2. Activation safety (Phase 3D — historical)

| Step | Result |
|------|--------|
| `marsops` key session held | **PASS** |
| Second independent keepalive SSH | **PASS** |
| `ufw allow 22/tcp comment 'MARS SSH'` before enable | **PASS** |
| `ufw --force enable` | **PASS** |
| Fresh session after enable | **PASS** |

---

## 3. Live status (post–Phase 3E3 cleanup)

```text
Status: active
Default: deny (incoming), allow (outgoing), disabled (routed)
22/tcp ALLOW IN Anywhere                   # MARS SSH
22/tcp (v6) ALLOW IN Anywhere (v6)         # MARS SSH
```

`IPV6=yes` in `/etc/default/ufw`. No global IPv6 address observed on the host — v6 rules present for readiness only; kernel IPv6 **not** disabled.

**Expected public allow:** **22/tcp only**.

---

## 4. Explicit non-goals

- No 3X-UI / Xray / nginx ports  
- No provider console firewall mutation  
- No Server A firewall work  

---

*Firewall baseline · UFW active · SSH 22 only inbound (public).*
