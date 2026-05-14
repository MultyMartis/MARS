# AGENTS.md

## Repository kind (read first)

Gulp-starter supports two repository **roles** (same architecture and workflow patterns; different content and delivery expectations):

1. **Canonical gulp-starter template** — the upstream **universal starter** repository. It exists to be **copied into new projects**; it keeps generic demo content and is not a default home for a shipped client production site or real brand.
2. **Client/product copy** — a repository or workspace **created from the starter** for a specific client or product. It holds real design materials, real content, and production implementation when tasks require them.

**This repository is the canonical gulp-starter template.** Treat generic demo content and “no real client site by default” as the baseline here.

Rules below use **“canonical template only”** where something must **not** turn the starter into a client delivery inside the template repo. They use **client/product copy** where real pages, real `src/assets/design/` work, and full pixel-perfect execution are normal.

## Project role

**In a client/product copy** (delivery workspace created from the starter):

- Real design files under `src/assets/design/` are expected for design-driven work.
- Real business/client pages, copy, SEO/service pages, and landings are allowed when the task requests them.
- **Pixel-perfect and design-execution rules apply in full** (see Pixel-Perfect Frontend Workflow and Pixel-Perfect Design Execution Standard).
- For **visual work**, **design execution rules take priority** over starter demo styling, default colors/spacing from examples, and “generic reusable” presentation choices.

**In this canonical template repository:**

- The repo is the reusable starter, not a client website.
- Keep demo pages generic; do not ship real client production sites from the template repo unless explicitly requested.

## Core rule
Preserve the gulp-starter **architecture** (folders, layers, build pipeline, include patterns).
Do not redesign or expand the **architecture** unless explicitly requested.

**Scope note:** “Preserve architecture” does **not** mean preserving starter **visual** defaults. In design-based tasks, visual output must follow the **design source**, not leftover starter appearance.

## Project structure
- src/pages — only final ready-to-build pages
- src/partials/layout — layout files only
- src/partials/sections — large page sections
- src/partials/components — small reusable UI parts
- src/scss mirrors the HTML structure
- src/scss/base — reset, base, typography
- src/scss/utils — vars, mixins, functions
- src/scss/layout — layout styles
- src/scss/sections — section styles
- src/scss/components — component styles
- src/js/main.js — initialization only
- src/js/modules — feature/component logic only when needed
- src/js/utils — generic helpers only when needed
- src/img — raster images
- src/svg — svg files and sprite sources
- src/fonts — fonts
- src/favicon — favicon source files
- src/assets/design — design sources and exports for implementation (see Pixel-Perfect Design Execution Standard)
- dist is build output and must never be edited manually

## Hard restrictions
- Do not edit dist
- Do not restructure folders
- Do not move files between directories
- Do not rename existing files unless explicitly requested
- Do not create unnecessary files
- Do not add frameworks unless explicitly requested
- Do not add libraries unless explicitly required by the task
- Do not create JS unless the task really requires JS
- Do not refactor unrelated files
- Do not modify unrelated pages or sections
- **Canonical template only:** do not generate real client production pages unless explicitly requested.
- **Client/product copy:** real client pages and implementation are allowed when the task requests them.

## Starter vs client/product copy rule
**Canonical gulp-starter template:**

- Keep pages generic; keep demo content reusable.
- Do not create real SEO/business/service pages unless explicitly requested.
- Do not turn template demo pages into a client website inside the template repo.

**Client/product copy:**

- Real business content is allowed and expected when tasks require it.
- Internal service pages, SEO pages, and landing pages may be created as requested.
- Real design files and pixel-perfect implementation against those sources are normal workflow, not an exception.

## Workflow rule
All multi-file operations must be executed as one coherent Codex task (single agent run for the **current step**).
**Design implementation exception:** “one coherent task” still means **at most one new visual block** per coding delivery; do not use this bullet to justify multi-block batching. Block-by-block and approval rules override a broad interpretation of “one task.”

Do not suggest manual step-by-step editing by default for:
- project structure
- page generation
- multi-file section/component creation
- mass changes

Default workflow:
1. Understand the task
2. Apply the required file changes directly
3. Report created and modified files
4. Run build validation
5. Fix build errors if any
6. Return final status

## Page rules
- One page = one H1
- Use semantic HTML
- Keep markup clean and production-ready
- Avoid meaningless wrapper nesting
- **Copy and content:** avoid fake demo filler (lorem ipsum, meaningless marketing fluff) unless the task explicitly allows temporary copy. This is unrelated to **visual assets** — see Pixel-Perfect rules: **no image/icon/logo placeholders** in design-based implementation unless explicitly approved.
- Internal pages must not use hero unless explicitly requested
- Homepage and special landing pages may use hero
- Internal page default structure:
  1. breadcrumb
  2. page-intro or main content block
  3. supporting sections below

