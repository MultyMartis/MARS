# MIG Keyword Surface Data Model v1

**Status:** **normative** — canonical data representation only (Phase 2c)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2c — Keyword Surface Data Model  
**Prior artifacts:** [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) · [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](../reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) · [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md)  
**Related (reference, not superseded):** [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md)  
**Validated market (examples):** Грузотакси / Краснодар / проект Триумф

**This document delivers:** canonical Keyword Surface objects, Keyword Object field model, provenance model, modifier storage model, intent signal storage model, numeric placeholder model, reality review.

**This document does not deliver:** runtime, JSON Schema, TypeScript types, acquisition adapters, Wordstat implementation, API integration, ORCA semantics, pack builder changes, or Phase 1 redesign.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This model defines **how demand-surface signals exist as data objects** — not how they are collected, stored on disk, or validated at runtime.

---

## Scope of this model

| In scope | Out of scope |
|----------|--------------|
| Canonical **Keyword Object** and related logical containers | Storage engine, file layout, registry writer |
| **Provenance** taxonomy and evidence discipline | Extraction algorithms, ingest adapters |
| **Modifier** attachment structure and normalization rules | Token matchers, NLP pipelines |
| **Intent shape** flag storage (multi-value, evidence, confidence) | ORCA intent taxonomy, funnel labels |
| **Numeric placeholder** slots (FREQ, TREND, SHARE) | Provider APIs, Wordstat UI, column mapping code |
| Alignment with `KS-CAP-*`, `KS-MOD-*`, `KS-INT-*` from Phase 2b | Schema registry files, verify scripts |

---

## Layer objects (overview)

Keyword Surface data consists of **four logical object kinds**. Only **Keyword Object** is canonical per phrase; the others are supporting structures.

| Object kind | Role | Cardinality per session |
|-------------|------|-------------------------|
| **Keyword Object** | Canonical record of one observable phrase + attached signals | 0..N |
| **Provenance Record** | Embedded or referenced evidence of where a phrase came from | 1..N per Keyword Object |
| **Modifier Attachment** | Lexical modifier tag with optional span evidence | 0..N per Keyword Object |
| **Numeric Signal Slot** | Placeholder for provider numeric columns | 0..3 types per Keyword Object |

**Normative container (future, logical only):** `keyword_registry` indexes Keyword Objects for a session. Rollup views (`keyword_surface`, pack projections) are **derivable** — registry wins on conflict per Keyword Intelligence v1 §6.4.

---

## Canonical Keyword Object

### Purpose

The **Keyword Object** is the single canonical representation of one **observable query-language string** at capture time, with provenance, optional modifiers, intent shape flags, numeric placeholders, and explicit unknowns.

One Keyword Object = **one phrase identity** within a session scope. Same human-readable string from **different provenance channels** may be **separate objects** or **merged** per dedup rules (§KO-DEDUP) — merge is a future implementation choice; the model allows both representations via `provenance_records[]`.

### Normative fields

