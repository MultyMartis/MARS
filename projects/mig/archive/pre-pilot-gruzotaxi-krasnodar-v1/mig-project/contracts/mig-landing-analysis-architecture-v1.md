# MIG Landing Analysis Architecture v1

**Status:** **documented** — domain-level architecture for MIG Landing Analysis (post-capture structuring channel).  
**Not:** implementation, JSON Schema registry, OpenRouter workflows, LLM extraction, block-detection ML, UX/conversion scoring, competitor ranking, ORCA semantics, Deep Research, or runtime product.

**Supersedes:** Implicit «landing observations» projection-only behavior in Website Acquisition §6 and pack builder stubs; «Future Landing Analysis» placeholder in [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) §1.4 / §10.3.  
**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md); Research Session; [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) (`competitors.json`); [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) (`website_snapshots.json`, per-snapshot artifacts).  
**Downstream:** [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) (projected sections — §8); [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md).

**Consumers (future, by reference only):** MIG Worker (landing analysis pass), session spine, operator HITL UX, ORCA, future MARS runtime observers.

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

Landing Analysis **structures observable page facts** into reusable market observations. It **must not** score conversion quality, recommend changes, rank competitors, evaluate design quality, or produce positioning, strategy, or marketing conclusions.

---

## 1. Landing Analysis — definition

### 1.1 What Landing Analysis is

**Landing Analysis** is the MIG processing channel that **transforms Website Acquisition artifacts** into **structured, evidence-linked landing observations** — visible blocks, offers, CTAs, trust elements, forms, and page patterns — suitable for Research Pack projection and ORCA intake **without** crossing into interpretation.

It answers:

> **How are captured page facts organized into a stable, reusable observation model per competitor URL?**

```text
Research Request
    ↓
Research Session
    ↓
Search Acquisition (SERP)
    ↓
Competitor Discovery
    ↓
Website Acquisition
    ↓
website_snapshots.json + snapshots/sites/*
    ↓
Landing Analysis Pass          ← this architecture
    ↓
landing_observations.json + landings/*
    ↓
Research Pack (landing / offer / CTA / trust / block projections)
    ↓
ORCA (R2) — interprets observations
```

| Concern | Landing Analysis owns |
|---------|------------------------|
| Per-snapshot **structuring** of flat extract fields | **Yes** |
| **Visible block** segmentation (hero, FAQ, pricing region, etc.) | **Yes** — structural labels only |
| **Typed** offer / CTA / trust / form / contact **observations** with evidence | **Yes** |
| **Page pattern** tags (e.g. single-scroll LP, multi-section service page) | **Yes** — descriptive, not quality |
| Linkage: `landing_id` ↔ `snapshot_id` ↔ `competitor_id` | **Yes** |
| Ambiguity flags (`confidence: structural` not marketing) | **Yes** |
| **SAFE UNKNOWN** for unresolvable structure | **Yes** |
| Evidence refs to `page.html` / snapshot JSON | **Yes** |
| New HTTP fetch or crawl | **No** — Website Acquisition only |

### 1.2 What Landing Analysis is not

| Anti-pattern | Owner / reason |
|--------------|----------------|
| HTTP fetch, redirect handling, raw HTML archive | **Website Acquisition** |
| Competitor discovery, SERP entity resolution | **Competitor Discovery** |
| UX scoring, conversion judgment, «best landing» | **ORCA** — excluded |
| Competitor **ranking** or relative strength | **ORCA** |
| Design quality, visual hierarchy judgment | **ORCA** |
| Positioning, value proposition synthesis | **ORCA** |
| Campaign / funnel / CRO recommendations | **ORCA** |
| Keyword clustering, intent labels | **ORCA** / **Keyword Intelligence** boundary |
| LLM-invented block labels or offers | **Forbidden** |
| OpenRouter / Deep Research synthesis | **Phase 4** — separate; does not replace landing artifacts |
| Website Factory blueprint generation | **ORCA → Factory** — not MIG |

### 1.3 Acquisition vs structuring vs interpretation

| Layer | Question answered |
|-------|-------------------|
| **Website Acquisition (MIG)** | What was **on the wire** and **in the DOM** at capture time? |
| **Landing Analysis (MIG)** | How are those facts **grouped** into blocks and typed observations with **evidence**? |
| **Interpretation (ORCA)** | What does the market **mean** for strategy, PPC, and Factory? |