## Include rules
- Use valid gulp-file-include syntax
- Include paths must be correct
- Parameters for includes must be valid JSON in one line
- Reuse existing includes before creating new ones
- Do not duplicate layout logic across pages if reusable includes are appropriate

## Naming rules
- Use lowercase
- Use kebab-case for file names, class names, section names, and component names
- Use descriptive practical names
- Do not use vague names like block, temp, test, new-section, item2

## Section rules
- Large standalone blocks belong in src/partials/sections
- A section should be reusable where reasonable
- Do not hardcode page-specific content into a reusable section unless explicitly requested
- Each new section must have matching SCSS in src/scss/sections if styling is needed

## Component rules
- Small reusable UI parts belong in src/partials/components
- Components must remain generic and reusable
- Each new component must have matching SCSS in src/scss/components if styling is needed

## SCSS rules
- SCSS structure must mirror HTML structure
- Add styles only to the proper layer: base / utils / layout / sections / components
- Connect new SCSS files in src/scss/style.scss
- Do not duplicate imports
- Do not break existing import order
- Do not place section styles in component files or vice versa
- Keep styles scoped, clean, and production-ready
- Avoid global leakage
- Avoid unnecessary visual overdesign
- Build responsive structure by default

## JS rules
- Use JS only if really needed
- Put initialization in src/js/main.js
- Put feature logic in src/js/modules
- Put generic helpers in src/js/utils
- Use explicit import/export pattern
- No global registry
- No inline scripts
- No inline handlers

**Architecture note (starter knowledge):** Avoid overengineering for simple UI blocks. For small, isolated, **critical** interactions (e.g. one accordion, one gallery), a short module or a deliberately simple boot path is preferable to deep dependency chains. Before debugging behavior, **verify the real execution path** (script loaded, init ran, selectors match DOM) — do not stack patches on assumed failure modes.

## JS hook rules
- Prefer data-* attributes for JS hooks and initialization
- Do not use presentational CSS classes as the primary JS selector when data-* is more appropriate
- Keep styling classes and JS hooks separated
- Use stable patterns such as:
  - data-modal
  - data-modal-open
  - data-modal-close
  - data-tabs
  - data-tab
  - data-tab-panel
  - data-accordion
  - data-accordion-button
  - data-accordion-panel
  - data-slider
  - data-fancybox
  - data-mask

## Library integration rules
When the task requires Swiper, Fancybox, Inputmask, or a similar plugin:
- first check whether the library is already used in the project
- connect it only if the task actually requires it
- prefer CDN by default unless local hosting is explicitly requested
- keep plugin markup valid
- keep plugin logic in src/js/modules
- initialize plugins from src/js/main.js
- do not place plugin logic inside HTML
- do not create inline scripts
- use stable data-* hooks where practical

**Swiper and Fancybox (roles and boundaries):**
- **Swiper** owns sliding and in-carousel navigation only (pagination, arrows, swiper API).
- **Fancybox** owns opening images (or grouped lightbox items) only.
- Do not add custom “bridge” scripts that duplicate or fight those responsibilities unless a **proven** conflict requires a minimal, documented workaround.
- In one gallery block, **do not** combine Swiper-driven movement with manual `scrollBy` / imperative scroll hacks for the same axis of interaction — pick one strategy.
- For **critical** gallery behavior (above-the-fold product visuals, legal disclosures): avoid fragile chains of dynamic `import()` that can fail silently; in constrained or unstable environments, a **classic script tag** plus `window.Swiper` / `window.Fancybox` can be more reliable than a long module graph. Prefer the simplest dependency path that still matches the build setup.

## Head rules
Every real project page must support:
- unique title
- meta description
- viewport
- charset
- robots when relevant
- Open Graph tags
- Twitter/social tags when relevant
- favicon links

Do not add fake verification tags.
Do not invent fake production URLs or fake image URLs.

## Favicon rules
- Favicon source files belong in src/favicon
- Reuse existing favicon markup in layout/head
- Do not invent nonexistent favicon filenames

## Content rules
For generated real project pages:
- write realistic production-ready content
- no lorem ipsum
- no filler text
- no generic AI fluff
- keep text practical, structured, and commercially useful when needed
- avoid keyword stuffing
- keep headings meaningful

For starter template files:
- keep content neutral, generic, reusable
- do not insert client-specific sales copy unless explicitly requested