| Field | Required | Meaning |
|-------|----------|---------|
| **keyword_id** | **Yes** | Stable identifier within session scope. Opaque to consumers; assigned at registry write time. **Not** a semantic hash of business meaning. |
| **phrase** | **Yes** | Exact captured string — display form. Trim outer whitespace only; preserve internal spacing, casing, and script as captured. |
| **phrase_normalized** | **Optional** | Normalized form for dedup identity only (see §KO-NORM). **Never** used for display or pack prose. |
| **session_id** | **Yes** | Owning research session. |
| **source_type** | **Yes** | Primary provenance channel — see §Provenance Model (`KS-PROV-*`). One **primary** channel per object; additional channels via `provenance_records[]`. |
| **provenance_records[]** | **Yes** | Ordered list of Provenance Records — minimum one entry matching `source_type`. |
| **region_scope** | **Optional** | Demand geography context for this object — region code, label, or explicit `unknown`. Aligns with session `scope.region` when applicable. |
| **period_scope** | **Optional** | Time window for numeric signals — e.g. month, week, custom export range, or `not_applicable` for non-Wordstat channels. |
| **locale** | **Optional** | BCP-47 when known (suggestion capture, SERP engine context). |
| **engine** | **Optional** | Search engine tag when channel-specific — `yandex`, `google`, or `unknown`. Null when not engine-bound (operator seed, Wordstat row without engine). |
| **modifier_tags[]** | **Yes** | Array of Modifier Attachments — may be empty `[]`. Empty means **no modifiers tagged**, not «modifiers unknown» (see §Modifier SAFE UNKNOWN). |
| **intent_shape_flags[]** | **Yes** | Array of Intent Shape Attachments — may include `KS-INT-UNKNOWN`. Empty array is **forbidden** — use explicit UNKNOWN flag instead. |
| **numeric_slots** | **Optional** | Container for FREQ / TREND / SHARE placeholders — absent or partially populated; see §Numeric Placeholder Model. |
| **evidence_refs[]** | **Yes** | Pointers to upstream artifacts (manifest, SERP, snapshot files). Minimum one ref when object is not purely operator-declared without artifact. |
| **evidence_grade** | **Yes** | Trust at capture: `operator` \| `provider` \| `extracted`. |
| **safe_unknown[]** | **Yes** | Explicit unknown declarations — may be empty `[]`. Session- or object-level gaps **must** appear here, not as silent nulls. |
| **capture_time** | **Yes** | ISO-8601 UTC — when this object was last materially updated in the registry. |
| **capability_refs[]** | **Optional** | Traceability to `KS-CAP-*` ids that this object satisfies — planning aid only. |

### Forbidden fields (normative)

These **must not** appear on Keyword Objects — ORCA and strategy layers own them:

`cluster_id`, `priority`, `intent` (ORCA enum), `campaign`, `ad_group`, `recommended_bid`, `semantic_group`, `keyword_difficulty`, `search_volume_tier`, `head_tail_class`, `theme`, `segment_label`.

### Identity and dedup rules

| Rule id | Statement |
|---------|-----------|
| **KO-01** | **keyword_id** is immutable once assigned within a session revision. |
| **KO-02** | **phrase** is the human-visible truth; **phrase_normalized** is dedup aid only. |
| **KO-03** | Same normalized phrase + same **primary** `source_type` + same **engine** (when applicable) → **one** Keyword Object; merge `provenance_records[]` and `evidence_refs[]`. |
| **KO-04** | Same phrase from **different** primary `source_type` (e.g. seed vs suggestion) → **separate** Keyword Objects unless operator explicitly merges with `evidence_grade: operator`. |
| **KO-05** | Wordstat row for phrase X and suggestion string X → **separate** objects linked by shared `phrase_normalized`, not forced merge. |
| **KO-06** | `page_visible` phrases **must** remain distinct from `executed_query` even when strings match — KS-02. |

### Normalization rules (identity only)

| Rule id | Statement |
|---------|-----------|
| **KO-NORM-01** | Trim leading/trailing whitespace on **phrase**. |
| **KO-NORM-02** | **phrase_normalized** = lowercase + Unicode NFC + collapse internal runs of whitespace to single space. |
| **KO-NORM-03** | No stemming, no synonym merge, no transliteration in v1 model. |
| **KO-NORM-04** | Punctuation preserved in **phrase**; normalization does not strip «?» or quotes. |
| **KO-NORM-05** | Cross-language and typo variants → **separate** identities unless operator merge — **SAFE UNKNOWN** for equivalence. |

### Illustrative object (conceptual — not schema)

```text
Keyword Object {
  keyword_id:           "kw-mqgt01-00007"
  phrase:               "грузотакси Краснодар"
  phrase_normalized:    "грузотакси краснодар"
  session_id:           "mig-20260605-mqgt01"
  source_type:          KS-PROV-OPERATOR-SEED
  provenance_records:   [ { ... seed from research request ... } ]
  region_scope:         { value: "Краснодар", code: null, status: "declared" }
  period_scope:         { status: "not_applicable" }
  locale:               "ru-RU"
  engine:               null
  modifier_tags:        [ GEO: "краснодар" ]
  intent_shape_flags:   [ KS-INT-LOCAL, KS-INT-COMMERCIAL ]
  numeric_slots:        { freq: { status: "not_captured" }, trend: ..., share: ... }
  evidence_refs:        [ manifest Query Set, research request ]
  evidence_grade:       operator
  safe_unknown:         [ "Frequency evidence not captured for this session" ]
  capture_time:         "2026-06-05T..."
}
```

