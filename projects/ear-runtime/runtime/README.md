# EAR Runtime

**Type:** Runtime implementation root — skeleton only  
**Program:** [projects/ear-runtime/](../)  
**Architecture source:** [shared/external-access-runtime/](../../shared/external-access-runtime/)

---

## Purpose

Local, human-operated runtime for External Access Runtime (EAR) acquisition workflows. CLI-first entry point for future connector, builder, and validator implementations under R1–R5.

---

## Scope

| In scope (this folder) | Out of scope |
|------------------------|--------------|
| Runtime folder structure | Live SFTP, SSH, FTP, or database access |
| Skeleton CLI (`cli.py`) | Connector implementations |
| Area READMEs (connectors, builders, validators, shared) | Credential loading or config execution |
| Deferred dependency manifest (`requirements.txt`) | PILOT execution |
| | Real credentials or external system access |

---

## Current state

| Field | Value |
|-------|-------|
| **Implemented** | **NONE** |
| **Execution** | **NOT AUTHORIZED** |
| **Live access** | **FORBIDDEN** |
| **Runtime Skeleton** | **CREATED** (R1.1) |

---

## Layout

| Path | Role |
|------|------|
| `cli.py` | CLI entry — banner and state only |
| `connectors/` | Future R1 connector implementations |
| `builders/` | Future R2/R3 evidence and snapshot builders |
| `validators/` | Future R5 validation helpers |
| `shared/` | Future cross-cutting runtime utilities |
| `requirements.txt` | Dependency manifest — comment-only at skeleton |

---

## Running the skeleton CLI

From this directory:

```
python cli.py
```

Prints runtime banner and state. Exits 0. No network, no credentials, no acquisition logic.