## Build validation rule
After changes:
1. Provide a short report:
   - created files
   - modified files
   - connected imports/includes/modules
2. Run:
   npm run build
3. If build fails, fix the errors
4. Final output must be:
   - Build succeeded
   or
   - a short concrete list of remaining errors

## Priority order
When in doubt (general tasks):

1. Preserve architecture (structure, layers, build safety).
2. Reuse existing project patterns.
3. Keep output minimal, clean, and build-safe.
4. Add libraries only when required.
5. Keep head/meta/favicon complete for real pages.
6. Do not make broad assumptions beyond the task.
7. For interactive UI: progressive enhancement and content safety (see **Progressive enhancement, motion, and content safety**) before clever JS-only patterns.

**Canonical template only:** avoid turning generic demo content into client-specific pages unless requested.

**Design-based implementation in a client/product copy:** if anything above conflicts with **design source fidelity** or the **mandatory pixel-perfect workflow** (analysis first, one block, approvals), **design execution wins for visuals**. See **Execution priority (design-based work)** at the end of this file.

## Pixel-Perfect Frontend Workflow

### Source of truth
Design source is the only visual source of truth.
The gulp-starter codebase is only a technical base:
- structure
- includes
- build system
- architecture

AI must not reinterpret, simplify, restyle, or approximate a design. **In a client/product copy,** this applies to all client-facing design implementation work.

### Priority of design sources
1. Figma (preferred)
2. PNG export
3. PDF export

If Figma is available, it must be used as the primary reference.

### Global workflow
Every page must be implemented using this sequence:

1. Full design analysis
2. Page split into exact visual blocks
3. Asset extraction plan
4. One-block implementation
5. Local preview
6. Pause for approval
7. Continue only after approval

### Block-by-block rule
- Only ONE block can be implemented at a time
- AI must not implement multiple sections in one step
- AI must not skip blocks
- AI must stop after each block

### Visual accuracy rule
AI must strictly reproduce:
- layout
- spacing
- typography
- proportions
- alignment
- visual hierarchy

AI must NOT:
- normalize spacing
- adjust typography “for better look”
- simplify compositions
- replace real assets with placeholders
- invent missing visual parts

### Asset rule
If the design contains:
- images
- icons
- logos
- decorative elements

AI must:
- use real assets
- or recreate them accurately

Placeholders are forbidden unless explicitly allowed.

### Responsive rule
Responsive behavior must follow the design.

If some breakpoint is not provided:
- preserve the logic of the closest available layout
- do not invent complex alternative layouts

### Isolation rule
While implementing a block:
- do not modify other blocks
- do not refactor unrelated files
- do not change approved sections

### Approval rule
After each block:
AI must:
1. ensure build works
2. update preview
3. report status
4. STOP

AI must wait for:
- approved
- continue
- fix this block

### Correction rule
If a block is not pixel-perfect:
- fix ONLY that block
- do not change page structure
- do not modify other sections

## Pixel-Perfect Design Execution Standard

### Purpose
Projects using this workflow must support strict pixel-perfect implementation from design files.
The design source is the only visual source of truth.
The gulp-starter layout (partials, SCSS layers, Gulp pipeline) remains only a technical base:
- project structure
- includes
- build system
- architecture

### Design source priority
Use this priority:
1. Connected Figma source
2. Exported design files inside project design folder
3. PNG export
4. PDF export

If a raw Figma source file is not technically accessible in the current environment, use exported PNG/PDF assets from the design folder as the implementation reference.

### Design folder rule
All design materials for implementation must be stored inside:
`src/assets/design/`

Recommended structure:
```
src/assets/design/
  page-name/
    original/
    exports/
    images/
    icons/
    notes/
```

Rules:
- `original` = raw provided design files
- `exports` = png/pdf/jpg exported screens
- `images` = extracted raster assets
- `icons` = svg/icon assets
- `notes` = implementation notes related to that page

AI must inspect this folder before starting design-based work.

### Mandatory design-first workflow
For any real page implementation from a design:
1. Inspect available design files in `src/assets/design/`
2. Analyze the full page before coding
3. Split the page into exact visual blocks
4. Write a structured implementation plan
5. Implement only one block at a time
6. Validate preview after that block
7. Stop and wait for approval
8. Continue only after approval

### Internal implementation notes rule
Before implementing a design-based page, AI must create or update a working note file in:
`docs/ai-workflow/`

This note must contain:
- page name
- detected design sources
- block list in top-to-bottom order
- asset list
- typography notes
- spacing/container notes
- responsive notes
- current implementation status per block

Purpose:
AI must keep a persistent self-check plan so it does not lose structure during long tasks.

