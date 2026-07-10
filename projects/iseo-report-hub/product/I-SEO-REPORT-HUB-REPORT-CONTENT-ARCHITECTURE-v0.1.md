# I-SEO Report Hub — Report Content Architecture v0.1

**Status:** PLANNING — report content architecture (deeper than structure model)  
**project_id:** `iseo-report-hub`  
**Version:** v0.1  
**Created:** 2026-07-10  
**Implementation:** **NOT STARTED**

---

## 1. Status

| Fact | State |
|------|-------|
| Document type | Planning / specification — **content logic**, not UI implementation |
| Depth | **Deeper than** [I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md](I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md) — defines *what goes inside* blocks, not only block inventory |
| Static demo v0.2 | Direction accepted by operator; **content depth insufficient** |
| Target consumer | Static demo v0.3, future product spec, SEO feedback charter |
| Final product spec | **Not yet** — subject to operator review of v0.3 and deferred SEO feedback |
| Runtime / code | **Does not exist** |

This document defines **report content architecture** — the philosophy, objects, flows, visibility rules, and quality standards that govern what a credible i-SEO monthly report and weekly checkpoint must contain.

**Upstream authority:**
- [I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md](I-SEO-REPORT-HUB-REPORT-STRUCTURE-MODEL-v0.2.md) — 13-block monthly skeleton, 9-block weekly skeleton
- [I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md](I-SEO-REPORT-HUB-DEMO-CONTENT-PACK-v0.1.md) — sanitized demo narratives (to be extended by staged states in v0.3)
- Operator review 2026-07-10 — v0.2 mechanics and direction accepted; content architecture needed before v0.3

**Companion documents:**
- [I-SEO-REPORT-HUB-REPORT-TYPE-BLOCK-MATRIX-v0.1.md](I-SEO-REPORT-HUB-REPORT-TYPE-BLOCK-MATRIX-v0.1.md) — full block matrix by project type
- [I-SEO-REPORT-HUB-DEMO-REPORT-STATES-v0.1.md](I-SEO-REPORT-HUB-DEMO-REPORT-STATES-v0.1.md) — staged demo scenarios for v0.3

---

## 2. Report Philosophy

An i-SEO Report Hub report is **not** an activity log, task dump, or raw export from Topvisor/Metrika. It is a **structured business communication** that connects SEO work to client outcomes.

### Primary audiences

| Audience | Need |
|----------|------|
| **Client (business owner / decision maker)** | Understand what changed, why it matters, what risks exist, what happens next — without SEO jargon overload |
| **SEO specialist (author)** | Capture work, evidence, interpretation, blockers, and plan in one place; reuse dictionary; submit for review |
| **SEO lead / reviewer** | Verify completeness, quality, honesty, and client-readiness before publication |

### Core principles

1. **Work → evidence → interpretation → next actions** — every meaningful claim in the report should trace this chain where possible.
2. **Not just activity** — listing tasks without purpose, outcome, or client benefit is insufficient.
3. **Facts vs interpretation vs risks vs plans** — keep these layers distinct inside blocks; do not merge speculation into KPI tables.
4. **Honest limitations** — tracking gaps, client delays, and data quality issues are reported calmly, not hidden.
5. **No overpromising** — avoid guarantees («TOP-1», «гарантированный рост»); use observed changes and qualified forecasts.
6. **Reviewable before client-facing** — internal detail may be richer; client snapshot is a curated subset after approval.
7. **Project-type awareness** — a service site report emphasizes leads and service pages; e-commerce emphasizes catalog/indexing; content emphasizes clusters; local emphasizes geo visibility.

### What a good report achieves

- Client can explain to stakeholders **what SEO did this month** and **why it mattered**.
- Specialist can defend work with **evidence links** and **metric context**.
- Reviewer can assess **completeness and tone** without re-interviewing the specialist.
- Next month plan is **actionable** — concrete items, owners or dependencies, client asks explicit.

---

## 3. Core Report Objects

Logical entities for content architecture (not DB schema):

### Client

Legal or commercial entity receiving reports. Attributes relevant to content: name, contact context, approval culture (fast/slow), tracking maturity.

### Project

Engagement container: one client may have multiple SEO projects (sites, brands, regions). Attributes: name, assigned specialist, reviewer, reporting calendar.

### Site

URL or site group under a project. One project may map to one primary site in MVP.

### Project Type

Profile selector determining block emphasis and extra fields. See §4 and Block Matrix v0.1.

Values: `service_corporate`, `ecommerce`, `content_information`, `local_regional`, `mixed_custom`.

### Reporting Period

Calendar month (YYYY-MM). Base unit for monthly final report.

