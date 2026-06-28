# SITE-002 — Project Site Container

**Site ID:** SITE-002  
**Slug:** site-002  
**Status:** **STABLE LIVE CHECKPOINT — M9.13 ABOUT COMPANY RESTORED 01** (2026-06-23)  
**Run:** Stable checkpoint after operator-approved About page restoration  
**Active stage:** **PRODUCTION PREPARATION** — BZPM UX Redesign recovery **CLOSED** (2026-06-28) · **Corporate Pages Program** implementation phase **COMPLETE on TEST** — M9.14–M9.18 **IMPLEMENTED** · **Visual Polish Pass 1** **REJECTED BY OPERATOR** — rolled back to Pre-Pass-1 (2026-06-28) · **Next:** Visual Polish Pass 1.1

### BZPM UX REDESIGN — project banner

| Field | Value |
|-------|--------|
| **Recovery status** | **CLOSED** |
| **Production status** | **READY AFTER OPERATOR GATES** |
| **Implementation (corp pages)** | M9.14–M9.18 **IMPLEMENTED** on TEST — program implementation phase **COMPLETE** (pending operator B6/B8) |
| **Closeout** | [reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) |

Copy source: [sites/_template-site/](../_template-site/README.md) folder map.

---

## Purpose

Second registered OCPilot project site workspace. **TEST** площадка для аудита и внедрения изменений PDP / Catalog UX.

**Domain:** `zpm.new-site.space`

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |
| **MANUAL UI / CSS / TWIG / JS REFINEMENTS ARE CANONICAL** | Operator manual edits on live TEST are the visual and behavioural authority |
| **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. [§7 Filter Architecture](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#7-filter-architecture), [§8 Live Files](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#8-live-files-with-business-logic), [§14 Commercial Trust Block](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#14-commercial-trust-block), [§16 Catalog State Persistence](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#16-catalog-state-persistence), [§17 About Page History](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#17-about-page-history) |
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
| Name | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |
| Status | **STABLE LIVE CHECKPOINT** — About page restored; catalog UX carried forward |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md) |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §17 About Page History |
| About page | M9.13 redesign **rejected** — **restored** pre-redesign `/about` |
| Catalog UX | Carried forward from M9.8.9 Catalog UX Complete 01 |
| Registration | [reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md](reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-COMPANY-RESTORED-01.md) |
| Rollback source | Beget full backup + current live TEST + About pass backups + file-level pass backups |

### Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md) |
| Scope | Catalog UX cluster — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| Baseline doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md) |
| Scope | Commercial Trust — superseded for live truth |

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
External credentials (when supplied): `C:\MARS Phenix\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\` — not git-tracked.

---

## External bulk storage

`C:\MARS Phenix\AI MARS STORAGE\ocpilot\project-sites\site-002\`

Metadata stays in this repo tree; large archives stay external.

---

## Rules

- No secrets. No live credentials.
- **PRE-TASK:** read Knowledge Map + latest Stable Checkpoint before any SITE-002 work; for About page — follow §17 + M9.13 restore/redesign/polish reports; for filters/sort/pagination/limit/only_with_price — follow §16 + 09A/09B/09C; for filter/catalog/1C/price/PLP — follow domain-specific rule in Knowledge Map §13; for trust block/certificates/dealers form/category CTA — follow §14.
- No site modifications, FTP, phpMyAdmin, or admin panel actions until chartered runs.
- Do not invent URLs, hosting, or client names beyond operator-supplied registration facts.
