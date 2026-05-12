# MARS Website Factory — Artifact Transfer Prompt Rules v0

**Status:** **documentation only** — how artifacts move between **prompts and stages** in the factory. **Not** a runtime artifact bus, **not** evidence of automated handoffs, **not** a wire format.

**Version:** v0.

**Related:** [artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md), [artifact-types-v0.md](artifact-types-v0.md), [website-factory-workflow-v0.md](website-factory-workflow-v0.md), [page-blueprint-contract-v0.md](page-blueprint-contract-v0.md), [design-handoff-contract-v0.md](design-handoff-contract-v0.md), [frontend-handoff-contract-v0.md](frontend-handoff-contract-v0.md), [qa-result-payloads-v0.md](qa-result-payloads-v0.md), [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md), [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md), [artifact-bus-overview-v0.md](artifact-bus-overview-v0.md) (Artifact Bus Layer v0 — envelope/routing/transfer discipline; **documentation only**).

---

## 1. Purpose

Factory stages produce **logical artifacts** ([artifact-types-v0.md](artifact-types-v0.md)) that must cross prompt boundaries cleanly. This document defines:

- how prompts **reference** artifacts,
- which artifact sections are **immutable** after approval,
- how **approval inherits** downstream,
- how **revisions** are handled,
- how **QA findings** inherit,
- how **dependency discipline** is enforced.

It is **prose discipline**, not a binding format.

---

## 2. Artifact reference rules

A prompt that consumes an artifact MUST reference it by:

1. **Artifact class** (per [artifact-types-v0.md](artifact-types-v0.md)).
2. **Artifact_id** (stable string, per project convention).
3. **Contract anchor** (e.g. `page-blueprint-contract-v0.md` field name).
4. **Mutability state** at the moment of consumption (mutable / frozen / superseded).

Forbidden:

- referencing an artifact by paraphrase only (“the blueprint we discussed”);
- consuming a draft artifact as if it were approved;
- consuming a superseded artifact silently.

If the referenced artifact is missing or ambiguous → emit **UNKNOWN** or **SAFE UNKNOWN** per [safe-unknown-prompt-rules-v0.md](safe-unknown-prompt-rules-v0.md).

---

## 3. How artifacts move between stages

The canonical artifact flow follows [website-factory-workflow-v0.md](website-factory-workflow-v0.md) §“Artifact flow map”:

```text
Intake artifact
   → Strategy + SEO strategy artifacts
   → IA artifact
   → Blueprint artifact
   → QA artifact (blueprint slice)
   → Design handoff artifact
   → Design artifact
   → QA artifact (design lane)
   → Frontend handoff artifact
   → Frontend production artifact
   → QA artifact (frontend lane)
   → Validation artifact (final)
   → Approval artifact
   → Delivery artifact
```

Each arrow is a **prompt boundary**. The prompt that produces the downstream artifact:

- declares its **artifacts in** (upstream references),
- declares its **artifacts out** (downstream production),
- preserves identifiers and contract anchors,
- does **not** rewrite upstream artifacts inline.

---

## 4. Immutable vs mutable sections

Artifacts have **mutability states**. The transfer rules below align with [artifact-types-v0.md](artifact-types-v0.md):

| Artifact class | Mutable while | Becomes immutable when |
|----------------|----------------|------------------------|
| Intake | discovery is open | G1 approves scope_in / scope_out |
| Strategy / SEO | hypothesis stage | G2 approves narrative |
| IA | drafting | G3 approves sitemap/templates |
| Blueprint | drafting | G3 batch approval |
| Design handoff | pack assembly | design lead signs off |
| Design | iteration | G5 design freeze |
| Frontend handoff | drafting | tech lead approves before S11 |
| Frontend production | code under change control | release tag intent at G6 |
| QA | within a single run | verdict filed for that run id |
| Validation | within S13 run | go/no-go recommendation filed |
| Approval | n/a | always immutable once recorded |

**Immutable-section rule:** when a downstream prompt receives an artifact in an **immutable** state, it **must not** modify the artifact body. Changes require a **revision** (see §6).

---

## 5. Approval inheritance

Approval at a gate cascades **downstream only** for the **scope that was approved**:

- G1 approves intake scope → downstream stages may rely on `scope_in` / `scope_out` as immutable.
- G2 approves strategy/SEO → blueprint stage may rely on narrative + intent as immutable.
- G3 approves IA + blueprint batch → design handoff may rely on URLs, templates, block ordering as immutable.
- G5 approves design freeze → frontend handoff may rely on visual baseline as immutable.
- G6 approves frontend PR / file set → final validation may rely on the file set as immutable.
- G7 approves release → delivery may package the approved baseline.

**Forbidden:** treating a **partial** or **conditional** approval as a full freeze. Conditional approvals must list bounded CR items; downstream prompts must respect them.

**Re-gate rule:** if a downstream prompt discovers that an upstream artifact would need to change to satisfy its objective, the prompt must **stop** and request a **re-gate** of the appropriate upstream stage.

---

## 6. Revision handling

Revisions occur **after** an artifact has been approved or frozen. Rules:

