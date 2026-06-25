# AG-WP-001 — WordPress-Native AI Interfaces Boundary v1

**Document type:** Future interface boundary  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Rule:** No interface becomes an agent tool merely because it exists. Each requires typed operation, permission model, environment boundary, audit trail, and rollback rule.

**Production exposure:** **Prohibited** at foundation stage.

---

## Interface classification

| Interface | Classification | Notes |
|-----------|----------------|-------|
| WordPress Abilities API | **EXPERIMENTAL** | Future typed ops only |
| WordPress MCP Adapter | **EXPERIMENTAL** | Not auto-wired to AG-WP-001 |
| Playground MCP | **AVAILABLE** (preview) | R0 inspect only; not dev SoT |
| AI Client (WP core direction) | **PLANNED** | Monitor; not required |
| Connectors API | **PLANNED** | Not approved for agent |
| ACF AI-discoverable surfaces | **EXPERIMENTAL** | Field discovery ≠ implementation authority |
| REST API | **AVAILABLE** | Read-biased R0; write needs typed op |
| WP-CLI | **AVAILABLE** | Local MLI; mapped in FW-03 command model |

---

## Adoption requirements (future FW-07B+)

1. Operation ID in [FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md](../registries/FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md)
2. Risk class assignment
3. Environment scope (local only at first)
4. Approval gate
5. Audit evidence format
6. Rollback method
7. Operator charter amendment

---

## Explicit rejections

| Pattern | Status |
|---------|--------|
| Unrestricted MCP tool surface | **NOT APPROVED** |
| Autonomous plugin via Abilities API | **NOT APPROVED** |
| Production MCP exposure | **NOT APPROVED** |
| Agent installs bridges without charter | **FORBIDDEN** |

---

*WP-native AI boundary v1 — assess only; do not implement runtime.*
