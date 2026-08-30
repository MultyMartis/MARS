# MARS Server Ops & VPS Forge — Operational Index

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **documented** navigation only — **not** a service registry, automated router, SSH connector, or VPS control plane.  
**Lane:** B — External Infrastructure (Human-Supervised)  
**Domain root:** this programme folder  
**Maturity:** **documentation-first** — human-supervised external infrastructure operations

---

## 1. Identity

| Field | Value |
|-------|-------|
| **Canonical name** | MARS Server Ops & VPS Forge |
| **Working folder** | `projects/mars-server-ops/` |
| **Purpose** | Human-supervised documentation, schemas, runbooks, and controlled procedures for external server infrastructure (VPS, Linux, VPN, Docker, n8n host, databases, reverse proxy, backups) |
| **Execution model** | Web-GPT → Cursor/Codex → **Human approval** |
| **Implementation** | **NOT STARTED** — no SSH fleet, no Docker deploy automation, no monitoring agents, no autonomous runtime |
| **Registry row** | **NONE** — no `project_id` assigned in this wave (see Phase 0 decision) |
| **ATLAS binding** | **NONE** — optional later documentation relationship only |

**Mandatory formulation:**

```text
Git documents and governs procedure.
External servers execute outside Git.
No live server is owned by the repository.
```

---

## 2. Current active phase

