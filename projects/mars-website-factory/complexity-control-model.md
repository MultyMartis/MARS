# MARS Website Factory - Complexity Control Model

**Status:** **documented** - Website Factory complexity-control model for human-supervised frontend governance.  
**Not:** automated process optimizer, universal complexity law, governance pruning engine, or replacement for human judgment.

**Parent layer:** [governance-minimalism.md](governance-minimalism.md).  
**Related taxonomy:** [governance-bloat-taxonomy.md](governance-bloat-taxonomy.md).

---

## 1. Purpose

The Complexity Control Model defines how Website Factory decides whether a governance concern should be essential, lightweight, escalation-only, optional, or out of scope for the current work.

It protects:

- proportional governance;
- complexity thresholds;
- governance layering boundaries;
- escalation-only logic;
- lightweight operation;
- readability preservation;
- governance survivability.

The model does not remove existing governance. It prevents every valid governance idea from becoming mandatory depth everywhere.

---

## 2. Layer Model

| Layer | Purpose | Use when |
|-------|---------|----------|
| **Essential governance layer** | Preserve honesty, authority, source lock, scope, and safety boundaries. | Missing it would create false claims, unsafe continuation, or source/approval drift. |
| **Operational-value layer** | Add practical clarity that helps the operator execute, validate, or hand off. | The layer improves next action, evidence, prioritization, or freeze confidence. |
| **Lightweight validation layer** | Check a concern with short, scoped review rather than full ceremony. | Risk is present but low or narrow; a concise finding is enough. |
| **Escalation-only layer** | Stay dormant until ambiguity, contradiction, risk, or authority boundary appears. | Most tasks do not need the layer, but high-risk triggers require it. |
| **Optional-depth layer** | Provide deeper methodology for complex or high-impact cases without forcing all scopes through it. | The task benefits from deeper review, but baseline execution can proceed without it. |
| **Cognitive-load layer** | Review whether the governance path remains understandable and usable. | Findings, checklists, or reports become hard to read, prioritize, or complete. |
| **Governance survivability layer** | Protect governance usability over time, handoffs, compression, fatigue, and future iteration. | The method must remain usable after long sessions, repeated patches, or project transfer. |

---

## 3. Complexity Thresholds

Governance depth should increase only when a threshold is crossed.

| Threshold | Signal | Typical response |
|-----------|--------|------------------|
| **Low risk / clear source** | Scope is local, reversible, source-backed, and easy to verify. | Essential + lightweight validation. |
| **Evidence gap** | PASS, freeze, or handoff confidence would exceed available evidence. | QA confidence + SAFE UNKNOWN; optional deeper checks if needed. |
| **Ambiguity / contradiction** | Source, authority, design, strategy, or implementation interpretation is unclear. | Human escalation or source interpretation; may become stop condition. |
| **Cross-layer dependency** | A finding affects source, visual, responsive, state, accessibility, strategy, workflow, or context. | Invoke only affected layers; keep findings scoped. |
| **Cumulative complexity** | Many layers are active and findings become hard to prioritize. | Governance minimalism review; reduce to essential, escalation-only, and optional-depth. |
| **Long-term survivability risk** | Freeze, lineage, context, recovery, or future handoff is threatened. | Temporal, workflow, context, or recovery review as targeted checks. |

---

## 4. Layering Boundaries

Use this boundary discipline before adding another required governance action:

- **Essential means blocking if absent.** Do not label a layer essential unless missing it would make the claim unsafe.
- **Operational-value means it changes a decision.** If it does not affect next action, confidence, escalation, or handoff, it may be optional.
- **Lightweight validation should stay lightweight.** Short scoped checks should not grow into full reports by default.
- **Escalation-only is a valid design.** A layer can remain dormant until risk appears.
- **Optional depth is not fake governance.** Available depth can be valuable without being mandatory.
- **Cognitive load is a first-class constraint.** A governance stack that operators cannot use is not mature.
- **Readability is part of quality.** The report should reveal priorities, not bury them under total coverage.

---

## 5. Escalation-Only Logic

Prefer escalation-only logic when:

- the risk is rare but high impact;
- the current task has no signal that the risk is active;
- a full checklist would duplicate existing evidence;
- human authority is the real resolver;
- optional depth would preserve quality without slowing simple tasks;
- the concern is better captured as a report finding than a mandatory phase.

Escalation-only does not mean ignored. It means the operator watches for triggers and applies depth only when the trigger appears.

---

## 6. Lightweight Operation

A lightweight governance pass should produce:

- one or two scoped observations;
- a clear PASS / PARTIAL / FAIL / SAFE UNKNOWN boundary;
- an explicit reason if deeper review is not needed;
- a pointer to escalation if the risk becomes active;
- no duplicate checklist ceremony.

Lightweight operation is preferred when it preserves evidence and clarity without increasing methodological weight.

---

## 7. Readability Preservation

Governance readability is preserved when:

- the operator can name the active concern in one sentence;
- findings are grouped by decision impact, not by every possible category;
- full depth is reserved for active risk;
- unresolved unknowns are visible;
- the report distinguishes essential blockers from optional observations;
- future operators can reconstruct why a layer was or was not used.

Readability fails when the method becomes technically complete but operationally obscure.

---

## 8. Complexity-Control Decisions

Use these dispositions:

| Disposition | Meaning |
|-------------|---------|
| **Essential** | Required for safe continuation, freeze, PASS, or handoff. |
| **Lightweight** | Short scoped validation is enough for the current risk. |
| **Escalation-only** | Watch for trigger; apply depth only if ambiguity, contradiction, authority, or risk appears. |
| **Optional-depth** | Available for complex cases; not mandatory for the current scope. |
| **Deferred** | Not needed now, but named for future review if conditions change. |
| **Out of current scope** | Not relevant to the task boundary. |
| **SAFE UNKNOWN** | Complexity need cannot be classified from available evidence. |

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial complexity-control model - essential, operational-value, lightweight validation, escalation-only, optional-depth, cognitive-load, and governance-survivability layers. |
