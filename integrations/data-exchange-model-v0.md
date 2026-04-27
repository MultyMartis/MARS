# MARS — Data Exchange Model v0

**Status:** documented — data exchange patterns for integration interactions. No runtime pipeline, adapters, or transport implementation are provided in-repo.

**Version:** v0. Revisable per [../governance/versioning-model.md](../governance/versioning-model.md).

---

## 1. Purpose

- Define integration data exchange types used across MARS contracts.
- Set non-bypass rules for validation and memory safety at integration boundaries.
- Keep exchange behavior system-agnostic and documentation-first.

---

## 2. Exchange types (v0)

| Type | Description |
|------|-------------|
| **synchronous** | Request-response exchange where caller waits for immediate outcome. |
| **asynchronous** | Deferred processing with callback/event or later retrieval of result. |
| **batch** | Grouped transfer of multiple records in one logical operation window. |

---

## 3. Data flow rules (normative v0)

1. **No direct memory write** — integration exchange must not directly mutate durable memory surfaces outside policy boundaries.
2. **No validation bypass** — inbound and outbound payloads must pass documented validation gates before use.
3. **Traceability required** — exchanges should retain `run_id` or equivalent correlation context for auditability.

---

## 4. Relation to other artefacts

| Artefact | Relation |
|----------|----------|
| [../memory/memory-write-policy-v0.md](../memory/memory-write-policy-v0.md) | Governs when integration-derived data can become durable memory. |
| [../tools/tool-validation-rules-v0.md](../tools/tool-validation-rules-v0.md) | Defines validation posture to apply before integration payload consumption. |
| [../tools/tool-contract-v0.md](../tools/tool-contract-v0.md) | Provides invocation/output envelope semantics used by integration exchanges. |

---

## 5. SAFE UNKNOWN

- Serialization format, transport protocol, and concrete message schemas are not fixed in v0.
- Delivery guarantees (at-most-once, at-least-once, exactly-once) are SAFE UNKNOWN until runtime design.

---

## 6. Changelog (documentation)

| Date | Change |
|------|--------|
| 2026-04-28 | Data Exchange Model v0 created: synchronous/asynchronous/batch patterns and non-bypass data flow rules. |

---

*End of Data Exchange Model v0.*