| Phase | Status | Scope |
|-------|--------|-------|
| **Phase 0** | **COMPLETE** (evidence review) | Programme placement, boundary decisions, authority reuse |
| **Phase 1A** | **COMPLETE** | Programme foundation — charter, schemas, templates, boundaries |
| **Phase 1B-0** | **COMPLETE** | Legacy VPN knowledge import — MCA-VPN-001 (Server A) |
| **Phase 1B-1** | **COMPLETE** (2026-08-25) | Server A live read-only intake — [LIVE-INTAKE-EVIDENCE-v1.md](assets/MCA-VPN-001/LIVE-INTAKE-EVIDENCE-v1.md) |
| **Phase 2A** | **SUPERSEDED for procurement** | Historical UpCloud / FI-HEL1 approval — eligibility conflict; see Provider Selection Intelligence |
| **Phase 2B** | **ARCHITECTURE DECISION APPROVED** | Server B initial transport, nginx exclusion, software baseline — [ARCHITECTURE-FREEZE-v1.md](assets/SERVER-B-PLANNING/ARCHITECTURE-FREEZE-v1.md) |
| **Phase 3A** | **COMPLETE** (procurement) | Procurement + identity prep — [SERVER-B-PLANNING](assets/SERVER-B-PLANNING/README.md) |
| **Phase 3B** | **COMPLETE** (2026-08-25) | Server B actual provisioning intake (read-only) — [SERVER-B-PROVISIONING-INTAKE-v1.md](assets/SERVER-B-PLANNING/SERVER-B-PROVISIONING-INTAKE-v1.md) — **PASS WITH RESIDUALS** |
| **VPS Provider Selection Intelligence** | **BASELINE v1 CREATED** | Reusable Stages 0–11 + gates — [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md) |
| **Phase 3C** | **COMPLETE** (2026-08-25) | Server B secure SSH bootstrap — [SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md](assets/SERVER-B-PLANNING/SERVER-B-SECURE-SSH-BOOTSTRAP-v1.md) — **PASS WITH RESIDUALS**; **KEY-ONLY** remote access |
| **Phase 3D** | **COMPLETE** (2026-08-25) | Server B base OS security + network baseline — [SERVER-B-BASE-OS-SECURITY-v1.md](assets/SERVER-B-PLANNING/SERVER-B-BASE-OS-SECURITY-v1.md) — **PASS WITH RESIDUALS**; UFW + fail2ban **ACTIVE** |
| **Phase 3E** | **PASS** reboot (2026-08-25); direct TCP/22 TUN-OFF **FAILED** | Controlled reboot — [SERVER-B-CONTROLLED-REBOOT-v1.md](assets/SERVER-B-PLANNING/SERVER-B-CONTROLLED-REBOOT-v1.md); direct gate — [SERVER-B-DIRECT-NETWORK-GATE-v1.md](assets/SERVER-B-PLANNING/SERVER-B-DIRECT-NETWORK-GATE-v1.md) |
| **Phase 3E2** | **CLOSED via 3E3** (2026-08-26) | Temporary SSH/443 forensic deployed then removed — [SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md](assets/SERVER-B-PLANNING/SERVER-B-DIRECT-CONNECTIVITY-FORENSIC-v1.md) |
| **Phase 3E3** | **COMPLETE** (2026-08-26) | Direct IP rejection + temp SSH cleanup + sudo rotation — [SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md](assets/SERVER-B-PLANNING/SERVER-B-PHASE-3E-FINAL-NETWORK-VERDICT-v1.md); support pack — [SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md](assets/SERVER-B-PLANNING/SERVER-B-ADMINVPS-NETWORK-SUPPORT-CASE-v1.md) |
| **Phase 4A+ (AdminVPS)** | **DEFERRED** | Domain / TLS / VPN stack on AdminVPS — only after assigned IP path **ACCEPTED** and explicit charter |
| **VPN Case Study Closeout 01** | **COMPLETE** (2026-08-30) | Knowledge consolidation — [MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md](reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md) |
| **FriendHosting Plus recon 01** | **SUPERSEDED for CPU/RAM** (2026-08-30) | Pre-panel-reboot guest still Start-class — [PLUS-POST-UPGRADE-RECONCILIATION-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-PLUS-POST-UPGRADE-RECONCILIATION-01.md) |
| **FriendHosting Plus panel reboot gate 01** | **COMPLETE** (2026-08-30) | CPU/RAM **PASS** (2 vCPU / ~1.9Gi); disk then still 10 GiB — [PLUS-CONTROL-PANEL-REBOOT-GATE-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-PLUS-CONTROL-PANEL-REBOOT-GATE-01.md) |
| **FriendHosting Plus disk expansion 01** | **COMPLETE** (2026-08-30) | CASE **A** auto-expanded; `/dev/sda` **20 GiB**; services/VPN **PASS** — [PLUS-DISK-EXPANSION-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-PLUS-DISK-EXPANSION-01.md) |
| **FriendHosting P2 operational hardening 01** | **PARTIAL** historical (2026-08-30) | Interrupted Cursor run recovered; TLS renew dry-run then **FAIL** — [P2-OPERATIONAL-HARDENING-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-P2-OPERATIONAL-HARDENING-01.md) |
| **FriendHosting P2 clean hardening reconciliation 02** | **PASS** (2026-08-30) | Live re-audit over VEESP control path; fresh backup; ACME webroot `:80`; `certbot renew --dry-run` **PASS**; SSH/UFW/fail2ban/swap preserved — [P2-CLEAN-HARDENING-RECONCILIATION-02](reports/MARS-SERVER-OPS-FRIENDHOSTING-P2-CLEAN-HARDENING-RECONCILIATION-02.md) |
| **FriendHosting P3 per-device VLESS identities 01** | **SERVER MODEL PASS** (2026-08-30) | Six NEW + legacy then present; 3X-UI UX PASS — [P3-PER-DEVICE-VLESS-IDENTITIES-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-PER-DEVICE-VLESS-IDENTITIES-01.md) |
| **FriendHosting P3.1 legacy retirement closeout 01** | **PASS / CLOSED** (2026-08-30) | Deleted exact legacy `MCA-ONE-FRIENDHOSTING-DE-RAW-8443`; **6** clients remain; WSP-ONE/MCA-PHONE PASS; Unit-* DEVICE_TEST_PENDING — [P3-LEGACY-RETIREMENT-CLOSEOUT-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-P3-LEGACY-RETIREMENT-CLOSEOUT-01.md) |
| **FriendHosting final operational backup 01** | **PASS** (2026-08-30) | Freeze post–Plus/P2/P3; remote+local twin SHA match; restore procedure CONFIRMED; bare-metal NOT YET EXERCISED — [FINAL-OPERATIONAL-BACKUP-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-FINAL-OPERATIONAL-BACKUP-01.md); restore — [FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md](runbooks/FRIENDHOSTING-FINAL-OPERATIONAL-RESTORE-v1.md) |
| **FriendHosting documentation + knowledge consolidation 01** | **PASS** (2026-08-30) | Canonical asset pack + doctrines/registry/runbooks/agent knowledge — [DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01](reports/MARS-SERVER-OPS-FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01.md); home — [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md) |
| **FriendHosting next** | **Soak T0 COMPLETE** (2026-08-30/31) · long-term soak **NOT YET PROVEN** | Checker + runbook live; next = T+24h checkpoint; P4 `:24443` **DEFERRED** |
| **VEESP 3X-UI admin access hardening 01** | **PASS** server-side (2026-08-30) | Username+password rotated; new login PASS; old REVOKED; VPN `:8443` unchanged; `:5928`/`:2096` PUBLIC residual documented — [3XUI-ADMIN-ACCESS-HARDENING-01](reports/MARS-SERVER-OPS-VEESP-3XUI-ADMIN-ACCESS-HARDENING-01.md) |
| **VEESP 3X-UI upgrade + panel exposure 01** | **PASS WITH RESIDUALS** (2026-08-30) | Official upgrade **3.4.1→3.7.0**; Xray **26.6.22→26.7.28** expected; VPN/clients preserved; panel exposure **DEFERRED** — [3XUI-UPGRADE-PANEL-EXPOSURE-01](reports/MARS-SERVER-OPS-VEESP-3XUI-UPGRADE-PANEL-EXPOSURE-HARDENING-01.md) |
| **VEESP system security hardening 01** | **PASS** server-side (2026-08-30) | KEY-ONLY SSH; UFW active; fail2ban; swap 1G; journald cap; VPN `:8443` unchanged; panel ports then TEMP PUBLIC; real-workload **PENDING OPERATOR** — [SYSTEM-SECURITY-HARDENING-01](reports/MARS-SERVER-OPS-VEESP-SYSTEM-SECURITY-HARDENING-01.md) |
| **VEESP panel exposure hardening 01** | **PASS WITH RESIDUALS** (2026-08-30) | `:2096` UNUSED UNPROVEN (left open); `:5928` OPTION C ACCEPTED RESIDUAL TLS-direct; nginx DEFERRED; mutations **0** — [PANEL-EXPOSURE-HARDENING-01](reports/MARS-SERVER-OPS-VEESP-PANEL-EXPOSURE-HARDENING-01.md) |
| **VEESP final full operational backup 01** | **PASS** (2026-08-30) | Preferred stamp `veesp-final-operational-20260830T184024Z`; remote+local SHA match; restore CONFIRMED; bare-metal NOT EXERCISED — [FINAL-FULL-OPERATIONAL-BACKUP-01](reports/MARS-SERVER-OPS-VEESP-FINAL-FULL-OPERATIONAL-BACKUP-01.md) |
| **VEESP next** | **STABLE / ACCEPTED CURRENT VPN WORKLOAD** · soak **T0 PASS_WITH_RESIDUALS** · long-term soak **NOT YET PROVEN** | Next: T+24h checkpoint; P4 `:24443` DEFERRED; first non-VPN workload planning |
| **Dual-node soak / lightweight monitoring 01** | **T0 COMPLETE** (2026-08-30) | Tool + runbook; evidence [DUAL-NODE-SOAK-MONITORING-T0-01](evidence/DUAL-NODE-SOAK-MONITORING-T0-01/); report [DUAL-NODE-SOAK-MONITORING-T0-01](reports/MARS-SERVER-OPS-DUAL-NODE-SOAK-MONITORING-T0-01.md) — combined **PASS_WITH_RESIDUALS** · `SOAK_T0_PASS` |

