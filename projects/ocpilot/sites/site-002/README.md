# SITE-002 — Project Site Container

**Site ID:** SITE-002  
**Slug:** site-002  
**Status:** **STABLE LIVE CHECKPOINT — M9.8 UX POLISH 01** (2026-06-19)  
**Run:** Stable live checkpoint after M9.8 deploy passes + operator manual PLP polish  
**Active stage:** **M9.8 UX Polish Pack** (remaining items)

Copy source: [sites/_template-site/](../_template-site/README.md) folder map.

---

## Purpose

Second registered OCPilot project site workspace. **TEST** площадка для аудита и внедрения изменений PDP / Catalog UX.

**Domain:** `zpm.new-site.space`

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| **MANUAL UI / CSS / TWIG REFINEMENTS ARE CANONICAL** | Operator manual edits on live TEST are the visual authority |
| **Conflict resolution** | If docs contradict current TEST → source of truth = live TEST on https://zpm.new-site.space/ |

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
| Name | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| Status | **STABLE LIVE CHECKPOINT** — live TEST after M9.8 passes + operator manual PLP polish |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md) |
| Completed M9.8 | M9.8.1 PDP Gallery Compact · M9.8.2 PDP Lightbox Constraints · M9.8.5 Products Per Page Selector |
| Operator manual | PLP Grid Density · PLP Compact · Filter Compact · Breakpoint Polish · Manual CSS · Manual Twig |
| Open bug | EC-01 — filter sidebar empty subcategories on branch 80 (Моечные ванны) |
| Roadmap | [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) — **M9.8 UX Polish Pack** |
| Next planned | Remaining M9.8 tasks · EC-01 fix · **M10** not authorized |
| Rollback source | Beget full backup + current live TEST + file-level pass backups |

### Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| Scope | PDP V5.1 · Category V2.3.1 — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` |
| Report | [reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md](reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md) |
| Scope | File baseline — historical file rollback only |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE` |
| Report | [reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md](reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md) |
| Scope | Historical — homepage 5-branch deploy capture |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9-COMPLETE-20260615` |
| Report | [reports/SITE-002-STABLE-M9-COMPLETE.md](reports/SITE-002-STABLE-M9-COMPLETE.md) |
| Scope | Pre-M9.7D / pre-manual UI |

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
