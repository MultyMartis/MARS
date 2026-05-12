# Triumph Manipulator Landing — local frontend workspace

This folder is the **local working area** for frontend implementation, initialized from the production **gulp-starter** template. Starter-specific structure, commands, and conventions follow below after the separator.

## Project documentation

See **[`../../projects/triumph-manipulator-landing/README.md`](../../projects/triumph-manipulator-landing/README.md)** and **[`../../projects/triumph-manipulator-landing/frontend-workspace.md`](../../projects/triumph-manipulator-landing/frontend-workspace.md)**.

## MARS workspace policy

- Do not commit **build output** or unreviewed **client assets** into MARS without explicit approval.
- Follow **[`../../agents/frontend-gulp-agent/`](../../agents/frontend-gulp-agent/)** for operational discipline.

---

# Gulp Starter

**Universal starter template** — production-ready base for static HTML, SCSS, and JavaScript using `gulp-file-include`. It is meant to be copied into new repos for real sites; **this repository** keeps generic architecture and reusable demo content, not a shipped client production site by default.

Built for multipage static sites, landing pages, and internal pages without CMS, PHP, or database.

## Structure

- `src/pages` - final page entry points (`index.html`, `about.html`, `service.html`)
- `src/partials/sections` - large page blocks
- `src/partials/components` - reusable UI parts
- `src/scss` - styles organized as `base`, `utils`, `layout`, `sections`, `components`
- `src/js/main.js` - initialization entry point
- `src/js/modules` - feature/component and plugin logic (when required)
- `src/js/utils` - shared helpers only when needed
- `dist` - generated output

## Commands

- `npm install`
- `npm run build`
- `npm run watch`

## Starter scope

- static HTML workflow only
- no CMS logic
- no PHP templates/routing
- no database/backend dependencies
- generic reusable template content (not a real client website by default)
- **critical UI** should avoid fragile chains of dynamic `import()` that can fail silently; prefer a load path you can verify in the build you actually use
- **classic script tags** and **`window` globals** (e.g. plugin UMD builds) are acceptable when reliability or build constraints require the simplest dependency path

## Frontend library integration

When a task requires Swiper, Fancybox, Inputmask, or similar plugins:

- add a plugin only when it is actually needed
- keep plugin markup valid according to plugin requirements
- keep plugin logic in `src/js/modules`
- initialize plugins from `src/js/main.js`
- avoid inline scripts and plugin logic in HTML
- use stable data-* attributes as primary JS hooks where practical
- keep styling classes separate from JS behavior hooks
- keep integration minimal and architecture-safe

Examples of stable hooks: `data-modal`, `data-modal-open`, `data-modal-close`, `data-slider`, `data-fancybox`, `data-mask="phone"`.

### Swiper vs Fancybox

- **Swiper** → carousel/slider behavior and in-slider navigation only.
- **Fancybox** → lightbox / enlarged image (or media) opening only.
- Avoid extra “glue” scripts unless a real conflict is proven.
- Do not combine Swiper-driven sliding with manual `scrollBy` in the same gallery block.

### Progressive enhancement and robust UI (summary)

Full detail lives in **`AGENTS.md`** (sections on progressive enhancement, gallery rules, FAQ accordion, interaction styling, debug order). In short:

- Ship a **usable HTML/CSS baseline** before JS enhancements; do not hide essential content behind JS-only failure points.
- **Motion:** support `prefers-reduced-motion`; prefer transform/opacity for light motion.
- **Accordions (e.g. FAQ):** one open item per group by default; toggle closed on second click; accessible button with `aria-expanded` and `aria-controls` (stable ids linking control to panel).
- **CSS interaction:** unify hover and `:focus-visible`; avoid `transition: all` and hover-driven layout shift; scope rules to blocks.
- **When interactions break:** verify script execution → globals → selectors → block scope → CSS blocking clicks — then logic.

### Anti-patterns (quick reference)

- Do **not** mix **Swiper** and **manual `scrollBy`** (or other scroll hacks) in one gallery block — pick one interaction owner.
- Do **not** patch blindly before checking the **real execution path** (loaded → init ran → selectors match DOM).
- Do **not** let **async / module / dynamic-import chains** silently break **critical** UI — simplify the path or make failures visible in development.
- Do **not** rewrite stable markup before checking **init, selectors, and CSS** (including hit targets and stacking).

## Rules

- edit only `src`
- `dist` is generated; do not edit `dist` manually
- `src/pages` contains only final pages; no partials, no sections, and no blocks
- naming convention: lowercase only
- naming convention: kebab-case only
- HTML and SCSS names must match (example: `hero.html` ↔ `_hero.scss`)
- avoid random names like `section1`, `new-block`, `final-block`
- layout contains only structural parts: `head`, `header`, `footer`, `scripts`
- sections are large page blocks (for example: `hero`, `contacts`)
- components are reusable small elements (for example: `button`, `modal`, `breadcrumb`)
- JS rule: `src/js/main.js` is initialization/bootstrapping only
- JS rule: `src/js/modules` contains component or block logic
- JS rule: `src/js/utils` is optional and used only for shared helpers
- JS hook rule: prefer data-* selectors over presentational class selectors for behavior
- script order rule: when module scripts are included before `main.js`, load order matters
- SEO rule: only one `h1` per page
- SEO rule: keep heading hierarchy `h1` → `h2` → `h3`
- SEO rule: use semantic tags (`header`, `main`, `section`, `nav`, `footer`)
- SEO rule: breadcrumbs are required before main page section on internal pages
- SEO rule: page title in `head` must match page meaning
- homepage/special pattern (pattern A): `head` → `header` → `hero` → content sections → `footer` → `scripts`
- internal page pattern (pattern B): `head` → `header` → `breadcrumb` → `page-intro` (main section with `h1` + intro text) → optional supporting sections → `footer` → `scripts`
- hero rule: use `hero` only on homepage or landing-style pages
- keep existing project structure; do not change architecture
- progressive enhancement, gallery boundaries (Swiper vs Fancybox), accessibility/motion, and interaction debug order: **`AGENTS.md`** (single source of truth)