**Normative:** Landing Analysis **may re-read** `page.html` for structural segmentation. It **must not** add facts absent from acquisition artifacts except via explicit operator `manual_annotation` (grade A) in Phase 2+.

### 1.4 Relationships

| Capability | Relationship |
|------------|--------------|
| **Website Acquisition** | **Hard upstream** — Landing Analysis **requires** successful or partial snapshots; no pass without `website_snapshots.json` (or explicit operator charter to analyze `manual_import` only). |
| **Competitor Discovery** | **Linkage upstream** — `competitor_id`, domain, entity type; **must not** infer offers from competitor names. |
| **Research Pack** | **Downstream projection** — pack sections are **views**; `landing_observations.json` remains SoT. |
| **Keyword Intelligence** | **Parallel** — may ingest `page_visible` from snapshots independently; Landing Analysis does not replace keyword registry. |
| **Deep Research** | **Out of scope v1** — Phase 4 may **cite** landing observations; must not replace artifact SoT. |
| **ORCA** | **Consumer** — after human approval; interprets structured observations. |
| **Website Factory** | **No direct consumption** — see §9. |

### 1.5 Relationship to current v0.1 implementation

**SAFE UNKNOWN (evidence):** `build-research-pack.js` projects **directly** from `website_snapshots.json` summary rows into pack sections (`formatWebsiteObservationBlocks`). That is **pack projection only**, not Landing Analysis. This architecture defines the **normative** pass and artifacts; implementation **not claimed** in repo until `lib/landing-analysis/` exists.

---

## 2. Analysis inputs

### 2.1 Input evaluation matrix

| Input | Role | Canonical? | Notes |
|-------|------|------------|-------|
| `snapshots/sites/{snapshot_id}/website_snapshot.json` | **Primary SoT** | **Yes** | Flat extract fields, status, grades, `artifact_refs` |
| `snapshots/sites/{snapshot_id}/page.html` | **Structural re-parse** | **Yes** (when present) | Block boundaries, DOM order, section cues |
| `snapshots/sites/{snapshot_id}/headers.json` | **Context only** | **Optional** | Status, redirects, timing — **not** content analysis input |
| `website_snapshots.json` | **Session index** | **Yes** | Plan, coverage, snapshot list |
| `competitors.json` | **Linkage** | **Yes** | `competitor_id`, domain, entity_type, `landing_evidence_refs[]` |
| Research Request (accepted) | **Scope context** | **Conditional** | `scope.niche`, `scope.region`, `page_role` hints — **no** strategy inference |
| `serp_result.json` | **Cross-check only** | **No** (default) | **Must not** populate landing sections without snapshot |
| `research_pack.draft.md` | **Output** | **Forbidden as input** | Pack is projection, not SoT |

### 2.2 Canonical input bundle (per landing)

```text
website_snapshot.json     (required)
page.html                 (required when status success and archive exists)
headers.json              (optional metadata attachment)
competitors.json          (session-level linkage slice for competitor_id)
```

**Normative:** If `page.html` missing but `website_snapshot.json` present → analysis runs in **snapshot-only mode** (structure from flat fields only); record SAFE UNKNOWN «block boundaries not re-derived from HTML».

### 2.3 Forbidden inputs

| Input | Reason |
|-------|--------|
| SERP snippets alone | Not page groundtruth |
| LLM-generated page summaries | Violates acquisition boundary |
| ORCA prior analysis | R2 must not write back into MIG pass |
| Website Factory blueprints | Downstream interpreted artifacts |
| Third-party «landing scores» | Interpretation product |

### 2.4 Research Request — allowed use

| Allowed | Forbidden |
|---------|-----------|
| Copy `scope` into observation metadata for traceability | Infer positioning from `niche` |
| Operator `signals.capture_urls[]` already consumed by acquisition | Override snapshot facts from request |
| `request_type` gates whether landing pass runs | Auto-expand URL plan |

---

## 3. Landing Observation Model

### 3.1 Session index: `landing_observations.json`

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `schema_version` | **Yes** | string | `"0.1"` |
| `session_id` | **Yes** | string | Owning session |
| `generated_at` | **Yes** | ISO-8601 UTC | Pass completion |
| `analysis_phase` | **Yes** | string | `"landing_analysis_v1"` |
| `upstream_artifacts` | **Yes** | object | `{ website_snapshots, competitors }` paths |
| `landings` | **Yes** | array | Summary rows or embedded refs |
| `session_coverage` | **Yes** | enum | `complete` \| `partial` \| `minimal` \| `unknown` |
| `section_evidence_grade` | **Yes** | A–X | Worst grade among landings |
| `safe_unknown` | **O** | string[] | Session-level gaps |

