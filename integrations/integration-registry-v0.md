# MARS — Integration Registry v0

**Status:** documented — central registry model for external integrations in MARS documentation. No live connectors, no configured endpoints, and no runtime integration implementation are claimed in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Provide one documentation SoT for external integration metadata and lifecycle posture.
- Standardize how integration entries are described before any real connector exists.
- Keep integration scope auditable across tool layer, execution bridge, and security governance.

**Explicit v0 boundary:** NO real integrations are configured in this repository.

---

## 2. Registry fields (v0)

| Field | Description |
|-------|-------------|
| **integration_id** | Stable unique identifier for the integration row (for example: `integration.crm.primary`). |
| **name** | Human-readable integration name. |
| **type** | Integration class: `api`, `webhook`, `file`, `automation`, or another documented class. |
| **direction** | Data flow direction: `inbound`, `outbound`, or `bidirectional`. |
| **status** | Lifecycle state: `planned`, `active`, `deprecated`. |
| **auth_type** | Authentication posture (for example: `token`, `oauth`, `none`, `mTLS`, `unknown`). |
| **data_scope** | What data categories are exchanged (for example: metadata-only, task outputs, notifications). |
| **risk_level** | Relative risk posture (`low`, `medium`, `high`, `critical`) aligned with security/risk review. |
| **approval_required** | Whether HITL approval is required before execution (`yes`/`no`). |

---

## 3. Lifecycle (v0)

| Stage | Meaning |
|-------|---------|
| **planned** | Integration is documented but not implemented or configured. |
| **active** | Integration is allowed by governance/contract posture (still not proof of runtime implementation unless evidenced elsewhere). |
| **deprecated** | Integration is retained for history/migration and should not be used for new flows. |

**Transition rule:** lifecycle transitions must be reviewed with [../governance/risk-register.md](../governance/risk-register.md) and reflected in governance updates when material.

---

## 4. Relation to other layers

| Artefact / layer | Relation |
|------------------|----------|
| [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md) | Integration invocation must align with tool-contract envelope and signal semantics. |
| [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) | Integration calls are routed through execution bridge boundary; no direct bypass path in v0 design. |
| [../security/threat-model-v0.md](../security/threat-model-v0.md) | Registry rows map to threat classes (exfiltration, injection, misuse). |
| [../security/approval-gates.md](../security/approval-gates.md) | `approval_required` posture and HITL obligations align with approval model. |

---

## 5. SAFE UNKNOWN

- Concrete endpoint URLs, secrets, API credentials, and SDK bindings are out of scope for v0.
- Transport-level protocol details are SAFE UNKNOWN until implementation contracts are introduced.

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Integration Registry v0 created: purpose, required fields, lifecycle, and layer relations (documentation-only). |

---

*End of Integration Registry v0.*
