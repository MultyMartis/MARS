# MIG Keyword Surface Capability Model v1

**Status:** **normative** — capability definitions only (Phase 2b)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2b — Keyword Surface Intelligence (Demand Surface)  
**Prior artifacts:** [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](../reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) · [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md)  
**Related (reference, not superseded):** [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md)  
**Validated market (examples):** Грузотакси / Краснодар / проект Триумф

**This document delivers:** normative capability ids, modifier taxonomy, intent signal model, boundaries, non-goals, reality review.

**This document does not deliver:** runtime, schemas, acquisition adapters, Wordstat implementation, API integration, ORCA semantics, SEO strategy, or Phase 1 redesign.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

Keyword Surface records **observable query language** — phrases, modifiers, and attached signals — at capture time. It **must not** cluster, prioritize, interpret intent for strategy, or estimate difficulty.

---

## Scope of this model

| In scope | Out of scope |
|----------|--------------|
| What MIG **should understand** about demand language | How data is **fetched** |
| Capability ids (`KS-CAP-*`), modifier types (`KS-MOD-*`), intent signals (`KS-INT-*`) | JSON Schema, registry files, pack builder |
| Evidence **source candidates** (logical channels) | Acquisition decisions, API choice, Wordstat ingest |
| SAFE UNKNOWN discipline per capability | Frequency interpretation, volume recommendations |
| Layer boundaries (KS-01..KS-06 from charter) | ORCA intent taxonomy, campaign grouping |

---

## Capability families — overview

Capabilities group into **four families**. Families are organizational only — not runtime modules.

| Family | ID prefix | Question answered |
|--------|-----------|-------------------|
| **Phrase registry** | `KS-CAP-PHR-*` | What exact strings were observed? |
| **Modifier surface** | `KS-CAP-MOD-*` | What lexical modifiers attach to phrases? |
| **Signal surface** | `KS-CAP-SIG-*` | What non-modifier demand signals appear in text? |
| **Numeric demand** | `KS-CAP-NUM-*` | What raw numeric signals attach to phrases (when captured)? |

**Normative:** A capability definition states **what may be recorded**, not **how** it is extracted. Extraction may be operator-declared, rule-based, or deferred — separate gate.

---

## Phrase registry capabilities

### KS-CAP-PHR-SEED — Declared seed query

| Field | Value |
|-------|-------|
| **Purpose** | Record exact query strings declared in Research Request before or at session bind — primary demand anchor. |
| **Examples** | «грузотакси Краснодар»; «перевозка мебели Краснодар»; «заказать газель Краснодар» |
| **Evidence source candidates** | `research_request.queries.seed_queries[]`; session manifest mirror; pack Query Set section |
| **Known ambiguity** | Seed may differ in casing/spacing from executed query; seed may never be run on SERP |
| **SAFE UNKNOWN** | If request lacks seeds: «Declared seed queries not supplied — demand anchor unknown» |
| **Boundary** | Seed is **phrase evidence**, not Market Surface entity. KS-03 applies. |

### KS-CAP-PHR-EXEC — Executed query

| Field | Value |
|-------|-------|
| **Purpose** | Record exact strings actually submitted to search acquisition — proves what was searched. |
| **Examples** | «грузотакси Краснодар» (from mqgt01 manifest `queries_executed`) |
| **Evidence source candidates** | `session_manifest.queries_executed[]`; `serp_result.json` query metadata; multi-query discovery index |
| **Known ambiguity** | Executed set may be subset of seeds (failed queries — q05–q07 in pilot); normalization for dedup ≠ display string |
| **SAFE UNKNOWN** | «Query X in seed list was not executed — SERP outcome for X unknown» |
| **Boundary** | Market Surface owns **SERP outcome** for same string; Keyword Surface owns **string as demand evidence**. KS-03. |

### KS-CAP-PHR-SUGGEST — Suggestion string

