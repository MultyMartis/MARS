# MARS Website Factory — Block Registry v0

**Status:** **documented** — human-readable **section/block** contract for Website Factory planning and blueprinting. **Not** a database schema, **not** a component library specification, **not** executable automation, **not** a claim that agents or build pipelines validate or enforce these rows at runtime.

---

## Intro

### Purpose

The **Block Registry** is the **second orchestration layer** after [Site Type Registry v0](site-type-registry-v0.md): it defines **reusable page sections** (`block_id`) with **commercial**, **SEO**, **trust**, **UX**, and **QA** semantics so humans and **future** agents can compose pages without inventing ad hoc names. Each row is **architecture logic** you can reuse across projects: what the block is for, where it usually sits, what content it needs, and what to **avoid**.

### Relation to Site Type Registry

- [Site Type Registry v0](site-type-registry-v0.md) sets **`site_type_id`**, goals, models, and **`required_blocks` / `optional_blocks`** as **roles** (some names there are **conceptual**; this registry supplies **canonical** `block_id` values for Phase 1 documentation).
- **Block Registry v0** answers: for a chosen **`block_id`**, what are the **SEO**, **conversion**, **trust**, and **UX** expectations, **dependencies**, **anti-patterns**, **QA** emphasis, and **which site types** typically **fit** or **conflict**?
- **Mapping:** when a site type row lists a role (e.g. `hero_primary`), treat it as **intent**; prefer the **`hero`** row here unless the project doc explicitly defines a variant ID. **SAFE UNKNOWN** when a site type references a role with no v0 block — record the gap in project artefacts.

### Orchestration role

In a **future** pipeline (not claimed for Phase 1), **`site_type_id`** would **shortlist** blocks; **Page Blueprint** would **instantiate** `block_id` entries with props; **Validator / QA** would check **compatibility**, **CTA_presence**, **content_requirements**, and **anti_patterns**. v0 remains **Markdown + normalized vocabulary** only — **no** machine enforcement asserted.

### SAFE UNKNOWN

- Exact **props** / JSON Schema for block instances — **not** fixed in v0; use **`notes`** for project-specific fields.
- **Design tokens** and **static HTML** mapping — see [design-layer-model.md](design-layer-model.md) and [frontend-production-model.md](frontend-production-model.md); per-block **design_complexity** is **guidance** only.
- Whether a block is **implemented** as one partial, Vue island, or plain section — **unknown** until stack is chosen; **`frontend_complexity`** signals **relative** effort, not hours.

### Reusable architecture logic

Rows are **stable references** for: intake checklists, IA notes, blueprint tables, SEO briefs, design briefs, and QA scripts. Prefer **`block_id`** in tables and cross-links over free-text section titles. **Hybrid** sites ([`hybrid_commercial`](site-type-registry-v0.md)) should tag each route with **compatible** blocks explicitly; use **`incompatible_site_types`** to catch **wrong** pairings early (e.g. **`pricing`** on thin **`seo_landing`** without editorial justification).

---

## Field glossary (v0)

| Field | Meaning |
|--------|--------|
| **block_id** | Stable snake_case identifier. |
| **category** | Coarse bucket: e.g. `hero`, `trust`, `services`, `content`, `social_proof`, `commercial`, `conversion`, `interaction`, `navigation`, `geo`. |
| **purpose** | What the section **does** for the visitor and the business. |
| **business_goal** | Primary measurable outcome this block supports. |
| **SEO_value** | How the block helps or must align with **search** (headings, intent, schema, internal links) — without overstating guarantees. |
| **conversion_value** | How it moves users toward leads, calls, cart, or **soft** next steps. |
| **trust_role** | Proof, risk reduction, or credibility function. |
| **UX_role** | Scanning, comparing, reading, or **task** support. |
| **typical_position** | Usual fold / page zone (not a rigid rule). |
| **content_requirements** | What copy, data, or assets must exist for the block to be **honest** and useful. |
| **CTA_presence** | `none` \| `implicit` \| `secondary` \| `primary` \| `repeated` |
| **mobile_priority** | `high` \| `standard` \| `desktop_first` |
| **dependencies** | Other blocks, data sources, or **legal** inputs typically required first. |
| **anti_patterns** | Trust, SEO, legal, or UX failures to flag in QA. |
| **frontend_complexity** | `low` \| `medium` \| `high` — relative implementation surface (static-first). |
| **design_complexity** | `low` \| `medium` \| `high` — layout, illustration, motion, brand surface. |
| **QA_focus** | What to verify first for this block. |
| **compatible_site_types** | `site_type_id` values where this block is **commonly appropriate** (from Site Type Registry v0). |
| **incompatible_site_types** | Types where this block is **usually wrong** or needs **HITL** / redesign (exceptions must be documented). |
| **notes** | Variants, **SAFE UNKNOWN**, pairing hints. |

