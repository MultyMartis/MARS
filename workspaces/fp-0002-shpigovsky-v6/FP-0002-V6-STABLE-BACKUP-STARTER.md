# FP-0002 V6 STABLE BACKUP STARTER

**Checkpoint:** FP-0002 V6 STABLE BACKUP STARTER  
**Created:** 2026-06-22T13:32:54+07:00  
**Branch:** `mars/post-cycle8-live-tests`  
**HEAD before checkpoint:** `bf313e4a38789ca7d332d24bb2ccddb57345aab6`  
**Status:** V6 CLEAN ROOM

---

## Workspace paths

| Kind | Path |
|------|------|
| Absolute | `C:\AI MARS\workspaces\fp-0002-shpigovsky-v6\` |
| Repo-relative | `workspaces/fp-0002-shpigovsky-v6/` |

---

## V6 CLEAN ROOM state

| Item | State |
|------|-------|
| Foundation | **Created** — Gulp build, SCSS tokens, zero skeleton HTML/JS |
| Header | **Not started** — placeholder text only in `index.html` |
| Hero | **Not started** — no hero section or partial |
| Footer | **Not started** — placeholder text only in `index.html` |
| Section layout | **Not started** — no `src/partials/`; no section SCSS |
| Visual source policy | **JPG_ONLY** |

---

## Workspace inventory (directories and files)

```
.gitignore
gulpfile.js
package.json
package-lock.json
backup/
  FP-0002-V6-STABLE-BACKUP-STARTER.inventory.json
  FP-0002-V6-STABLE-BACKUP-STARTER.zip
fonts/
  .gitkeep
img/
  .gitkeep
logs/
  .gitkeep
  v6-actions.log
  v6-decisions.log
  v6-safe-unknown.log
  v6-source-access.log
  v6-violations.log
qa/
  .gitkeep
reports/
  FP-0002-v6-CLEAN-ROOM-DECLARATION-v1.md
  FP-0002-v6-EXECUTION-LOGGING-SYSTEM-v1.md
  FP-0002-v6-JPG-ONLY-HARD-LAW-v1.md
  FP-0002-v6-JPG-ONLY-RULE-LOCK-AND-ASSET-SETUP-REPORT-v1.md
  FP-0002-v6-SOCIAL-ICON-NORMALIZATION-v1.md
  FP-0002-v6-SOURCE-ACCESS-GUARD-v1.md
  FP-0002-v6-SOURCE-CHECK-v1.md
  FP-0002-v6-ZERO-SKELETON-REPORT-v1.md
src/
  fonts/.gitkeep
  img/.gitkeep
  img/social/max.svg
  img/social/telegram.svg
  img/social/whatsapp.svg
  js/main.js
  pages/index.html
  scss/style.scss
  scss/base/_reset.scss
  scss/layout/_container.scss
  scss/utils/_mixins.scss
  scss/utils/_variables.scss
  svg/.gitkeep