| Field | Value |
|-------|-------|
| **Purpose** | Record autocomplete / suggestion list strings returned for a seed — ordered or unordered, unexpanded. |
| **Examples** | «грузотакси краснодар недорого»; «грузотакси краснодар цены»; «грузотакси краснодар с грузчиками» |
| **Evidence source candidates** | Future `suggestions_snapshot.json`; operator paste import; provider API response (future gate) |
| **Known ambiguity** | Suggestion rank may be unstable over time; engine/locale/device affect list |
| **SAFE UNKNOWN** | «Autocomplete suggestion surface not captured for this session» |
| **Boundary** | Single-depth only (KI-03). No recursive expansion. Not executed query unless separately run. |

### KS-CAP-PHR-RELATED — SERP related search string

| Field | Value |
|-------|-------|
| **Purpose** | Record refinement strings visible on captured SERP («people also search» blocks) — strings only. |
| **Evidence source candidates** | Extract from existing `serp_result.json` when block present; operator manual note |
| **Examples** | «грузотакси краснодар отзывы»; «вызов газели краснодар» — **pilot-scoped examples; capture not proven in MVP** |
| **Known ambiguity** | Block may be absent, collapsed, or engine-specific; related string ≠ user demand proof |
| **SAFE UNKNOWN** | «SERP related-search block not present or not extracted» |
| **Boundary** | Clickable result URLs → Market Surface. KS-04. |

### KS-CAP-PHR-PAGE — Page-visible phrase

| Field | Value |
|-------|-------|
| **Purpose** | Record phrase strings visible on acquired competitor pages (title, H1, meta) as demand-language evidence with distinct provenance. |
| **Examples** | «Грузовое такси в Краснодаре. Заказать недорогое грузотакси» (title from gtrgt01 ws003) |
| **Evidence source candidates** | `website_snapshot.json` title, H1, meta_description; landing observation extracts |
| **Known ambiguity** | Page copy reflects **supplier messaging**, not independent search demand; same string may appear in SERP title |
| **SAFE UNKNOWN** | «Page-visible phrase channel not indexed — competitor lexicon on pages unknown» |
| **Boundary** | Website Intelligence owns page facts; Keyword Surface may **reference** same string with `source_type: page_visible`. KS-02. |

### KS-CAP-PHR-OPERATOR — Operator-supplied phrase

| Field | Value |
|-------|-------|
| **Purpose** | Record phrases added by operator outside automated capture — imports, annotations, manual vocabulary pass. |
| **Examples** | Operator tags mqgt01 query set with modifier notes; CSV phrase drop (future) |
| **Evidence source candidates** | Operator annotation file; manifest `operator_phrases[]` (future); HITL worksheet |
| **Known ambiguity** | Operator phrase may not have been searched or validated in Wordstat |
| **SAFE UNKNOWN** | «Operator phrase list not supplied — extended vocabulary unknown» |
| **Boundary** | Evidence grade `operator`. Must not auto-trigger SERP or Wordstat. |

---

## Modifier surface capabilities

**Definition:** A **modifier** is an **observable token or short pattern** within or adjacent to a phrase that narrows geo, service, commercial shape, urgency, etc. Modifiers are **lexical observations** — not intent classes, not segments, not campaign groups.

**Attachment rule:** Modifiers attach to a **host phrase** (`host_phrase_ref`) or span within it. One phrase may carry **multiple** modifier tags. Tags may overlap (e.g. COMMERCIAL + PRICE on «недорого»).

**Extraction rule (planning):** Tags may be operator-declared or pattern-matched — **method not fixed here**.

---

### KS-CAP-MOD-GEO — Geo modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify geographic tokens that scope the query to a place — city, region, district, directional preposition + place. |
| **Examples** | «краснодар»; «по краснодару»; «в краснодаре»; «грузотакси **краснодар**» |
| **Evidence source candidates** | Token match in seed/executed/suggestion strings; `scope.region` cross-check; operator tag |
| **Known ambiguity** | Homonyms (street names, brand names containing city); «рядом» without named place is LOCATION_SIGNAL not GEO |
| **SAFE UNKNOWN** | «Geo modifier extraction not run — place scoping tokens unknown» |
| **Boundary** | Does not validate correct geography or service area. Does not infer «local intent». |

