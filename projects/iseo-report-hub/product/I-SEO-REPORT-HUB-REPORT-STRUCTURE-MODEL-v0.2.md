# I-SEO Report Hub — Report Structure Model v0.2

**Status:** PLANNING — report content structure for demo v0.2  
**project_id:** `iseo-report-hub`  
**Version:** v0.2  
**Created:** 2026-07-10  
**Implementation:** **NOT STARTED**

---

## 1. Status

This document **extends and refines** [I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md](I-SEO-REPORT-HUB-REPORT-MODEL-v0.1.md) with focus on **real report content structure** — the blocks, fields, and project-type emphasis needed for credible SEO reporting.

| Fact | State |
|------|-------|
| Purpose | Canonical structure model for static demo v0.2 and future product spec |
| Replaces v0.1 for content structure | **Partially** — v0.1 entity/cycle model remains valid; v0.2 adds block-level detail |
| Final product spec | **Not yet** — subject to SEO feedback after demo v0.2 |
| Static demo v0.1 | Mechanics only — **does not implement** this structure |

**Corpus alignment:** Structure informed by attested Denis (branded document) and Ilya (compact + Topvisor link) patterns in source corpus — not re-audited in this task.

---

## 2. Reporting Cycle

Approved model unchanged from v0.1:

| Element | Rule |
|---------|------|
| **Base period** | 1 calendar month |
| **Weekly checkpoints** | 3 preliminary (Week 1, 2, 3) |
| **Monthly final** | 4th report — month-close comprehensive report |
| **Weekly vs monthly** | Weekly ≠ copy of monthly; monthly ≠ naive rollup without interpretation |
| **Weekly client visibility** | **Internal by default** — client-facing delivery is monthly final after review |
| **Review gate** | Monthly report requires reviewer approval before client publication |

---

## 3. Universal Monthly Report Structure

Canonical block order for **Monthly Final Report**. All project types include this skeleton; profile-specific blocks insert or emphasize per §5.

### Block 1 — Cover / Meta

| Field | Visibility | Notes |
|-------|------------|-------|
| Client name | Client | |
| Site / project name | Client | |
| Site URL | Client | |
| Project type profile | Client | e.g. Service, E-commerce, Local |
| Reporting period | Client | Month YYYY |
| SEO specialist | Client | Name; optional photo — policy TBD |
| Reviewer | Internal default | May hide from client per policy |
| Report status | Internal | draft / review / approved / published |
| Publication date | Client | When published |
| Version number | Client + Internal | Published version identifier |

### Block 2 — Executive Summary

Short human-readable narrative (typically 2–4 paragraphs):

- What changed this month
- What matters for the client business
- Key wins and honest limitations
- Key risks in plain language
- Next focus preview

**Audience:** business owner / decision maker — not jargon-heavy.

### Block 3 — KPI Snapshot

Headline metrics grid (3–8 cards depending on profile):

| KPI category | Examples |
|--------------|----------|
| Traffic | Organic sessions/visits, YoY/MoM delta if available |
| Search visibility | Visibility index, impressions |
| Positions | TOP-10 / TOP-30 query counts |
| Leads/conversions | Forms, calls, orders |
| Technical health | Critical errors fixed, indexed priority pages |
| Commercial | Revenue/orders — e-commerce only if tracked |

Each card: **value**, **period**, **optional delta**, **short label**.

### Block 4 — Work Completed

Grouped completed works for the month:

| Sub-element | Content |
|-------------|---------|
| Work category | Technical SEO, Content/Semantic, Links, Analytics, Commercial factors, etc. |
| What was done | Dictionary-backed or free-text item |
| Why it matters | Client-readable benefit |
| Evidence | Link, screenshot, task reference |
| Status | Done / in progress / blocked |

**Source:** work dictionary (when available) + specialist narrative.

### Block 5 — Technical SEO

| Topic | Content |
|-------|---------|
| Crawl / indexing | Coverage changes, indexation issues resolved |
| Errors | 4xx/5xx, Search Console critical issues |
| Speed / CWV | Core Web Vitals if available |
| Duplicates / canonicals | Fixes applied |
| Sitemap / robots | Changes |
| Structured data | If relevant to project |

Omit or shorten if no technical work this month — do not show empty boilerplate.

### Block 6 — Semantic / Content Work

| Topic | Content |
|-------|---------|
| Pages/categories worked | List with URLs |
| Metadata | Title, description, H1 improvements |
| Texts | Rewrites, expansions |
| New content | New pages/articles/products |
| Clustering / semantic expansion | New query groups, semantic maps |
| Internal linking | Key linking work |

### Block 7 — Positions / Visibility

| Topic | Content |
|-------|---------|
| Topvisor link/card | Primary external report link (Ilya-style pattern) |
| Query group movement | Notable gains/losses by semantic group |
| TOP-10 / TOP-30 dynamics | Count changes |
| Winners / losers | Representative queries |
| Interpretation | Specialist explains movement — not raw tables only |