**Managed assets / controls:** see [SERVER-INVENTORY-v1.md](SERVER-INVENTORY-v1.md)

| Control | inventory_ref | Role | Acceptance (current) |
|---------|---------------|------|----------------------|
| **VEESP** | MCA-VPN-001 | Positive control · **STABLE / ACCEPTED CURRENT VPN WORKLOAD** | TRANSPORT **PASS** · REAL_WORKLOAD **PASS** · system security **PASS** · panel exposure **PASS WITH RESIDUALS** · final backup **PASS** · soak **T0 PASS_WITH_RESIDUALS** · long-term soak **NOT YET PROVEN** · 3X-UI **3.7.0** · Xray **26.7.28** · `:5928` ACCEPTED RESIDUAL · `:2096` PUBLIC UNUSED UNPROVEN |
| **EQVPS** | EQVPS-MICRO-IP | Negative/problematic control | TRANSPORT **PASS** · REAL_WORKLOAD **FAIL** · root cause **UNPROVEN** |
| **FriendHosting DE** | FRIENDHOSTING-DE | Independent modern control · **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** | TRANSPORT **PASS** · REAL_WORKLOAD **PASS** · soak **T0 PASS_WITH_RESIDUALS** · long-term soak **NOT YET PROVEN** · Plus/P2/P3/backup **PASS** · **not** PRODUCTION_ACCEPTED |
| **AdminVPS Server B** | SERVER-B-PLANNING | Assigned-IP rejection case | Direct gate **FAIL**; provider **NOT REJECTED**; VPN stack **ABSENT** |