### Weekly Checkpoint

One of three preliminary reports within a reporting period (Week 1, 2, 3). Feeds monthly synthesis; **internal by default** for client delivery.

### Monthly Report

Month-close comprehensive report — primary client deliverable after review and publish.

### Report Block

Atomic content section (e.g. Executive Summary, KPI Snapshot, Technical SEO). Has title, visibility, status, and structured sub-fields per §5.

### Work Item

Dictionary-backed or free-text unit of completed/planned work. Fields: category, description, purpose (why), evidence, status.

### KPI

Headline metric snapshot: label, value, period, optional delta, optional interpretation note.

### Evidence

Link, screenshot, export, or task reference supporting a work item or metric claim. May be client-visible or internal per item flag.

### Risk / Blocker

Issue affecting progress: type (client / technical / data / content approval), description, owner or dependency, client-safe summary variant.

### Plan Item

Forward-looking action for next week or next month: priority, description, dependency, client action flag.

### Reviewer Comment

Internal or specialist-visible note from review workflow; never auto-published to client unless rolled into approved client text.

### Published Snapshot

Immutable (or versioned) client-visible render of approved monthly report — strips internal-only and reviewer-only fields.

---

## 4. Project Type Selection

Explicit selector at project creation or first cycle setup. Operator or admin chooses **one primary type**; secondary emphases may be noted in Mixed/Custom.

### Selection model

| Project Type | When to choose | Required extra fields | Default report blocks | Optional blocks |
|--------------|----------------|----------------------|------------------------|-----------------|
| **Service / Corporate Site** | B2B/B2C services, corporate sites, lead-generation focus, service landing pages | Priority services (URL list); regions if applicable; lead tracking state; conversion goals | Universal skeleton + Service Pages, Leads/Calls/Forms, Commercial Factors | Links/Authority; Traffic deep-dive if low lead volume |
| **E-commerce** | Online store, catalog, marketplace, product/category SEO | Category clusters; top categories; product availability policy; filter/canonical policy | Universal + Category Pages, Product Pages, Indexing Coverage, Filters/Faceted Nav, Orders/Leads | Content clusters if hybrid blog+store |
| **Content / Information** | Media, blog, info portal, knowledge base | Topic clusters; content plan; content groups for traffic | Universal + Content Plan, Published/Updated Materials, Topic Clusters, Content Freshness | Leads if present; Links if active |
| **Local / Regional** | Geo-dominant service business, multi-city, franchise | Target regions; regional landing inventory; NAP/map notes; local trust checklist | Universal + Regional Landing Pages, Geo Queries, Local Trust, Contacts/Requisites | Service pages overlap with Service type |
| **Mixed / Custom** | Hybrid (store + content + local), or non-standard engagement | Operator-selected module checklist; primary KPI set | Universal blocks (KPI, Work, Risks, Plan, Evidence) always | Any profile-specific modules enabled manually |

### Selection rules

1. **One primary type per project** — drives default block matrix and KPI set.
2. **Overlap is normal** — Local may share Service blocks; E-commerce hybrid may enable Content modules in Mixed/Custom.
3. **Type change mid-engagement** — allowed with admin action; historical reports retain original profile snapshot (**SAFE UNKNOWN** migration UX).
4. **Demo v0.3** — must show type selector and visibly different block emphasis per assigned demo project.

### Decision helper (operator)

```
Lead/conversion goal on service pages?     → Service / Corporate (or Local if geo-dominant)
Product/category catalog SEO?              → E-commerce
Article/traffic/content cluster growth?    → Content / Information
City/region queries and geo landing focus? → Local / Regional
Multiple of the above equally?             → Mixed / Custom
```

---

## 5. Universal Report Block Anatomy

Every report block — universal or profile-specific — shares a common content anatomy for admin editor, review, and client render.

| Element | Purpose |
|---------|---------|
| **Block title** | Human-readable section name (may differ slightly client vs admin) |
| **Visibility** | `client` / `internal` / `reviewer` / `source` (data-source metadata) |
| **Status** | `empty` / `draft` / `needs_review` / `approved` / `published` |
| **Short client summary** | 1–3 sentences for client render or executive rollup |
| **Internal note** | Specialist/reviewer technical detail; never auto-client |
| **Data source** | Topvisor URL, Metrika counter, GSC export, manual entry — provenance |
| **Evidence** | Links, screenshots, attachments supporting this block |
| **Interpretation** | Specialist explains *what the numbers/work mean* for the business |
| **Next action** | Block-level forward item if section implies follow-up (e.g. unresolved technical issue) |
| **Owner** | Specialist default; blocker owner if different |
| **Updated date** | Last content edit timestamp |