### KS-CAP-MOD-SERVICE — Service modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify service variant, vehicle class, load type, or delivery mode wording in the query. |
| **Examples** | «газель»; «грузоперевозки»; «с грузчиками»; «перевозка мебели»; «квартирный переезд»; «грузовое такси» |
| **Evidence source candidates** | Seed query set (pilot); suggestions; page-visible titles; operator glossary |
| **Known ambiguity** | «грузотакси» vs «грузовое такси» — near-synonym strings, not automatically merged; «мебель» may be cargo type or vertical |
| **SAFE UNKNOWN** | «Service modifier vocabulary not derived for this session» |
| **Boundary** | Not a service taxonomy for ORCA. Not SKU or tariff classification. |

### KS-CAP-MOD-COMMERCIAL — Commercial modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify transactional or purchase-path language — order, buy, hire, tariff framing — without labeling «commercial intent». |
| **Examples** | «заказать»; «вызов»; «услуга»; «тариф»; «заказать газель краснодар» |
| **Evidence source candidates** | Executed queries; SERP titles/snippets (string channel); suggestions |
| **Known ambiguity** | Overlap with ACTION_SIGNAL («заказать»); overlap with PRICE («тариф»); Russian impersonal forms |
| **SAFE UNKNOWN** | «Commercial-shape tokens not tagged — transactional wording unknown» |
| **Boundary** | **Forbidden:** assigning funnel stage, conversion probability, or bid strategy. |

### KS-CAP-MOD-URGENCY — Urgency modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify time-pressure or immediacy tokens in query text. |
| **Examples** | «срочно»; «быстро»; «сегодня»; «24 часа»; «круглосуточно» |
| **Evidence source candidates** | Query strings; suggestions; page-visible copy (with `page_visible` provenance) |
| **Known ambiguity** | «24 часа» may mean availability (ATTRIBUTE) vs urgency; «быстрая подача» in ad copy ≠ user query |
| **SAFE UNKNOWN** | «Urgency tokens not extracted from query surface» |
| **Boundary** | Not SLA promise. Not dispatch priority for operations. |

### KS-CAP-MOD-PRICE — Price modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify price, cost, cheapness, or rate language in query text. |
| **Examples** | «дешево»; «недорого»; «цены»; «цена»; «стоимость»; «от 539 руб» (if appears in captured string) |
| **Evidence source candidates** | Queries; suggestions; related searches; Wordstat phrase column (future) |
| **Known ambiguity** | Overlap COMMERCIAL («тариф»); numeric price in string vs frequency column; «без переплат» is marketing claim |
| **SAFE UNKNOWN** | «Price-shape tokens not tagged in phrase surface» |
| **Boundary** | **Forbidden:** price recommendations, margin analysis, bid caps. Numeric **frequency** belongs to KS-CAP-NUM-*, not this modifier. |

### KS-CAP-MOD-QUESTION — Question modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify interrogative or question-shaped phrasing — lexical form only. |
| **Examples** | «сколько стоит грузотакси»; «как заказать газель»; «где грузотакси краснодар»; tokens «сколько», «как», «где», «можно ли» |
| **Evidence source candidates** | Query strings; suggestions; related searches |
| **Known ambiguity** | Question form ≠ informational intent (ORCA); rhetorical titles on landing pages |
| **SAFE UNKNOWN** | «Question-form phrases not flagged — interrogative shape unknown» |
| **Boundary** | Pairs with KS-INT-QUESTION signal but does not **classify** intent. No FAQ routing. |

### KS-CAP-MOD-BRAND — Brand modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify branded or trade-name tokens in query text — operator brand, franchise, platform. |
| **Examples** | «грузовичкоф»; «gruzovichkof»; «taximaxim»; «авито» (when in query string) |
| **Evidence source candidates** | Query strings; suggestions; operator brand list (declared, not inferred) |
| **Known ambiguity** | Brand in query vs brand in SERP result domain (Market Surface); genericized trademarks |
| **SAFE UNKNOWN** | «Brand token list not declared — branded queries not tagged» |
| **Boundary** | Does not identify «navigational intent». Domain ownership → Market Surface. |

