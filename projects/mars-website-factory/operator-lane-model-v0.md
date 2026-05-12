# MARS Website Factory — Operator Lane Model v0

**Status:** **documentation only** — **human role** definitions for Website Factory execution. **Not** RBAC implementation, **not** an access-control system.

**Version:** v0.

**Related:** [first-operational-runbook-v0.md](first-operational-runbook-v0.md), [reference-run-sequence-v0.md](reference-run-sequence-v0.md), [agent-map.md](agent-map.md), [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md), [artifact-governance-rules-v0.md](artifact-governance-rules-v0.md), [hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md).

---

## 1. Purpose

Normalize **who** may do **what** during a reference run: responsibilities, authority, forbidden actions, escalation paths, artifact ownership, freeze authority, and revision authority. Lanes align with **planned** agent cards for vocabulary — **cards are not runtime** ([`../../agents/cards/`](../../agents/cards/)).

---

## 2. Lanes

### 2.1 Strategy operator

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | Positioning, messaging architecture, commercial narrative alignment with **site_type_id**; co-owns CTA story with SEO/conversion. |
| **Authority** | Propose strategy artifacts; request intake clarification; escalate conflicts to HITL. |
| **Forbidden** | Approving own strategy (**no self-approval**); silent rewrite of intake scope; bypassing **G2**. |
| **Escalation** | **NEED HUMAN APPROVAL** / **STRUCTURE CHANGE** per [orchestration-signals-v0.md](orchestration-signals-v0.md). |
| **Artifact ownership** | Strategy memo, messaging tables, commercial risk lists. |
| **Freeze authority** | Cannot unilaterally freeze site-wide semantics; **C02** requires HITL-marketing alignment. |
| **Revision authority** | May initiate revision requests on own drafts before **G2**; post-**G2** revisions require HITL/reopen per [revision-semantics-v0.md](revision-semantics-v0.md). |

---

### 2.2 SEO operator

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | SEO hypotheses, keyword/intent alignment, IA SEO constraints, blueprint SEO fields, blueprint QA input. |
| **Authority** | Flag SEO blockers; refuse silent SEO downgrades. |
| **Forbidden** | Waiving own SEO blockers; approving blueprint batch alone if policy requires PM/tech co-approval. |
| **Escalation** | SEO vs UX conflicts → joint session + HITL if unresolved. |
| **Artifact ownership** | SEO intent artifacts per [seo-intent-model-v0.md](seo-intent-model-v0.md). |
| **Freeze authority** | Contributes evidence to **C02** / **C04**; cannot freeze frontend. |
| **Revision authority** | Same discipline as strategy; coordinated invalidation when IA changes. |

---

### 2.3 UX operator

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | IA, navigation, template model, blueprint structure, journey completeness. |
| **Authority** | Approve IA technical feasibility with tech lead (**G3** partial); reject incoherent blueprint structures. |
| **Forbidden** | Unilateral scope expansion beyond intake; hiding IA deltas from PM. |
| **Escalation** | CTA impossible in IA → loop to strategy/IA with explicit signal. |
| **Artifact ownership** | Sitemap, nav spec, template↔block expectation notes. |
| **Freeze authority** | **C03** co-owner with PM/tech. |
| **Revision authority** | IA revisions after freeze require HITL + invalidation propagation. |

---

### 2.4 Design operator

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | Design handoff pack integrity; visual production; consistency across templates. |
| **Authority** | Accept/reject handoff inputs from blueprint side; define design export format for project. |
| **Forbidden** | Approving own design QA; covert edits to frozen blueprint semantics without REPORT. |
| **Escalation** | Asset/compliance/security issues → stop line + security path. |
| **Artifact ownership** | Design sources/exports per project policy. |
| **Freeze authority** | Drives **C05** recommendation; freeze is **HITL-closed** (**G5**). |
| **Revision authority** | Post-freeze design changes require reopen semantics + downstream invalidation. |

---

### 2.5 Frontend operator

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | Implement static frontend per handoff; maintain `src/` discipline; honest build reporting. |
| **Authority** | Refuse implementation when handoff incomplete or design not frozen. |
| **Forbidden** | Hand-editing `dist/`; claiming CI green without evidence; silent stack changes. |
| **Escalation** | Unsupported requirement → **UNKNOWN** / **STRUCTURE CHANGE** to PM/HITL. |
| **Artifact ownership** | Repo `src/` files, build config (project-local). |
| **Freeze authority** | Proposes **C06** with tech+design evidence. |
| **Revision authority** | Executes revisions after approved reopen; documents in **Frontend implementation REPORT**. |

---

### 2.6 QA operator

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | Execute QA prompts per lane; produce evidence-backed findings; severity discipline. |
| **Authority** | Fail / conditional pass / pass recommendations per [qa-prompt-rules-v0.md](qa-prompt-rules-v0.md). |
| **Forbidden** | **Self-approval** of subject matter they solely produced; **silent overrides** of blockers; auto-waiver ([qa-gating-semantics-v0.md](qa-gating-semantics-v0.md)). |
| **Escalation** | Blocker disagreements → HITL + optional Validator observer input. |
| **Artifact ownership** | QA reports / payloads ([qa-result-payloads-v0.md](qa-result-payloads-v0.md)). |
| **Freeze authority** | QA does **not** “freeze” product artifacts; QA **blocks** advancement until HITL resolves waivers. |
| **Revision authority** | None over production artifacts — **issues lists only**; owners revise. |

---

### 2.7 HITL reviewer

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | Gate decisions **G1–G7**; waiver authority where policy allows; audit readability. |
| **Authority** | Approve / reject / request revision / park per [reference-project-hitl-governance-v0.md](reference-project-hitl-governance-v0.md). |
| **Forbidden** | Delegating approval to an LLM; rubber-stamping without reading evidence; **fake delivery acceptance**. |
| **Escalation** | Policy ambiguity → governance / security forum. |
| **Artifact ownership** | Approval records (format **TBD**), HITL annotations in REPORTs. |
| **Freeze authority** | **Authoritative** for governance freezes (pairs with **C04–C08**). |
| **Revision authority** | May require reopen of frozen baselines with documented invalidation. |

---

### 2.8 Validator observer

| Aspect | Definition |
|--------|------------|
| **Responsibilities** | Cross-cutting consistency checks where Validator role exists in policy; produces **observations**, not silent fixes. |
| **Authority** | Recommend go/no-go inputs to Final Validation; never overrides HITL. |
| **Forbidden** | Autonomous repair, autonomous waiver, or background enforcement (**no validator engine** in v0). |
| **Escalation** | Findings routed through **Validation REPORT** §4.5 and HITL flags. |
| **Artifact ownership** | Validator observation artifacts (project-defined storage). |
| **Freeze authority** | None independent of HITL; may **block recommendation** pending evidence. |
| **Revision authority** | None — issues returned to owning lanes. |

---

## 3. Global prohibitions

| Prohibition | Rationale |
|-------------|-----------|
| **Self-approval** | Same role cannot approve artifacts it solely authored without independent reviewer ([hitl-prompt-boundary-v0.md](hitl-prompt-boundary-v0.md)). |
| **Silent overrides** | All overrides appear in REPORT + HITL trail ([artifact-governance-rules-v0.md](artifact-governance-rules-v0.md)). |
| **Hidden revisions** | Revisions carry lineage, scope, and impact statements ([revision-semantics-v0.md](revision-semantics-v0.md)). |

---

*End of Operator Lane Model v0.*
