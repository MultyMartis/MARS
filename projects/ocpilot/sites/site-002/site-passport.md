# SITE-002 — Site Passport

**Status:** **STABLE LIVE CHECKPOINT — M9.8.9 COMMERCIAL TRUST 01**  
**Run:** Stable live checkpoint after filter recovery + filter UX + Commercial Trust redesign + operator manual polish (2026-06-21)

---

## Identity

| Field | Value |
|-------|-------|
| **Site ID** | SITE-002 |
| **Site Name** | ЗПМ |
| **Slug** | site-002 |
| **Platform** | ocStore / OpenCart |
| **Version** | SAFE UNKNOWN |
| **Baseline Match** | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| **Hosting** | Beget (FTP `polygonws.beget.tech`) — operator-recorded |
| **Access Methods** | Documented in [project-access-brief.md](project-access-brief.md); credential locations outside repo |
| **Storage Location** | `C:\AI MARS STORAGE\ocpilot\project-sites\site-002\` |
| **Environment** | TEST |
| **Test URL** | https://zpm.new-site.space/ |
| **Current Status** | **STABLE LIVE CHECKPOINT — M9.8.9 COMMERCIAL TRUST 01** |
| **Active baseline** | [baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md) |
| **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. [§7 Filter Architecture](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#7-filter-architecture), [§8 Live Files](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#8-live-files-with-business-logic), [§14 Commercial Trust Block](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#14-commercial-trust-block) |
| **Operator manual JS (04B)** | [reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md](reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md) |
| **Rollback source** | Beget full backup + current live TEST + file-level pass backups |
| **Notes** | TEST площадка. **MANUAL UI / CSS / TWIG / JS REFINEMENTS ARE CANONICAL**. Filter recovery + filter UX complete. Commercial Trust (03B/03C + operator polish) registered. EC-01 mitigated by subcategories hide (07). M10 not authorized. |

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| **MANUAL UI REFINEMENTS ARE CANONICAL** | Operator manual CSS, Twig, JS, and UX edits on live TEST override older M9.x deploy snapshots |
| **MANUAL CSS REFINEMENTS ARE CANONICAL** | Operator CSS edits on live TEST override repo work copies |
| **MANUAL TWIG REFINEMENTS ARE CANONICAL** | Operator Twig edits on live TEST override repo work copies |
| **Conflict resolution** | If any documentation contradicts current TEST state, **source of truth** = live TEST on https://zpm.new-site.space/ as registered in this checkpoint |
| **Do NOT use as visual baseline** | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01`, `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14`, pre-M9.8.9 work copies |

---

## Stable checkpoint (active)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| Registered | 2026-06-21 |
| Type | Stable live checkpoint (FTP capture + operator attestation) |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| Recovery scope | Product reset · fresh 1C import · price index · filter hotfixes (06D–06M) |
| Filter UX scope | Scroll (04/04B) · hide subcategories (07) · group reset (08/08A) |
| Commercial Trust scope | M9.8.9-03B redesign · M9.8.9-03C deploy · operator manual polish |
| Other UX | Wishlist/compare smart tooltips (01) |
| Completed M9.8 passes | M9.8.1 PDP Gallery · M9.8.2 Lightbox · M9.8.5 Products Per Page |
| Operator manual passes | PLP / filter / breakpoint / CSS / Twig polish · **JS refinements (04B)** |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Open bugs | **EC-01** — mitigated by subcategories hide (07); M9.8.7 deferred |
| Next planned | Remaining M9.8.9 tasks per roadmap · deferred M9.8.3/4/6/8 · **M10** — not authorized |
| Registration | [reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md](reports/SITE-002-STABLE-CHECKPOINT-COMMERCIAL-TRUST-01.md) |

**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md)

---

## Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md) |
| Scope | Filter recovery + filter UX — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md) |
| Scope | M9.8.1/2/5 + operator PLP polish — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Doc | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| Scope | PDP V5.1 · Category V2.3.1 — historical |

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
- **Product reset + fresh 1C import**
- **Price index recovery (06D, 06F)**
- **Filter UX polish (04, 04A, 04B, 07, 08, 08A)**
- **Wishlist / Compare smart tooltips (01)**
- **Commercial Trust block (03B/03C + operator manual polish)**

### Активный этап

**M9.8.9 Minor Fixes Pack #1** — remaining tasks per [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)

### Отложено (M9.8 UX Polish Pack — остаток)

M9.8.3 Homepage Hero · M9.8.4 PLP Density · M9.8.6 UltraWide · M9.8.7 EC-01 · M9.8.8 Thumbnail Rail — per roadmap

---

## Next work rule

Before next SITE-002 change:

1. Read [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Use `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` as authority
3. For filter / catalog / 1C / price / PLP — follow Knowledge Map §13 domain-specific PRE-TASK rule
4. For trust block / certificates / dealers form / category CTA — follow Knowledge Map §14 + §13 Commercial Trust PRE-TASK rule
5. Live-capture any files touched before deploy
5. **Do not** start M10 without operator charter

Rollback = Beget full backup → current live TEST → file-level pass backups.

---

## SAFE UNKNOWN

- ocStore / OpenCart exact version and release line
- Beget backup artifact location and timestamp (operator attestation only)
- M10 scope and authorization status
- Who populates `price2`, `price3`, `discount1c` in production workflow

---

## Security notes

| Check | Value |
|-------|-------|
| No secrets in checkpoint docs | **yes** |
| DB JSON in repo (prior baselines) | Row data only — treat as sensitive; no credentials in dumps |