### Status semantics

| Status | Meaning |
|--------|---------|
| `empty` | Block not started — valid early in cycle |
| `draft` | Content started, incomplete |
| `needs_review` | Submitted or flagged for reviewer attention |
| `approved` | Reviewer accepted block content for publication eligibility |
| `published` | Included in Published Snapshot (monthly final only) |

### Block maturity in demo v0.3

Monthly editor must show **per-block status** and completeness — operator should see why a report is not client-ready (e.g. Week 1 project with mostly `empty` blocks).

---

## 6. Monthly Report Content Flow

Final monthly report narrative flow (client-facing order). Maps to **13-block model** in Structure Model v0.2.

| Flow step | Client-facing intent | Maps to 13-block model |
|-----------|---------------------|------------------------|
| **1. Context / meta** | Who, what site, what period, who prepared | Block 1 — Cover / Meta |
| **2. Executive summary** | Month story in plain language | Block 2 — Executive Summary |
| **3. KPI snapshot** | Headline numbers at a glance | Block 3 — KPI Snapshot |
| **4. What changed this month** | Notable shifts before detail sections | Distributed across Blocks 5–9 interpretation layers; rollup pointer in Block 2 |
| **5. Work completed by category** | Grouped works with purpose | Block 4 — Work Completed (+ profile blocks) |
| **6. Results and interpretation** | Positions, traffic, leads/conversions explained | Blocks 7–9 — Positions, Traffic, Leads (+ profile blocks) |
| **7. Issues / blockers** | Honest status of impediments | Block 11 — Issues / Blockers / Risks |
| **8. Client actions needed** | Explicit asks | Part of Block 12 — Plan (client actions subsection) |
| **9. Plan for next month** | Prioritized forward work | Block 12 — Plan for Next Month |
| **10. Evidence appendix** | Supporting materials, external reports | Block 13 — Evidence / Appendix |

### 13-block mapping detail

| Block # | Name | Content flow role |
|---------|------|-------------------|
| 1 | Cover / Meta | Step 1 — context |
| 2 | Executive Summary | Step 2 — synthesizes 4–6 for business reader |
| 3 | KPI Snapshot | Step 3 |
| 4 | Work Completed | Step 5 — canonical work list |
| 5 | Technical SEO | Step 5–6 — technical category |
| 6 | Semantic / Content | Step 5–6 — content category |
| 7 | Positions / Visibility | Step 6 — results |
| 8 | Traffic / Behavior | Step 6 — results |
| 9 | Leads / Conversions | Step 6 — results (profile-dependent) |
| 10 | Links / Authority | Step 5–6 — optional when relevant |
| 11 | Issues / Blockers | Step 7 |
| 12 | Plan for Next Month | Steps 8–9 |
| 13 | Evidence / Appendix | Step 10 |

**Profile-specific blocks** (Service Pages, Category Pages, Regional Landing Pages, etc.) insert between Blocks 4–6 or replace emphasis — see Block Matrix v0.1. They do not replace the universal skeleton.

### Monthly synthesis from weeklies

Monthly final is **not** a blind concatenation of three weekly checkpoints:

1. Specialist **selects and edits** weekly works into monthly Work Completed.
2. KPI Snapshot reflects **full month**, not last week only.
3. Executive Summary **interprets** the month — wins, limits, risks, next focus.
4. Weekly internal notes **do not auto-appear** in client monthly unless explicitly rolled up.

---

## 7. Weekly Checkpoint Content Flow

Weekly checkpoint content flow (internal operational rhythm):

| Step | Content | Purpose |
|------|---------|---------|
| **1. What was done** | Completed works this week only | Accountability; feeds monthly Block 4 |
| **2. What changed / observed** | Metric notes, SERP observations, indexing changes | Early signal; not full KPI deck |
| **3. What is blocked** | Client, dev, content, data blockers | Surfaces issues before month-end crisis |
| **4. What is planned next** | 3–7 bullets for following week | Forward continuity |
| **5. What needs review** | Ready-for-review flag, submission notes | Reviewer queue input |

### Maps to 9-block weekly model (Structure Model v0.2)

| Weekly block | Flow step |
|--------------|-----------|
| Week meta | Context |
| Short weekly summary | Narrative wrap of steps 1–4 |
| Completed works | Step 1 |
| Metrics / observations | Step 2 |
| Blockers | Step 3 |
| Evidence links | Supporting step 1–2 |
| Next week plan | Step 4 |
| Internal notes | Specialist-only; step 5 prep |
| Ready for review flag | Step 5 |

### How 3 weeklies feed monthly final

