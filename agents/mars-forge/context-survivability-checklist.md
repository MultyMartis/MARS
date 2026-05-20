# Context Survivability Checklist - MARS Forge

**Status:** **documented** - Forge overlay checklist for human-supervised context survivability and compression integrity QA.  
**Not:** autonomous memory AI, runtime persistence, automatic summarization validator, universal memory law, or perfect continuity reconstruction.

**Parent governance:** [`../../projects/mars-website-factory/context-survivability-governance.md`](../../projects/mars-website-factory/context-survivability-governance.md).  
**Compression integrity model:** [`../../projects/mars-website-factory/context-compression-integrity-model.md`](../../projects/mars-website-factory/context-compression-integrity-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/context-drift-taxonomy.md`](../../projects/mars-website-factory/context-drift-taxonomy.md).

---

## 1. When To Run

Run this checklist before freeze, handoff, long-session closure, compressed-context continuation, multi-session continuation, reconstruction from prior reports, or report closure when any of the following affect the section, page, or delivery scope:

- chat or session context was compressed;
- continuation depends on a summary, handoff, prior report, or reconstructed state;
- checkpoint, freeze state, or escalation state may be missing;
- long-chain operational continuity matters;
- strategic, provenance, workflow, QA confidence, visual, or human escalation findings must survive;
- multiple agents/sessions created context fragments;
- current continuation would rely on memory, transcript archaeology, or implicit assumptions.

Record results as **CONTEXT SURVIVABILITY FINDINGS**.

---

## 2. Compression Integrity QA

- [ ] Original operational context or its known artifact sources are named, or **SAFE UNKNOWN** is recorded.
- [ ] Compressed context distinguishes source fact, report conclusion, inference, assumption, and unknown when material.
- [ ] Compression did not silently remove governance findings, source authority, QA evidence, or escalation state.
- [ ] Summary wording does not claim more certainty than the source context supports.
- [ ] Any omitted detail is non-material or explicitly disclosed.
- [ ] Coherent summary language is not treated as proof of completeness.

---

## 3. Checkpoint Persistence QA

- [ ] Last trusted checkpoint, freeze baseline, report, or continuity reference is identified.
- [ ] Scope, phase, evidence, findings, freeze posture, escalation posture, and next action survived compression.
- [ ] Open findings, deferrals, blockers, waivers, and SAFE UNKNOWN items remain visible.
- [ ] Checkpoint state is not inferred from memory or final-summary tone.
- [ ] Missing checkpoint evidence is marked **SAFE UNKNOWN**, checkpoint required, or HITL required.

---

## 4. Freeze-Memory QA

- [ ] Frozen, reopened, deferred, blocked, superseded, or unproven state is named for the active scope.
- [ ] Any unfreeze reason or freeze blocker survived compression.
- [ ] Adjacent or shared-scope edits do not rely on forgotten frozen-state assumptions.
- [ ] Freeze-memory loss is recorded before PASS, freeze, or handoff claims.
- [ ] Current context can explain what changed since the last trusted freeze or checkpoint.

---

## 5. Escalation-Memory QA

- [ ] HITL needs, stop conditions, contradictions, waivers, approvals, and unresolved ambiguity remain visible.
- [ ] Approval is not inferred from silence, fluent summary, or prior continuation.
- [ ] Missing escalation state is routed through human escalation governance.
- [ ] Summary does not flatten "HITL required" into "follow-up" or "known risk" without authority.
- [ ] Escalation memory is preserved in the report as action, not only background context.

---

## 6. Governance-Memory QA

- [ ] Source lineage/provenance findings survived separately from source interpretation findings.
- [ ] QA confidence evidence and proof boundaries survived separately from visual or build confidence.
- [ ] Workflow discipline findings preserved checkpoint, handoff, and execution-order state.
- [ ] Temporal evolution findings preserved version lineage and long-term continuity risk.
- [ ] Strategic intent findings preserved business priority, conversion hierarchy, proof hierarchy, and stakeholder intent when material.
- [ ] Visual reconciliation findings preserved qualitative visual intent rather than collapsing into "looks good."
- [ ] Human escalation findings preserved authority boundary and stop conditions.

---

## 7. Continuity Reconstruction QA

- [ ] Reconstruction is labeled as evidence-based, partial, assumption-based, or blocked.
- [ ] Reconstructed state cites artifacts, reports, checkpoints, or explicit unknowns.
- [ ] Evidence, inference, assumption, and unknown are not blended.
- [ ] Reconstruction does not promote compressed summary to source authority.
- [ ] Continuation action is classified: safe with disclosure, checkpoint required, HITL required, blocked, monitored risk, or STOP.

---

## 8. Context Drift Classification

Classify any issue using [`context-drift-taxonomy.md`](../../projects/mars-website-factory/context-drift-taxonomy.md):

- [ ] Summary hallucination
- [ ] Checkpoint amnesia
- [ ] Hidden assumption persistence
- [ ] Continuity collapse
- [ ] Context erosion
- [ ] Reconstruction ambiguity
- [ ] Governance compression loss
- [ ] Stale-memory continuation
- [ ] Implicit-context contamination
- [ ] Compression-induced drift
- [ ] Freeze-memory loss
- [ ] Historical reconstruction failure
- [ ] Context-lineage fragmentation

---

## 9. Reporting Block

Use this block in Forge reports when context survivability is in scope:

```text
CONTEXT SURVIVABILITY FINDINGS - <section or scope>

Context source: <original / compressed / summary / checkpoint / reconstructed / SAFE UNKNOWN>
Compression integrity: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Checkpoint persistence: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Freeze-state memory: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Escalation memory: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Governance memory: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Continuity reconstruction: evidence-based | partial | assumption-based | blocked | not needed

Context drift taxonomy:
- Patterns:
- Severity:
- Freeze / handoff / continuation impact:

Disposition:
- Action: safe to continue | checkpoint required | deferred | monitored risk | HITL required | STOP
- Evidence / unknowns:
```

Keep this separate from `WORKFLOW DISCIPLINE FINDINGS`, `TEMPORAL EVOLUTION FINDINGS`, `SOURCE LINEAGE FINDINGS`, `QA CONFIDENCE FINDINGS`, and `HUMAN ESCALATION FINDINGS`.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- original operational context is unavailable;
- compression boundary is unknown;
- checkpoint state cannot be reconstructed;
- freeze-state memory is missing;
- escalation state cannot be proven;
- summary may have removed governance findings;
- context fragments conflict or lack lineage;
- continuation depends on implicit assumptions;
- reconstruction requires guessing.

**Action:** state what is unknown, what would resolve it, and whether continuation is safe with disclosure, checkpoint required, HITL required, blocked, or monitored risk.

---

## 11. Non-Goals

- Do not redesign Triumph or any other project.
- Do not invent autonomous memory AI.
- Do not create runtime persistence systems.
- Do not define universal memory laws.
- Do not claim perfect continuity reconstruction.
- Do not treat compressed context as stronger authority than source, checkpoints, or human decisions.

---

*Documentation only - no runtime enforcement.*
