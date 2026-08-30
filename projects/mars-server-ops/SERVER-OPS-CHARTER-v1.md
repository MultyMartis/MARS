# MARS Server Ops & VPS Forge — Charter v1

**Programme:** MARS Server Ops & VPS Forge  
**Status:** **documented** — programme boundary charter  
**Not:** SSH automation product, VPS platform, or production admin runtime

---

## 1. Mission

Establish and maintain **human-supervised** documentation, schemas, and controlled procedures for external server infrastructure operations within the MARS ecosystem.

Server Ops enables operators to plan, classify risk, backup, execute, validate, and roll back changes on VPS and Linux hosts **without** treating Git or Cursor as an autonomous infrastructure controller.

---

## 2. Scope

In scope when explicitly chartered:

- VPS and Linux server inventory and passports (sanitized)  
- VPN infrastructure (including 3X-UI / Xray) — documentation and runbooks  
- Docker / Docker Compose host operations — documented procedures  
- n8n infrastructure at host level — passports and runbooks  
- PostgreSQL and other databases — backup, migration, health documentation  
- Reverse proxy / TLS — change procedures and evidence  
- Backups, restores, migrations — manifests and validation  
- Health checks and operational runbooks — human-operated  
- Controlled implementation procedures with evidence / REPORT requirements  

---

## 3. Non-scope

Explicitly **out of scope** for this programme:

| Item | Reason |
|------|--------|
| Autonomous server orchestrator | Human approval required for all external change |
| SSH automation fleet | No standing agent SSH product |
| VPS hosting platform | MARS does not sell or provision VPS |
| Kubernetes control plane | Not part of v1 programme |
| Automatic production administrator | All production mutation is human-led |
| Secret manager product | Secrets stay operator-local + Storage |
| Autonomous monitoring fleet | Not implemented |
| Local Windows / Laragon runtime | Owned by [MLI](../mars-localhost-infrastructure/OPERATIONAL-INDEX.md) |
| EAR live connector admin | EAR remains read-only acquisition architecture |
| Site-specific CMS ops (default) | Site Ops / WPilot / OCPilot lanes |

---

## 4. Human approval model

| Layer | Rule |
|-------|------|
| **Planning** | Web-GPT / Cursor may draft docs and charters |
| **Execution** | Operator must approve before any external mutation |
| **HITL default** | No implied "yes" from task phrasing alone |
| **Standing access** | **Forbidden** — no generic "server access approved" token |

Every external implementation requires a **separate exact charter** identifying at minimum:

- exact server (inventory ref / passport ref)  
- exact service  
- exact intended change  
- risk class (Survivability + Server Ops label)  
- backup / checkpoint plan  
- validation steps  
- rollback method  
- named operator approval  

---

## 5. External system boundary

```text
Repository (X:\AI MARS)     → procedures, schemas, sanitized templates, secret_ref only
Local operator store        → credentials, runtime.env, tokens (gitignored)
Bulk Storage (X:\AI MARS STORAGE\mars-server-ops\) → exports, backups, evidence
External servers          → live execution surface (never owned by Git)
```

No live server state is authoritative in Git. Git documents **how** work should be done, not **what** the server currently contains unless attested in a dated evidence artifact.

---

## 6. Read-only vs change execution model

| Mode | Default | Authorization |
|------|---------|---------------|
| **Read-only discovery** | **YES** — status, list, inspect, export metadata | Charter or task scope listing surfaces; no mutation |
| **Low-risk local doc** | Git-only artifact updates | Scope lock; Survivability LOW or MEDIUM as applicable |
| **Bounded change** | **NO** default | Explicit charter + operator approval + backup when required |
| **Destructive** | **NO** | Survivability destructive gate + explicit operator approval |

Agents must assume **read-only** for all external surfaces unless charter explicitly authorizes change class and paths.

---

## 7. Risk classification — Survivability authoritative

Server Ops uses practical labels in [CHANGE-RISK-MODEL-v1.md](CHANGE-RISK-MODEL-v1.md).  
**Authoritative taxonomy:** [agent-operation-risk-classes-v1.md](../mars-survivability/contracts/agent-operation-risk-classes-v1.md).

When labels conflict, **Survivability wins**. Ambiguous work → classify **HIGH RISK** minimum.

---

## 8. Destructive operation gate

Destructive server operations (drop database, delete volume, wipe host, overwrite production from backup, firewall reset, remove production user/client) require:

