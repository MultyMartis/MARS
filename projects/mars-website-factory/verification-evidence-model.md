# MARS Website Factory — Verification Evidence Model

**Status:** **documented** — Website Factory evidence vocabulary for human-supervised QA reporting only.  
**Not:** automated verification runtime, CI system, device lab, screenshot diff engine, or universal proof model.

**Parent layer:** [qa-confidence-governance.md](qa-confidence-governance.md).  
**Drift companion:** [qa-drift-taxonomy.md](qa-drift-taxonomy.md).  
**Forge checklist:** [`../../agents/mars-forge/qa-confidence-checklist.md`](../../agents/mars-forge/qa-confidence-checklist.md).

---

## 1. Purpose

The Verification Evidence Model gives Website Factory operators a shared language for declaring how a QA claim was supported.

It prevents:

- fake PASS states;
- evidence collapse;
- screenshot-only certainty;
- build-success illusion;
- inferred validation presented as direct verification;
- partial checks inflated into universal QA confidence.

---

## 2. Evidence Levels

| Level | Meaning | Reporting posture |
|-------|---------|-------------------|
| **Directly verified** | The behavior, state, flow, or output was actively checked in the relevant environment/scope. | Strongest scoped confidence; still name scope and environment. |
| **Rendered verified** | The UI was visually inspected in a rendered page/preview for named viewport/state. | Supports visual/layout claims for observed scope only. |
| **Source-level verified** | Code, markup, styles, scripts, configuration, or documentation were reviewed without rendered/runtime confirmation. | Supports implementation/source claims, not rendered or behavioral proof. |
| **Build-level verified** | A build/check command completed or failed with observed output. | Supports toolchain status only; not frontend correctness. |
| **Inferred** | Conclusion is derived from related evidence, pattern, source logic, or prior checks but was not directly verified. | Must be labeled; cannot support unqualified PASS. |
| **Assumed** | Practical assumption used because evidence is incomplete. | Must be disclosed, bounded, and reversible; often PARTIAL or SAFE UNKNOWN. |
| **Unknown** | Evidence is absent, contradictory, unavailable, or outside scope. | Use SAFE UNKNOWN, HITL, STOP, or scoped deferral. |

---

## 3. Evidence Boundaries

Evidence must stay inside its proof boundary:

- **Direct interaction evidence** does not prove every browser, device, role, or hidden state.
- **Rendered evidence** does not prove unobserved interactions, keyboard behavior, assistive output, or future regression survivability.
- **Source-level evidence** does not prove computed layout, actual browser behavior, or visual parity.
- **Build-level evidence** does not prove design correctness, accessibility correctness, interaction correctness, or responsive intent.
- **Inferred evidence** does not become direct verification because it is plausible.
- **Assumed evidence** is not evidence; it is an implementation/reporting risk.
- **Unknown** should remain visible until resolved.

---

## 4. Confidence Escalation Rules

Confidence may escalate only when stronger evidence is added.

| From | Can escalate to | Required evidence |
|------|-----------------|-------------------|
| Unknown | Assumed / inferred / source-level / build-level / rendered / direct | Name the new source, check, preview, command, or observed behavior. |
| Assumed | Inferred or verified level | Replace assumption with source, rendered, build, or direct evidence. |
| Inferred | Source-level / rendered / direct | Perform the relevant review or check. |
| Build-level | Rendered or direct | Inspect rendered output or exercise behavior; build alone cannot escalate. |
| Source-level | Rendered or direct | Preview/render or execute the behavior. |
| Rendered | Directly verified | Exercise interaction/state/flow, not only observe pixels. |

**Rule:** confidence cannot escalate through wording. It escalates only through evidence.

---

## 5. PASS Qualification

PASS claims must include:

- **scope** — section, page, file set, viewport, state, flow, command, or source artifact;
- **evidence level** — directly verified, rendered verified, source-level verified, build-level verified, inferred, assumed, or unknown;
- **boundary** — what the evidence does not cover;
- **unknowns** — material gaps, if any;
- **disposition** — PASS, PARTIAL, FAIL, SAFE UNKNOWN, HITL REQUIRED, or STOP.

Examples:

```text
PASS — build-level verified
Scope: `npm run build`
Boundary: rendered layout, interactions, accessibility, and device behavior not verified.
```

```text
PARTIAL — rendered verified
Scope: hero section at 1440px and 375px.
Boundary: tablet, hover/focus states, form behavior, and real device behavior remain SAFE UNKNOWN.
```

```text
SAFE UNKNOWN — interaction validation
Scope: CTA hover/focus/loading state.
Boundary: source does not define state and behavior was not exercised.
Resolver: source state notes, direct preview interaction, or HITL.
```

---

## 6. Verification Traceability

A traceable QA claim should answer:

1. What was checked?
2. Where was it checked?
3. How was it checked?
4. What evidence level supports it?
5. What remains unverified?
6. Did any inference or assumption affect the conclusion?
7. Does the disposition match the evidence?

If an operator cannot answer those questions from the REPORT, the QA record is not sufficiently readable.

---

## 7. SAFE UNKNOWN Disclosure

Use **SAFE UNKNOWN** when a claim depends on evidence that is missing, unavailable, contradictory, or outside scope.

Required disclosure format:

```text
SAFE UNKNOWN — <topic>
Scope:
Missing evidence:
Why it matters:
Potential resolver:
Current disposition: proceed with disclosed partial | defer | HITL required | STOP
```

SAFE UNKNOWN is not a failure of QA. It is a guardrail against false certainty.

---

## 8. Relationship to Adjacent Layers

| Layer | Evidence model role |
|-------|---------------------|
| [Source Interpretation Governance](source-interpretation-governance.md) | Separates observed, inferred, assumed, unknown source reads before confidence is claimed. |
| [Visual Reconciliation Layer](visual-reconciliation-layer.md) | Uses rendered/source evidence for qualitative visual intent; cannot claim interaction proof. |
| [Implementation Reliability Governance](implementation-reliability-governance.md) | Distinguishes source/rebuild/reliability evidence from current visual appearance. |
| [Accessibility Intent Governance](accessibility-intent-governance.md) | Requires evidence boundaries for focus, keyboard, labels, contrast, and assistive predictability. |
| [Responsive Intent Governance](responsive-intent-governance.md) | Keeps viewport evidence scoped; unobserved widths/devices remain unknown. |

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial verification evidence levels, confidence escalation, PASS qualification, SAFE UNKNOWN disclosure, and traceability model. |
