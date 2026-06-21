# SITE-001 WF-V3 Prototype Restore Point v1

**Type:** Restore point registry entry — **documentation only**  
**Date:** 2026-06-11  
**Site:** SITE-001 — Автосалон СИБКАР  
**Artifact:** Website Factory clean-room frontend prototype (NOT OpenCart · NOT TEST · NOT FTP)

**Explicit exclusions (honored):** No OCPILOT-STATE update · No OPERATIONAL-INDEX update · No git commit · No push · No TEST deploy · No FTP

---

## Restore point summary

| Field | Value |
|-------|-------|
| **Restore point name** | `site-001-wf-v3-pdp-prototype-v0.1-20260611` |
| **Version label** | WF-V3 PDP Prototype **v0.1** |
| **Backup path** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\site-001-wf-v3-pdp-prototype-v0.1-20260611\` |
| **Manifest** | `BACKUP-MANIFEST.md` (same folder) |
| **Source workspace** | `C:\AI MARS\workspaces\site-001-wf-v3-pdp-prototype\` |
| **Created** | 2026-06-11T01:21:51 |

---

## What this version represents

**WF-V3 PDP Prototype v0.1** — первый clean-room desktop visual model PDP для SITE-001 (СИБКАР) в стандартном стеке Website Factory:

- HTML + SCSS + JS + Gulp + `@@include`
- CSS и разметка написаны с нуля; legacy W4/W5/WF-V2 CSS **не использовались**
- Все секции PDP собраны и приняты оператором по **архитектуре**
- Визуальная полировка относительно design authority **ещё не завершена** — запланирована **v0.2**
- OpenCart integration и TEST deploy **не начаты**

**Design authority:** `projects/ocpilot/sites/site-001/design/wf-v3-concept/01-sibcar-v3-concept.png`

**Session report (source):** `workspaces/site-001-wf-v3-pdp-prototype/docs/REPORT.md`

---

## Visual status at restore point

| Aspect | Status |
|--------|--------|
| Architecture | **ACCEPTED BY OPERATOR** |
| Visual polish | **NEEDS v0.2** |
| OpenCart integration | **NOT STARTED** |
| TEST deploy | **NOT STARTED** |

---

## Backup contents

| Included | Excluded |
|----------|----------|
| `src/` — pages, partials, SCSS, JS, img | `node_modules/` |
| `docs/` — REPORT, ASSET-INVENTORY | temp cache (`.cache/`, `temp/`, `tmp/`) |
| `dist/` — built `pdp.html`, CSS, JS, img | secrets, FTP credentials |
| `package.json`, `package-lock.json` | |
| `gulpfile.js`, `README.md`, `.gitignore` | |

**File count:** 66 files (+ manifest).

---

## Why it was saved

Зафиксировать стабильную точку **перед визуальной доработкой v0.2**, чтобы:

1. Сохранить принятую архитектуру секций и clean-room stack без риска регресса при polish-pass.
2. Иметь offline restore point в external storage (`C:\AI MARS STORAGE`) независимо от git (workspace gitignored).
3. Отделить frontend prototype lifecycle от OpenCart/TEST backup chain (см. [SITE-001-RESTORE-POINT-REGISTRY-v1.md](SITE-001-RESTORE-POINT-REGISTRY-v1.md) для TEST-era points).

---

## How to restore

### Option A — Replace active workspace (recommended)

```powershell
$backup = "C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\site-001-wf-v3-pdp-prototype-v0.1-20260611"
$workspace = "C:\AI MARS\workspaces\site-001-wf-v3-pdp-prototype"

# Optional: rename current workspace before overwrite
# Rename-Item $workspace "$workspace.pre-restore-$(Get-Date -Format yyyyMMdd-HHmm)"

robocopy $backup $workspace /E /XD node_modules /XF BACKUP-MANIFEST.md
```

Then rebuild (see below). Do **not** copy `node_modules/` from backup — it is excluded by design.

### Option B — Restore to a new workspace folder

```powershell
$backup = "C:\AI MARS STORAGE\ocpilot\project-sites\site-001\backups\site-001-wf-v3-pdp-prototype-v0.1-20260611"
$target = "C:\AI MARS\workspaces\site-001-wf-v3-pdp-prototype-restored-v0.1"

New-Item -ItemType Directory -Path $target -Force
robocopy $backup $target /E /XD node_modules /XF BACKUP-MANIFEST.md
cd $target
npm install
npm run build
```

Open `dist/pdp.html` at viewport width ≥ 1280px.

---

## How to rebuild

From restored workspace:

```powershell
cd C:\AI MARS\workspaces\site-001-wf-v3-pdp-prototype
npm install
npm run build
```

| Step | Command | Output |
|------|---------|--------|
| Install deps | `npm install` | `node_modules/` |
| Build | `npm run build` | `dist/pdp.html`, `dist/css/main.css`, `dist/js/`, `dist/img/` |
| Preview | Open `dist/pdp.html` in browser | Desktop ≥ 1280px |

**Build pipeline:** Gulp (`gulpfile.js`) — HTML include, SCSS compile, static asset copy.

---

## Relationship to other restore points

| Restore point | Environment | Scope |
|---------------|-------------|-------|
| `site-001-rebrand-baseline-v1` | TEST (OpenCart) | Pre–Website Factory rebrand baseline |
| `site-001-wfv2-final-experimental-20260610` | TEST (OpenCart) | WF-V2 experimental CSS/Twig |
| **`site-001-wf-v3-pdp-prototype-v0.1-20260611`** | **Local workspace only** | **WF-V3 clean-room frontend prototype** |

This restore point is **independent** of TEST FTP backups. Restoring it does **not** change `https://sibcar.new-site.space/`.

---

## Verification reference

Post-backup checks (all **PASS** — see manifest):

- Backup folder, `src/`, `docs/`, `package.json`, `dist/pdp.html` present
- `node_modules/` absent in backup
- `BACKUP-MANIFEST.md` present

---

## Related documents

- [BACKUP-MANIFEST.md](file:///C:/AI%20MARS%20STORAGE/ocpilot/project-sites/site-001/backups/site-001-wf-v3-pdp-prototype-v0.1-20260611/BACKUP-MANIFEST.md) — external storage
- [SITE-001-RESTORE-POINT-REGISTRY-v1.md](SITE-001-RESTORE-POINT-REGISTRY-v1.md) — TEST-era registry (separate chain)
- `workspaces/site-001-wf-v3-pdp-prototype/docs/REPORT.md` — v0.1 session report
