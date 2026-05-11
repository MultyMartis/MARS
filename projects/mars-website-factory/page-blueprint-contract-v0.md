# MARS Website Factory — Page Blueprint Contract v0

**Status:** **documented** — human-readable **page-level orchestration** contract. **Not** a JSON Schema, **not** runtime validation, **not** a claim that any pipeline in this repo instantiates or enforces blueprints automatically.

---

## Purpose

### Orchestration role

A **page blueprint** is the **normalized handoff** between strategy, SEO, UX structure, design intent, frontend production scope, and QA. It answers, for **one URL (or one canonical page variant)**:

- *Why* this page exists (**page_goal**, commercial and SEO intent).
- *Who* it serves (**target_audience**).
- *How* proof and CTAs are staged (**trust_strategy**, **CTA_strategy**, **conversion_points**).
- *What* sections appear, in *what* order, mapped to **registry** block IDs (**required_sections**, **optional_sections**, **section_order**, **block_mapping**).
- *How* mobile and hierarchy are biased (**mobile_priority**, **content_depth**, **UX_strategy**).
- *What* machines and humans must verify (**QA_requirements**, **schema_candidates**, **internal_linking_strategy**).
- *When* a human must sign off (**HITL_required**, **notes**).

v0 is **Markdown + field vocabulary**; machine formats are **SAFE UNKNOWN** until a future schema is chosen.

### Relation to Site Type Registry

[Site Type Registry v0](site-type-registry-v0.md) supplies **`site_type_id`** and type-level defaults (goals, models, typical blocks, forbidden patterns). The blueprint **must** declare **`site_type_id`** and stay **compatible** with that row’s intent. If the page diverges (e.g. hybrid route), document the divergence in **`notes`** and align **`QA_requirements`** / **`HITL_required`** upward.

### Relation to Block Registry

[Block Registry v0](block-registry-v0.md) supplies canonical **`block_id`** values and compatibility semantics. **`required_sections`**, **`optional_sections`**, **`section_order`**, and **`block_mapping`** reference **`block_id`** (and optional instance labels in prose). Do **not** invent ad hoc section names without mapping them to a **`block_id`** or recording **SAFE UNKNOWN** in **`notes`**.

### Relation to future workflows

The [workflow-map](workflow-map.md) places **Page Blueprint** after IA and before wireframe/design. Future Tasks (see `workflows/task-contract-v0.md`, **planned**) may treat a blueprint as an artifact with **`required_agents`** and **`hitl_gates`**. **No** wire format or storage path is fixed in v0.

### SAFE UNKNOWN

- Exact serialization (JSON/YAML), versioning policy, and diff rules — **unknown**.
- Automated compatibility checking against registries — **not** asserted for Phase 1.
- Per-block props schema — **unknown**; use **`notes`** under **`block_mapping`** for instance-level detail.

---

## Normalized blueprint structure (v0)

Each blueprint is a **logical document** (one Markdown section per page, or a table row per page in a workbook). Fields below are **required unless marked optional**. Use **`n/a`** only when the field is consciously inapplicable **and** **`notes`** explains why.

