# Triumph Manipulator Landing V4 - Reset Plan

**Status:** planning only.  
**Do not execute cleanup from this document without explicit user instruction.**

## 1. Purpose

Prepare V4 for a future **full clean single-pass reconstruction rerun** while preserving authority, governance, assets, and build structure that remain valid.

This document does not wipe implementation, does not start reconstruction, does not polish current sections, and does not create V5.

## 2. Reset Objective

The next run should start from a clean V4 boundary:

- V1 source authority remains primary.
- Current reconstructed section implementation is treated as stale unless explicitly reapproved.
- Temporary reconstruction crops are treated as disposable implementation residue.
- Governance and source-audit documents survive as planning evidence.
- Build config survives if it remains valid after implementation reset.

## 3. MUST SURVIVE

The following should survive a future reset unless a later task explicitly supersedes them:

- `docs/` governance, audit, source-boundary, asset-boundary, and reset-boundary documents.
- Approved shared assets copied from `projects/triumph-manipulator-landing/design/shared-assets/` when path/name/integrity are still correct.
- Approved background assets when their source lineage and approval remain documented.
- Clean project structure: `src/pages/`, `src/partials/`, `src/scss/`, `src/img/`, `src/js/`, `src/favicon/`, `src/fonts/`.
- Build config if still valid: `package.json`, `package-lock.json`, `gulpfile.js`.
- Font Awesome build/bootstrap infrastructure if valid: approved source policy, local vendor delivery pattern, `css/` to `webfonts/` path relationship, real `woff2` / `woff` delivery, and build-copy logic.
- Base layout partials only if they are revalidated against the next run's clean-start boundary.

## 4. MUST BE RESET

The following should be deleted, replaced, or re-created during the future reset only after explicit cleanup approval:

- Reconstructed section HTML from the prior run.
- Reconstructed section SCSS from the prior run.
- Temporary crops under reconstruction asset folders.
- Local positioning hacks.
- Old continuity fixes.
- Stale overlays.
- Stale spacing tweaks.
- Stale responsive patches.
- Temporary FA choices or icon approximations.
- Arbitrary section-level icon guesses, placeholder icon decisions, and icon choices not revalidated by semantic meaning.
- Generated `dist/` output after source reset, via rebuild rather than hand editing.

## 5. Stale Reconstruction Definition

Stale reconstruction includes any implementation artifact created to approximate V1 before the next full run authority is re-opened:

- `src/partials/sections/equipment-prices.html`
- `src/partials/sections/trust-reviews.html`
- `src/partials/sections/faq.html`
- `src/partials/sections/final-contact-footer.html`
- `_equipment-prices.scss`
- `_trust-reviews.scss`
- `_faq.scss`
- `_final-contact-footer.scss`
- Temporary reconstruction PNG crops.
- Any import/include that keeps these sections reachable.

Screen 01 is not automatically approved for reuse. It may survive as a reference baseline only if the next run explicitly keeps it.

## 6. Reusable Authority

Reusable authority is evidence, not prior implementation convenience:

- `projects/triumph-manipulator-landing/design/v1/01.png`
- `projects/triumph-manipulator-landing/design/v1/02.png`
- `projects/triumph-manipulator-landing/design/v1/03.png`
- `projects/triumph-manipulator-landing/design/v1/04.png`
- `projects/triumph-manipulator-landing/design/v1/full.png`
- `projects/triumph-manipulator-landing/design/frontend-section-map.md`
- `projects/triumph-manipulator-landing/design/mockups-index.md`
- `projects/triumph-manipulator-landing/design/shared-assets/`
- V4 docs that document source boundaries, asset boundaries, execution boundaries, and reset boundaries.

## 7. Forbidden Carry-Over

Forbidden carry-over for the next full reconstruction:

- V2 code, V2 SCSS, V2 DOM, V2 section names used as implementation source.
- V3 code, V3 SCSS, V3 DOM, V3 crops, V3 hero/background hacks.
- Current V4 reconstructed sections as source authority.
- Current V4 temporary crops as approved standalone assets.
- Old continuity fixes as default spacing law.
- Any overlay that duplicates baked image annotations.
- Any Font Awesome or icon choice not revalidated by semantic meaning.
- Any reset that removes valid FA bootstrap infrastructure while preserving only temporary section icon choices.
- Any footer sizing assumption not tied to page role/context.

## 7.1 Font Awesome Reset Boundary

For the next clean rerun, FA readiness must survive as build/bootstrap infrastructure, while section-level temporary icon choices may reset.

Survive:

- approved FA source policy: `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`;
- local vendor delivery pattern if valid;
- build-copy logic if valid;
- real `woff2` / `woff` delivery and intact `css/` to `webfonts/` path relationship.

Reset:

- arbitrary temporary icon choices;
- section-specific icon guesses;
- placeholder icon decisions;
- any icon selected by visual approximation rather than semantic meaning.

## 8. Reset Sequence For Future Task

When the user explicitly authorizes cleanup:

1. Confirm git status and isolate unrelated user changes.
2. List active V4 source files and classify each as survive/reset/unknown.
3. Remove or detach stale section includes and SCSS imports.
4. Remove stale temporary reconstruction assets if explicitly authorized.
5. Preserve docs and approved shared assets.
6. Rebuild only after new source implementation exists.
7. Run contamination, asset, NBSP, iconography, rhythm/cadence, overlay/focal, and footer-context QA.

## 9. SAFE UNKNOWN

- Whether current Screen 01 should survive the next run is a human decision, not automatic.
- Whether `hero-bg-final.png` remains approved for future use depends on documented source lineage and next-run source audit.
- Exact cleanup list may change if new files are created before reset is authorized.
- Current `dist/` output is generated and should not be hand-edited; exact deletion/regeneration timing depends on the future task.
