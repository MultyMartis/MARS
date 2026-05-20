# Client workspace template v1 (Wave 5)

**Status:** **minimal starter** — copy to `workspaces/<client-slug>-v1/`, then adopt per charter.  
**Not:** a client delivery; **not** auto-scaffolding runtime.

---

## Quick start (minutes)

```powershell
# 1. Copy template
Copy-Item -Recurse "workspaces\_template-client-v1" "workspaces\acme-landing-v1"

# 2. Install + build
cd workspaces\acme-landing-v1
npm install
npm run build

# 3. Open dist/index.html
```

**First edits (order):**

1. `src/scss/foundations/_tokens.scss` — brand colors only  
2. `src/partials/layout/header.html` — logo / nav  
3. `src/partials/sections/hero.html` — offer copy  
4. Add blocks from [website-factory-reference-v1](../website-factory-reference-v1/) partials + scss

---

## Structure

| Path | Role |
|------|------|
| `src/pages/` | Page entries (`@@include` graph) |
| `src/partials/layout/` | Shell — header, footer, modal (not section-replaced by default) |
| `src/partials/sections/` | `data-section` + `data-block-id` units |
| `src/scss/foundations/` | **Critical** — copy wholesale; token brand edit only |
| `src/scss/sections/` | Per `block_id` scoped SCSS |
| `src/js/core/` | `WfLifecycle`, modal, form — do not fork API |
| `src/js/main.js` | `initCore` + `initPage` entry |
| `docs/REPORT-TEMPLATE.md` | Session REPORT skeleton |

---

## Onboarding docs (read order)

1. [onboarding-flow-v1.md](../../projects/mars-website-factory/onboarding-flow-v1.md) — Path B  
2. [foundation-adoption-charter-v1.md](../../projects/mars-website-factory/foundation-adoption-charter-v1.md)  
3. [adoption-validation-flow-v1.md](../../projects/mars-website-factory/adoption-validation-flow-v1.md)  
4. [operational-qa-entry-v1.md](../../projects/mars-website-factory/operational-qa-entry-v1.md)

**Reference implementation:** [website-factory-reference-v1](../website-factory-reference-v1/).

---

## Section placeholders

After hero, copy block partials from reference:

- `pricing`, `social_proof`, `faq`, `lead_form`, `cta_band`, `contact_block`, `sticky_cta`

Wire each `@@include` in `src/pages/index.html` and `@use` in `src/scss/main.scss`.

---

## REPORT

Use [docs/REPORT-TEMPLATE.md](docs/REPORT-TEMPLATE.md) for every bootstrap or section slice.

*Wave 5 — canonical client workspace scaffold.*
