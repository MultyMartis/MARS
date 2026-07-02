# FP-0002 Shpigovsky — V9 Frontend Workspace

**Status:** `FP0002_V9_OPERATOR_APPROVED_STATIC_FRONTEND_STABLE_BASELINE_COMPLETE`  
**Phase:** V9-03 stable baseline — operator-approved static frontend frozen in Git  
**Authority:** Current canonical static frontend (V8 remains historical approved baseline)

## Build

```bash
npm install
npm run build
npm run validate
npm run preview
```

- **`src/`** — canonical source
- **`dist/`** — generated clean-route static site (operator review target)
- **`tools/v9-route-manifest.json`** — route authority for build and future Forge intake

## Preview

After build: `npm run preview` → default **http://127.0.0.1:8791/** (V9-03G review server: **http://127.0.0.1:8797/**)

## Stable baseline (V9-03)

- Operator-approved V9-03G static frontend frozen in Git
- Tag: `fp-0002-v9-operator-approved-static-frontend-stable-01`
- See `FP-0002-V9-OPERATOR-APPROVED-STATIC-FRONTEND-STABLE-01-MANIFEST.md`
- Recovery ZIP: `X:\AI MARS STORAGE\website-factory\fp-0002-shpigovsky-v9\v9-03-stable-baseline-checkpoint\`

## V9-03G (operator approved)

- Operator-approved V9-03F state backed up before edits
- Shared scroll-to-top control on all 31 routes
- See `REPORT-FP-0002-V9-PHASE-03G-SCROLL-TO-TOP-v1.md`

## V9-03F (approved)

- Triumph-derived consultation modal runtime — operator visually approved
- See `REPORT-FP-0002-V9-PHASE-03F-TRIUMPH-MODAL-MIGRATION-v1.md`

## V9-03C (approved)

- V9-03B motion state backed up to Storage
- O-Centre obsolete mobile G6 block removed from source
- See `REPORT-FP-0002-V9-PHASE-03C-O-CENTRE-G6-REMOVAL-v1.md`

## V9-03B corrections (operator approved)

- Button hover: color-only (~0.3s), no lift/scale
- Modal: open + close animation with fallback timeout
- Gallery: Fancybox fade in/out + carousel fade
- Preloader: opaque white `#ffffff`; coordinated page shell fade-in
- See `REPORT-FP-0002-V9-PHASE-03B-MOTION-CORRECTION-v1.md`

## V9-03A additions (carried)

- Calm motion tokens (`--motion-base` ≈ 0.3s)
- Scroll reveal (`data-reveal`, IntersectionObserver)
- ZPM-adapted session preloader (logo + line, fail-safe 3s)
- `prefers-reduced-motion` support
- See `FP-0002-V9-MOTION-SYSTEM-v1.md`

## V9-02 additions

- Four full legal pages (`LEGAL_DEMO_DOCUMENT`) with `[ДЕМО: ...]` tokens
- Internal link audit complete — all meaningful navigation resolves
- See `FP-0002-V9-*-v1.md` documentation in this workspace

## Notes

- Phase 07C-B Storage static package is **superseded** — do not use for Forge or client delivery
- `/uslugi/genotipirovanie/` is **not published** in V9 (`NOT_PUBLISHED_IN_FRONTEND`)
- Canonical top-level dependencies route: `/uslugi/zavisimosti/` (label: **Зависимости**)
- `FORM_MODE=STATIC_DEMO_NO_BACKEND` — forms do not submit
- **No git checkpoint** until operator visual approval

See `foundation/FP-0002-V9-OPERATIONAL-STATUS.md` and `V9-MIGRATION-MANIFEST.md`.