| Week | Typical content density | Monthly contribution |
|------|-------------------------|---------------------|
| **Week 1** | Technical fixes started, early semantic work, blockers identified | Work items, early risks |
| **Week 2** | Core content/meta work, metric movement begins | Work items, observation seeds for interpretation |
| **Week 3** | Completion push, draft monthly started, review prep | Work items, KPI draft inputs, executive summary draft |

**Week 3 checkpoint** should include explicit **readiness toward month close**: on track / at risk / blocked.

---

## 8. Client-facing vs Internal Content

### Client sees (published monthly)

- Executive summary (approved wording)
- KPI snapshot with short labels
- Completed works (dictionary client-facing wording)
- Results sections: positions, traffic, leads — with interpretation, not raw tables only
- Profile-specific blocks enabled for project type
- Risks/blockers in **neutral, non-alarming** language — factual
- Plan for next month and **client actions needed**
- Evidence appendix (selected items flagged client-visible)
- External report links (Topvisor card)
- Publication metadata (date, version)

### Client does not see

- Internal notes on any block
- Reviewer comments and revision history
- Raw task/ticket URLs with internal tokens
- Data quality warnings meant for team only
- Specialist uncertainty drafts
- Unapproved blocks (`draft`, `needs_review`, `empty`)
- Weekly checkpoints (MVP default — **SAFE UNKNOWN** weekly client policy)

### Internal sees (admin / specialist)

- All block fields including internal notes
- Data source metadata and import gaps
- Block status and completeness
- Weekly checkpoints in full
- Work dictionary internal wording

### Reviewer sees

- Client-visible text **plus** internal checklist
- Reviewer-only comments
- Block approval state
- Missing required blocks alerts
- Evidence sufficient for claims made

---

## 9. Content Quality Rules

| Rule | Detail |
|------|--------|
| **No vague activity** | Forbidden as sole content: «работали над SEO», «оптимизация продолжается» without specifics |
| **Work item structure** | Every work item: **category** (technical, content, links, analytics, commercial…) + **purpose** (why it helps the business) |
| **Metric interpretation** | Every KPI in snapshot or results blocks should have **interpretation** — what changed and plausible why |
| **Risk ownership** | Every risk/blocker: **owner or dependency** (client, dev, specialist, third party) |
| **Concrete next actions** | Plan items must be actionable — «получить тексты до 15.08», not «улучшить контент» |
| **Calm business tone** | Professional Russian; no hype, no blame |
| **No unsupported claims** | Do not state revenue impact, ranking guarantees, or competitor outcomes without evidence |
| **No fake exact attribution** | If CRM ↔ Metrika linkage incomplete, say «ориентир», not audited fact |
| **Empty block policy** | Omit or shorten blocks with no relevant work — no boilerplate filler |
| **Evidence proportionality** | Major claims (large traffic swing, critical fix) should have evidence link or note |

---

## 10. Demo v0.3 Implications

Static demo v0.3 should implement **this content architecture** visually — still no backend.

| Requirement | Detail |
|-------------|--------|
| **Project type selector** | Visible on project setup / project detail — 5 types |
| **Richer data per weekly stage** | Week 1/2/3 content differs by maturity — see Demo Report States v0.1 |
| **One complete final report** | Project A — Local/Regional — all blocks filled, client report available |
| **One Week 3 in progress** | Project B — E-commerce — W1+W2 done, W3 partial, monthly draft incomplete |
| **One Week 1 in progress** | Project C — Service/Corporate — only W1 started, monthly mostly empty |
| **Block maturity state** | Monthly editor shows empty/draft/needs_review/approved per block |
| **Client report gate** | Client view only for approved/published project; others show «not ready» with reason |
| **SEO feedback** | Still **deferred** until operator approves v0.3 for specialist review charter |

**Demo v0.3 must NOT:**
- Claim implementation, persistence, or platform choice
- Use real client names, domains, or credentials
- Be presented as final product spec without SEO feedback

---

## 11. SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Final metric catalog per profile after SEO feedback | **UNKNOWN** |
| Weekly client-visible policy | **UNKNOWN** — internal default assumed |
| Auto-rollup rules from weekly to monthly | **UNKNOWN** — manual curation in MVP |
| Block-level approval vs report-level only | **UNKNOWN** |
| Work dictionary final sanitized content | **UNKNOWN** — extraction pending |
| Chart data binding in demo/product | **UNKNOWN** |
| Multi-language reports | **UNKNOWN** — Russian default |

---

## Document control

- **Created:** 2026-07-10 (report content architecture task 01)
- **Extends:** Report Structure Model v0.2 (block inventory → content logic)
- **Does not claim:** demo v0.3 built, implementation, or SEO sign-off