### 3.2 Per-landing object: `landing_observation.json`

Path: `landings/{landing_id}/landing_observation.json`

#### 3.2.1 Identity and linkage

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `landing_id` | **Yes** | string | `{session_id}-la{seq}` e.g. `mig-20260601-a1b2c3-la001` |
| `snapshot_id` | **Yes** | string | Source Website Snapshot |
| `session_id` | **Yes** | string | Session |
| `competitor_id` | **O** | string \| null | From snapshot / competitors |
| `domain` | **Yes** | string | Registrable domain |
| `final_url` | **Yes** | string | Captured URL |
| `page_role` | **Yes** | enum | Same as website snapshot `page_role` |
| `page_type` | **Yes** | enum | §3.2.2 — structural page classification |
| `analyzed_at` | **Yes** | ISO-8601 UTC | Analysis pass timestamp |

#### 3.2.2 `page_type` (structural, not strategic)

| Value | Meaning |
|-------|---------|
| `homepage` | Root / main entry |
| `serp_landing` | SERP destination URL |
| `service_landing` | Single-service focus visible in headings/nav |
| `catalog_entry` | Category/listing hub visible |
| `campaign_landing` | Narrow single-offer scroll (heuristic) |
| `contact_focus` | Contact/form dominant above fold |
| `unknown` | Insufficient structure — **not** failure |

**Normative:** `page_type` is **visible-structure heuristic** — ORCA may disagree; MIG records evidence only.

#### 3.2.3 Observation collections (all evidence-linked)

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `visible_blocks` | **Yes** | array | §4 — `block_id`, `block_type`, order, content_refs |
| `offers` | **Yes** | array | §5 |
| `cta_patterns` | **Yes** | array | §6 |
| `pricing_patterns` | **Yes** | array | Visible price **patterns** — not commercial truth |
| `trust_patterns` | **Yes** | array | §7 |
| `contact_patterns` | **Yes** | array | Phones, emails, messengers, addresses (structured) |
| `form_patterns` | **Yes** | array | Lead/callback forms as visible surfaces |
| `page_patterns` | **Yes** | array | §3.2.4 |
| `evidence` | **Yes** | object | §3.3 |
| `artifact_refs` | **Yes** | object | Paths to this file, upstream snapshot, `page.html` |
| `evidence_grade` | **Yes** | A–X | Inherited worst-case from snapshot + analysis mode |
| `safe_unknown` | **O** | string[] | Landing-level gaps |
| `analysis_notes` | **O** | string | Operator notes |

#### 3.2.4 `page_patterns[]` item (descriptive tags)

| `pattern_id` | Example visible basis |
|--------------|----------------------|
| `single_primary_cta` | One dominant CTA above fold |
| `multi_cta_same_intent` | Several «order» / «buy» labels |
| `phone_prominent` | `tel:` or phone in header |
| `messenger_prominent` | t.me / wa.me in header or hero |
| `long_scroll_sections` | ≥N heading bands (config, default 4) |
| `pricing_table_visible` | Tabular price rows in HTML |
| `review_widget_visible` | iframe/script vendor hint **or** review block text |
| `faq_section_visible` | FAQ heading or accordion markers |

**Forbidden pattern tags:** `high_converting`, `weak_trust`, `better_than_competitors`.

#### 3.2.5 Shared sub-object: `evidence` (on each observation item)

| Field | Required | Meaning |
|-------|----------|---------|
| `source` | **Yes** | `website_snapshot` \| `page_html` \| `manual_annotation` |
| `snapshot_field` | **O** | JSON pointer into snapshot e.g. `/offers/2` |
| `html_anchor` | **O** | `{ start_offset, end_offset }` or `{ selector_hint }` — **non-stable** |
| `verbatim_text` | **O** | Exact visible string |
| `capture_time` | **Yes** | From snapshot `capture_time` |
| `ambiguity` | **O** | `none` \| `low` \| `high` — structural only |

---

## 4. Block Detection

### 4.1 Purpose

Blocks are **visible regions** of the captured page — not design components and not ORCA «sections» for copywriting.

