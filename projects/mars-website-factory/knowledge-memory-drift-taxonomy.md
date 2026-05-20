# MARS Website Factory - Knowledge Memory Drift Taxonomy

**Status:** **documented** - Website Factory drift vocabulary for organizational memory and institutional knowledge.  
**Not:** automated detection taxonomy, universal organizational law, runtime monitoring, permanent memory system, or autonomous institutional AI.

**Parent governance:** [organizational-memory-governance.md](organizational-memory-governance.md).  
**Institutional model:** [institutional-knowledge-model.md](institutional-knowledge-model.md).  
**Forge checklist:** [`../../agents/mars-forge/organizational-memory-checklist.md`](../../agents/mars-forge/organizational-memory-checklist.md).

---

## 1. Purpose

This taxonomy names drift patterns where an organization appears to preserve documentation but loses reusable knowledge, operational lessons, institutional continuity, and historical traceability.

Use it for:

- `ORGANIZATIONAL MEMORY FINDINGS`;
- lesson-survivability QA;
- continuity-inheritance QA;
- rediscovery-risk QA;
- historical-traceability QA;
- institutional-readability QA;
- governance-memory continuity review.

This is a human review vocabulary, not an automated classifier.

---

## 2. Drift Patterns

| Drift pattern | Meaning | Typical symptom | Governance response |
|---------------|---------|-----------------|---------------------|
| **Institutional memory loss** | Important operational knowledge no longer survives into current work | Team repeats known mistakes despite old docs existing | Extract reusable lesson, restore lineage, record `ORGANIZATIONAL MEMORY FINDINGS` |
| **Rediscovery loop** | Operators repeatedly investigate or solve the same issue | Same source ambiguity, responsive issue, or freeze mistake reappears | Name lesson, define trigger, add continuity inheritance note |
| **Lesson fragmentation** | Related lessons are split across reports, chats, archives, and projects | No single readable path from issue to lesson | Consolidate as scoped lesson with source links |
| **Tribal knowledge collapse** | Critical knowledge lives only in people or remembered conversations | Work blocks or drifts when a person/session is unavailable | Convert to traceable artifact or mark SAFE UNKNOWN |
| **Undocumented operational wisdom** | Practical know-how exists but is not recorded as reusable learning | Operators know "what usually breaks" but future agents do not | Preserve operational wisdom with scope and limits |
| **Historical amnesia** | Current work forgets prior decisions, failures, freezes, or rejected paths | Old rejected assumptions return as new ideas | Restore historical traceability and decision authority |
| **Continuity inheritance failure** | Future work cannot inherit prior lessons safely | Lesson is known but source, scope, and applicability are unclear | Classify inheritance state: reusable, project-specific, partial, escalation-bound, deprecated, or SAFE UNKNOWN |
| **Governance-memory erosion** | Governance findings lose comparability across sessions | Same category changes names or disappears from reports | Re-anchor to governance layer and reporting block |
| **Reusable-lesson decay** | A lesson becomes too vague, stale, buried, or overgeneralized to use | "We learned this before" has no action or boundary | Refresh lesson source, limits, and application trigger |
| **Pattern-history loss** | The history of a recurring pattern disappears | A drift pattern is treated as isolated each time | Link pattern to prior occurrences and governance response |
| **Operational-lineage fragmentation** | The path from event to lesson to reuse breaks | Cannot trace why a rule exists or what event created it | Rebuild operational lineage or mark SAFE UNKNOWN |
| **Institutional drift** | Organizational practice diverges from its own lessons | Reports claim governance maturity while execution repeats old failure modes | Review lesson survivability and governance-memory continuity |
| **Historical-context collapse** | Archives remain, but context needed to interpret them is gone | Old docs exist but no one knows what still governs | Classify active, stale, superseded, deprecated, or unknown history |

---

## 3. Institutional Memory Loss

**Definition:** loss of operational lessons, decision history, or governance memory despite the presence of documents or archives.

Signals:

- repeated mistakes in the same governance category;
- reports cannot explain why a rule exists;
- old project lessons are invisible during new work;
- final files survive but operational rationale does not;
- future operators rely on memory, not artifacts.

Response:

- identify the missing lesson;
- trace the source event or decision;
- record reuse boundary;
- decide whether lesson is reusable, project-specific, partial, deprecated, or SAFE UNKNOWN.

---

## 4. Rediscovery Loop

**Definition:** the organization repeatedly spends effort rediscovering risks, constraints, decisions, or lessons that were already encountered.

Signals:

