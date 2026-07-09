# I-SEO Report Hub — Client Web Report Structure v0.1

**Status:** PLANNING — documentation-first only  
**Implementation:** **NOT STARTED** — no HTML, no theme, no renderer  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10

---

## 1. Status and Scope

This document defines the **planned structure of client-facing web reports** rendered on i-seo.su by WordPress.

| In scope | Out of scope |
|----------|--------------|
| Monthly and optional weekly web layouts | HTML/CSS implementation |
| Block types for client render | PDF export engine |
| URL strategy discussion (no final security design) | Client portal login |
| Topvisor MVP presentation | iframe embed (later) |
| Responsive/UX requirements | Website Factory prototype build |

**Primary client output:** controlled web pages on i-seo.su from **approved Published Report Version** only.

---

## 2. Report URL Strategy

### Principles

- Client reports are **not** public blog posts with guessable sequential IDs as the canonical delivery model.
- Delivery via **controlled private links** — exact mechanism deferred to implementation security gate.

### Candidates (not final)

| Approach | Notes |
|----------|-------|
| **Opaque token path** | e.g. `/report/{opaque-token}` — token mapped to Published Version |
| **Slug + secret** | Human-readable slug plus required query token |
| **Time-limited token** | Expiry/revocation — **SAFE UNKNOWN** |
| **Authenticated access** | Client login — **later optional**, not MVP |

### Requirements (product level)

- Draft reports **must not** be reachable at client URLs.
- Revoked versions return safe "unavailable" response.
- URLs shareable by account manager to client (email/messenger) — no operator login required for client in MVP.
- Avoid exposing internal project IDs in URL where possible.

**Do not** finalize security implementation in this document.

---

## 3. Monthly Final Web Report Structure

Top-to-bottom layout for approved monthly client web report:

### 3.1 Page skeleton