| Field | Role |
|--------|------|
| **blueprint_id** | Stable ID for this blueprint instance (project-scoped snake_case or UUID in project convention). |
| **site_type_id** | From Site Type Registry v0 (e.g. `service_landing`, `geo_landing`). |
| **page_goal** | Single primary outcome for this URL (lead, call, local visit, PLP view, entity clarity, etc.). |
| **target_audience** | Segment + situation (who lands here and why). |
| **commercial_intent** | `low` \| `mixed` \| `high` — aligns CTA aggressiveness and claim ethics with site type. |
| **SEO_intent** | Primary query class / intent (informational, transactional, local, branded, entity/AI-surface). |
| **CTA_strategy** | Primary action, secondary actions, repetition rules (incl. sticky mobile if any). |
| **trust_strategy** | What proof is shown, in what order, and what must **not** be claimed without evidence. |
| **UX_strategy** | Pacing model: scan-and-act, compare, browse, read-deep, task-complete (align with site type **UX_model**). |
| **content_depth** | `shallow` \| `medium` \| `deep` — expected copy/IA density for this page. |
| **mobile_priority** | `high` \| `standard` \| `desktop_first` (rare; justify in **notes** if `desktop_first`). |
| **required_sections** | Ordered or unordered list of **`block_id`** that **must** ship on this URL. |
| **optional_sections** | **`block_id`** list allowed if content exists and QA passes. |
| **section_order** | Ordered list of **`block_id`** (or `block_id` + short instance label) from top to bottom. |
| **block_mapping** | Narrative or table: each **`block_id`** → purpose on **this** page, key copy jobs, CTA role, SEO heading role. |
| **conversion_points** | Explicit list of conversion surfaces (form, call, chat, cart, soft “next article”) and where they appear. |
| **internal_linking_strategy** | Hub/spoke, sibling services, breadcrumbs, related geo pages, faceted links — **ethical** (no doorway patterns). |
| **schema_candidates** | JSON-LD types **candidates only** when content supports them honestly (e.g. `LocalBusiness`, `FAQPage`, `Product`); **no** fake ratings. |
| **QA_requirements** | Page-specific checks beyond the global checklist (claims, geo accuracy, stock truth, etc.). |
| **HITL_required** | `rare` \| `selective` \| `often` \| `yes` — gate before build or publish. |
| **notes** | Hybrid types, registry gaps, **SAFE UNKNOWN**, legal/compliance flags. |

---

## Example blueprints

### 1. Service landing (`service_landing`)

| Field | Example value |
|--------|-----------------|
| **blueprint_id** | `svc_roof_inspection_moscow_v1` |
| **site_type_id** | `service_landing` |
| **page_goal** | Qualified lead: request inspection or callback. |
| **target_audience** | Homeowners in Greater Moscow noticing leaks or aging roofs; mobile search majority. |
| **commercial_intent** | `high` |
| **SEO_intent** | Transactional local service (“roof inspection”, district modifiers); one primary intent per URL. |
| **CTA_strategy** | Primary: **lead_form** (short). Secondary: click-to-call in **hero** and **sticky_cta** on mobile scroll. Repeat **same** primary label after **process_steps** and before **final_cta**. |
| **trust_strategy** | **trust_block** early (certified roofer, warranty scope). **cases** mid-page (before/after, dated). **reviews** only with real sources. No aggregate “4.9/5” unless verifiable platform widget. |
| **UX_strategy** | `scan_and_act` — problem → proof → process → quote. |
| **content_depth** | `medium` |
| **mobile_priority** | `high` — tap-to-call, form fields ≤ essential, **sticky_cta** after first scroll. |
| **required_sections** | `hero`, `trust_block`, `services_grid` (single-offer focus or one row highlighted), `process_steps`, `faq`, `lead_form`, `final_cta` |
| **optional_sections** | `cases`, `reviews`, `pricing` (estimate ranges only if legally clear), `sticky_cta` |
| **section_order** | `hero` → `trust_block` → `services_grid` → `process_steps` → `cases` → `faq` → `reviews` → `lead_form` → `final_cta` (+ `sticky_cta` behavior on mobile, not duplicate content block) |
| **block_mapping** | **hero:** H1 = primary service + primary geo modifier once; one primary CTA. **services_grid:** maps to “what’s included in inspection” not unrelated SKUs. **faq:** real objections (price, timing, warranty); supports **FAQ** schema only if answers are on-page. |
| **conversion_points** | Hero CTA → form anchor; **lead_form** mid and repeated micro-copy near **final_cta**; tel: links in hero/sticky. |
| **internal_linking_strategy** | Link to sibling services (repair, replacement) with clear anchors; link to one **editorial** hub if exists; avoid thin reciprocal doorways. |
| **schema_candidates** | `LocalBusiness` (if NAP consistent sitewide), `Service` where fields truthful; **FAQPage** only if **faq** block is genuine Q&A. |
| **QA_requirements** | Verify license numbers; no guaranteed outcome claims; form GDPR/consent text; image alt for case photos. |
| **HITL_required** | `selective` — pricing ranges and warranty copy. |
| **notes** | If **pricing** omitted, state **SAFE UNKNOWN** for final price display rules until legal review. |

---

### 2. Geo landing (`geo_landing`)

