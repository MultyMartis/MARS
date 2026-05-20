# Static prototype readiness checklist v0.1

**Назначение:** gate для Phase 4 — первый **HTML wireframe prototype** в `workspaces/homegateway-v4-ai/` (workspace **не создан** в v0.1 pack).

**Prerequisite docs:** wireframe pack + [theme-system-draft-v0.1.md](../theme-system-draft-v0.1.md) + [block-screen-taxonomy-v0.1.md](../block-screen-taxonomy-v0.1.md)

---

## Charter boundary

| Allowed | Forbidden |
|---------|-----------|
| Static HTML / SCSS / JS | Backend, API, auth server |
| Sample / demo data | Secrets, tokens, real credentials |
| Gulp-style build (if aligned MARS frontend) | mars-runtime edits |
| Display-only MARS/bot blocks | Control plane / orchestration UI |
| Admin-aware markup | Working admin CRUD |
| Overlay system mock | Real integrations |

---

## Workspace (future)

**Path (recommended):** `workspaces/homegateway-v4-ai/`

**Status:** **NOT CREATED** — human charter before mkdir.

| Expected top-level | Purpose |
|--------------------|---------|
| `src/` or `app/` | HTML templates, SCSS, JS |
| `data/` | Sample JSON (no secrets) |
| `dist/` | Build output (generated — do not hand-edit) |
| `gulpfile.js` or `package.json` | Build — align with MARS Gulp frontend lane if chartered |

---

## Files needed (draft tree)

```text
workspaces/homegateway-v4-ai/
├── index.html              # login mock
├── cockpit.html            # OR single-page with view sections
├── src/
│   ├── scss/
│   │   ├── _tokens.scss
│   │   ├── _shell.scss
│   │   ├── _zones.scss
│   │   ├── _block-screen.scss
│   │   ├── _signals.scss
│   │   ├── _overlay.scss
│   │   ├── _views/
│   │   │   ├── _main.scss
│   │   │   ├── _systems.scss
│   │   │   ├── _focus.scss
│   │   │   └── _tactical.scss
│   │   └── main.scss
│   └── js/
│       ├── view-switch.js
│       ├── overlay.js
│       ├── theme.js
│       └── clipboard-mock.js
├── data/
│   ├── sample-clients.json
│   ├── sample-deadlines.json
│   ├── sample-systems.json
│   └── sample-leads.json
└── README.md               # local run instructions
```

**Minimum views in first prototype:** Main + Systems + Focus (+ Tactical rail on Main).

---

## Components needed (logical)

| Component | CSS class / hook | Wireframe source |
|-----------|------------------|------------------|
| Shell | `.hg-shell` | [navigation-shell-wireframe-v0.1.md](navigation-shell-wireframe-v0.1.md) |
| Top command | `.hg-zone--top` | all |
| Mode nav | `.hg-zone--nav` | navigation-shell |
| Canvas | `.hg-zone--canvas` | per view |
| Signal rail | `.hg-zone--rail` | main-cockpit |
| Bottom strip | `.hg-zone--strip` | main-cockpit |
| Block-screen | `.hg-block-screen` | block-screen-taxonomy |
| Signal row | `.hg-signal-row` | tactical-signals |
| Overlay host | `#hg-overlay-host` | overlay-and-popup |
| View container | `[data-hg-view]` | each view doc |

---

## SCSS architecture notes

1. **Tokens first** — `data-theme="dark|light"` on `:root`; import [theme-system-draft](../theme-system-draft-v0.1.md) semantic names only.
2. **No hardcoded hex** in components (except token definitions file).
3. **Zones before blocks** — layout shell grid independent of block internals.
4. **Signal levels** — modifiers `.hg-signal--overdue`, etc. map to tokens.
5. **Density** — `data-hg-density` on body scopes spacing scale (calm/standard/high).
6. **BEM-lite** — `.hg-block-screen`, `.hg-block-screen__header` — match taxonomy `data-hg-module-id`.

---

## JS behavior notes (mock only)

| Module | Behavior |
|--------|----------|
| `view-switch.js` | Toggle `[data-hg-view]` sections; update nav `aria-current` |
| `overlay.js` | Open/close by `data-hg-open-overlay`; stack rules |
| `theme.js` | Toggle `data-theme`; optional localStorage |
| `clipboard-mock.js` | `navigator.clipboard` or fallback alert |
| Login mock | Form → show cockpit (preventDefault) |

**No:** fetch to APIs, WebSocket, n8n triggers.

---

## Markup conventions (admin-aware)

Per [admin-entry-and-future-crud-notes-v0.1.md](../admin-entry-and-future-crud-notes-v0.1.md):

- `data-hg-module-id="hg-client-list"`
- `data-hg-entity="client"` / `data-hg-entity-id="sample-acme"`
- `data-hg-signal-level="overdue"`
- `data-hg-display-only="true"` on MARS/bot
- `data-hg-editable="false"` v0.1 static

---

## Responsive risks

| Risk | Check |
|------|-------|
| Rail overflow on tablet | Test 1024px; collapse to drawer |
| Grid too many columns | Systems grid → 2 col on medium |
| Overlay sheet 40% too narrow on mobile | Full width <768px |
| Sticky strip covers content | `padding-bottom` on canvas |
| Font scale breaks glass | Min 14px body |

---

## Overflow risks

| Area | Mitigation |
|------|------------|
| Tactical list | Virtual scroll future; wireframe: max-height + scroll |
| Signal rail | Cap height 40vh |
| Link hubs | «Show more» expand |
| Systems grid | Paginate or 2-row limit in calm density |

---

## Accessibility basics (Phase 4 minimum)

- [ ] `lang` on `<html>`
- [ ] Skip link to canvas
- [ ] Focus visible on nav and overlays
- [ ] `role="dialog"` + `aria-modal` on overlays
- [ ] Signal level not color-only (icon or text)
- [ ] Contrast check on signal tokens (Phase 3)
- [ ] Keyboard Esc closes overlay

---

## Security / honesty

- [ ] No `.env` in repo
- [ ] Sample clipboard strings — no API keys
- [ ] Label «sample data» in footer or settings
- [ ] MARS blocks: «display-only» visible
- [ ] No claim of live status in UI copy without integration

---

## Wireframe pack completion gate

Before opening workspace:

- [x] Main cockpit wireframe doc
- [x] Systems monitor wireframe doc
- [x] Focus workspace wireframe doc
- [x] Tactical signals wireframe doc
- [x] Navigation shell wireframe doc
- [x] Overlay behavior doc
- [x] Density experiments in pack master
- [ ] Human charter for workspace folder
- [ ] Operator sign-off on HTML-first vs Figma

---

## Recommended build order (Phase 4)

1. Tokens + shell HTML (empty zones)
2. Main view blocks with sample JSON
3. Overlay project panel
4. Theme toggle
5. Systems view grid
6. Focus view
7. Tactical view + rail on Main
8. Login mock flow
9. Admin stub
10. Responsive pass

---

## SAFE UNKNOWN

- Gulp vs Vite — align with `agents/frontend-gulp-agent` when workspace chartered.
- Single vs multi HTML entry — see navigation-shell recommendation.
- CI for workspace — out of scope.

---

*Last updated: 2026-05-20.*
