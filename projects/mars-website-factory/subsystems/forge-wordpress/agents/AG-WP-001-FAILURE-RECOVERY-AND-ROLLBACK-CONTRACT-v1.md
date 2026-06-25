# AG-WP-001 — Failure, Recovery and Rollback Contract v1

**Document type:** Failure and rollback contract  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

---

## 1. Pre-change snapshot requirements (R2+)

| Artifact | When |
|----------|------|
| Git checkpoint | Before source changes |
| DB backup | Before R3 mutations |
| File backup | Theme/plugin dirs before bulk edits |
| Plugin inventory export | Before plugin activation |
| Environment manifest | Runtime ID, URL, versions |

---

## 2. Failure classes

| Class | Examples |
|-------|----------|
| **SOURCE FAILURE** | Syntax error, failed build, bad merge |
| **RUNTIME FAILURE** | White screen, fatal PHP, Apache/PHP down |
| **DATABASE FAILURE** | Corrupt tables, failed migration |
| **VISUAL FAILURE** | Parity regression beyond waiver |
| **CONTENT FAILURE** | Wrong field mapping, data loss |
| **SECURITY FAILURE** | Credential leak, unsafe capability |
| **DEPENDENCY FAILURE** | Plugin conflict, version mismatch |
| **ENVIRONMENT FAILURE** | Wrong runtime, MLI profile mismatch |

---

## 3. Rollback procedure

1. **Trigger** — operator or agent stop condition
2. **Halt** — no further mutations
3. **Restore** — Git revert → file backup → DB restore (order per failure class)
4. **Verify** — integrity checks (Gate D minimum)
5. **Incident report** — failure class, cause, evidence, SAFE UNKNOWN
6. **Re-entry** — only after operator approves retry plan

FP-0002 baseline: `reset-to-foundation.ps1` + brain source revert per [FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md](../projects/fp-0002/FP-0002-FW-06B-APPROVED-FRONTEND-INTAKE-INPUT-v1.md)

---

## 4. Mandatory stop conditions

Agent must **stop** when:

- DB integrity is uncertain
- Source authority is ambiguous (commit vs working tree)
- Frontend approval is missing
- Production target detected unexpectedly
- Credentials boundary unclear
- Destructive migration lacks rollback
- Validation outputs conflict
- Risk class escalation not approved

---

## 5. SAFE UNKNOWN escalation

Record: unknown field, required evidence, blocking vs non-blocking, operator decision request.

---

*Failure contract v1 — rollback before retry.*
