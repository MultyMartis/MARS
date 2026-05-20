# Triumph Manipulator Landing V3

Clean Forge rebuild workspace for `triumph-manipulator-landing-v3`.

## Status

Initialization and execution readiness only.

This workspace does not yet contain rebuilt V1 sections, visual tuning, responsive reconstruction, QA evidence, freeze state, or production-readiness proof.

## Source Authority

Primary rebuild authority is locked in `docs/V3-SOURCE-LOCK.md`.

V3 rebuild work must start from the V1 source exports under `projects/triumph-manipulator-landing/design/v1/` and must not inherit V2 implementation code.

## Structure

- `src/pages/`: page entries.
- `src/partials/layout/`: document shell includes.
- `src/partials/sections/`: future source-derived section includes.
- `src/partials/components/`: future reusable include fragments.
- `src/scss/`: SCSS entry and modules.
- `src/js/`: JavaScript entry points.
- `src/assets/`: approved implementation assets only.
- `dist/`: generated build output; do not hand-edit.
- `docs/`: V3 execution documentation.

## Commands

```bash
npm install
npm run build
npm run watch
```

Dependency installation has not been run during initialization.

## Boundary

Do not rebuild sections, import V2 code, or claim fidelity until the next execution phase explicitly authorizes implementation scope.
