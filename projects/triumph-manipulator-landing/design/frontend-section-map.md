# Frontend section map — Triumph Manipulator Landing

**Scope:** Mockup → `landing-strip-*` **continuity map** (starter / foundation layer). **Not** the authoritative list of partials wired into the **current active V2** homepage. Filesystem roles and today’s `index.html` composition: [`../V2-CANONICAL-STATE.md`](../V2-CANONICAL-STATE.md).

**Purpose:** map raster mockup order → Gulp starter **section partials** (foundation only; no final copy or pixel-perfect layout).  
**Frontend workspace:** `workspaces/triumph-manipulator-landing/`

## Convention

Starter rule: **lowercase kebab-case**; section partials live under `src/partials/sections/` with matching SCSS under `src/scss/sections/`.

## Map (mockup → partial → SCSS)

| Mockup | Section partial | SCSS module | Role |
|--------|-----------------|-------------|------|
| `design/mockups/01.png` | `partials/sections/landing-strip-01.html` | `_landing-strip-01.scss` | Placeholder block for artwork segment 1. |
| `design/mockups/02.png` | `partials/sections/landing-strip-02.html` | `_landing-strip-02.scss` | Placeholder block for segment 2. |
| `design/mockups/03.png` | `partials/sections/landing-strip-03.html` | `_landing-strip-03.scss` | Placeholder block for segment 3. |
| `design/mockups/04.png` | `partials/sections/landing-strip-04.html` | `_landing-strip-04.scss` | Placeholder block for segment 4. |

## Homepage entry

**Operator note:** The subsection below stays **as written** for continuity with this strip-based mockup table. For the **live** Triumph V2 homepage partial sequence, use [`../V2-CANONICAL-STATE.md`](../V2-CANONICAL-STATE.md) and `workspaces/triumph-manipulator-landing-v2/src/pages/index.html`.

- **`src/pages/index.html`** includes `landing-strip-01` … `landing-strip-04` inside `<main>` (pattern A: head → header → main sections → footer → scripts).  
- **Semantic / product section names** (hero, pricing, FAQ, etc.) are **not** decided in this foundation pass — rename splits once design analysis names them.

## Other starter pages

- `about.html` and `service.html` retain the generic starter structure for internal-page pattern (B) reference; they are **not** the Triumph landing deliverable.

## Assets

- Mockups stay under **`projects/.../design/mockups/`** unless an explicit decision copies approved references into `src/img/` (not part of this task).
