# MARS Website Factory — QA Drift Taxonomy

**Status:** **documented** — Website Factory QA confidence drift vocabulary for human-supervised reporting only.  
**Not:** automated QA detection, scoring engine, test runner, real-device certification, or universal QA ontology.

**Parent layer:** [qa-confidence-governance.md](qa-confidence-governance.md).  
**Evidence model:** [verification-evidence-model.md](verification-evidence-model.md).  
**Forge checklist:** [`../../agents/mars-forge/qa-confidence-checklist.md`](../../agents/mars-forge/qa-confidence-checklist.md).

---

## 1. Purpose

This taxonomy names QA reporting drift: situations where the report sounds more certain, complete, or verified than the evidence supports.

Use it to record **QA CONFIDENCE FINDINGS** when confidence, evidence, scope, or unknowns are misaligned.

---

## 2. Drift Patterns

| Pattern | Definition | Governance response |
|---------|------------|---------------------|
| **Fake PASS inflation** | PASS is claimed without evidence or beyond the checked scope. | Downgrade to scoped PASS, PARTIAL, SAFE UNKNOWN, or FAIL. |
| **Screenshot certainty drift** | Screenshot/visual review is treated as proof of layout, interaction, state, responsive, or accessibility correctness. | Label as rendered/visual evidence only; disclose unverified states. |
| **Inferred responsiveness** | Responsive behavior is claimed from desktop source, CSS review, or one viewport without observed breakpoint evidence. | Scope widths checked; mark others SAFE UNKNOWN. |
| **Unverifiable pixel claims** | Pixel-perfect, exact spacing, exact parity, or objective visual match is claimed without measurement authority or approved method. | Replace with qualitative visual reconciliation or source-level note. |
| **Hidden QA gaps** | Known unrun checks, unavailable previews, missing source, or untested states are omitted. | Add explicit gaps and disposition. |
| **Evidence collapse** | Different evidence levels are blended into one generic “verified” claim. | Split by evidence level using [verification-evidence-model.md](verification-evidence-model.md). |
| **QA theater** | Report language performs certainty without readable evidence, scope, or action. | Rewrite into evidence, boundary, unknowns, and next action. |
| **Confidence escalation** | Weak evidence is promoted to high confidence through wording or repetition. | Re-anchor confidence to actual evidence. |
| **Fake completeness** | A subset of checks is presented as all required QA. | Mark partial validation and list missing check families. |
| **Weak evidence reporting** | Evidence is vague: “checked,” “looks fine,” “should work,” or “probably OK.” | Name the check, source, viewport, command, or direct interaction. |
| **Build-success illusion** | Successful build is treated as frontend correctness. | Limit to build-level evidence; require rendered/direct checks for broader claims. |
| **Partial-check overreach** | One section, viewport, state, or browser result is generalized to full page/system. | Scope PASS to the observed slice. |
| **Undocumented assumptions** | Practical assumptions influence QA outcome but are not disclosed. | Move assumption into ASSUMED / SAFE UNKNOWN with resolver. |
| **Interaction pretense** | Click, hover, focus, form, modal, carousel, or state behavior is claimed without exercising behavior. | Downgrade to source-level or unknown until directly checked. |
| **Fabricated device QA** | Real device, browser matrix, or cross-browser confidence is implied without running it. | Remove claim; list device/browser coverage as SAFE UNKNOWN. |
| **Accessibility certification drift** | Accessibility intent review or simple checks are reported as full compliance/certification. | Scope to observed accessibility evidence; disclose audit limits. |
| **Confidence contamination** | Confidence from one lane, such as source review or build, leaks into another lane, such as rendered UI or interactions. | Separate lanes and evidence levels. |

---

## 3. Severity Guide

| Severity | Description | Typical action |
|----------|-------------|----------------|
| **Low** | Wording is imprecise but evidence and scope are mostly recoverable. | Rewrite report language. |
| **Medium** | A PASS or PARTIAL claim overstates scope or hides material unknowns. | Downgrade disposition and add gaps. |
| **High** | QA claim could authorize freeze/delivery despite missing material evidence. | Stop freeze, require verification or HITL. |
| **Blocking** | Report fabricates tests, devices, interactions, source authority, or universal correctness. | STOP; correct report; rerun or disclose checks. |

---

## 4. Required Detection Prompts

Ask before accepting a QA disposition:

- Is every PASS scoped to the evidence that supports it?
- Was the rendered UI actually inspected, or only source/build reviewed?
- Were interactions exercised, or only inferred from code/source?
- Were viewport claims checked at named widths?
- Are device/browser claims based on real runs or assumptions?
- Are accessibility claims scoped to what was actually evaluated?
- Does the report show what remains unknown?
- Does any phrase imply “everything passed” when only partial checks ran?
- Is SAFE UNKNOWN used where evidence is missing?

---

## 5. Forbidden QA Language

Avoid or qualify:

- `PASS everywhere`
- `fully verified`
- `all good`
- `works on mobile` without named widths/devices
- `interactions work` without exercised flows
- `accessible` without scoped accessibility evidence
- `pixel-perfect` without an approved measurement method
- `tested on devices` without named device evidence
- `no issues` when checks were partial
- `probably`, `should`, `seems` as a substitute for evidence

Acceptable replacements:

- `PASS — build-level verified only`
- `PARTIAL — rendered at 1440px and 375px; interaction states unknown`
- `SAFE UNKNOWN — tablet behavior not observed`
- `PASS — source-level semantic review; rendered verification pending`

---

## 6. Triumph V2 Lessons Captured

Triumph V2 exposed reusable QA drift risks:

- Multi-layer frontend governance can still collapse into fake completeness if the final report summarizes partial checks as universal PASS.
- Screenshot-heavy design validation can overstate certainty for interaction, state, accessibility, and responsive behavior.
- Build success and static source review are valuable but cannot prove rendered commercial fidelity.
- Mobile, hover, focus, form, and assistive behavior are easy to leave implicit unless the report forces evidence boundaries.
- Confidence contamination can happen when successful semantic, visual, or reliability findings make unrelated unverified lanes feel “done.”

These are Website Factory QA governance lessons, not Triumph-specific QA results.

---

## 7. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial QA drift taxonomy — fake PASS inflation, screenshot certainty drift, QA theater, confidence escalation, evidence collapse, build-success illusion, and related reporting drift patterns. |
