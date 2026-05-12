# MARS Website Factory — Reference Run Failure & Recovery v0

**Status:** **documentation only** — **human** recovery methodology. **Not** an automated rollback engine.

**Version:** v0.

**Related:** [reference-run-sequence-v0.md](reference-run-sequence-v0.md), [project-execution-checkpoints-v0.md](project-execution-checkpoints-v0.md), [delivery-lifecycle-v0.md](delivery-lifecycle-v0.md), [failure-model-v0.md](../../workflows/failure-model-v0.md), [recovery-playbooks-v0.md](../../interfaces/recovery-playbooks-v0.md).

---

## 0. Honesty boundary

**No automatic rollback engine exists** in the Website Factory v0 documentation model. “Recovery” means **humans** follow **reported** steps, update artifacts, and re-run QA/HITL as needed. Any future Control Plane behavior is **out of scope** for this file.

---

## 1. Partial failure

**Definition:** A stage completes with **some** artifacts valid and **some** defective (e.g. partial blueprint batch).

**Recovery:**

1. **Stop** advancing checkpoint for the batch.
2. **Scope** the failure (pages/blocks/sections) in a REPORT.
3. **Revise** failed slice in owning lane or **split batch** with HITL if policy allows.
4. **Re-run** minimal QA for affected slice ([regeneration-semantics-v0.md](regeneration-semantics-v0.md) — safe partial regeneration discipline).

---

## 2. Stage rollback

**Definition:** Checkpoint reached but later evidence shows the stage must be **reopened** (e.g. wrong **site_type_id** discovered late).

**Recovery:**

1. HITL **reopen** per [approval-semantics-v0.md](approval-semantics-v0.md) / [stage-state-model-v0.md](stage-state-model-v0.md).
2. Emit **invalidation report** listing downstream artifacts now suspect ([reference-run-reporting-v0.md](reference-run-reporting-v0.md)).
3. Re-execute affected reference steps; **no** silent merge of old and new worlds.

---

## 3. QA fail recovery

| Lane | Typical recovery |
|------|------------------|
| Blueprint QA | Return **R05**; fix contract/registry issues; rerun **R06**. |
| Design QA | Return **R08** with bounded CRs; rerun **R09** until **C05** satisfied. |
| Frontend QA | Return **R11**; fix src; rerun **R12**; refresh validation inputs. |
| Final validation | Targeted fixes in owning stages; full or partial revalidation per risk. |

Waivers require **HITL** + audit trail ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)).

---

## 4. Stale artifact recovery

**Definition:** Downstream consumed an artifact that was superseded without proper handoff.

**Recovery:**

1. **Freeze** further delivery if package already built — assess blast radius.
2. Mark offending consumption in **invalidation report**.
3. Regenerate downstream artifacts from correct **parent** lineage ([artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md)).
4. Re-validate per **C07** rules.

---

## 5. Freeze break recovery

**Definition:** A change occurred that violates an approved freeze ([semantic-freeze-semantics-v0.md](semantic-freeze-semantics-v0.md)).

**Recovery:**

1. **Stop** line immediately for dependent lanes.
2. HITL-approved **reopen** with revised scope.
3. Full invalidation analysis → rerun QA gates that the change touches (often **all** downstream QA).

---

## 6. Delivery rollback

**Definition:** Post-release defect or wrong package shipped.

**Recovery:**

- Follow **operational** playbooks (hosting revert, DNS, artifact swap) — **project-specific**, **SAFE UNKNOWN** in factory docs.
- Document incident in **delivery report** addendum; do **not** claim automated rollback.

---

## 7. Escalation recovery

**Definition:** **NEED HUMAN APPROVAL** / **SECURITY RISK** / **STRUCTURE CHANGE** stuck unresolved.

**Recovery:**

1. **Escalation report** names blocker owner and deadline ([reference-run-reporting-v0.md](reference-run-reporting-v0.md)).
2. Governance forum decision recorded.
3. Resume only after REPORT closes the escalation with allowed path.

---

*End of Reference Run Failure & Recovery v0.*
