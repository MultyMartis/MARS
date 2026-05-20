# MARS Website Factory - Governance Bloat Taxonomy

**Status:** **documented** - drift vocabulary for governance bloat and process overload in Website Factory.  
**Not:** automated detector, process scoring engine, universal governance critique, or instruction to remove existing governance.

**Parent layer:** [governance-minimalism.md](governance-minimalism.md).  
**Control model:** [complexity-control-model.md](complexity-control-model.md).

---

## 1. Purpose

This taxonomy names drift patterns where governance becomes heavier than its operational value.

The goal is not anti-governance. The goal is to prevent governance from becoming so dense that operators stop understanding, applying, or trusting it.

---

## 2. Drift Patterns

| Drift pattern | Symptom | Risk |
|---------------|---------|------|
| **Governance inflation** | New rules, checklists, and report sections are added after every observed issue. | Coverage grows faster than usability. |
| **Process paralysis** | Operators hesitate to act because the governance path is too large or unclear. | Execution slows or stops despite solvable work. |
| **Ritualized QA** | Checks are completed as ceremony without evidence, judgment, or decision impact. | PASS language becomes performative. |
| **Checklist fatigue** | The number of checklist items exceeds operator attention and practical priority. | Important checks are skimmed or missed. |
| **Documentation sprawl** | Docs multiply until canonical entry points and source-of-truth boundaries blur. | Operators cannot find the right rule quickly. |
| **Methodological obesity** | The method contains excessive categories, phases, and findings for routine work. | Governance becomes harder than execution. |
| **Governance-over-execution** | Process compliance consumes more energy than producing, validating, and improving the artifact. | The system rewards ceremony over outcome. |
| **Cognitive overload** | Operators cannot hold the governance path, active risk, and next action in working memory. | Mistakes increase despite more process. |
| **Excessive layering** | Every valid concern becomes another mandatory layer. | Priorities flatten and reports become unreadable. |
| **Performative governance** | The system appears mature because it has many controls, not because controls create value. | Sophistication hides usability failure. |
| **Operational slowdown** | Iteration becomes slow without a matching increase in safety, clarity, or quality. | Teams bypass governance or avoid changes. |
| **Survivability erosion** | Governance records become too long or dense to survive handoff, compression, or future review. | Continuity fails under its own documentation weight. |
| **Governance collapse through weight** | The whole governance system becomes impractical, ignored, or selectively applied without clarity. | Discipline fails because it is too heavy to operate. |

---

## 3. Early Warning Signals

- The report contains many findings but no clear next action.
- Operators cannot explain which checks were essential and which were optional.
- Every task triggers nearly every governance layer.
- PASS/PARTIAL/SAFE UNKNOWN language becomes repetitive rather than evidential.
- Checklists duplicate each other under different labels.
- Governance notes are longer than the artifact change they support.
- Escalation-only risks are treated as mandatory ceremony.
- Future operators need private context to understand why a layer was invoked.
- "More complete" documentation makes the operational entry path less clear.

---

## 4. Severity

| Severity | Meaning | Response |
|----------|---------|----------|
| **Low** | Minor duplication or extra checklist weight, still readable. | Keep lightweight; note optional-depth boundary. |
| **Medium** | Governance slows work or obscures priority for a scoped task. | Run governance minimalism review; classify essential vs optional. |
| **High** | Operators cannot tell what is required, what passed, or what matters. | Stop and simplify current governance path; escalate if freeze/report claims depend on it. |
| **Blocking** | Governance weight prevents safe execution, handoff, or credible reporting. | Treat as `GOVERNANCE MINIMALISM FINDINGS`; no freeze/readiness claim until path is readable. |

---

## 5. Forbidden Reframes

Do not normalize governance bloat as:

- "maturity" when it reduces usability;
- "thoroughness" when it hides priorities;
- "safety" when it creates checklist fatigue;
- "quality" when it produces no evidence;
- "discipline" when it blocks proportionate execution;
- "documentation completeness" when it weakens source-of-truth readability.

---

## 6. Relationship to Other Drift Taxonomies

Governance bloat can amplify other drift:

- QA drift becomes **ritualized QA** when evidence is replaced by checklist completion.
- Workflow drift becomes **process paralysis** when execution order is buried under ceremony.
- Context drift becomes **survivability erosion** when compressed context cannot carry bloated findings.
- Temporal drift becomes **governance fatigue** when the system is too heavy to survive long projects.
- Human escalation drift becomes **methodology absolutism** when every uncertainty is treated as universal mandatory depth instead of a proportionate stop or HITL path.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial governance bloat taxonomy - governance inflation, process paralysis, ritualized QA, checklist fatigue, documentation sprawl, methodological obesity, governance-over-execution, cognitive overload, excessive layering, performative governance, operational slowdown, survivability erosion, and collapse through weight. |
