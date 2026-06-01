# MIG Deep Research Architecture v1

**Status:** **documented** — architecture contract (Phase 4 design).  
**Not:** implementation, JSON Schema registry, OpenRouter setup, model selection, API keys, prompt templates as code, ORCA methodology, Website Factory generation, or runtime product.

**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md); Research Session; [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md); [mig-multi-query-discovery-design-v0.md](mig-multi-query-discovery-design-v0.md); [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md); [mig-landing-analysis-architecture-v1.md](mig-landing-analysis-architecture-v1.md); [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md).  
**Downstream:** [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) (projected sections — §8); [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md).  
**Consumers (future, by reference only):** MIG Worker (deep research pass), session spine, operator HITL UX, ORCA, future MARS runtime observers.

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

---

## 1. Deep Research — definition and boundaries

### 1.1 What Deep Research is

**Deep Research** is the MIG **synthesis channel** (R1 Phase 4) that **aggregates evidence already captured** in session artifacts into **structured, citation-backed research findings** — cross-page and cross-competitor **patterns**, **recurrences**, and **explicit unknowns** — without adding net-new groundtruth from the open web or crossing into strategic interpretation.

Deep Research answers questions of the form:

- «What **recurring structures** appear across captured competitors?»
- «What **offer / CTA / trust / website patterns** repeat in the evidence?»
- «What **market-structure observations** are supported by SERP + competitor + landing artifacts?»
- «What remains **unknown** despite synthesis?»

Deep Research **preserves MIG boundaries**: findings are **observations over evidence**, not recommendations.

```text
Research Request
    ↓
Search Acquisition (SERP)
    ↓
Competitor Discovery
    ↓
Website Acquisition
    ↓
Landing Analysis
    ↓
[Keyword Intelligence]  (optional parallel / upstream enrich)
    ↓
Deep Research           ← this contract
    ↓
Research Pack (projection + human review)
    ↓
ORCA (R2)
```

### 1.2 What Deep Research is not

| Anti-pattern | Owner / phase |
|--------------|----------------|
| New SERP fetch, new URL crawl, open-web browse (default) | **Acquisition channels** — not Deep Research |
| Per-page block/offer/CTA extraction | **Landing Analysis** — upstream SoT |
| Competitor discovery rules, entity typing | **Competitor Discovery** — upstream SoT |
| Keyword capture, Wordstat tables, suggestion APIs | **Keyword Intelligence** — parallel SoT |
| Strategy, positioning, prioritization, scoring, ranking | **ORCA** — forbidden in MIG |
| PPC / SEO plans, campaign structure, semantic clusters | **ORCA** |
| Website Factory blueprints, content packs, LRL | **ORCA → Factory** |
| «Best competitor», market opportunity score, TAM | **ORCA** |
| Business-value interpretation («high-intent niche») | **ORCA** |
| Replacing artifact SoT with narrative-only memo | **Forbidden** — artifacts remain SoT |

### 1.3 Relationship map

| Neighbor | Relationship |
|----------|----------------|
| **Landing Analysis** | **Upstream producer** — supplies per-landing structured observations (`landing_observations.json`, `landings/*`). Deep Research **reads**; does **not** re-extract DOM. May **summarize recurrence** across landings. |
| **Website Acquisition** | **Upstream producer** — `website_snapshots.json`, per-snapshot facts. Deep Research cites snapshots; does **not** re-fetch. |
| **Competitor Discovery** | **Upstream producer** — `competitors.json` entity set and discovery audit. Deep Research may describe **presence patterns**; must **not** rank competitors. |
| **Keyword Intelligence** | **Optional upstream** — phrase/surface artifacts. Deep Research may note **recurring lexicon in evidence**; must **not** build semantic core or intent clusters. |
| **Research Pack** | **Downstream projection** — new pack sections are **views** of `research_findings.json`. Pack markdown is human-readable; **not** SoT. |
| **ORCA** | **Consumer** after human approval — interprets findings; must **not** treat findings as strategy or scores. |
| **Website Factory** | **No direct consumption** — Factory path remains MIG → ORCA → strategy → Factory. |
| **Research Request** | **Scope anchor** — niche, region, seeds, `request_type`, capture profile gate whether Deep Research runs. |

