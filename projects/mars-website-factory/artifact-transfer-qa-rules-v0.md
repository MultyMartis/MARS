# MARS Website Factory — Artifact Transfer QA Rules v0

**Status:** **documentation only** — **QA discipline for the transfer layer** (envelopes, routes, lineage, publication, consumption). **Not** an automated test suite, **not** CI gates unless a project adds them (**SAFE UNKNOWN**).

**Version:** v0.

**Related:** [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md), [artifact-envelope-model-v0.md](artifact-envelope-model-v0.md), [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md), [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md), [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md), [semantic-qa-rules-v0.md](semantic-qa-rules-v0.md), [safe-unknown-boundary.md](safe-unknown-boundary.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md).

---

## 1. Finding classes

| Finding | Description |
|---------|-------------|
| **stale_transfer** | Downstream depends on superseded/invalidated/expired upstream without update. |
| **orphan_transfer** | **dependencies** / **lineage** unresolved. |
| **invalid_route** | Transfer violates [artifact-routing-rules-v0.md](artifact-routing-rules-v0.md) (e.g. skip design). |
| **broken_lineage** | Circular parent, missing parent, contradiction vs body authorship. |
| **approval_mismatch** | **approval_state** wider than HITL record or **fake approval inheritance**. |
| **freeze_mismatch** | Work proceeds as if frozen when **freeze_state** is not frozen, or vice versa. |
| **semantic_mismatch** | **semantic_state** inconsistent with semantic layer findings. |
| **delivery_mismatch** | Export manifest ≠ actual frozen baselines; missing rollback notes at G7. |

---

## 2. Severity

| Level | Typical handling |
|-------|------------------|
| **P0 / Blocker** | **DELIVERY BLOCKED**; **invalid_route**, **approval_mismatch** on release path, **delivery_mismatch**, open **SECURITY RISK**. |
| **P1** | **Stage blocked** until fixed; **orphan_transfer**, **broken_lineage**, **freeze_mismatch**. |
| **P2** | **Conditional** proceed with bounded CR + HITL; **stale_transfer** on non-release pages if isolated. |
| **P3 / Info** | Documentation cleanup; does not block if no downstream reliance. |

Exact numeric severities align with project QA matrix ([reference-project-qa-matrix-v0.md](reference-project-qa-matrix-v0.md)) when used.

---

## 3. Blocking semantics

- **Blocker** → forward **route** **forbidden** until resolved or **waived** per [qa-gating-semantics-v0.md](qa-gating-semantics-v0.md).  
- **Validator** (when used) may cite these classes as **cross-cutting** checks — depth **TBD** per [agent-map.md](agent-map.md).

---

## 4. Waiver rules

Waivers **require**:

1. Named **approver** + date.  
2. **Residual risk** statement.  
3. **Scope** bound (which pages/routes).  
4. **Expiration** where applicable.

**Forbidden:** blanket waiver for **invalid_route** or **fake approval inheritance**.

---

## 5. SAFE UNKNOWN handling

When **envelope** completeness cannot be verified (missing **revision_id** policy, unclear **payload_reference**):

| Step | Action |
|------|--------|
| 1 | Emit **SAFE UNKNOWN** with explicit assumptions per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md). |
| 2 | **Downgrade** publication class to **review** until resolved — **unless** HITL accepts bounded risk. |
| 3 | Record in **risk summary** for delivery candidate ([delivery-lifecycle-v0.md](delivery-lifecycle-v0.md)). |

---

## 6. QA artifact output (recommended fields)

For transfer-focused QA REPORTs (conceptual):

- `transfer_findings[]` with `{ class, severity, evidence, affected_artifact_ids, suggested_route }`  
- `blocking_transfer: boolean`  
- `waivers[]` if any

**Not** mandated wire format — **prose + tables** suffice in v0.

---

## 7. Non-claims

- **Not** automated envelope linter in-repo.  
- **Not** real-time bus monitoring.

---

## 8. Revision history

| Date | Change |
|------|--------|
| 2026-05-12 | **v0** — initial transfer QA rules (documentation only). |
