# Legacy / unused partials (quarantine staging)

**Status:** documentation only (2026-05-28). No files moved in canonicalization pass.

## Purpose

This folder is reserved for **fully inactive** HTML partials that are:

- not in the `index.html` include closure,
- not referenced by build,
- not required as rollout scaffolds.

## Do not move here

- `src/partials/sections/v5-ppc/*` scaffold folders (11 remaining pages depend on them).
- Any partial marked **risky-remove** in `projects/triumph-manipulator-landing/V6-LEGACY-AND-DEAD-AUDIT.md`.

## First quarantine candidates (human review required)

V2/V3 root orphans under `src/partials/sections/` (non-`v5-page01`, non-`v5-ppc`) and V2 `partials/layout/head.html` / `header.html` / `scripts.html`.

See project audit doc before moving files.
