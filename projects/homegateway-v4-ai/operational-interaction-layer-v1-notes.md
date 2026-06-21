# Operational Interaction Layer v1 — implementation notes

**Date:** 2026-05-25  
**Workspace:** `workspaces/homegateway-v4-ai/v1/`  
**Archive:** `workspaces/homegateway-v4-ai/archive/v1.3-operational-interaction-prepass/`

## What was implemented

1. **Font Awesome Pro 5.15.4** wired from MARS shared library (gulp copy → `dist/assets/vendor/fontawesome/`).
2. **Semantic utility controls** — Profile, Settings, About system, Theme toggle (icon-only, `title` / `aria-label`).
3. **Operational telemetry** — four indicators per project/tool row (entities, problems, active tasks, completed).
4. **Navigation icons** — duotone FA on list rows by domain (`project`, `systems`, `processes`, `robots`, `wiki`).
5. **Favorites structure** — icon zone, text zone, hover external-open placeholder; star icon pagination control.
6. **Monitor cards** — A1/A2/A3 semantic duotone icons in indicator column.
7. **Status A4** — `fa-heartbeat` aggregate health semantics; metric row icons.
8. **Canonical map** — `icon-and-indicator-map-v0.1.md`.

## Placeholder semantics

| Area | Current state | Not in this pass |
|------|---------------|-------------------|
| Utility buttons | Click hooks preserved; no panels/routes | Real profile/settings/about modals |
| Telemetry values | Static demo integers in HTML includes | Live API / WebSocket feeds |
| Favorites icons | `fa-star` in `data-slot="fav-icon"` | Custom per-site SVG |
| Favorites external action | Hover-only visual placeholder | Separate navigation handler |
| A4 chart bars | Retained minimal bars + health index | Dynamic charting |

## Future: custom SVG favorites

- `hg-fav-btn__icon-zone[data-slot="fav-icon"]` accepts inline `<svg>` or `<img>` without layout change.
- Remove `hg-fav-btn__icon-placeholder` class when SVG assets land.
- Keep text and action zones stable for rhythm (50px height row in favorites band).

## Future: dynamic loading

- Telemetry partial accepts `entities`, `problems`, `active`, `completed` via file-include context.
- Rows expose `data-telemetry-*` attributes for JS hydration.
- Panel head counters remain separate aggregate placeholders.

## Future: pagination logic

- `data-hook="favorites-slide"` reserved for page index.
- No animation in v1; structure supports `aria-label` page description and icon-only control.

## Future: operational states

- Telemetry items: `data-state="zero|active|warn"` for problems/tasks.
- Signal cards: existing `OK|WARN|ALERT` status classes unchanged.
- Theme: `hg-theme-alt` body class via existing hook.

## Preservation checklist (verified at build)

- Exo 2, no letter-spacing hacks, no uppercase transform on new controls
- 4px radius only
- 30/20/10/5 rhythm, 50px control height
- Centered shell, empty `#main_area`
- UTF-8 Russian copy in source partials