**Server B (AdminVPS) residual:** [SERVER-B-PLANNING](assets/SERVER-B-PLANNING/README.md) — assigned IP **REJECTED** for direct entry; support case remains available; **not** the active VPN build path while FriendHosting/VEESP carry accepted VPN workload.

**Core Run / next operator action (VPN track):** FriendHosting remains **OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD** (soak **T0 PASS_WITH_RESIDUALS**; long-term soak **NOT YET PROVEN**; **not** PRODUCTION_ACCEPTED). VEESP is **STABLE / ACCEPTED CURRENT VPN WORKLOAD** with documented panel residuals, preferred final backup `20260830T184024Z`, and soak **T0 PASS_WITH_RESIDUALS**. **Next:** T+24h soak checkpoint · then T+72h / T+7d · begin planning first non-VPN Server Ops workload (Docker deploy/restore lab). P4 `:24443` **DEFERRED**. Wider Server Ops: [SERVER-OPS-WIDER-ROADMAP-v1.md](SERVER-OPS-WIDER-ROADMAP-v1.md). Monitoring: [VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md](runbooks/VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md).

**Canonical methodology / knowledge:**

- [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md)  
- [CONTROL-EVIDENCE-METHODOLOGY-v1.md](CONTROL-EVIDENCE-METHODOLOGY-v1.md)  
- [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](SUPERSEDED-CONCLUSIONS-REGISTER-v1.md)  
- [SERVER-OPS-AGENT-KNOWLEDGE-v1.md](SERVER-OPS-AGENT-KNOWLEDGE-v1.md)  
- [SERVER-OPS-CAPABILITY-MATURITY-v1.md](SERVER-OPS-CAPABILITY-MATURITY-v1.md)  
- [SERVER-OPS-WIDER-ROADMAP-v1.md](SERVER-OPS-WIDER-ROADMAP-v1.md)  
- [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md)
- [runbooks/VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md](runbooks/VPN-NODES-LIGHTWEIGHT-MONITORING-v1.md)
- [reports/MARS-SERVER-OPS-DUAL-NODE-SOAK-MONITORING-T0-01.md](reports/MARS-SERVER-OPS-DUAL-NODE-SOAK-MONITORING-T0-01.md)

