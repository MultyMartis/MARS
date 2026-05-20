# MARS Website Factory - Provenance Drift Taxonomy

**Status:** **documented** - Website Factory drift vocabulary for provenance and source-lineage governance.  
**Not:** automated drift detector, runtime provenance monitor, universal evidence taxonomy, or source-trust engine.

**Parent layer:** [knowledge-provenance-governance.md](knowledge-provenance-governance.md).  
**Lineage model:** [source-lineage-model.md](source-lineage-model.md).  
**Forge checklist:** [`../../agents/mars-forge/source-lineage-checklist.md`](../../agents/mars-forge/source-lineage-checklist.md).

---

## 1. Purpose

This taxonomy gives Website Factory a shared vocabulary for naming provenance and lineage failures before they become frontend implementation, QA, freeze, or handoff defects.

Provenance drift occurs when source origin, authority, freshness, transformation, or uncertainty becomes less visible while downstream confidence increases.

---

## 2. Drift Pattern Index

| Pattern | Short definition |
|---------|------------------|
| **Lineage loss** | The chain from current artifact back to source authority is missing or unreadable. |
| **Undocumented transformation** | A source was interpreted, summarized, rewritten, normalized, converted, or implemented without disclosing what changed. |
| **Stale-source reuse** | Superseded, archive, contradicted, or freshness-unknown material continues to drive work. |
| **Authority-chain collapse** | Primary, derived, interpreted, summarized, inferred, and implementation outputs blend into one authority story. |
| **Derived-source confusion** | A derivative artifact is treated as if it were primary source. |
| **Summary contamination** | A compressed summary drops uncertainty, contradiction, scope limits, or parent-source nuance. |
| **Transformation ambiguity** | Operators cannot tell whether a claim is observed, interpreted, rewritten, inferred, or implemented. |
| **Provenance invisibility** | Source origin and authority are omitted from notes, reports, or handoffs. |
| **Interpretation propagation** | One interpreted or assumed read moves downstream as verified fact. |
| **Source freshness erosion** | Active/stale/superseded status becomes unclear over sessions or handoffs. |
| **Inherited hallucination** | A fabricated or weak claim is inherited from prior output and becomes stronger by repetition. |
| **Secondary-source inflation** | Reports, screenshots, generated docs, or code comments gain more authority than their parent source. |
| **Unknown-origin implementation** | Code, assets, copy, structure, behavior, or QA claims are reused without known origin. |

---

## 3. Pattern Details

### 3.1 Lineage Loss

**Definition:** The source chain cannot be reconstructed from current artifacts.

**Symptoms:**

- "Based on previous work" without parent source.
- Code or report references source vaguely.
- A section uses copy, icons, layout, or behavior with no active source path.
- Future operator cannot tell whether the artifact is primary or derivative.

**Risk:** unknown authority drives implementation or freeze.

**Response:** record `SOURCE LINEAGE FINDINGS`; restore parent source or mark SAFE UNKNOWN.

### 3.2 Undocumented Transformation

**Definition:** A material source change occurs without disclosure.

**Symptoms:**

- Visual design becomes semantic matrix without noting inferred grouping.
- Summary rewrites source language and drops qualifiers.
- Implementation converts a layout pattern into DOM structure without explaining changed grouping.
- QA report turns source-only review into rendered PASS.

**Risk:** future work inherits transformation as source truth.

**Response:** name transformation type, scope, authority retained/lost, and uncertainty.

### 3.3 Stale-Source Reuse

**Definition:** Superseded, archive, contradicted, or freshness-unknown material continues to govern work.

**Symptoms:**

- V1 or archive source influences V2 implementation.
- Old report is reused after source pack changed.
- Previous CSS/DOM becomes layout authority despite new design source.
- Source freshness is assumed because file exists.

**Risk:** stale decisions contaminate current source chain.

**Response:** check active source priority; quarantine stale material or escalate.

### 3.4 Authority-Chain Collapse

**Definition:** Different source layers collapse into one undifferentiated authority.

**Symptoms:**

- Primary screenshots, implementation pack, code, report, and summary are cited as equal.
- "The source says" refers to a mixture of observed facts and inferred conclusions.
- QA treats prior implementation as proof of design intent.

**Risk:** downstream artifacts gain fake authority.

**Response:** classify layers with [source-lineage-model.md](source-lineage-model.md).

### 3.5 Derived-Source Confusion

**Definition:** A derivative artifact is treated as primary source.

**Symptoms:**

- Cropped screenshot, agent summary, extracted matrix, or previous report overrides original approved source.
- Implementation notes are used as design authority without parent-source check.
- Structured checklist output is treated as the actual source.

**Risk:** reduced-authority artifacts drive material frontend choices.

**Response:** identify parent source and inherited authority limits.

### 3.6 Summary Contamination

**Definition:** A summary omits important uncertainty, contradiction, or scope boundaries.

**Symptoms:**

- SAFE UNKNOWN disappears from handoff summary.
- "All sections aligned" replaces multiple partial findings.
- Summary shortens a contradiction into a preference.
- Prior report becomes canonical while evidence is missing.

**Risk:** confidence inflates as detail decreases.

**Response:** treat summaries as reduced authority; require parent source for material decisions.

### 3.7 Transformation Ambiguity

**Definition:** It is unclear whether a claim is source fact, interpretation, assumption, transformation, or output.

**Symptoms:**

- "Final design" could mean screenshot, code, QA note, or report.
- "Canonical section" could mean active source or current implementation.
- A rewritten CTA is not labeled as source copy, operator rewrite, or agent rewrite.