| Field | Example value |
|--------|-----------------|
| **blueprint_id** | `geo_delivery_spb_center_v1` |
| **site_type_id** | `geo_landing` |
| **page_goal** | Local conversion: order or “check delivery zone” without misleading coverage. |
| **target_audience** | Residents in declared delivery polygon; often mobile, map-first mental model. |
| **commercial_intent** | `high` |
| **SEO_intent** | Local pack / “near me” + district name; avoid duplicate thin clones — each URL must have **distinct** local value. |
| **CTA_strategy** | Primary: start order or **lead_form** for B2B catering. Secondary: “see full city coverage” hub link. **sticky_cta** mirrors primary. |
| **trust_strategy** | **geo_trust** (hours, zone, SLA in plain language). **trust_block** with payment/delivery badges. No fake “serves 1000+ cities” if polygon is small. |
| **UX_strategy** | `task_complete` — confirm “you are in zone”, show ETA bands, then convert. |
| **content_depth** | `medium` |
| **mobile_priority** | `high` — map embed lazy; address copy readable without horizontal scroll. |
| **required_sections** | `hero`, `geo_trust`, `services_grid` (delivery tiers), `process_steps`, `contact_cta` or `lead_form`, `final_cta` |
| **optional_sections** | `faq` (returns, cut-off times), `reviews`, `sticky_cta` |
| **section_order** | `hero` → `geo_trust` → `services_grid` → `process_steps` → `faq` → `reviews` → `lead_form` → `final_cta` |
| **block_mapping** | **geo_trust:** unique local facts (polygon, landmarks, store photo). **hero:** H1 includes **one** geo modifier aligned with true service area. |
| **conversion_points** | CTA to menu/checkout; optional “call dispatcher” for B2B. |
| **internal_linking_strategy** | Hub page “all zones”; adjacent district pages only where content differs materially. |
| **schema_candidates** | `LocalBusiness`, `OpeningHoursSpecification` if accurate; avoid **FAQPage** unless **faq** is non-boilerplate. |
| **QA_requirements** | Polygon matches ops reality; phone hours; holiday exceptions in **notes** or **faq**. |
| **HITL_required** | `often` — geo claims are ops-sensitive. |
| **notes** | If zone data source is manual spreadsheet, label **SAFE UNKNOWN** for sync frequency until integrated. |

---

### 3. Catalog page (`catalog_site` — category PLP)

| Field | Example value |
|--------|-----------------|
| **blueprint_id** | `cat_industrial_pumps_v1` |
| **site_type_id** | `catalog_site` |
| **page_goal** | Faceted browse + click-through to PDP; optional RFQ for enterprise lines. |
| **target_audience** | Procurement and engineers comparing specs; mixed desktop/mobile. |
| **commercial_intent** | `mixed` |
| **SEO_intent** | Category head + long-tail modifiers; transactional PLP intent; canonical/facet rules belong in **notes** / technical SEO doc. |
| **CTA_strategy** | Primary: view PDP / add to cart where applicable. Secondary: “request quote” on rows with **high** variability. Avoid competing **primary** CTAs in **hero** and grid simultaneously. |
| **trust_strategy** | **trust_block** (brands carried, certifications). **comparison** optional for subfamilies. No fake “in stock” badges. |
| **UX_strategy** | `compare` / `browse` — filters visible, stable sort, scannable cards. |
| **content_depth** | `deep` for intro copy + **shallow** per card (spec-led). |
| **mobile_priority** | `standard` — filters as drawer; preserve reachability of sort/filter. |
| **required_sections** | `hero` (category title + scope), `catalog_grid`, `contact_cta` or inline RFQ entry |
| **optional_sections** | `trust_block`, `comparison`, `faq` (fit/compatibility), `sticky_cta` for RFQ-heavy campaigns |
| **section_order** | `hero` → `trust_block` → `comparison` → `catalog_grid` → `faq` → `contact_cta` |
| **block_mapping** | **catalog_grid:** each card needs spec truth, price rules, **internal_linking_strategy** to PDP. **hero:** H1 = category; avoid stuffing every synonym. |
| **conversion_points** | PDP links; RFQ modal or **lead_form** on qualified SKUs only. |
| **internal_linking_strategy** | Facet links follow SEO policy (indexable vs noindex in tech doc); related categories; “guides” hub for **read_deep** support. |
| **schema_candidates** | `ItemList` / `Product` snippets only when PDP data is consistent and permitted; **no** fabricated `AggregateRating`. |
| **QA_requirements** | Price/stock source of truth; filter combinations that produce thin results flagged. |
| **HITL_required** | `selective` — compatibility claims in **faq** / **comparison**. |
| **notes** | Canonical URL and facet rules — **SAFE UNKNOWN** in blueprint until SEO task attaches a technical addendum. |

