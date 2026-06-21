# SITE-002 — Project Site Container

**Site ID:** SITE-002  
**Slug:** site-002  
**Status:** **STABLE LIVE CHECKPOINT — M9.8.9 COMMERCIAL TRUST 01** (2026-06-21)  
**Run:** Stable checkpoint after filter recovery + filter UX + Commercial Trust + operator manual polish  
**Active stage:** **M9.8.9 Minor Fixes Pack #1** (remaining tasks per roadmap)

Copy source: [sites/_template-site/](../_template-site/README.md) folder map.

---

## Purpose

Second registered OCPilot project site workspace. **TEST** площадка для аудита и внедрения изменений PDP / Catalog UX.

**Domain:** `zpm.new-site.space`

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| **MANUAL UI / CSS / TWIG / JS REFINEMENTS ARE CANONICAL** | Operator manual edits on live TEST are the visual and behavioural authority |
| **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. [§7 Filter Architecture](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#7-filter-architecture), [§8 Live Files](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#8-live-files-with-business-logic), [§14 Commercial Trust Block](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#14-commercial-trust-block) |
| **Operator manual JS (04B)** | [knowledge §12](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#12-operator-manual-js-refinements) · [registration report](reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md) |
| **Conflict resolution** | If docs contradict current TEST → source of truth = live TEST on https://zpm.new-site.space/ |

---

## Folder map

| Subfolder | Use |
|-----------|-----|
| `baselines/` | Stable checkpoint definitions (metadata; may not include site files) |
| `knowledge/` | Persistent technical knowledge map and architecture reference |
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
| Name | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| Status | **STABLE LIVE CHECKPOINT** — filter recovery + filter UX + Commercial Trust complete |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md) |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Recovery | Product reset · 1C import · price index (06D/06F) · filters (06H/06J/06M) |
| Filter UX | Scroll (04/04B) · hide subcategories (07) · group reset (08/08A) |
| Commercial Trust | 03B redesign · 03C deploy · operator manual polish |
| Other UX | Wishlist/compare smart tooltips (01) |
| Completed M9.8 | M9.8.1 PDP Gallery · M9.8.2 Lightbox · M9.8.5 Products Per Page |
| Operator manual | PLP / filter / breakpoint / CSS / Twig polish · JS refinements (04B) · Commercial Trust polish |
| Open bugs | EC-01 — mitigated by subcategories hide (07); limit+filter persistence · page-intro__description — open |
| Roadmap | [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) |
| Registration | [reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md](reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md) |
| Rollback source | Beget full backup + current live TEST + file-level pass backups |

### Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md) |
| Scope | Filter recovery + filter UX — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01` |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-RECOVERY-01.md) |
| Scope | Filter recovery — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md) |
| Scope | M9.8.1/2/5 + operator PLP polish — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| Scope | PDP V5.1 · Category V2.3.1 — historical |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` |
| Report | [reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md](reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md) |
| Scope | File baseline — historical file rollback only |

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
- **PRE-TASK:** read Knowledge Map + latest Stable Checkpoint before any SITE-002 work; for filter/catalog/1C/price/PLP — follow domain-specific rule in Knowledge Map §13; for trust block/certificates/dealers form/category CTA — follow §14.
- No site modifications, FTP, phpMyAdmin, or admin panel actions until chartered runs.
- Do not invent URLs, hosting, or client names beyond operator-supplied registration facts.
