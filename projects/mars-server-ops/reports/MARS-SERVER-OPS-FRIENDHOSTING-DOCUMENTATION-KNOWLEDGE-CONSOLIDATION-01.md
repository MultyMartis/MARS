# REPORT — FriendHosting Documentation + Knowledge Consolidation 01

**Programme:** MARS Server Ops & VPS Forge  
**Wave:** FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01  
**Date:** 2026-08-30  
**Mode:** DOCUMENTATION / KNOWLEDGE / REGISTRY only  
**Target:** FRIENDHOSTING-DE / FriendHosting / `92.42.99.126` / `metacode-cloud.com`  

**Mutations this wave:** FriendHosting = **0** · VEESP = **0** · EQVPS = **0** · secret disclosure = **0** · foreign WIP = **0** · commit/push = **0**

---

## 1. Executive verdict

**FRIENDHOSTING DOCUMENTATION + KNOWLEDGE CONSOLIDATION: PASS**

FriendHosting is reconciled from scattered reports into a canonical asset pack, updated doctrines, inventory/lifecycle promotion to **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD**, operator runbooks, and reusable Server Ops knowledge — **without** live server mutation and **without** claiming `PRODUCTION_ACCEPTED` or long-term soak.

| Gate | Result |
|------|--------|
| Canonical current truth | **PASS** |
| Architecture document | **PASS** |
| Port/service map | **PASS** |
| Access / security / identities / TLS / backup state | **PASS** |
| 3X-UI operator runbook | **PASS** |
| Doctrines + superseded register | **PASS** |
| Agent knowledge + maturity + wider roadmap | **PASS** |
| Inventory + OPERATIONAL-INDEX | **PASS** |
| P4 `:24443` created | **NO** (correctly DEFERRED) |
| Long-term soak proven | **NO** (honest) |

---

## 2. Source authority

Hierarchy applied:

`AGENTS.md` / `.cursorrules` → X-drive governance → programme OPERATIONAL-INDEX → current reports/evidence → historical handoffs.

Conflicts: newer reproducible evidence wins; stale claims marked **SUPERSEDED** (SC-007 update, SC-011, SC-012).

---

## 3. Final FriendHosting current truth

Canonical record:

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-CURRENT-TRUTH-v1.md`

Summary: FRIENDHOSTING-DE · FriendHosting DE · `92.42.99.126` · `metacode-cloud.com` · Ubuntu 24.04.4 · 2 vCPU / ~1.9 GiB / 20 GiB / 2 GiB swap · 3X-UI 3.7.0 · Xray 26.7.28 · VLESS TLS RAW `:8443` · six per-device identities · legacy retired · transport/real-workload PASS · soak NOT YET PROVEN.

---

## 4. Final architecture

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-ARCHITECTURE-v1.md`

Paths documented:

1. Client → v2rayN/TUN → `metacode-cloud.com:8443` → Xray → Internet  
2. Operator browser → `:443` nginx → localhost 3X-UI `:20901`  
3. Let's Encrypt HTTP-01 `:80` → nginx webroot → certbot → hook → nginx + Xray consumers  

---

## 5. Hardware/network baseline

| Item | Value |
|------|-------|
| vCPU / RAM / disk / swap | 2 / ~1.9 GiB / 20 GiB / 2 GiB |
| Prefix / ASN | `92.42.99.0/24` / AS47447 |
| SSH | `:3333` |
| VPN | `:8443` |
| Panel front | `:443` |
| ACME | `:80` |

---

## 6. Port/service map

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md`

Classes: PUBLIC REQUIRED / PUBLIC NARROW / LOCALHOST / DENIED / DEFERRED.  
`:2096` = DENIED / **ACCEPTED HARDENED BOUNDARY**.  
`:24443` = DEFERRED.

---

## 7. Access model

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-ACCESS-MODEL-v1.md`

SSH: marsops key + sudo; password auth off; root key recovery retained.  
3X-UI: nginx `:443` + secret path (local only); panel localhost.  
VPN mgmt: 3X-UI preferred UX; local files = backup/registry.

---

## 8. Security posture

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md`

Covers SSH, UFW, fail2ban, TLS, swap, logging, updates, backup, secrets, residuals (`:2096` listener + UFW DENY).

---

## 9. VPN architecture

VLESS + TLS + RAW/TCP `:8443` · SNI `metacode-cloud.com` · flow empty · sniffing OFF · inbound remark `FRIENDHOSTING-DE-RAW-8443`.

---

## 10. Per-device identities

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-DEVICE-IDENTITY-MODEL-v1.md`

