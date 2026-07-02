# FP-0002 V9-04 Forge Authority Hierarchy v1

**Date:** 2026-07-02 | **Phase:** V9-04

## Ordered authority (highest first)

1. **Operator decisions** — visual approval, legal approval, production launch gates.
2. **Stable V9 tag** — `fp-0002-v9-operator-approved-static-frontend-stable-01` @ commit `a51376872fbfefb7d5f68a58b440c726d6cf3de3`.
3. **V9 `dist/`** — rendered visual/runtime behavior authority (modal timing, spacing, responsive output).
4. **V9 `src/`** — editable implementation structure (partials, SCSS, JS hooks).
5. **V9 route manifest** — `tools/v9-route-manifest.json` (31 published routes).
6. **V9 stable documentation** — `FP-0002-V9-FORGE-READINESS-NOTES-v1.md`, motion/modal/scroll contracts.
7. **This intake pack** — `forge-intake/**` (V9-04).
8. **Forge WordPress capability contracts** — `projects/mars-website-factory/subsystems/forge-wordpress/**`.
9. **Historical V8/V7 documents** — only where not superseded by V9.

## Non-authoritative (explicit exclusions)

| Item | Reason |
|------|--------|
| Rejected V9 07C-B static package | Failed nested asset paths — `SUPERSEDED_FAILED_STATIC_PACKAGING` |
| V9-03D / V9-03E modal runtimes | Superseded by V9-03F Triumph-derived runtime |
| Preloader implementation | Removed — must not be recreated |
| O-Centre G6 (`data-inf-group="g6"`) | Intentionally absent |
| Genotyping route `/uslugi/genotipirovanie/` | `NOT_PUBLISHED_IN_FRONTEND` |
| Triumph Manipulator **visual design** | Runtime reference only — Shpigovsky visuals remain V9 authority |
| C:/D:/E: historical paths | Recovery evidence only — not operational targets |
| V8 as implementation default | Superseded by V9 stable baseline |

## Implementation constraint

Forge must not reinterpret approved visuals. When intake text conflicts with `dist/`, **stop** and escalate — do not patch product source in implementation planning.