**Normative:** Deep Research **extends** the same Research Pack object (`mig_phase: 4`); it does **not** introduce a separate «Deep Research Pack» product type (per Research Pack contract Phase 4 note).

---

## 2. Research inputs

### 2.1 Input evaluation matrix

| Artifact / source | Role | MVP required | Phase 2+ | Deep Research use |
|-------------------|------|--------------|----------|-------------------|
| **Research Request** (accepted, session-bound) | Scope gate | **Yes** | **Yes** | Niche, region, seeds, `request_type`, `capture_profile`, operator notes — **no** semantic clusters in request |
| **`session_manifest.json`** | Session index | **Yes** | **Yes** | Artifact registry, phase flags, manifest `safe_unknown[]` |
| **`serp_result.json`** | SERP SoT | **Yes** | **Yes** | Market structure on SERP, ads/organic/local patterns, query surface |
| **`competitors.json`** | Competitor SoT | **Yes** | **Yes** | Entity set, discovery reasons, domains — **not** for ranking |
| **`website_snapshots.json`** + `snapshots/sites/*` | Page capture SoT | **Conditional** | **Yes** | Required when website pass ran; cite `snapshot_id` |
| **`landing_observations.json`** + `landings/*` | Landing SoT | **Conditional** | **Yes** | Required when landing pass ran; primary cross-competitor pattern source |
| **`serp_index.json`** / multi-query bundle | Multi-query SoT | **No** | **Yes** | Cross-query recurrence when multi-query discovery executed |
| **`keyword_registry.json`** | Keyword SoT | **No** | **O** | Recurring phrases **as observed in registry/SERP** — no clustering |
| **`wordstat_snapshot.json`** | Demand capture | **No** | **O** | Frequency tables as **cited numbers only** — no «target these» |
| **`suggestions_snapshot.json`** | Suggestion capture | **No** | **O** | Surface recurrence — no expansion automation |
| **Operator manual annotations** | Human evidence | **O** | **O** | Grade **A** when operator-attested; must be listed in `evidence_refs` |
| **ORCA prior outputs** | — | **Forbidden** | **Forbidden** | R2 must not write back into Deep Research pass |

### 2.2 Canonical input bundle (normative)

**Deep Research pass** MUST declare `upstream_artifacts` with resolved paths. Minimum MVP bundle when phase allows:

```json
{
  "research_request_ref": "session-bound copy or request_id pointer",
  "session_manifest": "session_manifest.json",
  "serp": "serp_result.json",
  "competitors": "competitors.json",
  "website_snapshots": "website_snapshots.json | null",
  "landing_observations": "landing_observations.json | null",
  "keyword_registry": null,
  "serp_index": null
}
```

**Gate rules:**

1. Deep Research **must not** run if `serp_result.json` or `competitors.json` is missing — fail closed with session-level SAFE UNKNOWN.
2. If `request_type` / `capture_profile` excludes website or landing passes, Deep Research operates on **SERP + competitor (+ keyword if present)** only; landing-derived finding categories **must** emit SAFE UNKNOWN entries, not fabricated cross-landing patterns.
3. LLM input boundary (MVP): **excerpts and structured slices** from the above files only — **no** default open-web retrieval.

### 2.3 Research Request fields consumed

| Field | Use |
|-------|-----|
| `scope.*` | Bound synthesis to declared niche/region/device |
| `queries.seed_queries[]`, executed queries | Anchor «market language» findings to declared search surface |
| `request_type` | Gate depth (e.g. `serp_capture` vs future `deep_research`) |
| `capture_profile` | Determines which upstream artifacts are in-bounds |
| `signals[]` | Operator hints — **not** evidence; may appear in `analysis_notes` only |

**Forbidden from Request:** pre-built clusters, `downstream_context` with strategy, competitor priority lists.

---

## 3. Research Finding Model

### 3.1 Design principles

