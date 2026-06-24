# Forge WordPress — Agent Documents

**Subsystem:** Forge WordPress  
**Agent ID:** `AG-WP-001`  
**Stage:** FW-07B — COMPLETE

---

## Canonical agent pack

| # | Document | Purpose |
|---|----------|---------|
| 0 | [AG-WP-001-CURRENT-ARCHITECTURE-AUDIT-v1.md](AG-WP-001-CURRENT-ARCHITECTURE-AUDIT-v1.md) | Architecture audit at FW-07A |
| 1 | [AG-WP-001-WORDPRESS-IMPLEMENTATION-AGENT-CARD-v1.md](AG-WP-001-WORDPRESS-IMPLEMENTATION-AGENT-CARD-v1.md) | Canonical agent card |
| 2 | [AG-WP-001-APPROVED-FRONTEND-INPUT-CONTRACT-v1.md](AG-WP-001-APPROVED-FRONTEND-INPUT-CONTRACT-v1.md) | Input contract |
| 3 | [AG-WP-001-WORDPRESS-IMPLEMENTATION-OUTPUT-CONTRACT-v1.md](AG-WP-001-WORDPRESS-IMPLEMENTATION-OUTPUT-CONTRACT-v1.md) | Output contract |
| 4 | [AG-WP-001-WORDPRESS-IMPLEMENTATION-MODE-DECISION-v1.md](AG-WP-001-WORDPRESS-IMPLEMENTATION-MODE-DECISION-v1.md) | Theme mode decision framework |
| 5 | [AG-WP-001-THEME-FUNCTIONALITY-SEPARATION-CONTRACT-v1.md](AG-WP-001-THEME-FUNCTIONALITY-SEPARATION-CONTRACT-v1.md) | Theme vs functionality plugin |
| 6 | [AG-WP-001-CONTENT-MODEL-AND-EDITOR-GOVERNANCE-CONTRACT-v1.md](AG-WP-001-CONTENT-MODEL-AND-EDITOR-GOVERNANCE-CONTRACT-v1.md) | Content model and editor |
| 7 | [../registries/FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md](../registries/FORGE-WORDPRESS-AG-WP-001-OPERATION-REGISTRY-v1.md) | Typed operations (contract level) |
| 8 | [AG-WP-001-RISK-AND-APPROVAL-MATRIX-v1.md](AG-WP-001-RISK-AND-APPROVAL-MATRIX-v1.md) | Risk and approval |
| 9 | [AG-WP-001-QA-AND-ACCEPTANCE-GATES-v1.md](AG-WP-001-QA-AND-ACCEPTANCE-GATES-v1.md) | QA gates |
| 10 | [AG-WP-001-FAILURE-RECOVERY-AND-ROLLBACK-CONTRACT-v1.md](AG-WP-001-FAILURE-RECOVERY-AND-ROLLBACK-CONTRACT-v1.md) | Failure and rollback |
| 11 | [AG-WP-001-WEBSITE-FACTORY-INTEGRATION-CONTRACT-v1.md](AG-WP-001-WEBSITE-FACTORY-INTEGRATION-CONTRACT-v1.md) | Website Factory integration |
| 12 | [AG-WP-001-MLI-RUNTIME-INTEGRATION-CONTRACT-v1.md](AG-WP-001-MLI-RUNTIME-INTEGRATION-CONTRACT-v1.md) | MLI runtime integration |
| 13 | [AG-WP-001-WPILOT-HANDOFF-CONTRACT-v1.md](AG-WP-001-WPILOT-HANDOFF-CONTRACT-v1.md) | WPilot handoff |
| 14 | [AG-WP-001-WORDPRESS-NATIVE-AI-INTERFACES-BOUNDARY-v1.md](AG-WP-001-WORDPRESS-NATIVE-AI-INTERFACES-BOUNDARY-v1.md) | Future WP-native AI boundaries |
| 15 | [AG-WP-001-EXECUTION-WORKFLOW-v1.md](AG-WP-001-EXECUTION-WORKFLOW-v1.md) | Execution workflow |
| 16 | [AG-WP-001-FP-0002-PILOT-READINESS-MAP-v1.md](AG-WP-001-FP-0002-PILOT-READINESS-MAP-v1.md) | FP-0002 pilot readiness |

