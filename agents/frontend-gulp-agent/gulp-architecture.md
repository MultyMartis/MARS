# Target gulp-starter architecture (reference shape)

This section documents the **intended** static-site layout aligned with the Website Factory **frontend production model** and common gulp-starter patterns. **It is not evidence** that any particular clone in the MARS repo matches these paths.

## Reference tree (verify in target repo)

| Area | Typical path | Role |
|------|----------------|------|
| Page entries | `src/pages/` | Final HTML entry points only (no embedded section bodies). |
| Layout partials | `src/partials/layout/` | Shell, head fragments, shared wrappers. |
| Sections | `src/partials/sections/` | Large page blocks mapped from **`section_map`**. |
| Components | `src/partials/components/` | Smaller reusable UI fragments. |
| Styles | `src/scss/` | Tokens, base, layout, sections, components partials. |
| JS modules | `src/js/modules/` | Feature/component behaviors. |
| JS utils | `src/js/utils/` | Shared helpers when truly shared. |
| Images | `src/img/` | Raster (exact folder name may differ e.g. `src/images/`). |
| Fonts | `src/fonts/` | Font files referenced from SCSS. |

Many starters also use **`src/js/main.js`** as the init entry, **`src/svg/`** or sprite dirs, **`src/favicon/`**, and **`src/assets/design/`** for design exports — **SAFE UNKNOWN** until the target repo is inspected.

## Build output

- **`dist/`** (or the directory named in **`integration_notes`**) is **generated only** — never hand-edited for “quick fixes”.

## Honesty

- **Do not assume** exact paths without listing the target repo’s tree or README.
- If the project differs (e.g. Vite, different partials folder), document the **actual** mapping in REPORT **SAFE UNKNOWN** / notes and follow **that** repo’s SoT.
