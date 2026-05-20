# Adoption validation flow v1 (Wave 5)

**Status:** **documented** — determine if a workspace is **Foundation-compatible**, **Forge-compatible**, and **survivability-compatible**.  
**Timebox:** ~20 minutes after first build.

**Not:** certification, **not** automated validator product.

---

## Outcome labels

| Label | Meaning |
|-------|---------|
| **Foundation-compatible** | `foundations/` + `js/core/` present; tokens/layers contract honored |
| **Forge-compatible** | `data-section`, `data-block-id`, REPORT + mode discipline possible |
| **Survivability-compatible** | destroy/init/replace safe for touched sections |
| **Adoption-ready** | All three PASS + build PASS |
| **Blocked** | Any Critical fail — do not freeze |

---

## 1. Foundation copy validation

- [ ] `src/scss/foundations/` includes `_tokens`, `_layers`, `_breakpoints`, `_utilities`, `_forms`, `_modal`
- [ ] `src/js/core/lifecycle.js`, `modal.js`, `form.js` present
- [ ] `main.scss` import order: foundations → sections
- [ ] Only `_tokens.scss` brand customized (no fork of `_layers` without REPORT Critical)

**Fail:** missing core file → copy from [website-factory-reference-v1](../../workspaces/website-factory-reference-v1/) or [_template-client-v1](../../workspaces/_template-client-v1/).

---

## 2. Build validation

```powershell
cd workspaces/<slug>
npm install
npm run build
```

- [ ] Exit code 0  
- [ ] `dist/index.html` (or page entry) opens without 404 on css/js  
- [ ] Record PASS/FAIL in REPORT

**SAFE UNKNOWN** if operator did not run locally.

---

## 3. Section replacement validation

Skip if bootstrap-only (hero only).

- [ ] Section roots have `data-section` + `data-block-id`  
- [ ] Swap demo or doc workflow understood: destroy → swap → init  
- [ ] One module section tested (`form` or `sticky-cta`) if present

---

## 4. Lifecycle validation

- [ ] `WfLifecycle.initPage()` called once from `main.js`  
- [ ] No duplicate modal handlers after re-init (manual click test)  
- [ ] `data-module` names registered before init

---

## 5. Responsive validation

- [ ] 375px — no horizontal scroll  
- [ ] 768px — grids intentional  
- [ ] Desktop — container centered  

Use [visual-regression-workflow-v1.md](visual-regression-workflow-v1.md) when slice is visual.

---

## 6. Onboarding validation

- [ ] README or charter path documented in REPORT  
- [ ] Operator knows reference vs client boundary  
- [ ] Chat memory not treated as SoT (handoff + REPORT cited)

---

## 7. REPORT validation

- [ ] `# REPORT —` heading present  
- [ ] Files created/updated listed  
- [ ] Verification + SAFE UNKNOWN sections  
- [ ] Freeze state explicit for Standard+

Template: [golden-report-examples-v1.md](operational-examples/golden-report-examples-v1.md), [_template-client-v1 REPORT](../../workspaces/_template-client-v1/docs/REPORT-TEMPLATE.md).

---

## Compact checklist (copy to REPORT)

```markdown
## Adoption validation (v1)
- Foundation copy: PASS | FAIL
- Build: PASS | FAIL | SAFE UNKNOWN
- Section replacement: PASS | N/A | FAIL
- Lifecycle: PASS | FAIL
- Responsive 375/768/desktop: PASS | partial | SAFE UNKNOWN
- REPORT complete: PASS | FAIL
- **Verdict:** Adoption-ready | Blocked — <reason>
```

*Wave 5 — adoption validation.*
