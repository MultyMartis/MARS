# EAR Credential Boundary v1

**Purpose:** Define where credentials live, what each layer may access, and what must never enter git, snapshots, or reports.  
**Status:** architecture specification only — **no** vault product, encryption implementation, or secret store in MARS repo.  
**Phase:** 2D  
**Relation:** Extends [EAR-SECURITY-MODEL-v1.md](EAR-SECURITY-MODEL-v1.md) for the connector layer.

---

## Principles

1. **Credentials are operator-owned** — EAR documents boundaries; EAR does not own identity stores.
2. **References, not values** — Runtime may load secrets from external paths; artifacts carry **refs** only where explicitly allowed.
3. **Least exposure** — Connectors see credentials during **Armed → Acquiring** only; consumers never need them for snapshot analysis.
4. **Fail closed** — Missing credential ref blocks Mode 2; do not fall back to embedded secrets in repo.

---

## Where credentials live

| Location | Role | Git |
|----------|------|-----|
| Operator external `secrets/` (e.g. consumer-specific tree) | Primary store for FTP, SFTP, SSH, admin passwords | **Never** |
| Hosting panel / provider vault | Source of truth for rotation | **Never** |
| Operator password manager | Human retrieval for Mode 0/1 | **Never** |
| Environment variables on operator machine | Future runtime injection — local only | **Never** in repo |
| EAR documentation | Describes **shapes** of refs, not values | Yes (docs only) |
| MARS git repository | **No** credential values | Docs and contracts only |

**SAFE UNKNOWN:** Organization-wide vault product selection — not chosen at Phase 2D.

---

## What connectors may access

| Access | Allowed | Forbidden |
|--------|---------|-----------|
| Read credential via `credential_ref` at session start | Yes (future runtime) | Reading secrets from git |
| Use credentials for read-only protocol login | Yes, within approved channel | Storing password in Evidence Package |
| Log connection success/failure | Yes, without secret values | Logging password, key material, cookies |
| Cache session token for acquisition session | Yes, in memory / temp store outside git | Writing token into snapshot `metadata` |
| Pass credential to another connector | Only via Hybrid charter + operator approval | Implicit sharing without scope |

Connectors **must** release credential context on **Closed** lifecycle state.

---

## What consumers may access

| Access | Allowed | Forbidden |
|--------|---------|-----------|
| Published Snapshot Package | Yes | Raw credentials |
| `secret_ref` in metadata for **operator** follow-up | Optional, documented in security model — consumer audit runs should not require it | Using refs to auto-connect during read-only audit |
| Bulk file tree with redacted `config.php` | Yes if published | Full `config.php` with DB password in consumer-visible bulk without charter |
| `acquisition-log` channel names | Yes | Session cookies, API keys |

Consumers analyze **evidence**, not **live systems**, by default per OCPilot model.

---

## What EAR may access

| Layer | Credentials | Evidence | Published snapshot |
|-------|-------------|----------|-------------------|
| **Documentation (Phase 2D)** | None | N/A | N/A |
| **Validation (future)** | No — reads Evidence Package only | Yes | Assembles sections |
| **Connector orchestration (future)** | Via ref at Acquire only | Produces | No direct publish |
| **Operator HITL records** | No | Charter refs | Approval ids only |

EAR **must not** copy connector session secrets into validation logs committed to git.

---

## What must never enter git

| Material | Reason |
|----------|--------|
| Passwords, API keys, private keys | Irreversible exposure |
| `config.php`, `.env` with live secrets | Site compromise |
| Full database dumps with PII | GDPR + security |
| SFTP/FTP session logs with AUTH details | Credential leakage |
| Browser cookies / admin session exports | Session hijack |
| Unredacted Evidence Packages | May contain secrets from SITE |

Bulk acquisition artifacts belong in **external storage** per [EAR-STORAGE-MODEL-v1.md](EAR-STORAGE-MODEL-v1.md).

---

## What must never enter snapshots (published)

| Material | Alternative |
|----------|-------------|
| Raw passwords and keys | Channel name + `credential_ref` omitted or external-only operator note |
| Live session tokens | Not in contract |
| Full row-level customer/order data | `database-metadata` schema-only |
| Unredacted `config.php` | Structure-only excerpt or hash of redacted file |
| Operator personal secrets unrelated to SITE | N/A |

Published snapshot = consumer contract per Phase 2A — not a dump of Evidence Package.

---

## What must never enter reports

| Material | Rule |
|----------|------|
| Credential values | Use channel + outcome only |
| Full paths to secret files in public reports | Use logical ref class only if needed |
| PII from accidental over-collection | Halt and quarantine — see failure model |

MARS `# REPORT — …` discipline and Cursor agent rules: do not paste secrets into chat logs that may be committed.

---

## Separation of concerns

```
┌──────────────────────────────────────────────────────────┐
│ Operator — owns credentials, HITL, rotation              │
└────────────────────────────┬─────────────────────────────┘
                             │ credential_ref (external)
                             ▼
┌──────────────────────────────────────────────────────────┐
│ Connector — transient use; read-only acquisition         │
└────────────────────────────┬─────────────────────────────┘
                             │ Evidence Package (redacted)
                             ▼
┌──────────────────────────────────────────────────────────┐
│ EAR Validation — maps to sections; no credential access  │
└────────────────────────────┬─────────────────────────────┘
                             │ Snapshot Package (publish gate)
                             ▼
┌──────────────────────────────────────────────────────────┐
│ Consumer — analysis only; no default live reconnect        │
└──────────────────────────────────────────────────────────┘
```

---

## Redaction responsibilities

| Stage | Owner |
|-------|-------|
| Before ZIP enters quarantine | Operator scrubs `config.php` or EAR rejects |
| During SFTP/SSH read | Connector policy: skip or redact secret files |
| At Evidence → Snapshot mapping | EAR Validation enforces publish rules |
| At consumer intake | Consumer rejects publish if secrets detected |

---

## Mode 0 / 1 note

Operator may possess credentials while manually collecting files. EAR still applies **same publish rules** — manual delivery does not exempt snapshot from credential boundary.

---

## SAFE UNKNOWN

- Automated secret scanning in Evidence Package — future tooling.
- Multi-operator credential escrow — not defined.

---

## Non-goals

- Implementing a secrets manager or encrypting external bulk at rest.
