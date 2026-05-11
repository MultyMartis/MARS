# MARS Website Factory — Site Type Registry v0

**Status:** **documented** — human-readable **classification** contract for Website Factory planning. **Not** a database schema, **not** executable automation, **not** a claim that agents or workflows enforce these rows at runtime.

---

## Intro

### Purpose

The **Site Type Registry** is the **first classification layer** for Website Factory work: it ties **business intent** (why the site exists) to **SEO posture**, **UX priorities**, **page architecture defaults**, **block selection hints**, **frontend complexity expectations**, and **QA emphasis**. Downstream registries and agents (when they exist) consume `site_type_id` as **orchestration input**, not as a magic default.

### How this registry is used

- **Strategy / intake:** pick or propose a `site_type_id` (or hybrid with explicit primary).
- **IA & blueprints:** `typical_pages`, `required_blocks`, and `forbidden_patterns` constrain proposals.
- **SEO & content:** `SEO_model`, `commercial_intent`, and `content_depth` align titles, snippets, and internal linking **patterns** (pattern libraries are **separate**, **future** artefacts).
- **UX & design:** `UX_model`, `trust_model`, `CTA_model`, and `design_complexity` set expectations for layout and component density.
- **Frontend production:** `frontend_complexity` and block lists inform estimates and **Gulp-oriented** static implementation scope ([frontend-production-model.md](frontend-production-model.md)).
- **QA:** `QA_focus`, `forbidden_patterns`, and `HITL_required` drive checklist depth and human gates ([qa-validation-model.md](qa-validation-model.md)).

### Relation to workflows and agents

- Aligns with the **documentation-first** pipeline in [workflow-map.md](workflow-map.md): intake → strategy → IA → blueprints → design → frontend → QA → HITL → delivery.
- **Planned** agent roles (see [agent-map.md](agent-map.md)) such as **Site Type Classifier**, **Marketing Strategy**, **SEO Strategy**, **Page Blueprint**, and **Validator** are expected to **read** and **propose** classifications **against** this registry — **no** claim here that any agent **implements** or **enforces** these fields automatically in Phase 1.

### SAFE UNKNOWN

- Exact **machine** format (JSON Schema, YAML, DB) for a future registry service — **unknown**; v0 is **Markdown + normalized vocabulary** only.
- Whether a given real project maps **cleanly** to one row — often **unknown** until intake; use **`notes`** and explicit **hybrid** handling (`hybrid_commercial` or composed primary + secondary type in project docs).
- Industry-specific compliance (medical, financial, gambling, etc.) — **not** exhaustively encoded; when in doubt, set **`HITL_required`** higher and record **SAFE UNKNOWN** in project artefacts.

---

## Field glossary (v0)

Use these fields consistently across rows. Values are **guidance**, not validation rules.

| Field | Meaning |
|--------|--------|
| **site_type_id** | Stable snake_case identifier for references. |
| **category** | Coarse bucket: e.g. `conversion`, `brand`, `commerce`, `programmatic_seo`, `campaign`, `hybrid`. |
| **primary_goal** | Main measurable outcome the business optimizes for. |
| **monetization_model** | How value is captured (leads, ads, transactions, subscriptions, mixed). |
| **typical_pages** | Expected page **kinds** (not a sitemap mandate). |
| **conversion_logic** | How users move toward the goal (forms, calls, cart, soft CTAs). |
| **SEO_model** | Dominant SEO stance: e.g. `brand_queries`, `intent_pages`, `local_pack`, `transactional_plp`, `editorial_hub`. |
| **CTA_model** | Primary CTA rhythm: e.g. `single_primary`, `repeated_soft`, `transactional`. |
| **trust_model** | What proof the user needs: logos, cases, reviews, certifications, team, policies. |
| **UX_model** | Interaction bias: e.g. `scan_and_act`, `compare`, `browse`, `read_deep`, `task_complete`. |
| **mobile_priority** | `high` \| `standard` \| `desktop_first` (rare; document why if used). |
| **content_depth** | `shallow` \| `medium` \| `deep` — copy and IA density, not word count alone. |
| **commercial_intent** | `low` \| `mixed` \| `high` — aligns SEO snippet and CTA aggressiveness **ethics**. |
| **design_complexity** | `low` \| `medium` \| `high` — layout variety, illustration, motion, brand surface. |
| **frontend_complexity** | `low` \| `medium` \| `high` — components, state, filters, cart, geo, personalization hooks. |
| **required_blocks** | Section **roles** the type usually needs (map to future Block Registry `block_id`s). |
| **optional_blocks** | Common add-ons. |
| **forbidden_patterns** | Anti-patterns and trust/SEO risks to flag in QA. |
| **QA_focus** | What reviewers and validators stress first. |
| **HITL_required** | `rare` \| `selective` \| `often` \| `yes` — legal, claims, pricing, regulated sectors. |
| **notes** | Edge cases, pairing with other types, **SAFE UNKNOWN** reminders. |

