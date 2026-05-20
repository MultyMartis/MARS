# MARS — Documentation fatigue review (Phase 3)

**Status:** **documented** — analysis only. **Not** a pruning execution pass.  
**Date:** 2026-05-19.  
**Question:** Where did docs stop improving operational value?

---

## 1. Executive summary

Documentation fatigue is **uneven**: Factory governance expansion shows the strongest **prestige and triplication** signals; governance meta-layers show **catalog fatigue**; ORCA remains **relatively disciplined**. Compression should favor **navigation tiers, banners, and merge-on-edit** — not bulk deletion.

---

## 2. Prestige-documentation risks

| Signal | Where | Why it hurts | Compression opportunity |
|--------|-------|--------------|-------------------------|
| **Philosophy stacks without task hook** | Factory meta-governance, governance-evolution, trust-calibration, reasoning-visibility | Read for gravitas, not for next action | Mark **reference-only** in OPERATIONAL-INDEX; open only on escalation |
| **Long normative preambles** | Many `*-governance.md` files | Re-states honesty already in AGENTS | First screen = **operator actions** + links; move philosophy to § appendix on next edit |
| **“Architecture model” pairs** | `governance-architecture-model`, `self-refinement-model` | Sounds like shipped design system | Banner: **documentation-only model** |
| **Coherence / compression reviews** | governance `*-review-v0.md` cluster | Valuable once; reread as if law | Treat as **stabilization input** with date; link from operational-survivability, don’t duplicate findings in new docs |

---

## 3. Governance-for-governance signals

| Pattern | Example surfaces | Operational value cliff |
|---------|------------------|---------------------------|
| Meta-governance governing meta-governance | `meta-governance-integrity`, `governance-evolution-governance`, `governance-compression-governance` | High for **authors** of new governance; low for **implementers** |
| Governance minimalism docs inside dense pack | `governance-minimalism.md` adjacent to ~59 governance files | Ironic overload — use minimalism doc as **gate**, not as extra reading |
| Factory teaching Factory how to compress | Compression + operational modes + meta-governance | Correct content; fatigue from **count** — tiered modes, not new compression layer |

**Rule:** If a doc’s primary reader is “future governance author,” it is **Tier 3 reference**, not onboarding.

---

## 4. Taxonomy inflation

| Metric | Observation |
|--------|-------------|
| Factory `*taxonomy*.md` | ~34 files — strong for **post-mortem diagnosis** |
| Drift taxonomy per concern | Pairs 1:1 with governance triads |
| Risk | Operators read taxonomy before governance |

**Compression opportunities:**

1. **Drift taxonomy index** — README appendix: link list only (no new ontology).  
2. On edit: fold small taxonomy tables into parent `*-governance.md` as **Appendix: drift codes**.  
3. REPORT discipline: cite taxonomy **by code**, not by re-summarizing entire taxonomy doc.

---

## 5. Checklist fatigue

| Layer | Count / behavior | Fatigue driver |
|-------|------------------|----------------|
| Forge mirrored checklists | ~38 | Each mirrors a governance triad |
| Foundation `qa-checklist.md` | Base layer | Correct but hidden under Forge enumeration |
| QA confidence / human escalation / multi-agent | Meta-QA on QA | Valuable at battle-test; heavy for daily |

**Compression opportunities:**

- **operational-modes-model** — light / standard / battle (documented, underused in practice).  
- Triumph V3 charter = **battle** mode only — do not normalize for routine pages.  
- `qa-checklist.md` remains **single overlay orchestrator** — specialist checklists invoked by reference, not README inline list.

---

## 6. Repeated semantic declarations

| Concept | Repetition count (approx.) | Stop condition |
|---------|---------------------------|----------------|
| Not a runtime / not autonomous | 6+ global surfaces | Link AGENTS; one sentence max elsewhere |
| Registry row ≠ deployed | 4+ | Link terminology registry |
| Forge overlay / foundation wins | 4+ | Link transition stabilization doc |
| Documentation-only validation | 3+ Factory + governance | Link validation-chain-semantics |
| Phase 1 documentation-first | README, AGENTS, execution-model, Factory safe-unknown | README + AGENTS only for new prose |

---

## 7. Over-explained concepts

| Concept | Symptom | Lighter surface |
|---------|---------|-----------------|
| Seven-layer Factory story | Multiple overviews | `system-overview.md` + INDEX row |
| Artifact bus / semantic objects | Several v0 overviews | `artifact-architecture-overview-v0.md` only |
| Execution bridge / queue / orchestrator | Runtime contracts + Factory semantics | mars-runtime README + terminology registry |
| HITL | Repeated in Factory + governance + Forge | `execution-model.md` + Factory workflow v0 |
| SAFE UNKNOWN | Defined everywhere | AGENTS + one Factory boundary doc |

---

## 8. Where operational value plateaued

| Zone | Plateau signal |
|------|----------------|
| **New governance triads** | Marginal navigation gain; increased INDEX width |
| **New drift taxonomies** | Marginal unless tied to a new failure mode observed in production |
| **New meta-governance docs** | Teaches governance about governance — rarely unblocks a page build |
| **Additional topology maps** | Diminishing unless a **new entity** joins ecosystem |
| **Parallel README essays** | Duplicates OPERATIONAL-INDEX purpose |

**Still high value (do not compress blindly):**

- `website-factory-workflow-v0.md`, handoff contracts, artifact architecture  
- `safe-unknown-boundary.md`, `first-operational-runbook-v0.md`  
- Forge `AGENT.md`, `workflow.md`, core `qa-checklist.md`  
- governance honesty spine (AGENTS, execution-model, registry rules)  
- ORCA OPERATIONAL-INDEX discipline  

---

## 9. Compression opportunities (prioritized, human-gated)

| Priority | Action | Effort |
|----------|--------|--------|
| P0 | Factory OPERATIONAL-INDEX: **core run** vs **extended** sections | Small editorial |
| P0 | Tier banners in pack READMEs (see entrypoint model) | Tiny |
| P1 | Drift taxonomy link appendix in Factory README | Small |
| P1 | Dedupe OPERATIONAL-INDEX Frontend duplicate block | Small |
| P2 | Merge taxonomy into governance on **touch-only** edits | Ongoing |
| P2 | Deprecation banners on superseded Forge design doc sections | Small |
| P3 | Prune only with lifecycle log + human sign-off | Per [documentation-entropy-rules.md](documentation-entropy-rules.md) |

**Explicitly reject:** semantic merge bots, auto-prune, governance certification.

---

## 10. Relation to existing pack self-awareness

Factory already documents compression and minimalism ([governance-compression-governance.md](../projects/mars-website-factory/governance-compression-governance.md), [governance-minimalism.md](../projects/mars-website-factory/governance-minimalism.md)). Phase 3 recommendation: **apply** those docs — **do not** author a competing meta-layer.

---

## Related

- [website-factory-compression-review-v0.md](website-factory-compression-review-v0.md)  
- [survivability-lightweight-maintenance-model-v0.md](survivability-lightweight-maintenance-model-v0.md)
