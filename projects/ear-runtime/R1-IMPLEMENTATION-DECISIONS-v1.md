# R1 — Implementation Decisions v1

**Type:** Evidence-backed decision record — decisions **already justified** in repository documentation only  
**Date:** 2026-06-02  
**Backlog item:** R1 — SFTP Read-Only Connector  
**Review:** [R1-IMPLEMENTATION-READINESS-REVIEW-v1.md](R1-IMPLEMENTATION-READINESS-REVIEW-v1.md)

**Rule:** No new decisions without repository evidence. Items marked **SAFE UNKNOWN** or **PARTIAL** are **not** decisions.

---

## Decided (KNOWN)

| Decision | Value | Evidence |
|----------|-------|----------|
| Primary language | **Python** | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) § Runtime Stack |
| Execution style | **CLI-first** | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md); [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) § Human operated |
| Execution model | **Human-operated** | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md); [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) |
| Connected mode | **Mode 2 — Read-only** | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md); [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) |
| Connector class | **SFTP Read-Only** | [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md); [EAR-CONNECTOR-TYPES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-TYPES-v1.md) |
| Reference acquisition path | **CON-L1-A** | [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md); [EAR-CONNECTED-PATHS-v1.md](../../shared/external-access-runtime/EAR-CONNECTED-PATHS-v1.md) |
| Credential handling | **`credential_ref` only** — secrets outside git | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md); [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) § Credential boundary |
| Failure posture | **Fail closed** | [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md); [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) |
| R1 output role (planning) | **Raw acquisition artefacts** — not published snapshot | [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) § Outputs; [EAR-RUNTIME-BACKLOG-v1.md](../../shared/external-access-runtime/EAR-RUNTIME-BACKLOG-v1.md) § R1 |
| Evidence Package assembly | **R2** — not R1 | [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) § Boundaries; backlog dependency R1 → R2 |
| Implementation placement | **`projects/ear-runtime/runtime/connectors/`** (proposed) | [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) |
| First design consumer (pilot) | **PILOT-001** — SITE-001, TEST, Level 1 | [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md); [PILOT-CHARTER-v1.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/PILOT-CHARTER-v1.md) |
| Autonomous / scheduled acquisition | **Forbidden** in v1 | [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) § No autonomous actions |
| Mode 3 / write connectors | **Forbidden** without architecture amendment | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md); [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) |

---

## Partially decided (PARTIAL)

| Area | What is known | What remains open | Evidence |
|------|---------------|-------------------|----------|
| Credential binding | Ref-only model | External path resolution procedure | [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md); pilot sub-charter §4 **SAFE UNKNOWN** |
| Logging | Human-inspectable outputs required | Log format, paths, retention | [ENGINEERING-PRINCIPLES-v1.md](ENGINEERING-PRINCIPLES-v1.md) § Inspectability; [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) examples only |
| Failure reporting | Taxonomy and classes | Runtime artefact location and schema | [EAR-CONNECTOR-FAILURES-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-FAILURES-v1.md) |
| Connector contract conformance | Normative contract frozen | R1 session output vs `evidence_package_ref` — document in Implementation Charter | [EAR-CONNECTOR-CONTRACT-v1.md](../../shared/external-access-runtime/EAR-CONNECTOR-CONTRACT-v1.md) vs R1 charter |

---

## Not decided (SAFE UNKNOWN)

| Area | Notes | Evidence |
|------|-------|----------|
| Python minor version | "Python" only — no 3.10/3.11/3.12 pin | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) |
| Packaging strategy | Explicitly deferred from Engineering Charter | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) § Explicit non-decisions |
| SFTP client library | Deferred to Implementation Charter | [R1-SFTP-CONNECTOR-CHARTER-v1.md](R1-SFTP-CONNECTOR-CHARTER-v1.md) § Next gate |
| Output / evidence / snapshot filesystem paths | Operator-bound | [EAR-STORAGE-MODEL-v1.md](../../shared/external-access-runtime/EAR-STORAGE-MODEL-v1.md); pilot sub-charter §4 |
| Test layout | Deferred | [RUNTIME-STRUCTURE-v1.md](RUNTIME-STRUCTURE-v1.md) § Explicit non-goals |
| CI/CD | Out of scope | [ENGINEERING-CHARTER-v1.md](ENGINEERING-CHARTER-v1.md) |

---

## Explicit non-decisions (do not infer)

| Topic | Status |
|-------|--------|
| PILOT-001 live SFTP execution | **NOT AUTHORIZED** — [pilots/.../STATUS.md](../../shared/external-access-runtime/pilots/PILOT-001-SITE-001-SFTP-READONLY/STATUS.md) |
| R1 code implementation | **NOT AUTHORIZED** — this document |
| Vault product | **SAFE UNKNOWN** org-wide — [EAR-CREDENTIAL-BOUNDARY-v1.md](../../shared/external-access-runtime/EAR-CREDENTIAL-BOUNDARY-v1.md) |

---

## Truth statement

This file records **documentation-derived** decisions only. **No** runtime code exists to validate implementation choices.