---

## Provenance Model

### Purpose

Answer: **Where did this phrase come from?** Provenance is **channel + evidence**, not interpretation. Every Keyword Object **must** carry enough provenance to replay «what was observed» without inferring demand strength.

### Provenance channel enum (`KS-PROV-*`)

Maps to Phase 2b phrase capabilities (`KS-CAP-PHR-*`).

| Provenance id | Capability | Meaning | Primary `source_type` value |
|---------------|------------|---------|----------------------------|
| **KS-PROV-OPERATOR-SEED** | KS-CAP-PHR-SEED | Declared in Research Request before/at session bind | `operator_seed` |
| **KS-PROV-EXECUTED-QUERY** | KS-CAP-PHR-EXEC | String actually submitted to SERP acquisition | `executed_query` |
| **KS-PROV-SEARCH-SUGGESTION** | KS-CAP-PHR-SUGGEST | Autocomplete / suggestion list string | `search_suggestion` |
| **KS-PROV-RELATED-SEARCH** | KS-CAP-PHR-RELATED | SERP-visible related / «people also search» string | `related_search` |
| **KS-PROV-PAGE-VISIBLE** | KS-CAP-PHR-PAGE | Phrase visible on acquired page (title, H1, meta) | `page_visible` |
| **KS-PROV-OPERATOR-INPUT** | KS-CAP-PHR-OPERATOR | Operator-added outside automated capture | `operator_input` |
| **KS-PROV-FUTURE-WORDSTAT** | *(numeric row anchor)* | Phrase row from Wordstat export or API — **not implemented** | `future_wordstat` |
| **KS-PROV-FUTURE-PROVIDER** | *(generic)* | Third-party numeric or phrase provider — **charter only** | `future_provider` |

**Normative:** `future_*` values are **valid in the model** but **must** carry `safe_unknown` until acquisition is chartered. They exist so Wordstat rows do not require object redesign.

### Provenance Record structure (conceptual)

Each entry in `provenance_records[]`:

| Field | Required | Meaning |
|-------|----------|---------|
| **provenance_id** | **Yes** | `KS-PROV-*` channel id |
| **capture_time** | **Yes** | When this channel observation occurred |
| **host_context** | **Optional** | Parent context — e.g. seed query for suggestion, SERP query for related search, page URL for page_visible |
| **ordinal** | **Optional** | Rank in list (suggestion rank, related-search position) when observable |
| **import_method** | **Optional** | `manual_paste`, `api`, `extracted`, `declared` — method label only |
| **evidence_refs[]** | **Yes** | Artifact pointers supporting this provenance claim |
| **evidence_grade** | **Yes** | Per-record grade when it differs from object default |
| **safe_unknown[]** | **Yes** | Channel-specific unknowns |

### Evidence discipline

| Rule id | Statement |
|---------|-----------|
| **PR-01** | Every non-operator-only object **must** have ≥1 **evidence_refs[]** entry traceable to session artifacts. |
| **PR-02** | Provenance **must not** be inferred from SERP position, ad presence, or competitor count. |
| **PR-03** | `page_visible` **must** reference Website Intelligence snapshot ref — Keyword Surface does not re-fetch HTTP. |
| **PR-04** | `executed_query` **must** reference manifest or SERP metadata — Market Surface owns SERP **outcome**, not query string ownership. |
| **PR-05** | `search_suggestion` without snapshot artifact → `evidence_grade: operator` + SAFE UNKNOWN «suggestion surface not captured». |
| **PR-06** | `future_wordstat` rows **must** reference future `wordstat_snapshot` logical artifact — until then, object may exist with phrase only and numeric slots `not_captured`. |
| **PR-07** | Multiple provenance records on one object **allowed** when same phrase reappears on another channel without dedup merge (e.g. seed later executed). |

### Boundaries

