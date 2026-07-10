# I-SEO Report Hub — Report Type Block Matrix v0.1

**Status:** PLANNING — full block matrix by project/site type  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10  
**Implementation:** **NOT STARTED** — not final DB schema

---

## 1. Status

| Fact | State |
|------|-------|
| Purpose | Canonical **block inclusion matrix** by project type for demo v0.3 and future product design |
| Relationship | Implements §4–§5 of [I-SEO-REPORT-HUB-REPORT-CONTENT-ARCHITECTURE-v0.1.md](I-SEO-REPORT-HUB-REPORT-CONTENT-ARCHITECTURE-v0.1.md) |
| Structure model | Aligns with [I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md](I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md) universal 13-block skeleton |
| DB schema | **Not final** — matrix is product/content spec only |

---

## 2. Legend

| Mark | Meaning |
|------|---------|
| **Required** | Must be present and filled before monthly submit/publish (profile-dependent validation) |
| **Recommended** | Expected for credible report; warn if empty |
| **Optional** | Include when relevant work occurred |
| **Internal only** | Never in client Published Snapshot |
| **Not usually used** | Omitted by default for this profile; enable manually in Mixed/Custom |

---

## 3. Universal Blocks

Default visibility for blocks present across all project types (monthly final).

| Block | Default visibility | Typical role |
|-------|-------------------|--------------|
| Meta | Client | Context |
| Executive Summary | Client | Month narrative |
| KPI Snapshot | Client | Headline metrics |
| Work Completed | Client | Grouped works |
| Technical SEO | Client | Technical category |
| Semantic / Content | Client | Content/meta category |
| Positions / Visibility | Client | Rankings + Topvisor |
| Traffic / Behavior | Client | Organic traffic story |
| Leads / Conversions | Client (profile-dependent emphasis) | Business outcomes |
| Links / Authority | Client (optional) | Link work summary |
| Issues / Blockers / Risks | Client (sanitized) | Honest status |
| Plan for Next Month | Client | Forward plan + client actions |
| Evidence / Appendix | Client (selective items) | Supporting materials |
| Client Actions Needed | Client | Explicit subsection of Plan or standalone callout |
| Data Quality Notes | Internal only | Tracking gaps, source limitations |
| Review Notes | Reviewer only | Checklist, revision requests |

---

## 4. Service / Corporate Site Block Set

**Profile ID:** `service_corporate`

### Monthly block matrix

| Block | Inclusion | Visibility |
|-------|-------------|------------|
| Meta | Required | Client |
| Executive Summary | Required | Client |
| KPI Snapshot | Required | Client |
| Work Completed | Required | Client |
| **Service Pages** | Required | Client |
| **Leads / Calls / Forms** | Required | Client |
| Technical SEO | Required | Client |
| Semantic / Content | Required | Client |
| **Commercial Factors** | Required | Client |
| Positions / Visibility | Required | Client |
| Traffic / Behavior | Recommended | Client |
| Links / Authority | Optional | Client |
| Issues / Blockers | Required | Client |
| Plan for Next Month | Required | Client |
| Client Actions Needed | Required | Client |
| Evidence / Appendix | Required | Client |
| Data Quality Notes | Recommended | Internal only |
| Review Notes | Required | Reviewer only |
| Category Pages | Not usually used | — |
| Product Pages | Not usually used | — |
| Indexing Coverage (catalog) | Not usually used | — |
| Content Plan (editorial) | Optional | Client |

### Extra fields (Service / Corporate)

| Field | Required | Notes |
|-------|----------|-------|
| Priority services (URL list) | Required | Core commercial pages |
| Regions (if applicable) | Recommended | Geo-targeted service areas |
| Lead quality notes | Recommended | Qualitative feedback |
| Conversion tracking state | Required | Goals configured / gaps |
| Commercial trust checklist | Required | Contacts, cases, certs, pricing signals |
| Client approvals needed | Required | Pending content/assets |

---

## 5. E-commerce Block Set

**Profile ID:** `ecommerce`

### Monthly block matrix

| Block | Inclusion | Visibility |
|-------|-------------|------------|
| Meta | Required | Client |
| Executive Summary | Required | Client |
| KPI Snapshot | Required | Client |
| Work Completed | Required | Client |
| **Category Pages** | Required | Client |
| **Product Pages** | Required | Client |
| **Indexing Coverage** | Required | Client |
| **Filters / Faceted Navigation** | Required | Client |
| **Semantic Expansion** | Required | Client |
| **Internal Linking** | Required | Client |
| Positions / Visibility | Required | Client |
| Traffic / Behavior | Required | Client |
| **Orders / Leads** | Required | Client |
| Technical SEO | Recommended | Client |
| Semantic / Content (general) | Recommended | Client (may merge with Category/Product) |
| Links / Authority | Optional | Client |
| Issues / Blockers | Required | Client |
| Plan for Next Month | Required | Client |
| Client Actions Needed | Required | Client |
| Evidence / Appendix | Required | Client |
| Data Quality Notes | Required | Internal only (CRM ↔ analytics gaps common) |
| Review Notes | Required | Reviewer only |
| Service Pages | Not usually used | — |
| Regional Landing Pages | Optional | Client (if geo store) |

