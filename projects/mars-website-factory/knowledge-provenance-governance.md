# MARS Website Factory - Knowledge Provenance & Source Lineage Governance

**Status:** **documented** - Website Factory provenance governance and human-supervised source-lineage methodology only.  
**Not:** runtime provenance engine, autonomous source-trust AI, immutable lineage guarantee, universal provenance law, or replacement for human project authority.

**Core principle:** frontend AI systems must preserve **source authority visibility, derivation traceability, provenance integrity, transformation transparency, lineage continuity, and evidence survivability**.

**Companion documents:** [source-lineage-model.md](source-lineage-model.md), [provenance-drift-taxonomy.md](provenance-drift-taxonomy.md).  
**Related layers:** [decision-transparency-governance.md](decision-transparency-governance.md), [strategic-intent-governance.md](strategic-intent-governance.md), [source-interpretation-governance.md](source-interpretation-governance.md), [qa-confidence-governance.md](qa-confidence-governance.md), [human-escalation-governance.md](human-escalation-governance.md), [multi-agent-coordination-governance.md](multi-agent-coordination-governance.md), [temporal-evolution-governance.md](temporal-evolution-governance.md), [context-survivability-governance.md](context-survivability-governance.md), [cross-project-transfer-governance.md](cross-project-transfer-governance.md), [organizational-memory-governance.md](organizational-memory-governance.md), [visual-reconciliation-layer.md](visual-reconciliation-layer.md), [artifact-lineage-semantics-v0.md](artifact-lineage-semantics-v0.md), [artifact-transfer-semantics-v0.md](artifact-transfer-semantics-v0.md).  
**Forge checklist:** [`../../agents/mars-forge/source-lineage-checklist.md`](../../agents/mars-forge/source-lineage-checklist.md).

---

## 1. Positioning

Knowledge Provenance & Source Lineage Governance formalizes how Website Factory frontend work keeps track of **where knowledge came from**, **how it changed**, **what authority it still carries**, and **what uncertainty survived the transformation**.

| This layer governs | This layer does not govern |
|--------------------|----------------------------|
| Source lineage, provenance visibility, authority continuity, transformation traceability, and derivation integrity | Automated provenance storage, cryptographic lineage, runtime trust scoring, or source ranking AI |
| Human-readable disclosure of primary, derived, interpreted, transformed, summarized, inferred, stale, and unknown-origin sources | A universal epistemology or legal evidence standard |
| Drift vocabulary for lineage loss, stale-source contamination, derived-source confusion, authority-chain collapse, and source laundering | Claims that polished downstream artifacts are automatically more authoritative |
| Forge reporting discipline for `SOURCE LINEAGE FINDINGS` | Redesigning Triumph or any other project |

This layer exists because a frontend system can keep files, screenshots, notes, and prior outputs while still losing provenance. The risk is not merely absent files. The risk is that a downstream artifact starts to look canonical while its original authority, derivation path, transformation boundary, or uncertainty has disappeared.

---

## 2. Canonical Definition

**Knowledge provenance** is the visible relationship between an implementation-relevant claim and the source chain that produced it.

**Source lineage** is the traceable path from original authority to current use, including every meaningful derivation, interpretation, transformation, summary, inference, or uncertainty.

Together they preserve:

- **Source authority visibility** - the current operator can see which source has governing authority.
- **Derivation traceability** - downstream artifacts disclose what they came from and how.
- **Provenance integrity** - origin, freshness, and authority are not laundered by repetition.
- **Transformation transparency** - interpretation, summarization, extraction, rewriting, or implementation conversion remains visible.
- **Lineage continuity** - a later session can reconstruct the source chain without relying on memory.
- **Evidence survivability** - source gaps, stale links, SAFE UNKNOWN, and contradictions survive handoff and reporting.
- **Authority continuity** - authority does not silently increase as an artifact becomes cleaner, newer, or more polished.