### KS-CAP-MOD-COMPETITOR — Competitor modifier

| Field | Value |
|-------|-------|
| **Purpose** | Identify competitor or aggregator names appearing **inside query text** (not SERP domain column). |
| **Examples** | «грузотакси грузовичкоф»; «газель maxim краснодар» — **hypothetical query shapes** |
| **Evidence source candidates** | Query strings; suggestions; operator-maintained competitor alias list cross-walk |
| **Known ambiguity** | Strong overlap with BRAND_MODIFIER; competitor entity card lives in Market Surface / Atlas (future) |
| **SAFE UNKNOWN** | «Competitor names in query text not tagged — comparative query shape unknown» |
| **Boundary** | SERP ranking of competitor **URLs** → Market Surface. This modifier is **string-only**. |

---

## Signal surface capabilities

Signals are **observable patterns** that are not simple modifier tokens but still attach to phrase evidence. They overlap modifiers by design — record **both** when evidence supports it; do not collapse into one ORCA label.

### KS-CAP-SIG-INTENT — Intent signal (lexical)

| Field | Value |
|-------|-------|
| **Purpose** | Record **evidence-only** intent **shape** flags derived from phrase text — see §Intent Signal Model. Not ORCA intent taxonomy. |
| **Examples** | Flag set `{ commercial_shape, local_shape }` on «заказать газель краснодар недорого» |
| **Evidence source candidates** | Rule/operator derivation from phrase + modifiers; **never** from SERP position alone |
| **Known ambiguity** | Multiple shapes may apply; «unknown» is valid; shape ≠ user motivation |
| **SAFE UNKNOWN** | «Intent shape signals not derived — phrase intent surface unknown» |
| **Boundary** | **Forbidden:** ORCA enums, funnel labels, content-type recommendations. |

### KS-CAP-SIG-ACTION — Action signal

| Field | Value |
|-------|-------|
| **Purpose** | Identify verb-led or imperative action tokens suggesting desired user action in the query. |
| **Examples** | «заказать»; «вызвать»; «найти»; «арендовать»; «заказать газель» |
| **Evidence source candidates** | Token match in phrase; overlap list with COMMERCIAL_MODIFIER |
| **Known ambiguity** | Action in query vs CTA on landing (Website Intelligence) |
| **SAFE UNKNOWN** | «Action tokens not extracted from phrases» |
| **Boundary** | Not conversion tracking. Not CTA effectiveness score. |

### KS-CAP-SIG-LOCATION — Location signal

| Field | Value |
|-------|-------|
| **Purpose** | Identify proximity or place-relative language **without** a resolved geo entity — «near me» class. |
| **Examples** | «рядом»; «близко»; «возле»; «по адресу» (without address); «на дом» |
| **Evidence source candidates** | Query strings; suggestions |
| **Known ambiguity** | «по краснодару» is GEO not LOCATION; geolocation not captured in MIG |
| **SAFE UNKNOWN** | «Proximity language not tagged; user geolocation unknown» |
| **Boundary** | Does not resolve coordinates or service radius. |

### KS-CAP-SIG-ATTRIBUTE — Attribute signal

| Field | Value |
|-------|-------|
| **Purpose** | Identify product/service attribute tokens — capacity, hours, equipment, quality — not covered by SERVICE or PRICE alone. |
| **Examples** | «24 часа»; «1.5т»; «до 3 тонн»; «с грузчиками» (also SERVICE); «отзывы»; «рейтинг»; «без переплат» |
| **Evidence source candidates** | Query strings; page-visible copy; related searches |
| **Known ambiguity** | «отзывы» triggers comparison/reputation shape (INTENT) and ATTRIBUTE; «24 часа» vs URGENCY |
| **SAFE UNKNOWN** | «Attribute tokens not tagged on phrase surface» |
| **Boundary** | Not product catalog. Not trust score. |

---

## Numeric demand capabilities (placeholder)