---

## 3. Operational model

| Principle | Detail |
|-----------|--------|
| **Human-supervised** | Every external change requires explicit operator approval and a scoped charter |
| **Documentation-first** | Schemas, passports, and runbooks precede any live operation |
| **Read-only default** | Discovery and status work default to read-only unless charter authorizes change |
| **Evidence discipline** | REPORT artifacts record what was done; secrets stay out of Git |
| **No autonomous admin** | Cursor/agents do not hold standing production credentials or unrestricted server access |

---

## 4. Authority dependencies

| Authority | Role for Server Ops |
|-----------|---------------------|
| [AGENTS.md](../../AGENTS.md) | Repository honesty, filesystem boundaries, git discipline |
| [.cursorrules](../../.cursorrules) | X-drive roots, preflight, selective staging |
| [governance/mars-x-drive-root-authority-v1.md](../../governance/mars-x-drive-root-authority-v1.md) | Canonical roots on `X:` |
| [projects/mars-survivability/contracts/agent-operation-risk-classes-v1.md](../mars-survivability/contracts/agent-operation-risk-classes-v1.md) | **Authoritative** risk taxonomy |
| [projects/mars-survivability/contracts/destructive-operations-policy-v1.md](../mars-survivability/contracts/destructive-operations-policy-v1.md) | **Authoritative** destructive-operation gate |
| [projects/mars-survivability/OPERATIONAL-INDEX.md](../mars-survivability/OPERATIONAL-INDEX.md) | Snapshot, halt, rollback discipline |

Server Ops **CHANGE-RISK-MODEL-v1.md** is a **practical adapter only** — Survivability classes remain authoritative.

---

## 5. Programme-owned surfaces

Server Ops **may** own (when chartered):

