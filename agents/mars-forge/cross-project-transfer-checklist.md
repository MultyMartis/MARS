# Cross-Project Transfer Checklist - MARS Forge

**Status:** **documented** - Forge overlay checklist for human-supervised cross-project knowledge transfer QA.  
**Not:** autonomous transfer AI, automatic compatibility detection, universal pattern engine, reusable frontend framework, or cross-project governance enforcement.

**Factory governance:** [`../../projects/mars-website-factory/cross-project-transfer-governance.md`](../../projects/mars-website-factory/cross-project-transfer-governance.md).  
**Compatibility model:** [`../../projects/mars-website-factory/knowledge-transfer-compatibility-model.md`](../../projects/mars-website-factory/knowledge-transfer-compatibility-model.md).  
**Drift taxonomy:** [`../../projects/mars-website-factory/transfer-drift-taxonomy.md`](../../projects/mars-website-factory/transfer-drift-taxonomy.md).

---

## 1. When To Run

Run this checklist when a Forge task uses, references, or is influenced by:

- a prior project lesson;
- a Triumph V2 reference lesson;
- a reusable template;
- copied governance language;
- a prior implementation pattern;
- a visual treatment from another project;
- cross-project assumptions about CTA, proof, trust, audience, stack, workflow, QA, or design language;
- a report finding from another project;
- a "standard" whose fit has not been validated for the current project.

Record material results as **CROSS-PROJECT TRANSFER FINDINGS**.

---

## 2. Transfer Source

- [ ] Transfer source is named: project, artifact, report, checklist, implementation, template, or human decision.
- [ ] Source authority is classified: factory principle, layer methodology, project lesson, local project rule, workaround, prior report, or unknown-origin.
- [ ] Original problem solved by the source pattern is stated.
- [ ] Original constraints are visible: strategy, audience, source state, design language, stack, workflow, QA evidence, maintenance capacity.
- [ ] Transfer is treated as candidate knowledge, not current-project authority.
- [ ] Unknown-origin transfer is marked **SAFE UNKNOWN** before it influences implementation, QA, or freeze.

---

## 3. Transfer Compatibility QA

- [ ] Receiving project context is named: audience, offer, source authority, active design/version, implementation stack, workflow state.
- [ ] Problem similarity is validated, not assumed from surface resemblance.
- [ ] Transfer boundaries are visible: reused, adapted, rejected, unknown, escalated.
- [ ] Pattern integrity is preserved: the transferred pattern's purpose and limits remain clear.
- [ ] Compatibility matters more than reuse speed.
- [ ] Transfer does not override project-specific meaning, source authority, or HITL decisions.

Disposition:

```text
TRANSFER COMPATIBILITY: PASS | PARTIAL | FAIL | SAFE UNKNOWN
Reason:
Action:
```

---

## 4. Semantic Portability QA

- [ ] Entity roles survive transfer or are rebuilt from local source.
- [ ] CTA roles are validated locally: commit, qualify, request, learn, compare, defer, or other source-approved role.
- [ ] Proof authority is re-ranked for the receiving project.
- [ ] Section purpose is confirmed locally; same section type is not treated as same meaning.
- [ ] Local terminology, stakeholder language, and project-specific meaning are preserved.
- [ ] Semantic mismatch is documented instead of hidden by similar component shape.

Drift patterns to watch:

- unsafe pattern reuse;
- false analogy drift;
- semantic portability failure;
- cross-project assumption leakage;
- inherited incompatibility.

---

## 5. Strategic-Fit QA

- [ ] Business objective matches or differences are documented.
- [ ] Conversion hierarchy is validated locally.
- [ ] Proof hierarchy and trust posture fit the receiving audience and offer.
- [ ] CTA pressure is appropriate for local operational seriousness.
- [ ] Visual familiarity does not substitute for strategic fit.
- [ ] Local UI polish, engagement, or reusable pattern consistency does not weaken business intent.
- [ ] HITL is triggered when transfer affects business priority, stakeholder intent, proof authority, or conversion path without clear source authority.

Drift patterns to watch:

- strategic mismatch inheritance;
- aesthetic transfer without strategic fit;
- reusable-pattern dogmatism;
- universal-solution thinking.

---

## 6. Operational Compatibility QA