```
┌─────────────────────────────────────────────────────────────┐
│ HEADER — i-SEO branding, logo, report title                 │
├─────────────────────────────────────────────────────────────┤
│ META — Client name · Project/site · Period (Month YYYY)     │
├─────────────────────────────────────────────────────────────┤
│ EXECUTIVE SUMMARY — narrative                               │
├─────────────────────────────────────────────────────────────┤
│ KEY KPI CARDS — 3–6 headline metrics                        │
├─────────────────────────────────────────────────────────────┤
│ TRAFFIC BLOCK — chart/table + short interpretation          │
├─────────────────────────────────────────────────────────────┤
│ POSITIONS / VISIBILITY — metrics + Topvisor external card   │
├─────────────────────────────────────────────────────────────┤
│ LEADS / CONVERSIONS — if profile applicable                 │
├─────────────────────────────────────────────────────────────┤
│ COMPLETED WORKS — grouped list from dictionary wording      │
├─────────────────────────────────────────────────────────────┤
│ WEEKLY PROGRESS SUMMARY — optional condensed week 1–3       │
├─────────────────────────────────────────────────────────────┤
│ PROFILE BLOCKS — technical / content / link / local / ecom  │
│   (only blocks enabled for project profile)                 │
├─────────────────────────────────────────────────────────────┤
│ RISKS / BLOCKERS — if any                                   │
├─────────────────────────────────────────────────────────────┤
│ NEXT MONTH PLAN                                             │
├─────────────────────────────────────────────────────────────┤
│ EVIDENCE / APPENDIX — collapsible or secondary section      │
├─────────────────────────────────────────────────────────────┤
│ EXTERNAL REPORT LINKS — Topvisor card prominent             │
├─────────────────────────────────────────────────────────────┤
│ FOOTER — publication date, version, i-SEO contact           │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 Section notes

| Section | Client-facing intent |
|---------|---------------------|
| **Header** | Professional i-SEO branded cover — informed by Denis-style corpus (branded document) |
| **Meta** | Clear client/project/period without internal IDs |
| **Executive summary** | Business-owner readable; no jargon overload |
| **KPI cards** | Scannable wins; manual metrics in MVP |
| **Traffic / Positions / Leads** | Core SEO story; charts from entered data |
| **Completed works** | Standardized dictionary wording |
| **Weekly progress summary** | Optional rollup — not full weekly paste |
| **Profile blocks** | Only applicable sections render (no empty placeholders) |
| **Risks/blockers** | Honest status; builds trust |
| **Next month plan** | Forward-looking commitments |
| **Evidence** | Available but not overwhelming — collapsible recommended |
| **External links** | Topvisor: link card + optional screenshot preview (Ilya-style pattern) |
| **Footer** | Version metadata (`Published: YYYY-MM-DD`, version N) |

---

## 4. Weekly Client Report Structure

### If weekly checkpoint is client-visible (policy optional)

Short single-page layout:

| Block | Content |
|-------|---------|
| Header | i-SEO branding, project, week N of month |
| Summary | Week status narrative |
| Completed work | Dictionary items this week |
| Important changes | Metric highlights |
| Blockers | If any |
| Next step | Next week plan |
| Evidence links | Selected client-visible evidence |

### If not client-visible (MVP default assumption)

Weekly checkpoints remain **internal only** — no public URL. Monthly final is primary client delivery.

**Operator decision:** weekly client visibility — **SAFE UNKNOWN** for MVP.

---

## 5. Report Blocks

Block types for client web renderer:

| Block type | Renders |
|------------|---------|
| **text / narrative** | Prose sections (summary, interpretation, plan) |
| **metric cards** | Grid of label + value + optional delta |
| **chart** | Line/bar/donut from metric snapshots |
| **table** | Tabular metrics or rankings |
| **completed work list** | Grouped dictionary items with optional sub-notes |
| **evidence list** | Links and thumbnails |
| **external report card** | Provider icon, label, CTA link to Topvisor/etc. |
| **screenshot gallery** | Lightbox-friendly image grid |
| **status badge** | Week/cycle status for weekly (if shown) |
| **appendix** | Secondary collapsible content |

**Rendering rule:** Block order follows `sort_order` from approved Published Version snapshot. Internal-visibility blocks omitted.

---

## 6. Topvisor Presentation

### MVP (required pattern support)

| Element | Behavior |
|---------|----------|
| **External link card** | Title, description, button "Открыть отчёт Topvisor" → `target="_blank"` |
| **Screenshot preview** | Optional thumbnail below card |
| **Export attachment** | Optional downloadable file link |

### Explicitly not MVP-required

- Live iframe/embed
- API-synced position tables
- Automated refresh

### Later (optional)

- API snapshot block with dated import
- iframe only if technically, legally, and security-reviewed

---

## 7. Responsive / UX Requirements

Client report must be:

| Requirement | Detail |
|-------------|--------|
| **Clean** | White space, clear hierarchy, i-SEO brand consistent with site |
| **Readable** | Business owner audience; 16px+ body; contrast compliant |
| **Mobile friendly** | KPI cards stack; tables scroll or simplify; charts responsive |
| **Not overloaded** | Progressive disclosure for evidence/appendix |
| **Professional** | Suitable for forwarding to stakeholders |
| **Evidence available** | But secondary — not dominating main narrative |
| **Print-friendly** | Optional CSS print styles — **SAFE UNKNOWN** priority |

**Corpus alignment:** Blend Denis branded clarity with Ilya compact metrics/link utility — unified block system, not two separate products.

---

## 8. Website Factory Demo Candidate

**High priority** for future Website Factory HTML prototype (operator charter required):

- Full **monthly client web report page** with sample data
- Individual **block components**: KPI cards, work list, Topvisor card, evidence gallery
- Desktop + mobile breakpoints per MARS gulp starter conventions

Purpose: validate visual treatment and block composition **before** WordPress renderer implementation.

**No prototype created in this task.**

---

## 9. Security Notes

| Rule | Requirement |
|------|-------------|
| Only approved reports | Renderer reads Published Report Version only |
| No draft access | Draft preview uses separate admin-only route with watermark |
| No secrets | No credentials, internal URLs with tokens, or admin paths in client HTML |
| No internal notes | Strip `visibility: internal` content from snapshot |
| Version metadata | Show publish date/version; not internal reviewer names unless policy allows |
| Revocation | Revoked versions must not render report body |

---

## 10. SAFE UNKNOWN

| Topic | Notes |
|-------|-------|
| Exact URL pattern and token entropy | Security implementation gate |
| Token expiry policy | Business vs security tradeoff |
| Weekly public URLs | Policy |
| Chart library on front-end | Product + Anton decision |
| Comparison to previous month in UI | Delta display |
| PDF "Save as PDF" browser print | vs server PDF later |
| i-SEO site theme integration vs standalone report template | WP theme decision |
| Language | Russian default assumed |
| Client logo in header | Optional per client |

---

## Document control

- **Does not claim:** any web report page or renderer exists on i-seo.su
- **Upstream:** [I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md), [I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md](I-SEO-REPORT-HUB-ADMIN-UX-FLOW-v0.1.md)
- **Website Factory:** prototype lane only — not production renderer
