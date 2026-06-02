# EAR Security Model v1

Security and operational safety rules for External Access Runtime. Complements [external-access-patterns/safety-boundaries.md](../external-access-patterns/safety-boundaries.md) and MARS survivability discipline.

**Not:** automated enforcement, vault product, or SOC2 certification.

---

## Principles

1. **Secrets stay outside the repo**
2. **EAR reads references, not committed passwords**
3. **Read-only is the default**
4. **Operator approval (HITL) before connected acquisition**
5. **Consumers never need raw credentials in git**
6. **Future write modes require rollback discipline**

---

## Secrets handling

| Rule | Detail |
|------|--------|
| No raw passwords in git | Including `.env`, `config.php`, connection strings |
| Secret storage | External paths (e.g. OCPilot `...\secrets\`) — operator controlled |
| **Secret reference** | Snapshot may include `{ "secret_ref": "external://ocpilot/.../secrets/ftp.json" }` for operator tools — **not** for agent to paste into chat logs committed to repo |
| Credential rotation | Operator responsibility — EAR logs **which** channel, not secret values |
| Agent/Cursor | Must not read secret files into reports unless explicit human task and no commit |

---

## EAR reads references

EAR (future implementation) should:

- Load connection parameters from operator-local store at runtime
- Never write acquired secrets into snapshot `metadata`
- Redact hostnames in public reports if operator requests — **SAFE UNKNOWN** policy per task

---

## Read-only default

| Layer | Expectation |
|-------|-------------|
| Modes 0–2 | Read-only acquisition only in v1 |
| Mode 3 | Forbidden in v1 |
| Connectors | LIST/GET/export/navigation without save |
| Database | Metadata and structure exports preferred over full dumps |
| Admin UI | View-only; stop before any save dialog |

If read-only cannot be guaranteed (e.g. admin auto-save plugin), fall back to Mode 0 file drop.

---

## Operator approval (HITL)

Before Mode 2 connected acquisition:

| Gate | Question |
|------|----------|
| Target | Correct site id, URL, hosting account? |
| Environment | TEST vs production — verbal/written OK |
| Channel | SFTP vs SSH vs admin — scoped |
| Backup fact | For write-class elsewhere; read-only audit still records backup **claim** |
| Scope | Path prefixes, max size, tables excluded |
| Publish | Operator approves snapshot move to consumer-visible bulk |

EAR `access-log` records approvals without secrets.

---

## Consumer isolation

- Consumers analyze snapshots; they do not re-open live connections by default in audit runs.
- If consumer needs live re-check, new HITL cycle — not implied by snapshot age.

---

## Rollback requirements (future write modes)

**Not applicable to v1** (Mode 3 forbidden). Documented for Phase 5 evaluation:

| Requirement | Detail |
|-------------|--------|
| Pre-write snapshot | File + DB backup verified restorable |
| Rollback plan | Human-written, mars-survivability templates |
| Risk class | MEDIUM+ minimum |
| Stop conditions | Halt protocol on drift or wrong target |

No write connector without explicit charter referencing rollback artifacts.

---

## Threat notes (documentation)

| Threat | Mitigation |
|--------|------------|
| Wrong-site acquisition | HITL target checklist; manifest spot-check |
| Zip/shell malware in intake | Quarantine policy — consumer/OCPilot incoming rules |
| Over-collection (PII) | Scope limits in charter |
| Leak via REPORT | Redact secrets; reference external paths only |
| Autonomous agent drift | No Mode 2 without operator start/stop |

---

## SAFE UNKNOWN

- Encryption at rest for external bulk storage — operator infrastructure
- MFA requirements per host — operator policy
- Formal penetration test — not in scope v1 docs