- [ ] Frontend stack, build path, include graph, tokens, breakpoints, and JS hooks can support the pattern.
- [ ] Assets, icons, media, and brand files are approved for the receiving project.
- [ ] Responsive behavior is validated against local content density and hierarchy.
- [ ] QA evidence required by the pattern is available or marked **SAFE UNKNOWN**.
- [ ] Maintenance complexity is appropriate for the receiving project.
- [ ] Transfer does not bypass workflow checkpoints, freeze state, source lineage, or context survivability.

Drift patterns to watch:

- operational mismatch reuse;
- inherited incompatibility;
- inappropriate standard transfer;
- inappropriate frontend cloning.

---

## 7. Governance Portability QA

- [ ] Governance rule scope is identified: factory-wide principle, layer methodology, project-derived lesson, project-specific rule, workaround, or unknown-origin rule.
- [ ] Local/project-specific governance is not copied as universal law.
- [ ] Checklist items are applied only when their risk is in scope.
- [ ] Project-specific implementation-pack rules do not govern another project unless explicitly promoted or adapted.
- [ ] Prior report findings are treated as evidence or lessons, not automatic authority.
- [ ] Copied governance is rewritten when local source, strategy, semantics, or authority differs.

Drift patterns to watch:

- copied-governance overreach;
- template overreach;
- template absolutism;
- copied governance without validation.

---

## 8. Project-Identity QA

- [ ] Transfer preserves local brand voice, visual language, trust model, audience expectation, and operational seriousness.
- [ ] Visual treatments from another project do not contaminate local radius, surface, card, shadow, CTA, density, or proof style.
- [ ] Reuse does not flatten the receiving project into generic Website Factory style.
- [ ] Project-specific meaning remains stronger than template familiarity.
- [ ] If identity fit is ambiguous, record **SAFE UNKNOWN** and escalate before freeze.

Drift patterns to watch:

- visual-language contamination;
- project-identity erosion;
- template contamination;
- project identity flattening.

---

## 9. Incompatibility Escalation QA

Escalate when:

- transfer source cannot be named;
- compatibility evidence is missing;
- local strategy or semantics differ from source project;
- governance authority is local, stale, or unknown;
- visual language may contaminate project identity;
- operational conditions differ materially;
- template boundaries are invisible;
- transfer would influence freeze, CTA role, proof hierarchy, implementation architecture, design language, or PASS claims.

Allowed outcomes:

| Outcome | Meaning |
|---------|---------|
| **Compatible** | Transfer can proceed with traceability. |
| **Adapt with disclosure** | Transfer can proceed after local adaptation is named. |
| **HITL recommended** | Transfer has material uncertainty but may continue with disclosure. |
| **HITL required** | Transfer affects authority, strategy, identity, or freeze. |
| **Reject transfer** | Pattern does not fit this project. |
| **Blocked** | Missing source, authority, or compatibility evidence prevents continuation. |

---

## 10. Transfer Traceability

Add a short traceability note when material transfer occurs:

```text
CROSS-PROJECT TRANSFER FINDINGS - <scope>

Transfer source:
Transfer candidate:
Original problem:
Compatibility read:
- Semantic portability:
- Strategic fit:
- Operational fit:
- Governance portability:
- Project identity:
Disposition: Compatible | Adapt with disclosure | HITL recommended | HITL required | Reject transfer | Blocked
Rejected assumptions:
SAFE UNKNOWN:
Next action:
```

---

## 11. Anti-Patterns

Forbidden drift:

- [ ] Blind pattern reuse.
- [ ] Template absolutism.
- [ ] Cross-project assumption inheritance.
- [ ] Copied governance without validation.
- [ ] Aesthetic transfer without strategic fit.
- [ ] Inappropriate frontend cloning.
- [ ] Project identity flattening.
- [ ] Transfer without compatibility review.
- [ ] Reusable-pattern dogmatism.
- [ ] Universal-solution thinking.

---

## 12. Not Claimed

This checklist does not claim:

- automatic compatibility detection;
- autonomous transfer review;
- universal reusable systems;
- universal frontend standards;
- automatic project-identity protection;
- automatic governance portability;
- implementation transfer safety without human review.

---

## 13. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge cross-project transfer checklist - compatibility QA, semantic portability QA, strategic-fit QA, governance portability QA, incompatibility escalation QA, project-identity QA, and `CROSS-PROJECT TRANSFER FINDINGS`; documentation only. |
