# MARS Website Factory - Transfer Drift Taxonomy

**Status:** **documented** - drift vocabulary for human-supervised cross-project knowledge transfer review.  
**Not:** automated drift detector, compatibility scoring system, universal pattern classifier, or autonomous governance enforcement.

**Parent governance:** [cross-project-transfer-governance.md](cross-project-transfer-governance.md).  
**Compatibility model:** [knowledge-transfer-compatibility-model.md](knowledge-transfer-compatibility-model.md).  
**Forge checklist:** [`../../agents/mars-forge/cross-project-transfer-checklist.md`](../../agents/mars-forge/cross-project-transfer-checklist.md).

---

## 1. Purpose

This taxonomy names the ways cross-project learning can become drift. It helps operators distinguish useful knowledge transfer from unsafe reuse, false analogy, template overreach, inherited assumptions, and project-identity erosion.

Use this taxonomy in `CROSS-PROJECT TRANSFER FINDINGS` when prior projects, templates, governance rules, implementation patterns, or visual treatments influence current work.

---

## 2. Drift Classes

| Drift pattern | Definition | Typical symptom | Governance response |
|---------------|------------|-----------------|---------------------|
| **Unsafe pattern reuse** | A prior pattern is reused before compatibility is validated. | "This worked on the last project" becomes implementation authority. | Run compatibility model; adapt, escalate, or reject. |
| **False analogy drift** | Surface similarity hides strategic, semantic, operational, or audience differences. | Same section type is treated as same meaning. | Re-check local source, CTA role, proof hierarchy, and audience. |
| **Template contamination** | Template structure, wording, visual tone, or assumptions overpower project-specific meaning. | The project starts reading like the template, not the source. | Separate shell from local meaning; rewrite project-specific regions. |
| **Strategic mismatch inheritance** | Business intent from a source project is inherited without current-project validation. | CTA pressure, proof order, or trust model feels wrong. | Record strategic fit findings; HITL when business meaning changes. |
| **Semantic portability failure** | Meaning does not survive transfer across entities, CTAs, proof, sections, or source vocabulary. | Correct-looking component carries the wrong role. | Treat as semantic mismatch; rebuild from local source. |
| **Copied-governance overreach** | Governance created for one project is applied elsewhere as universal law. | Local constraints become factory-wide commands. | Validate governance portability and authority scope. |
| **Cross-project assumption leakage** | Hidden assumptions from the source project enter the receiving project. | Uncited claims about audience, stack, proof, brand, or workflow appear. | Surface assumptions; require source evidence or SAFE UNKNOWN. |
| **Inappropriate standard transfer** | A useful standard is applied where the receiving project has different maturity, risk, or context. | Checklist or rule creates noise, delay, or false confidence. | Scope the standard to actual risk; document non-applicability. |
| **Visual-language contamination** | Visual treatments from another project leak into local brand, tone, hierarchy, or trust model. | Radius, card style, shadow, SaaS mood, dark/light treatment, or CTA styling feels foreign. | Run design intent and visual reconciliation QA. |
| **Operational mismatch reuse** | Implementation or workflow pattern assumes conditions the receiving project lacks. | Stack, build, assets, QA, or maintenance capacity do not match. | Run operational compatibility review; adapt or reject. |
| **Transfer-context blindness** | Transfer occurs without documenting source context, original problem, constraints, or adaptation. | Future operator cannot tell why reuse happened. | Add transfer traceability or mark SAFE UNKNOWN. |
| **Inherited incompatibility** | A known source-project limitation or workaround is transferred as if it were valid. | Old workaround becomes current architecture. | Identify original constraint; reject or replace locally. |
| **Project-identity erosion** | Reuse gradually flattens the receiving project's voice, visual language, trust posture, or strategic meaning. | Distinct projects begin to feel interchangeable. | Re-anchor to project sources and identity signals; escalate if material. |

---

## 3. Unsafe Pattern Reuse

**Definition:** using a prior solution because it is familiar, efficient, or previously successful before checking receiving-project fit.

Signals:

- reuse is justified by precedent instead of source authority;
- local audience, offer, proof, or tone is not checked;
- implementation shape is copied before semantic roles are confirmed;
- template or prior code is treated as faster than reading local sources.

Risk:

- strategic mismatch;
- semantic mismatch;
- hidden implementation coupling;
- wrong visual tone;
- governance authority inflation.

---

## 4. False Analogy Drift

**Definition:** assuming two projects, sections, assets, or governance needs are equivalent because they look similar.

Signals:

- "same kind of landing page" becomes enough evidence;
- service grids, CTAs, reviews, proof strips, or hero patterns are treated as interchangeable;
- operational offers inherit SaaS-style patterns from unrelated contexts;
- project-specific trust model is ignored.

Response:

- state the analogy;
- identify which dimensions actually match;
- list mismatches;
- transfer only after adaptation or HITL.

---

## 5. Template Contamination

**Definition:** a reusable shell imports meaning, hierarchy, tone, or assumptions beyond its intended structure.