## FW-07B typed operations pack

| # | Document | Purpose |
|---|----------|---------|
| B1 | [../schemas/AG-WP-001-OPERATION-CONTRACT-SCHEMA-v1.json](../schemas/AG-WP-001-OPERATION-CONTRACT-SCHEMA-v1.json) | Operation contract JSON schema |
| B2 | [../operations/ag-wp-001/operations-v1.json](../operations/ag-wp-001/operations-v1.json) | Machine-readable operation registry |
| B3 | [AG-WP-001-FW-07B-OPERATION-RECONCILIATION-v1.md](AG-WP-001-FW-07B-OPERATION-RECONCILIATION-v1.md) | FW-07A → canonical ID reconciliation |
| B4 | [AG-WP-001-FAILURE-CODE-REGISTRY-v1.md](AG-WP-001-FAILURE-CODE-REGISTRY-v1.md) | Failure codes |
| B5 | [AG-WP-001-TOOL-CAPABILITY-MATRIX-v1.md](AG-WP-001-TOOL-CAPABILITY-MATRIX-v1.md) | Tool capability audit |
| B6 | [AG-WP-001-TOOL-BINDING-CONTRACT-v1.md](AG-WP-001-TOOL-BINDING-CONTRACT-v1.md) | Tool binding contract |
| B7 | [AG-WP-001-FILESYSTEM-SCOPE-CONTRACT-v1.md](AG-WP-001-FILESYSTEM-SCOPE-CONTRACT-v1.md) | Filesystem scope |
| B8 | [AG-WP-001-COMMAND-EXECUTION-CONTRACT-v1.md](AG-WP-001-COMMAND-EXECUTION-CONTRACT-v1.md) | Command execution |
| B9 | [AG-WP-001-APPROVAL-TOKEN-CONTRACT-v1.md](AG-WP-001-APPROVAL-TOKEN-CONTRACT-v1.md) | Approval tokens |
| B10 | [AG-WP-001-EXECUTION-ENVELOPE-CONTRACT-v1.md](AG-WP-001-EXECUTION-ENVELOPE-CONTRACT-v1.md) | Execution envelope |
| B11 | [AG-WP-001-OPERATION-STATE-MACHINE-v1.md](AG-WP-001-OPERATION-STATE-MACHINE-v1.md) | State machine |
| B12 | [AG-WP-001-IDEMPOTENCY-AND-REPEATABILITY-CONTRACT-v1.md](AG-WP-001-IDEMPOTENCY-AND-REPEATABILITY-CONTRACT-v1.md) | Idempotency |
| B13 | [AG-WP-001-SECRET-BOUNDARY-CONTRACT-v1.md](AG-WP-001-SECRET-BOUNDARY-CONTRACT-v1.md) | Secret boundary |
| B14 | [AG-WP-001-FP-0002-PILOT-SAFE-OPERATION-PROFILE-v1.md](AG-WP-001-FP-0002-PILOT-SAFE-OPERATION-PROFILE-v1.md) | Pilot-safe profile |
| B15 | [../tools/validate-ag-wp-001-operation-contracts.mjs](../tools/validate-ag-wp-001-operation-contracts.mjs) | Contract validator |
| B16 | [AG-WP-001-FW-07B-CONTRACT-VALIDATION-REPORT-v1.md](AG-WP-001-FW-07B-CONTRACT-VALIDATION-REPORT-v1.md) | Validation report |
| B17 | [AG-WP-001-FW-07B-READINESS-ASSESSMENT-v1.md](AG-WP-001-FW-07B-READINESS-ASSESSMENT-v1.md) | Readiness assessment |

---

## MARS registry cross-links

- [agents/registry.md](../../../../agents/registry.md) §4.1 — `wordpress_implementation_agent`
- [agents/cards/wordpress-implementation-agent-v1.md](../../../../agents/cards/wordpress-implementation-agent-v1.md) — catalog card

---

## Lifecycle honesty

```text
AG-WP-001:
REGISTERED (FW-07A + FW-07B)

Operation contracts:
DEFINED (42 ops; validator AVAILABLE)

Runtime state:
NOT ACTIVE

Production authority:
NONE

Pilot execution:
BLOCKED until Frontend Production Pass + FW-06B
```

---

*Agent documents — documentation only; not autonomous runtime.*