**Risk:** operators cannot know what may safely govern implementation.

**Response:** label layer, transformation, and authority.

### 3.8 Provenance Invisibility

**Definition:** Source origin and authority are not visible in artifacts or reports.

**Symptoms:**

- No source path in REPORT.
- No version, screen, block, or artifact reference.
- Asset origin not named.
- Handoff uses "same as before" without lineage.

**Risk:** future sessions depend on memory or assumptions.

**Response:** add source reference, freshness, layer, and disposition.

### 3.9 Interpretation Propagation

**Definition:** An interpreted, inferred, or assumed read moves downstream as verified fact.

**Symptoms:**

- Inferred grouping becomes DOM law.
- Desktop-only visual read becomes mobile intent.
- Unverified interaction behavior becomes JS requirement.
- Weak source read is repeated until it sounds explicit.

**Risk:** interpretation drift becomes implementation truth.

**Response:** restore observed/inferred/assumed/unknown labels and escalate when material.

### 3.10 Source Freshness Erosion

**Definition:** Active/stale/superseded status becomes unclear over time.

**Symptoms:**

- Multiple same-named exports exist.
- Implementation pack has no version reference.
- Old notes and new screenshots are both cited.
- No one can tell whether a prior report is current.

**Risk:** outdated source remains invisible inside current work.

**Response:** re-establish active source charter or mark SAFE UNKNOWN.

### 3.11 Inherited Hallucination

**Definition:** A fabricated, weak, or unsupported claim is inherited and strengthened across outputs.

**Symptoms:**

- An invented entity count appears in later docs.
- A guessed hover behavior becomes accepted requirement.
- Multiple agents agree because they share the same unsupported premise.
- A prior implementation mistake becomes source evidence.

**Risk:** hallucination becomes harder to challenge downstream.

**Response:** trace to parent source; if no authority exists, quarantine and report.

### 3.12 Secondary-Source Inflation

**Definition:** Secondary artifacts gain more authority than primary source.

**Symptoms:**

- QA report outranks active source because it is newer.
- Code comments become source of truth for content.
- Generated summary is treated as design pack.
- Screenshot crop overrides full screen source.

**Risk:** convenience replaces authority.

**Response:** restore authority chain and demote secondary artifacts to their proper layer.

### 3.13 Unknown-Origin Implementation

**Definition:** Implementation uses material whose source origin cannot be proven.

**Symptoms:**

- Copied copy, icons, images, CSS, JS, pricing, equipment lists, or section structure have no source path.
- Existing code is assumed to be canonical because it exists.
- Asset folder contents are reused without brand/source authority.

**Risk:** legal, brand, semantic, visual, or conversion drift enters the product.

**Response:** SAFE UNKNOWN; quarantine or HITL before reuse when material.

---

## 4. Severity Guide

| Severity | Use when | Typical action |
|----------|----------|----------------|
| **Low** | Lineage gap is local, reversible, and does not affect meaning, trust, source priority, or freeze. | Continue with disclosure. |
| **Medium** | Derived/source layer is unclear but likely recoverable; implementation can be scoped or partial. | `SOURCE LINEAGE FINDINGS`; restore parent source before freeze. |
| **High** | Unknown, stale, or transformed source affects meaning, CTA, structure, assets, responsive behavior, QA confidence, or freeze. | SAFE UNKNOWN, HITL, or stop. |
| **Critical** | Contradictory or unknown-origin material would drive business claims, legal/compliance content, pricing, brand assets, delivery readiness, or approval inheritance. | STOP until human/source authority resolves. |

---

## 5. Anti-Patterns

Forbidden drift:

- Blind inheritance.
- Undocumented transformations.
- Summary-as-source.
- Hidden provenance gaps.
- Stale-source continuation.
- Fake authority inheritance.
- Unknown-origin reuse.
- Source laundering.
- Derivation opacity.
- Lineage collapse.
- Polished downstream artifact treated as stronger than original source.
- Multiple-agent agreement treated as provenance proof.

---

## 6. Triumph V2 Lessons Captured

Triumph V2 exposed reusable provenance drift lessons:

- V1/V2 blend is a lineage problem before it becomes visual or semantic drift.
- A clean V2 report can still carry V1 assumptions if the derivation path is not visible.
- Equipment/pricing claims, fleet entities, CTA meaning, and section order need source freshness and authority disclosure.
- Shared assets may be legitimate media sources while still lacking authority to define layout, hierarchy, or semantics.
- Prior implementation can help locate work, but it is not source authority unless project governance explicitly promotes it.

These are Website Factory taxonomy lessons, not Triumph-specific redesign instructions.

---

## 7. SAFE UNKNOWN

Use **SAFE UNKNOWN** for provenance drift when:

| Drift condition | Required response |
|-----------------|-------------------|
| Origin cannot be named | Treat as unknown-origin source. |
| Parent source is missing | Do not use derivative as primary authority. |
| Freshness cannot be proven | Avoid PASS/freeze until resolved or waived. |
| Summary may have hidden uncertainty | Return to parent source for material decisions. |
| Transformation changed meaning but is undocumented | Escalate and document boundary. |
| Prior output is the only evidence | Treat as low-authority and verify against source. |

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Provenance Drift Taxonomy - lineage loss, undocumented transformation, stale-source reuse, authority-chain collapse, derived-source confusion, summary contamination, transformation ambiguity, provenance invisibility, interpretation propagation, source freshness erosion, inherited hallucination, secondary-source inflation, and unknown-origin implementation. |