---

## Registry rows (v0)

### 1. `landing`

| Field | Value |
|--------|--------|
| **site_type_id** | `landing` |
| **category** | `conversion` |
| **primary_goal** | Single-offer conversion (lead, call, signup, download). |
| **monetization_model** | Lead capture, trial signup, or low-friction sale; often ad-supported traffic upstream. |
| **typical_pages** | One primary URL; optional legal/thank-you/short FAQ on same flow. |
| **conversion_logic** | One **primary** CTA; supporting proof reduces anxiety; minimal navigation. |
| **SEO_model** | Often **paid + brand** driven; organic may target one head term or long-tail offer phrase. |
| **CTA_model** | `single_primary` with repeated **same** action (sticky mobile CTA acceptable). |
| **trust_model** | Logos, short testimonial, guarantee, security note near form. |
| **UX_model** | `scan_and_act` — fast scroll, clear hierarchy, low cognitive load. |
| **mobile_priority** | `high` |
| **content_depth** | `shallow` |
| **commercial_intent** | `high` |
| **design_complexity** | `low`–`medium` |
| **frontend_complexity** | `low` |
| **required_blocks** | `hero_primary`, `value_props`, `social_proof`, `primary_cta`, `footer_minimal` |
| **optional_blocks** | `faq_compact`, `logo_strip`, `risk_reversal` |
| **forbidden_patterns** | Competing primary CTAs; fake urgency; hidden pricing when claims imply transparency; keyword-stuffed footers. |
| **QA_focus** | CTA clarity, form labels/a11y, CLS on hero, claim substantiation for numbers. |
| **HITL_required** | `selective` (regulated offers → `often`). |
| **notes** | If the “landing” is really a **geo** or **SEO** program page, prefer `geo_landing` or `seo_landing` for honest SEO_model alignment. |

---

### 2. `service_landing`

| Field | Value |
|--------|--------|
| **site_type_id** | `service_landing` |
| **category** | `conversion` |
| **primary_goal** | Qualified requests for a **service** (quote, booking, call). |
| **monetization_model** | Lead → offline/CRM close; retainer or project billing. |
| **typical_pages** | Service hero + process + coverage + proof + FAQ; may mirror **one** service per URL in campaigns. |
| **conversion_logic** | Trust-first then CTA; phone/chat/booking; optional calculator. |
| **SEO_model** | `intent_pages` + `local_pack` when geography matters. |
| **CTA_model** | `single_primary` with **secondary** contact options (phone, messenger) clearly secondary. |
| **trust_model** | Cases, before/after (where ethical), certifications, team, service area, guarantees. |
| **UX_model** | `scan_and_act` with **process** clarity (how it works in 3–5 steps). |
| **mobile_priority** | `high` |
| **content_depth** | `medium` |
| **commercial_intent** | `high` |
| **design_complexity** | `medium` |
| **frontend_complexity** | `low`–`medium` |
| **required_blocks** | `hero_service`, `process_steps`, `service_scope`, `proof_cases`, `cta_booking_or_form`, `faq_service` |
| **optional_blocks** | `coverage_map`, `pricing_ballpark`, `team_credentials` |
| **forbidden_patterns** | Fake local addresses; “near you” without real service area; medical/financial guarantees; review gating copy. |
| **QA_focus** | Service area honesty, NAP consistency (if local), schema only when content supports it, booking widget a11y. |
| **HITL_required** | `often` for regulated trades; `selective` otherwise. |
| **notes** | Distinguish from **`corporate_site`**: service landing **optimizes one offer**; corporate carries **brand + multi-service** navigation. |

---

