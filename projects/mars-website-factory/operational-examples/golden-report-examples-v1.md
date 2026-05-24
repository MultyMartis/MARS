# Golden REPORT examples v1 (Wave 4)

**Status:** **documented** — canonical **onboarding copies** for REPORT shape. Adapt paths and evidence to your task.  
**Standard:** [reporting-standard-v0.md](../reporting-standard-v0.md).  
**Modes:** [forge-operational-modes-v1.md](../../agents/mars-forge/forge-operational-modes-v1.md).

**Not:** real session logs; **not** evidence of a specific run. Viewport examples (375 / 768 / desktop) are **supplementary generic responsive validation only**. **For RU commercial landings use:** [ru-landing-qa-preset-v1.md](../ru-landing-qa-preset-v1.md).

---

## 1. Forge Lite — token tweak in reference workspace

```markdown
# REPORT — WF reference hero CTA radius tweak

**Mode:** Lite  
**Scope:** `workspaces/website-factory-reference-v1` — visual only, `scss/sections/_hero.scss`

## Created files
- (none)

## Updated files
- workspaces/website-factory-reference-v1/src/scss/sections/_hero.scss

## Artifact changes
- (none — no handoff artifact)

## QA changes
- (none)

## Forge execution
**FOUNDATION FINDINGS:** none — foundations untouched.

## Verification results
- `npm run build` — PASS (operator-run)
- 375px spot-check — PASS, no horizontal scroll

## SAFE UNKNOWN
- CI not run
- Production hosting not verified

## Risks
- None identified for scoped selector change

## Git status
M workspaces/website-factory-reference-v1/src/scss/sections/_hero.scss

## Runtime exclusions
- mars-runtime/*
- governance/* (no expansion)

## Push status
not requested

## Freeze state
frozen: false (Lite — no freeze)
```

---

## 2. Forge Standard — new `pricing` section in client workspace

```markdown
# REPORT — Acme landing pricing block implementation

**Mode:** Standard  
**Scope:** `workspaces/acme-landing-v1` — `block_id: pricing`, page `index`

## Created files
- workspaces/acme-landing-v1/src/partials/sections/pricing.html
- workspaces/acme-landing-v1/src/scss/sections/_pricing.scss

## Updated files
- workspaces/acme-landing-v1/src/pages/index.html
- workspaces/acme-landing-v1/src/scss/main.scss

## Artifact changes
- frontend-handoff-acme-v1 (pricing row marked in-progress → ready for QA)

## QA changes
- (none — findings inline)

## Forge execution
**STRUCTURE FINDINGS:** partial uses `data-section` + `data-block-id="pricing"` — PASS  
**RESPONSIVE FINDINGS:** 375px cards stack; featured tier first — PASS  
**CTA FINDINGS:** featured plan uses `data-modal-open` — PASS  

## Verification results
- `npm run build` — PASS
- Viewport: 375 / 768 / desktop — PASS (operator)

## SAFE UNKNOWN
- Real payment integration not in scope
- WCAG formal audit not run

## Risks
- Pricing copy claims require HITL legal review before production deploy

## Git status
?? workspaces/acme-landing-v1/src/partials/sections/pricing.html
?? workspaces/acme-landing-v1/src/scss/sections/_pricing.scss
 M workspaces/acme-landing-v1/src/pages/index.html
 M workspaces/acme-landing-v1/src/scss/main.scss

## Runtime exclusions
- dist/ (generated)

## Push status
not requested

## Freeze state
frozen: true  
**Files:** pricing.html, _pricing.scss, index.html (include), main.scss (import)
```

---

## 3. Section replacement — hero variant swap

```markdown
# REPORT — Acme hero replacement (survivability)

**Mode:** Standard  
**Scope:** `block_id: hero` — partial swap + regression

## Created files
- workspaces/acme-landing-v1/src/partials/sections/hero-v2.html

## Updated files
- workspaces/acme-landing-v1/src/pages/index.html (include target)

## Unfreeze
- Reason: handoff v2 screen — CTA hierarchy change
- Blast radius: section + adjacent social_proof spacing
- Re-freeze criteria: modal + sticky regression PASS

## Survivability
- `WfLifecycle.destroySection(hero)` before include swap — PASS (operator)
- Post-build: modal from hero CTA — PASS
- Sticky sentinel `#hero-sentinel` present after swap — PASS

## Verification results
- `npm run build` — PASS
- [section-swap-demo-flow-v1.md](../section-swap-demo-flow-v1.md) Demo A equivalent — PASS

## SAFE UNKNOWN
- Automated DOM harness not run

## Risks
- If sentinel id removed, sticky CTA show logic degrades — document in handoff

## Git status
(changes as per operator)

## Push status
not requested

## Freeze state
frozen: true (re-freeze after replacement)
```

---

## 4. Freeze / unfreeze — lead form defect fix

```markdown
# REPORT — Acme lead_form unfreeze (validation bug)

**Mode:** Critical (frozen section + form behavior)  
**Scope:** `block_id: lead_form`

## Unfreeze record
- **Reason:** phone field validation message not clearing on blur
- **Blast radius:** section local — `form.js` untouched
- **Prior freeze:** 2026-05-18 REPORT — lead_form frozen

## Updated files
- workspaces/acme-landing-v1/src/partials/sections/lead_form.html
- workspaces/acme-landing-v1/src/scss/sections/_lead_form.scss

## Forge execution
**STATE CONSISTENCY FINDINGS:** error state clears on valid input — PASS after fix

## Verification results
- `npm run build` — PASS
- Form submit once after re-init — PASS
- Modal unrelated — spot-check PASS

## SAFE UNKNOWN
- Backend endpoint not tested

## Risks
- None for scoped fix

## Git status
(M operator)

## Push status
not requested

## Freeze state
frozen: true (re-freeze same day)
**Re-freeze criteria met:** validation + single-submit verified
```

---

## Usage

Copy the closest example; replace workspace slug, file paths, and PASS/FAIL with **honest** evidence. Do not mark PASS without build or viewport check performed.

*Wave 4 — golden REPORT examples.*