- VPS / Linux server **passports** and inventory schemas  
- Service topology maps (documentation)  
- Access surface models (capabilities, not credentials)  
- Host-level runbooks for n8n, PostgreSQL, Docker Compose, reverse proxy, VPN (3X-UI / Xray)  
- Backup/restore procedure documentation  
- Storage layout references under `X:\AI MARS STORAGE\mars-server-ops\`  
- Implementation charters for scoped external work  
- Evidence and REPORT pointers for server operations  

---

## 6. Explicitly excluded surfaces

Server Ops **does not** own and **must not** claim:

| Excluded | Owner / note |
|----------|----------------|
| Local Windows / Laragon runtime | [MARS Localhost Infrastructure](../mars-localhost-infrastructure/OPERATIONAL-INDEX.md) |
| Autonomous SSH orchestration fleet | **Not planned** in v1 |
| VPS hosting platform / provisioning product | **Not planned** |
| Kubernetes control plane | **Out of scope** |
| Secret manager product | Secrets remain operator-local + Storage |
| Autonomous monitoring fleet | **Not implemented** |
| EAR connector / live acquisition automation | [EAR](../ear-runtime/OPERATIONAL-INDEX.md) — read-only snapshot acquisition only |
| Git as runtime for servers | External systems remain external |
| ATLAS infrastructure IDs | No IDs invented in Phase 1A |
| Generic MetaBOT workflow logic | [MetaBOT](../metabot-seo-content-agent/) — consumer, not VPS authority |
| Site-specific WordPress/OpenCart ops (default) | Site Ops / OCPilot / WPilot programmes |

---

## 7. Related programmes

| Programme | Relationship |
|-----------|--------------|
| **MARS Localhost Infrastructure** | **Sibling** — owns `X:\MARS-Localhost` local runtime; Server Ops does **not** own Laragon/Windows local stack |
| **EAR / EAR Runtime** | **Sibling dependency** — external-access architecture and read-only acquisition concepts; Server Ops does **not** turn EAR into admin automation |
| **MARS Survivability** | **Authoritative** for risk classes, destructive ops, filesystem safety, snapshots/checkpoints, rollback |
| **MetaBOT** | **Infrastructure consumer** — may depend on n8n/PostgreSQL host; owns workflow/product concerns |
| **n8n** | **External runtime** — Server Ops may document host-level passport/runbook when chartered |
| **ATLAS** | **Optional later** documentation link — no VPS IDs in Phase 1A |
| **WPilot / OCPilot / Website Factory** | **Consumers or programme-specific owners** — not generic infrastructure authority |
| **Site Ops** (e.g. i-seo, polygon-ws) | **Pattern source** for access models and local `secrets.local.md` — site-specific, not Server Ops default |

---

## 8. External-system boundary

| Rule | Detail |
|------|--------|
| **External** | All VPS, Linux servers, VPN panels, Docker hosts, production databases |
| **Not in Git** | Live configs, credentials, dumps, private keys, raw exports |
| **No standing agent access** | Cursor does not imply SSH, panel login, or API tokens |
| **Charter per change** | Each implementation wave names exact server, service, change, risk, backup, rollback |

---

## 9. Active artifacts (Phase 1A + selection intelligence)

| Document | Role |
|----------|------|
| [SERVER-OPS-CHARTER-v1.md](SERVER-OPS-CHARTER-v1.md) | Ownership boundary and execution contract |
| [SERVER-INVENTORY-v1.md](SERVER-INVENTORY-v1.md) | Inventory schema + MCA-VPN-001 legacy row |
| [assets/MCA-VPN-001/](assets/MCA-VPN-001/README.md) | Server A legacy managed asset — Phase 1B-0 import |
| [assets/SERVER-B-PLANNING/](assets/SERVER-B-PLANNING/README.md) | Server B procurement + architecture freeze + Phase 3B live intake |
| [VPS-PROVIDER-SELECTION-RUNBOOK-v1.md](VPS-PROVIDER-SELECTION-RUNBOOK-v1.md) | **VPS PROVIDER SELECTION INTELLIGENCE** — Stages 0–11 |
| [VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md](VPS-PROVIDER-REQUIREMENT-INTAKE-v1.md) | Stage 0 requirement intake |
| [VPS-PROVIDER-RESEARCH-SCORECARD-v1.md](VPS-PROVIDER-RESEARCH-SCORECARD-v1.md) | Hard exclusion + weighted scorecard |
| [VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md](VPS-NETWORK-PREFLIGHT-RUNBOOK-v1.md) | Pre-purchase / post-provision network tests |
| [VPS-PROCUREMENT-GATE-v1.md](VPS-PROCUREMENT-GATE-v1.md) | Procurement allow/deny gate |
| [VPS-PASSPORT-v1.md](VPS-PASSPORT-v1.md) | Reusable passport template |
| [SERVICE-MAP-v1.md](SERVICE-MAP-v1.md) | Service relationship model |
| [ACCESS-MODEL-v1.md](ACCESS-MODEL-v1.md) | Access surface capability model |
| [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md) | Git vs local vs Storage secret boundaries |
| [STORAGE-MODEL-v1.md](STORAGE-MODEL-v1.md) | Out-of-Git Storage layout (proposed) |
| [BACKUP-RESTORE-MODEL-v1.md](BACKUP-RESTORE-MODEL-v1.md) | Backup classes and restore discipline |
| [CHANGE-RISK-MODEL-v1.md](CHANGE-RISK-MODEL-v1.md) | Server Ops labels → Survivability mapping |
| [REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md](REAL-WORKLOAD-ACCEPTANCE-DOCTRINE-v1.md) | Scoped acceptance states + evidence hierarchy |
| [CONTROL-EVIDENCE-METHODOLOGY-v1.md](CONTROL-EVIDENCE-METHODOLOGY-v1.md) | Controls, anti-config-churn, hypothesis vocabulary |
| [SUPERSEDED-CONCLUSIONS-REGISTER-v1.md](SUPERSEDED-CONCLUSIONS-REGISTER-v1.md) | Canonical superseded claims |
| [SERVER-OPS-AGENT-KNOWLEDGE-v1.md](SERVER-OPS-AGENT-KNOWLEDGE-v1.md) | Reusable Server Ops operator/agent knowledge |
| [SERVER-OPS-CAPABILITY-MATURITY-v1.md](SERVER-OPS-CAPABILITY-MATURITY-v1.md) | Demonstrated vs non-claimed capabilities |
| [SERVER-OPS-WIDER-ROADMAP-v1.md](SERVER-OPS-WIDER-ROADMAP-v1.md) | Post-VPN wider roadmap |
| [assets/FRIENDHOSTING-DE/](assets/FRIENDHOSTING-DE/README.md) | FriendHosting canonical infrastructure pack |
| [reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md](reports/MARS-SERVER-OPS-VPN-CASE-STUDY-CLOSEOUT-01.md) | VPN investigation knowledge closeout |
| [reports/MARS-SERVER-OPS-FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01.md](reports/MARS-SERVER-OPS-FRIENDHOSTING-DOCUMENTATION-KNOWLEDGE-CONSOLIDATION-01.md) | FriendHosting documentation consolidation |

---

## 10. Future phases (deferred / roadmap)

**Require separate charters** (not claimed implemented):

- FriendHosting soak / lightweight monitoring  
- FriendHosting P4 reserve `:24443` (DEFERRED)  
- FriendHosting bare-metal DR drill  
- CURRENT-VPN-SERVER-PASSPORT instances per control (optional polish)  
- N8N-INFRA-PASSPORT / POSTGRES-FOR-METABOT-PLAN / DOCKER-APP-STANDARD  
- MONITORING-HEALTHCHECKS / INCIDENT-RUNBOOK  
- Production deployment runbooks for non-VPN stacks  

**General reusable lifecycle (post-VPN mission):**

```text
REQUIREMENTS → PREFLIGHT → PROVIDER/CAPACITY → BACKUP/ROLLBACK → DEPLOY → TECHNICAL VALIDATION
→ REAL-WORKLOAD ACCEPTANCE → HARDEN → BACKUP → DOCUMENT → MONITOR → RECOVER
```

Workloads: Linux VPS · Docker · PostgreSQL · n8n · reverse proxy · TLS · migration · capacity · incident response.

See [SERVER-OPS-WIDER-ROADMAP-v1.md](SERVER-OPS-WIDER-ROADMAP-v1.md).

---

## 11. Canonical reading order

| Step | Document | Why |
|------|----------|-----|
| 1 | This index | Programme scope and phase |
| 2 | [SERVER-OPS-CHARTER-v1.md](SERVER-OPS-CHARTER-v1.md) | Mission and non-scope |
| 3 | [CHANGE-RISK-MODEL-v1.md](CHANGE-RISK-MODEL-v1.md) | Risk adapter → Survivability |
| 4 | [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md) | What never enters Git |
| 5 | [ACCESS-MODEL-v1.md](ACCESS-MODEL-v1.md) | Surface capabilities |
| 6 | [STORAGE-MODEL-v1.md](STORAGE-MODEL-v1.md) + [BACKUP-RESTORE-MODEL-v1.md](BACKUP-RESTORE-MODEL-v1.md) | Artifacts outside Git |
| 7 | Schemas: inventory, passport, service map | Intake templates for Phase 1B |

---

*Operational Index · FriendHosting OPERATIONALLY ACCEPTED — CURRENT VPN WORKLOAD · VEESP STABLE / ACCEPTED CURRENT VPN WORKLOAD · dual-node soak T0 PASS_WITH_RESIDUALS · long-term soak NOT YET PROVEN · EQVPS negative control · AdminVPS IP rejection residual · no autonomous runtime claimed.*