1. **Finding = declarative observation + evidence pointers** — never an imperative recommendation.
2. **No recommendation fields** — no `priority`, `score`, `recommended_action`, `should`, `best`, `opportunity_rating`.
3. **Stable ids** — reproducible within session for pack cross-refs and ORCA citation.
4. **Worst-grade inheritance** — finding `evidence_grade` = worst grade among cited refs (Research Pack §4 pessimistic rule).
5. **SAFE UNKNOWN** is a first-class finding category — not a failure mode only.

### 3.2 Session envelope: `research_findings.json` (canonical SoT)

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `schema_version` | **Yes** | string | `"1.0"` for this contract |
| `session_id` | **Yes** | string | Owning session |
| `generated_at` | **Yes** | ISO-8601 UTC | Pass completion |
| `synthesis_phase` | **Yes** | string | `"deep_research_v1"` |
| `upstream_artifacts` | **Yes** | object | Resolved paths (§2.2) |
| `findings` | **Yes** | array | Finding objects (§3.3) |
| `cross_competitor_summary` | **O** | object | **Counts only** — e.g. `competitors_with_trust_pattern: 3` — no ranking |
| `session_coverage` | **Yes** | enum | `complete` \| `partial` \| `minimal` \| `unknown` |
| `section_evidence_grade` | **Yes** | A–X | Worst grade among findings |
| `safe_unknown` | **Yes** | string[] | Session-level gaps (mirrors finding category) |
| `synthesis_metadata` | **O** | object | Pass id, operator, `human_reviewed: false` until review |

### 3.3 Finding object (canonical)

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `finding_id` | **Yes** | string | `{session_id}-rf{seq}` e.g. `mig-20260601-a1b2c3-rf001` |
| `finding_type` | **Yes** | enum | Category id — §4 |
| `finding_text` | **Yes** | string | Single declarative sentence — observable, past/present tense |
| `finding_scope` | **Yes** | enum | `session` \| `query` \| `competitor` \| `cross_competitor` \| `landing` |
| `scope_refs` | **O** | object | `{ query_id?, competitor_id?, landing_id?, domain? }` |
| `pattern_key` | **O** | string | Stable machine key for recurrence (e.g. `cta_phone_prominent`) — **not** a score |
| `recurrence` | **O** | object | `{ observed_count, eligible_count, competitor_ids[] }` — descriptive counts only |
| `evidence_refs` | **Yes** | array | §3.4 — min 1 for non-`safe_unknown` findings |
| `source_artifacts` | **Yes** | string[] | Logical artifact names e.g. `landing_observations.json` |
| `coverage` | **Yes** | enum | `complete` \| `partial` \| `minimal` \| `unknown` — per Research Pack §4.5 |
| `confidence_class` | **Yes** | enum | §3.5 — **not** numeric probability |
| `evidence_grade` | **Yes** | A–X | Worst cited ref grade |
| `safe_unknown` | **O** | boolean | `true` when finding explicitly registers a gap |
| `contradiction_flag` | **O** | boolean | Evidence sources disagree — describe in `finding_text` |
| `forbidden_if_present` | — | — | **Must not exist:** `priority`, `score`, `rank`, `recommendation`, `action`, `strategy_hint` |

**Example (valid):**

```json
{
  "finding_id": "mig-20260601-a1b2c3-rf003",
  "finding_type": "cta_patterns",
  "finding_text": "Among three captured competitor homepages, a click-to-call control appears in the header on two pages.",
  "finding_scope": "cross_competitor",
  "pattern_key": "phone_prominent",
  "recurrence": { "observed_count": 2, "eligible_count": 3, "competitor_ids": ["…-c001", "…-c002"] },
  "evidence_refs": [
    { "artifact": "landings/mig-…-la001/landing_observation.json", "json_pointer": "/cta_patterns/0" },
    { "artifact": "landings/mig-…-la002/landing_observation.json", "json_pointer": "/cta_patterns/1" }
  ],
  "source_artifacts": ["landing_observations.json"],
  "coverage": "partial",
  "confidence_class": "multi_source_structured",
  "evidence_grade": "B",
  "safe_unknown": false
}
```

**Example (invalid — ORCA territory):**