svg/.gitkeep
FP-0002-V6-STABLE-BACKUP-STARTER.md
```

**Excluded from workspace tree (not part of checkpoint payload):** `node_modules/`, `dist/`, cache, temporary files.

---

## Foundation state

- **Build:** Gulp 4 (`gulp build` → `dist/`)
- **HTML:** `src/pages/index.html` — zero skeleton; `HEADER NOT STARTED`, `MAIN NOT STARTED`, `FOOTER NOT STARTED`
- **SCSS:** reset, variables (`$container-max: 1220px`), mixins, container layout
- **JS:** `src/js/main.js` — empty stub (no behavior)
- **Assets:** normalized social SVG icons (`telegram`, `whatsapp`, `max`)
- **Reports:** v6 clean-room, JPG-only law, logging system, source guard, zero-skeleton reports
- **Logs:** append-only v6 execution logs under `logs/`

---

## Allowed visual source (external, not copied)

| Field | Value |
|-------|-------|
| Path (repo-relative) | `workspaces/website-factory-operations/FP-0002-SHPIGOVSKY/INCOMING/01_DESIGN/HOME-PAGE-FULL-MOCKUP.jpg` |
| Path (absolute) | `C:\AI MARS\workspaces\website-factory-operations\FP-0002-SHPIGOVSKY\INCOMING\01_DESIGN\HOME-PAGE-FULL-MOCKUP.jpg` |
| Size | 8 107 632 bytes |
| SHA-256 | `cdd1d5bcc512b617dcf93efa97af88cf4ad99a0895cfc27a63c07bc704945290` |

No duplicate JPG was created inside the v6 workspace or ZIP.

---

## Forbidden sources

- FIG / Figma source files
- PDF exports
- v1, v2, v3, v4, v5 workspaces and deliverables
- Old workspaces
- Old reports (outside v6 `reports/`)
- Old visual measurements
- Old decisions from prior versions

---

## Technical stack

| Layer | Technology |
|-------|------------|
| Build | Gulp 4, gulp-file-include, gulp-sass (Dart Sass) |
| Markup | HTML (zero skeleton) |
| Styles | SCSS (`@use` modules) |
| Scripts | Vanilla JS stub |
| Package manager | npm |

---

## Layout parameters

| Parameter | Value |
|-----------|-------|
| Container max-width | **1220px** (`$container-max`) |
| Approach | **Desktop-first** |
| Primary breakpoint | **1024px** (`$breakpoint-desktop-min`) |

---

## Mandatory work order (post-checkpoint)

1. **audit** — JPG Visual Audit (no HTML until approved)
2. **extraction** — asset and token extraction from approved audit
3. **geometry map** — block geometry documentation
4. **structure lock** — HTML structure approval before styling
5. **HTML** — one block at a time
6. **SCSS** — matching block styles

---

## Backup artifacts

| Artifact | Path |
|----------|------|
| Manifest | `FP-0002-V6-STABLE-BACKUP-STARTER.md` |
| Inventory | `backup/FP-0002-V6-STABLE-BACKUP-STARTER.inventory.json` |
| ZIP archive | `backup/FP-0002-V6-STABLE-BACKUP-STARTER.zip` |

### ZIP verification

| Field | Value |
|-------|-------|
| Size | 74 983 bytes |
| SHA-256 | `016a9b0626115635e92e073f682d902f680ba21b10efb73fa5cd8da6ce13e3b1` |
| Entries | 38 files (no `node_modules`, no `dist`, no self-reference, no FIG/PDF) |
| Opens | Verified |

---

## Required logs

| Log | Purpose |
|-----|---------|
| `logs/v6-decisions.log` | Architectural and source decisions |
| `logs/v6-actions.log` | File changes and build actions |
| `logs/v6-source-access.log` | Source file access record |
| `logs/v6-safe-unknown.log` | Information gaps |
| `logs/v6-violations.log` | Rule breaches (empty if none) |

---

## SAFE UNKNOWN

- Exact production domain, favicon set, and font files are not defined at this checkpoint.
- Responsive behavior beyond 1024px split must come from JPG Visual Audit, not from prior versions.
- Operator approval is required before any layout HTML begins.

---

## Restore procedure

1. Extract `backup/FP-0002-V6-STABLE-BACKUP-STARTER.zip` to a clean directory.
2. Verify every file SHA-256 against `backup/FP-0002-V6-STABLE-BACKUP-STARTER.inventory.json`.
3. Run `npm ci` (or `npm install` from existing `package-lock.json`).
4. Run `npm run build` — expect successful foundation build.
5. Confirm `index.html` still shows zero-skeleton placeholders (Header/Hero/Footer not started).
6. Do **not** import FIG, PDF, or prior workspace assets.
7. Resume workflow at **JPG Visual Audit** — not HTML implementation.

---

**Checkpoint status:** FP-0002 V6 STABLE BACKUP STARTER — foundation preserved; layout not started.