| Concern | Keyword Surface provenance | Other layer |
|---------|---------------------------|-------------|
| Query string as demand evidence | **Owns** | — |
| SERP URLs, positions, domains | References only | Market Surface **owns** |
| Page HTML facts | References snapshot | Website Intelligence **owns** |
| Wordstat column semantics | Stores raw attachment | Interpretation → ORCA |
| Operator strategy notes | **Forbidden** on Keyword Object | ORCA / HITL outside registry |

### SAFE UNKNOWN (provenance)

| Situation | Declaration |
|-----------|-------------|
| Seed declared but never executed | «Query X in seed list was not executed — SERP outcome for X unknown» |
| Suggestion pass not run | «Autocomplete suggestion surface not captured for this session» |
| Related block absent | «SERP related-search block not present or not extracted» |
| Wordstat not ingested | «Frequency evidence not captured for this session» |
| Page phrase channel not indexed | «Page-visible phrase channel not indexed — competitor lexicon on pages unknown» |

---

## Modifier Storage Model

### Purpose

Modifiers are **lexical observations** attached to a host phrase — not intent classes, not segments. Storage model defines **how** `KS-MOD-*` tags exist on Keyword Objects without fixing extraction logic.

### Modifier Attachment structure

Each entry in `modifier_tags[]`:

| Field | Required | Meaning |
|-------|----------|---------|
| **modifier_type** | **Yes** | `KS-MOD-*` taxonomy id |
| **matched_text** | **Optional** | Exact token or span as observed in **phrase** — omit when operator tags type without span |
| **span_hint** | **Optional** | Character offset range or token index — implementation-deferred; may be `unknown` |
| **evidence_basis** | **Yes** | `lexical_match` \| `operator_declared` \| `cross_layer_ref` |
| **provenance_id** | **Optional** | Which `provenance_records[]` entry this tag applies to — required when tag applies to `page_visible` only |
| **evidence_refs[]** | **Optional** | Supporting refs when tag derived from external glossary |
| **safe_unknown[]** | **Yes** | Tag-level unknowns — usually empty |

### Modifier taxonomy (storage ids)

| modifier_type | Token class | Example on pilot phrases |
|---------------|-------------|--------------------------|
| **KS-MOD-GEO** | Place names, directional geo | краснодар, по краснодару |
| **KS-MOD-SERVICE** | Service, vehicle, cargo, crew | газель, с грузчиками, перевозка мебели |
| **KS-MOD-COMMERCIAL** | Transaction / order path | заказать, вызов, тариф |
| **KS-MOD-PRICE** | Price / cost framing | недорого, цены, стоимость |
| **KS-MOD-URGENCY** | Time pressure | срочно, быстро, сегодня |
| **KS-MOD-QUESTION** | Interrogative shape | сколько, как, где |
| **KS-MOD-BRAND** | Brand / franchise in query | *(operator glossary dependent)* |
| **KS-MOD-COMPETITOR** | Competitor name in query text | *(operator glossary dependent)* |

### Normalization rules

| Rule id | Statement |
|---------|-----------|
| **MOD-01** | Modifiers are **multi-label** — zero to many tags per Keyword Object. |
| **MOD-02** | Overlapping types on same span **allowed** (PRICE + COMMERCIAL on «недорого») — **do not merge** for convenience. |
| **MOD-03** | **matched_text** stored as captured — no lemmatization in storage model. |
| **MOD-04** | Same modifier_type may appear **once per distinct matched_text**; duplicate identical entries forbidden. |
| **MOD-05** | Tags on `page_visible` objects **must** set `provenance_id` to page channel — MT-04 from capability model. |
| **MOD-06** | BRAND and COMPETITOR tags **require** operator glossary or explicit `safe_unknown: "Brand token list not declared"`. |
| **MOD-07** | LOCATION proximity tokens («рядом») → **KS-SIG-LOCATION** signal surface, **not** KS-MOD-GEO — do not store as GEO modifier. |

### SAFE UNKNOWN (modifiers)

| Situation | Storage behavior |
|-----------|------------------|
| Extraction not run | `modifier_tags: []` **plus** object-level `safe_unknown: ["Modifier surface not derived — lexical modifiers unknown"]` |
| Extraction run, no tags found | `modifier_tags: []` **without** modifier unknown — absence is explicit «no tags applied» |
| Partial pass (operator manual) | Tags present + `safe_unknown` listing untagged modifier **families** not reviewed |
| Brand/competitor glossary missing | Omit BRAND/COMPETITOR tags; declare glossary unknown |