### 4.2 MVP block registry

| `block_type` | Detection principle (deterministic) | Out of scope |
|--------------|-------------------------------------|--------------|
| `hero` | First `h1` + following sibling content until next `h2` or landmark `header`/`main` boundary | Visual hero image quality |
| `offer_block` | Cluster of offer-like headings/list items (from snapshot `offers[]` or `h2`+list) | Whether offer is «compelling» |
| `pricing_block` | Region containing `pricing_signals[]` or table with price regex density | Price fairness |
| `benefits` | Bullet list under headings matching benefit lexicon (config) | Benefit truth |
| `faq` | Heading text matches FAQ patterns (`/faq|вопрос|ответ/i`) + following dl/accordion | Answer quality |
| `reviews` | Review vendor markers, star glyphs, «отзыв» blocks | Sentiment score |
| `cases` | «кейс|портфолио|наши работы|projects» section | Case effectiveness |
| `contacts` | `address`, contact columns, map embeds, contact `h2` | Geo accuracy |
| `lead_form` | `<form>` with ≥2 fields in region | Conversion rate |
| `messenger_cta` | Prominent `t.me` / `wa.me` in header/hero block | Channel preference |

**Phase 2 registry additions (non-MVP):** `nav`, `footer`, `partners`, `certificates_row`, `stats_row`.

### 4.3 `visible_blocks[]` item

| Field | Required | Meaning |
|-------|----------|---------|
| `block_id` | **Yes** | `{landing_id}-b{seq}` |
| `block_type` | **Yes** | Registry enum |
| `order` | **Yes** | Document order index |
| `heading_text` | **O** | Nearest heading verbatim |
| `content_summary` | **O** | **First N chars** of visible text in region only — **not** LLM summary |
| `child_observation_refs` | **O** | IDs linking to offers/ctas/trust within block |
| `detection_method` | **Yes** | `heading_heuristic` \| `dom_landmark` \| `snapshot_field_map` \| `unknown` |
| `evidence` | **Yes** | §3.2.5 |

### 4.4 Detection principles (normative)

1. **Deterministic rules only** in MVP — config-driven regex / heading levels / tag paths.  
2. **No computer vision** — no screenshot layout inference in MVP.  
3. **Overlapping blocks allowed** — record overlap in `safe_unknown` if ambiguous.  
4. **JS shell pages** — if snapshot `render_status: js_shell`, blocks **may be empty**; mandatory SAFE UNKNOWN.  
5. **No design judgment** — block presence is observation, not quality.

### 4.5 Block detection failure modes

| Situation | Behavior |
|-----------|----------|
| No `h1` | `hero` block omitted or `unknown` hero with SAFE UNKNOWN |
| Pricing only in image alt text | **Not detected** — no OCR in MVP |
| Accordion FAQ closed in static HTML | Detect section header only; content may be partial |

---

## 5. Offer Analysis

### 5.1 What qualifies as an offer (MIG)

A **visible offer observation** is a **verbatim or minimally normalized** string that **states a product, service, bundle, or commercial promise** visible on the page — not ORCA «value proposition».

| Qualifies | Does not qualify |
|-----------|------------------|
| «Аренда манипулятора 5 т» | «Лучшая компания города» (marketing claim without product) |
| «Доставка за 24 часа» when tied to service line | Pure navigation («Главная») |
| Service card title in list | Footer copyright |
| Price line «от 12 000 ₽/смена» as **offer+pricing** dual link | Hidden JSON-LD not rendered |

**Source priority:**  
1. Snapshot `offers[]`  
2. `h1`–`h3` in offer_block region  
3. List items under service headings  

### 5.2 `offers[]` item model

| Field | Required | Meaning |
|-------|----------|---------|
| `offer_id` | **Yes** | `{landing_id}-of{seq}` |
| `text` | **Yes** | Visible offer string |
| `offer_surface` | **O** | `heading` \| `list_item` \| `card_title` \| `button_label` \| `unknown` |
| `block_id` | **O** | Containing block |
| `pricing_ref` | **O** | `pricing_id` if co-located |
| `ambiguity` | **O** | `none` \| `multi_interpretation` |
| `evidence` | **Yes** | §3.2.5 |

### 5.3 Evidence storage