### Block 8 — Traffic / Behavior

| Topic | Content |
|-------|---------|
| Organic traffic | Sessions/users, trend |
| Landing pages | Top gainers/decliners |
| Engagement | Bounce, time on site if available |
| Anomalies | Seasonality, campaigns, tracking changes |
| Interpretation | Specialist narrative |

### Block 9 — Leads / Conversions

| Topic | Content |
|-------|---------|
| Forms / calls / orders | Counts if tracking exists |
| Conversion tracking quality | Goals configured, gaps |
| Changes vs prior period | Delta narrative |
| Limitations | Honest data gaps |

**Profile note:** Critical for service/local; important for e-commerce; optional emphasis for pure content sites.

### Block 10 — Links / Authority

| Topic | Content |
|-------|---------|
| External links | Acquired/placed links |
| Internal links | Strategic internal linking summary |
| Mentions | Brand mentions if tracked |
| Link risks | Toxic links, disavow notes |

**Optional block** — include when link work occurred or risks exist.

### Block 11 — Issues / Blockers / Risks

| Type | Examples |
|------|----------|
| Client-side blockers | Content approval delays, missing assets |
| Technical blockers | Dev queue, CMS limitations |
| Content approval | Waiting for client copy/photos |
| Tracking/data limitations | Missing goals, analytics gaps |

Honest status builds trust — not hidden until crisis.

### Block 12 — Plan for Next Month

| Element | Content |
|---------|---------|
| Priority works | 5–10 ordered items |
| Expected focus | Semantic, technical, content, links |
| Client actions needed | Explicit asks (approve texts, provide photos, fix tracking) |
| Dependencies | What blocks progress |

### Block 13 — Evidence / Appendix

Secondary/collapsible section:

- Screenshots
- External report links (Topvisor, Metrika, GSC exports)
- Task/ticket links (internal URLs stripped from client view)
- Uploaded materials
- Before/after examples

**UX principle:** available but not overwhelming main narrative.

---

## 4. Weekly Checkpoint Structure

Canonical blocks for **Week 1, 2, 3** checkpoints:

| # | Block | Content |
|---|-------|---------|
| 1 | **Week meta** | Week number (1–3), reporting month, project, specialist, status |
| 2 | **Short weekly summary** | 1–3 paragraphs — what happened this week |
| 3 | **Completed works** | Dictionary items or bullets — this week only |
| 4 | **Metrics / observations** | Notable metric changes; not full KPI deck |
| 5 | **Blockers** | Current blockers affecting progress |
| 6 | **Evidence links** | URLs, screenshots for week's work |
| 7 | **Next week plan** | 3–7 bullets for following week |
| 8 | **Internal notes** | Specialist-only technical notes |
| 9 | **Ready for review flag** | Submitted / draft / needs revision |

**Default visibility:** blocks 1–7 may have client-visible subsets; blocks 8–9 **internal only**.

---

## 5. Report Types / Project Types

Project type profile determines **emphasis**, **optional blocks**, and **KPI selection** — not a different cycle model.

### A. Service / Corporate Site SEO

**Typical clients:** B2B services, industrial services, professional services, corporate sites with lead goals.

**Emphasis:**

- Leads / forms / calls
- Service landing pages visibility
- Local/regional queries where applicable
- Commercial factors (contacts, trust, requisites)
- Technical health baseline
- Content/service pages expansion

**Typical extra blocks / fields:**

| Extra | Content |
|-------|---------|
| Priority service pages | URL list with position/traffic notes |
| Regional queries | Geo-targeted query groups |
| Lead quality notes | Qualitative feedback on lead types |
| Commercial factors checklist | Contacts, cases, certificates, pricing signals |

**De-emphasis:** product catalog indexing, filter/canonical e-commerce complexity.

---

### B. E-commerce SEO

**Typical clients:** Online stores, marketplaces, catalog-heavy retail.

**Emphasis:**

- Category and product page visibility
- Indexing coverage (categories, products, filters)
- Faceted navigation / filter / canonical issues
- Product availability and duplicate content
- Commercial snippets (price, availability in SERP)
- Revenue/orders if tracking available
- Large semantics (category clusters)

**Typical extra blocks / fields:**

| Extra | Content |
|-------|---------|
| Category cluster progress | Cluster map, pages optimized |
| Product/indexing issues | Out of stock, thin descriptions, duplicate URLs |
| Filters / canonicals | Facet indexing policy, fixes |
| Availability / content gaps | Missing descriptions, attributes |
| Top categories | Performance by category branch |

**De-emphasis:** pure content cluster articles unless hybrid store.

---

### C. Content / Information SEO

**Typical clients:** Media, blogs, info portals, knowledge bases.

**Emphasis:**

- Articles and topical clusters
- Organic traffic growth to content
- Informational query coverage
- Internal linking between articles
- Content freshness and updates
- Indexing of new content

**Typical extra blocks / fields:**

