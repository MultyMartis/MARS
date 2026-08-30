# MARS Server Ops — Capability & maturity reconciliation v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **documentation reconciliation** after FriendHosting VPN investigation (2026-08)  
**Not:** product certification, runtime maturity score, or autonomous ops claim  

---

## 1. Overall maturity posture

| Layer | State |
|-------|-------|
| Documentation / doctrines | **Raised** — acceptance, controls, superseded register, FriendHosting asset pack |
| Human-supervised chartered execution | **Demonstrated** |
| Runtime / automation product | **Unchanged / not claimed** |
| Production VPN (generic) | FriendHosting **scoped operational acceptance** only; soak incomplete |
| Forbidden overclaim | No Server Ops Agent product, CMDB, or unattended remediation |

---

## 2. Demonstrated capabilities (evidence-backed)

| Capability | Evidence class |
|------------|----------------|
| Provider research / selection intelligence | AdminVPS / EQVPS / FriendHosting case trail |
| Direct network qualification (assigned IP + known-listener gates) | Intake / AdminVPS rejection / FriendHosting TCP gates |
| Linux VPS intake (read-only → controlled deploy) | Multiple REPORT waves |
| Controlled deployment (3X-UI / Xray / nginx / TLS) | FriendHosting build + P2/P3 |
| SSH hardening (key-only, non-default port, sudo model) | FriendHosting + Server B patterns |
| Firewall (UFW) + fail2ban | P2 PASS |
| ACME / certbot webroot renew path | P2 dry-run PASS |
| Backup planning + hash-verified twin archive | Final operational backup PASS |
| Restore **procedure** confirmation | Restore runbook CONFIRMED |
| Service regression after change | P2/P3 post gates |
| Real-workload acceptance discipline | Doctrine + FriendHosting / EQVPS contrast |
| Per-device identity lifecycle | P3 + P3.1 |
| Interruption recovery (partial wave → clean reconcile) | P2 interrupted → reconciliation 02 |
| Evidence / REPORT closeout | Programme reports tree |

---

## 3. Explicitly NOT demonstrated (do not claim)

| Non-capability | Note |
|----------------|------|
| Bare-metal disaster restore drill | **NOT YET EXERCISED** |
| Large DB recovery / PostgreSQL HA | Not exercised |
| Docker production orchestration product | Not exercised as Server Ops product |
| Unattended autonomous remediation | Forbidden claim |
| Multi-day soak proof | FriendHosting soak **NOT YET PROVEN** |
| Generic production suitability for arbitrary apps | Not claimed |

---

## 4. Control-node maturity (VPN case)

| Node | Role | Maturity note |
|------|------|---------------|
| VEESP | Positive control | Real-workload PASS (historical/operational) |
| EQVPS | Negative control | Transport PASS / real-workload FAIL; root cause **UNPROVEN** |
| FriendHosting | Independent modern control | **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD**; soak pending |
| AdminVPS Server B | Assigned-IP rejection case | VPN stack ABSENT; provider not globally rejected |

---

## 5. Related

- [SERVER-OPS-AGENT-KNOWLEDGE-v1.md](SERVER-OPS-AGENT-KNOWLEDGE-v1.md)  
- [SERVER-OPS-WIDER-ROADMAP-v1.md](SERVER-OPS-WIDER-ROADMAP-v1.md)  
- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

*Capability/maturity v1 · 2026-08-30.*