### Extra fields (E-commerce)

| Field | Required | Notes |
|-------|----------|-------|
| Category clusters | Required | Priority branch map |
| Product availability | Required | Out-of-stock / thin content policy |
| Duplicate / filter risks | Required | Facet indexing status |
| Catalog structure notes | Recommended | Feed, URL patterns |
| Snippets / metadata | Recommended | Price, availability in SERP |
| Top categories | Required | Performance focus list |
| Unavailable products count | Recommended | Index cleanup backlog |

---

## 6. Content / Information Site Block Set

**Profile ID:** `content_information`

### Monthly block matrix

| Block | Inclusion | Visibility |
|-------|-------------|------------|
| Meta | Required | Client |
| Executive Summary | Required | Client |
| KPI Snapshot | Required | Client |
| Work Completed | Required | Client |
| **Content Plan** | Required | Client |
| **Published / Updated Materials** | Required | Client |
| **Topic Clusters** | Required | Client |
| **Organic Traffic** | Required | Client |
| Positions / Visibility | Required | Client |
| **Internal Linking** | Required | Client |
| **Content Freshness** | Required | Client |
| Technical SEO | Recommended | Client |
| Semantic / Content | Recommended | Client |
| Traffic / Behavior | Recommended | Client (may merge with Organic Traffic) |
| Leads / Conversions | Optional | Client |
| Links / Authority | Optional | Client |
| Issues / Blockers | Required | Client |
| Plan for Next Month | Required | Client |
| Client Actions Needed | Recommended | Client |
| Evidence / Appendix | Required | Client |
| Data Quality Notes | Recommended | Internal only |
| Review Notes | Required | Reviewer only |
| Category Pages | Not usually used | — |
| Commercial Factors | Optional | Client |

### Extra fields (Content / Information)

| Field | Required | Notes |
|-------|----------|-------|
| Topic cluster map | Required | Clusters in progress / done |
| Article status | Required | Draft / published / updated |
| Traffic by content group | Required | Section/blog breakdown |
| Outdated content list | Recommended | Refresh candidates |
| Content gaps | Recommended | Missing topics vs plan |

---

## 7. Local / Regional SEO Block Set

**Profile ID:** `local_regional`

### Monthly block matrix

| Block | Inclusion | Visibility |
|-------|-------------|------------|
| Meta | Required | Client |
| Executive Summary | Required | Client |
| KPI Snapshot | Required | Client |
| Work Completed | Required | Client |
| **Regional Landing Pages** | Required | Client |
| **Geo Queries** | Required | Client |
| **Leads / Calls / Forms** | Required | Client |
| **Local Trust / Commercial Factors** | Required | Client |
| **Contacts / Requisites** | Required | Client |
| Technical SEO | Required | Client |
| Positions / Visibility | Required | Client |
| Semantic / Content | Recommended | Client |
| Traffic / Behavior | Recommended | Client |
| Service Pages | Recommended | Client (overlap with Service profile) |
| Issues / Blockers | Required | Client |
| Plan for Next Month | Required | Client |
| Client Actions Needed | Required | Client |
| Evidence / Appendix | Required | Client |
| Data Quality Notes | Recommended | Internal only |
| Review Notes | Required | Reviewer only |
| Category Pages | Not usually used | — |
| Product Pages | Not usually used | — |

### Extra fields (Local / Regional)

| Field | Required | Notes |
|-------|----------|-------|
| Target regions | Required | Cities / areas |
| Local landing pages inventory | Required | URLs + status |
| Local proof / cases | Recommended | Geo-tagged examples |
| Map / profile notes | Optional | **SAFE UNKNOWN** integration depth |
| Contact completeness | Required | NAP, hours, schema |

---

## 8. Mixed / Custom Project

**Profile ID:** `mixed_custom`

### Rules

