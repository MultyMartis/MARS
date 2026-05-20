# Design system — working notes (Triumph Manipulator Landing)

**Status:** foundation / handoff notes only. **No confirmed token table** is implied by this file.

## PDF labeled “DESIGN SYSTEM EXPORT”

If the uploaded PDF only lists **required export categories** (colors, typography, spacing, components, etc.) without concrete values:

- Treat listed **categories** as a checklist for what to extract next from Figma or an approved export.  
- Do **not** treat missing numbers as implicitly approved.  
- Prefer **measuring mockups** or reading **real design exports** before locking tokens.

## What is already in the repo (evidence-based)

- **Gulp workspace** (`workspaces/triumph-manipulator-landing/`) ships a dark starter baseline in `src/scss/base/_base.scss` (background, text, Arial stack). That is **starter demo**, not proof of final brand tokens.  
- **Layout width** in `src/scss/utils/_variables.scss`: `$container-width: 1230px`, `$container-padding: 15px` — starter defaults until replaced.

## Token placeholders (SCSS)

`src/scss/utils/_tokens.scss` lists **categories** for:

- colors  
- typography  
- spacing  
- containers  
- buttons  
- forms  
- cards  
- sections  

Variables there are **scaffolding** (comments + safe structural hooks). Values must be reconciled against an approved design source before claiming brand fidelity.

## SAFE UNKNOWN (until verified)

- Exact brand palette, font families, type scale, radii, shadows.  
- Grid / breakpoint system relative to mockup artboard vs browser viewport.  
- Whether `04.png` size difference vs `01–03` is intentional artboard change or export setting — confirm with design owner.
