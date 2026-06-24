# AG-WP-001 — Risk and Approval Matrix v1

**Document type:** Risk and approval model  
**Version:** v1  
**Stage:** FW-07A  
**Date:** 2026-06-24

**Extends:** [FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md](../FORGE-WORDPRESS-COMMAND-AND-OPERATION-MODEL-v1.md) (FW-03 risk classes refined for AG-WP-001)

**Rule:** No operation may silently escalate risk class.

---

## R0 — Read-only inspection

| Examples | `inspect_*` operations |
|----------|------------------------|
| Inspect files, routes, plugins, runtime, handoff | |

| Approval | Pre-authorized in approved local runtime context |
| Rollback | N/A |
| Agent self-approve | N/A |

---

## R1 — Draft generation

| Examples | Architecture proposal, content model, plugin recommendation, test plan |
|----------|-----------------------------------------------------------------------|

| Approval | Human review **before** implementation |
| Rollback | Discard draft artifacts |
| Agent self-approve | **Forbidden** |

---

## R2 — Local reversible source change

| Examples | Theme code, plugin code, ACF JSON, tests |
|----------|------------------------------------------|

| Approval | Approved plan + Git checkpoint + local backup |
| Rollback | Git revert + file restore |
| Agent self-approve | **Forbidden** |

---

## R3 — Local runtime mutation

| Examples | Plugin activation, DB schema change, content migration, option changes |
|----------|-----------------------------------------------------------------------|

| Approval | **Explicit operator approval** |
| Rollback | DB backup + plugin inventory restore |
| Agent self-approve | **Forbidden** |

---

## R4 — Staging mutation

| Examples | Deploy to staging, staging DB import, staging plugin updates |
|----------|--------------------------------------------------------------|

| Approval | Explicit operator approval + backup + rollback plan |
| Rollback | Staging restore per WPilot/ops charter |
| Agent self-approve | **Forbidden** |
| AG-WP-001 foundation | **NOT AUTHORIZED** without future charter |

---

## R5 — Production mutation

| Default | **NOT AUTHORIZED FOR AG-WP-001 FOUNDATION** |
|---------|---------------------------------------------|

All production changes remain **human + WPilot/ops** domain until separate promotion charter.

---

## Escalation matrix

| From | To | Requires |
|------|-----|----------|
| R0 | R1 | Task scope includes design |
| R1 | R2 | Operator architecture approval |
| R2 | R3 | Explicit operator approval + backup |
| R3 | R4 | Staging charter + operator |
| Any | R5 | **Denied** at foundation stage |

---

## Audit evidence

Every R2+ operation must leave:

- Operation ID
- Timestamp
- Input hash / commit ref
- Operator approval reference (when required)
- Rollback pointer

---

*Risk matrix v1 — production forbidden at foundation.*
