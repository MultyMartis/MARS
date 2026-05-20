# MARS Website Factory - Production Drift Taxonomy

**Status:** **documented** - drift vocabulary for human-supervised production-readiness and delivery-survivability review.  
**Not:** automated drift detection, production monitoring, deployment scanner, runtime reliability engine, or universal maintainability law.

**Parent governance:** [production-readiness-governance.md](production-readiness-governance.md).  
**Model:** [delivery-survivability-model.md](delivery-survivability-model.md).  
**Forge checklist:** [`../../agents/mars-forge/production-readiness-checklist.md`](../../agents/mars-forge/production-readiness-checklist.md).

---

## 1. Purpose

This taxonomy names production-survivability drift: frontend projects that look complete, pass QA, or ship successfully while becoming fragile after delivery, handoff, onboarding, maintenance, future edits, deployment packaging, or long-term operation.

It is used to report `PRODUCTION READINESS FINDINGS`. It does not detect drift automatically.

---

## 2. Drift Patterns

| Drift pattern | Definition | Common signal |
|---------------|------------|---------------|
| **Handoff collapse** | Delivery output cannot be safely continued because state, evidence, ownership, or next action is missing. | "Here are the files" without source, risk, freeze, validation, or resolver notes. |
| **Onboarding fragility** | A new operator cannot understand the project without private memory or long archaeology. | Setup, source authority, build path, asset rules, or known unknowns are not readable. |
| **Maintenance drift** | Maintenance work gradually accumulates hidden patches, unclear ownership, and source divergence. | Small fixes keep adding exceptions instead of preserving structure. |
| **Post-delivery erosion** | Trust and quality degrade after launch, archive, transfer, or delayed future work. | Delivery report disappears from active context; known risks are forgotten. |
| **Future-edit instability** | Predictable later edits create hidden regressions or unsafe coupling. | Content, asset, CTA, responsive, or token changes require risky global guessing. |
| **Deployment survivability failure** | Delivery assumes build, assets, hosting, environment, verification, or rollback readiness without evidence. | "Ready to deploy" is claimed without documented deployment assumptions and limits. |
| **Delivery-readiness illusion** | Visual polish, QA pass, or shipped state is mistaken for operational readiness. | "It looks done" replaces handoff, onboarding, maintenance, and lifecycle review. |
| **Frozen-build fragility** | Freeze state exists but cannot be maintained, reopened, or traced safely. | Frozen scope lacks baseline, evidence, deferrals, or unfreeze path. |
| **Maintainability collapse** | Source becomes too opaque or coupled for reliable future maintenance. | Future fixes require rewriting, guessing, or touching unrelated areas. |
| **Long-term frontend decay** | Frontend stability weakens across time, operators, or revisions. | Repeated updates reduce readability, source authority, and operational trust. |
| **Operational continuity erosion** | Delivery loses checkpoint, report, evidence, lesson, or ownership continuity. | Future sessions cannot reconstruct what was ready, partial, risky, or unknown. |
| **Lifecycle survivability failure** | Project cannot move safely through build, QA, freeze, delivery, maintenance, and revision states. | Lifecycle state is treated as a single "done" condition. |
| **Delivery-traceability loss** | Future operators cannot tell why readiness was claimed or what evidence supported it. | Readiness verdict exists without source-to-evidence chain. |

---

## 3. Severity Read

| Severity | Meaning |
|----------|---------|
| **Critical** | Delivery, handoff, maintenance, or deployment trust is unsafe without HITL or blocking review. |
| **High** | Future edits, onboarding, or freeze survivability are materially fragile. |
| **Medium** | Readiness is partial; risks are visible but require follow-up before strong delivery claims. |
| **Low** | Minor survivability gaps exist but do not block scoped continuation when disclosed. |
| **SAFE UNKNOWN** | Evidence is insufficient to classify readiness or drift. |

Severity should reflect delivery consequence, not report volume.

---

## 4. Drift Differentiation

| Nearby layer | Difference |
|--------------|------------|
| **Implementation reliability** | Focuses on source stability and safe modification; production drift asks whether the delivered project survives ownership and operation after delivery. |
| **Temporal evolution** | Focuses on continuity over time; production drift asks whether delivery state can enter that long-term lifecycle safely. |
| **Operational workflow** | Focuses on execution traceability; production drift asks whether the final handoff and post-delivery state remain survivable. |
| **Context survivability** | Focuses on memory/compression; production drift asks whether delivery-readiness evidence survives beyond the active session. |
| **Organizational memory** | Focuses on reusable lessons; production drift asks whether delivery output carries enough lessons and state to prevent future collapse. |
| **Governance compression** | Focuses on deployable governance density; production drift asks whether delivery readiness was compressed without hiding material survivability risks. |

---

## 5. Reporting Language

Use this taxonomy in `PRODUCTION READINESS FINDINGS`:

```text
PRODUCTION READINESS FINDINGS - <scope>

Readiness area: handoff | onboarding | maintenance | future-edit | deployment | freeze | lifecycle
Drift pattern: <taxonomy term>
Evidence: <what was observed or not observed>
Risk: <delivery / maintenance / future-edit consequence>
Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL required
Resolver: <artifact, evidence, owner, or decision needed>
```

---

## 6. Anti-Pattern Vocabulary

These anti-patterns should be named directly when observed:

- **Delivery-and-forget culture**
- **Frozen-build worship**
- **Handoff opacity**
- **Onboarding-hostile architecture**
- **Future-edit fragility**
- **Maintainability neglect**
- **Post-delivery abandonment**
- **Deployment-without-survivability**
- **Lifecycle blindness**
- **"It shipped therefore finished"**

---

## 7. SAFE UNKNOWN

Use **SAFE UNKNOWN** when:

- handoff evidence is missing;
- onboarding path cannot be proven;
- maintenance ownership is unclear;
- future-edit safety is unreviewed;
- deployment assumptions are undocumented;
- freeze state lacks reopen or traceability evidence;
- delivery-readiness claim lacks proof boundary;
- long-term operational continuity cannot be reconstructed.

**Rule:** do not convert missing production-readiness evidence into confidence language.

---

## 8. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Production Drift Taxonomy - handoff collapse, onboarding fragility, maintenance drift, post-delivery erosion, future-edit instability, deployment survivability failure, delivery-readiness illusion, frozen-build fragility, maintainability collapse, long-term frontend decay, operational continuity erosion, lifecycle survivability failure, and delivery-traceability loss; documentation only. |