| Revision type | Trigger | Behavior |
|---------------|---------|----------|
| **Bounded CR** (correction request) | QA finding within tolerance | New revision of the same artifact_id (e.g. `_v1` → `_v1.1`); re-gate at the **same** gate; downstream artifacts based on the old revision are invalidated where they intersect the change. |
| **Structure change** | Contract shape needs to shift | `STRUCTURE CHANGE` signal; new artifact_id (or major version bump); upstream stages re-plan affected slices. |
| **Security override** | `SECURITY RISK` finding | Stop line; emergency revision with HITL; never silent. |
| **Supersede** | Replacing a baseline entirely | New artifact_id; old one marked superseded; downstream consumers re-issued prompts against the new id. |

A revision **never** silently mutates an immutable section without:

- a recorded gate decision,
- an updated artifact identifier or revision tag,
- an updated REPORT entry listing the artifact change.

---

## 7. QA inheritance

QA findings ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)) follow the artifact:

- **Open findings** attach to the artifact_id and revision; they persist across prompts until resolved.
- **Waivers** are recorded per finding, with named approver and date; they do **not** detach the finding from the artifact.
- **Resolved findings** become part of the artifact’s **QA history**; they are not deleted.
- **Cross-lane findings** propagate: a Frontend QA finding that exposes a Blueprint contract gap must be referenced in a STRUCTURE CHANGE signal back to the blueprint, not silently fixed in frontend.

A downstream prompt that consumes an artifact MUST also reference its **open QA state**:

- if open blockers exist and are not waived, the prompt cannot proceed,
- if open warns exist, the prompt either resolves them in scope or marks them as known-state SAFE UNKNOWN with rationale.

---

## 8. Artifact references inside prompts

A well-formed prompt names artifacts the same way [prompt-structure-standard-v0.md](prompt-structure-standard-v0.md) prescribes:

| Section | Artifact discipline |
|---------|---------------------|
| `context` | Stage anchor + relevant upstream artifact_ids. |
| `artifacts in` | One row per artifact: class, artifact_id, mutability state, contract anchor. |
| `artifacts out` | One row per artifact to produce: class, expected artifact_id, target path or document, contract anchor. |
| `escalation rules` | What to do when artifact references resolve to unknowns or contradictions. |

Drift between `artifacts in` and what the prompt actually consumes is a **scope violation**.

---

## 9. Dependency discipline

Artifacts have **dependency chains**. Discipline rules:

- A prompt may consume an artifact only if its **direct upstream chain** is satisfied (approved or in an explicitly allowed mutable state).
- A prompt that needs an artifact from a stage **earlier** than its parent must reference it explicitly — no silent reach-throughs.
- Cross-project artifact references (e.g. a Website Factory prompt referencing MetaBOT or another project) require explicit acknowledgment and are typically **SAFE UNKNOWN** for behavior unless a documented bridge exists ([safe-unknown-boundary.md](safe-unknown-boundary.md)).

---

## 10. Tie to workflow v0

This document **does not** redefine the workflow stages. It refines what crosses the **stage boundary** as artifacts move:

| Workflow concept | Transfer rule applied |
|------------------|------------------------|
| `input artifacts` row (per stage) | becomes `artifacts in` in the stage prompt |
| `output artifacts` row | becomes `artifacts out` |
| `HITL requirements` | gates approval inheritance |
| `SAFE UNKNOWN escalation` | governs ambiguous transfers |
| `downstream dependencies` | governs dependency discipline |

---

## 11. Tie to handoff contracts

The two key handoff contracts each have an **explicit transfer point**:

| Contract | Transfer point |
|----------|----------------|
| [Design Handoff Contract v0](design-handoff-contract-v0.md) | Blueprint (approved) → Design production input. Frontend-side references must come **after** design freeze. |
| [Frontend Handoff Contract v0](frontend-handoff-contract-v0.md) | Frozen design + approved blueprint → Frontend production input. Build/CI references default to SAFE UNKNOWN unless evidenced. |

Both contracts are **field vocabularies**, not wire formats; transfer is **prose-anchored** in v0.

---

## 12. Tie to artifact architecture layer

The Artifact Architecture Layer v0 ([artifact-architecture-overview-v0.md](artifact-architecture-overview-v0.md)) defines **terms** (workflow / agent / artifact / payload / contract / registry). This document uses those terms:

- “Artifact” = logical deliverable.
- “Contract” = field vocabulary the artifact follows.
- “Payload” = the field-level content shape; conceptual in v0.
- “Registry” = canonical rows the artifact references.

Transfer rules apply **to the artifact**, anchored **to its contract**, and may **reference** registries — but transfer does **not** mutate registries silently. Registry amendments require governance review.

---

## 13. Non-claims

- This document does **not** ship an artifact bus, queue, or persistence layer.
- It does **not** imply automated artifact validation.
- It does **not** assume an LLM enforces these rules.

What it **does** do is define **how prompts speak about artifacts** so transfers are **traceable** and **honest**.

---

## 14. Revision history

| Date | Change |
|------|--------|
| 2026-05-11 | **v0** — initial artifact transfer prompt rules (documentation only). |
