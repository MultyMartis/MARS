# Source lineage checklist - MARS Forge (overlay v0)

**Status:** **overlay checklist** for human-supervised provenance and source-lineage QA.  
**Not:** runtime provenance engine, source-trust AI, immutable audit log, autonomous authority system, or substitute for foundation QA.

**Factory methodology:** [`../../projects/mars-website-factory/knowledge-provenance-governance.md`](../../projects/mars-website-factory/knowledge-provenance-governance.md).  
**Lineage model:** [`../../projects/mars-website-factory/source-lineage-model.md`](../../projects/mars-website-factory/source-lineage-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/provenance-drift-taxonomy.md`](../../projects/mars-website-factory/provenance-drift-taxonomy.md).

---

## 1. When to Run

Run this checklist:

- after semantic source lock identifies the active source charter;
- before source interpretation findings are treated as implementation authority;
- before implementation choices rely on summaries, previous outputs, existing code, screenshots, matrices, implementation packs, or agent handoffs;
- before QA confidence, human escalation, multi-agent coordination, PASS, freeze, or delivery-readiness claims when source chains affect the scope;
- whenever source origin, freshness, transformation, authority inheritance, or derivation is unclear.

This checklist does not authorize guessing, source laundering, hidden transformations, stale-source continuation, or unknown-origin reuse.

---

## 2. Source Lineage QA

- [ ] **Primary source named** - active source path, version, scope, artifact type, and freshness are named.
- [ ] **Source layer classified** - primary, derived, interpreted, transformed, summarized, inferred, or unknown-origin.
- [ ] **Parent source linked** - every material derived, interpreted, transformed, summarized, or inferred artifact names its parent source.
- [ ] **Authority inheritance stated** - what authority is retained, reduced, lost, or unknown.
- [ ] **Derivation disclosed** - extraction, interpretation, summary, rewrite, normalization, implementation conversion, QA conclusion, or human decision is named.
- [ ] **Transformation boundary visible** - material meaning, hierarchy, CTA, asset, responsive, interaction, state, accessibility, or QA changes are disclosed.
- [ ] **Source freshness checked** - active, stale, superseded, archive, partial, contradicted, or unknown.
- [ ] **Summary authority reduced** - summaries are not treated as primary source unless explicitly promoted by human/project authority.
- [ ] **Unknown-origin material quarantined** - source origin gaps are SAFE UNKNOWN before reuse.
- [ ] **Lineage readable** - a future operator can reconstruct the source chain without relying on session memory.

---

## 3. Source Authority QA

- [ ] Primary source governs unless a named priority rule or human decision supersedes it.
- [ ] Derived artifacts do not exceed parent authority.
- [ ] Existing implementation is not treated as design/source authority by default.
- [ ] Prior reports and summaries are evidence records, not source authority, unless explicitly promoted.
- [ ] Polished downstream artifacts are not assumed stronger than original source.
- [ ] Shared assets are not allowed to define structure, hierarchy, or semantics unless source authority grants that role.
- [ ] Multiple-agent agreement is not treated as proof of source authority.

---

## 4. Drift Taxonomy Gate

Check for and record patterns from [`provenance-drift-taxonomy.md`](../../projects/mars-website-factory/provenance-drift-taxonomy.md):

- [ ] Lineage loss.
- [ ] Undocumented transformation.
- [ ] Stale-source reuse.
- [ ] Authority-chain collapse.
- [ ] Derived-source confusion.
- [ ] Summary contamination.
- [ ] Transformation ambiguity.
- [ ] Provenance invisibility.
- [ ] Interpretation propagation.
- [ ] Source freshness erosion.
- [ ] Inherited hallucination.
- [ ] Secondary-source inflation.
- [ ] Unknown-origin implementation.

Any material match requires `SOURCE LINEAGE FINDINGS`.

---

## 5. Stale-Lineage Gate

Stop, quarantine, or escalate when:

- source freshness cannot be proven;
- archive, V1, old PDF, prior report, or stale implementation is influencing active work;
- a derived artifact was created before a source update;
- a source contradiction appears after downstream work already began;
- a summary is newer than the primary source but does not supersede it;
- current implementation depends on old assumptions or undocumented transformations.

Use **SAFE UNKNOWN**, **PARTIAL - lineage**, **HITL REQUIRED**, or **STOP** rather than silent continuation.

---

## 6. Transformation-Boundary QA

For each material transformation, verify:

- [ ] What changed from parent source is named.
- [ ] What remained source-faithful is named.
- [ ] What authority was reduced is named.
- [ ] What uncertainty survived is named.
- [ ] What was inferred or assumed is not presented as observed.
- [ ] What requires human decision is escalated.
- [ ] What affects implementation is recorded before PASS/freeze.

Material transformations include source extraction, visual interpretation, semantic matrix creation, copy rewrite, component mapping, responsive translation, implementation conversion, QA conclusion, and report summary.

---

## 7. Escalation Boundary

Stop and escalate when lineage uncertainty would affect:

- meaning, section order, entity count, offer, price, service, equipment, trust claim, or CTA role;
- visual hierarchy, grouping, screen-local role, composition, or design authority;
- asset origin, icon source, logo, image, illustration, or brand usage;
- responsive behavior, interaction behavior, UI state, accessibility behavior, or JS hook authority;
- QA confidence, PASS, freeze, delivery readiness, approval inheritance, or waiver;
- multi-agent handoff, reviewer independence, validator evidence, or responsibility ownership.

Unknown origin, stale lineage, and authority-chain collapse are not implementation details. They are source-authority risks.

---

## 8. REPORT Block

Use this block when lineage affects implementation:

```text
SOURCE LINEAGE FINDINGS - <section or block_id> - <source ref>

Primary source:
- <path / version / scope / freshness>

Source layers:
- <primary / derived / interpreted / transformed / summarized / inferred / unknown-origin artifacts>

Derivation and transformation:
- <parent source -> transformation type -> authority retained/reduced/lost>

Authority chain:
- <what governs, what is secondary, what is quarantined, what requires HITL>

Drift taxonomy:
- <lineage loss / stale-source reuse / summary contamination / etc.>

Unknown / stale / contradictory lineage:
- <SAFE UNKNOWN / HITL / STOP items>

Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
Action: proceed | continue with disclosure | quarantine | request source | escalate | stop
Evidence: <paths, docs, report refs>
```

---

## 9. Not Claimed

- No runtime provenance engine.
- No autonomous source-trust AI.
- No immutable lineage guarantee.
- No universal provenance law.
- No automatic source freshness detection.
- No authority to redesign Triumph or any project.
- No permission to reuse unknown-origin source silently.

---

## 10. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge source lineage checklist; adds `SOURCE LINEAGE FINDINGS` for provenance QA, lineage traceability QA, source-authority QA, derivation disclosure QA, stale-lineage QA, and transformation-boundary QA. |