- **Always** retain `verbatim_text` equal to snapshot or HTML extract.  
- **Always** set `source: website_snapshot` when mapped from acquisition.  
- When re-segmented from HTML, add `html_anchor` and `source: page_html`.

### 5.4 Ambiguity handling

| Case | Handling |
|------|----------|
| Same string, multiple DOM locations | One observation; `ambiguity: multi_interpretation`; list anchors in evidence |
| Heading could be offer or brand slogan | `ambiguity: high`; **no** disambiguation by niche |
| Empty `offers[]` but service lists in body | Re-parse HTML; if still empty → SAFE UNKNOWN «no offer strings classified» |
| SERP snippet differs from page | **Do not merge** — SERP stays in SERP section |

**Forbidden:** Choosing «primary offer» for the market.

---

## 6. CTA Analysis

### 6.1 CTA types (visible intent surface)

| `cta_type` | Detection basis |
|------------|-----------------|
| `lead_form` | `<form>` submit + field labels (name, phone, email) |
| `phone` | `tel:` link or click-to-call button |
| `messenger` | t.me, wa.me, viber deep links |
| `callback_request` | Labels matching callback lexicon («перезвоните», «заказать звонок») |
| `external_link` | Off-site booking/CRM URLs |
| `anchor_scroll` | `#` href to on-page section |
| `generic_action` | Other CTA pattern matches from config |
| `multi_step` | Visible step indicator («Шаг 1», wizard tabs) — **structure only** |

### 6.2 `cta_patterns[]` item

| Field | Required | Meaning |
|-------|----------|---------|
| `cta_id` | **Yes** | `{landing_id}-cta{seq}` |
| `cta_type` | **Yes** | Enum above |
| `label_text` | **Yes** | Visible label |
| `target_href` | **O** | Resolved URL |
| `element_type` | **O** | `link` \| `button` \| `input` |
| `position_band` | **O** | `header` \| `hero` \| `body` \| `footer` \| `floating` \| `unknown` |
| `form_id` | **O** | Link to `form_patterns[]` |
| `block_id` | **O** | Containing block |
| `evidence` | **Yes** | §3.2.5 |

### 6.3 Lead forms (`form_patterns[]`)

| Field | Required | Meaning |
|-------|----------|---------|
| `form_id` | **Yes** | `{landing_id}-fm{seq}` |
| `action` | **O** | Form action URL |
| `method` | **O** | get/post |
| `fields` | **Yes** | From snapshot `forms[]` |
| `visible_purpose` | **O** | Nearest heading — verbatim |
| `cta_type` | **Yes** | Always `lead_form` when observation is form-centric |

### 6.4 Multi-step CTA (structural)

Record **visible steps only** — e.g. `{ steps_visible: 3, step_labels: ["Контакты", "Детали", "Отправить"] }`.  
**Must not** infer completion rates or funnel drop-off.

### 6.5 Representation rules

- Map from snapshot `cta_elements[]` first; enrich type from href/field patterns.  
- **No ranking** of CTAs by importance.  
- Duplicate labels → separate observations with distinct evidence anchors.

---

## 7. Trust Analysis

### 7.1 Trust pattern types (capture only)

| `trust_type` | Examples (visible text / structure) |
|--------------|-------------------------------------|
| `review_snippet` | Review quotes, aggregator widget text |
| `rating_display` | «4.9», star count visible as text |
| `case_reference` | Client logos list, «наши клиенты» |
| `guarantee` | «гарантия», «возврат» |
| `certificate` | ISO, license numbers visible |
| `experience_claim` | «с 2010 года», «10 лет на рынке» |
| `statistics` | «500+ клиентов», «1000 проектов» |
| `partner_badge` | Bank/partner logos with alt text |
| `legal_entity` | ИНН/ОГРН visible in footer |

### 7.2 `trust_patterns[]` item

| Field | Required | Meaning |
|-------|----------|---------|
| `trust_id` | **Yes** | `{landing_id}-tr{seq}` |
| `trust_type` | **Yes** | Enum above |
| `text` | **Yes** | Verbatim visible string |
| `numeric_value` | **O** | Parsed number if present — **no** validation |
| `block_id` | **O** | Containing block |
| `evidence` | **Yes** | §3.2.5 |

### 7.3 Capture rules

1. Ingest `trust_signals_visible[]` from snapshot.  
2. Re-scan HTML for review/FAQ/case blocks per §4.  
3. **No trust score**, no authenticity judgment, no «social proof strength».  
4. Rating without source → `trust_type: rating_display`, `ambiguity: high`.