### 3. `promo_site`

| Field | Value |
|--------|--------|
| **site_type_id** | `promo_site` |
| **category** | `campaign` |
| **primary_goal** | Time-bound awareness, waitlist, launch, or event signup. |
| **monetization_model** | Often pre-revenue; may include early purchases or tickets. |
| **typical_pages** | 1–3 pages: hero/story, detail, register; countdown optional. |
| **conversion_logic** | Emotional narrative → single signup/purchase; social share secondary. |
| **SEO_model** | Often **low organic** reliance; **brand + social + paid**; lightweight SEO for discoverability only. |
| **CTA_model** | `single_primary` or **waitlist** rhythm. |
| **trust_model** | Team/brand credibility, press quotes, partner logos; less “review wall” than commerce. |
| **UX_model** | `scan_and_act` with **story** scroll; motion/illustration acceptable if performant. |
| **mobile_priority** | `high` |
| **content_depth** | `shallow`–`medium` |
| **commercial_intent** | `mixed` |
| **design_complexity** | `medium`–`high` |
| **frontend_complexity** | `low`–`medium` |
| **required_blocks** | `hero_campaign`, `narrative_sections`, `signup_or_ticket_cta`, `legal_footer` |
| **optional_blocks** | `countdown`, `speaker_grid`, `sponsor_strip` |
| **forbidden_patterns** | Expired campaign copy left live; false scarcity; undisclosed sponsorship; pre-ticked consent. |
| **QA_focus** | Date accuracy, timezone for events, performance (hero weight), legal for contests. |
| **HITL_required** | `selective`; `yes` for sweepstakes/contests. |
| **notes** | After campaign end, plan **redirect or archive** policy — **SAFE UNKNOWN** until product owner specifies. |

---

### 4. `corporate_site`

| Field | Value |
|--------|--------|
| **site_type_id** | `corporate_site` |
| **category** | `brand` |
| **primary_goal** | Credibility, recruitment, investor/partner trust, **multi-offer** navigation to products/services. |
| **monetization_model** | Indirect: supports sales pipeline, hiring, ecosystem. |
| **typical_pages** | Home, about, products/solutions hub, industries, resources/blog hub, careers, legal, contact/locations. |
| **conversion_logic** | Multiple **soft** CTAs + clear “contact sales” / demo for B2B; careers ATS links. |
| **SEO_model** | `brand_queries` + `editorial_hub` for content; competitive **non-brand** via thought leadership (not guaranteed). |
| **CTA_model** | `repeated_soft` with **segmented** primary per audience (buyer vs candidate — avoid confusion). |
| **trust_model** | Leadership, milestones, compliance, case studies, partner ecosystem, security/privacy pages. |
| **UX_model** | `browse` + `read_deep` for resource areas; clear **information scent** in mega-menus. |
| **mobile_priority** | `standard` (still test critical paths on mobile). |
| **content_depth** | `deep` across subtree; home may stay `medium`. |
| **commercial_intent** | `mixed` |
| **design_complexity** | `high` |
| **frontend_complexity** | `medium`–`high` |
| **required_blocks** | `nav_mega_or_primary`, `hero_brand`, `solution_teasers`, `proof_logos`, `resource_teaser`, `careers_entry`, `footer_corporate` |
| **optional_blocks** | `investor_snippet`, `global_locations`, `newsroom` |
| **forbidden_patterns** | Orphan hub pages; duplicate H1 patterns across “solutions” clones; stale leadership; conflicting regional messaging. |
| **QA_focus** | Nav consistency, internal linking to money pages, careers ATS deep links, accessibility on mega-menu, i18n if multi-locale. |
| **HITL_required** | `selective` (financial/legal/regulated disclosures). |
| **notes** | Often **hybrid** with `catalog_site` or `ecommerce` for a subset of routes — document **primary** type per subtree. |

---

### 5. `catalog_site`

