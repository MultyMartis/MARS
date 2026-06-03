# Lifecycle Log Alignment v1

**Date:** 2026-06-03  
**Lane:** B — MARS Cleanup Wave 2B  
**Upstream:** [lifecycle-log-deep-review-v2.md](../discoveries/lifecycle-log-deep-review-v2.md), Wave 2A lifecycle backfill  
**Architect decision:** Lifecycle Log = **Key Event History** + optional **Lifecycle Tracking Mode** for long operations

---

## Normative model

| Mode | When | SoT |
|------|------|-----|
| **Key Event History** (default) | Material registry/governance/stage changes | `logs/lifecycle-log.md` append-only events |
| **Lifecycle Tracking Mode** (optional) | Long-running human operations needing temporal audit | Same file — extended `description` or dedicated tracking section; **not** mandatory for normal work |

**Distinction:**

- **Normal work** (task REPORT, cleanup evidence, program notes) **≠** mandatory lifecycle append
- **Long operation** (multi-session stabilization, large intake) **may** use Lifecycle Tracking Mode — operator choice

---

## Three-log model (reinforced)

| Log | Role |
|-----|------|
| `logs/lifecycle-log.md` | Governance **events** |
| `logs/cleanup/` | Ecosystem **audit / classification** evidence |
| `logs/releases/` | Baseline **publication** checkpoints |

---

## Actions taken

| Surface | Change |
|---------|--------|
| `logs/lifecycle-log.md` | Header: Key Event History + Lifecycle Tracking Mode |
| `governance/registry-architecture.md` | Lifecycle kinds + three-log cross-ref |
| `logs/cleanup/README.md` | Lifecycle alignment pointer |
| `governance/ecosystem-topology-index.md` | Lifecycle quick-ref note |

**Not done:** automation; registry→lifecycle sync; mandatory append policy (L-03 deferred).

---

## Files changed

- `logs/lifecycle-log.md`
- `governance/registry-architecture.md`
- `logs/cleanup/README.md`
- `governance/ecosystem-topology-index.md`

---

*Lifecycle alignment v1 — Wave 2B evidence.*