**Critical distinction:** Empty `modifier_tags[]` means two different things depending on **safe_unknown** presence — never overload empty array alone.

---

## Intent Signal Storage

### Purpose

Store Phase 2b **intent shape flags** (`KS-INT-*`) as evidence-derived attachments — not ORCA intent, not a single exclusive class.

### Intent Shape Attachment structure

Each entry in `intent_shape_flags[]`:

| Field | Required | Meaning |
|-------|----------|---------|
| **signal_id** | **Yes** | `KS-INT-*` enum value |
| **confidence** | **Optional** | `declared` \| `derived` \| `operator` — **not** numeric probability |
| **evidence_basis[]** | **Yes** | List of bases: `modifier:KS-MOD-*`, `lexical_pattern`, `operator`, `none` |
| **evidence_refs[]** | **Optional** | When operator or external worksheet supports flag |
| **safe_unknown[]** | **Yes** | Per-flag unknowns — usually empty |

### Intent signal enum (storage)

| signal_id | Meaning (evidence-only) |
|-----------|-------------------------|
| **KS-INT-COMMERCIAL** | Transactional or hire wording present |
| **KS-INT-LOCAL** | Named geo or local scoping present |
| **KS-INT-QUESTION** | Interrogative form |
| **KS-INT-INFORMATIONAL** | Explain / learn shape (non-question) |
| **KS-INT-COMPARISON** | Compare, price-check, reviews shape |
| **KS-INT-SUPPORT** | Help / problem / contact shape |
| **KS-INT-UNKNOWN** | Insufficient evidence for other shapes |

### Single value vs multi-value

| Question | Answer |
|----------|--------|
| **Single exclusive intent class?** | **No.** Forbidden. |
| **Multi-value flag set?** | **Yes.** Normative — `intent_shape_flags[]` is a **set**, not a scalar. |
| **Can COMMERCIAL + LOCAL + COMPARISON co-exist?** | **Yes** — e.g. «грузотакси краснодар недорого». |
| **Must UNKNOWN appear?** | **Yes**, when no other signal is evidenced (IS-04). |
| **Can UNKNOWN co-exist with others?** | **No** — if any non-UNKNOWN flag is evidenced, omit UNKNOWN. |

### Confidence model (planning)

**No numeric confidence scores in v1 model.** Allowed values:

| confidence | Meaning |
|------------|---------|
| **declared** | Rule-derived from modifiers / lexical patterns (future extraction) |
| **operator** | Human tagged in manual pass |
| **derived** | Composite derivation documented in `evidence_basis[]` |

**Forbidden:** `0.0–1.0` floats, «likely commercial», ML class probabilities.

### Evidence requirements

| Rule id | Statement |
|---------|-----------|
| **IS-01** | Every non-UNKNOWN flag **must** list ≥1 entry in `evidence_basis[]`. |
| **IS-02** | **KS-INT-LOCAL** requires GEO modifier or explicit place token in **phrase** — not `region_scope` alone. |
| **IS-03** | **KS-INT-QUESTION** requires QUESTION modifier or «?» in **phrase**. |
| **IS-04** | SERP position, ad presence, competitor count **must not** appear in `evidence_basis[]`. |
| **IS-05** | Field name in future artifacts: `intent_shape_flags[]` — **never** `intent:` ORCA enums. |
| **IS-06** | Intent storage **independent** from modifier storage — flags may duplicate modifier implications; do not collapse layers. |

### Intent vs modifier (storage example)

Phrase: «заказать газель краснодар»

| Layer | Stored as |
|-------|-----------|
| Modifiers | KS-MOD-GEO, KS-MOD-SERVICE, KS-MOD-COMMERCIAL |
| Intent flags | KS-INT-LOCAL, KS-INT-COMMERCIAL |
| ORCA (excluded) | *(no field)* |

---

## Numeric Placeholder Model

### Purpose

Reserve structured slots for future provider numbers (Wordstat, other exports) **without** provider assumptions, unit conversion, or volume interpretation.

### Container: `numeric_slots`

