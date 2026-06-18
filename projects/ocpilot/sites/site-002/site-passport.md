# SITE-002 — Site Passport

**Status:** **STABLE LIVE CHECKPOINT — M9.8 UX POLISH 01**  
**Run:** Stable live checkpoint after M9.8 deploy passes + operator manual PLP polish (2026-06-19)

---

## Identity

| Field | Value |
|-------|-------|
| **Site ID** | SITE-002 |
| **Site Name** | ЗПМ |
| **Slug** | site-002 |
| **Platform** | ocStore / OpenCart |
| **Version** | SAFE UNKNOWN |
| **Baseline Match** | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| **Hosting** | Beget (FTP `polygonws.beget.tech`) — operator-recorded |
| **Access Methods** | Documented in [project-access-brief.md](project-access-brief.md); credential locations outside repo |
| **Storage Location** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` |
| **Environment** | TEST |
| **Test URL** | https://zpm.new-site.space/ |
| **Current Status** | **STABLE LIVE CHECKPOINT — M9.8 UX POLISH 01** |
| **Active baseline** | [baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md) |
| **Rollback source** | Beget full backup + current live TEST + file-level pass backups |
| **Notes** | TEST площадка. **MANUAL UI / CSS / TWIG REFINEMENTS ARE CANONICAL** — operator edits on live TEST are the visual authority. M9.8.1 · M9.8.2 · M9.8.5 complete; operator PLP/filter/breakpoint polish complete. Open bug: EC-01 (filter sidebar, branch 80). M10 not authorized. |

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| **MANUAL UI REFINEMENTS ARE CANONICAL** | Operator manual CSS, Twig, and UX edits on live TEST override older M9.x deploy snapshots |
| **MANUAL CSS REFINEMENTS ARE CANONICAL** | Operator CSS edits on live TEST override repo work copies |
| **MANUAL TWIG REFINEMENTS ARE CANONICAL** | Operator Twig edits on live TEST override repo work copies |
| **Conflict resolution** | If any documentation contradicts current TEST state, **source of truth** = live TEST on https://zpm.new-site.space/ as registered in this checkpoint |
| **Do NOT use as visual baseline** | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI`, `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14`, pre-M9.8 work copies |

---

## Stable checkpoint (active)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| Registered | 2026-06-19 |
| Type | Metadata-only stable live checkpoint (operator attestation + pass QA) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Completed M9.8 passes | M9.8.1 PDP Gallery Compact · M9.8.2 PDP Lightbox Constraints · M9.8.5 Products Per Page Selector |
| Operator manual passes | PLP Grid Density · PLP Compact · Filter Compact · Breakpoint Polish · Manual CSS · Manual Twig |
| Active stage | **M9.8 UX Polish Pack** (remaining M9.8 items per roadmap) |
| Next planned | Remaining M9.8 tasks · EC-01 fix · **M10** — not authorized |

**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md)

---

## Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Doc | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| Scope | PDP V5.1 · Category V2.3.1 · operator manual polish — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` |
| Doc | [reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md](reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md) |
| Scope | File + scoped DB JSON backup — historical file rollback only |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE` |
| Doc | [reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md](reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md) |
| Scope | Historical capture — homepage 5-branch deploy |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9-COMPLETE-20260615` |
| Doc | [reports/SITE-002-STABLE-M9-COMPLETE.md](reports/SITE-002-STABLE-M9-COMPLETE.md) |
| Scope | Pre-M9.7D / pre-manual UI |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` |
| Doc | [reports/SITE-002-STABLE-M8.3-BEFORE-M9.md](reports/SITE-002-STABLE-M8.3-BEFORE-M9.md) |
| Scope | Pre-M9 rollback — M7.1 + M8.3 only |

---

## Project status (BZPM)

### Завершено

- M7.1 Launch Mode
- M8 Cleanup
- M9 Filter Profiles
- M9.5 Hub Mode
- M9.7 Images
- M9.7 Megamenu Cleanup
- Homepage Neutral Branches
- Manual UI Refinement
- M9.8.1 PDP Gallery Compact
- M9.8.2 PDP Lightbox Constraints
- M9.8.5 Products Per Page Selector
- Operator manual PLP / filter / breakpoint / CSS / Twig polish

### Активный этап

**M9.8 UX Polish Pack** (remaining items) — [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md) § M9.8

---

## Next work rule

Before next SITE-002 change: use `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` as authority. Live-capture any files touched before deploy. **Do not** start M10 without operator charter. Rollback = Beget full backup → current live TEST → file-level pass backups.

---

## SAFE UNKNOWN

- ocStore / OpenCart exact version and release line
- Beget backup artifact location and timestamp (operator attestation only)
- M10 scope and authorization status

---

## Security notes

| Check | Value |
|-------|-------|
| No secrets in checkpoint docs | **yes** |
| DB JSON in repo (prior baselines) | Row data only — treat as sensitive; no credentials in dumps |