1. Classification per Survivability (typically **FORBIDDEN** for agents, or **CRITICAL** / human-only)  
2. Exact path/resource list  
3. Dry-run or equivalent impact review where applicable  
4. Checkpoint / backup per [BACKUP-RESTORE-MODEL-v1.md](BACKUP-RESTORE-MODEL-v1.md)  
5. Explicit operator approval with rollback method  
6. Post-action audit evidence  

Cross-reference: [destructive-operations-policy-v1.md](../mars-survivability/contracts/destructive-operations-policy-v1.md).

Agents **must refuse** recursive delete, mass wipe, and agent-initiated `git clean` / `git reset --hard` per Survivability FORBIDDEN list.

---

## 9. Secret boundary

| Location | Allowed content |
|----------|-----------------|
| **Git** | `secret_ref`, sanitized hostnames, capability docs — **never values** |
| **Local** | `X:\AI MARS\local\infrastructure\<server-or-passport-ref>\` — operator-controlled |
| **Storage** | Raw configs, exports, backups — out of Git |

See [SECRET-HANDLING-MODEL-v1.md](SECRET-HANDLING-MODEL-v1.md).

Agents must not read secret files into committed reports unless explicit human task and no commit of values.

---

## 10. Backup-before-change expectation

Before **MEDIUM RISK** or higher external change:

- Document backup class per [BACKUP-RESTORE-MODEL-v1.md](BACKUP-RESTORE-MODEL-v1.md)  
- Create checkpoint where practical  
- Record backup manifest location (Storage path or operator attestation)  

**Server Ops programme rule:** A backup is not operationally complete until a **restore strategy** exists (see backup model). This is programme discipline derived from Survivability rollback patterns — **not** claimed as a new global MARS rule.

---

## 11. Restore strategy expectation

Every production-impacting change charter must state:

- what will be restored (files, DB, volume, config)  
- restore order  
- validation after restore  
- evidence location  

Prefer scoped restore over full-host rollback when issue is narrow (Forge backup lesson pattern).

---

## 12. Evidence / REPORT requirements

| Event | Expectation |
|-------|-------------|
| External read-only discovery | REPORT with surfaces used, mutations **0**, evidence refs |
| External change | REPORT with charter id, backup ref, commands class (not secret values), validation, rollback readiness |
| Failed or halted work | STOP token + halt per Survivability |

Reports live under programme `reports/` when created in future waves — not required for Phase 1A foundation.

---

## 13. Git discipline

- **Default:** no commit unless operator requests  
- **Never:** `git add .`, `git add -A`, `git commit -a`  
- Stage only allowlisted paths from task charter  
- Foreign WIP must not be staged or cleaned  
- No secrets in Git — see secret model  

---

## 14. Storage boundary

- **Active Brain:** `X:\AI MARS` — canonical docs only  
- **Bulk:** `X:\AI MARS STORAGE\mars-server-ops\` — raw/sensitive artifacts  
- Storage is **not** a second repository  

See [STORAGE-MODEL-v1.md](STORAGE-MODEL-v1.md).

---

## 15. Relationship with other MARS programmes

| Programme | Server Ops stance |
|-----------|-------------------|
| **MLI** | Sibling — local runtime owner; no overlap on Laragon/Windows |
| **EAR** | Reuse read-only / snapshot concepts; do not automate admin via EAR |
| **Survivability** | Authoritative risk, destructive ops, snapshots |
| **MetaBOT** | Consumer of n8n/DB host; Server Ops documents host when chartered |
| **Site Ops** | Pattern reuse for access/secrets; site passports stay in site programmes |
| **OCPilot / WPilot / Forge** | Consumers; promotion and CMS authority stay in those lanes |
| **ATLAS** | Optional future cross-reference — no infrastructure IDs in Phase 1A |

---

## 16. SAFE UNKNOWN policy

If a fact is not provable from repository evidence, operator attestation, or scoped read-only discovery:

- State **SAFE UNKNOWN** explicitly  
- Do not invent servers, IPs, credentials, or service topology  
- Document what would verify the unknown  

---

## 17. Implementation authorization model

**Phase 1A** authorizes **documentation only**.

Future phases require **Implementation Charter** per target, including:

```text
IMPLEMENTATION CHARTER — required fields
- charter_id
- server_ref / passport_ref
- service(s)
- change description (exact)
- risk_class (Survivability + Server Ops label)
- read_only: yes|no
- backup_plan_ref
- rollback_plan_ref
- validation_steps
- operator_approval (name/date)
- evidence_output_path
```

No charter → no external mutation. No generic infrastructure blanket approval.

---

*Charter v1 · Phase 1A · documentation-first foundation.*
