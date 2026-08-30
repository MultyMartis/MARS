# Network Topology v1 — MCA-VPN-001

**Status:** **LIVE RECONCILIATION 2026-08-25** — read-only intake; operator review before mutation  
**Critical correction:** **nginx is NOT installed** and is **NOT** in the Server A traffic path.

**Evidence:** [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md) · [SERVER-A-CURRENT-PASSPORT-v1.md](SERVER-A-CURRENT-PASSPORT-v1.md)

---

## 1. Last-known VPN data path (Server A)

```
VPN Client
    |
    | encrypted VPN connection
    v
wsp-cloud.com / <SERVER_IP>  (Server A — MCA-VPN-001)
    |
    v
Xray / 3X-UI managed inbound
    |
    | VLESS — two live inbounds:
    |   • port 8443 — TLS + WebSocket (MCA-Gate-TLS)  [LIVE — CHANGED vs legacy "no WS on A"]
    |   • port 46489 — Reality (MCA-Gate-Reality)
    v
Xray
    |
    v
Internet
```

**Classification:** **LIVE VERIFIED** direction — inbound ports and protocols from read-only intake 2026-08-25.

**Explicitly NOT on Server A (live):**

- nginx as reverse proxy in VPN path — **not installed**
- Separate "Web Mask" node — still **PLANNED / NOT IMPLEMENTED**

**Live addition (non-VPN path):**

- Docker MTProto proxy — host port **8445** → container :443 (`telegrammessenger/proxy:latest`)

---

## 2. Management path (3X-UI panel)

```
Browser
    |
    | HTTPS :5928  (known-good after repair — LEGACY LAST-KNOWN)
    v
wsp-cloud.com
    |
    v
3X-UI built-in web server
    |
    v
<3XUI_PANEL_PATH>  (secret — not in Git)
```

**Note:** During incident, transitional listeners on **443** and **2096** were observed — **CONFIRMED HISTORICAL** incident state, not documented as current topology.

---

## 3. nginx / WS / TLS — future separate node (NOT Server A)

**Operator decision (PLANNED / NOT IMPLEMENTED — HIGH confidence):**

Future **WS + TLS + nginx** masking contour was intended for a **separate dedicated VPS**, not retrofit onto Server A or the n8n VPS.

Conceptual future mask path (not current):

```
Client → domain → nginx → TLS → WebSocket → Xray → ...
```

**MARS must not import nginx as a confirmed-current component of MCA-VPN-001.**

---

## 4. Infrastructure separation map

| Node | Role | Relationship to Server A |
|------|------|------------------------|
| **Server A (MCA-VPN-001)** | Existing production VPN | This document |
| **Server B** | Planned independent second VPN | No dependency A→B; separate failure domain |
| **Web Mask node** | Future WS/TLS/nginx if justified | Independent; not merged with A |
| **n8n VPS** | Existing automation host (separate VEESP VPS) | **Separate asset** — do not conflate |

```
                    ┌─────────────┐     ┌─────────────┐
                    │  Server A   │     │  Server B   │
                    │  (legacy)   │     │  (planned)  │
                    └──────┬──────┘     └──────┬──────┘
                           │                   │
                           └─────────┬─────────┘
                                     v
                                 Internet

     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
     │  n8n VPS    │     │ Web Mask    │     │ GEO nodes   │
     │ (separate)  │     │ (future)    │     │ (planned)   │
     └─────────────┘     └─────────────┘     └─────────────┘
```

**No shared:** DB, private keys, certificates, credentials, filesystem, control plane between A and B.

---

## 5. Ports (live + legacy)

| Port | Live observation (2026-08-25) | Tag |
|------|------------------------------|-----|
| 5928/TCP | 3X-UI panel HTTPS | **LIVE MATCH** |
| 2096/TCP | x-ui subscription listener | **LIVE PRESENT** |
| 8443/TCP | xray VLESS + WebSocket (`MCA-Gate-TLS`) | **LIVE PRESENT** |
| 46489/TCP | xray VLESS + Reality (`MCA-Gate-Reality`) | **LIVE PRESENT** |
| 8445/TCP | Docker MTProto proxy | **LIVE PRESENT** |
| 22/TCP | SSH/SFTP administration | **LIVE MATCH** |
| 443/TCP | Observed during historical incident only | CONFIRMED HISTORICAL — **not primary live panel path** |

---

## 6. Multi-region resilience (planning only)

Discussed conceptual map — **not purchased / not deployed:**

| Role | Location |
|------|----------|
| MAIN | Finland / Netherlands |
| WEB MASK | France |
| GEO FALLBACK | UAE / Serbia (UAE preferred first) |

Uzbekistan / Tajikistan noted as exploratory alternatives only.

---

## Related documents

- [VPN-RUNTIME-LEGACY-v1.md](VPN-RUNTIME-LEGACY-v1.md)
- [SERVER-B-CLONE-BASELINE-v1.md](SERVER-B-CLONE-BASELINE-v1.md)

---

*Network Topology v1 · live intake 2026-08-25 · nginx not on Server A · WS on 8443 is live fact.*
