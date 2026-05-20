# MARS Website Factory - Institutional Knowledge Model

**Status:** **documented** - Website Factory model for human-supervised institutional knowledge preservation.  
**Not:** database schema, memory engine, RAG architecture, autonomous knowledge graph, permanent memory system, or universal organizational model.

**Parent governance:** [organizational-memory-governance.md](organizational-memory-governance.md).  
**Drift taxonomy:** [knowledge-memory-drift-taxonomy.md](knowledge-memory-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/organizational-memory-checklist.md`](../../agents/mars-forge/organizational-memory-checklist.md).

---

## 1. Purpose

The Institutional Knowledge Model defines the layers that make organizational memory reusable inside Website Factory governance.

It distinguishes:

- stored documentation from reusable lessons;
- project history from institutional knowledge;
- archive preservation from operational memory;
- prior reports from continuity inheritance;
- tribal memory from durable, traceable learning.

The model is conceptual and documentation-only. It does not prescribe storage technology or claim automated memory.

---

## 2. Layer Overview

| Layer | Preserves | Primary risk if missing |
|-------|-----------|-------------------------|
| **Operational-history layer** | What happened, in what scope, with what evidence and outcome | History becomes anecdotal or reconstructed from memory |
| **Lesson layer** | What was learned, what risk it prevents, and when it applies | Reports accumulate without reusable learning |
| **Freeze-history layer** | What states were frozen, reopened, superseded, or blocked | Future work cannot inherit continuity safely |
| **Governance-history layer** | Which governance findings, rules, and boundaries shaped the work | Governance memory fragments across sessions |
| **Reusable-understanding layer** | Transferable principles, limits, and operational wisdom | Prior learning becomes either buried or overgeneralized |
| **Escalation-history layer** | Human decisions, HITL boundaries, contradictions, waivers, and stop conditions | Future operators mistake unresolved ambiguity for resolved context |
| **Continuity-survivability layer** | What must survive handoff, compression, archive, transfer, and long delay | Knowledge exists but cannot be inherited reliably |

These layers are human-readable review categories, not runtime objects.

---

## 3. Operational-History Layer

The operational-history layer records what materially happened.

It should preserve:

- project or scope identifier;
- source artifacts and active versions;
- relevant reports, findings, and checkpoints;
- decisions made and decisions deferred;
- failures, recoveries, repeated risks, and accepted constraints;
- evidence used for PASS, PARTIAL, FAIL, HITL, or SAFE UNKNOWN.

Operational history becomes institutional knowledge only when it is readable enough to support lessons. Raw history without lesson extraction can still leave future operators in rediscovery loops.

---

## 4. Lesson Layer

The lesson layer converts operational history into reusable understanding.

A lesson should identify:

- what was learned;
- what mistake, drift, or risk it prevents;
- what evidence created it;
- what context makes it valid;
- what context makes it unsafe or partial;
- what governance layer should use it;
- how future operators should apply, adapt, reject, or escalate it.

**Rule:** a lesson is not reusable because it is old. It is reusable because its source, scope, limitation, and operational value remain readable.

---

## 5. Freeze-History Layer

The freeze-history layer preserves how approved states evolved over time.

It should record:

- frozen baseline;
- reopen or unfreeze reason;
- supersede path;
- rollback or recovery relationship;
- affected governance findings;
- continuity inheritance notes;
- unresolved risks that survived freeze.

Freeze history helps future operators avoid treating current files as self-explanatory authority. A file can be current while its historical meaning, approval path, or superseded context is unclear.

---

## 6. Governance-History Layer

The governance-history layer preserves the evolution of governance findings and operational rules.

It should answer:

- which governance layers were applied;
- what findings appeared repeatedly;
- what findings were resolved, deferred, waived, or escalated;
- what new rule or checklist item emerged from repeated operational friction;
- whether a rule is Website Factory methodology, project-specific lesson, or temporary workaround;
- whether the governance memory remains readable across later reports.

Governance history prevents isolated findings from becoming forgotten fragments.

---

## 7. Reusable-Understanding Layer

The reusable-understanding layer contains institutional principles that can travel beyond one project after compatibility review.

Examples:

- source ambiguity should be escalated before implementation confidence;
- visual reconciliation must preserve perceived hierarchy, not only DOM correctness;
- freeze states require traceability to remain useful;
- compressed context is not complete authority;
- cross-project transfer requires compatibility, not analogy;
- documentation storage does not equal organizational memory.

Reusable understanding should carry boundaries. A strong lesson without limits can become template overreach.

---

## 8. Escalation-History Layer

The escalation-history layer preserves human authority boundaries.

It should record:

- HITL-required decisions;
- unresolved contradictions;
- waivers and their scope;
- stop conditions;
- approval or rejection rationale;
- assumptions that were not approved;
- decisions that should not be silently inherited.

Escalation history prevents future operators from treating silence, continuation, or archive presence as approval.

---

## 9. Continuity-Survivability Layer

The continuity-survivability layer governs whether institutional knowledge can survive handoff, compression, archive, team change, and later reuse.

It should preserve:

- lesson source;
- lesson scope;
- historical traceability;
- reuse boundary;
- governance relationship;
- escalation and unknowns;
- continuity inheritance path;
- project-specific limits.

Continuity survivability is the bridge between "we learned something" and "future operators can safely inherit it."

---

## 10. Lesson Preservation

Preserve a lesson when it:

- prevents repeated mistakes;
- explains a governance rule;
- captures operational wisdom not obvious from final files;
- clarifies a historical decision;
- identifies a recurring drift pattern;
- improves future freeze, handoff, transfer, recovery, or QA quality;
- makes an old report useful without requiring full transcript archaeology.

Lesson preservation should be concise. The goal is institutional readability, not exhaustive archive duplication.

---

## 11. Rediscovery Prevention

Rediscovery prevention requires:

- naming repeated mistakes;
- preserving why the mistake happened;
- identifying the governance layer that prevents recurrence;
- defining the trigger for future operators;
- keeping the lesson findable from operational indexes or Forge checklists;
- stating when the lesson is not applicable.

Rediscovery is not prevented by storing the old report. It is prevented when the future operator can see the lesson before repeating the work.

---

## 12. Operational Lineage

Operational lineage traces:

```text
operational event / drift / failure / decision
-> evidence and report
-> lesson extraction
-> governance placement
-> reuse boundary
-> continuity inheritance
```

Lineage is weak when any step is missing, inferred, or dependent on private memory.

---

## 13. Continuity Inheritance

Continuity inheritance defines how future work may inherit institutional knowledge.

| Inheritance state | Meaning |
|-------------------|---------|
| **Reusable** | Lesson is traceable, scoped, and applicable after compatibility review. |
| **Project-specific** | Lesson is valuable but should remain local unless promoted or adapted. |
| **Partial** | Lesson is useful but missing evidence, scope, or limitation. |
| **Escalation-bound** | Lesson requires HITL or explicit authority before reuse. |
| **Deprecated** | Lesson no longer governs, but historical reason remains useful. |
| **SAFE UNKNOWN** | Lesson source, scope, authority, or lineage cannot be established. |

Inheritance is never automatic just because a lesson is old, repeated, or stored.

---

## 14. Historical Traceability

Historical traceability should answer:

- Where did this lesson come from?
- What project, version, freeze, failure, or report created it?
- What decision or evidence made it credible?
- What governance layer owns or references it?
- What later work reused, adapted, rejected, or superseded it?
- What remains unknown?

If those questions cannot be answered, the knowledge may be archived but not institutionally survivable.

---

## 15. Institutional Survivability

Institutional survivability requires:

- readable lessons;
- visible lineage;
- explicit reuse boundaries;
- project-specific limits;
- governance placement;
- escalation memory;
- SAFE UNKNOWN discipline;
- protection from overgeneralization.

An institution survives through knowledge only when future operators can understand what was learned without mythologizing the past.

---

## 16. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Institutional Knowledge Model - operational-history, lesson, freeze-history, governance-history, reusable-understanding, escalation-history, and continuity-survivability layers; documentation only. |
