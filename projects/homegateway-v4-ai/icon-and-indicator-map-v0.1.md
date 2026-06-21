# Icon and indicator map v0.1

**Project:** HomeGateway v4.ai  
**Status:** Canonical semantics documentation (MVP v1)  
**Library:** Font Awesome Pro 5.15.4 — `shared/assets/icon-libraries/Font Awesome Pro 5.15.4/`  
**Style default:** Duotone (`fad`) — solid fallback only when no suitable duotone exists

---

## Navigation icons

| Entity | Meaning | FA icon | Style | Operational role | Visual priority | Future notes |
|--------|---------|---------|-------|------------------|-----------------|--------------|
| Projects (row) | Project workspace / tree | `fa-folder-tree` | duotone | Primary navigation affordance for project list | High | — |
| Systems (tool) | Layered system stack | `fa-layer-group` | duotone | Tool navigation — systems domain | High | — |
| Processes (tool) | Live process stream | `fa-stream` | duotone | Tool navigation — processes domain | High | — |
| Robots (tool) | Automation agents | `fa-robot` | duotone | Tool navigation — robots domain | High | — |
| Wiki (tool) | Documentation corpus | `fa-book-open` | duotone | Tool navigation — wiki domain | High | — |

---

## Utility icons

| Entity | Meaning | FA icon | Style | Operational role | Visual priority | Future notes |
|--------|---------|---------|-------|------------------|-----------------|--------------|
| Profile | Operator profile access | `fa-user-circle` | duotone | Topbar utility — identity | Medium | May open profile drawer |
| Settings | Workspace configuration | `fa-sliders-h` | duotone | Topbar utility — configuration | Medium | — |
| About system | Runtime / product metadata | `fa-info-circle` | duotone | Topbar utility — system info | Low | — |
| Theme toggle | Light/dark theme switch | `fa-adjust` | duotone | Topbar utility — presentation mode | Low | Icon-only; no visible text label |

---

## Project telemetry indicators

| Entity | Meaning | FA icon | Style | Operational role | Visual priority | Future notes |
|--------|---------|---------|-------|------------------|-----------------|--------------|
| Indicator 5 — entity count | Count of entities in scope | `fa-folders` | duotone | Row telemetry — inventory density | Medium | Supports 1–999 |
| Indicator 6 — active problems | Open operational problems | `fa-exclamation-triangle` | duotone | Row telemetry — risk surface | High when &gt; 0 | Warn tint when non-zero |
| Indicator 7 — active tasks | In-flight tasks | `fa-tasks` | duotone | Row telemetry — workload | Medium | — |
| Indicator 8 — completed tasks | Finished tasks | `fa-check-circle` | duotone | Row telemetry — throughput | Low | Positive tint |

---

## Tool telemetry indicators

Same four indicators as **Project telemetry** — shared component (`telemetry-group`) for Системы, Процессы, Роботы, Вики rows.

| Entity | Meaning | FA icon | Style | Operational role | Visual priority | Future notes |
|--------|---------|---------|-------|------------------|-----------------|--------------|
| Indicator 5–8 (tools) | Identical semantics to project rows | (see above) | duotone | Tool-row operational scan | Medium | Shared SCSS + partial |

---

## Favorites placeholders

| Entity | Meaning | FA icon | Style | Operational role | Visual priority | Future notes |
|--------|---------|---------|-------|------------------|-----------------|--------------|
| Fav icon slot (temporary) | Brand / site identity placeholder | `fa-star` | duotone | `data-slot="fav-icon"` until custom SVG | Low | **Replace with custom SVG** per site |
| Pagination control | Favorites page / set index | `fa-star` | duotone | Slide control — not primary navigation | Low | Future pagination animation |
| External open (hover) | Open favorite in new context | `fa-external-link-alt` | duotone | Hover-only utility action placeholder | Low | Visible on row hover only |

---

## Monitor signal icons

| Entity | Meaning | FA icon | Style | Operational role | Visual priority | Future notes |
|--------|---------|---------|-------|------------------|-----------------|--------------|
| A1 | Critical operational signal | `fa-exclamation-circle` | duotone | Monitor card — severity / attention | High | Replaces type-code-only label |
| A2 | Notification / update | `fa-bell` | duotone | Monitor card — inbound notice | Medium | — |
| A3 | Operational event | `fa-stream` | duotone | Monitor card — event stream | Medium | — |

---

## Status system icons

| Entity | Meaning | FA icon | Style | Operational role | Visual priority | Future notes |
|--------|---------|---------|-------|------------------|-----------------|--------------|
| A4 aggregate health | Runtime / system health index | `fa-heartbeat` | duotone | Status module — aggregate vitality | Medium | No graph expansion; compact module |
| Metric rows (CPU / RAM / disk) | Resource telemetry | `fa-microchip`, `fa-memory`, `fa-hdd` | duotone | Inline metric affordance | Low | Per-metric mapping in partial |

---

## Implementation reference

- Markup: `workspaces/homegateway-v4-ai/v1/src/partials/`
- Styles: `src/scss/components/_icons.scss`, `_telemetry.scss`
- Build copies FA from MARS shared library into `dist/assets/vendor/fontawesome/`