Logical grouping on Keyword Object — **optional** entire container; individual slots may be populated independently.

### Slot types (`KS-NUM-*`)

| Slot key | Capability | Typical provider columns (illustrative only) |
|----------|------------|-----------------------------------------------|
| **freq** | KS-CAP-NUM-FREQ | shows, query count, impressions |
| **trend** | KS-CAP-NUM-TREND | period-over-period delta, seasonality series |
| **share** | KS-CAP-NUM-SHARE | shows_share, click share, ratio columns |

### Slot structure (conceptual)

Each slot (freq, trend, share) shares the same **status-first** shape:

| Field | Required | Meaning |
|-------|----------|---------|
| **status** | **Yes** | `known` \| `unknown` \| `not_captured` \| `provider_conflict` |
| **value** | When status=`known` | Raw number or string **exactly as returned** — no unit conversion |
| **raw_columns** | **Optional** | Unmapped export columns preserved verbatim |
| **period** | **Optional** | Window label from provider |
| **as_of** | **Optional** | Provider timestamp for this value |
| **provider_ref** | **Optional** | Opaque handle — export file, API request id |
| **evidence_refs[]** | When status=`known` | Pointer to snapshot row |
| **safe_unknown[]** | **Yes** | Column semantics doubts, missing denominator, etc. |

### Status semantics

| status | Meaning | Example |
|--------|---------|---------|
| **known** | Provider supplied a value stored in **value** | shows=12400 in export row |
| **unknown** | Provider column existed but cell empty or unreadable | blank cell |
| **not_captured** | No provider pass for this session/channel | MVP default for all slots |
| **provider_conflict** | Two sources disagree; both preserved in conflict detail | manual re-import with different shows |

### Provider conflict handling (conceptual)

When `status: provider_conflict`:

| Field | Meaning |
|-------|---------|
| **conflict_values[]** | Array of `{ value, provider_ref, capture_time }` — no winner picked |
| **safe_unknown[]** | Must include «Numeric provider conflict — operator verification required» |

**Normative:** MIG **must not** average, max, or «prefer latest» without operator evidence_grade override.

### Rules

| Rule id | Statement |
|---------|-----------|
| **NUM-01** | Absent `numeric_slots` container ≡ all slots `not_captured`. |
| **NUM-02** | **Never** infer freq from SERP recurrence or landing prominence. |
| **NUM-03** | Missing Wordstat ≠ zero — use `not_captured` or `unknown`, never `0` as default. |
| **NUM-04** | Store all export columns in **raw_columns** when mapping uncertain. |
| **NUM-05** | No derived metrics (CTR, opportunity score, tiers) in Keyword Object. |
| **NUM-06** | `region_scope` / `period_scope` on object **must** align with numeric slot context or declare mismatch in **safe_unknown**. |

### Illustrative states (pilot — no Wordstat)

| Phrase source | freq.status | trend.status | share.status |
|---------------|-------------|--------------|--------------|
| operator_seed (MVP) | not_captured | not_captured | not_captured |
| future_wordstat row | known | unknown | not_captured |

---

## Cross-object relationships (logical)

```text
Research Request ──seed──► Keyword Object (KS-PROV-OPERATOR-SEED)
Session manifest ──executed──► Keyword Object (KS-PROV-EXECUTED-QUERY)
suggestions_snapshot ──► Keyword Object (KS-PROV-SEARCH-SUGGESTION)
serp_result ──related block──► Keyword Object (KS-PROV-RELATED-SEARCH)
website_snapshot ──title/H1──► Keyword Object (KS-PROV-PAGE-VISIBLE)
wordstat_snapshot ──row──► Keyword Object (KS-PROV-FUTURE-WORDSTAT) + numeric_slots
```

**Linking, not embedding:** Keyword Objects reference upstream artifacts via `evidence_refs[]`; they do not duplicate SERP or page SoT.

---

## Architecture decisions (data model)

