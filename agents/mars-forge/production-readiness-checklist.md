# Production readiness checklist - MARS Forge

**Overlay only.** Run when delivery, handoff, onboarding, maintenance continuity, future edits, deployment assumptions, frozen-build survivability, or post-delivery stability affects the scope.

**Factory methodology:** [`../../projects/mars-website-factory/production-readiness-governance.md`](../../projects/mars-website-factory/production-readiness-governance.md), [`../../projects/mars-website-factory/delivery-survivability-model.md`](../../projects/mars-website-factory/delivery-survivability-model.md), [`../../projects/mars-website-factory/production-drift-taxonomy.md`](../../projects/mars-website-factory/production-drift-taxonomy.md).

**Report as:** `PRODUCTION READINESS FINDINGS`.

---

## 1. Production Readiness QA

- [ ] Delivery claim separates proven facts from assumptions.
- [ ] Canonical source, generated output, and forbidden edit paths are visible.
- [ ] Build and validation evidence are listed or marked **SAFE UNKNOWN**.
- [ ] Known deferrals, waivers, risks, and unresolved unknowns are preserved.
- [ ] Delivery posture is classified: ready, ready with disclosed risk, partial, blocked, HITL required, or SAFE UNKNOWN.

---

## 2. Handoff-Survivability QA

- [ ] Handoff states what was delivered, what changed, what was validated, and what remains unknown.
- [ ] Freeze state, scope, baseline, deferrals, and unfreeze path are readable.
- [ ] Next operator can identify next safe action without private memory.
- [ ] Handoff does not collapse into "files delivered" without state, evidence, and risk.
- [ ] Handoff collapse, handoff opacity, or delivery-traceability loss is recorded when present.

---

## 3. Onboarding-Readability QA

- [ ] A new operator can find project entry points, source of truth, setup expectations, and active design/source paths.
- [ ] Project-specific vocabulary, asset rules, implementation-pack constraints, and known unknowns are findable.
- [ ] Onboarding does not require chat memory, personal recollection, or archaeology through unrelated files.
- [ ] Onboarding fragility or onboarding-hostile architecture is recorded when present.

---

## 4. Maintainability QA

- [ ] Ownership of source files, includes, styles, tokens, assets, breakpoints, and JS hooks is readable enough for maintenance.
- [ ] Local overrides, exceptions, temporary patches, and fragile areas are named or escalated.
- [ ] Maintenance path does not depend on patch stacking, hidden coupling, or undocumented manual steps.
- [ ] Maintainability continuity is preserved across future fixes and delayed edits.
- [ ] Maintenance drift, maintainability neglect, or maintainability collapse is recorded when present.

---

## 5. Future-Edit QA

- [ ] Likely future edits have visible scope and risk boundaries.
- [ ] Frozen or adjacent sections have anti-regression expectations when future edits touch shared selectors, tokens, assets, includes, components, or breakpoints.
- [ ] Structural, source, visual, or business-intent changes have escalation triggers.
- [ ] Future-edit instability or future-edit fragility is recorded when present.

---

## 6. Deployment-Survivability QA

- [ ] Build, assets, environment, hosting, export, rollback, and verification assumptions are separated from proven evidence.
- [ ] No "deployment ready" claim is made from visual polish, build success, or QA pass alone.
- [ ] Missing deployment evidence is reported as **SAFE UNKNOWN**, not inferred readiness.
- [ ] Deployment survivability failure or deployment-without-survivability is recorded when present.

---

## 7. Frozen-Build Survivability QA

- [ ] Freeze state is traceable to evidence, scope, and baseline.
- [ ] Frozen build can be reopened safely through named unfreeze rules.
- [ ] Frozen state remains maintainable and readable, not merely locked.
- [ ] Frozen-build fragility or frozen-build worship is recorded when present.

---

## 8. Lifecycle-Survivability QA

- [ ] Project lifecycle state is readable: build, QA, freeze, delivery, handoff, maintenance, revision, or archive.
- [ ] Post-delivery continuity preserves lessons, risks, ownership, and readiness limits.
- [ ] Long-term frontend stability is not inferred from current PASS, visual polish, or shipment.
- [ ] Operational continuity erosion, lifecycle survivability failure, post-delivery erosion, or long-term frontend decay is recorded when present.

---

## 9. Report Expectations

Record:

- `PRODUCTION READINESS FINDINGS`;
- readiness area: production, handoff, onboarding, maintenance, future-edit, deployment, freeze, lifecycle;
- drift taxonomy term when applicable;
- evidence and proof boundary;
- disposition: PASS, PARTIAL, FAIL, SAFE UNKNOWN, or HITL required;
- resolver or next safe action.

Keep these findings separate from `IMPLEMENTATION RELIABILITY FINDINGS`, `TEMPORAL EVOLUTION FINDINGS`, `WORKFLOW DISCIPLINE FINDINGS`, `GOVERNANCE COMPRESSION FINDINGS`, `RECONSTRUCTION FIDELITY FINDINGS`, and `ORGANIZATIONAL MEMORY FINDINGS`.

---

## 10. Not Claimed

- No autonomous maintenance AI.
- No runtime deployment system.
- No CI/CD implementation.
- No universal production law.
- No perfect maintainability claim.
- No claim that QA pass, visual polish, freeze state, or successful shipment proves production readiness.
