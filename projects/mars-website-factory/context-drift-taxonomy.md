# Context Drift Taxonomy - Website Factory

**Status:** **documented** - drift vocabulary for context survivability and compression integrity reviews.  
**Not:** automated detector, runtime memory validator, universal memory framework, or proof of autonomous continuity.

**Parent governance:** [context-survivability-governance.md](context-survivability-governance.md).  
**Integrity model:** [context-compression-integrity-model.md](context-compression-integrity-model.md).  
**Forge checklist:** [`../../agents/mars-forge/context-survivability-checklist.md`](../../agents/mars-forge/context-survivability-checklist.md).

---

## 1. Purpose

This taxonomy names context drift patterns that can appear when Website Factory frontend work continues through summaries, compressed context, long sessions, handoffs, checkpoint reconstruction, or partial memory.

The critical risk: compressed context can look coherent, preserve terminology, and appear complete while still losing checkpoints, hiding ambiguity, mutating governance meaning, or eroding strategic continuity.

---

## 2. Taxonomy

| Drift pattern | Definition | Typical symptom | Governance response |
|---------------|------------|-----------------|---------------------|
| **Summary hallucination** | A summary introduces facts, completions, approvals, findings, or decisions not supported by artifacts. | Report says something was resolved but no checkpoint or evidence supports it. | Mark SAFE UNKNOWN; reconstruct from artifacts or escalate. |
| **Checkpoint amnesia** | Named state anchors disappear or become vague progress statements. | "Work continued from previous state" without phase, evidence, freeze, or next action. | Require checkpoint reconstruction or block freeze claims. |
| **Hidden assumption persistence** | Prior unstated assumptions survive as if they were approved context. | Later work treats a guess as project truth. | Surface assumption chain; classify via escalation governance. |
| **Continuity collapse** | Current state can no longer be connected to source, checkpoint, freeze, or report history. | Operator cannot explain what changed since the last trusted state. | Pause for continuity checkpoint or HITL. |
| **Context erosion** | Each summary loses small details until operational meaning becomes fragile. | Findings become too generic to guide next work. | Restore layer-specific findings and source links. |
| **Reconstruction ambiguity** | Later reconstruction cannot distinguish evidence, inference, assumption, and unknown. | "Likely from earlier work" becomes basis for continuation. | Label reconstruction mode and unknowns. |
| **Governance compression loss** | Governance findings are flattened into a generic "QA passed" or "done." | Layer-specific risks vanish from report. | Re-expand findings by layer before continuation. |
| **Stale-memory continuation** | Old summaries, archived notes, prior versions, or superseded decisions drive active work. | V1/archive assumptions influence V2 work without disclosure. | Re-check active source/version and provenance. |
| **Implicit-context contamination** | Unrelated session memory or adjacent work pollutes the current scope. | Decisions appear from nowhere or from other sections/projects. | Quarantine unexplained context; require source authority. |
| **Compression-induced drift** | Meaning, priority, scope, authority, or uncertainty changes during compression. | Compressed text says the same terms but changes their operational role. | Compare against original context or record SAFE UNKNOWN. |
| **Freeze-memory loss** | Frozen, reopened, deferred, blocked, or superseded state is lost. | A section is treated as safe to edit or freeze without baseline. | Require freeze-state reconstruction or escalation. |
| **Historical reconstruction failure** | Past state cannot be reconstructed from available artifacts without guessing. | The current operator depends on private memory or transcript archaeology. | Declare reconstruction failure; identify resolver. |
| **Context-lineage fragmentation** | Multiple context fragments exist without clear relationship or authority order. | Several summaries conflict or partially overlap. | Establish context lineage and active authority. |

---

## 3. Severity Guide

| Severity | Meaning | Action |
|----------|---------|--------|
| **Low** | Drift affects wording but not state, authority, or next action. | Correct summary wording and continue with disclosure. |
| **Medium** | Drift affects a finding, checkpoint detail, source boundary, or QA confidence. | Record `CONTEXT SURVIVABILITY FINDINGS`; reconstruct or defer. |
| **High** | Drift affects freeze state, escalation state, strategic intent, source authority, or validation confidence. | Checkpoint required or HITL required before freeze/PASS. |
| **Blocking** | Continuation would require guessing about authority, approval, frozen state, or unresolved contradiction. | STOP or blocked-by-ambiguity until resolved. |

---

## 4. Drift Clusters

### 4.1 Summary Drift

- Summary hallucination
- Fake context completeness
- Compressed report overconfidence
- Governance compression loss
- Summary-as-source promotion

### 4.2 Checkpoint Drift

- Checkpoint amnesia
- Freeze-memory loss
- Continuity checkpoint omission
- Historical reconstruction failure
- Context-lineage fragmentation

### 4.3 Assumption Drift

- Hidden assumption persistence
- Implicit-context contamination
- Memory contamination
- Stale-memory continuation
- Assumption inheritance without authority

### 4.4 Reconstruction Drift

- Reconstruction ambiguity
- Continuity reconstruction guessing
- Evidence/inference/assumption blending
- Context erosion
- Continuity collapse

---

## 5. Anti-Patterns

Forbidden continuation patterns:

| Anti-pattern | Why it is drift |
|--------------|-----------------|
| **Blind continuation from summaries** | No proof that the summary preserved operational state. |
| **Compression without checkpoints** | Removes the anchors needed for safe resumption. |
| **Hidden assumption inheritance** | Makes guesses persistent and hard to detect. |
| **Governance erosion through summarization** | Turns layer-specific checks into vague confidence. |
| **Continuity reconstruction guessing** | Invents history to avoid stopping. |
| **Fake context completeness** | Coherent writing hides missing proof. |
| **Freeze-state forgetting** | Weakens change control and regression trust. |
| **Escalation memory loss** | Hides human-owned decisions and stop conditions. |
| **Context laundering** | Repetition or compression makes weak context seem canonical. |
| **Historical ambiguity accumulation** | Many small unknowns become unusable history. |

---

## 6. Reporting Vocabulary

Use these labels in `CONTEXT SURVIVABILITY FINDINGS`:

- **PASS** - context is traceable enough for the named scope.
- **PARTIAL** - some layers survived, but gaps require disclosure or checkpoint follow-up.
- **FAIL** - context cannot support the requested continuation, PASS, freeze, or handoff.
- **SAFE UNKNOWN** - context may be usable only with disclosed uncertainty and bounded continuation.
- **CHECKPOINT REQUIRED** - context must be re-anchored before safe continuation.
- **HITL REQUIRED** - missing or contradictory context crosses a human decision boundary.
- **STOP** - continuation would require inventing state, approval, freeze posture, or source authority.

---

## 7. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- drift pattern is suspected but cannot be proven from available artifacts;
- original context is missing and summaries conflict;
- checkpoint, freeze, escalation, or source authority cannot be reconstructed;
- prior memory may be stale or contaminated;
- compressed context appears complete but lacks traceability;
- historical state would need guessing.

**Action:** name the drift pattern if possible, identify what evidence would resolve it, and classify continuation as safe with disclosure, checkpoint required, HITL required, blocked, or monitored risk.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Context Drift Taxonomy - summary hallucination, checkpoint amnesia, hidden assumption persistence, continuity collapse, context erosion, governance compression loss, stale-memory continuation, freeze-memory loss, historical reconstruction failure, and related anti-patterns; documentation only. |
