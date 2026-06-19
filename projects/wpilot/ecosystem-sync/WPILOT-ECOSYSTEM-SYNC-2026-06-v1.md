# WPilot Ecosystem Sync Notes — 2026-06 v1

**Classification:** Cross-system visibility notes — documentation only.  
**Date:** 2026-06-19  
**Trigger:** WPilot v0.3.0 state freeze — first proven plugin REST write path on DEV.

**Scope:** Notes for sibling systems. **Does not modify** OCPilot, Website Factory, ATLAS, or any external codebase.

---

## Purpose

Зафиксировать уроки и статус WPilot для смежных систем MARS после перехода в **proven runtime** (DEV). Это visibility layer, не governance expansion.

---

## WPilot (self)

| Field | Value |
|-------|-------|
| Version | `0.3.0` / schema `0.2.0` |
| Environment | DEV only |
| Maturity | Proven content writes on DEV via plugin REST |
| State freeze | [WPILOT-STATE-FREEZE-2026-06-19-v1.md](../WPILOT-STATE-FREEZE-2026-06-19-v1.md) |

---

## OCPilot

### Reusable pattern

WPilot DEV sprints подтвердили переносимый **human-supervised write safety loop**:

```
inspect → backup → apply → validate → rollback
```

| Step | WPilot proof | OCPilot relevance |
|------|--------------|-------------------|
| **inspect** | REST read + checksum baseline | Pre-change state capture before any mutation |
| **backup** | Plugin-owned snapshot before write | Mandatory rollback source before apply |
| **apply** | Scoped exact-once replace | Narrowest write primitive; refuse on ambiguity |
| **validate** | Post-write checksum + content confirmation | Fail closed; no silent partial success |
| **rollback** | Restore from plugin backup + checksum verify | Recovery path must be proven before expanding write scope |

### Notes for OCPilot operators

- WPilot evidence is **WordPress-only** — does not transfer as OpenCart proof.
- Pattern is **workflow discipline**, not a shared runtime product.
- Token rotation and local-only credential storage observed during sprints — apply same local-storage policy.

### No changes to OCPilot

This document does not amend OCPilot charters, roadmaps, or code.

---

## Website Factory

### Lesson

**Never build write operations before rollback proof.**

WPilot sequence that worked:

1. Read-only bridge (v0.1) — inspect proven first.
2. Backup + rollback REST (v0.2.0) — **rollback proven before any apply**.
3. Scoped replace execute (v0.3.0) — write only after recovery path validated on WPBakery pages.

### Implication for Factory handoffs

- Factory-native WordPress payloads (Mode A) should assume **rollback-capable target** before automated or semi-automated apply.
- Content mutation zones must map to a **single proven primitive** (WPilot: `page.post_content` exact-once replace) until broader targets are proven.
- DEV helper writes predating plugin REST are **historical** — Factory integrations should target formal bridge endpoints only.

### No changes to Website Factory

This document does not amend Factory contracts, pipelines, or delivery workspaces.

---

## ATLAS

### Suggested status entry

| System | Suggested ATLAS field | Value |
|--------|----------------------|-------|
| WPilot | `runtime_maturity` | `proven_content_writes` |
| WPilot | `environment_scope` | `dev_only` |
| WPilot | `plugin_version` | `0.3.0` |
| WPilot | `evidence_date` | `2026-06-19` |
| WPilot | `proof_reports` | Runtime Proof Sprint; Runtime Prototype Sprint 1–2 |

### Maturity definition (for ATLAS indexing)

**`proven_content_writes`** means:

- Plugin REST `scoped-replace` execute proven on DEV.
- Backup, validate (checksum), rollback proven via same plugin on same environment.
- Human-supervised; not production; not autonomous.

**Not implied by this status:**

- menu/widget/CSS/footer runtime
- production deployment
- multisite
- Factory Mode A pipeline integration

### No changes to ATLAS

Suggested status only — ATLAS maintainers apply if/when registry is updated.

---

## Related Documents

| Document | Role |
|----------|------|
| [WPILOT-STATE-FREEZE-2026-06-19-v1.md](../WPILOT-STATE-FREEZE-2026-06-19-v1.md) | Canonical freeze |
| [WPILOT-PROVEN-CAPABILITIES-v1.md](../WPILOT-PROVEN-CAPABILITIES-v1.md) | Evidence register |
| [milestones/WPILOT-MILESTONE-001-FIRST-PROVEN-WRITE-PATH.md](../milestones/WPILOT-MILESTONE-001-FIRST-PROVEN-WRITE-PATH.md) | Milestone record |

---

## Document Status

| Field | Value |
|-------|-------|
| Version | v1 |
| Date | 2026-06-19 |
| Modifies external systems | No |
| Implements runtime | No |