Numeric capabilities name **what may be stored** when a provider returns numbers. **No acquisition authorized** by this document.

### KS-CAP-NUM-FREQ — Frequency signal

| Field | Value |
|-------|-------|
| **Purpose** | Attach raw frequency values to a phrase+region+period as returned by provider — uninterpreted. |
| **Examples** | `shows: 12400` for «грузотакси краснодар» (illustrative — **not captured in MVP**) |
| **Evidence source candidates** | Future `wordstat_snapshot.json`; manual export row; API response (future gate) |
| **Known ambiguity** | Column semantics vary by export; broad vs exact match; period mismatch |
| **SAFE UNKNOWN** | «Frequency evidence not captured for this session» — **never** infer from SERP recurrence |
| **Boundary** | **Forbidden:** head/tail label, volume tier, «high/low demand» prose. |

### KS-CAP-NUM-TREND — Trend signal

| Field | Value |
|-------|-------|
| **Purpose** | Attach period-over-period or time-series values when present in provider export. |
| **Examples** | Month-over-month column in Wordstat export — **SAFE UNKNOWN until export chartered** |
| **Evidence source candidates** | Wordstat export columns; provider API (future) |
| **Known ambiguity** | Seasonality interpretation → ORCA; incomplete series |
| **SAFE UNKNOWN** | «Trend evidence not present in source export» |
| **Boundary** | No forecasting. No seasonality narrative in MIG pack. |

### KS-CAP-NUM-SHARE — Share / ratio signal

| Field | Value |
|-------|-------|
| **Purpose** | Store share, click share, or ratio columns exactly as returned — no recomputation. |
| **Examples** | `shows_share` column when mapped in Keyword Intelligence logical shape |
| **Evidence source candidates** | Wordstat export; API (future) |
| **Known ambiguity** | Column may be absent; denominator unknown |
| **SAFE UNKNOWN** | «Share columns not present in export — ratio signals unknown» |
| **Boundary** | No market share conclusions in MIG artifacts. |

---

## Modifier taxonomy

### What types of modifier can exist?

MIG recognizes **eight modifier types** (`KS-MOD-*`) aligned to capabilities KS-CAP-MOD-*. A ninth cross-cutting type **NONE** applies when no modifier tag is attached — absence is explicit, not implied.

| Taxonomy id | Capability | Token class | Example tokens / spans |
|-------------|------------|-------------|-------------------------|
| **KS-MOD-GEO** | KS-CAP-MOD-GEO | Place names, directional geo phrases | краснодар, по краснодару, в краснодаре |
| **KS-MOD-SERVICE** | KS-CAP-MOD-SERVICE | Service / vehicle / cargo / crew | газель, грузоперевозки, с грузчиками, мебель, переезд |
| **KS-MOD-COMMERCIAL** | KS-CAP-MOD-COMMERCIAL | Transaction / order path | заказать, вызов, услуга, тариф |
| **KS-MOD-URGENCY** | KS-CAP-MOD-URGENCY | Time pressure | срочно, быстро, сегодня |
| **KS-MOD-PRICE** | KS-CAP-MOD-PRICE | Price / cost framing | дешево, недорого, цены, стоимость |
| **KS-MOD-QUESTION** | KS-CAP-MOD-QUESTION | Interrogative shape | сколько, как, где, сколько стоит … |
| **KS-MOD-BRAND** | KS-CAP-MOD-BRAND | Named brand / franchise in query | грузовичкоф, taximaxim |
| **KS-MOD-COMPETITOR** | KS-CAP-MOD-COMPETITOR | Competitor / aggregator name in query | *(operator-list dependent)* |

**Signal types** (`KS-SIG-*`) may co-exist on the same phrase: ACTION, LOCATION, ATTRIBUTE, INTENT (lexical shape set).

### Pilot phrase classification (illustrative)

No frequency assumptions. Classification shows **taxonomy application** on real pilot seeds (gtrgt01 / mqgt01).