```json
{
  "finding_text": "Competitor A should be prioritized for PPC because of stronger trust signals.",
  "priority": 1
}
```

### 3.4 Evidence reference item

| Field | Required | Meaning |
|-------|----------|---------|
| `artifact` | **Yes** | Session-relative path or registry key |
| `json_pointer` | **O** | RFC 6901 pointer into JSON artifact |
| `field_path` | **O** | Legacy alias — prefer `json_pointer` |
| `verbatim_excerpt` | **O** | Short quoted substring — must match source |
| `snapshot_id` / `landing_id` / `competitor_id` | **O** | Linkage convenience |
| `source_type` | **Yes** | `filesystem_artifact` \| `human` \| `serp_provider` \| `snapshot` \| `unknown` |

### 3.5 Confidence class (qualitative — not ORCA confidence)

| Value | Meaning |
|-------|---------|
| `single_source_structured` | One artifact, structured field |
| `single_source_narrative` | One artifact, prose excerpt (LLM-narrated from JSON) — grade capped **C** |
| `multi_source_structured` | ≥2 independent artifact refs agree |
| `multi_source_partial` | Pattern visible but not all eligible entities captured |
| `operator_attested` | Human annotation with explicit ref |
| `not_assessed` | Reserved — prefer `safe_unknown` finding instead |

**Excluded:** numeric `confidence`, `probability`, `model_logprobs`.

### 3.6 Optional run metadata: `research_synthesis.json`

**Not SoT** for findings — audit trail for pass execution:

| Field | Purpose |
|-------|---------|
| `pass_id`, `started_at`, `completed_at` | Traceability |
| `input_token_estimate`, `model_family` | Ops — **no** model vendor lock in architecture |
| `validation_result` | `passed` \| `rejected` \| `partial` |
| `rejected_claims[]` | Claims that failed citation validation |
| `prompt_profile` | Opaque profile id — **not** prompt text in repo |

Findings **must** be copied into `research_findings.json` only after validation passes.

### 3.7 Future: `finding_registry.json`

**Phase 3 optional** — cross-session pattern catalog for operator search. **Not MVP.** Session SoT remains `research_findings.json`.

---

## 4. Finding categories

### 4.1 Category evaluation

| Category id | Description | MVP | Phase 2 | Notes |
|-------------|-------------|-----|---------|-------|
| `market_structure` | SERP composition: aggregators, local pack density, ads presence, entity types observed | **Yes** | ✓ | From `serp_result.json` + `competitors.json` |
| `competitor_presence` | Who appears on surfaces and how discovered — **not** who is «stronger» | **Yes** | ✓ | Counts and discovery reasons only |
| `offer_patterns` | Recurring visible offer phrasing across landings | **Yes** | ✓ | Requires landing pass or SERP stubs |
| `cta_patterns` | Recurring CTA labels, channels (`tel:`, messenger) | **Yes** | ✓ | |
| `trust_patterns` | Reviews, badges, certificates, policies visible | **Yes** | ✓ | No trust **quality** judgment |
| `website_patterns` | Structural page types, block recurrence, nav/footer patterns | **Yes** | ✓ | From landing + snapshot metadata |
| `pricing_patterns` | Visible price presentation (tables, «from X», units) | **O** | **Yes** | Observation only — no price fairness |
| `keyword_patterns` | Recurring phrases on SERP/landings/registry | **O** | **Yes** | **Not** intent clusters |
| `safe_unknown` | Explicit uncaptured or inconclusive areas | **Yes** | ✓ | Mandatory category |

### 4.2 MVP category set (normative)

Deep Research MVP **must** emit findings only from:

`market_structure` · `competitor_presence` · `offer_patterns` · `cta_patterns` · `trust_patterns` · `website_patterns` · `safe_unknown`

**Optional MVP:** `pricing_patterns` when landing pass includes `pricing_patterns[]`.

**Deferred:** `keyword_patterns` until Keyword Intelligence artifacts exist in session.

### 4.3 Forbidden finding types (never)

