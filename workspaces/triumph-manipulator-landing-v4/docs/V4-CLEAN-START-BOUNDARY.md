# Triumph Manipulator Landing V4 - Clean Start Boundary

**Status:** boundary document only.  
**No files are authorized for deletion by this document alone.**

## 1. Clean Start Definition

A clean V4 restart means the next reconstruction run starts from source authority and governed structure, not from prior approximation artifacts.

Clean start does not mean deleting the workspace blindly. It means separating:

- reusable authority;
- valid scaffolding;
- stale reconstruction;
- temporary assets;
- forbidden carry-over;
- unknown ownership.

## 2. Survive Boundary

The following may survive:

| Category | Boundary |
|----------|----------|
| Governance docs | Keep V4 docs unless a future task supersedes them. |
| Approved shared assets | Keep copies that match `design/shared-assets/` and are still required. |
| Approved background assets | Keep only if source lineage and approval remain documented. |
| Clean project structure | Keep source directories and build conventions. |
| Build config | Keep `gulpfile.js`, package files, and build scripts if still valid. |
| Font Awesome bootstrap infrastructure | Keep approved FA source policy, valid local vendor delivery pattern, valid build-copy logic, real `woff2` / `woff` delivery, and intact `css/` to `webfonts/` paths. |
| Layout scaffolding | Keep only after revalidation against clean-start source authority. |

## 3. Reset Boundary

The following are reset candidates:

| Category | Examples |
|----------|----------|
| Reconstructed section HTML | Prior run section partials, includes, local wrappers. |
| Reconstructed SCSS | Prior run section modules, imports, local overrides. |
| Temporary crops | Any reconstruction PNG created from source screenshots. |
| Positioning hacks | Background-position nudges, focal patches, hardcoded offsets. |
| Continuity fixes | Old spacing/rhythm patches created for the prior run. |
| Stale overlays | Scrims, gradients, labels, annotation overlays without current authority. |
| Responsive patches | Breakpoint-specific fixes created to rescue prior implementation. |
| Temporary FA/icon choices | Icons not revalidated against semantic iconography governance. |
| Section icon guesses | Arbitrary temporary icon choices, placeholder icon decisions, or visual-approximation FA selections. |

Reset candidate does not mean delete immediately. It means the artifact cannot serve as source authority for the next run.

## 4. Stale Reconstruction Criteria

An artifact is stale reconstruction when at least one is true:

- It was produced during the previous V4 full reconstruction attempt.
- It approximates V1 from raster source but was not approved as final source truth.
- It depends on temporary crops or local visual fixes.
- It encodes section spacing, overlay, focal point, footer sizing, or icon choices that have not been revalidated under the new governance lessons.
- It makes a section reachable through includes/imports after its source authority was reopened.

## 5. Reusable Authority Criteria

An artifact is reusable authority when:

- It comes from the primary V1 source set.
- It comes from approved `shared-assets/`.
- It documents governance, boundaries, source audit, or reset intent.
- It is build scaffolding and does not impose visual/semantic source decisions.
- It is valid Font Awesome build/bootstrap infrastructure rather than a section-level icon guess.
- Its lineage is documented and not derived from V2/V3 or stale V4 implementation.

## 6. Forbidden Carry-Over Criteria

Forbidden carry-over includes:

- V2/V3 implementation code or styles.
- V2/V3 assets used as substitutes for V1/shared-assets authority.
- Prior V4 sections reused because they are convenient.
- Temporary crops promoted to approved assets.
- Old overlay/focal/spacing/footer/icon decisions reused without explicit revalidation.
- Baked image annotations duplicated as DOM overlays.
- Footer expansion or compactness chosen by absolutism instead of context.
- Random Font Awesome usage or semantically weak icon carry-over.
- Removing valid FA startup/build delivery while keeping arbitrary temporary icon choices.

## 7. Clean Start Preflight

Before a future reconstruction begins:

- Confirm source paths exist.
- Confirm section order from `full.png`, `mockups-index.md`, and section map.
- Confirm approved assets and temporary asset boundaries.
- Confirm FA readiness survives as infrastructure when valid: approved source policy, local vendor delivery, build-copy logic, `woff2` / `woff`, and `css/` to `webfonts/` paths.
- Classify current V4 files as survive/reset/unknown.
- Confirm no V2/V3 implementation contamination.
- Confirm rhythm/cadence, transition continuity, footer context, iconography, overlay balance, and focal-point governance will be reviewed.
- Confirm PowerShell-safe validation commands.

## 8. Not Authorized

This document does not authorize:

- deleting files;
- moving files;
- wiping implementation;
- rebuilding landing sections;
- creating V5;
- treating the current V4 implementation as failed production output;
- claiming a reset has already happened.

## 9. SAFE UNKNOWN

- Exact deletion list remains unknown until the future reset task is authorized.
- Exact reusable status of current Screen 01 remains unknown until the next run explicitly decides it.
- Exact approved status of any local background or crop asset remains unknown unless lineage is documented and accepted.
- Exact responsive reset needs remain unknown until current implementation is classified and new source audit is completed.