Signals:

- placeholder language remains semantically active;
- generic CTA roles replace approved CTA roles;
- proof blocks follow template order instead of local authority;
- sections are added because the template has them;
- project voice becomes generic Website Factory voice.

Response:

- mark template regions as shell, not source;
- rewrite local meaning from project artifacts;
- record rejected template assumptions.

---

## 6. Strategic Mismatch Inheritance

**Definition:** a receiving project inherits business logic from another project without validating strategy.

Signals:

- copied CTA urgency;
- copied trust/proof placement;
- copied operational seriousness;
- copied lead-form pressure;
- copied audience assumptions;
- copied "best practice" that changes business priority.

Response:

- run strategic intent QA;
- compare business objective, conversion hierarchy, proof hierarchy, trust posture, stakeholder intent;
- escalate when mismatch affects conversion or trust.

---

## 7. Semantic Portability Failure

**Definition:** the transferred pattern keeps its shape but loses or mutates meaning.

Signals:

- same label means a different thing locally;
- same icon suggests wrong entity or proof;
- same card pattern flattens different service priorities;
- same CTA position changes action commitment;
- same section order changes narrative logic.

Response:

- rebuild semantic map from receiving project source;
- preserve only the abstract lesson if compatible;
- record mismatch in `CROSS-PROJECT TRANSFER FINDINGS`.

---

## 8. Copied-Governance Overreach

**Definition:** governance rules created for one project, version, or risk state are applied elsewhere without authority.

Signals:

- Triumph-specific lessons become universal commands;
- emergency mitigation becomes standard;
- local implementation-pack rule governs unrelated projects;
- prior checklist item creates false blocker where risk is absent;
- a report finding is treated as factory law.

Response:

- classify governance portability level;
- cite parent authority;
- adapt wording or reject transfer;
- keep local/project-specific rules local unless promoted.

---

## 9. Visual-Language Contamination

**Definition:** visual language crosses project boundaries without strategic or identity fit.

Signals:

- copied radius/shadow/card systems;
- imported SaaS mood;
- inherited industrial seriousness where the receiving brand needs softness;
- copied CTA color/shape/pressure;
- hero/proof/footer treatments travel as style defaults.

Response:

- run design intent QA and visual reconciliation QA;
- validate brand/source authority;
- document whether the visual treatment is transferable, adapted, or rejected.

---

## 10. Operational Mismatch Reuse

**Definition:** implementation or workflow pattern is reused despite mismatched operational conditions.

Signals:

- copied SCSS partial structure does not match include graph;
- JS pattern assumes hooks absent in local handoff;
- responsive solution assumes different content density;
- QA standard assumes evidence that does not exist;
- maintenance complexity exceeds project capacity.

Response:

- run implementation reliability QA;
- check stack, build, include ownership, tokens, breakpoints, assets, QA evidence, and maintenance scope;
- adapt or reject before coding.

---

## 11. Project-Identity Erosion

**Definition:** repeated transfer makes a project lose its local meaning, tone, visual language, or strategic posture.

Signals:

- projects begin to share the same CTA pressure, card systems, proof style, and tone without source support;
- local brand language is normalized into generic commercial language;
- project-specific trust markers are replaced by reusable trust widgets;
- visual restraint or visual polish becomes dogma rather than local fit.

Response:

- re-anchor to project-specific sources;
- document local identity signals;
- reject patterns that flatten meaning;
- escalate if identity conflict affects strategic trust.

---

## 12. Triumph V2 Lessons Captured

Triumph V2 illustrates several transfer drift risks:

- V1/V2 contamination is a same-project version example of transfer contamination.
- Foundation defaults can overpower screen-local meaning; cross-project visual transfer can be even more misleading.
- Strategic lessons about operational seriousness and proof hierarchy are useful but not universally portable.
- Implementation reliability lessons should travel as review questions, not as copied code structure.
- Context and provenance findings must survive transfer so future projects know which lessons are evidence-backed and which are cautionary.

These are Website Factory drift lessons, not Triumph implementation instructions.

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Drift risk |
|-----------|------------|
| Source project or artifact is unnamed | Transfer-context blindness, source laundering. |
| Reason for source-project success is unknown | Unsafe pattern reuse, false analogy drift. |
| Local strategy differs or is unclear | Strategic mismatch inheritance. |
| Semantic roles are not mapped locally | Semantic portability failure. |
| Governance authority is unclear | Copied-governance overreach. |
| Template boundaries are unclear | Template contamination. |
| Visual language fit is unproven | Visual-language contamination, project-identity erosion. |
| Operational conditions differ | Operational mismatch reuse, inherited incompatibility. |

**Action:** name the suspected drift pattern, state what evidence is missing, and classify the transfer as compatible, adapted, HITL required, rejected, or blocked.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Transfer Drift Taxonomy - unsafe pattern reuse, false analogy drift, template contamination, strategic mismatch inheritance, copied-governance overreach, cross-project assumption leakage, operational mismatch reuse, and project-identity erosion; documentation only. |