---

## Registry rows (v0)

### 1. `hero`

| Field | Value |
|--------|--------|
| **block_id** | `hero` |
| **category** | `hero` |
| **purpose** | Above-the-fold **value proposition**: who it’s for, what’s offered, why now. |
| **business_goal** | Reduce bounce; establish **primary** conversion path. |
| **SEO_value** | Single clear **H1** aligned with page intent; optional supporting subheading; avoid competing H1 semantics. |
| **conversion_value** | **High** — primary CTA or clear path to the next step. |
| **trust_role** | Light (brand, one proof line); heavy proof belongs in **`trust_block`**. |
| **UX_role** | **Scan_and_act** — immediate orientation. |
| **typical_position** | Top of page (first viewport). |
| **content_requirements** | Offer headline, supporting line, **one** primary action or clear drill-down; hero media optional but must not bury CTA on mobile. |
| **CTA_presence** | `primary` or `secondary` (brand-first corporate heroes). |
| **mobile_priority** | `high` |
| **dependencies** | Page **meta** / intent agreed; legal claims in hero need **`HITL`**. |
| **anti_patterns** | Keyword-stuffed H1; **multiple** competing primary CTAs; auto-playing video with sound; false urgency. |
| **frontend_complexity** | `low`–`medium` |
| **design_complexity** | `medium` |
| **QA_focus** | CLS, H1 uniqueness on URL, tap targets, contrast, claim substantiation. |
| **compatible_site_types** | `landing`, `service_landing`, `promo_site`, `corporate_site`, `catalog_site`, `ecommerce`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `ai_visibility_page` (prefer factual **`entity_definition`**-style openers per that pack — hero *campaign* tone may clash unless scoped as “summary hero”). |
| **notes** | Pair with **`sticky_cta`** on long mobile landings. **`seo_landing`** may use a **minimal** hero after breadcrumb — still `hero` if it carries H1 + promise. |

---

### 2. `trust_block`

| Field | Value |
|--------|--------|
| **block_id** | `trust_block` |
| **category** | `trust` |
| **purpose** | Consolidated **credibility**: logos, certifications, metrics, guarantees — bounded and verifiable. |
| **business_goal** | Reduce anxiety before **lead_form** or **`pricing`** commitment. |
| **SEO_value** | **Moderate** — avoid boilerplate keyword lists; structured facts only when truthful (`notes` / legal). |
| **conversion_value** | **Indirect** — lifts conversion on next CTA. |
| **trust_role** | **Primary** for this row. |
| **UX_role** | **Scan** — skimmable badges and short labels. |
| **typical_position** | Early–mid page (after hero or after first value section). |
| **content_requirements** | Verifiable logos/awards; dated stats need source; regulated industries need disclaimers. |
| **CTA_presence** | `none` or `implicit` (link to policies). |
| **mobile_priority** | `high` |
| **dependencies** | Asset rights cleared; **`reviews`** or **`cases`** may **feed** content but are separate blocks. |
| **anti_patterns** | Fake “as seen on”; unverifiable awards; **review gating** copy; irrelevant logo soup. |
| **frontend_complexity** | `low` |
| **design_complexity** | `low`–`medium` |
| **QA_focus** | Logo legibility, alt text, permission trail, numeric claims. |
| **compatible_site_types** | `landing`, `service_landing`, `corporate_site`, `catalog_site`, `ecommerce`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `seo_landing` when used as **generic** filler without page-specific proof (thin E-E-A-T). |
| **notes** | For **`ai_visibility_page`**, prefer **`fact_table`** + **`sources`** idiom from that site type doc rather than marketing **`trust_block`**. |

