# MCA-VPN-001 — Server A Legacy VPN VPS

**Asset reference:** `MCA-VPN-001`  
**Human label:** Server A — Current Legacy VPN VPS  
**Provider:** VEESP  
**Purpose:** Dedicated production VPN VPS (3X-UI / Xray / VLESS-Reality direction)

**Documentation maturity:** Legacy knowledge imported (Phase 1B-0); Phase 1B-1 read-only live intake **completed 2026-08-25 — PASS WITH GAPS**  
**Current authority status:** **LIVE + SYSTEM SECURITY HARDENING 01 APPLIED (2026-08-30)** — see [SERVER-A-CURRENT-PASSPORT-v1.md](SERVER-A-CURRENT-PASSPORT-v1.md) · [SECURITY-POSTURE-v1.md](SECURITY-POSTURE-v1.md)  
Legacy passport remains historical reference; gaps listed in [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md).

---

## Source provenance

| Item | Value |
|------|-------|
| **Primary source** | Legacy Web-GPT chat *WS + TLS + nginx* |
| **Handoff file (Storage)** | `X:\AI MARS STORAGE\incoming\MARS-SERVER-OPS-LEGACY-VPN-FULL-HANDOFF.md` |
| **Git archive copy** | [legacy/WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md](legacy/WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md) |
| **Classification** | Sanitized historical handoff — **no live-state authority** |
| **Import wave** | MARS Server Ops Phase 1B-0 |

---

## Relationship to other infrastructure

| Entity | Relationship |
|--------|--------------|
| **Server B** | **Planned** independent second VPN VPS — not built; see [SERVER-B-CLONE-BASELINE-v1.md](SERVER-B-CLONE-BASELINE-v1.md) |
| **n8n VPS** | **Separate** existing VEESP VPS for n8n/automation — **must not** be conflated with MCA-VPN-001 |
| **Web Mask (WS/TLS/nginx)** | **Future** independent node — **not** current Server A traffic path |
| **ATLAS** | **No** ATLAS ID registered — `MCA-VPN-001` is legacy managed-asset reference only |

---

## Live verification status

| Check | Status |
|-------|--------|
| Read-only live intake | **COMPLETE 2026-08-25 — PASS WITH GAPS** — [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md) |
| Provider panel reconciliation | **PENDING** |
| 3X-UI semver verification | **SAFE UNKNOWN** |
| Backup integrity (checksum / tar -tf) | **NOT CHECKED** |
| Full disaster recovery test | **NOT TESTED** (legacy) |

---

## Asset document navigation

| Document | Role |
|----------|------|
| [README.md](README.md) | This index |
| [SERVER-A-LEGACY-PASSPORT-v1.md](SERVER-A-LEGACY-PASSPORT-v1.md) | Normalized legacy passport |
| [SERVER-A-CURRENT-PASSPORT-v1.md](SERVER-A-CURRENT-PASSPORT-v1.md) | Live passport — read-only intake 2026-08-25 |
| [LIVE-INTAKE-EVIDENCE-v1.md](LIVE-INTAKE-EVIDENCE-v1.md) | Phase 1B-1 session evidence |
| [CURRENT-STATE-RECONCILIATION-v1.md](CURRENT-STATE-RECONCILIATION-v1.md) | Live vs legacy comparison template |
| [NETWORK-TOPOLOGY-v1.md](NETWORK-TOPOLOGY-v1.md) | Last-known traffic topology |
| [VPN-RUNTIME-LEGACY-v1.md](VPN-RUNTIME-LEGACY-v1.md) | 3X-UI / Xray runtime facts |
| [CLIENT-COMPATIBILITY-v1.md](CLIENT-COMPATIBILITY-v1.md) | Client-side compatibility notes |
| [BACKUP-STATE-v1.md](BACKUP-STATE-v1.md) | Backup scope and verified twins |
| [SECURITY-POSTURE-v1.md](SECURITY-POSTURE-v1.md) | SSH / UFW / fail2ban / swap / logging posture |
| [FILESYSTEM-MAP-v1.md](FILESYSTEM-MAP-v1.md) | Known paths and sensitivity |
| [RECOVERY-STATE-v1.md](RECOVERY-STATE-v1.md) | Proven vs unproven recovery |
| [INCIDENT-HISTORY-v1.md](INCIDENT-HISTORY-v1.md) | Operational incidents and lessons |
| [KNOWN-GOOD-PROCEDURES-v1.md](KNOWN-GOOD-PROCEDURES-v1.md) | Historical procedure catalog (not authorization) |
| [SERVER-B-CLONE-BASELINE-v1.md](SERVER-B-CLONE-BASELINE-v1.md) | Server B planning bridge |
| [RESEARCH-BACKLOG-v1.md](RESEARCH-BACKLOG-v1.md) | Time-sensitive research items |
| [LIVE-INTAKE-CHECKLIST-v1.md](LIVE-INTAKE-CHECKLIST-v1.md) | Read-only intake checklist |
| [legacy/WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md](legacy/WS-TLS-NGINX-LEGACY-VPN-FULL-HANDOFF.md) | Complete sanitized source archive |

---

## Programme links

- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md)
- [SERVER-INVENTORY-v1.md](../../SERVER-INVENTORY-v1.md)

---

*MCA-VPN-001 · live baseline 2026-08-25 · operator review required before Server A mutation.*