| Label | Status |
|-------|--------|
| WSP-ONE / MCA-PHONE | physically PASS |
| Unit-01/02/03 / Unit-MichaelPhone | SERVER_IDENTITY_READY · DEVICE_TEST_PENDING |
| MCA-ONE-… | RETIRED / REMOVED FROM SERVER |

Revoke/rotate: `runbooks/FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md`

---

## 11. 3X-UI operator UX

`X:\AI MARS\projects\mars-server-ops\runbooks\FRIENDHOSTING-3XUI-OPERATOR-RUNBOOK-v1.md`

Based on actual 3.7.0 P3 behaviour: open panel → inbound → client → native QR/copy-link; create/revoke/rotate; no `:2096` exposure; local files not primary UX.

---

## 12. TLS/ACME lifecycle

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-TLS-ACME-LIFECYCLE-v1.md`

Let's Encrypt · HTTP-01 webroot · `:80` · certbot.timer · dry-run PASS · hook consumers · incident paths for near-expiry / dry-run fail / hook fail / nginx / Xray reload regressions · monitoring requirement stated.

---

## 13. Backup/restore state

`X:\AI MARS\projects\mars-server-ops\assets\FRIENDHOSTING-DE\FRIENDHOSTING-DE-BACKUP-RESTORE-STATE-v1.md`

| Field | Value |
|-------|-------|
| Remote | `/root/mars-backups/friendhosting-final-operational-20260830T125003Z.tgz` |
| Local | `X:\AI MARS\local\infrastructure\FRIENDHOSTING-GERMANY\backups\friendhosting-final-operational-20260830T125003Z.tgz` |
| Size | 80746687 |
| SHA-256 | `1012e3157db97ea3ba2a1c4d0b8d02328223e6656adf12ade22fa1adbb3a0ea2` |
| Match / readability | PASS |
| Restore procedure | CONFIRMED (`runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md`) |
| Bare-metal | NOT YET EXERCISED |

**BACKUP VERIFIED ≠ FULL DISASTER RESTORE TESTED** — also added to BACKUP-RESTORE-MODEL-v1.

---

## 14. Operational acceptance / lifecycle

Taxonomy extended in REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1 with:

`OPERATIONALLY_ACCEPTED_CURRENT_VPN_WORKLOAD`

FriendHosting promoted to that state. Still **not** `PRODUCTION_ACCEPTED`. Control role retained. SC-011 records supersession of “candidate-only forever after gates” framing.

---

## 15. Long-term soak status

**NOT YET PROVEN**

---

## 16. EQVPS diagnostic reconciliation

| Exact root cause | **UNPROVEN** |
|------------------|--------------|
| VEESP | real workloads PASS |
| FriendHosting | same general client/Xray/RAW class · real workloads PASS |
| EQVPS | transport PASS · real workloads FAIL |

**Strongly weakened:** generic Windows / v2rayN / TUN / Xray 26.7.28 / VLESS+TLS+RAW / generic Goodline inability.  
**Strengthened domain:** EQVPS endpoint/IP/prefix/Hetzner-HEL/path/application interaction.  
**Do not overclaim** exact mechanism.

---

## 17. AdminVPS / provider lessons

Provider doctrine + network preflight updated:

```text
looking-glass PASS ≠ assigned IP/subnet PASS
```

AdminVPS Finland remains canonical negative lesson for assigned-IP rejection.  
FriendHosting shows independent provider/ASN + assigned-IP validation + known-listener TCP + real-workload acceptance value.

---

## 18. Real-workload doctrine

Acceptance ladder preserved and expanded; EQVPS = negative case; FriendHosting = independent positive case. Agents must not collapse PING→PRODUCTION.

---

## 19. Anti-config-churn doctrine

CONTROL-EVIDENCE-METHODOLOGY-v1 reinforced: healthy transport + failing apps ⇒ classify + controls + single-variable A/B — not Reality/WS/gRPC/MTU/BBR roulette.

---

## 20. Server Ops Agent knowledge update

**YES**

Created: `X:\AI MARS\projects\mars-server-ops\SERVER-OPS-AGENT-KNOWLEDGE-v1.md`

Reusable lifecycle:

REQUIREMENTS → PREFLIGHT → PROVIDER/CAPACITY → BACKUP/ROLLBACK → DEPLOY → TECHNICAL VALIDATION → REAL-WORKLOAD ACCEPTANCE → HARDEN → BACKUP → DOCUMENT → MONITOR → RECOVER

Mechanism is **documentation knowledge**, not an autonomous agent system.

---

## 21. Capability / maturity update

**YES**

Created: `X:\AI MARS\projects\mars-server-ops\SERVER-OPS-CAPABILITY-MATURITY-v1.md`

**Safe summary:** documentation + human-supervised chartered execution maturity **raised**; runtime/automation product **unchanged/not claimed**; demonstrated VPN-adjacent ops capabilities listed; bare-metal DR / DB HA / Docker product / unattended remediation **not** claimed.

---

## 22. Wider Server Ops roadmap

Created: `X:\AI MARS\projects\mars-server-ops\SERVER-OPS-WIDER-ROADMAP-v1.md`

Order: **A** soak/monitoring → **B** optional P4 `:24443` → **C** first non-VPN workload.  
**Recommended C:** Docker service deployment (lab/chartered). Alternatives: PostgreSQL, n8n host, reverse-proxy app, bare-metal DR drill. **None deployed this wave.**

---

## 23. FriendHosting future roadmap

| Item | State |
|------|-------|
| P4 `:24443` | **DEFERRED** (not cancelled) |
| Before P4 | Documentation consolidation **closed** |
| After P4 | WSP-ONE reserve test; same per-device model; keep `:8443` primary |
| Bare-metal restore | Future optional high-value DR wave |
| Next ops | Soak / lightweight monitoring |

---

## 24. Canonical files created/updated

### Created

| Path |
|------|
| `assets/FRIENDHOSTING-DE/README.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-CURRENT-TRUTH-v1.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-ARCHITECTURE-v1.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-PORT-SERVICE-MAP-v1.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-ACCESS-MODEL-v1.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-SECURITY-POSTURE-v1.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-DEVICE-IDENTITY-MODEL-v1.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-TLS-ACME-LIFECYCLE-v1.md` |
| `assets/FRIENDHOSTING-DE/FRIENDHOSTING-DE-BACKUP-RESTORE-STATE-v1.md` |
| `runbooks/FRIENDHOSTING-3XUI-OPERATOR-RUNBOOK-v1.md` |
| `SERVER-OPS-AGENT-KNOWLEDGE-v1.md` |
| `SERVER-OPS-CAPABILITY-MATURITY-v1.md` |
| `SERVER-OPS-WIDER-ROADMAP-v1.md` |
| `reports/MARS-SERVER-OPS-FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01.md` |

### Updated

| Path |
|------|
| `OPERATIONAL-INDEX.md` |
| `SERVER-INVENTORY-v1.md` |
| `REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md` |
| `CONTROL-EVIDENCE-METHODOLOGY-v1.md` |
| `SUPERSEDED-CONCLUSIONS-REGISTER-v1.md` |
| `BACKUP-RESTORE-MODEL-v1.md` |
| `VPS-PROVIDER-SELECTION-RUNBOOK-v1.md` |
| `VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md` |
| `runbooks/FRIENDHOSTING-DEVICE-VLESS-IDENTITY-REVOCATION-ROTATION-v1.md` |

---

## 25. Remaining unknowns

| Unknown | Note |
|---------|------|
| Long-term soak | NOT YET PROVEN |
| Bare-metal DR | NOT YET EXERCISED |
| Exact EQVPS root cause | UNPROVEN |
| Unit-* physical acceptance | DEVICE_TEST_PENDING |
| Exact FriendHosting panel SKU numbers | NOT YET PERSISTED |
| P4 reserve behaviour | NOT DEPLOYED |
| Monitoring automation | NOT IMPLEMENTED |

---

## 26. Git closeout

| Item | Status |
|------|--------|
| Branch | `mars/canonical-post-recovery` |
| Volume | `X:` / `AI WS` |
| Workspace | `X:\AI MARS` |
| Commit | **0** |
| Push | **0** |
| Broad git add | **0** |
| Foreign WIP | Present elsewhere — **out of scope** · not staged · not mutated |
| Unpushed commits (pre-existing) | Noted; **not altered** |
| Server mutations | **0** |

**STOP.** Next action requires a **separate charter** (recommended: FriendHosting soak / lightweight monitoring; wider Docker lab only after VPN soak priority clarified by operator).

---

*End of report · documentation consolidation 01 · 2026-08-30.*
