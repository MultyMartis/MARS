# Triumph Manipulator Landing V4 — Execution Boundaries

## 1. Purpose

This document defines execution boundaries for the V4 clean reconstruction battle test.

V4 is documentation-first, human-supervised, and methodology-bound. It does not prove production readiness, pixel-perfect fidelity, autonomous reconstruction, perfect responsive accuracy, or runtime intelligence.

## 2. Clean-Start Rule

V4 is not a continuation of V3.

Forbidden as authority:

- V3 partials.
- V3 SCSS.
- V3 DOM.
- V3 layout fixes.
- V3 hero hacks.
- V3 responsive patches.
- V3 reconstruction assets.
- V3 crops.
- V3 local overrides.

Allowed V3 use:

- Governance lesson source.
- Drift-history source.
- Anti-pattern evidence.
- Reconstruction failure history.

## 3. Source Authority Boundary

Primary:

- `projects/triumph-manipulator-landing/design/v1/`
- `projects/triumph-manipulator-landing/design/mockups-index.md`
- `projects/triumph-manipulator-landing/design/frontend-section-map.md` only as V1 continuity context.

Approved asset candidates:

- `projects/triumph-manipulator-landing/design/shared-assets/`

Governance:

- Forge governance layers guide evidence discipline, survivability, escalation, and review scaling.

## 4. Header Boundary

Critical invariant:

**HEADER != HERO != SLIDER**

V4 must separately define:

- Header system.
- First-screen shell.
- Hero content system.
- Hero background ownership.
- Future slider possibility.
- Mobile header ownership.
- Navigation survivability.

No implementation may collapse these into one patch-driven hero block unless source evidence and human review explicitly approve that structure.

## 5. Russian Typography Boundary

Russian typography survivability is mandatory in future HTML.

Use `&nbsp;` in required cases, including:

- `в&nbsp;Краснодаре`
- `с&nbsp;НДС`
- `от&nbsp;30&nbsp;минут`
- `и&nbsp;т.д.`
- `для&nbsp;юр.&nbsp;лиц`

This rule applies during source copy transfer and implementation, not only final polish.

## 6. Asset Boundary

Approved existing assets must be used as-is.

Forbidden without documented reason:

- Rename.
- Recompression.
- Resize.
- Derived replacement.
- Silent crop.
- Substitution from V3.
- Decorative replacement from outside the approved source set.

Derived asset creation requires documented lineage, dimensions, transformation reason, and human-supervised approval.

## 7. Background Content Ownership and Baked Annotations

Approved background/image assets own all visible content already baked into their pixels.

If labels, callouts, numbers, arrows, technical marks, or annotations are baked into an approved background/image asset:

- Do not duplicate them as HTML/CSS overlay.
- Do not reconstruct them as separate decorative DOM when they already exist in the source image.
- Do not use overlay annotations to imply source structure that is not independently proven.

HTML annotations are allowed only when:

- The source clearly shows annotations as independent UI/text elements.
- They are not already baked into the image.
- They are needed for accessibility/content reasons.
- The decision is documented.

For V4 Screen 01, background annotations are baked into `hero-bg-final.png`; they belong to the background asset and must not be duplicated by `hero-screen-01__annotations` or equivalent overlay classes.

## 8. Scope Boundary for This Task

Allowed in this task:

- Workspace initialization.
- Required documentation.
- Source authority audit.
- Shared asset mapping.
- First-screen decomposition planning.
- Section language planning.
- Shell-safe validation.

Forbidden in this task:

- Full implementation.
- Hero rebuild.
- Screen 02 rebuild.
- Section marathon.
- Production readiness claim.
- Pixel-perfect claim.
- Responsive accuracy claim.
- Runtime/autonomous intelligence claim.

## 9. Contamination Prevention

Before future implementation:

- Search V4 workspace for V3 path references.
- Search V4 workspace for V3 class/partial inheritance if any code appears.
- Confirm no V3 assets were copied.
- Confirm no V3 local overrides were recreated.
- Treat any V3 solution memory as a risk signal, not as authority.

## 10. Stop Conditions

Stop and mark SAFE UNKNOWN when:

- V1 source files are unavailable.
- V1 pixels cannot confirm a structural choice.
- Header/hero/slider ownership is ambiguous.
- A required asset is missing.
- A responsive decision would change hierarchy.
- A copy decision would invent or alter commercial meaning.
- V3 or V2 implementation convenience begins answering unresolved V1 questions.
- Background/image-baked content ownership is ambiguous.

## 11. Shell-Safe Execution

Validation and setup commands must be PowerShell-compatible.

Forbidden:

- Bash-only syntax.
- Assumed Unix utilities for critical validation.
- Copy/paste command chains that are not Windows-safe.

Preferred:

- `Get-ChildItem`
- `Select-String`
- `Test-Path`
- `git diff --check`
- Package manager commands only after the workspace stack exists.

## 12. Current SAFE UNKNOWN

- V1 raster files were not confirmed by file search during this planning pass.
- Exact build stack for V4 is not initialized.
- Exact section semantics, copy locks, and responsive behavior remain pending V1 raster inspection.
