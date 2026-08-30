# MARS Server Ops — Wider roadmap v1 (post-VPN return)

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **planned roadmap** — no deployment in this documentation wave  
**Principle:** finish FriendHosting knowledge consolidation before adding VPN features; then return Server Ops to reusable non-VPN workloads  

---

## 1. Immediate order

| Priority | Item | Notes |
|----------|------|-------|
| **A** | FriendHosting soak + lightweight monitoring | Multi-day real-workload stability; cert expiry awareness; basic health checks — **charter required** |
| **B** | Optional P4 reserve `:24443` | DEFERRED — after soak/docs; same per-device model; keep `:8443` primary; no transport churn |
| **C** | First non-VPN reusable workload | Pick one from §2 |

---

## 2. Recommended first non-VPN workload

**Recommendation:** **Docker service deployment** on a chartered lab/non-prod host (or explicitly scoped FriendHosting capacity review first).

| Why Docker first | Reason |
|------------------|--------|
| Reuses | Linux intake, firewall, TLS/reverse-proxy patterns |
| Avoids | Premature PostgreSQL HA / MetaBOT production coupling |
| Teaches | Image pin, compose, backup of volumes, rollback |

**Alternatives (any may be chosen by charter):**

- PostgreSQL service for a named MARS project (passport + backup/restore first)  
- n8n operational node (host-level only; workflow ownership stays MetaBOT)  
- Reverse-proxy / app deployment (non-VPN)  
- Full bare-metal restore exercise on FriendHosting (high-value DR)

Do **not** deploy any of these without a separate charter.

---

## 3. FriendHosting-specific future

| Item | State |
|------|-------|
| P4 VLESS TLS RAW `:24443` | **DEFERRED** (not cancelled) |
| Before P4 | Documentation consolidation **closed** (this wave) |
| After P4 | Test WSP-ONE reserve profile; same per-device model; preserve `:8443` |
| Bare-metal restore drill | Optional high-value DR wave |
| Unit-* device physical tests | Ops residual |

---

## 4. Lifecycle reminder

```text
REQUIREMENTS → PREFLIGHT → PROVIDER/CAPACITY → BACKUP/ROLLBACK → DEPLOY
→ TECHNICAL VALIDATION → REAL-WORKLOAD ACCEPTANCE → HARDEN → BACKUP
→ DOCUMENT → MONITOR → RECOVER
```

---

## 5. Related

- [SERVER-OPS-AGENT-KNOWLEDGE-v1.md](SERVER-OPS-AGENT-KNOWLEDGE-v1.md)  
- [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md)  
- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

*Wider roadmap v1 · planned only · 2026-08-30.*
