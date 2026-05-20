# MARS Website Factory - Knowledge Transfer Compatibility Model

**Status:** **documented** - compatibility model for human-supervised cross-project knowledge transfer.  
**Not:** compatibility engine, automated classifier, universal transfer graph, project scoring system, or reusable frontend framework.

**Parent governance:** [cross-project-transfer-governance.md](cross-project-transfer-governance.md).  
**Companion taxonomy:** [transfer-drift-taxonomy.md](transfer-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/cross-project-transfer-checklist.md`](../../agents/mars-forge/cross-project-transfer-checklist.md).

---

## 1. Purpose

The Knowledge Transfer Compatibility Model defines what must be true before lessons, patterns, governance rules, implementation approaches, visual treatments, or templates from one project influence another project.

It separates:

- what can transfer directly;
- what can transfer only after adaptation;
- what must remain project-specific;
- what requires human review;
- what must be rejected because it creates mismatch, contamination, or project-identity erosion.

The model is a readability and escalation tool. It does not detect compatibility automatically.

---

## 2. Compatibility Layers

| Layer | Primary question | Transfer posture |
|-------|------------------|------------------|
| **Transferable patterns** | What lesson or pattern is being considered, and what problem did it solve in the source project? | Candidate only; not authority. |
| **Project-specific semantics** | Does meaning survive transfer: entities, CTA roles, proof authority, section purpose, stakeholder language? | Block direct reuse when meaning differs. |
| **Strategic compatibility layer** | Does the pattern preserve business objective, conversion hierarchy, trust model, operational seriousness, and audience fit? | Requires validation before use. |
| **Operational compatibility layer** | Can the receiving project support the pattern with its stack, workflow, assets, QA evidence, maintenance capacity, and source state? | Adapt or reject if conditions differ. |
| **Governance portability layer** | Does the source rule have authority outside its original project, or is it local/temporary/source-specific? | Port only with scope and authority. |
| **Escalation/review layer** | What ambiguity, contradiction, or authority gap requires HITL or explicit review? | Escalate before implementation authority. |
| **Incompatibility boundary layer** | What signs mean the transfer should stop, be rejected, or be rewritten as a local solution? | Protects project identity and governance integrity. |

---

## 3. Transfer Candidates

Transferable candidates may include:

- governance lessons;
- QA questions;
- frontend implementation patterns;
- visual reconciliation findings;
- design-system intent observations;
- CTA/proof hierarchy lessons;
- source lineage practices;
- context survivability practices;
- workflow discipline;
- naming conventions;
- report structures;
- project artifact templates.

Each candidate should be treated as **candidate knowledge**, not as current-project authority.

---

## 4. Transfer Boundary Fields

Every material transfer should identify:

| Field | Required read |
|-------|---------------|
| **Source project** | Which project produced the lesson or pattern. |
| **Source artifact** | Which file, report, checklist, implementation, design, or decision introduced it. |
| **Original problem** | What issue the pattern solved in the source project. |
| **Original constraints** | What stack, source authority, brand tone, governance maturity, or timeline shaped it. |
| **Receiving project fit** | Why the current project can safely use it. |
| **Adaptation required** | What must change for local strategy, semantics, visuals, operations, or governance. |
| **Rejected elements** | What should not transfer. |
| **Escalation state** | Compatible, adapt with disclosure, HITL recommended, HITL required, reject, or blocked. |
| **Traceability note** | How future operators can see what transferred and why. |

---

## 5. Compatibility Validation

Before reuse, validate:

1. **Source validity** - the transfer source is named, current enough, and not unknown-origin.
2. **Problem similarity** - the source problem and receiving problem are actually comparable.
3. **Semantic portability** - meaning survives across entities, CTA roles, proof roles, and section purpose.
4. **Strategic fit** - business priority, conversion path, trust posture, and audience expectations align.
5. **Operational fit** - stack, assets, workflow, QA, evidence, and maintenance conditions support the transfer.
6. **Governance authority** - the rule can travel or has been adapted with explicit scope.
7. **Identity preservation** - brand, tone, visual language, and project-specific meaning remain intact.
8. **Escalation threshold** - unresolved mismatch is visible and routed before implementation authority.

Validation is qualitative and human-supervised. It is not scoring, linting, or automatic pattern matching.

---

## 6. Semantic Mismatch Handling

Semantic mismatch occurs when the transferred pattern uses the same shape but carries different meaning.

| Mismatch | Handling |
|----------|----------|
| Same section type, different strategic role | Reclassify locally; do not inherit source-project hierarchy. |
| Same CTA label, different action commitment | Validate CTA role and conversion pressure before reuse. |
| Same proof component, different authority | Re-rank proof hierarchy for local trust model. |
| Same visual card pattern, different entity meaning | Adapt grouping, labels, density, and hierarchy. |
| Same service grid, different audience decision path | Rebuild semantic order from local source. |
| Same testimonial/review treatment, different trust posture | Validate authority, placement, and visual weight. |

**Rule:** semantic mismatch does not forbid learning. It forbids blind transfer.

---

## 7. Strategic Fit Validation

Strategic compatibility requires more than structural similarity.

Ask:

- Does the source-project pattern solve the same business problem?
- Does the receiving project have the same conversion objective?
- Does the same proof hierarchy increase trust here, or does it distort trust?
- Does the visual language support the receiving project's operational seriousness?
- Does copied CTA pressure match the receiving audience's decision readiness?
- Does the pattern preserve stakeholder intent, or replace it with precedent?
- Would reuse flatten the receiving project into a generic Website Factory style?

If strategic fit cannot be proven, record **SAFE UNKNOWN** and route to HITL when the transfer affects business meaning.

---

## 8. Operational Compatibility Layer

Operational fit must be checked before implementation patterns travel.

| Operational dimension | Risk if ignored |
|-----------------------|-----------------|
| **Frontend stack** | Pattern assumes different build, SCSS, JS, component, or include behavior. |
| **Asset authority** | Assets, icons, images, or brand files are copied without local approval. |
| **Token model** | Source tokens imply visual language the receiving project does not use. |
| **Responsive constraints** | Breakpoint behavior transfers without local content/density validation. |
| **QA capacity** | Pattern requires checks the receiving project cannot evidence. |
| **Maintenance capacity** | Complex pattern becomes fragile in a smaller or less governed project. |
| **Source maturity** | Pattern assumes stable source when receiving project is ambiguous or evolving. |
| **Workflow state** | Reuse bypasses local checkpoints, freeze state, or escalation memory. |

Operational mismatch can make a strategically good idea unsafe to implement.

---

## 9. Governance Portability Layer

Governance rules have different portability levels:

| Portability level | Meaning | Example posture |
|-------------------|---------|-----------------|
| **Factory-wide principle** | May guide many projects, still applied through local evidence. | "Compatibility matters more than reuse." |
| **Layer methodology** | Applies when the risk is in scope. | Source lineage, context survivability, strategic intent QA. |
| **Project-derived lesson** | Travels as a question or caution, not a command. | Triumph V2 lessons. |
| **Project-specific rule** | Must not transfer unless promoted or adapted. | A V2 implementation-pack constraint. |
| **Temporary workaround** | Usually should not transfer. | Emergency CSS patch or one-off report deferral. |
| **Unknown-origin rule** | Cannot govern transfer until provenance is restored. | Uncited prior note or summary claim. |

Governance portability should be documented in `CROSS-PROJECT TRANSFER FINDINGS` when material.

---

## 10. Escalation Rules

Escalate when:

- source-project context cannot be named;
- pattern success reason is unclear;
- local strategy differs from source strategy;
- semantic roles look similar but carry different meaning;
- project identity may be flattened;
- governance authority is local or unknown;
- operational requirements differ materially;
- template boundaries are invisible;
- transfer would influence freeze, CTA role, proof authority, design language, implementation architecture, or report PASS.

Escalation outcomes:

| Outcome | Meaning |
|---------|---------|
| **Compatible** | Transfer can proceed with traceability. |
| **Adapt with disclosure** | Transfer may proceed after local adaptation is named. |
| **HITL recommended** | Transfer is possible, but material uncertainty remains. |
| **HITL required** | Transfer affects authority, strategy, identity, or freeze state. |
| **Reject transfer** | The pattern is not compatible with this project. |
| **Blocked** | Missing source, authority, or compatibility evidence prevents continuation. |

---

## 11. Transfer Traceability

Future operators should be able to read:

- what was transferred;
- from which project and artifact;
- why it seemed relevant;
- what compatibility checks passed;
- what adaptations were made;
- what assumptions were rejected;
- what mismatch remained;
- what escalation outcome governed the decision.

Traceability prevents transfer from becoming hidden context, summary contamination, or project mythology.

---

## 12. Triumph V2 Lessons Captured

Triumph V2 contributes transfer lessons as compatibility prompts:

- V2's semantic rebuild discipline can inform future projects, but the exact section meaning, proof hierarchy, and industrial tone are local.
- V2's visual restraint lessons should not become universal anti-SaaS law for projects that explicitly charter another language.
- V2's provenance and context survivability lessons show why prior reports need lineage before becoming reusable knowledge.
- V2's implementation reliability lessons are transferable as stability questions, not as mandatory code architecture.
- V2's contamination risks demonstrate that even same-project version transfer can drift; cross-project transfer must be stricter.

These lessons are reference knowledge, not direct implementation instructions.

---

## 13. SAFE UNKNOWN

Record **SAFE UNKNOWN** when:

| Situation | Why it is unknown |
|-----------|-------------------|
| Transfer candidate lacks source artifact | Cannot prove origin, authority, or original problem. |
| Original constraints are missing | Cannot know why the pattern worked. |
| Receiving project context is incomplete | Cannot validate fit. |
| Semantic roles may differ | Cannot claim portability of meaning. |
| Strategic fit cannot be proven | Cannot safely inherit CTA, proof, trust, or tone. |
| Operational conditions differ | Cannot safely reuse implementation or workflow assumptions. |
| Governance portability is unclear | Cannot know whether the rule is factory-wide or local. |
| Escalation owner is absent | Cannot resolve compatibility boundary. |

**Action:** document the missing compatibility layer, safest continuation posture, and what evidence or human decision would resolve it.

---

## 14. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Knowledge Transfer Compatibility Model - transfer boundaries, compatibility validation, semantic mismatch handling, strategic fit validation, escalation rules, and transfer traceability; documentation only. |
