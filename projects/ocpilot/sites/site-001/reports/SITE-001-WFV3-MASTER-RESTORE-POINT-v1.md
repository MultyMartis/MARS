# SITE-001 WF-V3 Master Restore Point v1

**Type:** Master restore point — **documentation + external backup**  
**Date:** 2026-06-14  
**Site:** SITE-001 — Автосалон СИБКАР  
**Artifact:** Unified WF-V3 frontend prototype (NOT OpenCart · NOT TEST · NOT FTP)

**Explicit exclusions (honored):** No layout changes · No refactor · No deletions · No OCPILOT-STATE update · No OPERATIONAL-INDEX update · No git commit · No push · No TEST deploy · No FTP

---

## Restore point summary

| Field | Value |
|-------|-------|
| **Restore point name** | `wf-v3-master-restore-point-2026-06-14` |
| **Version label** | WF-V3 Unified Master Restore Point **v1** |
| **Backup path** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\wf-v3-master-restore-point-2026-06-14\` |
| **Manifest** | `BACKUP-MANIFEST.md` (same folder) |
| **Source workspace** | `C:\AI MARS\workspaces\site-001-wf-v3\` |
| **Created** | 2026-06-14T01:44:32 |

---

## Состояние

| Page | Source | Build output | Status |
|------|--------|--------------|--------|
| **Homepage** | `src/pages/homepage.html` | `dist/homepage.html` | Consolidated, built |
| **Catalog** | `src/pages/catalog.html` | `dist/catalog.html` | Consolidated, built |
| **PDP** | `src/pages/pdp.html` | `dist/pdp.html` | Consolidated, built |

Unified workspace consolidates three former standalone prototypes (homepage, catalog, PDP) into one Gulp build. See `workspaces/site-001-wf-v3/docs/WF-V3-CONSOLIDATION-REPORT-v1.md`.

---

## Статус

| Layer | Status |
|-------|--------|
| **WF-GRID** | **ACTIVE** |
| **WF-LAYOUT** | **ACTIVE** |
| **Unified Workspace** | **ACTIVE** |
| **Brand Layer** | **COMPLETE** |

---

## Build

```powershell
cd "C:\AI MARS\workspaces\site-001-wf-v3"
npm install
npm run build
```

| Output | Path |
|--------|------|
| Homepage | `dist/homepage.html` |
| Catalog | `dist/catalog.html` |
| PDP | `dist/pdp.html` |

Shared: `dist/css/main.css`, `dist/js/`, `dist/img/`, `dist/favicon/`.

**Build pipeline:** Gulp (`gulpfile.js`) — HTML include, SCSS compile, static asset copy.

---

## Следующий этап

**OpenCart Mapping**

---

## Запрещено считать частью restore point

| Exclusion | Notes |
|-----------|-------|
| OpenCart integration | Not started |
| Twig integration | Not started |
| CRM integration | Not started |
| Real inventory data | Placeholder / mock data only |
| Vehicle photography | SVG placeholders only |
| Bank asset pack | SVG placeholders only |

---

## Backup contents

| Included | Excluded |
|----------|----------|
| `src/` — pages, partials, SCSS, JS, img | `node_modules/` |
| `dist/` — all three built pages + assets | `.cache/`, `temp/`, `tmp/` |
| `docs/` — consolidation and prototype reports | `*.log` |
| `scripts/` — screenshot capture | secrets, FTP credentials |
| `screenshots/catalog-v0.2/` — 4 existing PNG | |
| `package.json`, `package-lock.json`, `gulpfile.js`, `README.md`, `.gitignore` | |

**File count:** 159 workspace files (+ `BACKUP-MANIFEST.md`).  
**Total size:** ~2.07 MB.

---

## Why it was saved

Главная точка восстановления WF-V3 **перед OpenCart Mapping**, чтобы:

1. Зафиксировать принятое unified-состояние Homepage + Catalog + PDP без риска регресса при mapping-этапе.
2. Иметь offline restore point в external storage (`C:\AI MARS STORAGE`) независимо от git (workspace gitignored).
3. Отделить clean-room frontend lifecycle от OpenCart/TEST backup chain.

---

## How to restore

### Option A — Replace active workspace (recommended)

```powershell
$backup = "C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\wf-v3-master-restore-point-2026-06-14"
$workspace = "C:\AI MARS\workspaces\site-001-wf-v3"

# Optional: rename current workspace before overwrite
# Rename-Item $workspace "$workspace.pre-restore-$(Get-Date -Format yyyyMMdd-HHmm)"

robocopy $backup $workspace /E /XD node_modules /XF BACKUP-MANIFEST.md
```

Then rebuild (see Build section). Do **not** copy `node_modules/` from backup — excluded by design.

### Option B — Restore to a new workspace folder

```powershell
$backup = "C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\wf-v3-master-restore-point-2026-06-14"
$target = "C:\AI MARS\workspaces\site-001-wf-v3-restored-master"

New-Item -ItemType Directory -Path $target -Force
robocopy $backup $target /E /XD node_modules /XF BACKUP-MANIFEST.md
cd $target
npm install
npm run build
```

Open `dist/homepage.html`, `dist/catalog.html`, or `dist/pdp.html` at viewport width ≥ 1280px.

---

## Relationship to other restore points

| Restore point | Environment | Scope |
|---------------|-------------|-------|
| `site-001-wf-v3-pdp-prototype-v0.1-20260611` | Local workspace | PDP-only prototype v0.1 |
| **`wf-v3-master-restore-point-2026-06-14`** | **Local workspace + external storage** | **Unified WF-V3 master (Homepage + Catalog + PDP)** |
| TEST-era points | TEST (OpenCart) | See [SITE-001-RESTORE-POINT-REGISTRY-v1.md](SITE-001-RESTORE-POINT-REGISTRY-v1.md) |

This restore point is **independent** of TEST FTP backups. Restoring it does **not** change `https://sibcar.new-site.space/`.

---

## Verification reference

Post-backup checks (all **PASS** — see manifest):

- Backup folder, `src/`, `dist/`, `docs/`, `package.json`, `gulpfile.js`, `README.md` present
- `dist/homepage.html`, `dist/catalog.html`, `dist/pdp.html` present
- `node_modules/` absent in backup
- `screenshots/catalog-v0.2/` — 4 PNG files copied
- `BACKUP-MANIFEST.md` present

---

## Related documents

- [BACKUP-MANIFEST.md](file:///C:/AI%20MARS%20STORAGE/ocpilot/project-sites/site-001/backups/wf-v3-master-restore-point-2026-06-14/BACKUP-MANIFEST.md) — external storage
- [SITE-001-RESTORE-POINT-REGISTRY-v1.md](SITE-001-RESTORE-POINT-REGISTRY-v1.md) — TEST-era registry
- [SITE-001-WF-V3-PROTOTYPE-RESTORE-POINT-v1.md](SITE-001-WF-V3-PROTOTYPE-RESTORE-POINT-v1.md) — prior PDP-only restore point
- `workspaces/site-001-wf-v3/docs/WF-V3-CONSOLIDATION-REPORT-v1.md` — consolidation source of truth
