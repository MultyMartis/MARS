# SERVER-B-PLANNING — Server B Procurement, Architecture & Provisioning Intake

**Planning locus:** `SERVER-B-PLANNING`  
**Final MCA asset ID:** **NOT ASSIGNED** — **PROVISIONED — FINAL ASSET REGISTRATION PENDING**  
**Status:** **PROVISIONED — APPLICATION NOT CONFIGURED** · SSH **KEY-ONLY** (22 only) · UFW/fail2ban **ACTIVE** · Phase 3E reboot **PASS** · Phase **3E3** direct IP **REJECTED** for operator entry · temp SSH/443 **REMOVED** (2026-08-26)  
**Provider (current):** **AdminVPS** — Finland / Helsinki / FI1 preferred — provider **NOT REJECTED**; current assigned IP **REJECTED** for direct entry  
**Wave:** MARS Server Ops Phase 3A → 3B → 3C → 3D → 3E → 3E2 → **3E3**

---

## Purpose

Record operator-approved Server B procurement, architecture freeze, and **post-provision read-only intake** facts.

This folder remains the **planning / intake locus** until an authoritative asset-ID procedure assigns a permanent MCA/internal inventory ref. **Do not invent** ATLAS/MCA IDs here.

---

## Relationship to Server A

| Entity | Relationship |
|--------|--------------|
| **Server A (MCA-VPN-001)** | Existing production VPN — **remains untouched** during Server B construction |
| **Server B** | Independent secondary production VPN node — **provisioned**, application stack **not** installed |
| **Failure domain** | Server B must **not** depend on Server A |

Planning bridge (conceptual): [../MCA-VPN-001/SERVER-B-CLONE-BASELINE-v1.md](../MCA-VPN-001/SERVER-B-CLONE-BASELINE-v1.md)

---

## Document navigation

| Document | Role |
|----------|------|
| [README.md](README.md) | This index |
| [SERVER-B-PROVISIONING-INTAKE-v1.md](SERVER-B-PROVISIONING-INTAKE-v1.md) | **Phase 3B** live read-only intake + verdict |
| [SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md](SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md) | **Phase 3C** secure SSH bootstrap evidence |
| [SERVER-B-BASE-OS-SECURITY-v1.md](SERVER-B-BASE-OS-SECURITY-v1.md) | **Phase 3D** base OS security + network baseline |
| [SERVER-B-CONTROLLED-REBOOT-v1.md](SERVER-B-CONTROLLED-REBOOT-v1.md) | **Phase 3E** controlled reboot evidence |
| [SERVER-B-DIRECT-NETWORK-GATE-v1.md](SERVER-B-DIRECT-NETWORK-GATE-v1.md) | **Phase 3E/3E3** direct TUN-OFF network gate — current IP **REJECTED** |
| [SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md](SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md) | **Phase 3E2→3E3** forensic + temp SSH/443 removed |
| [SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md](SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md) | **Phase 3E3** final direct network verdict |
| [SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md](SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md) | Operator copy/paste AdminVPS support pack |
| [SERVER-B-FIREWALL-BASELINE-v1.md](SERVER-B-FIREWALL-BASELINE-v1.md) | UFW baseline |
| [SERVER-B-FAIL2BAN-BASELINE-v1.md](SERVER-B-FAIL2BAN-BASELINE-v1.md) | fail2ban sshd jail |
| [SERVER-B-TIME-DNS-BASELINE-v1.md](SERVER-B-TIME-DNS-BASELINE-v1.md) | NTP residual + DNS resolver path |
| [SERVER-B-PROVIDER-PORT-POLICY-v1.md](SERVER-B-PROVIDER-PORT-POLICY-v1.md) | AdminVPS blocked ports (2026-08-25) |
| [SERVER-B-DIRECT-NETWORK-TEST.ps1](SERVER-B-DIRECT-NETWORK-TEST.ps1) | Operator TUN-OFF network retest script |
| [SERVER-B-SSH-ACCESS-MODEL-v1.md](SERVER-B-SSH-ACCESS-MODEL-v1.md) | Key-only remote access model |
| [SERVER-B-SSH-ROLLBACK-v1.md](SERVER-B-SSH-ROLLBACK-v1.md) | Managed drop-in rollback |
| [SERVER-B-CURRENT-PASSPORT-v1.md](SERVER-B-CURRENT-PASSPORT-v1.md) | Live passport (sanitized) |
| [SERVER-B-BOOTSTRAP-BASELINE-v1.md](SERVER-B-BOOTSTRAP-BASELINE-v1.md) | Bootstrap + Phase 3C SSH delta |
| [SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md](SERVER-B-POST-PROVISION-NETWORK-EVIDENCE-v1.md) | Workstation → assigned IP evidence (TUN caveat) |
| [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) | AdminVPS Finland procurement decision |
| [SERVER-B-PROVIDER-SELECTION-CASE-v1.md](SERVER-B-PROVIDER-SELECTION-CASE-v1.md) | Provider selection case study |
| [SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md](SERVER-B-NETWORK-PREFLIGHT-EVIDENCE-v1.md) | Pre-purchase network evidence |
| [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) | **SUPERSEDED** — historical UpCloud decision (retained) |
| [ARCHITECTURE-FREEZE-v1.md](ARCHITECTURE-FREEZE-v1.md) | Initial Server B architecture decisions |
| [IDENTITY-AND-SECRETS-CHECKLIST-v1.md](IDENTITY-AND-SECRETS-CHECKLIST-v1.md) | Independent identity/secret fields — **no values in Git** |
| [PROVISIONING-INTAKE-CHECKLIST-v1.md](PROVISIONING-INTAKE-CHECKLIST-v1.md) | Checklist template (pre/post facts) |