1. **Starts with universal blocks** — Meta, Executive Summary, KPI Snapshot, Work Completed, Issues, Plan, Evidence always Required.
2. **Operator/admin selects modules** from any profile block set via checklist.
3. **Minimum credible set** — KPI + Work + Risks + Plan + Evidence cannot be disabled.
4. **KPI card set** — operator picks 3–8 KPIs from union of profile KPI libraries.
5. **Validation** — warn on unusual combinations (e.g. Product Pages without E-commerce type note).

### Suggested module picker groups

| Group | Example modules |
|-------|-----------------|
| Commercial | Service Pages, Leads, Commercial Factors, Orders |
| Catalog | Category Pages, Product Pages, Indexing, Filters |
| Content | Content Plan, Topic Clusters, Content Freshness |
| Local | Regional Landing, Geo Queries, Contacts/Requisites |
| Performance | Traffic, Positions, Links |

---

## 9. Weekly Block Matrix

Required weekly content by project type (all types share skeleton; emphasis differs).

### Universal weekly requirements

| Weekly content | All types |
|----------------|-----------|
| Completed works | Required |
| Metrics observed | Required |
| Blockers | Required (or explicit «none») |
| Evidence | Recommended |
| Next week plan | Required |
| Internal notes | Optional |
| Review readiness | Required by Week 3 |

### Weekly emphasis by project type

| Project type | Week 1 focus | Week 2 focus | Week 3 focus |
|--------------|--------------|--------------|--------------|
| **Service / Corporate** | Technical baseline; priority service meta | Service page content; commercial factors | Lead tracking check; monthly draft |
| **E-commerce** | Indexing/filter audit; category meta | Category text; SKU descriptions | Catalog dev blockers; monthly KPI draft |
| **Content / Information** | Content plan alignment | Publish/update articles | Cluster linking; traffic observation |
| **Local / Regional** | Regional landing drafts; schema | Publish geo pages; trust blocks | NAP/map tasks; geo query movement |
| **Mixed / Custom** | Per enabled modules | Per enabled modules | Completeness toward enabled module set |

### Weekly internal-only fields (all types)

- Raw crawl notes
- Uncertain metric readings
- Internal task URLs
- Reviewer prep notes

---

## 10. Client Visibility Matrix

| Block / field type | Client-visible | Internal-only | Reviewer-only | Source/evidence |
|--------------------|----------------|---------------|---------------|-----------------|
| Meta (client fields) | ✓ | | | |
| Meta (reviewer, draft status) | | ✓ | ✓ | |
| Executive Summary | ✓ | | | |
| KPI Snapshot | ✓ | | | |
| Work Completed | ✓ | | | |
| Profile blocks (client wording) | ✓ | | | |
| Positions + Topvisor card | ✓ | | | source link |
| Traffic / Leads interpretation | ✓ | | | |
| Issues (client-safe summary) | ✓ | | | |
| Issues (internal detail) | | ✓ | ✓ | |
| Plan + Client Actions | ✓ | | | |
| Evidence (flagged items) | ✓ | | | ✓ |
| Evidence (internal-only) | | ✓ | ✓ | ✓ |
| Data Quality Notes | | ✓ | ✓ | |
| Review Notes | | | ✓ | |
| Weekly internal notes | | ✓ | ✓ | |
| Weekly full checkpoint | | ✓ default | ✓ | |

**Published Snapshot rule:** include only client-visible + approved blocks; strip all internal-only and reviewer-only fields.

---

## 11. Demo v0.3 Mapping

| Demo project | Type | Reporting state | Block matrix emphasis |
|--------------|------|-----------------|----------------------|
| **Project A — Регион Сервис** | Local / Regional | **Complete final report** | Full Local block set; all Required filled; client report published |
| **Project B — Industrial Tools** | E-commerce | **Week 3 in progress** | E-commerce Required blocks partial; W1+W2 weekly complete; monthly draft accumulating |
| **Project C — Инжиниринг Сервис** | Service / Corporate | **Week 1 in progress** | Service Required blocks mostly empty; W1 draft only; monthly shell |

### Cross-demo visibility demo

| Project | Client report | Reason if not ready |
|---------|---------------|---------------------|
| A — Регион Сервис | Available | Approved + published |
| B — Industrial Tools | Not ready | Monthly draft incomplete; Week 3 needs review; missing traffic interpretation |
| C — Инжиниринг Сервис | Not ready | Week 1 only; monthly blocks empty; insufficient period coverage |

---

## 12. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Exact block sort order when profile blocks insert into universal skeleton | **UNKNOWN** — demo v0.3 UX decision |
| Strict vs warn validation for Recommended blocks | **UNKNOWN** |
| Block Library admin UI for Mixed/Custom | **UNKNOWN** |

---

## Document control

- **Created:** 2026-07-10
- **Does not claim:** demo v0.3 built or database schema finalized