| Forbidden type | Reason |
|----------------|--------|
| `strategy_recommendation` | ORCA |
| `competitor_ranking` | ORCA |
| `market_scoring` | ORCA |
| `positioning_statement` | ORCA |
| `campaign_structure` | ORCA |
| `seo_plan` / `ppc_plan` | ORCA |
| `factory_blueprint_hint` | ORCA / Factory |

### 4.4 `finding_text` language rules

| Allowed | Forbidden |
|---------|-----------|
| «Three of five captured pages display …» | «You should …» |
| «SERP shows local pack for query X» | «This is a high-value niche» |
| «Pattern Z appears on domains A and B» | «Competitor A is the leader» |
| «Pricing units not visible on captured pages» | «Prices are competitive» |

---

## 5. Evidence rules

### 5.1 Minimum evidence

| Finding kind | Minimum evidence |
|--------------|------------------|
| **Session-scope structural** (market_structure) | ≥1 `serp_result.json` ref; preferably + `competitors.json` |
| **Cross-competitor pattern** | ≥2 `landing_observation.json` refs **or** ≥2 competitor-linked snapshot refs; if only 1 captured → `coverage: partial` + `safe_unknown` sibling |
| **Single-competitor observation** | ≥1 landing or snapshot ref |
| **safe_unknown** | May cite manifest gap or absence record — `evidence_refs` may point to `session_manifest.json` `/safe_unknown` or empty section marker |
| **LLM-only claim** | **Rejected** — zero refs → not written to SoT |

### 5.2 Cross-artifact validation

1. **Independence:** Multi-source finding should cite artifacts from **different upstream passes** when claiming cross-channel recurrence (e.g. SERP ad headline + landing CTA).
2. **Agreement:** If refs contradict, emit **two findings** or one finding with `contradiction_flag: true` — never resolve by «likely truth».
3. **Eligibility denominator:** `recurrence.eligible_count` = competitors **in scope for capture**, not total market size.

### 5.3 Single-source vs multi-source

| Class | Rule | `confidence_class` |
|-------|------|---------------------|
| **Single-source** | Allowed for per-entity facts | `single_source_structured` |
| **Multi-source pattern** | Required for `finding_scope: cross_competitor` recurrence claims | `multi_source_structured` or `multi_source_partial` |
| **Partial market** | When eligible_count < declared competitor set | `multi_source_partial` + SAFE UNKNOWN for uncaptured |

### 5.4 Citation requirements

1. Every non-`safe_unknown` finding: **`evidence_refs.length >= 1`**.
2. `verbatim_excerpt` when used **must** be substring of referenced artifact field.
3. LLM synthesis output **must** be validated: each proposed finding → resolver checks pointers → on failure → `research_synthesis.json` `rejected_claims[]`, **not** promoted to SoT.
4. **Grade cap:** LLM-narrated finding without structured upstream ref: max grade **C** (`normalized_derivative`).

### 5.5 SAFE UNKNOWN behavior

| Situation | Required behavior |
|-----------|-------------------|
| Landing pass not run | Category `offer_patterns` / `cta_patterns` / etc. → `safe_unknown` finding — not omitted |
| Blocked snapshot | Finding: «Page body not captured for competitor X» + ref to snapshot `capture_status` |
| Model refuses to cite | Reject claim; add session `safe_unknown` string |
| Thin evidence (1 of 5 competitors) | Pattern finding allowed with `coverage: partial` — **must** state denominator in `finding_text` |
| Operator asks for strategy in prompt | **Out of scope** — Worker must not emit |

**Normative:** Prefer **explicit SAFE UNKNOWN findings** over silent empty pack sections.

### 5.6 Hallucination prevention (architecture)

| Control | Layer |
|---------|-------|
| Closed-world input (artifacts only) | Pass design |
| Structured finding JSON output | Pass design |
| Post-validate citation resolver | Pass design |
| Human review before `approved` | HITL |
| Pessimistic evidence grades | Research Pack §4 |
| Reject uncited claims | Validation |

---

## 6. LLM role definition

**Architecture only** — no model selection, no API keys, no OpenRouter setup in this document.

### 6.1 What the model is allowed to do

