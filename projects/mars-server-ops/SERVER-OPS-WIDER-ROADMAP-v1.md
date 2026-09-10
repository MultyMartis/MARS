# MARS Server Ops — Wider roadmap v1 (post-VPN return)

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **planned roadmap** — no deployment in this documentation wave  
**Principle:** finish FriendHosting knowledge consolidation before adding VPN features; then return Server Ops to reusable non-VPN workloads  

---

## 1. Immediate order

| Priority | Item | Notes |
|----------|------|-------|
| **A0** | Windows Clash Verge / System TUN long soak | Preferred candidate client is Clash Verge; **FINAL SOAK PENDING**. Do not treat as production-final. See [CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md](CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md) |
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

## 3a. Windows VPN client — captured, not executed

| Item | State |
|------|-------|
| Long-duration Clash Verge / Mihomo **System** soak | **FINAL SOAK PENDING** |
| Full migration of required process-based DIRECT rules | Future charter — do **not** adopt Cursor→FriendHosting process rule |
| Review IPv6 runtime vs profile collision | Future charter |
| Optional 3X-UI Clash/Mihomo subscription enablement (VEESP / FriendHosting) | Future **mutation** charter; currently `/clash/` not enabled on VEESP |
| AlphaVPS integration into unified Clash profile | Later |
| Decision whether v2rayN can be retired | After soak + process-rule work; keep installed until then |
| Optional cleanup/archive of experimental local `*-ab.yaml` | Only after acceptance; **do not delete now** |

Authority: [CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md](CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md) · closure [reports/WINDOWS-VPN-CLIENT-MIGRATION-CLASH-VERGE-CLOSURE-01.md](reports/WINDOWS-VPN-CLIENT-MIGRATION-CLASH-VERGE-CLOSURE-01.md)

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
- [CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md](CLASH-VERGE-WINDOWS-OPERATOR-BASELINE-v1.md)  
- [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md)  
- [OPERATIONAL-INDEX.md](OPERATIONAL-INDEX.md)

---

*Wider roadmap v1 · planned only · 2026-08-30 · Windows Clash Verge pending 2026-09-11.*