| Phrase (pilot) | Modifier tags | Signal tags | Notes |
|----------------|---------------|-------------|-------|
| грузотакси Краснодар | GEO | local_shape | Core seed |
| грузовое такси Краснодар | GEO, SERVICE | local_shape | Synonym variant |
| газель Краснодар | GEO, SERVICE | local_shape | Vehicle class |
| грузоперевозки Краснодар | GEO, SERVICE | local_shape, commercial_shape | |
| перевозка мебели Краснодар | GEO, SERVICE | local_shape, commercial_shape | Cargo type |
| квартирный переезд Краснодар | GEO, SERVICE | local_shape, commercial_shape | |
| вызов газели Краснодар | GEO, SERVICE, COMMERCIAL, ACTION | local_shape, commercial_shape | |
| газель с грузчиками Краснодар | GEO, SERVICE | local_shape, commercial_shape | «с грузчиками» also ATTRIBUTE |
| грузовое такси с грузчиками Краснодар | GEO, SERVICE | local_shape, commercial_shape | |
| грузоперевозки по Краснодару | GEO, SERVICE | local_shape | Prepositional geo |
| заказать газель Краснодар | GEO, SERVICE, COMMERCIAL, ACTION | local_shape, commercial_shape | |
| *(hypothetical)* грузотакси краснодар **срочно** | GEO, URGENCY | local_shape, commercial_shape | Not in pilot seeds |
| *(hypothetical)* грузотакси краснодар **дешево** | GEO, PRICE | local_shape, commercial_shape, comparison_shape | |
| *(hypothetical)* грузотакси краснодар **цены** | GEO, PRICE | local_shape, comparison_shape | |
| *(hypothetical)* **сколько стоит** грузотакси краснодар | GEO, QUESTION, PRICE | question_shape, comparison_shape | |
| *(hypothetical)* грузотакси краснодар **отзывы** | GEO, ATTRIBUTE | comparison_shape, support_shape | Reputation attribute |
| *(hypothetical)* грузотакси **рядом** | LOCATION | local_shape, unknown | No named city token |

### Taxonomy rules

| Rule id | Statement |
|---------|-----------|
| **MT-01** | Modifiers are **multi-label** — a phrase may carry zero to many tags. |
| **MT-02** | Tags record **observed tokens**, not inferred user persona. |
| **MT-03** | Overlapping tags (PRICE + COMMERCIAL) are **allowed** — do not merge for convenience. |
| **MT-04** | Tags on `page_visible` phrases **must** carry provenance distinct from seed/suggestion. |
| **MT-05** | Operator may override or add tags with `evidence_grade: operator` — still not ORCA interpretation. |
| **MT-06** | **No** frequency-based modifier prominence — «common modifier» is **UNKNOWN** without Wordstat. |

---

## Intent signal model

### Purpose

Provide a **lightweight MIG reality model** for phrase-level **shape flags** — evidence derived from text and modifier tags only. This is **not** ORCA intent clustering, **not** a semantic core, **not** a content plan.

### Intent signal enum (`KS-INT-*`)

| Signal id | Meaning (evidence-only) | Typical lexical triggers | Example phrase sketch |
|-----------|-------------------------|--------------------------|---------------------|
| **KS-INT-COMMERCIAL** | Transactional or hire wording present | заказать, вызов, услуга, тариф + SERVICE tokens | заказать газель краснодар |
| **KS-INT-INFORMATIONAL** | Explain / learn shape (non-question) | «виды», «что такое», guides — **rare in pilot seeds** | что такое грузотакси |
| **KS-INT-COMPARISON** | Compare, price-check, reviews shape | цены, отзывы, рейтинг, сравнить, недорого vs дешево context | грузотакси краснодар цены |
| **KS-INT-LOCAL** | Named geo or local scoping present | city tokens, «по краснодару», «в краснодаре» | грузотакси краснодар |
| **KS-INT-SUPPORT** | Help / problem / contact shape | телефон, контакты, жалоба — **more common on pages than queries** | *(page_visible)* «как связаться» |
| **KS-INT-QUESTION** | Interrogative form | сколько, как, где, можно ли | сколько стоит грузотакси краснодар |
| **KS-INT-UNKNOWN** | Insufficient evidence for other shapes | single generic token; ambiguous string | газель *(without geo in short query)* |