| Allowed task | Constraint |
|--------------|------------|
| **Summarize** artifact excerpts into `finding_text` | Must attach `evidence_refs` per finding |
| **Compare** observed fields across competitors | Counts and recurrence only |
| **Identify recurrence** of pattern keys already defined in landing/SERP schemas | No new pattern keys without `analysis_notes` flag for operator review |
| **Group** findings by `finding_type` | Structural only |
| **Phrase** SAFE UNKNOWN entries from manifest gaps | No invented gaps |
| **Detect contradiction** between cited fields | Report, do not adjudicate |

### 6.2 What the model is forbidden to do

| Forbidden | Owner |
|-----------|-------|
| Browse open web (MVP default) | Acquisition — charter-only exception future |
| Invent facts not in artifacts | — |
| Recommend actions, priorities, strategies | ORCA |
| Rank competitors or score markets | ORCA |
| Generate PPC/SEO plans | ORCA |
| Produce positioning or value propositions | ORCA |
| Upgrade evidence grade above cited refs | Research Pack §4 |
| Write directly to `approved` pack state | HITL |
| Mutate upstream artifacts (`competitors.json`, landings, etc.) | Pass boundary |

### 6.3 Structured prompt shape (conceptual)

Prompts **must** be structured in four blocks:

1. **Scope block** — Research Request scope fields only.  
2. **Evidence block** — Serialized artifact excerpts with stable ids (`snapshot_id`, `landing_id`).  
3. **Task block** — Allowed finding types + output JSON schema reference.  
4. **Constraint block** — Forbidden language list + citation requirement + «closed world» instruction.

**No** strategy examples in few-shot slots.

### 6.4 Output validation (conceptual pipeline)

```text
LLM raw JSON
    → schema shape check (finding object)
    → forbidden-field scanner
    → citation resolver (each evidence_ref)
    → language linter (imperative / recommendation patterns)
    → promote to research_findings.json OR reject
```

### 6.5 Mapping findings back to evidence

| Step | Rule |
|------|------|
| Resolver loads artifact by path | Session-relative only |
| Pointer walk | Must resolve to existing value |
| Grade assignment | `min(grades of refs)` |
| Recurrence counts | Recomputed deterministically from refs where possible; LLM counts are **hints** — Worker overwrites with deterministic count when mismatch |

**Deterministic fallback (MVP):** Deep Research may run **rules-only** mode (no LLM) for recurrence of known `pattern_key` values from landing observations — LLM optional for phrasing.

---

## 7. Deep Research artifacts

### 7.1 Artifact tiering

| Artifact | Tier | SoT? | Purpose |
|----------|------|------|---------|
| **`research_findings.json`** | **Required** | **Yes** | Canonical finding list |
| **`research_synthesis.json`** | **Optional** | No | Pass audit, validation, rejected claims |
| **`finding_registry.json`** | **Future** | No (catalog) | Cross-session pattern index — Phase 3 |
| **`research_memo.md`** | **Optional** | No | Human-readable narrative projection — **not** cited as evidence by ORCA |
| Per-finding sidecars | **Future** | No | Large verbatim bundles — Phase 3 |

### 7.2 Artifact relationships

```text
upstream: serp_result.json, competitors.json, website_snapshots.json,
          landing_observations.json, [keyword_*]
                    │
                    ▼
          [ Deep Research Pass ]
                    │
        ┌───────────┴───────────┐
        ▼                       ▼
research_findings.json    research_synthesis.json (optional)
        │
        ▼
research_pack.draft.md (projection sections)
        │
        ▼
ORCA handoff bundle (includes research_findings.json when phase ≥ 4)
```

**Principle:** Artifacts = **source of truth**. Research Pack = **projection**. LLM memo = **never** SoT.

### 7.3 Session manifest registration

`session_manifest.json` **artifacts** map gains:

| Key | File |
|-----|------|
| `research_findings` | `research_findings.json` |
| `research_synthesis` | `research_synthesis.json` (optional) |

`deep_research_pass_at`, `deep_research_status`: `complete` \| `partial` \| `skipped` \| `failed_validation`.

---

## 8. Research Pack integration