The central test: **can a future operator tell why this implementation decision is authorized, what source it derives from, what changed during transformation, and what remains unknown?**

---

## 3. Required Vocabulary

| Concept | Meaning |
|---------|---------|
| **Source lineage** | The visible chain from source origin to current use, including derived, interpreted, transformed, summarized, inferred, or unknown-origin stages. |
| **Provenance integrity** | The source chain remains honest about origin, authority, freshness, transformation, and uncertainty. |
| **Authority chain** | The ordered relationship between source artifacts, project rules, implementation packs, human decisions, and downstream artifacts. |
| **Derivation traceability** | A future operator can identify what artifact or claim was derived from what source and by what kind of transformation. |
| **Transformation visibility** | Meaningful changes such as interpretation, summarization, extraction, rewrite, normalization, implementation conversion, or QA conclusion are disclosed. |
| **Source mutation** | A source or source-derived artifact changes content, scope, authority, version, or meaning after downstream work relied on it. |
| **Stale derivation** | A downstream artifact continues to rely on a source that has been superseded, invalidated, contradicted, or made incomplete. |
| **Provenance contamination** | Prior outputs, summaries, archive material, stale screenshots, adjacent sections, or foundation defaults distort the active source chain. |
| **Derived-source ambiguity** | It is unclear whether a downstream artifact is authoritative source, summary, interpretation, approximation, or implementation output. |
| **Authority inheritance** | A downstream artifact carries only the authority that is explicitly allowed by its parent source and transformation boundary. |
| **Lineage survivability** | The chain remains readable across sessions, agents, reviews, and reports. |
| **Provenance readability** | Lineage is written in a way a human operator can use, not hidden in vague phrases like "based on previous work." |
| **Source freshness** | Whether the source remains active, current, superseded, stale, partial, or contradicted. |
| **Transformation escalation** | A transformation is material enough to require disclosure, QA finding, HITL, or stop condition. |
| **Provenance uncertainty** | The origin, authority, transformation, freshness, or chain continuity cannot be proven from available artifacts. |

---

## 4. Core Rules

- **Source authority should stay visible.**
- **Derivation must remain traceable.**
- **Summaries reduce authority** unless a human or project rule explicitly promotes them.
- **Transformed artifacts require disclosure** when they affect implementation, QA, source interpretation, or freeze.
- **Stale lineage increases risk** even when the downstream artifact is polished.
- **Provenance gaps must surface** as findings, SAFE UNKNOWN, HITL, or stop conditions.
- **Unknown origin requires escalation** when the artifact would drive meaning, structure, copy, CTA, visual hierarchy, interaction, responsive behavior, asset authority, QA, or freeze.
- **Lineage readability matters** because future operators cannot preserve what they cannot understand.
- **Authority does not automatically flow downstream** through summaries, screenshots, agent outputs, or prior implementations.
- **A polished downstream artifact may be semantically weaker, less authoritative, and more contaminated than the original source.**

---

## 5. Authority vs Polish

Frontend AI systems are vulnerable to polished-source bias: a clean implementation note, confident summary, visually attractive mockup, or previous agent report can feel more trustworthy than the messy original source.

Governance rule:

| Artifact condition | Authority posture |
|--------------------|------------------|
| Original approved source is messy but active | Preserves primary authority unless superseded by named human/project decision. |
| Downstream summary is polished but derivative | Carries reduced authority; must cite parent source and transformation. |
| Implemented UI is visually coherent | Does not become source authority for future meaning unless explicitly promoted. |
| Prior report is confident but source chain is missing | Treat as provenance risk, not proof. |
| Current file exists but origin is unknown | Treat as unknown-origin source until lineage is restored or escalated. |

**Rule:** polish improves readability, not authority. Authority depends on lineage, source priority, freshness, and disclosed transformation.

---

## 6. Transformation Boundaries

Every source transformation should identify:

