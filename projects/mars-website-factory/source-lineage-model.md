# MARS Website Factory - Source Lineage Model

**Status:** **documented** - Website Factory source-lineage model for human-supervised frontend governance.  
**Not:** runtime lineage graph, provenance database, autonomous trust model, immutable audit log, or universal source law.

**Parent layer:** [knowledge-provenance-governance.md](knowledge-provenance-governance.md).  
**Companion taxonomy:** [provenance-drift-taxonomy.md](provenance-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/source-lineage-checklist.md`](../../agents/mars-forge/source-lineage-checklist.md).

---

## 1. Purpose

The Source Lineage Model gives Website Factory a common vocabulary for classifying source layers before they influence frontend implementation, QA, escalation, or freeze.

Its purpose is to prevent:

- primary source being replaced by a summary;
- transformed artifacts looking more authoritative than their parents;
- unknown-origin artifacts entering implementation;
- stale source chains surviving through polished downstream work;
- human decisions, assumptions, and SAFE UNKNOWN states disappearing across handoffs.

---

## 2. Lineage Layers

| Layer | Definition | Authority posture | Required handling |
|-------|------------|-------------------|-------------------|
| **Primary source** | Original active source with governing authority for the scope: approved design export, implementation pack, project pack, human decision, canonical matrix, or named source path. | Highest authority inside its scope, unless superseded by named priority rule or human decision. | Name path/version, scope, freshness, and priority. |
| **Derived source** | Artifact created from primary or another source: extracted matrix, exported crop, copied section note, generated handoff, or structured checklist. | Inherits limited authority from parent; cannot exceed parent authority. | Disclose parent source and derivation type. |
| **Interpreted source** | A source read that separates observed, inferred, assumed, unknown, and contradictory claims. | Carries interpretation confidence, not raw source authority. | Pair with [source-interpretation-governance.md](source-interpretation-governance.md). |
| **Transformed source** | Artifact whose form or semantics changed: rewrite, normalization, layout conversion, component mapping, responsive translation, or design-to-code conversion. | Authority depends on disclosed transformation boundary. | State what changed and what authority survived. |
| **Summarized source** | Condensed version of a larger source, prior report, checklist output, or agent handoff. | Lower authority than parent; may omit nuance, contradiction, or uncertainty. | Do not treat as full source unless promoted by explicit human/project decision. |
| **Inferred source** | A claim generated from patterns, adjacency, prior section logic, visual rhythm, or implementation convention. | Weak authority; never primary. | Label inference strength and escalate when material. |
| **Unknown-origin source** | Artifact, content, asset, code, rule, or claim whose origin or authority cannot be proven. | No reliable authority until lineage is restored or approved. | Mark SAFE UNKNOWN; escalate when material. |

---

## 3. Authority Inheritance

Authority inheritance is conservative:

1. A child artifact cannot inherit more authority than its parent source grants.
2. A summary inherits less authority than the source it summarizes.
3. A transformation inherits authority only for the parts it preserves and discloses.
4. An interpreted source carries confidence labels, not raw certainty.
5. An inferred source cannot become primary by repetition.
6. Unknown-origin material has no governing authority until lineage is restored or human authority promotes it.

**Rule:** downstream usefulness is not the same as downstream authority.

---

## 4. Derivation Disclosure

Every material derived, interpreted, transformed, summarized, or inferred source should disclose:

| Field | Question |
|-------|----------|
| **Parent source** | What source did this artifact come from? |
| **Source layer** | Is it primary, derived, interpreted, transformed, summarized, inferred, or unknown-origin? |
| **Transformation type** | Extraction, interpretation, summary, rewrite, normalization, implementation conversion, QA conclusion, or human decision? |
| **Scope** | Which page, section, block, asset, breakpoint, interaction, or QA claim does it govern? |
| **Authority inherited** | What authority does it retain, reduce, or lose? |
| **Freshness** | Is the parent source active, stale, superseded, partial, or contradicted? |
| **Uncertainty carried** | What SAFE UNKNOWN, ambiguity, contradiction, or assumption remains? |
| **Escalation status** | Does the chain need HITL, stop, or continue-with-disclosure? |

---

## 5. Transformation Boundaries

Transformation boundaries mark where meaning, authority, or evidence may change.

| Boundary | Risk | Governance response |
|----------|------|---------------------|
| **Design export -> visual read** | Screenshot artifacts or visual ambiguity become source truth. | Use source interpretation and visual reconciliation findings. |
| **Visual read -> semantic matrix** | Grouping, hierarchy, CTA role, or entities may be inferred. | Preserve observed/inferred/assumed/unknown labels. |
| **Matrix -> implementation pack** | Details may be normalized, omitted, or generalized. | Disclose derivation and authority limits. |
| **Implementation pack -> code** | DOM, CSS, JS, assets, and responsive rules may change semantics. | Record transformation and source-authority QA. |
| **Code -> QA report** | Passing build or visual check may inflate source confidence. | Use QA confidence boundaries. |
| **Report -> future session** | Summaries may lose uncertainty, contradictions, or source priority. | Preserve lineage and findings explicitly. |

Material transformations should be reported as `SOURCE LINEAGE FINDINGS` when the transformation affects implementation authority, QA confidence, or freeze.

---

## 6. Stale-Source Handling

A source or derivation becomes stale when:

- a newer active version supersedes it;
- a human decision revokes or narrows it;
- an implementation pack changes after a derived artifact was created;
- a screenshot, matrix, or report is from an archive path;
- a source contradiction is discovered;
- a downstream artifact depends on old assumptions;
- source freshness cannot be proven.

Required handling:

| Stale condition | Action |
|-----------------|--------|
| Confirmed superseded source | Do not use as authority; quarantine or cite as historical context only. |
| Possible stale source | Mark SAFE UNKNOWN until freshness is verified. |
| Stale source already influenced implementation | Record lineage risk, inspect affected scope, and escalate if material. |
| Stale summary conflicts with active source | Active primary source wins unless human/project priority says otherwise. |
| Unknown freshness affects freeze | Stop or HITL before PASS/freeze. |

---

## 7. Lineage Traceability

Lineage is traceable when a future operator can answer:

- Which source was primary?
- What artifacts were derived from it?
- What was interpreted, transformed, summarized, or inferred?
- What authority was inherited or reduced?
- What source freshness was known?
- What uncertainty, contradiction, or SAFE UNKNOWN survived?
- What human decision or governance rule resolved conflicts?
- Which report findings preserve the chain?

If these cannot be answered from available documents and reports, lineage is not sufficiently traceable.

---

## 8. Provenance Escalation

Escalate provenance issues when they affect:

- section meaning, order, or entity count;
- CTA role, conversion intent, trust claims, pricing, equipment, or legal/compliance content;
- visual hierarchy, grouping, screen-local role, or composition;
- asset origin, icon family, logo, illustration, image, or brand usage;
- responsive behavior, interaction behavior, UI states, or accessibility behavior;
- QA confidence, PASS language, freeze, delivery readiness, or approval inheritance;
- multi-agent handoff, reviewer independence, validator evidence, or HITL boundary.

Escalation levels:

| Level | Use when |
|-------|----------|
| **Continue with disclosure** | Low-impact, reversible lineage gap; clearly reported. |
| **PARTIAL - lineage** | Work can proceed but authority is narrowed or unresolved. |
| **SAFE UNKNOWN** | Origin, authority, freshness, or transformation cannot be proven. |
| **HITL required** | Human/project authority must resolve source priority, promotion, or contradiction. |
| **STOP** | Unknown-origin, stale, or contradictory lineage would drive material implementation or freeze. |

---

## 9. Reporting Shape

Use this compact block when lineage affects implementation:

```text
SOURCE LINEAGE FINDINGS - <section or block_id> - <source ref>

Primary source:
- <path / version / scope / freshness>

Derived / interpreted / transformed / summarized / inferred sources:
- <artifact> -> <parent source> -> <transformation type> -> <authority retained/lost>

Authority chain:
- <what governs, what is secondary, what is quarantined>

Lineage risks:
- <stale source / unknown origin / summary contamination / transformation ambiguity>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
Action: proceed | continue with disclosure | quarantine | request source | escalate | stop
Evidence: <paths, docs, report refs>
```

---

## 10. SAFE UNKNOWN

Use **SAFE UNKNOWN** when:

| Situation | Required response |
|-----------|-------------------|
| Primary source is missing | Do not promote derived artifacts to primary authority. |
| Parent source cannot be identified | Treat as unknown-origin. |
| Transformation is undocumented | Disclose gap and narrow authority. |
| Summary is the only available artifact | Treat as reduced authority; request parent source when material. |
| Freshness is unclear | Do not freeze until active/stale status is resolved or explicitly waived. |
| Authority inheritance is unclear | Escalate before material implementation decisions. |
| Unknown-origin code/assets/copy exist | Quarantine or HITL before reuse. |

---

## 11. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Source Lineage Model - primary/derived/interpreted/transformed/summarized/inferred/unknown-origin layers, authority inheritance, derivation disclosure, stale-source handling, lineage traceability, and provenance escalation. |