### Exact visual fidelity rule
AI must reproduce exactly:
- section order
- layout
- spacing
- dimensions
- proportions
- typography
- visual hierarchy
- alignments
- real assets
- breakpoint behavior visible in the design

AI must not:
- simplify composition
- visually reinterpret
- improve design on its own
- normalize spacing “for consistency”
- replace real assets with placeholders unless explicitly allowed

### Container and page padding rule
Default container side paddings:
- desktop: 50px
- mobile/tablet: 10px
- very small mobile: 5px

Minimum supported viewport width:
- 320px

Main responsive split:
- Desktop: >= 1025px
- Mobile/Tablet: <= 1024px

### Breakpoint rule
Use these project breakpoints:
- 1440
- 1310
- 1199
- 1024
- 767
- 660
- 580
- 490
- 390
- 370

Main layout switch:
- desktop >= 1025
- mobile/tablet <= 1024

Rules:
- do not invent random breakpoints
- do not remove listed breakpoints
- use only the breakpoints relevant to the current design
- do not force all breakpoints into every block if unnecessary

### Block isolation rule
While implementing one block:
- do not modify other blocks
- do not touch approved blocks
- do not refactor unrelated files
- do not batch multiple sections in one step

### Approval-stop rule
After each block:
AI must:
1. report changed files
2. confirm preview/build status
3. summarize what was implemented
4. stop

AI must wait for:
- approved
- continue
- fix this block

### Correction rule
If the user requests a correction:
- fix only the current block
- preserve all correct parts
- do not rewrite the whole page
- do not touch unrelated sections

## Progressive enhancement, motion, and content safety

Applies to all projects built from this starter unless a task explicitly defines a different standard.

### Progressive enhancement
- **Default visible state first:** HTML/CSS must expose meaningful content and structure **without** JavaScript. JS enhances; it must not be the only thing making content usable.
- **Do not** hide critical copy, navigation, or media behind JS-only gates without a safe non-JS fallback (e.g. progressive disclosure must still leave content accessible or links usable).
- **Avoid** JS-dependent fully hidden panels for essential content unless failure modes were reviewed (SEO, accessibility, partial page load, ad blockers, script errors).

### Reveal, animation, and reduced motion
- **No disappearing content if JS fails:** Initial render must remain sensible; do not rely on JS to “create” essential text or structure.
- Prefer **transform** and **opacity** for lightweight motion; avoid animating properties that trigger heavy layout (width/height/top/left) unless required by design.
- Implement **`prefers-reduced-motion`**: respect user OS settings; provide a non-animated or minimally animated fallback.
- Animation systems (scroll reveals, entrance effects) must degrade safely when JS is off or fails — static layout remains readable.

### FAQ / accordion pattern
- **One panel open at a time** within the same accordion group unless design explicitly requires otherwise.
- **Toggle:** clicking the **currently open** header closes it (optional single-open behavior).
- Use **accessible controls:** `<button>` (or equivalent) with `aria-expanded`, `aria-controls`, and stable ids linking to panels.
- Keep JS **minimal and scoped** to the block root; no unrelated global listeners.

### Interaction styling (hover, focus, layout)
- **Unify** hover and `:focus-visible` treatments so keyboard users get parity with pointer hover where appropriate.
- **Avoid `transition: all`** — transition only properties you intend to animate (opacity, transform, colors with care).
- **No layout shift** on hover/active: avoid margin/padding changes that move surrounding content unless specified in design.
- **Scope styles** to block/section roots (BEM-style or equivalent); avoid leaking interaction rules globally.

### Debug priority when interactive UI fails
Work through in order before rewriting logic:

1. Script **actually runs** (no early error; bundle loads).
2. **Dependencies exist** (`window.Swiper`, Fancybox API, etc.) when using globals.
3. **Selectors match** real DOM (typos, dynamic markup, wrong partial).
4. **Block root / scope** is correct (init targets the intended section).
5. **CSS** does not block clicks (`pointer-events`, overlays, z-index, `overflow: hidden` clipping hit targets).
6. Only then: deeper application logic, timing, or plugin options.

### Anti-patterns (avoid)
- Mixing **multiple interaction strategies** in one block (e.g. Swiper + manual scroll + another carousel helper) without a clear single owner.
- **Repeated patches** without confirming load order, execution chain, and DOM match.
- Letting **async import / module chains** become a silent failure point for **critical** UI — simplify the path or surface errors in dev.
- **Rebuilding stable markup** repeatedly to “fix” interaction bugs instead of fixing initialization or selectors.

---

## Frontend Interaction and JS Hook Standard

### Data-attribute rule
For JS behavior, prefer `data-*` attributes as the default hook system.

