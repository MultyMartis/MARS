# SITE-002 — Project Site Container

**Site ID:** SITE-002  
**Slug:** site-002  
**Status:** **STABLE LIVE CHECKPOINT** — active metadata baseline; live hosting is source-of-truth  
**Run:** 4.139 — Stable Live PDP V5.1 Checkpoint (2026-06-14)

Copy source: [sites/_template-site/](../_template-site/README.md) folder map.

---

## Purpose

Second registered OCPilot project site workspace. **TEST** площадка для аудита и внедрения изменений PDP / Catalog UX.

**Domain:** `zpm.new-site.space`

---

## Folder map

| Subfolder | Use |
|-----------|-----|
| `baselines/` | Stable checkpoint definitions (metadata; may not include site files) |
| `materials/` | Source materials from operator (sanitized briefs, path lists, screenshots without secrets) |
| `audits/` | General audit outputs |
| `opencart-analysis/` | OpenCart version, core structure, theme layout findings |
| `catalog-analysis/` | Categories, products, attributes, filters, options |
| `extension-analysis/` | Modules, extensions, ocMod, vQmod if present |
| `theme-analysis/` | Templates, layouts, theme overrides |
| `controller-analysis/` | Controllers, models, language files touched by project logic |
| `seo-url-analysis/` | SEO URLs, redirects, aliases, route mapping |
| `database-analysis/` | Schema observations, table map, safe metadata only |
| `import-planning/` | Future catalog import plans — no uncontrolled import files in repo |
| `backups/files/`, `backups/database/` | Backup references or sanitized backup metadata |
| `snapshots/files/`, `snapshots/database/` | Sanitized snapshots or manifests |
| `tasks/` | Scoped task files |
| `reports/` | `# REPORT — …` outputs |
| `safe-unknown/` | Unresolved findings and questions |
| `qa/` | QA checklists and results |

---

## Active stable checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Status | **STABLE LIVE CHECKPOINT** |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| Supersedes | `SITE-002-STABLE-LIVE-MANUAL-COMPACT-2026-06-14` (historical) |
| Active passes | PDP V5.1 (specs collapse, scroll UX, scroll offset) · Category V2.3.1 · operator manual polish |
| Rollback source | Beget global backup + operator live state |

Live TEST storefront after PDP V5.1 passes and operator manual CSS/Twig edits is **source-of-truth**. This checkpoint does **not** contain site files.

---

## Passport

[site-passport.md](site-passport.md) — per [site-passport-standard.md](../../site-passport-standard.md).

---

## Project access brief (required before Run 5)

[project-access-brief.md](project-access-brief.md) — access inventory and operation permissions for Cursor/OCPilot.

| Item | Status |
|------|--------|
| Brief file | Present — access inventory **incomplete** (credentials pending) |
| Intake materials | **PENDING** |
| Run 5 gate | **NO** — access brief incomplete; intake not closed |

Template: [templates/project-access-brief-template.md](../../templates/project-access-brief-template.md).  
External credentials (when supplied): `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\` — not git-tracked.

---

## External bulk storage

`C:\AI MARS STORAGE\ocpilot\project-sites\site-002\`

Metadata stays in this repo tree; large archives stay external.

---

## Rules

- No secrets. No live credentials.
- No site modifications, FTP, phpMyAdmin, or admin panel actions until chartered runs.
- Do not invent URLs, hosting, or client names beyond operator-supplied registration facts.