| ID | Decision | Rationale |
|----|----------|-----------|
| **KS-DM-01** | Keyword Object is **canonical** per phrase identity | Single registry truth |
| **KS-DM-02** | Provenance uses `KS-PROV-*` including `future_*` | Wordstat-ready without redesign |
| **KS-DM-03** | Modifiers and intent flags **separate arrays** | Prevents ORCA-style collapse |
| **KS-DM-04** | Intent is **multi-flag set** with explicit UNKNOWN | IS-01 from capability model |
| **KS-DM-05** | Numeric slots are **status-first placeholders** | Honest absence + conflict |
| **KS-DM-06** | Empty modifier array ≠ unknown without **safe_unknown** | MOD discipline |
| **KS-DM-07** | Keyword Intelligence v1 §5 **reference** — this doc owns Phase 2 surface extensions | Traceability |

---

## Reality Review

### Question

Would this model support **Wordstat**, **Search Suggestions**, **Related Searches**, and **Manual Operator Input** without redesign?

### Answer

**Yes — for data representation.** The model explicitly reserves provenance channels, evidence refs, and numeric slots for all four inputs. **Implementation** (adapters, snapshots, registry writer) remains unbuilt and unauthorized.

### Source-by-source assessment

| Source | Supported without redesign? | Mechanism | Honest gaps |
|--------|----------------------------|-----------|-------------|
| **Manual Operator Input** | **Yes** | `KS-PROV-OPERATOR-SEED`, `KS-PROV-OPERATOR-INPUT`; `evidence_grade: operator` | Dedup vs automated channels needs operator merge policy at implementation |
| **Search Suggestions** | **Yes** | `KS-PROV-SEARCH-SUGGESTION`; `host_context` seed; optional `ordinal` rank | No recursive expansion in model — by design (KI-03) |
| **Related Searches** | **Yes** | `KS-PROV-RELATED-SEARCH`; SERP artifact refs | MVP did not extract block — object shape still valid with SAFE UNKNOWN |
| **Wordstat** | **Yes** | `KS-PROV-FUTURE-WORDSTAT`; `numeric_slots.freq/trend/share`; `period_scope`, `region_scope` | Column mapping, multi-row history, API vs export — implementation gates, not model gaps |

### What would **not** fit without model amendment

| Need | Current model | Amendment required? |
|------|---------------|---------------------|
| ORCA intent enum on object | Forbidden | **No amendment** — use ORCA layer |
| Semantic cluster id | Forbidden | **No amendment** — ORCA |
| Single scalar «primary intent» | Forbidden | **No amendment** — by design |
| Time-series array &gt;2 points in one slot | Not defined | **Possible Phase 2d** extension to `trend` slot — array of observations |
| Cross-session phrase identity | Session-scoped **keyword_id** | **Future** catalog layer — out of Phase 2c scope |

### Confidence

| Area | Level | Basis |
|------|-------|-------|
| Canonical object completeness | **B+** | Fields cover Phase 2b capabilities |
| Provenance coverage | **A-** | All charter channels + future Wordstat |
| Modifier / intent storage | **B+** | Aligns with KS-MOD-* / KS-INT-*; extraction still undefined |
| Numeric placeholder sufficiency | **B** | Status model handles absence and conflict; rich time-series deferred |
| Ready for runtime implementation | **N/A** | **Not authorized** — design only |

---

## Recommended Next Step

1. **Human review** of Keyword Object fields against mqgt01 manifest seeds — tabletop mapping exercise (no runtime).
2. **Phase 2d gate (optional):** Logical registry container sketch (`keyword_registry` index fields only) — still no JSON Schema.
3. **Operator manual tag pass** on pilot query set — validate modifier and intent storage against real phrases.
4. **Research Pack contract stub** — projection field names from this model (`intent_shape_flags`, `modifier_tags`, numeric status summaries).
5. **Wordstat readiness decision** — separate charter; this model does not authorize ingest.
6. **Stop condition:** If work shifts to schema files, pack builder, or ORCA enums — stop and split per [boundaries.md](../boundaries.md).

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) | Phase 2b — what MIG should understand |
| [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](../reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) | Phase 2a mission and layers |
| [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) | Acquisition channel (future) — §5 Keyword Object reference |
| [boundaries.md](../boundaries.md) | MIG vs ORCA |
| [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md) | Phase 1 evidence |

---

*MIG Keyword Surface Data Model v1 · 2026-06-06 · canonical representation only · no runtime*