---

## 8. Research Pack Integration

### 8.1 Projection model

Landing Analysis **feeds** existing Research Pack section ids — **no rename**:

| Pack section id | Projected from |
|-----------------|----------------|
| `landing_observations` | `page_type`, `page_patterns`, top blocks summary, title/meta via snapshot ref |
| `offer_observations` | `offers[]` |
| `cta_observations` | `cta_patterns[]` + `form_patterns[]` |
| `trust_observations` | `trust_patterns[]` |
| `block_observations` | **New subsection** under landing (markdown) or merged into landing — **full blocks in artifact only** |

**Normative:** Pack uses section id `landing_observations` per [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md); «Website observations» markdown heading in v0.1 spine is a **representation label** — align to `landing_observations` in future spine revision.

### 8.2 Projection rules

| Rule | Detail |
|------|--------|
| Artifacts = SoT | Pack lists excerpts + `landing_id` / `snapshot_id` refs |
| Caps (MVP) | Max 5 offers, 5 CTAs, 5 trust, 5 pricing, 10 block summaries per landing in pack |
| Grades | Section grade = worst landing `evidence_grade` |
| Duplication | Do not duplicate SERP snippets or competitor narrative |
| Missing pass | SAFE UNKNOWN: «Landing Analysis pass not executed» |
| Partial pass | Per-competitor gaps listed |

### 8.3 Artifact registry extensions

| Artifact key | Path |
|--------------|------|
| `landing_observations` | `landing_observations.json` |
| `landing_detail` | `landings/{landing_id}/landing_observation.json` |

Register in `session_manifest.artifacts` when pass completes.

### 8.4 `mig_phase` interaction

| Condition | Pack behavior |
|-----------|---------------|
| Landing pass complete with ≥1 landing grade ≤ C | `mig_phase` ≥ `3`; populate landing/offer/cta/trust from **landing artifacts** |
| Website acquisition only (no landing pass) | May project from snapshot (legacy path) + SAFE UNKNOWN «structured landing analysis pending» |
| All landings X | Sections minimal + mandatory SAFE UNKNOWN |

---

## 9. Website Factory Relationship

### 9.1 Consumption path (normative)

```text
MIG Landing Analysis artifacts
    ↓ (human-approved Research Pack)
ORCA interpretation
    ↓
Strategy / content-pack / blueprint artifacts
    ↓
Website Factory (R3)
```

### 9.2 What Website Factory may consume

| Allowed (via ORCA chain) | Form |
|--------------------------|------|
| ORCA-derived **semantic locks**, page briefs, content packs | ORCA-owned artifacts |
| Operator-approved **interpreted** competitor summaries | ORCA workspace |
| Explicit human export of **observation tables** for reference | HITL copy — not automated pipe |

### 9.3 What Website Factory must never consume directly

| Forbidden direct intake | Reason |
|-------------------------|--------|
| `landing_observations.json` / `landings/*` | Uninterpreted groundtruth — R1 only |
| `page.html` raw archives | Acquisition evidence, not blueprint input |
| `website_snapshots.json` | Same |
| Unapproved `research_pack.draft.md` | No HITL |
| MIG session folders by path convention | Boundary per [boundaries.md](../boundaries.md) |

### 9.4 What remains ORCA responsibility

- Positioning, offers prioritization, trust narrative  
- Landing **strategy** and Factory blueprint semantics  
- Which competitor patterns matter for production  
- Conversion and design recommendations  

**Normative:** Factory **must not** read MIG session directories as a default integration (aligned with Research Pack §1 and boundaries).

---

## 10. Roadmap

### 10.1 MVP (Landing Analysis v0.1)

| # | Deliverable | Acceptance |
|---|-------------|------------|
| 1 | `run-landing-pass.js` | Reads `website_snapshots.json`; emits `landing_observations.json` |
| 2 | Per-landing artifact writer | `landings/{landing_id}/landing_observation.json` |
| 3 | Snapshot-field mapper | Offers/CTA/trust/forms from snapshot → typed models |
| 4 | Minimal block detector | Hero + offer_block + lead_form from headings/HTML |
| 5 | Pack projection switch | Prefer landing artifacts over raw snapshot rows |
| 6 | `verify-landing-analysis-v0.mjs` | Golden fixtures from `test/fixtures/website-html/` |
| 7 | SAFE UNKNOWN discipline | js_shell, skipped snapshots documented |