### 8.1 New projected sections (Phase 4)

Research Pack gains **logical sections** (markdown headings in spine — ids normative):

| Section id | Content source | Notes |
|------------|----------------|-------|
| `research_findings` | Top findings by type — bullet list with `finding_id` | **New** — primary human scan |
| `observed_patterns` | Subset: recurrence findings (`pattern_key` present) | **New** — cross-landing |
| `cross_competitor_observations` | `finding_scope: cross_competitor` | **New** — no ranking language |
| `evidence_summary` | Aggregated grades, coverage, artifact registry refs | Extends existing `evidence_grades` narrative |
| `safe_unknown` | Union: manifest + findings where `safe_unknown: true` | **Existing section** — extended, not replaced |

**Unchanged:** `serp_observations`, `competitor_observations`, `landing_observations`, etc. remain **upstream projections** — Deep Research does not replace them.

### 8.2 Projection rules

1. Pack builder **reads** `research_findings.json` — does not invent findings in markdown.
2. Each projected bullet **should** include `(finding_id)` for traceability.
3. `mig_phase` = `4` when Deep Research pass complete (even if partial coverage).
4. LLM narrative in markdown **cannot** introduce facts absent from `research_findings.json`.
5. **Approval gate:** Deep Research sections appear in `draft` and `review`; ORCA handoff requires `approved` + human review of synthesis (recommended charter).

### 8.3 Pack vs artifact on conflict

**Artifact wins.** If draft markdown disagrees with `research_findings.json`, markdown is wrong — regenerate projection.

---

## 9. ORCA relationship

### 9.1 What ORCA receives (after human approval)

| Deliverable | Content |
|-------------|---------|
| Approved Research Pack | Includes projected Deep Research sections |
| **`research_findings.json`** | Machine-readable SoT for synthesis |
| Upstream artifacts | Unchanged — ORCA may drill down |
| `research_synthesis.json` | Optional — audit only |
| SAFE UNKNOWN (union) | Preserved |

### 9.2 What ORCA may infer

| Allowed inference | Example |
|-------------------|---------|
| Strategic meaning of recurring CTA patterns | «Callback-first market» |
| Competitor prioritization for pilots | Ordered list with rationale |
| Positioning hypotheses | Value proposition drafts |
| PPC/SEO structure | Campaigns, ad groups, semantic core |
| Opportunity scoring | Business judgment |
| Factory-bound blueprints | Via ORCA chain |

**Condition:** ORCA **must** label outputs as **interpretation** — separate from MIG grades.

### 9.3 What ORCA must never assume

| Assumption | Why forbidden |
|------------|---------------|
| Findings are recommendations | MIG declarative only |
| Missing finding category = negative evidence | May be uncaptured |
| `recurrence.observed_count` implies market share | Capture-bounded denominator |
| Deep Research replaced need for landing pass | Upstream SoT still authoritative for page facts |
| `confidence_class` is campaign confidence | MIG qualitative capture class only |
| Approved pack without human review of LLM synthesis | HITL charter |

### 9.4 Exclusively ORCA responsibility (R2)

- Strategy and prioritization  
- Semantic / intent clustering  
- Market scoring and competitor ranking  
- PPC and SEO planning  
- Positioning and messaging architecture  
- Website Factory inputs  
- Business-value interpretation  

### 9.5 R1 / R2 boundary preservation

```text
R1 (MIG):  capture → structure → evidence-backed synthesis (this contract)
R2 (ORCA): interpret → prioritize → plan → hand to Factory
```

**Handoff direction:** MIG → ORCA only. ORCA **must not** write into MIG session artifacts.

---

## 10. Roadmap

### 10.1 Deep Research MVP

| Item | Decision |
|------|----------|
| **Trigger** | After competitor discovery + SERP; landing/website when passes exist |
| **Mode** | **Rules-first** recurrence for `pattern_key` from landing obs; **optional** single LLM phrasing pass with strict validation |
| **Inputs** | `serp_result.json`, `competitors.json`, conditional landing/website |
| **Output** | `research_findings.json` only (synthesis file optional) |
| **Categories** | §4.2 MVP set |
| **Pack** | Project §8 sections into `research_pack.draft.md` |
| **Open web** | **Off** |
| **Failure** | Pass `failed_validation` — pack valid without findings; SAFE UNKNOWN explains |

