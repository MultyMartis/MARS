# MARS Website Factory — Validation escalation model v0

**Status:** **documentation only** — **when validation escalates** and **how it maps** to governance signals. **Not** routing code, **not** ticketing integration.

**Version:** v0.

**Related:** [validation-failure-semantics-v0.md](validation-failure-semantics-v0.md), [orchestration-signals-v0.md](orchestration-signals-v0.md), [`../../governance/system-signals-dictionary.md`](../../governance/system-signals-dictionary.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md).

---

## 1. Escalation triggers (examples)

| Trigger | Typical signal / outcome |
|---------|-------------------------|
| **V3** / **critical** finding | **NEED HUMAN APPROVAL** and/or **SECURITY RISK** |
| Policy / secrets / scope escape suspicion | **SECURITY RISK** |
| Plan or blueprint decomposition wrong | **STRUCTURE CHANGE** |
| Missing mandatory binding (no approver, no artifact) | **UNKNOWN** |
| Unverified but bounded gap | **SAFE UNKNOWN** (with explicit “what would verify”) |
| Freeze break attempted without authority | **NEED HUMAN APPROVAL** + freeze semantics per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md) |
| Contradictory evidence | **NEED HUMAN APPROVAL** or **STRUCTURE CHANGE** depending on whether plan is wrong vs data conflict |

---

## 2. Escalation severity

Align with [validation-result-semantics-v0.md](validation-result-semantics-v0.md): **V0–V3** drives default escalation tier. **V3** + policy → treat as highest tier until human disposition.

---

## 3. Escalation authority

- **Humans** named in HITL matrices own disposition for **NEED HUMAN APPROVAL**.
- **Security** roles own **SECURITY RISK** paths per [`../../security/approval-gates.md`](../../security/approval-gates.md) when applicable.
- **Validator** and specialist QA **raise** escalations; they **do not** replace security or legal sign-off.

---

## 4. Escalation routing (documentation sense)

“Routing” means **which role reads next** in runbooks and REPORT sections — not message bus routing. Cross-ref [workflow-map.md](workflow-map.md), [reporting-standard-v0.md](reporting-standard-v0.md).

---

## 5. Escalation freeze

- An open **SECURITY RISK** or unresolved **NEED HUMAN APPROVAL** on a **blocking** finding **should** place the affected scope in **blocked** validation state per [validation-lifecycle-v0.md](validation-lifecycle-v0.md).
- **Freeze** may be applied as a **governance** action to stop mutation while escalation resolves — per [semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md).

---

## 6. Signal mapping table

| Factory escalation posture | Governance signal(s) |
|----------------------------|----------------------|
| Human must sign off | **NEED HUMAN APPROVAL** |
| Suspected policy / injection / danger | **SECURITY RISK** |
| Re-scope / replan required | **STRUCTURE CHANGE** |
| Hard missing binding | **UNKNOWN** |
| Honest unverified slice | **SAFE UNKNOWN** |

---

*Last updated: 2026-05-12.*