---

### 3. `services_grid`

| Field | Value |
|--------|--------|
| **block_id** | `services_grid` |
| **category** | `services` |
| **purpose** | Present **service lines** or modules in a scannable grid with links to detail. |
| **business_goal** | Route users to the right **service_landing** or deep page; support multi-offer **corporate**. |
| **SEO_value** | **Internal links** to money/detail URLs; unique blurbs per tile (avoid duplicate microcopy). |
| **conversion_value** | **Medium** — click-through to intent-matched pages. |
| **trust_role** | Low–medium (clarity of scope implies competence). |
| **UX_role** | **Browse** — compare at a glance. |
| **typical_position** | Home or hub after hero; mid-page on large landings. |
| **content_requirements** | One line **outcome** per service; avoid jargon-only titles; link targets must exist. |
| **CTA_presence** | `implicit` (card links) or `secondary` (“Get quote”). |
| **mobile_priority** | `high` |
| **dependencies** | IA for service URLs; optional **`process_steps`** later on same page. |
| **anti_patterns** | Orphan tiles linking to **empty** pages; 10+ equal-weight tiles without grouping. |
| **frontend_complexity** | `low`–`medium` |
| **design_complexity** | `medium` |
| **QA_focus** | Link rot, heading order, keyboard grid navigation, duplicate H2 patterns sitewide. |
| **compatible_site_types** | `service_landing`, `corporate_site`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `ecommerce` **PLP** (use **`catalog_grid`**); **`seo_landing`** unless the grid is **editorial** categories with real depth. |
| **notes** | **`landing`** single-offer may use a **reduced** grid (2–3 “ways we help”) — still valid. |

---

### 4. `faq`