---

### 4. AI visibility page (`ai_visibility_page`)

| Field | Example value |
|--------|-----------------|
| **blueprint_id** | `ai_vis_acme_corp_entity_v1` |
| **site_type_id** | `ai_visibility_page` |
| **page_goal** | Clear, citable **entity** facts for humans and retrieval systems; reduce brand hallucination risk without overclaiming control of third-party models. |
| **target_audience** | Researchers, partners, LLM-oriented citation seekers; often **read_deep** on desktop. |
| **commercial_intent** | `low` |
| **SEO_intent** | Branded + entity clarification; may overlap with “About” but must not be a disguised hard-sell landing. |
| **CTA_strategy** | Soft: contact/partnership, documentation, official careers. **No** dark-pattern newsletter gates. Primary CTA at end only. |
| **trust_strategy** | Factual **trust** via **sources**, dates, editorial ownership — prefer **`fact_table`** / narrative per site type doc over hype **trust_block**. |
| **UX_strategy** | `read_deep` — inverted pyramid: who/what/when first; methodology and limits explicit. |
| **content_depth** | `deep` |
| **mobile_priority** | `standard` — readable tables (wrap or stack). |
| **required_sections** | Site-type roles from [Site Type Registry v0](site-type-registry-v0.md) **`ai_visibility_page`**: `entity_definition`, `fact_table`, `scope_and_limits`, `sources`, `contact_corrections` — treat as **section intents**; map each to concrete **`block_id`** in **`block_mapping`** when a row exists, else document the gap (**SAFE UNKNOWN** per [Block Registry v0](block-registry-v0.md) intro on role vs `block_id`). |
| **optional_sections** | `faq` (genuine policy/scope only), `changelog` (if site type optional block used) |
| **section_order** | `entity_definition` → `fact_table` → `scope_and_limits` → `faq` (if used) → `sources` → `contact_corrections` |
| **block_mapping** | **`entity_definition`:** tight factual opener; avoid campaign **hero** tone — if implemented as **`hero`**, scope copy as “summary strip” only (see Block Registry **`hero`** / **`ai_visibility_page`** notes). **`fact_table`:** definition list / table of verifiable fields. **`scope_and_limits`:** what the product/org does **not** guarantee (incl. third-party model behavior). **`sources`:** primary URLs, archived citations, “last verified” date. **`contact_corrections`:** single path to report inaccuracies — map to **`contact_cta`** with correction-specific copy or a dedicated minimal block documented here. |
| **conversion_points** | Single soft **contact_cta**; optional “report inaccuracy” path (support email), not a lead funnel in disguise. |
| **internal_linking_strategy** | Link to canonical About, product truth pages, developer docs; avoid keyword-stuffed cross-links. |
| **schema_candidates** | `Organization` / `Corporation` where accurate; **avoid** **FAQPage** unless questions are real and stable. |
| **QA_requirements** | Every stat has source; “last reviewed” date; explicit “what we cannot guarantee” (model behavior). |
| **HITL_required** | `yes` — reputational and misinformation risk. |
| **notes** | **SAFE UNKNOWN:** how third-party assistants will cite this page — not controllable; page only supplies **checkable** facts. |

---

## Anti-patterns (blueprint level)

- Declaring **`required_sections`** that **conflict** with **`site_type_id`** without **HITL** and **`notes`**.
- Empty **`conversion_points`** on **`commercial_intent`:** `high` pages.
- **`schema_candidates`** that cannot be honestly populated from on-page content.
- Duplicate **`section_order`** entries that imply two **H1**-carrying heroes — fix mapping or split URLs.

---

*Contract version: v0 — documentation only, aligned with Site Type Registry v0 and Block Registry v0.*