### 10.2 Phase 2

| Item | Decision |
|------|----------|
| LLM single-pass synthesis with citation validator (required for promotion) | |
| `pricing_patterns`, `keyword_patterns` categories when artifacts exist | |
| `research_synthesis.json` standard audit artifact | |
| Multi-query: ingest `serp_index.json` for cross-query `market_structure` | |
| `research_memo.md` optional operator-readable narrative | |

### 10.3 Phase 3

| Item | Decision |
|------|----------|
| Multi-pass: extract findings → cross-validate → narrate (human review between) | |
| Optional dual-model validation for high-stakes sessions (charter) | |
| `finding_registry.json` cross-session pattern catalog | |
| External browse only via **new acquisition channel** + explicit charter — not default Deep Research |

### 10.4 Anti-bloat rules

1. **No** separate pack type.  
2. **No** numeric scoring fields in findings.  
3. **No** new acquisition in Deep Research MVP.  
4. **Defer** cross-session memory until Phase 3.  
5. **Defer** JSON Schema files to implementation wave — this contract is semantic SoT.

---

## 11. Architecture decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| **DR-01** | Deep Research is a **channel**, not a replacement for Landing Analysis | Preserves per-page SoT |
| **DR-02** | `research_findings.json` is **only** synthesis SoT | Prevents memo drift |
| **DR-03** | Findings are **declarative** — no recommendation fields | ORCA boundary |
| **DR-04** | Cross-competitor claims need **≥2 refs** or partial + SAFE UNKNOWN | Anti-hallucination |
| **DR-05** | LLM grade cap **C** when narrative-only | Research Pack §4 |
| **DR-06** | Same Research Pack object, `mig_phase: 4` | No product proliferation |
| **DR-07** | Rules-only recurrence acceptable for MVP | Reduces LLM dependence |
| **DR-08** | Keyword patterns deferred until KI artifacts in session | Avoid premature clustering |
| **DR-09** | ORCA reads findings + upstream artifacts | Drill-down integrity |
| **DR-10** | Validation failure does not block deterministic pack | Survivability |

---

## 12. Risks

| Risk | Mitigation |
|------|------------|
| LLM hallucination | Closed-world input + citation validator + reject uncited |
| Boundary creep into strategy | Forbidden fields + language linter + boundaries.md |
| Thin competitor capture → false «market norms» | Mandatory denominators + partial coverage + SAFE UNKNOWN |
| Operator treats findings as orders | Pack labeling «observations only»; ORCA handoff doc |
| Duplicate work with Landing Analysis | Deep Research reads only; no re-extraction |
| Over-reliance on narrative memo | Memo not SoT; findings JSON required for phase 4 |
| Phase 4 before Phase 3 artifacts | Request gate + skip categories with explicit unknowns |

---

## 13. Related documents

| Document | Role |
|----------|------|
| [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) | Pack sections, evidence grades, Phase 4 note |
| [mig-landing-analysis-architecture-v1.md](mig-landing-analysis-architecture-v1.md) | Upstream landing SoT |
| [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) | Upstream snapshot SoT |
| [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) | Keyword boundary |
| [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) | Minimum handoff |
| [../boundaries.md](../boundaries.md) | MIG vs ORCA matrix |
| [../reports/REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) | Phase 4 placement (historical) |

---

## 14. Recommended next step

1. **Human review** of this contract against a real session folder (e.g. `sessions/mig-*` with competitors + snapshots + landings).  
2. **Draft JSON Schema** for `research_findings.json` (implementation wave — out of scope here).  
3. **Spine spec**: extend `build-research-pack.js` projection map (implementation charter).  
4. **Pilot rules-only pass** before any LLM integration.  
5. **Update** Research Pack contract §2 table with explicit Phase 4 section ids (minor doc alignment — optional).

---

*End of MIG Deep Research Architecture v1.*