| Field | Value |
|--------|--------|
| **block_id** | `faq` |
| **category** | `content` |
| **purpose** | Answer **objections** and support queries with **genuine** Q&A pairs. |
| **business_goal** | Pre-sales support; snippet eligibility **only** when content is real FAQ (not decoration). |
| **SEO_value** | **High** when questions match **People Also Ask** / long-tail; **FAQ** schema only if policy allows and pairs match on-page text. |
| **conversion_value** | **Medium** — removes friction before **`lead_form`** / **`pricing`**. |
| **trust_role** | Medium (transparency). |
| **UX_role** | **Read** + expand/collapse scan. |
| **typical_position** | Mid–lower page; before final CTA on landings. |
| **content_requirements** | Distinct questions; accurate answers; legal review for regulated topics; **update** process when offer changes. |
| **CTA_presence** | `none` or `secondary` (“Still unsure? Contact”). |
| **mobile_priority** | `high` |
| **dependencies** | Support/product truth sources; avoid contradicting **`pricing`**. |
| **anti_patterns** | FAQ schema on **non-FAQ** copy; duplicate questions; keyword stuffing; “SEO FAQ” unrelated to page intent. |
| **frontend_complexity** | `low`–`medium` |
| **design_complexity** | `low` |
| **QA_focus** | Accordion a11y (roving tabindex), schema honesty, consistency with policies. |
| **compatible_site_types** | `landing`, `service_landing`, `corporate_site`, `catalog_site`, `ecommerce`, `geo_landing`, `seo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `promo_site` **if** it creates legal **contest** risk without review; `ai_visibility_page` **if** FAQ tone **replaces** factual spec (prefer structured facts there). |
| **notes** | **`seo_landing`**: FAQ must add **unique** value, not thin repeat of body. |

---

### 5. `cases`

| Field | Value |
|--------|--------|
| **block_id** | `cases` |
| **category** | `social_proof` |
| **purpose** | **Project- or client-level** outcomes: before/after, metrics, industry relevance. |
| **business_goal** | Prove execution ability for **high-consideration** offers. |
| **SEO_value** | **Case** titles can rank for “[industry] + [service]”; avoid duplicate thin case URLs. |
| **conversion_value** | **High** for B2B services; **medium** for consumer. |
| **trust_role** | **Primary** proof. |
| **UX_role** | **Scan** + optional deep link to full case. |
| **typical_position** | Mid-page after value prop; sometimes near **`pricing`**. |
| **content_requirements** | Client permission; truthful metrics; anonymization rules; industry tags. |
| **CTA_presence** | `secondary` (“Read case”) or `implicit`. |
| **mobile_priority** | `high` |
| **dependencies** | Approved assets; legal for “before/after” in regulated verticals. |
| **anti_patterns** | Fabricated clients; misleading metrics; **stock** photos passed as client sites. |
| **frontend_complexity** | `low`–`medium` |
| **design_complexity** | `medium` |
| **QA_focus** | Consent trail, metric methodology, image rights, link to **full** case if promised. |
| **compatible_site_types** | `service_landing`, `corporate_site`, `catalog_site`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `promo_site` **unless** cases are **pre-launch** social proof (then **light** use + HITL). |
| **notes** | **`ecommerce`** may use “customer stories” variant — same **`cases`** id with commerce-oriented **`notes`**. |

---

### 6. `reviews`

| Field | Value |
|--------|--------|
| **block_id** | `reviews` |
| **category** | `social_proof` |
| **purpose** | **Third-party or first-party** ratings/testimonials with attribution. |
| **business_goal** | Social proof for **conversion** and **local** trust. |
| **SEO_value** | **Review** rich results **only** with eligible policy and **real** reviews; aggregate rating must be honest. |
| **conversion_value** | **High** near **`lead_form`** / checkout. |
| **trust_role** | **Primary** (with moderation transparency). |
| **UX_role** | **Scan** carousel or list; filters by product/service where relevant. |
| **typical_position** | Mid-page or beside **`pricing`** / **`lead_form`**. |
| **content_requirements** | Moderation policy; source (Google, partner, onsite); refresh rules; product linkage for PDP. |
| **CTA_presence** | `none` or `secondary` (“Write a review”). |
| **mobile_priority** | `high` |
| **dependencies** | Feed/API or manual curation; **`trust_block`** for aggregate badges if separate. |
| **anti_patterns** | Selective deletion of negatives (policy breach); **incentivized** reviews without disclosure; fake reviews. |
| **frontend_complexity** | `medium` (widgets, carousels). |
| **design_complexity** | `medium` |
| **QA_focus** | Widget performance, a11y for carousels, disclosure, star math vs text. |
| **compatible_site_types** | `landing`, `service_landing`, `ecommerce`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `ai_visibility_page` **as** marketing wall (use **`sources`** / **`fact_table`** instead). |
| **notes** | **`seo_landing`**: use **sparingly** unless reviews are **the** topic (e.g. roundup with editorial criteria). |

---

### 7. `pricing`

| Field | Value |
|--------|--------|
| **block_id** | `pricing` |
| **category** | `commercial` |
| **purpose** | Present **plans**, **tiers**, or **ballpark** with clear limits and next step. |
| **business_goal** | Qualify leads; enable self-serve purchase where applicable. |
| **SEO_value** | **Transactional** queries (“price”, “plans”) — unique copy per tier; avoid **thin** duplicate pricing URLs. |
| **conversion_value** | **Very high** — direct revenue or qualified handoff. |
| **trust_role** | Medium (transparency reduces bounce). |
| **UX_role** | **Compare** — column scan; mobile stack order must preserve meaning. |
| **typical_position** | Dedicated pricing page or lower-mid on **service_landing**. |
| **content_requirements** | Currency, tax/VAT disclaimer, what's included/excluded; legal for promos; B2B “Contact sales” fallback. |
| **CTA_presence** | `primary` |
| **mobile_priority** | `high` |
| **dependencies** | SKU/plan truth source; sync with checkout if **`ecommerce`**. |
| **anti_patterns** | Hidden fees; **bait** tiers; dark patterns; stale promo timers. |
| **frontend_complexity** | `medium`–`high` (toggle billing, feature matrix). |
| **design_complexity** | `medium`–`high` |
| **QA_focus** | Price accuracy vs cart, a11y of tables, legal promos, mobile horizontal scroll traps. |
| **compatible_site_types** | `landing`, `service_landing`, `corporate_site`, `ecommerce`, `hybrid_commercial` |
| **incompatible_site_types** | `seo_landing` **unless** editorial **comparison** with methodology (then pair with **`comparison`** + HITL); **`geo_landing`** **if** pricing **varies** illegally by location without disclosure. |
| **notes** | Regulated industries → **`HITL_required`** on all numbers. |

---

### 8. `process_steps`

| Field | Value |
|--------|--------|
| **block_id** | `process_steps` |
| **category** | `content` |
| **purpose** | Explain **how it works** in 3–7 steps: intake → delivery → outcome. |
| **business_goal** | Reduce uncertainty for **services** and **high-friction** signups. |
| **SEO_value** | **Moderate** — can capture “how does X work” queries when headings are specific. |
| **conversion_value** | **Medium** — supports CTA after understanding. |
| **trust_role** | Medium (operational clarity). |
| **UX_role** | **Scan** numbered path. |
| **typical_position** | Early–mid on **`service_landing`**; corporate “How we engage”. |
| **content_requirements** | Honest timelines; who does what; what client must provide. |
| **CTA_presence** | `secondary` at end (“Start step 1”). |
| **mobile_priority** | `high` |
| **dependencies** | Sales/ops alignment on actual process (**SAFE UNKNOWN** until interviewed). |
| **anti_patterns** | Vague “we’ll handle everything”; steps that **omit** billing/legal touchpoints. |
| **frontend_complexity** | `low` |
| **design_complexity** | `low`–`medium` |
| **QA_focus** | Step count vs mobile viewport, icon meaning, timeline honesty. |
| **compatible_site_types** | `service_landing`, `corporate_site`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `ecommerce` **checkout** funnel (use **progress** UI there — different contract); **`catalog_site`** **unless** B2B **RFQ** process narrative. |
| **notes** | **`landing`** may use **3-step** micro **`process_steps`**. |

---

### 9. `contact_cta`

| Field | Value |
|--------|--------|
| **block_id** | `contact_cta` |
| **category** | `conversion` |
| **purpose** | **Prominent** contact module: phone, chat, office, callback — not necessarily full form. |
| **business_goal** | Increment **calls/chats**; support **local** and **corporate** routing. |
| **SEO_value** | **Local** NAP consistency if addresses shown; **no** keyword stuffing in address blocks. |
| **conversion_value** | **High** for **`service_landing`**, **`geo_landing`**. |
| **trust_role** | Medium (human reachable). |
| **UX_role** | **Task** — initiate contact fast. |
| **typical_position** | Mid or sidebar; repeated in **`footer`** patterns separately. |
| **content_requirements** | Correct regional hours; GDPR/consent if callback stores PII. |
| **CTA_presence** | `primary` |
| **mobile_priority** | `high` |
| **dependencies** | Telephony/chat availability; routing rules. |
| **anti_patterns** | Dead numbers; chat widgets that **never** connect; fake “local” numbers. |
| **frontend_complexity** | `low`–`medium` (widgets). |
| **design_complexity** | `low` |
| **QA_focus** | tap-to-call, focus traps in widgets, hours accuracy. |
| **compatible_site_types** | `service_landing`, `corporate_site`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `ecommerce` **as sole** checkout path (use cart/checkout CTAs); **`seo_landing`** **if** it **dilutes** editorial with **sales** box above the fold without intent match. |
| **notes** | Pairs with **`lead_form`** when async capture preferred. |

---

### 10. `calculator`

| Field | Value |
|--------|--------|
| **block_id** | `calculator` |
| **category** | `interaction` |
| **purpose** | **Interactive** estimate: savings, ROI, loan, quote range — outputs **disclaimed** ranges. |
| **business_goal** | Lead qualification + **engagement** time on page. |
| **SEO_value** | **Low–medium** — often **thin** if only JS; add **static** explanatory copy for crawl. |
| **conversion_value** | **High** when followed by **`lead_form`** with prefill. |
| **trust_role** | Medium if methodology transparent. |
| **UX_role** | **Task** — input/output clarity. |
| **typical_position** | Mid-page after value prop on **`service_landing`**; finance verticals. |
| **content_requirements** | Formula documentation; disclaimers; **not** a legal offer unless reviewed. |
| **CTA_presence** | `secondary` (“Get exact quote”) after result. |
| **mobile_priority** | `high` |
| **dependencies** | Validated formula; optional CRM field mapping (**unknown** until stack). |
| **anti_patterns** | **Misleading** defaults; hidden sliders biasing output; storing PII without consent. |
| **frontend_complexity** | `high` |
| **design_complexity** | `medium` |
| **QA_focus** | Edge inputs, error messages, a11y of sliders/inputs, disclaimer visibility. |
| **compatible_site_types** | `service_landing`, `corporate_site`, `landing`, `hybrid_commercial` |
| **incompatible_site_types** | `seo_landing` **unless** tool is **the** content (methodology + static fallbacks); **`ai_visibility_page`** (use **`fact_table`**). |
| **notes** | **`ecommerce`** may use **shipping** or **finance** calculators — same id, different **`notes`**. |

---

### 11. `comparison`

| Field | Value |
|--------|--------|
| **block_id** | `comparison` |
| **category** | `content` |
| **purpose** | **Feature / plan / competitor** matrix (ethical: factual rows, clear dates). |
| **business_goal** | Accelerate **decision** for evaluators; support **`pricing`** narrative. |
| **SEO_value** | **High** for “vs” and “alternative” intents when **substantive**; **risk** of thin affiliate tables. |
| **conversion_value** | **High** for mid-funnel. |
| **trust_role** | Medium–high if **balanced**; **low** if one-sided spin. |
| **UX_role** | **Compare** — table scan; sticky header on wide tables. |
| **typical_position** | Mid–lower page; dedicated comparison URLs. |
| **content_requirements** | Source for competitor claims; **update** cadence; “last verified” date. |
| **CTA_presence** | `secondary` or `primary` after fair context. |
| **mobile_priority** | `high` (horizontal scroll or card fallback). |
| **dependencies** | Legal for naming competitors; **`pricing`** alignment. |
| **anti_patterns** | Strawman competitor columns; outdated **2023** rows; hidden affiliate bias. |
| **frontend_complexity** | `medium`–`high` |
| **design_complexity** | `medium` |
| **QA_focus** | Table a11y (`scope`, captions), mobile degradation path, claim evidence. |
| **compatible_site_types** | `corporate_site`, `catalog_site`, `seo_landing`, `service_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `promo_site` **unless** single **benign** compare (e.g. plan tiers only); **`geo_landing`** **for** competitor bashing **without** local relevance. |
| **notes** | **`ecommerce`** compare SKUs — same block with product-specific **`content_requirements`**. |

