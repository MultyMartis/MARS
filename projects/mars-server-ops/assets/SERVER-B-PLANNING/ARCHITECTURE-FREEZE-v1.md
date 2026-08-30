# Server B Architecture Freeze v1

**Status:** **ARCHITECTURE DECISION APPROVED** — **NOT YET IMPLEMENTED**  
**Wave:** MARS Server Ops Phase 3A  
**Server B existence:** **NOT PROVISIONED**  
**Provider binding (current):** [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) — **AdminVPS** Finland / Helsinki  
**Historical provider (superseded):** [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) — UpCloud

---

## 1. Server role

| Field | Decision |
|-------|----------|
| **Role** | Independent secondary production VPN node |
| **Dependency on Server A** | **NONE** — separate failure domain |
| **Server A during build** | **UNTOUCHED** — no mutation during Server B construction |
| **Provider (current)** | AdminVPS — Finland / Helsinki (FI1 preferred tested network) |

---

## 2. Transport decisions

### Server A Reality — corrected classification

Do **not** classify Server A Reality as broken.

| Aspect | Classification |
|--------|----------------|
| **Reality inbound** | **PRESENT** |
| **Server-side listener** | **PRESENT** (live intake 2026-08-25 — port 46489, `MCA-Gate-Reality`) |
| **Client connectivity** | **NOT VERIFIED** |
| **Troubleshooting state** | **REQUIRED LATER** |
| **Root cause** | **SAFE UNKNOWN** |

Possible causes (configuration/client mismatch, network behaviour, etc.) are **not proven** in this wave. **No diagnosis** in Phase 3A.

### Server B — initial transport profile

| Priority | Transport | Role |
|----------|-----------|------|
| **PRIMARY INITIAL / PROVEN COMPATIBILITY** | VLESS + TLS + WebSocket | Initial Server B transport — confirmed working for operator on Server A |
| **SECONDARY / VALIDATION** | VLESS + Reality | Configured **independently** on Server B; tested **separately** after initial build |

**Reality on Server B:** Must not be classified as deprecated, failed, blocked, or preferred until **actual Server B tests** exist.

---

## 3. nginx decision

| Field | Decision |
|-------|----------|
| **nginx in initial Server B architecture** | **NOT INCLUDED** |
| **Reason** | Server A proves VLESS + TLS + WebSocket can operate directly through Xray **without** nginx |
| **Future WS/TLS/nginx masking** | Separate optional Server Ops project/node — **not** part of this wave |

Do **not** create nginx implementation plans in Phase 3A.

---

## 4. Software baseline

| Component | Intended baseline |
|-----------|-------------------|
| **OS** | Ubuntu 24.04 LTS |
| **3X-UI** | Current stable version — **re-verify immediately before installation** |
| **Xray** | Version bundled/recommended by chosen current stable 3X-UI release, unless Phase 3 implementation research identifies a blocker |
| **Database** | SQLite for 3X-UI initially |
| **Docker** | **Not required** for core Server B VPN stack |
| **MTProto** | **Not part** of initial Server B scope |

### Version discipline

Do **not** hard-code a future binary version (3X-UI, Xray) as immutable truth — versions are time-sensitive.

At implementation time:

1. Re-verify current stable 3X-UI release.  
2. Confirm compatible Xray version for that release.  
3. Record verified versions in implementation evidence — not as pre-provisioned guarantees.

---

## 5. Deployment model

| Field | Decision |
|-------|----------|
| **3X-UI supervision** | Native / systemd |
| **Xray management** | Through compatible 3X-UI installation |
| **Client failover (initial)** | **Manual** profile switching — Server A profile / Server B profile |
| **Automatic failover** | **Not** in initial implementation |

---

## 6. SSH / security baseline (target — not executed)

Planning target only — **no execution** in Phase 3A:

| Step | Target |
|------|--------|
| Bootstrap access | Provider-supported initial method |
| Operator user | Dedicated operator sudo user |
| SSH keys | Ed25519 key authentication |
| Validation | Verify key login; verify sudo; verify **provider** emergency console access |
| Hardening (after validation) | Disable direct root SSH login; disable SSH password authentication |

### Firewall target

| Rule | Target |
|------|--------|
| Default inbound | Deny |
| Allowed services | Explicitly required only |
| IPv4 / IPv6 | Handled intentionally |
| fail2ban | Enabled |
| Provider firewall | May be added later as second layer after host-level smoke tests |

Exact production port numbers: **not defined** in this freeze except where generated during build.

---

## 7. Backup / recovery baseline

Server B requires three layers:

| Layer | Scope |
|-------|-------|
| **Layer 1** | Provider backup / snapshot (AdminVPS — confirm available features at checkout) |
| **Layer 2** | Server Ops application/config backup |
| **Layer 3** | MARS off-server backup under Storage |

MARS backup artifacts must include:

- manifest  
- exact scope  
- timestamp  
- versions  
- checksum  
- sensitivity classification  
- restore procedure  

**Programme rule:** A backup is not operationally complete until a **restore strategy** exists.

**Later:** Isolated restore rehearsal before claiming **DR PROVEN**.

See [../../BACKUP-RESTORE-MODEL-v1.md](../../BACKUP-RESTORE-MODEL-v1.md) and [../../STORAGE-MODEL-v1.md](../../STORAGE-MODEL-v1.md).

---

## 8. Client strategy

| Field | Decision |
|-------|----------|
| **Initial mode** | Manual switching between profiles |
| **Profile A** | Server A (MCA-VPN-001) |
| **Profile B** | Server B (new — independent credentials) |
| **Server A client profiles** | **Do not modify** during this documentation wave |

See [../MCA-VPN-001/CLIENT-COMPATIBILITY-v1.md](../MCA-VPN-001/CLIENT-COMPATIBILITY-v1.md).

---

## 9. Identity independence

All Server B secrets and identities must be **new and independent** of Server A.

Checklist (fields only): [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md)

**No secret values in Git.**

---

## 10. Implementation gate

This freeze **does not** authorize:

- Provider API calls  
- VPS creation  
- SSH access  
- DNS changes  
- Package installation  
- 3X-UI / Xray configuration  

Implementation requires a **separate explicit implementation charter** after provisioning intake.

---

## 11. Related documents

- [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) — **current** procurement
- [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) — **SUPERSEDED** UpCloud
- [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md)
- [PROVISIONING-INTAKE-CHECKLIST-v1.md](PROVISIONING-INTAKE-CHECKLIST-v1.md)
- [../MCA-VPN-001/SERVER-A-CURRENT-PASSPORT-v1.md](../MCA-VPN-001/SERVER-A-CURRENT-PASSPORT-v1.md)

---

*Architecture Freeze v1 · Phase 3A · planning only · not implemented.*
