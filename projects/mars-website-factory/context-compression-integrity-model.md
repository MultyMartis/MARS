# Context Compression Integrity Model - Website Factory

**Status:** **documented** - human-supervised model for preserving operational meaning through context compression.  
**Not:** memory storage architecture, summarization algorithm, autonomous context engine, or guarantee of perfect reconstruction.

**Parent governance:** [context-survivability-governance.md](context-survivability-governance.md).  
**Drift taxonomy:** [context-drift-taxonomy.md](context-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/context-survivability-checklist.md`](../../agents/mars-forge/context-survivability-checklist.md).

---

## 1. Purpose

The Context Compression Integrity Model defines which layers must remain visible when operational context is compressed, summarized, handed off, reconstructed, or resumed.

Compression is acceptable only when it preserves the context needed to answer:

- What state are we continuing from?
- What source, governance, and checkpoint authority still applies?
- What was verified, deferred, escalated, frozen, reopened, or unknown?
- What cannot be safely reconstructed?

This model treats compression as a governance transformation, not as simple token reduction.

---

## 2. Layer Model

| Layer | What it preserves | Integrity risk |
|-------|-------------------|----------------|
| **Original operational context** | Full source reads, edits, findings, decisions, evidence, scope, and uncertainty before compression | Later summaries may omit nuance, contradiction, or checkpoint order |
| **Compressed operational context** | Shortened state that should preserve operational meaning and next-action safety | Coherence can hide lost evidence, flattened findings, or mutated authority |
| **Summary layer** | Human-readable recap of progress, decisions, risks, and next steps | Summary hallucination, fake completeness, or implicit assumption persistence |
| **Checkpoint layer** | Named state anchors: scope, phase, evidence, freeze posture, open findings, and next action | Checkpoint amnesia, vague progress notes, or missing resolver |
| **Freeze-state memory layer** | Frozen, reopened, deferred, blocked, superseded, or unproven states | Freeze-memory loss, silent unfreeze, or stale freeze claims |
| **Escalation memory layer** | HITL needs, stop conditions, contradictions, waivers, unresolved ambiguity, and authority boundaries | Escalation memory loss, fake approval, hidden unresolved decisions |
| **Reconstruction layer** | Later attempt to rebuild state from artifacts, summaries, reports, and available evidence | Continuity reconstruction guessing, historical ambiguity, memory contamination |

---

## 3. Compression Boundaries

Compression may reduce:

- repeated wording;
- low-risk implementation detail already captured in files;
- redundant status prose;
- non-material chat flow;
- resolved local steps when final evidence remains traceable.

Compression must not silently reduce:

- checkpoint identity, scope, phase, evidence, or next action;
- freeze state, unfreeze reason, or supersede relationship;
- source authority, provenance, or transformation boundaries;
- QA confidence evidence and proof boundary;
- human escalation needs, unresolved contradictions, or waiver state;
- strategic intent, conversion hierarchy, proof hierarchy, or stakeholder decision;
- SAFE UNKNOWN items and their resolvers;
- drift classifications and layer-specific findings.

If a compressed record cannot preserve a material boundary, it should say so and classify the context as PARTIAL or SAFE UNKNOWN.

---

## 4. Continuity Preservation

Continuity is preserved when compressed context still states:

- current scope and task boundary;
- last trusted checkpoint or freeze baseline;
- active source/version and stale/forbidden sources;
- completed and incomplete governance checks;
- evidence level for PASS, PARTIAL, FAIL, or SAFE UNKNOWN;
- open risks, deferrals, escalation state, and next safe action;
- what changed since the last trusted state;
- which context was omitted or cannot be reconstructed.

Continuity is not preserved by a generic statement such as "previous work completed," "continue from earlier context," or "summary preserved."

---

## 5. Checkpoint Traceability

A survivable checkpoint should include:

| Checkpoint field | Required preservation |
|------------------|-----------------------|
| **Scope** | Project, page, section, `block_id`, document, or affected layer |
| **State** | Draft, in progress, partial, PASS, FAIL, frozen, reopened, deferred, blocked, or SAFE UNKNOWN |
| **Evidence** | Source reads, rendered checks, build output, QA findings, or explicitly missing evidence |
| **Governance findings** | Layer-specific findings and their disposition |
| **Freeze posture** | Baseline, frozen scope, unfreeze reason, blocker, or unknown |
| **Escalation posture** | Autonomous-safe, disclosure, HITL recommended, HITL required, blocked, waiver, or unknown |
| **Next action** | Safe continuation, checkpoint required, review, rebuild, escalation, or stop |

If these fields are missing, a future operator should not infer them from summary tone.

---

## 6. Reconstruction Handling

Continuity reconstruction should be explicit:

- **Evidence-based reconstruction** - state is rebuilt from named artifacts, reports, checkpoints, and sources.
- **Partial reconstruction** - some layers are known, while others remain unknown or inferred.
- **Assumption-based reconstruction** - continuation depends on plausible but unproven assumptions; must be disclosed.
- **Blocked reconstruction** - missing or contradictory context prevents safe continuation.

Reconstruction output should say:

- what was reconstructed;
- what source or checkpoint supports it;
- what remains ambiguous;
- what cannot be proven;
- what action is safe next.

Reconstruction must not upgrade compressed summaries into full source authority.

---

## 7. Ambiguity Escalation

Escalate ambiguity when compressed or reconstructed context cannot prove:

- which source/version governs;
- whether a section is frozen, reopened, or blocked;
- whether a finding was resolved, deferred, or lost;
- whether HITL approval or waiver exists;
- whether a summary introduced or removed assumptions;
- whether strategic intent survived;
- whether QA confidence still matches evidence;
- whether continuation requires guessing.

Use [human-escalation-governance.md](human-escalation-governance.md) when ambiguity crosses a decision boundary, and [qa-confidence-governance.md](qa-confidence-governance.md) when confidence exceeds available evidence.

---

## 8. Memory Survivability

Memory is survivable when it is:

- **Readable** - a human can understand it without private chat memory.
- **Traceable** - claims point to artifacts, checkpoints, reports, or named unknowns.
- **Layered** - provenance, workflow, QA, escalation, strategic, temporal, and visual findings remain separate.
- **Scoped** - context names what it applies to and what it does not.
- **Honest** - uncertainty survives compression.
- **Actionable** - the next safe action is clear.

Memory is not survivable when it is merely fluent, short, confident, terminology-preserving, or aesthetically coherent.

---

## 9. Integrity Review

Before relying on compressed context, classify:

| Integrity question | PASS means |
|--------------------|------------|
| **Operational meaning** | Current scope, source, state, and next action remain understandable. |
| **Governance continuity** | Layer findings and rules remain visible. |
| **Checkpoint integrity** | Named checkpoints survived with evidence and state. |
| **Freeze-state readability** | Frozen/reopened/deferred/blocked state is clear. |
| **Escalation visibility** | HITL, waiver, contradiction, and stop conditions remain visible. |
| **Strategic continuity** | Business intent and conversion/proof hierarchy were not flattened. |
| **Reconstruction honesty** | Missing context is named rather than invented. |

Any PARTIAL or FAIL should be recorded as `CONTEXT SURVIVABILITY FINDINGS`.

---

## 10. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

- original context is unavailable;
- checkpoint fields cannot be reconstructed;
- compression boundaries are unknown;
- summary may have omitted unresolved risk;
- freeze-state memory is missing;
- escalation memory is missing;
- reconstruction depends on unverified assumptions;
- compressed context is coherent but not traceable.

**Action:** state the missing layer, identify the resolver, and classify whether continuation is safe with disclosure, checkpoint required, HITL required, blocked, or monitored risk.

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Context Compression Integrity Model - layer model, compression boundaries, checkpoint traceability, reconstruction handling, ambiguity escalation, and memory survivability; documentation only. |