---

### 12. `geo_trust`

| Field | Value |
|--------|--------|
| **block_id** | `geo_trust` |
| **category** | `geo` |
| **purpose** | **Location-native** proof: map, service area, local team, neighborhood coverage, NAP. |
| **business_goal** | Win **local** intent and phone calls; reduce “are they near me?” friction. |
| **SEO_value** | **High** for **`geo_landing`** when content is **unique** per locale; **risk** if duplicate across doorways. |
| **conversion_value** | **High** (call/directions). |
| **trust_role** | **Primary** local proof. |
| **UX_role** | **Scan_and_act** — map + CTA. |
| **typical_position** | Mid-page on **`geo_landing`**; footer-adjacent on hybrid local pages. |
| **content_requirements** | True service area; consistent NAP; map embed ToS; no PO boxes masquerading as offices. |
| **CTA_presence** | `primary` (call / directions). |
| **mobile_priority** | `high` |
| **dependencies** | GBP alignment (**SAFE UNKNOWN** if GBP unused); driving directions API policy. |
| **anti_patterns** | **Doorway** pages; same map for unrelated cities; keyword-stuffed city lists. |
| **frontend_complexity** | `medium` (maps). |
| **design_complexity** | `low`–`medium` |
| **QA_focus** | Schema locality, sister-page uniqueness, map performance, NAP match. |
| **compatible_site_types** | `geo_landing`, `service_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `seo_landing` **as** pure geo spam without editorial value; **`ai_visibility_page`**. |
| **notes** | **`corporate_site`** global HQ page: use **partial** **`geo_trust`** (single real HQ), not a farm of fake locals. |

---

### 13. `catalog_grid`

| Field | Value |
|--------|--------|
| **block_id** | `catalog_grid` |
| **category** | `services` |
| **purpose** | **Product/category** discovery grid with filters/sort signals (may be **lite** without full PLP engine). |
| **business_goal** | Drive **PLP/PDP** paths; support **`catalog_site`** and **`ecommerce`**. |
| **SEO_value** | **High** on hub pages; faceted navigation must follow **indexation** strategy (**planned** SEO pattern lib). |
| **conversion_value** | **High** — click to detail or add-to-cart teaser. |
| **trust_role** | Low–medium (badges, stock hints). |
| **UX_role** | **Browse** — filter/sort mental model. |
| **typical_position** | Category hubs; home “featured range”. |
| **content_requirements** | Stable product data; image aspect ratios; out-of-stock rules. |
| **CTA_presence** | `implicit` or `primary` (“View range”). |
| **mobile_priority** | `high` |
| **dependencies** | PIM/feed or CMS list; **`pricing`** truth for displayed prices. |
| **anti_patterns** | Broken filters; **infinite** scroll without footer access; indexing uncontrolled params. |
| **frontend_complexity** | `high` |
| **design_complexity** | `medium`–`high` |
| **QA_focus** | Filter URL behavior, card a11y, image lazy-load CLS, stock accuracy. |
| **compatible_site_types** | `catalog_site`, `ecommerce`, `hybrid_commercial` |
| **incompatible_site_types** | `landing` **full** catalog (dilutes single-offer); **`seo_landing`** **unless** editorial **curated** set with commentary. |
| **notes** | **`corporate_site`** “product families” teaser — **`catalog_grid`** **lite** with 6–8 items. |

---

### 14. `sticky_cta`

| Field | Value |
|--------|--------|
| **block_id** | `sticky_cta` |
| **category** | `navigation` |
| **purpose** | **Persistent** mobile (or desktop) bar/button repeating **one** primary action. |
| **business_goal** | Recover conversions on long landings. |
| **SEO_value** | **Low** — ensure it doesn’t **hide** main content from crawlers (DOM order / CLS). |
| **conversion_value** | **High** on mobile long pages. |
| **trust_role** | Low (can **hurt** if aggressive). |
| **UX_role** | **Persistent task** — must not trap focus. |
| **typical_position** | Fixed bottom or top after scroll threshold. |
| **content_requirements** | **Same** action as hero primary; dismiss rules where legally needed. |
| **CTA_presence** | `repeated` |
| **mobile_priority** | `high` |
| **dependencies** | **`hero`** primary CTA agreed first. |
| **anti_patterns** | **Different** primary than hero (confusion); covers **cookie** banner incorrectly; fake “1 slot left”. |
| **frontend_complexity** | `medium` (viewport, safe-area). |
| **design_complexity** | `low` |
| **QA_focus** | z-index vs modals, focus order, WCAG reflow, **CLS** on appear. |
| **compatible_site_types** | `landing`, `service_landing`, `promo_site`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `corporate_site` **wide** multi-audience hubs (CTA conflict); **`seo_landing`** **editorial** (can feel spammy — use **`final_cta`** inline instead); **`ecommerce`** **checkout** (use checkout chrome). |
| **notes** | One **primary** per URL policy still applies site-wide. |

---

### 15. `lead_form`

| Field | Value |
|--------|--------|
| **block_id** | `lead_form` |
| **category** | `conversion` |
| **purpose** | Capture **lead** data: name, contact, intent, optional qualifiers. |
| **business_goal** | **MQL/SQL** creation; booking requests. |
| **SEO_value** | **Low** — keep indexable **intro** copy nearby; don’t **orphan** thin form-only pages. |
| **conversion_value** | **Very high** — core conversion surface. |
| **trust_role** | Medium (privacy copy, security). |
| **UX_role** | **Task** — minimize fields vs value. |
| **typical_position** | Mid or lower page; dedicated contact pages. |
| **content_requirements** | Privacy policy link; consent checkboxes where required; spam protection (**SAFE UNKNOWN** method). |
| **CTA_presence** | `primary` |
| **mobile_priority** | `high` |
| **dependencies** | CRM endpoint or email handler; **`trust_block`** above fold on cold traffic. |
| **anti_patterns** | **Pre-ticked** consent; hidden fields; asking **credit card** for “free” lead magnet without clarity. |
| **frontend_complexity** | `medium` (validation, i18n). |
| **design_complexity** | `low` |
| **QA_focus** | Labels/errors, autofill, keyboard submit, double-submit protection, GDPR. |
| **compatible_site_types** | `landing`, `service_landing`, `corporate_site`, `geo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `ecommerce` **guest checkout** block (different validation contract — still “forms” but not this **`lead_form`** id); **`ai_visibility_page`** (prefer **`contact_corrections`** pattern from site type doc). |
| **notes** | Pair with **`calculator`** prefill when applicable. |