| Field | Value |
|--------|--------|
| **site_type_id** | `catalog_site` |
| **category** | `commerce` (browse-heavy) |
| **primary_goal** | Discovery, comparison, and **request** or **dealer** conversion — not always checkout on-domain. |
| **monetization_model** | Leads to partners, RFQs, “where to buy”, or light transaction. |
| **typical_pages** | PLP-style categories, product families, compare, specs/downloads, support docs. |
| **conversion_logic** | Filter/sort → spec confirmation → contact/dealer/locator; “buy” may be off-site. |
| **SEO_model** | `transactional_plp` + long-tail spec queries; faceted URL strategy must be **designed**, not ad hoc. |
| **CTA_model** | `repeated_soft` + **contextual** primary (quote, find store, download datasheet). |
| **trust_model** | Spec accuracy, warranties, compliance marks, compatibility matrices, support visibility. |
| **UX_model** | `compare` + `browse` |
| **mobile_priority** | `high` for locator and quick spec checks. |
| **content_depth** | `medium`–`deep` (data-heavy). |
| **commercial_intent** | `mixed`–`high` |
| **design_complexity** | `medium`–`high` |
| **frontend_complexity** | `high` (filters, tables, param URLs). |
| **required_blocks** | `category_plp`, `product_detail_template`, `comparison_table`, `spec_accordion`, `support_links` |
| **optional_blocks** | `dealer_locator`, `rfq_form`, `downloads_gated` |
| **forbidden_patterns** | Infinite thin facets indexed; hidden incompatible accessories; fake “in stock” without inventory source. |
| **QA_focus** | Facet indexation rules, table a11y, spec drift vs PDF, performance on PLP, parameter hygiene. |
| **HITL_required** | `selective`; `often` when compliance labels (energy, safety) apply. |
| **notes** | Merge to **`ecommerce`** when on-domain cart/checkout is the dominant path. |

---

### 6. `ecommerce`

| Field | Value |
|--------|--------|
| **site_type_id** | `ecommerce` |
| **category** | `commerce` |
| **primary_goal** | On-domain **purchase** completion (D2C or B2B cart). |
| **monetization_model** | Transaction fees, margin on goods, subscriptions, cross-sell. |
| **typical_pages** | Home, PLP, PDP, cart, checkout, account, policies, shipping/returns, trust badges context. |
| **conversion_logic** | PLP → PDP → cart → checkout; guest vs account; upsell with **cart integrity**. |
| **SEO_model** | `transactional_plp` + PDP long-tail; avoid thin duplicate PDPs. |
| **CTA_model** | `transactional` — add to cart, buy now, sticky cart on mobile. |
| **trust_model** | Reviews (authentic), payment icons, returns, security, stock truthfulness. |
| **UX_model** | `task_complete` on checkout; `browse` on discovery. |
| **mobile_priority** | `high` |
| **content_depth** | `medium` on marketing; `deep` in PDP when technical. |
| **commercial_intent** | `high` |
| **design_complexity** | `medium`–`high` |
| **frontend_complexity** | `high` |
| **required_blocks** | `plp`, `pdp`, `cart`, `checkout_progress`, `policy_returns`, `trust_payment` |
| **optional_blocks** | `recommendations`, `size_guide`, `b2b_quote_in_cart` |
| **forbidden_patterns** | Dark patterns in checkout; fake countdowns; review fraud; sneaky subscriptions. |
| **QA_focus** | Price/display consistency, checkout a11y, payment flows, cookie/consent placement, Core Web Vitals on PLP/PDP. |
| **HITL_required** | `often` for promotions/pricing/legal; `yes` for regulated goods. |
| **notes** | **SAFE UNKNOWN** for payment/shipping integrations until stack is specified — do not document fake “connected” payment flows here. |

---

### 7. `geo_landing`

| Field | Value |
|--------|--------|
| **site_type_id** | `geo_landing` |
| **category** | `programmatic_seo` |
| **primary_goal** | Capture **location-modified** intent (city/region/service). |
| **monetization_model** | Leads, bookings, calls — same as service but **page factory** per geo. |
| **typical_pages** | Template-driven: [service] in [city], optional neighborhoods when real coverage exists. |
| **conversion_logic** | Local proof → CTA; map embed; clear **true** service area. |
| **SEO_model** | `local_pack` + `intent_pages`; careful **duplicate** control via unique local copy blocks. |
| **CTA_model** | `single_primary` (call/book) with tap-to-call on mobile. |
| **trust_model** | Local proof (real projects in area), NAP, reviews tied to **location**, not generic filler. |
| **UX_model** | `scan_and_act` |
| **mobile_priority** | `high` |
| **content_depth** | `shallow` per URL if templated — mitigate with **unique** local paragraphs (**HITL** or strict templates). |
| **commercial_intent** | `high` |
| **design_complexity** | `low`–`medium` |
| **frontend_complexity** | `low`–`medium` (map, schema, optional dynamic phone). |
| **required_blocks** | `local_hero`, `local_proof`, `service_area`, `map_optional`, `cta_call_book`, `faq_local` |
| **optional_blocks** | `neighborhood_list`, `local_team` |
| **forbidden_patterns** | Doorway pages with no local value; same body swapped city name only; fake multiple addresses. |
| **QA_focus** | Uniqueness vs sister pages, schema locality match, NAP match with GBP (if used), index bloat control. |
| **HITL_required** | `often` — thin local scale is a **brand + SEO** risk. |
| **notes** | Programmatic scale without editorial rules → escalate **HITL_required** to `yes`. |