| Transformation | Disclosure requirement |
|----------------|------------------------|
| **Extraction** | What was pulled from source and what was omitted. |
| **Interpretation** | What is observed, inferred, assumed, unknown, or contradictory. |
| **Summary** | What detail, uncertainty, contradiction, or source nuance may have been lost. |
| **Normalization** | What terms, fields, sections, or component mappings changed shape. |
| **Implementation conversion** | How source meaning became DOM, CSS, JS, assets, or responsive rules. |
| **QA conclusion** | What evidence supports the conclusion and what source lineage it relies on. |
| **Human decision** | Who or what authority changed the chain, and what it superseded or clarified. |

Material transformation requires `SOURCE LINEAGE FINDINGS` when it affects authority, confidence, freshness, or downstream implementation decisions.

---

## 7. Required Provenance Questions

Before frontend implementation, QA confidence, escalation, or freeze, ask:

- What is the **primary source** for this decision?
- Is this artifact primary, derived, interpreted, transformed, summarized, inferred, or unknown-origin?
- What authority does this artifact inherit, and what authority has it lost?
- Has the source been superseded, mutated, contradicted, or made stale?
- Did a summary remove uncertainty, contradiction, or scope limits?
- Did a transformation change meaning, hierarchy, CTA role, asset authority, interaction behavior, or responsive intent?
- Can a future operator reconstruct the lineage without this session's memory?
- Are provenance gaps visible in REPORT, not hidden in implementation?

---

## 8. Anti-Patterns

Forbidden drift:

| Anti-pattern | Why it is forbidden |
|--------------|---------------------|
| **Blind inheritance** | Treats previous outputs as authority without checking lineage. |
| **Undocumented transformations** | Hides interpretation, summary, rewrite, extraction, or implementation conversion. |
| **Summary-as-source** | Promotes compressed downstream notes above original authority. |
| **Hidden provenance gaps** | Makes unknown origin look safe by silence. |
| **Stale-source continuation** | Keeps building from superseded or invalidated material. |
| **Fake authority inheritance** | Claims downstream artifacts have authority that was never granted. |
| **Unknown-origin reuse** | Reuses content, assets, layout, or code without knowing where it came from. |
| **Source laundering** | Repetition, formatting, or agent handoff makes weak or unknown claims look canonical. |
| **Derivation opacity** | A future operator cannot see what source produced the artifact. |
| **Lineage collapse** | Primary, derived, interpreted, summarized, and inferred sources blend into one confidence story. |

---

## 9. Forge Integration

When Forge is selected, provenance governance becomes a pre-freeze QA concern:

- Run [`source-lineage-checklist.md`](../../agents/mars-forge/source-lineage-checklist.md) before declaring section PASS, freeze, or source-authority completion when source chains affect implementation.
- Record **SOURCE LINEAGE FINDINGS** for provenance QA, lineage traceability QA, source-authority QA, derivation disclosure QA, stale-lineage QA, and transformation-boundary QA.
- Use [source-lineage-model.md](source-lineage-model.md) to classify source layers and authority inheritance.
- Use [provenance-drift-taxonomy.md](provenance-drift-taxonomy.md) to name lineage loss, stale-source reuse, authority-chain collapse, summary contamination, unknown-origin implementation, and related patterns.
- Keep **SOURCE LINEAGE FINDINGS** separate from **SOURCE INTERPRETATION FINDINGS**, **QA CONFIDENCE FINDINGS**, **HUMAN ESCALATION FINDINGS**, and **MULTI-AGENT FINDINGS**, then summarize whether the source chain is readable and safe to continue.
- Keep strategy-origin and stakeholder-authority gaps visible for `STRATEGIC INTENT FINDINGS` when source lineage affects business priority, conversion hierarchy, proof authority, or operational trust.
- Keep version lineage, freeze-state divergence, and stale-history risk visible for `TEMPORAL EVOLUTION FINDINGS` when source lineage affects long-term continuity.
- Keep compressed-source, summarized-source, checkpoint-memory, and reconstruction ambiguity visible for `CONTEXT SURVIVABILITY FINDINGS` when source lineage must survive compression or later continuation.
- Keep cross-project source, transfer authority, inherited assumptions, and compatibility evidence visible for `CROSS-PROJECT TRANSFER FINDINGS` when prior projects, templates, or reports influence current work.
- Keep reasoning path, assumption disclosure, transformation tradeoffs, and traceable conclusions visible for `REASONING VISIBILITY FINDINGS` when source lineage drives a recommendation or escalation.
- Keep lesson source, operational lineage, historical traceability, and reuse boundaries visible for `ORGANIZATIONAL MEMORY FINDINGS` when provenance becomes institutional knowledge or reusable operational wisdom.
- Treat unknown-origin or stale-lineage material as SAFE UNKNOWN or HITL when it affects meaning, structure, CTA, visual role, asset authority, responsive behavior, QA, or freeze.

