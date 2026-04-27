# MARS — Integration Contract v0

**Status:** documented — standard interface contract for integration execution in MARS. No SDK bindings, no live adapters, and no real external calls are implemented by this file.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md) and [../governance/master-build-map.md](../governance/master-build-map.md).

---

## 1. Purpose

- Define one consistent request/response envelope for external integrations.
- Ensure integrations remain compatible with tool-layer and execution-bridge contract patterns.
- Prevent ad-hoc integration interfaces that bypass validation, signals, or governance controls.

---

## 2. Input envelope (normative v0)

| Field | Required | Description |
|-------|----------|-------------|
| **request_payload** | yes | Integration-specific request data for one invocation. |
| **context** | yes | Correlation and policy context (task/run/project references, execution constraints). |
| **run_id** | yes | Correlation id for the current run; used for traceability and observability links. |

---

## 3. Output envelope (normative v0)

| Field | Required | Description |
|-------|----------|-------------|
| **response** | yes | Primary integration response payload (structured or opaque). |
| **status** | yes | Invocation outcome classification (`success`, `failure`, `partial`). |
| **artifacts** | no | Produced references (files, URIs, export pointers) when applicable. |
| **signals** | yes | Canonical system signals required by policy or outcome context. |

---

## 4. Contract rules

1. **Must go through execution bridge** — integration invocation must transit [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) and must not use undocumented direct-call paths.
2. **Must respect tool contract patterns** — envelope semantics, status mapping, and signal posture align with [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md).
3. **No silent policy bypass** — permission/approval failures must emit explicit outcomes/signals.
4. **Documentation-only boundary** — this contract defines interface shape, not implementation.

---

## 5. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md) | Integration interface mirrors tool contract I/O and status/signal posture. |
| [../mars-runtime/execution-bridge-v0.md](../mars-runtime/execution-bridge-v0.md) | Bridge is normative dispatch and return boundary for integration calls. |

---

## 6. SAFE UNKNOWN

- Concrete schemas for individual systems are intentionally not defined in v0.
- Auth headers, token exchange, retry backoff, and endpoint topology are SAFE UNKNOWN until implementation-stage design.

---

## 7. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Integration Contract v0 created: input/output envelope, mandatory bridge transit, tool-contract alignment. |

---

*End of Integration Contract v0.*
