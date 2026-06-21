# REPORT — HomeGateway v4.ai MVP v1 Stabilization

**Date:** 2026-05-25  
**Workspace:** `workspaces/homegateway-v4-ai/v1/`  
**Task:** Source audit, UTF-8 repair, schema alignment, frontend stabilization

---

## Source audit

### Found schema files

| Path | Exists | Size | Notes |
|------|--------|------|-------|
| `projects/homegateway-v4-ai/design/v1/hg_shem-v1.png` | **Yes** | 279 KB | Only layout schema PNG in repo |
| `projects/homegateway-v4-ai/design/v1/hg_shem-v2.png` | **No** | — | Not present on disk |
| `projects/homegateway-v4-ai/design/materials/logo/logo--dark theme.svg` | Yes | — | Brand asset, not layout |
| `projects/homegateway-v4-ai/design/materials/logo/logo--light-theme.svg` | Yes | — | Brand asset, not layout |

No other `hg_shem*` files found under `C:\AI MARS`.

### Actual active schema

**`design/v1/hg_shem-v1.png`** — sole layout source of truth in repository.

Per task rule: `hg_shem-v2.png` was expected as operational layout but **does not exist**. v1 remains active; no invented v2 alignment.

### Outdated references

| Location | Reference | Status |
|----------|-----------|--------|
| `workspaces/homegateway-v4-ai/v1/README.md` | `hg_shem-v1.png` | Correct (updated with audit note) |
| `projects/homegateway-v4-ai/reports/mvp-v1-initialization-report.md` | `hg_shem-v1.png` | Correct; historical init report |
| `projects/homegateway-v4-ai/tools/bootstrap-mvp-v1.ps1` | Implicit v1 layout | Correct source; **encoding execution issue** (see below) |

No in-repo references to non-existent `hg_shem-v2.png` were found.

### Fixes applied

- Confirmed structural zones match v1 schema intent: topbar, left sidebar, favorites row, empty `#main_area`, right monitor + system status.
- Monitor block titles aligned to required operational placeholders (see Structural fixes).
- Added `projects/homegateway-v4-ai/tools/repair-mvp-v1-encoding.mjs` for reliable UTF-8 HTML regeneration (Node, not PowerShell 5.1).

---

## Encoding fixes

### Root cause

Initial bootstrap via `bootstrap-mvp-v1.ps1` under **Windows PowerShell 5.1** corrupted Cyrillic in here-strings (script parsed as system ANSI, written as UTF-8 → mojibake like `Рџ`, `РЎ`, `Р°` in browser).

### Files repaired

All HTML partials and pages rewritten with UTF-8 (no BOM) via Node repair script:

- `src/partials/shell/head.html`, `scripts.html`
- `src/pages/index.html`
- `src/partials/sections/*.html` (app-shell, topbar, left-sidebar, favorites-row, main-area, right-sidebar)
- `src/partials/components/*.html` (counter-pill, list-row, signal-card, metric-row)
- `workspaces/homegateway-v4-ai/v1/README.md`

SCSS and JS were already ASCII-safe; no mojibake found there.

### Mojibake removed

Post-repair verification on `dist/index.html`:

- All 21 required Russian labels present and readable
- Mojibake pattern scan (`Р[Ѐ-Я]`) → **clean**
- `<meta charset="UTF-8">` present in head

### UTF-8 verification

```bash
node projects/homegateway-v4-ai/tools/repair-mvp-v1-encoding.mjs
cd workspaces/homegateway-v4-ai/v1 && npm run build
```

Build exit code **0**. Cyrillic labels verified in `dist/index.html` via Node UTF-8 read.

---

## Structural fixes

### Areas preserved (unchanged architecture)

| Zone | Partial | Status |
|------|---------|--------|
| Topbar | `topbar.html` | Nav tabs + utilities + profile |
| Left sidebar | `left-sidebar.html` | Logo, projects, tools, quick access |
| Favorites row | `favorites-row.html` | 5 links + `#01` slide hook |
| Main area | `main-area.html` | **Empty** — label + hint only |
| Right monitor | `right-sidebar.html` | Signal cards + log link |
| System status | `right-sidebar.html` | Metrics + A4 placeholder |

### Alignment corrections

- **Monitor titles** updated to spec placeholders:
  - «Название сигнала»
  - «Название уведомления»
  - «Название события»
- **Quick access** button: «Открыть список» (capitalized per spec)
- **Signal actions**: «Подробнее / Удалить» retained in `signal-card.html`
- **Counter `999`** on «Песочница» row preserved (rectangular pills)
- **`#main_area`**: no widgets, charts, or cards added

### Layout stabilization

- Grid shell unchanged: `.hg-app` → topbar + workspace (left | center | right)
- Palette lock unchanged: `#02091b`, `#d1e5ff`, `#ff0000`, `#00bf02`, `#00bdf0`
- `archive/v0/` untouched

---

## Build result

```text
cd workspaces/homegateway-v4-ai/v1
npm run build
→ exit 0
```

**Outputs verified:**

- `dist/index.html` — exists, UTF-8, all RU labels correct
- `dist/assets/css/main.css` — compiled
- `dist/assets/js/` — theme, favorites, main hooks
- `dist/assets/img/logo/logo-dark.svg` — copied

**Structure checks:**

- `#main_area` contains only tactical frame + placeholder text
- No mojibake in built HTML
- Viewport overflow controlled via existing grid (`overflow: hidden` on shell)

---

## Remaining issues

1. **`hg-theme-alt`** — theme toggle hook only; no alternate token set in SCSS yet.
2. **Icon placeholders** — CSS shapes, not final `design/materials/` icons.
3. **Favorites slider** — `#01` hook only; no carousel UI/logic.
4. **Bootstrap script encoding** — `bootstrap-mvp-v1.ps1` should not be re-run under PS 5.1 for Cyrillic HTML; use `repair-mvp-v1-encoding.mjs` instead (or add UTF-8 BOM to bootstrap + PS 7).
5. **Visual pass** — operator comparison against `hg_shem-v1.png` at 2560×1440 / 1920×1080 not automated in this task.

---

## SAFE UNKNOWN

1. **`hg_shem-v2.png`** — Task context references v2 as “current operational layout,” but **file not in repo**. Cannot confirm v2 exists elsewhere or whether v1 is outdated relative to an external v2 asset. **Active source: v1 only.**

2. **Pixel-perfect schema match** — Structural zones align with documented MVP map; no automated diff against PNG was run (visual QA required).

3. **Workspace git tracking** — `workspaces/homegateway-v4-ai/` may be outside default git visibility; operator should confirm tracking policy for workspace vs project docs.

---

## Git status summary

**Changed/added by this task (project docs/tools):**

- `projects/homegateway-v4-ai/tools/repair-mvp-v1-encoding.mjs` (new)
- `projects/homegateway-v4-ai/reports/mvp-v1-stabilization-report.md` (new)

**Changed in workspace (not committed):**

- `workspaces/homegateway-v4-ai/v1/src/partials/**/*.html`
- `workspaces/homegateway-v4-ai/v1/src/pages/index.html`
- `workspaces/homegateway-v4-ai/v1/README.md`
- `workspaces/homegateway-v4-ai/v1/dist/*` (build output)

**No commit, stage, or push performed** (per MARS default).

---

## Operator next step

Open `workspaces/homegateway-v4-ai/v1/dist/index.html` in browser and confirm Cyrillic rendering. Re-apply encoding fix anytime:

```bash
node projects/homegateway-v4-ai/tools/repair-mvp-v1-encoding.mjs
cd workspaces/homegateway-v4-ai/v1 && npm run build
```