- same ambiguity gets escalated repeatedly without a reusable lesson;
- repeated debates about already-settled freeze, source, or visual authority;
- recurring "new" findings that match previous reports;
- operators search archives instead of inheriting a clear lesson.

Response:

- name the loop;
- preserve the lesson trigger;
- link to the governing layer;
- make the future action explicit.

---

## 5. Lesson Fragmentation

**Definition:** lesson evidence and meaning are distributed across disconnected documents until the organization cannot reuse the lesson safely.

Signals:

- lesson source appears in one report, limitation in another, and action in a third;
- summaries mention a lesson without evidence;
- archives contain all pieces but no operational reading path;
- future operators reconstruct by guesswork.

Response:

- consolidate the lesson in a human-readable entry or governance reference;
- preserve source, scope, limitation, and reuse boundary;
- mark unresolved gaps as SAFE UNKNOWN.

---

## 6. Tribal Knowledge Collapse

**Definition:** institutional knowledge depends on people, chat memory, or unstated habits instead of durable, readable artifacts.

Signals:

- "everyone knows" becomes the reason;
- work pauses because one operator remembers the context;
- governance rules are applied inconsistently because history is private;
- decisions are inherited without written authority.

Response:

- document the knowledge as operational lesson or decision history;
- identify owner or source if possible;
- refuse to promote private memory into authority without evidence.

---

## 7. Historical Amnesia

**Definition:** prior decisions, rejected paths, failures, freezes, or lessons are forgotten and later reintroduced as if new.

Signals:

- old V1/archive assumptions re-enter active work;
- rejected visual or semantic approaches return without decision review;
- previous failure modes appear again under new wording;
- freeze state is treated as current output rather than historical authority.

Response:

- restore historical traceability;
- identify active vs stale vs superseded history;
- record whether the prior lesson still applies.

---

## 8. Governance-Memory Erosion

**Definition:** governance findings lose continuity over time, making it hard to compare, inherit, or improve them.

Signals:

- finding categories change names without mapping;
- reports omit previously material governance findings;
- layer relationships disappear from handoffs;
- lessons remain local to one checklist and never become organizational learning.

Response:

- re-anchor findings to canonical governance layers;
- preserve comparable reporting language;
- avoid flattening distinct findings into generic "risk" or "done."

---

## 9. Reusable-Lesson Decay

**Definition:** a lesson exists but becomes stale, vague, buried, or overgeneralized.

Signals:

- lesson cannot answer "when does this apply?";
- lesson is cited as universal law despite local origin;
- lesson exists only inside a long report;
- future work uses the lesson without its limitation.

Response:

- refresh scope, evidence, limits, and applicability;
- keep cross-project transfer boundaries visible;
- deprecate or mark SAFE UNKNOWN when authority cannot be restored.

---

## 10. Operational-Lineage Fragmentation

**Definition:** the chain from operational event to lesson to future reuse is broken.

Signals:

- rule exists but originating problem is unknown;
- lesson is reused without evidence or source event;
- report finding cannot be tied to later governance;
- future operators cannot explain why the lesson matters.

Response:

- rebuild lineage from available artifacts;
- disclose any reconstruction assumptions;
- classify continuation as reusable, partial, HITL required, or SAFE UNKNOWN.

---

## 11. Forbidden Drift Summary

Forbidden drift includes:

- documentation without reusable lessons;
- endless rediscovery;
- tribal-knowledge dependence;
- historical amnesia;
- disconnected archives;
- institutional-memory erosion;
- lesson burial;
- governance-history fragmentation;
- continuity reset thinking;
- "start from scratch" operational culture;
- old reports treated as memory without lesson extraction;
- archive completeness treated as institutional continuity.

---

## 12. SAFE UNKNOWN

Use **SAFE UNKNOWN** when:

- the lesson source cannot be named;
- historical authority cannot be established;
- operational lineage is missing;
- reuse boundary is unclear;
- archive status is known but meaning is not;
- tribal memory is the only evidence;
- current work depends on a lesson no one can trace;
- prior reports mention a lesson but omit evidence or scope.

**Action:** state what memory is missing, what would restore traceability, and whether current work should continue with disclosure, stop, request HITL, or preserve a partial lesson.

---

## 13. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Knowledge Memory Drift Taxonomy - institutional memory loss, rediscovery loops, lesson fragmentation, tribal knowledge collapse, historical amnesia, continuity inheritance failure, governance-memory erosion, reusable-lesson decay, pattern-history loss, operational-lineage fragmentation, institutional drift, and historical-context collapse. |