**MVP scope limits:**

- One landing per snapshot (1:1)  
- No LLM, no OpenRouter, no new HTTP  
- No Deep Research integration  
- Block registry: **subset** §4.2 MVP table only  

### 10.2 Phase 2

| Item | Notes |
|------|-------|
| Full block registry | FAQ, reviews, cases, pricing_block, messenger_cta |
| HTML re-segmentation | `page.html` anchors for all blocks |
| `page_patterns` enrichment | Configurable lexicon per `scope.region` |
| Second URL per entity | When Website Acquisition Phase 2 adds pricing/contact pages — **one landing per snapshot** |
| Operator `manual_annotation` | Grade A evidence for mis-detected blocks |
| Competitor cross-landing index | Session-level matrix artifact (facts only, **no** ranking columns) |

### 10.3 Phase 3

| Item | Notes |
|------|-------|
| Playwright-rendered DOM analysis | Only when acquisition provides `dom.html` |
| Cross-session landing pattern corpus | Aggregated **frequency of visible patterns** — still not strategy |
| Optional review-widget vendor parsers | Visible text only |
| Pack `research_pack.json` serialization | Machine interchange for landing sections |

### 10.4 Explicitly out of scope (all phases unless new charter)

- Deep Research synthesis replacing landing artifacts  
- Conversion scoring, A/B judgment, design critique  
- ORCA handoff automation changes  
- Website Factory direct MIG wiring  
- Competitor ranking matrices  

---

## 11. Architecture decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| **LA-01** | Landing Analysis is **separate** from Website Acquisition | Fetch vs structure; stable artifacts |
| **LA-02** | **No new network I/O** in landing pass | Preserves acquisition SoT |
| **LA-03** | `landing_observation.json` is artifact SoT; pack is projection | Research Pack contract |
| **LA-04** | Blocks are **structural**, not design components | MIG/ORCA boundary |
| **LA-05** | Ambiguity recorded, not resolved by niche context | No interpretation |
| **LA-06** | Snapshot `offers[]` seed offer model; HTML refines | Reuse acquisition work |
| **LA-07** | 1:1 `landing_id` ↔ `snapshot_id` in MVP | Scope control |
| **LA-08** | Trust patterns typed but **not scored** | Boundary compliance |
| **LA-09** | Factory consumes ORCA outputs only | boundaries.md |
| **LA-10** | Legacy pack projection from snapshots remains until pass ships | Operational continuity |

---

## 12. Risks

| Risk | Mitigation |
|------|------------|
| Duplicate truth (snapshot vs landing) | Landing pass **references** snapshot; does not mutate snapshot files |
| Block detector false positives | `ambiguity` + HITL; conservative rules |
| Operators confuse structure with strategy | Pack labels «visible structure only» |
| JS-heavy sites empty analysis | Inherit `render_required` SAFE UNKNOWN from acquisition |
| Scope creep into scoring | Explicit non-goals + verifier checks |
| v0.1 spine bypasses landing pass | Document «projection-only» until MVP implemented |

---

## 13. Proposed implementation artifacts (not required for architecture approval)

| Artifact | Path (proposed) |
|----------|-----------------|
| Landing observation schema | `schemas/landing-observation-v0.1.schema.json` |
| Session index schema | `schemas/landing-observations-v0.1.schema.json` |
| Block registry config | `config/landing-block-registry-v0.json` |
| Library | `lib/landing-analysis/*` |
| Verifier | `tools/verify-landing-analysis-v0.mjs` |
| Pack builder extension | `lib/session-spine/build-research-pack.js` |

---

## 14. Explicit non-goals

- Implementation, n8n wiring, OpenRouter  
- Deep Research  
- ORCA / Website Factory redesign  
- UX scoring, conversion evaluation, recommendations, competitor ranking  
- Proof that landing pass exists in repo  

---

## Related

| Document | Path |
|----------|------|
| Website Acquisition | [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) |
| Research Pack | [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) |
| Competitor Discovery | [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) |
| Keyword Intelligence | [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) |
| ORCA handoff | [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) |
| Boundaries | [../boundaries.md](../boundaries.md) |
| Data Acquisition (overview) | [../reports/REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) |

---

*Architecture v1 — documentation only. No implementation. No git commit by default.*
