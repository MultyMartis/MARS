# SITE-001 — Project Site Container

**Site ID:** SITE-001  
**Slug:** site-001  
**Status:** **AWAITING INTAKE**  
**Run:** 4 — First Project Site Intake (container only; no dealership data)

Copy source: [sites/_template-site/](../_template-site/README.md) folder map.

---

## Purpose

First registered OCPilot project site workspace. Actual dealership information will be attached when operator supplies materials.

---

## Folder map

| Subfolder | Use |
|-----------|-----|
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

## Passport

[site-passport.md](site-passport.md) — per [site-passport-standard.md](../../site-passport-standard.md).

---

## Project access brief (required before Run 5)

[project-access-brief.md](project-access-brief.md) — access inventory and operation permissions for Cursor/OCPilot.

| Item | Status |
|------|--------|
| Brief file | Present — **incomplete** (SAFE UNKNOWN fields) |
| Run 5 gate | **NO** until operator completes brief and [intake-readiness-review.md](../../intake-readiness-review.md) |

Template: [templates/project-access-brief-template.md](../../templates/project-access-brief-template.md).  
External credentials (if any): `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\secrets\` — not git-tracked.

---

## External bulk storage

`C:\AI MARS STORAGE\ocpilot\project-sites\site-001\`

Metadata stays in this repo tree; large archives stay external.

---

## Rules

- No secrets. No live credentials.
- No site modifications, FTP, phpMyAdmin, or admin panel actions until chartered runs.
- Do not invent URLs, hosting, or client names.