### Derivation rules (normative planning)

| Rule id | Statement |
|---------|-----------|
| **IS-01** | Intent signals are **flags**, not a single exclusive class — use a **set** per phrase. |
| **IS-02** | **KS-INT-LOCAL** requires geo modifier or explicit place token — not inferred from `scope.region` alone. |
| **IS-03** | **KS-INT-QUESTION** requires QUESTION modifier or «?» in captured string. |
| **IS-04** | **KS-INT-UNKNOWN** must appear when no other signal is evidenced — do not default to COMMERCIAL. |
| **IS-05** | SERP position, ad presence, or competitor count **must not** set intent signals. |
| **IS-06** | Intent signals **must not** appear in artifacts as `intent: "commercial"` ORCA enums — use `intent_shape_flags[]` with `KS-INT-*` ids only (future schema gate). |

### Intent vs modifier vs ORCA

| Layer | Example on «грузотакси краснодар недорого» |
|-------|-------------------------------------------|
| **Modifiers** | GEO: краснодар; PRICE: недорого; SERVICE: *(implicit грузотакси)* |
| **Intent signals (MIG)** | `{ KS-INT-LOCAL, KS-INT-COMMERCIAL, KS-INT-COMPARISON }` |
| **ORCA (excluded)** | «Price-sensitive local commercial segment → bid strategy X» |

---

## Boundaries

### Layer rules (from charter — normative)

| Rule | Statement |
|------|-----------|
| **KS-01** | Domains / competitor entities → Market Surface, not Keyword Surface primary object |
| **KS-02** | Page phrase facts → Website Intelligence primary; Keyword Surface references with `page_visible` |
| **KS-03** | Executed query: Market Surface owns SERP outcome; Keyword Surface owns string as demand evidence |
| **KS-04** | Related search strings → Keyword Surface; result URLs → Market Surface |
| **KS-05** | Comparison matrix / landing observations unchanged — no keyword columns without charter |
| **KS-06** | Missing demand data **must not** be inferred from market recurrence or landing copy |

### Capability boundary matrix

| Concern | Keyword Surface | ORCA / excluded |
|---------|-----------------|-----------------|
| Modifier tags | Lexical token attachment | Segment labels, personas |
| Intent signals | Shape flag sets | Intent taxonomy, funnel, content type |
| Frequency | Raw provider numbers | Volume tier, priority, forecast |
| Phrase dedup | Normalization for identity | Semantic merge / clustering |
| Query expansion | **Forbidden** autonomously | May propose seeds to human for new session |

### Forbidden fields on future keyword objects

`cluster_id`, `priority`, `intent` (ORCA enum), `campaign`, `ad_group`, `recommended_bid`, `semantic_group`, `keyword_difficulty`, `search_volume_tier`.

---

## Non-goals

Explicit exclusions for this capability model and immediate Phase 2 follow-on until separately chartered:

| Non-goal | Rationale |
|----------|-----------|
| **SEO clustering / semantic core** | ORCA — not acquisition |
| **Campaign grouping / ad groups** | ORCA PPC structure |
| **ORCA semantic architecture** | Downstream interpretation layer |
| **Content planning / calendar** | MetaBOT / Factory / ORCA |
| **Autonomous intent interpretation** | Human + ORCA after handoff |
| **Search volume estimation** (derived) | MIG stores provider numbers only; no tiers |
| **Keyword difficulty** | Third-party SEO metric — excluded |
| **SERP strategy** | Ranking tactics, snippet optimization — ORCA |
| **Wordstat runtime / ingest** | Phase 2c+ gate |
| **External APIs** | Acquisition gate |
| **Schema / registry implementation** | Phase 2c design gate |
| **Phase 1 redesign** | MVP freeze honored |

---

## Reality review

### Question

Does this capability model appear **sufficient** to support a future Wordstat layer?

### Answer

