# AG-WP-001 — Approval Token Contract v1

**Document type:** Logical approval contract (not authentication)  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

---

## Required fields

| Field | Type | Rule |
|-------|------|------|
| `approval_id` | string | Unique per issuance |
| `operator` | string | Human operator identity |
| `operation_id` or `operation_group` | string | Scoped — not wildcard |
| `project_id` | string | e.g. `FP-0002` when chartered |
| `environment` | enum | Must match operation `environment_scope` |
| `approved_scope` | string | Human-readable bounded scope |
| `approved_files` | string[] | Allowlist when source mutation |
| `approved_runtime_changes` | string[] | Explicit runtime mutations when R3 |
| `issued_at` | ISO datetime | — |
| `expires_at` or `single_use` | datetime / bool | Required |
| `source_commit` | string | Git SHA when source involved |
| `rollback_reference` | string | Checkpoint or backup id |

---

## Risk rules

| Class | Approval |
|-------|----------|
| R0 | Pre-authorized locally for read-only inspection/validation |
| R1 | Architecture / plan human review |
| R2 | Approved plan + checkpoint reference |
| R3 | Explicit operator approval + backup |
| R4 | Explicit staging approval (not authorized at foundation) |
| R5 | **Prohibited** — no token may authorize |

---

## Scope binding

Phrases like «делай всё» or «implement everything» **do not** authorize:

- production access
- unrestricted operations
- operations outside `approved_files` / `approved_scope`

**FP-0002 pilot:** **LOCKED** — no approval tokens before FW-06B and pilot charter.

---

*Approval token contract v1 — logical only.*
