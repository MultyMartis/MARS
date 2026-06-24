# AG-WP-001 — Operation State Machine v1

**Document type:** Operation sequencing and state machine  
**Version:** v1  
**Stage:** FW-07B  
**Date:** 2026-06-24

**Extends:** [AG-WP-001-EXECUTION-WORKFLOW-v1.md](AG-WP-001-EXECUTION-WORKFLOW-v1.md)

---

## States

`NO_INTAKE` · `INTAKE_RECEIVED` · `INPUT_VALIDATED` · `RUNTIME_VALIDATED` · `ARCHITECTURE_DRAFTED` · `ARCHITECTURE_APPROVED` · `SOURCE_SCAFFOLDED` · `CONTENT_MODEL_APPROVED` · `IMPLEMENTATION_IN_PROGRESS` · `AUTOMATED_QA` · `VISUAL_QA` · `OPERATOR_REVIEW` · `CORRECTIONS` · `ACCEPTED` · `HANDOFF_READY` · `FROZEN` · `BLOCKED` · `ROLLED_BACK`

---

## Allowed transitions (examples)

| From | To | Typical operations |
|------|-----|-------------------|
| `NO_INTAKE` | `INTAKE_RECEIVED` | external FW-06B handoff |
| `INTAKE_RECEIVED` | `INPUT_VALIDATED` | `wp.inspect.frontend_handoff` |
| `INPUT_VALIDATED` | `RUNTIME_VALIDATED` | `wp.inspect.runtime`, `wp.validate.database` |
| `RUNTIME_VALIDATED` | `ARCHITECTURE_DRAFTED` | `wp.plan.*` |
| `ARCHITECTURE_DRAFTED` | `ARCHITECTURE_APPROVED` | operator review |
| `ARCHITECTURE_APPROVED` | `SOURCE_SCAFFOLDED` | `wp.scaffold.*` (when authorized) |
| `SOURCE_SCAFFOLDED` | `CONTENT_MODEL_APPROVED` | `wp.plan.content_model` + approval |
| `IMPLEMENTATION_IN_PROGRESS` | `AUTOMATED_QA` | `wp.validate.*` |
| `AUTOMATED_QA` | `VISUAL_QA` | `wp.validate.visual_fidelity` |
| `VISUAL_QA` | `OPERATOR_REVIEW` | `wp.review.prepare` |
| `OPERATOR_REVIEW` | `ACCEPTED` | operator sign-off |
| `ACCEPTED` | `HANDOFF_READY` | WPilot handoff prep (human) |
| any | `BLOCKED` | `WP_SAFE_UNKNOWN_*`, approval failures |
| R2+ failure | `ROLLED_BACK` | `wp.rollback.prepare` |

---

## Forbidden transitions

| From | To | Reason |
|------|-----|--------|
| `INPUT_VALIDATED` | `PRODUCTION_DEPLOYMENT` | R5 prohibited |
| `NO_INTAKE` | `IMPLEMENTATION_IN_PROGRESS` | skip gates |
| `ARCHITECTURE_DRAFTED` | `SOURCE_SCAFFOLDED` | without `ARCHITECTURE_APPROVED` |
| any | staging/production mutation | AG-WP-001 foundation |

---

## Operation → state map (read-only cluster)

| State | Allowed operations |
|-------|-------------------|
| `INTAKE_RECEIVED` | `wp.inspect.frontend_handoff` |
| `INPUT_VALIDATED` | `wp.inspect.runtime`, `wp.inspect.theme`, `wp.inspect.plugin_state` |
| `RUNTIME_VALIDATED` | `wp.plan.*`, `wp.validate.php_syntax`, `wp.validate.core_checksums` |
| `AUTOMATED_QA` | all `wp.validate.*` |

---

*Operation state machine v1 — contract only.*