| Extra | Content |
|-------|---------|
| Content plan | Planned vs published |
| Published/updated articles | List with URLs |
| Cluster coverage | Topic cluster completion % |
| Traffic by content group | Section/blog category breakdown |

**De-emphasis:** lead forms (unless present), e-commerce metrics.

---

### D. Local / Regional SEO

**Typical clients:** Regional service businesses, multi-city operators, local franchises.

**Emphasis:**

- Geo-targeted query visibility
- Maps / business profile if relevant (**SAFE UNKNOWN** integration depth)
- Regional landing pages
- Local trust and commercial factors
- NAP consistency, regional contacts

**Typical extra blocks / fields:**

| Extra | Content |
|-------|---------|
| Regional visibility | City/region query groups |
| Local landing pages | Geo pages created/updated |
| Contacts / requisites / commercial trust | Trust block improvements |
| Regional cases / reviews | Social proof by region |

**Note:** May overlap with Service profile — operator may tag primary as `local` when geo is dominant.

---

## 6. Internal Admin Fields vs Client-Facing Fields

### Visibility classes

| Class | Description | Examples |
|-------|-------------|----------|
| **internal-only** | Never in client render | Internal notes, reviewer comments, raw task URLs, readiness flags |
| **reviewer-only** | Visible to reviewer, not client | Review checklist, revision requests, approval audit |
| **client-visible** | In published monthly report | Executive summary, KPIs, works (client wording), plan, risks (sanitized) |
| **data-source** | Metadata for import/link | Topvisor URL, Metrika counter ID — may show as link card, not raw config |
| **evidence** | Attachments and links | May be client-visible selectively per item flag |

### Field rules

1. **Published Report Version** snapshot strips all `internal-only` and `reviewer-only` fields.
2. Weekly **internal notes** never appear in client monthly unless explicitly rolled up by specialist into client-visible summary.
3. **Work dictionary** may have `client_facing_wording` distinct from `internal_notes`.
4. **Blockers** may have internal detail + client-safe summary variants.
5. **Reviewer name** — policy TBD for client footer.

### Admin vs client render

| Surface | Purpose |
|---------|---------|
| Admin weekly editor | All fields including internal |
| Admin monthly editor | Full block set + validation panel |
| Review queue | Reviewer fields + diff/history — **SAFE UNKNOWN** depth |
| Client web report | Client-visible blocks only, professional layout |

---

## 7. Demo v0.2 Implications

Static demo v0.1 status (operator review 2026-07-10):

| v0.1 state | Limitation |
|------------|------------|
| Workflow mechanics | ✓ Demonstrated |
| Report field structure | ✗ Generic placeholders |
| Project type differentiation | ✗ Single e-commerce demo project |
| Corpus-realistic content | ✗ Not grounded in report patterns |

**Demo v0.2 must:**

1. Replace generic fields with blocks defined in §3–§4
2. Add **report type / project profile** selector or visible profile badge per project
3. Show **3 distinct demo projects** (Service, E-commerce, Local) — see [I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md](I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md)
4. Show **different block emphasis** per project type on monthly editor and client report
5. Show **one monthly report per project** with realistic sanitized content
6. Show **weekly checkpoints** (W1–W3) feeding monthly narrative — condensed rollup on monthly/client views

**Demo v0.2 must NOT:**

- Be shown to SEO specialists as final product
- Claim backend, persistence, or platform implementation exists
- Use real client names, domains, or metrics

---

## 8. Mapping to Existing Docs

| Document | v0.2 relationship |
|----------|-------------------|
| REPORT-MODEL v0.1 | Entity model (cycle, checkpoint, monthly) — still valid |
| WEB-REPORT-STRUCTURE v0.1 | Client layout skeleton — v0.2 blocks populate that skeleton |
| ADMIN-UX-FLOW v0.1 | Screen flow unchanged; field inventory expands |
| DEMO-CONTENT-PACK v0.1 | Sanitized content for 3 projects |

---

## 9. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Final metric catalog per profile | **UNKNOWN** — refine after SEO feedback |
| Exact data import sources (Metrika, GSC, Topvisor API) | **UNKNOWN** — MVP manual entry assumed |
| Topvisor integration depth beyond external link | **UNKNOWN** |
| Client-visible weekly checkpoint policy | **UNKNOWN** — internal default |
| Chart rendering library and data binding | **UNKNOWN** |
| Evidence storage (WP media vs app storage) | **UNKNOWN** — platform dependent |
| Review workflow strictness (mandatory fields, checklist) | **UNKNOWN** |
| Work dictionary final sanitized content | **UNKNOWN** — extraction pending |
| Versioning (immutable snapshot vs editable published) | **UNKNOWN** |
| Multi-language reports | **UNKNOWN** — Russian default assumed |

---

## Document control

- **Created:** 2026-07-10
- **Supersedes for block detail:** generic placeholders in demo v0.1; extends REPORT-MODEL v0.1
- **Does not claim:** implementation, demo v0.2 build, or SEO sign-off