Examples:
- `data-modal`
- `data-modal-open`
- `data-modal-close`
- `data-tabs`
- `data-tab`
- `data-tab-panel`
- `data-accordion`
- `data-accordion-button`
- `data-accordion-panel`
- `data-slider`
- `data-fancybox`
- `data-mask`

Rules:
- do not use presentational CSS classes as the primary JS selector when a `data-*` hook is more appropriate
- keep JS hooks separate from styling classes
- keep hooks stable and readable
- use semantic and task-specific `data-*` names

### Design-driven interaction rule
If interaction states are not visible in the design:
- do not invent complex behavior
- implement only the minimal technical behavior required by the task
- preserve visual consistency with the shown design states

## Design Analysis First Rule

Before implementing any page from design:

AI MUST:

1. Inspect design sources in:
   `src/assets/design/`

2. Identify:
   - available screens (desktop/mobile/tablet)
   - page type
   - main layout structure

3. Build a structured plan:
   - full list of sections (top to bottom)
   - section hierarchy
   - reusable components
   - assets per section

4. Create or update a design analysis file in:
   `docs/ai-workflow/`

This file must include:
- page name
- design sources used
- section list (ordered)
- asset list
- typography notes
- spacing notes
- responsive behavior notes
- unknown/missing states
- planned implementation order

5. STOP

AI must NOT:
- write HTML
- write SCSS
- create components
- create sections

until analysis is complete.

---

## Rule precedence (non-design vs design)

- **Always:** architecture preservation, folder structure, `dist` safety, valid includes, and successful `npm run build` after changes (unless the task says otherwise).
- **Design-based visual work:** sections **Pixel-Perfect Frontend Workflow**, **Pixel-Perfect Design Execution Standard**, and **Design Analysis First Rule** override generic “starter look,” convenience shortcuts, and any weaker workflow wording elsewhere in this file.
- **Conflict resolution:** if a bullet suggests placeholders, approximation, multi-block delivery, or skipping analysis/approval, treat it as **invalid for design implementation** unless it explicitly defers to this pixel-perfect section.

---

## Execution priority (design-based work)

For **design-based frontend implementation** in a **client/product copy**, execution priority is:

1. **Design source fidelity** (layout, spacing, type, assets, hierarchy, stated breakpoints).
2. **Approved workflow steps** (full analysis → `docs/ai-workflow/` plan → **one block** → preview/build report → **STOP** → user approval or “fix this block”).
3. **Architecture preservation** (partials/sections/components/layers, no manual `dist` edits).
4. **Build safety** (valid includes/SCSS imports; fix build errors).

**Not** valid priorities for design visuals:

- Convenience or speed over fidelity
- Simplification or “cleaning up” the design
- Starter default colors, spacing, or demo components as a stand-in for the design
- Placeholder images/icons/logos/decorative assets **unless explicitly approved**

---

## Agent behavior mode (real design tasks)

For **real design implementation** tasks in a **client/product copy**, the agent must behave as an **execution system**, not a generic advisor.

That means:

- Perform **only** the required phase (e.g. analysis-only until analysis is approved; **one** implementation block per step).
- Do **not** expand scope beyond the task or the current block.
- Do **not** propose alternative creative directions, frameworks, or redesigns unless the user explicitly asks for options.
- Do **not** skip design analysis or `docs/ai-workflow/` documentation before code.
- Do **not** skip approval checkpoints (stop after each block; wait for **approved** / **continue** / **fix this block**).
- Do **not** pad responses with generic explanatory filler; report what changed, build/preview status, and what is blocked on user input.

## Real Project Transition Rule

**This repository** is the canonical **gulp starter template** (universal upstream). It is **not** a default client delivery: no real brand, no production site content, and no client-specific design implementation should live here **by default**.

**Where real work happens**

- Client or production work is done in a **separate copy** of this starter (a new repo or folder created from the template).
- After copy, the same architecture applies, and **business pages, real copy, SEO targets, and design-to-HTML work** are expected in that **client/product copy** when the task requires them.

**Pixel-perfect workflow**

- In a **client/product copy**, the pixel-perfect, design-first, block-by-block, and approval rules in this file (and in `.cursorrules`) are the **active** standard for any design-based implementation.
- In **this canonical template repository**, keep examples generic; do not turn template pages into a live client site.

**Design files**

- Real design exports (Figma/PNG/PDF, assets, notes) belong in the **delivery project’s** `src/assets/design/` (per-page folders as documented in the design folder README).
- Do not commit or add real client design deliverables to the canonical starter unless the maintainer explicitly chooses to use this repo for that purpose.
