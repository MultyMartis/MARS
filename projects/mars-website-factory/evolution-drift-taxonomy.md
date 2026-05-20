# MARS Website Factory - Evolution Drift Taxonomy

**Status:** **documented** - named long-term evolution drift vocabulary for human-supervised frontend governance.  
**Not:** automated drift detector, runtime maintenance engine, universal lifecycle rulebook, or autonomous refactor tool.

**Parent layer:** [temporal-evolution-governance.md](temporal-evolution-governance.md).  
**Survivability model:** [project-drift-survivability-model.md](project-drift-survivability-model.md).  
**Forge checklist:** [`../../agents/mars-forge/temporal-evolution-checklist.md`](../../agents/mars-forge/temporal-evolution-checklist.md).

---

## 1. Purpose

This taxonomy names long-term evolution drift patterns that can degrade a frontend project while each local change still appears justified, QA-passed, and visually acceptable.

Use it in **TEMPORAL EVOLUTION FINDINGS** to avoid vague labels such as "old project got messy," "too many fixes," "probably fine," or "needs cleanup."

---

## 2. Drift Patterns

| Drift pattern | Definition | Typical symptom | Governance response |
|---------------|------------|-----------------|---------------------|
| **Gradual design erosion** | Approved visual identity weakens through many small, acceptable-looking changes. | Current UI looks polished but no longer reads like the frozen design direction. | Run continuity checkpoint; compare against freeze/source identity. |
| **Freeze-state divergence** | Current state differs from frozen baseline without visible reopen, supersede, or divergence rationale. | Frozen section was changed through local edits or shared styles. | Identify baseline; record freeze break or SAFE UNKNOWN. |
| **Cumulative override decay** | Repeated exceptions become the hidden operating model. | Normal token/component/path is bypassed by many local rules. | Review override stack; normalize, bound, or escalate. |
| **Patch-history contamination** | Old fixes, emergency notes, or prior session assumptions drive current behavior as if canonical. | Operators preserve a hack because it "has always been there." | Trace source of patch; classify temporary, accepted, stale, or drift. |
| **Architectural fragmentation** | Structure splits into incompatible local patterns across sections, breakpoints, or components. | Similar sections require different mental models and fixes. | Identify canonical owner or continuity checkpoint. |
| **Governance fatigue** | Operators stop applying governance because exceptions, urgency, or checklist volume feel normal. | Findings disappear, PASS language becomes vague, unknowns are not surfaced. | Re-establish required gates and escalate skipped boundaries. |
| **Iterative inconsistency** | Repeated scoped changes create inconsistent behavior, rhythm, states, or source interpretation. | No single edit is wrong, but siblings no longer match as a system. | Review cumulative changes by concern, not only latest diff. |
| **Modernization drift** | New style, code, tooling, dependency, or design conventions replace older identity without continuity. | "Modernized" area feels like another product or architecture. | Require lineage, authority, and identity-preservation review. |
| **Silent identity mutation** | Project identity changes without an explicit decision. | Business tone, visual language, component philosophy, or architecture shifts unnoticed. | HITL / checkpoint; decide preserve, supersede, or branch. |
| **Continuity collapse** | Future operators cannot explain current state from artifacts. | Understanding requires memory, archaeology, or reading many unrelated patches. | Reconstruct continuity record or mark SAFE UNKNOWN. |
| **Version-lineage loss** | Relationship between V1/V2/current/frozen/superseded artifacts is unclear. | Old and new sources mix or current state has no traceable parent. | Restore version chain; quarantine stale sources. |
| **Historical ambiguity** | It is unclear whether a behavior came from source, patch, bug, decision, or drift. | Reports say "existing behavior" without authority. | Record unknown origin and resolver. |
| **Uncontrolled evolution** | The project keeps changing without checkpoints, scope boundaries, or authority review. | Delivery is always "almost done" but never stable as a governed state. | Stop or checkpoint; define next baseline. |

---

## 3. Related Drift Families

### 3.1 Freeze and Lineage Drift

Includes:

- freeze-state divergence;
- version-lineage loss;
- historical ambiguity;
- continuity collapse;
- stale baseline reuse.

Primary risk: the project loses the ability to prove what state it is preserving, superseding, or diverging from.

### 3.2 Override and Patch Drift

Includes:

- cumulative override decay;
- patch-history contamination;
- endless patch evolution;
- override stacking over years;
- small-change accumulation blindness.

Primary risk: local fixes become a hidden architecture, and future operators treat entropy as source truth.

### 3.3 Identity and Modernization Drift

Includes:

- gradual design erosion;
- modernization drift;
- silent identity mutation;
- local improvement identity damage;
- strategic or visual identity dilution.

Primary risk: the project still works but no longer expresses the approved Website Factory, project, design, or business identity.

### 3.4 Governance and Continuity Drift

Includes:

- governance fatigue;
- uncontrolled evolution;
- iterative inconsistency;
- architectural fragmentation;
- checkpoint abandonment.

Primary risk: governance no longer survives time, so current correctness replaces long-term continuity.

---

## 4. Severity Guidance

| Severity | Meaning |
|----------|---------|
| **P0 - stop / HITL** | Drift changes identity, breaks freeze integrity, loses version lineage, or makes approved baseline unknowable. |
| **P1 - freeze blocker** | Drift materially affects continuity, architectural readability, cumulative override risk, or governance survivability for the scope. |
| **P2 - partial allowed** | Drift is known and bounded; freeze may proceed only with explicit `TEMPORAL EVOLUTION FINDINGS` and follow-up. |
| **P3 - monitored risk** | Minor accumulation or readability risk; record if it may affect future evolution. |

Severity is based on long-term survivability, not visual severity. A tiny local patch can be P1 if it hides a freeze break or lineage loss.

---

## 5. Anti-Pattern Phrases

Use these as named drift, not casual criticism:

- **endless patch evolution**
- **modernization without continuity**
- **silent redesign accumulation**
- **historical lineage loss**
- **override stacking over years**
- **uncontrolled local evolution**
- **governance abandonment**
- **iterative fragmentation**
- **small change accumulation blindness**
- **freeze-state erosion**

If one of these phrases appears in a review, include the affected scope, evidence, severity, and recommended resolver.

---

## 6. Taxonomy Use in REPORT

When temporal evolution is in scope, report:

- drift pattern name;
- affected freeze state, version, section, component, token, breakpoint, or governance layer;
- lineage or continuity risk;
- cumulative impact if known;
- severity;
- whether the result is preserved, superseded, deferred, monitored, escalated, or blocked;
- SAFE UNKNOWN if baseline, authority, or history cannot be established.

Example:

```text
Evolution drift taxonomy:
- Pattern: Freeze-state divergence
- Scope: <block_id / version / frozen baseline>
- Severity: P1
- Risk: current state differs from frozen baseline through shared override with no unfreeze reason
- Disposition: PARTIAL - temporal evolution; continuity checkpoint required
```

---

## 7. Boundaries

This taxonomy does not require one maintenance strategy, design system, framework, or release process. It names long-term survivability risk regardless of stack.

It does not authorize autonomous modernization, redesign, cleanup, or refactor. A finding may recommend a continuity checkpoint, scoped normalization, monitored risk, SAFE UNKNOWN, or HITL escalation, but identity-changing work remains governed by project source authority and Website Factory workflow.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Evolution Drift Taxonomy - gradual design erosion, freeze-state divergence, cumulative override decay, patch-history contamination, architectural fragmentation, governance fatigue, iterative inconsistency, modernization drift, silent identity mutation, continuity collapse, version-lineage loss, historical ambiguity, and uncontrolled evolution. |
