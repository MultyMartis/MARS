# QA confidence checklist — MARS Forge

**Status:** Forge overlay checklist for **human-supervised** QA confidence and verification transparency.  
**Not:** automated QA engine, device lab, screenshot diff, runtime verification system, autonomous approval, or substitute for foundation QA.

**Website Factory layers:**

- [QA Confidence & Verification Governance](../../projects/mars-website-factory/qa-confidence-governance.md)
- [Verification Evidence Model](../../projects/mars-website-factory/verification-evidence-model.md)
- [QA Drift Taxonomy](../../projects/mars-website-factory/qa-drift-taxonomy.md)

Run this checklist before declaring section PASS, PARTIAL, FAIL, SAFE UNKNOWN, or freeze when Forge QA is in scope.

---

## 1. Scope and Evidence Anchor

- [ ] QA scope is named: page, section, `block_id`, file set, viewport, state, flow, command, or source artifact.
- [ ] Evidence level is labeled for material claims: directly verified, rendered verified, source-level verified, build-level verified, inferred, assumed, or unknown.
- [ ] Evidence paths, commands, source artifacts, preview notes, or manual observations are readable enough for a future operator.
- [ ] PASS/PARTIAL/FAIL/SAFE UNKNOWN disposition matches evidence.
- [ ] No claim is broader than the checked scope.

---

## 2. Evidence-Level QA

- [ ] **Directly verified** claims name the flow/state/environment actually exercised.
- [ ] **Rendered verified** claims name viewport/state and do not imply interaction proof.
- [ ] **Source-level verified** claims do not imply rendered correctness.
- [ ] **Build-level verified** claims do not imply frontend correctness.
- [ ] **Inferred** claims are explicitly labeled and not reported as verified.
- [ ] **Assumed** claims are disclosed, bounded, and reversible.
- [ ] **Unknown** items are reported as SAFE UNKNOWN, HITL REQUIRED, STOP, or scoped deferral.

---

## 3. PASS Qualification QA

- [ ] PASS claims include scope and evidence level.
- [ ] Universal PASS language is absent unless full scope evidence exists.
- [ ] Partial validation is reported as PARTIAL, not upgraded to PASS.
- [ ] Build success is reported only as build-level evidence.
- [ ] Screenshot/visual inspection is not used as interaction, state, accessibility, or device proof.
- [ ] Source-level review is not used as rendered verification.
- [ ] Responsive claims name observed widths/devices or disclose SAFE UNKNOWN.
- [ ] Accessibility claims remain scoped and do not imply certification.

---

## 4. Verification Transparency QA

- [ ] Report states what was checked.
- [ ] Report states what was not checked when material.
- [ ] Report states how evidence was obtained.
- [ ] Report states confidence boundaries and proof boundaries.
- [ ] Report keeps source interpretation, visual reconciliation, implementation reliability, responsive intent, interaction/state/accessibility, and foundation QA findings distinguishable.
- [ ] Hidden uncertainty is surfaced before freeze.
- [ ] SAFE UNKNOWN is used instead of fake certainty.

---

## 5. Drift Taxonomy QA

Check for patterns from [qa-drift-taxonomy.md](../../projects/mars-website-factory/qa-drift-taxonomy.md):

- [ ] Fake PASS inflation.
- [ ] Screenshot certainty drift.
- [ ] Inferred responsiveness.
- [ ] Unverifiable pixel claims.
- [ ] Hidden QA gaps.
- [ ] Evidence collapse.
- [ ] QA theater.
- [ ] Confidence escalation.
- [ ] Fake completeness.
- [ ] Weak evidence reporting.
- [ ] Build-success illusion.
- [ ] Partial-check overreach.
- [ ] Undocumented assumptions.
- [ ] Interaction pretense.
- [ ] Fabricated device QA.
- [ ] Accessibility certification drift.
- [ ] Confidence contamination.

Any material match requires **QA CONFIDENCE FINDINGS**.

---

## 6. Escalation Boundary

Stop or escalate when a report would:

- claim PASS without named evidence;
- claim full QA from partial checks;
- claim rendered, interaction, accessibility, responsive, device, or browser proof without verification;
- hide missing source, preview, build output, interaction state, breakpoint, or keyboard/focus evidence;
- fabricate test/device/browser coverage;
- use screenshot review as universal correctness proof;
- authorize freeze while material QA uncertainty is hidden.

Use **PARTIAL — QA confidence**, **SAFE UNKNOWN**, **HITL required**, or **STOP** rather than QA theater.

---

## 7. REPORT Block

Use this block when QA confidence affects the result:

```text
QA CONFIDENCE FINDINGS — <section or block_id> — <source/ref>

Scope:
- <what the QA claim covers>

Evidence levels:
- Directly verified:
- Rendered verified:
- Source-level verified:
- Build-level verified:
- Inferred:
- Assumed:
- Unknown:

PASS qualification:
- Disposition: PASS | PARTIAL | FAIL | SAFE UNKNOWN | HITL REQUIRED | STOP
- Proof boundary:
- Unverified but material:

QA drift taxonomy:
- Patterns:
- Severity:

Confidence statement:
- Confidence: high scoped | medium scoped | low | unsafe to claim
- Why confidence matches evidence:

Action:
- proceed | verify further | disclose partial | defer | HITL required | stop freeze
Evidence:
- <paths, commands, preview notes, observations>
```

---

## 8. Not Claimed

- No automatic QA confidence detection.
- No autonomous verification engine.
- No fake device/browser/testing coverage.
- No replacement for project-specific QA, foundation QA, HITL, or specialist audits.
- No universal QA truth or delivery certification.

Defer to Website Factory governance layers, project implementation packs, foundation QA, and HITL decisions where scoped.

---

## 9. Changelog

| Version | Date | Notes |
|---------|------|-------|
| v0 | 2026-05-17 | Initial Forge QA confidence checklist; adds `QA CONFIDENCE FINDINGS` and evidence-level PASS discipline. |