---

### 8. `seo_landing`

| Field | Value |
|--------|--------|
| **site_type_id** | `seo_landing` |
| **category** | `programmatic_seo` |
| **primary_goal** | Earn rankings/citations for a **specific** informational or commercial query cluster. |
| **monetization_model** | Ads, affiliate, leads, or support for **other** SKUs (editorial → money page). |
| **typical_pages** | Long-form article, comparison page, “best X”, tool landing with helpful content. |
| **conversion_logic** | Content satisfies query first; CTAs **secondary** unless **clear** commercial intent query. |
| **SEO_model** | `intent_pages` — one primary intent per URL; internal links to hub/money pages. |
| **CTA_model** | `repeated_soft` or **inline contextual** after value delivered. |
| **trust_model** | Authoritativeness (bylines, sources, methodology), update dates, original data/images. |
| **UX_model** | `read_deep` — TOC, scannable headings, tables, summaries. |
| **mobile_priority** | `high` |
| **content_depth** | `deep` |
| **commercial_intent** | `low`–`mixed` (match query; do not disguise ads as editorial without disclosure). |
| **design_complexity** | `low`–`medium` |
| **frontend_complexity** | `low`–`medium` (TOC, tables, code samples if dev content). |
| **required_blocks** | `article_header`, `toc_optional`, `body_sections`, `sources_or_methodology`, `related_links`, `author_trust` |
| **optional_blocks** | `faq_schema_only_if_genuine`, `comparison_table`, `snippet_summary` |
| **forbidden_patterns** | Thin affiliate lists; FAQ schema on non-FAQ pages; “AI slop” undifferentiated summaries; doorway chains. |
| **QA_focus** | E-E-A-T signals honesty, internal link discipline, snippet bait without delivery, duplicate cluster cannibalization. |
| **HITL_required** | `selective`; `often` for YMYL topics. |
| **notes** | For **AI overview** visibility, see **`ai_visibility_page`** — do not conflate classic SEO landing with **entity** packaging. |

---

### 9. `ai_visibility_page`

| Field | Value |
|--------|--------|
| **site_type_id** | `ai_visibility_page` |
| **category** | `brand` (entity packaging) |
| **primary_goal** | Clear **entity** and **fact** presentation so **third-party** AI systems and summaries can **accurately** represent the brand/product (**not** a guarantee of ranking or inclusion). |
| **monetization_model** | Indirect — supports discovery and trust; may pair with lead gen. |
| **typical_pages** | “What is X”, product truth sheet, FAQ grounded in **verifiable** facts; may live on corporate or docs subdomain. |
| **conversion_logic** | Secondary; primary is **clarity**, consistent naming, structured facts, citations. |
| **SEO_model** | `brand_queries` + **structured clarity**; classic blue-link SEO is **adjacent**, not promised. |
| **CTA_model** | `repeated_soft` — contact/docs after establishing facts. |
| **trust_model** | Primary sources, version/changelog, explicit limitations, contact for corrections. |
| **UX_model** | `read_deep` + **skimmable** fact blocks (definition lists, tables). |
| **mobile_priority** | `standard`–`high` |
| **content_depth** | `medium`–`deep` (precision over volume). |
| **commercial_intent** | `low`–`mixed` |
| **design_complexity** | `low` |
| **frontend_complexity** | `low` |
| **required_blocks** | `entity_definition`, `fact_table`, `scope_and_limits`, `sources`, `contact_corrections` |
| **optional_blocks** | `same_as_links`, `changelog`, `multilingual_facts` |
| **forbidden_patterns** | Claims of “AI ranking” or guaranteed inclusion in models; stuffing keywords for “LLM SEO”; fabricated citations. |
| **QA_focus** | Factual accuracy, no overstated capabilities, alignment with **public** docs, stale date hygiene. |
| **HITL_required** | `often` — public **entity** errors are high reputation risk. |
| **notes** | **SAFE UNKNOWN:** how third-party models ingest or refresh data is **outside** this registry; this row only defines **honest** on-page packaging. |