This is human-supervised source-lineage methodology. It does not create immutable lineage, provenance automation, runtime source scoring, or autonomous authority decisions.

---

## 10. Triumph V2 Lessons Captured

Triumph V2 exposed reusable Website Factory provenance lessons:

- A canonical-looking implementation pack can still inherit stale or weak source assumptions if its derivation path is not visible.
- A screenshot, semantic matrix, validation note, or prior report may be useful while carrying lower authority than the active original source.
- V1/V2 contamination is not only visual or semantic; it is also provenance contamination when archive material survives without disclosure.
- A polished downstream artifact can be semantically weaker, less authoritative, and more contaminated than the original source.
- Multi-session rebuilds need lineage survivability because source decisions can otherwise become "known" only through memory.
- Unknown-origin icons, copied text, prices, fleet entities, or section structures require escalation before they become implementation facts.

These are Website Factory governance lessons, not Triumph redesign instructions.

---

## 11. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Primary source cannot be named | Authority cannot be proven. |
| Artifact origin is unknown | Cannot decide whether it is source, summary, interpretation, or output. |
| Derivation path is missing | Cannot prove what changed during transformation. |
| Source freshness is unclear | Cannot know whether source is active, stale, superseded, or contradicted. |
| Summary may have removed uncertainty | Cannot use it as full source authority. |
| Prior implementation is the only evidence | Cannot prove it reflects active source rather than drift. |
| Authority inheritance is not explicit | Cannot know whether downstream artifact may govern future work. |
| Transformation boundary is unclear | Cannot tell whether meaning, hierarchy, CTA, asset, or behavior changed. |

**Action:** state what lineage is unknown, what source or decision would resolve it, whether continuation is safe with disclosure, and whether HITL or stop is required.

---

## 12. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Knowledge Provenance & Source Lineage Governance layer - provenance integrity, source lineage, authority continuity, transformation transparency, drift taxonomy, and Forge `SOURCE LINEAGE FINDINGS`; documentation only. |
| v0.1 | 2026-05-17 | Linked Temporal Evolution & Project Drift Governance for version lineage, freeze-state divergence, stale-history risk, and long-term continuity. |
| v0.2 | 2026-05-17 | Linked Knowledge Compression & Context Survivability Governance for compressed-source risk, summarized-source authority, checkpoint memory, and reconstruction ambiguity. |
| v0.3 | 2026-05-17 | Linked Cross-Project Knowledge Transfer Governance for transfer source authority, inherited assumption visibility, and compatibility traceability. |
| v0.4 | 2026-05-17 | Linked Decision Transparency & Reasoning Visibility Governance for source-lineage rationale, transformation tradeoff disclosure, and traceable provenance-driven conclusions. |
| v0.5 | 2026-05-17 | Linked Organizational Memory & Institutional Knowledge Governance for lesson source, operational lineage, historical traceability, and reuse boundaries when provenance becomes institutional knowledge. |