### Generic Server Ops capability

| Document | Role |
|----------|------|
| [../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](../../VPS-PROVIDER-SELECTION-RUNBOOK-v1.md) | Canonical selection workflow |
| [../../VPS-PROCUREMENT-GATE-v1.md](../../VPS-PROCUREMENT-GATE-v1.md) | Procurement gate |
| [../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](../../VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md) | Network preflight procedure |

---

## Lifecycle state

```text
PROVISIONED — FINAL ASSET REGISTRATION PENDING
PROVISIONED — APPLICATION NOT CONFIGURED
Phase 3B intake: PASS WITH RESIDUALS (2026-08-25)
Phase 3C SSH: PASS WITH RESIDUALS (2026-08-25) — KEY-ONLY REMOTE ACCESS
Phase 3D base OS security: PASS WITH RESIDUALS (2026-08-25) — UFW + fail2ban ACTIVE
Phase 3E controlled reboot: PASS (2026-08-25)
Phase 3E/3E3 direct path: FAILED (ping/22/443 TUN-OFF) — current IP REJECTED for direct entry
Root cause owner: SAFE UNKNOWN
Phase 3E2 temp SSH/443: REMOVED (Phase 3E3)
AdminVPS Finland provider: NOT REJECTED
Next: OPERATOR → AdminVPS network/routing support case
Provider: AdminVPS / Finland / Helsinki (FI1 preferred)
```

| Historical | Current |
|------------|---------|
| UpCloud / FI-HEL1 — [PROCUREMENT-DECISION-v1.md](PROCUREMENT-DECISION-v1.md) | **SUPERSEDED** |
| AdminVPS / Finland — [SERVER-B-PROVIDER-DECISION-v2.md](SERVER-B-PROVIDER-DECISION-v2.md) | **PROCURED** |
| Phase 3B live intake | [SERVER-B-PROVISIONING-INTAKE-v1.md](SERVER-B-PROVISIONING-INTAKE-v1.md) |

Domain registered: `metacode-cloud.com` — **no DNS mutation** until a later controlled charter.

---

## Secret boundary

| Layer | Path |
|-------|------|
| **Git (this folder)** | Sanitized facts, `secret_ref` pointers only |
| **Local-only** | `X:\AI MARS\local\infrastructure\SERVER-B-PLANNING\secrets.local.md` |
| **Storage** | `X:\AI MARS STORAGE\mars-server-ops\` — backups, exports, evidence |

Future approved build charters may authorize MARS/Cursor to **generate** secrets and write them **only** to the local-only contour. See [../../SECRET-HANDLING-MODEL-v1.md](../../SECRET-HANDLING-MODEL-v1.md).

---

## Next operator action

1. Open AdminVPS support using [SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md](SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md) (do not auto-send from agents).  
2. After provider route fix / IPv4 replace / Finland subnet migrate — repeat TUN-OFF direct retest (`Test-NetConnection` TCP/22 and TCP/443).  
3. Only after direct path **PASS** return to Phase 4A charter.  
4. Keep Server A untouched.  
5. Do **not** install 3X-UI / Xray / mutate DNS A/AAAA while current assigned IP remains rejected for direct entry.  
6. Do **not** automatically order or delete this VPS.

---

## Programme links

- [OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md)
- [SERVER-INVENTORY-v1.md](../../SERVER-INVENTORY-v1.md)
- [SERVER-OPS-CHARTER-v1.md](../../SERVER-OPS-CHARTER-v1.md)

---

*SERVER-B-PLANNING · AdminVPS Finland · provisioned · Phase 3E3 · current IP rejected for direct entry · provider not rejected · no secrets in Git.*