---

### 16. `final_cta`

| Field | Value |
|--------|--------|
| **block_id** | `final_cta` |
| **category** | `conversion` |
| **purpose** | **Last** high-contrast CTA band after FAQs/cases — recap offer + **one** action. |
| **business_goal** | Capture **scroll-to-bottom** intent; bookend page narrative. |
| **SEO_value** | **Low** — avoid stuffing keywords; **H2** should describe user benefit, not spam. |
| **conversion_value** | **High** — final conversion lift. |
| **trust_role** | Light repeat of guarantee line. |
| **UX_role** | **Decision** — closure. |
| **typical_position** | Above footer. |
| **content_requirements** | Restate **primary** value; optional risk reversal; match **`hero`** offer. |
| **CTA_presence** | `primary` |
| **mobile_priority** | `high` |
| **dependencies** | **`hero`** / **`pricing`** / **`lead_form`** alignment on **same** promise. |
| **anti_patterns** | **New** unrelated offer; **second** primary conflicting with **`sticky_cta`**. |
| **frontend_complexity** | `low` |
| **design_complexity** | `low`–`medium` |
| **QA_focus** | Contrast, redundant **link** text uniqueness, mobile padding vs **`sticky_cta`**. |
| **compatible_site_types** | `landing`, `service_landing`, `promo_site`, `corporate_site`, `catalog_site`, `geo_landing`, `seo_landing`, `hybrid_commercial` |
| **incompatible_site_types** | `ecommerce` **cart** page (use checkout CTAs); **`ai_visibility_page`** **if** it **oversells** vs factual body (tone clash — use soft **`contact_corrections`** instead). |
| **notes** | Often pairs with **`faq`** immediately above. |

---

## Future integrations

| Artefact | Role relative to Block Registry v0 |
|----------|-------------------------------------|
| **Site Type Registry v0** | Supplies **`site_type_id`** and block **roles**; this registry supplies **canonical** `block_id` semantics and compatibility matrices. |
| **Page Blueprint contract** (planned) | Lists ordered **`block_id`** instances with **props** (future contract). |
| **SEO Pattern Library** (planned) | Constrains headings/schema use **per** `SEO_value` and site type. |
| **Commercial Pattern Library** (planned) | Constrains urgency/claims **near** **`pricing`**, **`final_cta`**, **`sticky_cta`**. |
| **Frontend Production Rules** (planned) | Maps **`frontend_complexity`** to static build patterns ([frontend-production-model.md](frontend-production-model.md)). |

**Orchestration input:** **`site_type_id`** shortlists blocks; **`block_id`** rows refine **QA**, **copy**, and **implementation** risk — always subject to **SAFE UNKNOWN** where project facts are missing.

---

*Registry version: v0 — Markdown only. Last updated: 2026-05-11.*
