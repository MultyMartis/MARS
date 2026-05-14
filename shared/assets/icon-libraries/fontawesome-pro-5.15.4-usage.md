# Font Awesome Pro 5.15.4 — local usage registry (MARS)

**Layer:** controlled shared asset tree under `shared/` — classification and boundaries: [`../../README.md`](../../README.md).

**Canonical local path (do not relocate into public `dist/` or publish):**

`D:\AI MARS\shared\assets\icon-libraries\Font Awesome Pro 5.15.4`

This asset is a **licensed, local-only** dependency. Treat every glyph as covered by your Font Awesome Pro agreement. Do not upload the folder, do not attach the whole library to tickets or public repos, and do not ship the entire `webfonts/` or full `all.css` bundle unless your license explicitly allows that distribution model.

---

## What is in this folder

Top-level layout (inspected):

| Path | Purpose |
|------|---------|
| `css/` | Stylesheets mapping icon class names to font families and Unicode code points |
| `webfonts/` | Font binaries: `.woff2`, `.woff`, `.ttf`, `.eot`, and **SVG font** files (aggregated font sources, not one icon per file) |

Representative `css/` entry points:

- `all.css` / `all.min.css` — **full Pro stack** (solid, regular, light, duotone, brands, plus Free/shims as bundled)
- `solid.css`, `regular.css`, `brands.css` — **subset** stylesheets
- `fontawesome.css` — base + dependencies for layered use
- `svg-with-js.css` — SVG+JS integration (requires Font Awesome JS; not part of this doc’s recommended static-SVG workflow)
- `v4-shims.css` — Font Awesome 4 class compatibility
- `free.css` / `free.min.css` — Free tier subset (this tree also contains Pro webfonts; prefer explicit Pro usage)

`webfonts/` naming pattern:

- `pro-fa-solid-900-*.woff2` — **Solid** (weight 900)
- `pro-fa-regular-400-*.woff2` — **Regular**
- `pro-fa-light-300-*.woff2` — **Light**
- `pro-fa-duotone-900-*.woff2` — **Duotone**
- `pro-fa-brands-400-*.woff2` — **Brands**
- Version suffixes (e.g. `-5.15.4`) reflect incremental glyph additions across FA 5.x; `all.css` wires the correct files.

---

## Available icon styles (Pro 5.x)

| Style | CSS prefix (typical) | When to use |
|-------|----------------------|-------------|
| **Solid** | `fas` | Small sizes, dense UI, maximum legibility on busy backgrounds |
| **Regular** | `far` | Marketing UI, softer strokes on large icons |
| **Light** | `fal` | Hero sections, airy layouts, large display icons |
| **Duotone** | `fad` | Accent highlights; heavier file/CSS cost; two-layer look |
| **Brands** | `fab` | Social and product logos permitted under Brands license |

Confirm a glyph exists in **this** build by searching `css/all.css` for the class, e.g. `.fa-truck-loading:before`.

---

## “SVG folders” and individual icon files

**There is no `svgs/` (or similar) directory of standalone per-icon SVG files in this installation.**

The `.svg` files under `webfonts/` are **SVG font** containers (many glyphs in one font file), not export-ready single-icon assets.

**Implications for MARS frontends:**

- Default **registry role** of this path: **source of truth for names, styles, and licensing** + optional **local reference** when previewing in a private HTML page linked to `all.css` (never committed as a wholesale dependency).
- For **shipping** icons in a static site: copy **only** curated, exported single-glyph SVGs (or a manually built sprite) into the project’s `src/` tree, following the policy note for each project.

**Safe ways to obtain a single-icon SVG (pick what your license allows):**

1. **Official Font Awesome workflows** included with your Pro entitlement (e.g. icon search + SVG download from Font Awesome’s tools, if applicable to your plan). Store only the extracted files in the repo.
2. **Vectorize from a permitted export** using design tooling, without redistributing the full font folder.
3. **Do not** copy entire `webfonts/` or `all.min.css` into `src/` or `dist/` “for convenience.”

---

## Recommended styles by context

| Context | Recommendation |
|---------|------------------|
| **Landing pages (marketing)** | **Light** (`fal`) or **Regular** (`far`) for large hero and benefit icons; pair with generous size and ample contrast |
| **Dark backgrounds** | **Solid** or **Regular** with sufficient `currentColor` contrast; avoid ultra-thin light strokes at small sizes |
| **Light backgrounds** | **Light** or **Regular** for elegance; **Solid** for small inline metaphors |
| **Default for mixed MARS landings** | **Regular** for primary decorative icons; **Solid** for compact UI (buttons, dense lists) |

---

## How to copy selected icons into a project

1. **Choose the icon** in `css/all.css`: search for `.fa-<name>:before` (hyphenated name, Font Awesome 5 naming).
2. **Pick one style** (`fal`, `far`, `fas`, `fad`, `fab`) and stick to it per section (see project policy notes).
3. **Export a single SVG** via an allowed channel (see above). Prefer **flattened** paths and a single color (`currentColor`) where the build uses stroke/fill utilities.
4. **Place files** under the project’s existing convention (e.g. Triumph: `workspaces/triumph-manipulator-landing/src/svg/` for sprite symbols, or `src/img/...` for raster-like social marks — follow that project’s architecture).
5. **Do not** add symlinks from `dist/` back to `shared/assets/icon-libraries/` (avoids accidental publishing).

---

## Naming copied icons

Use **kebab-case**, descriptive, **project-prefixed** when ambiguity exists:

- Good: `hero-truck-route.svg`, `trust-shield-check.svg`, `ui-plus.svg`
- Tie names to **purpose**, not only FA names, so refactors stay readable.
- If you keep FA provenance in an internal comment, use a one-line HTML/XML comment inside the SVG **only** if your build preserves it and the comment does not leak license keys.

---

## Avoid copying the full library into `src/` or `dist/`

- **Never** commit `webfonts/` or full `all.css` / `all.min.css` as a project dependency unless explicitly approved under your license and deployment policy.
- **Never** configure bundlers to glob-import `../shared/assets/icon-libraries/**`.
- **Do** add only the minimal number of SVGs (often 10–40 for a landing), reviewed for weight and contrast.

---

## Licensing and local-only discipline

- Keep the library under `shared/assets/icon-libraries/` on trusted workstations and internal backups **only** as your agreement permits.
- **Do not** expose this directory via static file servers, Storybook public builds, or CI artifacts.
- Generated **dist** should contain **only** the subset you deliberately copied or inlined.
- Third-party marks (e.g. review platforms, messengers) may require **their** brand guidelines; Font Awesome **Brands** covers many social glyphs — still verify trademark rules separately.

---

## Quick reference: discover icon names locally

From the repo root (PowerShell example):

```powershell
Select-String -Path "D:\AI MARS\shared\assets\icon-libraries\Font Awesome Pro 5.15.4\css\all.css" -Pattern "\.fa-truck" | Select-Object -First 20
```

Use the `.fa-<slug>:before` slug as the Font Awesome icon name.

---

## Related project policy

Triumph Manipulator landing: `projects/triumph-manipulator-landing/notes/icon-source-policy.md`