---

### 10. `hybrid_commercial`

| Field | Value |
|--------|--------|
| **site_type_id** | `hybrid_commercial` |
| **category** | `hybrid` |
| **primary_goal** | **Multiple** revenue motions on one property (e.g. content hub + shop, or corporate + self-serve trial). |
| **monetization_model** | **Mixed**: leads + transactions + partners; requires **explicit** priority per subtree. |
| **typical_pages** | Combination of hub/editorial, product/commerce, and landing-style campaign routes — **must** document primary funnel. |
| **conversion_logic** | Segment by entry channel; avoid **one** global CTA; use role/intent-based paths. |
| **SEO_model** | **Mixed** — risk of cannibalization; needs hub/spoke rules and **clear** primary intent per URL. |
| **CTA_model** | **Segmented** primaries by section; global nav as **wayfinding**, not CTA spam. |
| **trust_model** | Combine **brand/corporate** trust with **commerce** trust where applicable. |
| **UX_model** | `browse` + `read_deep` + `task_complete` depending on subtree. |
| **mobile_priority** | `high` for commerce paths; `standard` for heavy editorial. |
| **content_depth** | `deep` overall; allow `shallow` campaign islands. |
| **commercial_intent** | `high` (varies by subtree). |
| **design_complexity** | `high` |
| **frontend_complexity** | `high` |
| **required_blocks** | **Inherited** from subtrees: at minimum `nav_segmentation`, `intent_routing`, `subtree_hero_templates` (map in project doc). |
| **optional_blocks** | `personalization_hooks` (document **SAFE UNKNOWN** until stack known). |
| **forbidden_patterns** | Single template for all URLs; editorial pages accidentally carrying **transactional** schema; checkout leaks on informational URLs. |
| **QA_focus** | Cannibalization audit, CTA conflict checks, schema/page-type pairing, performance budget per subtree. |
| **HITL_required** | `often` — hybrids amplify policy and analytics mistakes. |
| **notes** | Prefer **declaring** a **primary** `site_type_id` per route group in `workflow-map` / project registry; use `hybrid_commercial` only when the **same** domain truly mixes motions at scale. |

---

## Future integrations

These artefacts are **planned** or **partially described** elsewhere in this pack; they **consume** and **refine** `site_type_id` — they do **not** replace the Site Type Registry.

| Artefact | Role relative to Site Type Registry v0 |
|----------|----------------------------------------|
| **Block Registry v0** ([block-registry-v0.md](block-registry-v0.md); index [registries.md](registries.md)) | Maps `required_blocks` / `optional_blocks` **roles** to canonical `block_id`, semantics, compatibility, and planned validator checks (**documentation only**). |
| **Commercial Pattern Library** | Supplies **ethical** offer framing, urgency, and proof **patterns** filtered by `commercial_intent` and `HITL_required`. |
| **SEO Pattern Library** | Supplies title/meta/internal-link and schema **patterns** constrained by `SEO_model` and `forbidden_patterns`. |
| **Design System Rules** | Translates `design_complexity` and `UX_model` into tokens, components, and density guidance. |
| **Frontend Production Rules** | Translates `frontend_complexity` and block choices into **Gulp/static** implementation and **forbidden** edit paths. |

**Orchestration input:** in a **future** automated pipeline, the **first** stable input for stage routing would be **`site_type_id`** (plus project overrides), driving **defaults** for block shortlists, SEO pattern tier, QA checklist template, and HITL gates — **always** subject to human intake and **SAFE UNKNOWN** where the project does not fit a single row. Phase 1 remains **documentation-first**; no runtime enforcement is claimed.

---

*Registry version: v0 — Markdown only. Last updated: 2026-05-11.*