**Yes — as a planning foundation, with explicit gaps.** The model defines **what** phrases, modifiers, intent shapes, and numeric slots MIG must understand before any Wordstat ingest is chartered. Keyword Intelligence v1 logical shapes (`wordstat_snapshot`, frequency_signal) **align** with KS-CAP-NUM-* capabilities.

### What the model covers for Wordstat

| Wordstat need | Covered by |
|---------------|------------|
| Phrase identity (exact string) | KS-CAP-PHR-* |
| Region / period attachment | Numeric capability context + manifest `scope.region` |
| Raw shows/clicks/share columns | KS-CAP-NUM-FREQ, SHARE, TREND |
| Honest absence | SAFE UNKNOWN per capability |
| No interpretation bleed | Non-goals + forbidden fields |

### What remains undefined (honest gaps)

| Gap | Impact | Suggested next gate |
|-----|--------|---------------------|
| **Extraction algorithm** for modifiers | Tags undefined operationally until manual pilot pass or rules doc | Operator manual tag pass on mqgt01 (charter step 4) |
| **JSON Schema** for modifier/intent attachments | Cannot validate in runtime | Phase 2c schema stub |
| **Dedup / normalization rules** beyond trim/lowercase | Phrase identity edge cases | Keyword Object design (Keyword Intelligence §5 — implementation gate) |
| **Cross-language / typo handling** | Pilot is Russian single-market | SAFE UNKNOWN for other locales |
| **Suggestion / Wordstat phrase alignment** | Unmapped export rows | Keyword Intelligence `unmapped_phrases` — ingest gate |
| **Brand/competitor token lists** | KS-MOD-BRAND/COMPETITOR need operator glossary | Atlas counterparty cross-walk (future) |
| **Validation by replay** | No keyword artifacts in MVP evidence | Cannot empirically test until capture chartered |
| **Generalization beyond Грузотакси Краснодар** | Taxonomy examples pilot-scoped | Additional markets — **UNKNOWN** |

### Confidence

| Area | Level | Basis |
|------|-------|-------|
| Capability completeness for planning | **B+** | Charter categories + task families covered |
| Modifier taxonomy fit for pilot | **B** | mqgt01 seeds classifiable; hypothetical rows marked |
| Intent model distinct from ORCA | **A-** | Explicit KS-INT-* + IS-* rules |
| Ready for Wordstat **implementation** | **N/A** | **Not authorized** — design only |

---

## Architecture decisions (capability model)

| ID | Decision | Rationale |
|----|----------|-----------|
| **KS-CM-01** | Capability ids use `KS-CAP-*` prefix | Traceability to Keyword Surface layer |
| **KS-CM-02** | Modifiers and intent signals **separate** | Prevents ORCA-style single intent class |
| **KS-CM-03** | Intent signals are **multi-flag sets** | Phrases span commercial + local + comparison |
| **KS-CM-04** | Numeric capabilities **named but not implemented** | Wordstat remains future gate |
| **KS-CM-05** | Pilot examples labeled; hypotheticals explicit | Reality-first discipline |
| **KS-CM-06** | Keyword Intelligence v1 remains **reference** for ingest | This doc owns **understanding**, not **fetch** |

---

## Recommended next step

1. **Human review** of modifier taxonomy against mqgt01 seed list — operator manual tag pass (no runtime).
2. **Phase 2c gate:** Schema stub for `modifier_tags[]`, `intent_shape_flags[]` on logical Keyword Object — no pack builder changes yet.
3. **Extend Research Pack contract** (design stub) — section ids from charter; populate rules unchanged.
4. **Wordstat readiness decision** — separate charter after manual export column one-pager (Keyword Intelligence §16).
5. **Stop condition:** If work shifts to clustering, volume tiers, or ORCA enums — stop and split per [boundaries.md](../boundaries.md).

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](../reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) | Phase 2a mission and layer stack |
| [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md) | Phase 1 evidence |
| [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) | Acquisition channel (future) |
| [boundaries.md](../boundaries.md) | MIG vs ORCA |
| [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) | Pack projections |

---

*MIG Keyword Surface Capability Model v1 · 2026-06-06 · normative capabilities only · no runtime*
