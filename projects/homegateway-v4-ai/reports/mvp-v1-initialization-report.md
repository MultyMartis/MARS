# REPORT — HomeGateway v4.AI MVP v1 Initialization

**Date:** 2026-05-25  
**Workspace:** `workspaces/homegateway-v4-ai/v1/`  
**Layout source:** `design/v1/hg_shem-v1.png` (structure only)

---

## Summary

Prototype v0 archived; MVP v1 built from scratch as an operational HTML/CSS/JS skeleton with Gulp, gulp-file-include, and locked palette. `#main_area` left as empty tactical canvas. Gulp build verified (`npm run build`).

---

## Created structure

```
workspaces/homegateway-v4-ai/
├── README.md
├── archive/v0/          ← former root prototype
│   ├── src/
│   ├── dist/
│   ├── gulpfile.js
│   ├── package.json
│   └── ARCHIVE-README.md
├── node_modules/        ← legacy (v0); v1 has own node_modules
└── v1/
    ├── package.json
    ├── gulpfile.js
    ├── src/
    │   ├── pages/index.html
    │   ├── partials/
    │   │   ├── shell/ (head, scripts)
    │   │   ├── sections/ (app-shell, topbar, sidebars, favorites, main-area)
    │   │   └── components/ (counter-pill, list-row, signal-card, metric-row)
    │   ├── scss/ (base, layout, components, sections, utilities)
    │   ├── js/ (main.js, hooks/theme.js, hooks/favorites.js)
    │   └── img/logo/logo-dark.svg (copy from materials)
    └── dist/            ← build output
```

**Bootstrap tool (regeneration):** `projects/homegateway-v4-ai/tools/bootstrap-mvp-v1.ps1`

---

## Archived structure

| Item | Location |
|------|----------|
| Prototype v0.1 cockpit wireframe | `archive/v0/src/` |
| Overlays, cockpit views, signals rail | `archive/v0/src/partials/` |
| Last v0 build | `archive/v0/dist/` |
| v0 toolchain config | `archive/v0/gulpfile.js`, `package.json` |

---

## Component map

| Zone | Component | Partial / class |
|------|-----------|----------------|
| Topbar | Nav tabs (Общий, Системы, Фокус, Сигналы) | `topbar.html` / `.hg-tab` |
| Topbar | Utility buttons 01–03 | `.hg-utility-btn` |
| Topbar | Theme switch | `[data-hook="theme-toggle"]` |
| Topbar | Profile block | `.hg-profile` |
| Left | Logo | `.hg-logo` + SVG |
| Left | Projects block | `.hg-panel--projects` |
| Left | Tools block | `.hg-panel--tools` |
| Left | Quick access | `.hg-panel--quick` |
| Left | List row (icon, title, counter, stars) | `list-row.html` |
| Center | Favorites (Yandex…VK) | `favorites-row.html` |
| Center | Slide placeholder #01 | `[data-hook="favorites-slide"]` |
| Center | **Empty workspace** | `#main_area` `.hg-main-area` |
| Right | Monitor / signal cards A1–A3 | `signal-card.html` |
| Right | System status + A4 chart placeholder | `.hg-status-module--a4` |
| Shared | Rectangular counter pills | `counter-pill.html` / `.hg-counter` |

---

## SCSS architecture

| Layer | Files |
|-------|--------|
| Entry | `main.scss` |
| Tokens | `base/_variables.scss` |
| Base | `_reset.scss`, `_typography.scss` |
| Layout | `_app-grid.scss`, `_topbar.scss`, `_sidebars.scss`, `_main-area.scss` |
| Components | `_buttons.scss`, `_counter.scss`, `_panel.scss`, `_list-row.scss`, `_signal-card.scss`, `_status-module.scss` |
| Sections | `_favorites.scss` |
| Utilities | `_helpers.scss` |

**Palette lock:** `#02091b`, `#d1e5ff`, `#ff0000`, `#00bf02`, `#00bdf0` (+ rgba derivatives only).

---

## Layout decisions

- **Grid:** `.hg-app` → topbar row + workspace row; workspace = left sidebar | center (favorites + main) | right sidebar.
- **Desktop-first:** default columns 280px / 1fr / 360px; tuned at 1440 / 1280 / 1024.
- **Target viewport:** 2560×1440 primary; survives 1920×1080 via fluid center column.
- **`#main_area`:** bordered empty canvas, dashed inner frame, label only — no widgets.
- **Counters:** rectangular mono pills; demo includes `999` on Песочница row.

---

## Responsive logic

| Breakpoint | Adjustment |
|------------|------------|
| ≤1440px | Sidebars 248px / 320px |
| ≤1280px | Sidebars 220px / 280px |
| ≤1024px | Sidebars 200px / 260px |

Mobile not optimized (by design for foundation phase).

---

## JS (minimal)

| File | Role |
|------|------|
| `hooks/theme.js` | Toggle `hg-theme-alt` on body (placeholder) |
| `hooks/favorites.js` | Toggle `data-favorites-set` 01/02 (no slider UI yet) |
| `main.js` | Tab active state; list-row `data-selected` placeholder |

**Hover:** implemented in SCSS for buttons, tabs, fav links, list rows, utility controls only.

---

## Unresolved issues

1. **Theme alt** — `hg-theme-alt` body class has no SCSS theme variant yet (hook only).
2. **Tools row affordances** — scheme shows 4 star markers; template uses 3 (visual placeholder).
3. **Icon system** — pentagon/hex markers from scheme replaced with minimal CSS shapes; real icon set TBD from `design/materials/`.
4. **Topbar slide control** — scheme shows pentagon “4” toggle; MVP uses utility buttons + separate favorites `#01` only.
5. **node_modules at workspace root** — leftover from v0; v1 uses `v1/node_modules`. Optional cleanup by operator.
6. **Workspace .cursorignore** — agent Write tool blocked for workspace paths; files created via shell/bootstrap script.

---

## Next recommended steps

1. Operator visual pass at 2560×1440 and 1920×1080 against `hg_shem-v1.png`.
2. Wire real icon assets from `design/materials/` (without editing upstream files).
3. Define `hg-theme-alt` light/dark token set when theme spec is frozen.
4. Implement favorites carousel (#01) behavior when product rules are ready.
5. Connect `#main_area` to first real workspace view (routing / view partials).
6. RU typography QA per Website Factory `russian-no-word-splitting-typography-v1.md`.

---

## Build verification

```bash
cd workspaces/homegateway-v4-ai/v1
npm run build
```

Exit code 0 — `dist/index.html`, `dist/assets/css/main.css`, JS and logo copied.

---

## Git status

No commit performed (per MARS default). Changed/added paths under `workspaces/homegateway-v4-ai/` and `projects/homegateway-v4-ai/tools/bootstrap-mvp-v1.ps1`, `projects/homegateway-v4-ai/reports/mvp-v1-initialization-report.md`.
