# REPORT — MIG Data Acquisition Architecture v1

**Status:** Architecture only — no implementation, no integrations, no deployment, no API keys.  
**Date:** 2026-06-01  
**Lane:** B — MIG Data Acquisition Architecture  
**Evidence base:** [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md); domain contracts under `projects/mig/contracts/`; session spine `projects/mig/lib/`; [REPORT-mig-runtime-design-metabot-patterns-v1.md](REPORT-mig-runtime-design-metabot-patterns-v1.md); [REPORT-mig-n8n-node-level-specification-v1.md](REPORT-mig-n8n-node-level-specification-v1.md); MetaBOT patterns in `incoming/metabot/`.

**Normative boundary (unchanged):**

> **MIG acquires reality. ORCA interprets reality.**

---

## Executive Summary

MIG today has a **mature domain model** (Research Request → Research Session → Research Pack) and **post-capture** processing (SERP normalization, competitor discovery logic, pack assembly). What is missing is a **designed, production-oriented acquisition layer** — the physical “eyes” that obtain search results, page bodies, keyword surfaces, and deep evidence **before** normalization.

**Recommendation:** adopt a **four-channel acquisition topology** plus an **orchestration spine** (already partially implemented as session spine + future Worker routes):

| Layer | Delivers | MVP posture |
|-------|----------|-------------|
| **Search Acquisition** | Normalized SERP groundtruth | **Hybrid:** operator manual import + **one** paid Yandex-capable API |
| **Keyword Surface Acquisition** | Observable query/phrase **surfaces** (not strategy) | **Operator seeds + SERP features**; no Wordstat automation in MVP |
| **Website Acquisition** | Fetch + extract evidence for landing/trust/offer | **HTTP + static HTML extract** for top-N URLs |
| **Deep Research Acquisition** | Cited synthesis over **existing** artifacts | **Deferred** until Phases 1–3 artifacts are reliable |
| **Competitor Discovery** (derived) | Entities from SERP surfaces | **Wire existing** `discover-from-serp` into spine after SERP |

**Orchestration:** MetaBOT-style **n8n Intake / Worker / Admin** on existing VPS; **heavy fetch/parse in standalone Node** (session-spine library + small acquisition modules); n8n owns **locks, Telegram UX, scheduling hooks, provider HTTP nodes** — not browser farms or complex DOM pipelines.

**Russian market default:** `search_engine: yandex`, mobile-first SERP, regional/geo parameters explicit in every capture artifact; Google as **secondary** capture profile only when chartered.

**Ruthless MVP:** do **not** build Wordstat API, Playwright grid, multi-model LLM research, or query generation in v1 acquisition. Ship **one SERP provider path**, **manual fallback**, **competitor pass**, **lightweight HTTP site fetch**, **HITL approval** — then expand.

---

## Acquisition Layer Topology

### Design principle

Acquisition is **not** a single API call. It is a **set of bounded channels**, each producing **versioned session artifacts** consumed by normalization and pack builders. Channels are **independent** (can fail separately) and **merge** only at pack assembly with explicit SAFE UNKNOWN.

### Final topology

```text
                    ┌─────────────────────────────────────┐
                    │   Research Request (intake SoT)    │
                    │   seeds, scope, request_type        │
                    └─────────────────┬───────────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │  Acquisition Orchestrator            │
                    │  (Worker routes / session spine)     │
                    │  manifest.stage, retry, coverage     │
                    └─────────────────┬───────────────────┘
          ┌───────────┬───────────┬───┴───┬───────────┬───────────┐
          ▼           ▼           ▼       ▼           ▼           ▼
    ┌──────────┐ ┌──────────┐ ┌────────┐ ┌────┐ ┌──────────┐ ┌──────────┐
    │ Search   │ │ Keyword  │ │Website │ │Comp│ │ Deep     │ │ Manual   │
    │Acquisit. │ │ Surface  │ │Acquis. │ │Disc│ │ Research │ │ Override │
    │ Layer    │ │ Layer    │ │ Layer  │ │(*) │ │ Layer    │ │ (all)    │
    └────┬─────┘ └────┬─────┘ └───┬────┘ └─┬──┘ └────┬─────┘ └────┬─────┘
         │            │           │        │         │            │
         ▼            ▼           ▼        ▼         ▼            ▼
    serp_result   keyword_    site_    competitors  research_   operator
    .json /       surface.    capture.  .json       memo.       JSON
    serp_bundle   json        json                  .json       drops
         │            │           │        │         │            │
         └────────────┴───────────┴────────┴─────────┴────────────┘
                                      │
                    ┌─────────────────▼───────────────────┐
                    │  Normalization + Pack Assembly       │
                    │  build-research-pack, evidence grades  │
                    └─────────────────┬───────────────────┘
                                      ▼
                              Research Pack
                                      ▼
                                   ORCA (R2)
```

(*) **Competitor Discovery** is **derived acquisition** — no separate external “competitor API”; it consumes Search (+ optional Website) artifacts per [mig-competitor-discovery-contract-v0.md](../contracts/mig-competitor-discovery-contract-v0.md).

### Layer responsibilities

| Layer | Owns | Does not own |
|-------|------|----------------|
| **Search Acquisition** | Live or imported SERP JSON, ads/maps blocks, organic lists, related-search **if visible on SERP** | Query generation, intent labels, PPC bids |
| **Keyword Surface Acquisition** | Seeds executed, suggestion strings **as captured**, competitor page **visible** phrases (title/H1/meta) | Volume strategy, clustering, campaign structure |
| **Website Acquisition** | HTTP status, raw/archived HTML, extracted text blocks, optional screenshot | Site strategy, semantic locks, content packs |
| **Deep Research Acquisition** | Multi-source **synthesis with citations** to session artifacts | Inventing facts not in artifacts; ORCA interpretation |
| **Orchestrator** | Ordering, coverage metadata, failure branches, `safe_unknown` aggregation | Business recommendations |

### Phase alignment (pack contract)

| Pack phase | Acquisition channels required |
|------------|------------------------------|
| **Phase 1** | Search (+ manual override) |
| **Phase 2** | Search (multi-query) + Competitor Discovery |
| **Phase 3** | + Website Acquisition (landing/offer/CTA/trust) |
| **Phase 4** | + Deep Research Acquisition |

---

## Search Acquisition Layer

### Role

Obtain **search engine results pages** as structured evidence: organic, ads, local pack/maps, aggregators, marketplaces, review snippets visible **on SERP** — aligned with `serp_result.json` schema v0.1 and future `serp_bundle` for multi-query.

### Options evaluated

| Option | Advantages | Limitations | Cost (order of magnitude) | Operational complexity | MIG suitability |
|--------|------------|-------------|---------------------------|------------------------|-----------------|
| **Yandex Search API** | Official; compliant; predictable for Yandex RU | Narrow feature parity vs real SERP UI; access/quotas; may miss ads/local nuances | Medium (commercial API) | Low–medium (HTTP + mapping) | **High** for RU core — if contract covers mobile + geo |
| **SerpApi** | Fast integration; Yandex/Google; JSON SERP | Per-query pricing; vendor dependency; rate limits | **$$** at volume (~$0.002–0.01+/query tier-dependent) | Low | **High** for MVP automation |
| **DataForSEO** | SERP + related APIs; scale; task-based | Heavier API model; learning curve; overkill for tiny MVP | **$$–$$$** (task + volume) | Medium | **High** Phase 2+ / multi-client scale |
| **Browser automation** (Playwright/Puppeteer) | Closest to “what user sees”; ads/local | Captcha, blocks, maintenance, VPS RAM; fragile | Infra + operator time | **High** | **Medium** — fallback only, not primary |
| **Manual import** | Zero API risk; HITL quality; **proven v0.1** | Slow; inconsistent; operator burden | Operator time | Low | **Required** forever as override |
| **Hybrid** | Provider primary + manual fallback + optional browser | Two code paths to test | Mixed | Medium | **Recommended production shape** |

### Russian / Yandex / SEO / PPC notes

- **Default engine:** `yandex` in scope; capture profile must record **region, city, device, language**.
- **PPC relevance:** capture **ads_blocks** and visible ad patterns on SERP — MIG observation only; ORCA maps to campaigns.
- **SEO relevance:** organic titles, URLs, sitelinks, FAQ rich results if present in provider payload — map to schema, else SAFE UNKNOWN.
- **Website Factory:** Factory does **not** consume raw SERP; approved pack → ORCA → strategy. Search acquisition still matters as **upstream groundtruth**.

### Recommendations

| Horizon | Recommendation |
|---------|----------------|
| **MVP** | **Hybrid:** keep **manual_serp** (operator JSON template + browser copy discipline) + integrate **one** paid provider with **proven Yandex mobile** support (**SerpApi** or **DataForSEO** — operator chooses one; do not integrate both in MVP). **Fail closed** to manual + `source_mode: fallback` with explicit SAFE UNKNOWN (v0.1 pattern). |
| **Phase 2** | **Multi-query loop:** N queries per session → `serp_bundle/` or indexed `serp_result.{query_id}.json`; coverage block per [mig-multi-query-discovery-design-v0.md](../contracts/mig-multi-query-discovery-design-v0.md). Provider scheduler in Worker (sequential + backoff), not parallel burst. |
| **Long-term** | **Hybrid tiered:** provider → manual override → **selective** Playwright capture for sessions where provider returns `degraded` or missing local pack; store raw provider payload in `snapshots/serp/raw/` for audit. |

### Acquisition artifact (search)

| File | When |
|------|------|
| `serp_result.json` | Single-query session |
| `serp_bundle/manifest.json` + `serp_result.{query_id}.json` | Multi-query v0.3+ |
| `snapshots/serp/raw/{provider}_{query_id}.json` | Optional audit (Phase 2+) |

---

## Website Acquisition Layer

**Normative design (v1):** [mig-website-acquisition-architecture-v1.md](../contracts/mig-website-acquisition-architecture-v1.md) — Website Snapshot object, artifacts, SAFE UNKNOWN, MVP scope. This report retains the **channel overview** only.

### Role

Inspect **URLs discovered on SERP** (and operator `signals[]`) to produce **landing/offer/CTA/trust** evidence for Phase 3 pack sections — without replacing ORCA semantics.

### Options evaluated

| Method | Advantages | Limitations | MVP / Phase / Long-term |
|--------|------------|-------------|-------------------------|
| **Raw HTML (HTTP GET)** | Cheap; fast; VPS-friendly; easy to archive | No JS rendering; bot blocking | **MVP primary** |
| **HTTP fetch + headers** | Redirect chain, status, charset | Same as above | **MVP** |
| **DOM extraction** (Cheerio/jsdom) | Structured selectors: title, h1, meta, links | Breaks on SPAs | **MVP** |
| **Readability / boilerplate removal** | Cleaner text for pack excerpts | Can strip useful nav/pricing tables | **Phase 2** enhancement |
| **Playwright** | JS-rendered content; real DOM | RAM, maintenance, captcha | **Phase 2** selective |
| **Browser screenshots** | Strong HITL evidence | Storage; not searchable | **Phase 2** optional per URL |
| **Full-page capture** (MHTML/PDF) | Legal/audit grade | Size; tooling | **Long-term** high-value sessions |
| **Hybrid** | Static first; Playwright only on `render_required` flag | Two pipelines | **Long-term default** |

### Policy

1. **Respect robots / rate limits** — per-domain delay (design: 2–5 s default between fetches on same host).
2. **No unbounded crawl** — only URLs from SERP organic/ads/local entities + explicit operator seeds (max **10–15 URLs/session** MVP).
3. **Store evidence:** `site_capture.{url_hash}.json` + optional `snapshots/sites/{url_hash}.html`.
4. **Never** LLM-invent page content at capture stage.

### Recommendations

| Horizon | Recommendation |
|---------|----------------|
| **MVP** | **HTTP GET + DOM extract** (title, meta description, h1–h2, visible CTA text, phone patterns, trust badges if in static HTML). Mark `render_status: static_only`. |
| **Phase 2** | Add **Playwright** path for URLs with `render_required: true` (operator flag or heuristic: empty body / SPA shell). Optional **screenshot** to `snapshots/sites/`. |
| **Long-term** | **Hybrid pipeline** with readability extraction + full-page archive for approved packs; link from `competitor_observations` via `landing_evidence_refs[]` per competitor contract §10.2. |

---

## Keyword Acquisition Layer

### Critical boundary: MIG vs ORCA

| Concern | **MIG (R1)** — acquire | **ORCA (R2)** — interpret |
|---------|------------------------|---------------------------|
| Seed / executed query strings | **Yes** — operator-provided, exact capture text | Uses for intent mapping |
| SERP-visible related searches / suggestions | **Yes** — if shown on captured SERP | Clusters into intent groups |
| Competitor page visible phrases (title, H1, meta) | **Yes** — as website capture facts | Semantic locks, content architecture |
| Wordstat **raw export** / API response tables | **Yes** — as **evidence artifact** (optional) | Volume prioritization, campaign structure |
| Search volume strategy, phrase prioritization | **No** | **Yes** |
| Intent clustering, semantic clusters | **No** | **Yes** |
| Campaign / ad group / keyword bids | **No** | **Yes** |
| LRL, Commander exports, PPC pilots | **No** | **Yes** |
| Query **generation** / expansion automation | **No** (explicit in multi-query design §1.4) | May propose queries for **human** re-submission to MIG |

**Rule:** MIG records **what was observable** on surfaces. ORCA decides **what it means** for SEO/PPC/Factory.

### Sources evaluated

| Source | MIG? | Notes |
|--------|------|-------|
| **Manual seed queries** | **Yes — MVP core** | `queries.seed_queries[]` / `query_set[]` — operator or ORCA-submitted request file, not generated inside MIG |
| **Search suggestions** (Yandex/Google autocomplete) | **Phase 2** — if captured via API or SERP feature | Store in `keyword_surface.json`; no auto-execute without operator approval |
| **Yandex Wordstat API** | **Phase 2+ artifact only** | Raw table → `wordstat_capture.json`; interpretation ORCA |
| **Google suggestions** | **Optional secondary** | Same as suggestions |
| **SERP snippets** (titles/descriptions) | **Yes** — part of SERP normalization | Already in organic results |
| **Competitor-derived keywords** | **Yes — Phase 2+** | From website capture visible text — **not** scraped site-wide keyword tools |
| **Third-party SEO APIs** (Ahrefs, etc.) | **Long-term / charter** | High cost; vendor lock-in; separate acquisition module if ever |

### Keyword Surface artifact (design)

```json
{
  "schema_version": "0.1",
  "session_id": "mig-YYYYMMDD-xxxxxx",
  "seed_queries": [],
  "queries_executed": [],
  "surfaces": [
    {
      "surface_type": "seed|serp_related|suggestion_api|wordstat_export|page_visible",
      "source_artifact": "serp_result.json",
      "strings": [],
      "captured_at": "ISO-8601",
      "evidence_grade": "operator|provider|extracted"
    }
  ],
  "safe_unknown": []
}
```

### Recommendations

| Horizon | Recommendation |
|---------|----------------|
| **MVP** | **Operator seeds only** + mirror executed queries in pack **Query Set**; SERP organic titles as implicit keyword surface (no separate file required). |
| **Phase 2** | `keyword_surface.json` for related searches + optional **manual Wordstat CSV import** (operator uploads file → adapter ingests). |
| **Phase 3** | Controlled suggestion capture (single API call per seed, stored not auto-run). |
| **Long-term** | Wordstat API batch job as **scheduled acquisition module** (standalone JS), not n8n logic. |

---

## Deep Research Layer

### Role

Phase 4: extend evidence with **structured synthesis** across session artifacts — **citations mandatory**, **SAFE UNKNOWN** for gaps, **no** new facts without artifact pointers.

### Options evaluated

| Approach | Advantages | Limitations | Fit |
|----------|------------|-------------|-----|
| **OpenRouter** (single model) | Ecosystem already used by MetaBOT; model choice | Cost; hallucination risk | **Phase 2+** with strict guardrails |
| **LLM research passes** (multi-step) | Deeper narratives | Token cost; drift | Phase 3–4 |
| **Multiple-model validation** | Reduces single-model bias | 2–3× cost | Long-term high-stakes only |
| **Structured extraction** (JSON schema) | Pack-friendly | Needs validation node | **Recommended** alongside narrative |
| **Citation requirements** | Audit trail | Prompt engineering | **Mandatory** |
| **SAFE UNKNOWN behavior** | Aligns with MIG discipline | Model may resist | Enforce post-validate + reject uncited claims |

### Rules (normative)

1. **Input boundary:** LLM receives **only** session artifact excerpts (SERP JSON, site captures, competitor list) — not open web browse in MVP.
2. **Output:** `research_memo.json` + optional `research_memo.md` section in pack — **not** SoT; artifacts remain SoT per pack contract.
3. **OpenRouter in Worker only** — not Intake; not on raw SERP capture (per runtime design report).
4. **Failure:** `failed_llm` stage; pack remains valid without memo; gaps in SAFE UNKNOWN.

### Recommendations

| Horizon | Recommendation |
|---------|----------------|
| **MVP** | **None** — deterministic pack from spine only. |
| **Phase 2** | Optional **single-pass** summarization: «narrate existing SERP + competitors» with **citation map** `{claim_id → artifact_ref}`. |
| **Phase 3** | Multi-pass: extract → cross-check → narrative; human review required before `approved`. |
| **Long-term** | Dual-model validation for `deep_research` request type; external browse only via **explicit charter** + new acquisition channel (not default). |

---

## n8n Architecture Recommendations

Aligned with [REPORT-mig-runtime-design-metabot-patterns-v1.md](REPORT-mig-runtime-design-metabot-patterns-v1.md) and MetaBOT v14 patterns.

### Run inside n8n

| Concern | Rationale |
|---------|-----------|
| **MIG Intake** | Telegram, locks, Sheets, webhook dispatch — proven MetaBOT UX |
| **MIG Worker — orchestration** | Route commands, stage updates, Telegram `editMessageText`, Sheets registry |
| **Provider HTTP Request nodes** | SERP API calls with n8n credentials store — simple request/response |
| **MIG Admin** | Health, cancel, lock cleanup |
| **Thin Code nodes** | Call `require()` session-spine paths when `NODE_FUNCTION_ALLOW_*` configured on VPS |

### Standalone JS (repo `projects/mig/lib/`)

| Module | Rationale |
|--------|-----------|
| **session-spine** | Already exists; filesystem SoT |
| **normalize-serp, competitor-discovery** | Testable, versioned, used from CLI + n8n |
| **site-fetcher** (future) | HTTP, parsing, hashing — unsuitable for n8n Code node complexity |
| **wordstat-ingest** (future) | File/API ingest + validation |
| **acquisition-coverage** (future) | Merge coverage metadata across channels |

### Reusable services (Phase 2+ — optional)

| Service | When |
|---------|------|
| **Local HTTP microservice** `127.0.0.1:3xxx/mig/acquire` | If Playwright must run outside n8n process; Worker calls via HTTP |
| **Not required for MVP** | Spine invoked via `child_process` from Worker Code node or task-file adapter is enough |

### Do NOT run in n8n

| Anti-pattern | Why |
|--------------|-----|
| **Playwright / headless farm** | Memory, hangs, n8n execution timeout |
| **Heavy DOM crawling loops** | Hard to debug in graph; no unit tests |
| **OpenRouter on Intake** | Violates separation; key exposure risk |
| **Long-running deep research chains** | Exceeds webhook TTL; use async Worker + status message |
| **Filesystem as only registry** | Sheets lock/registry stays in n8n ecosystem |
| **Embedding SEO Content Agent workflows** | Boundary violation vs MetaBOT |

### VPS compatibility

- Same host as `n8n.ai-metacode.com` (per runtime design).
- `MIG_SESSION_ROOT` on disk accessible to n8n Code nodes (`fs`).
- Playwright (Phase 2): install browsers on VPS; **isolate** in subprocess/service — monitor RAM (≥2 GB headroom recommended for concurrent sessions).

---

## Artifact Flow

### End-to-end

```text
Research Request
  request_id, request_type, scope, queries.seed_queries[], signals[]
        │
        ▼
session_manifest.json ◄──────────────────────────┐
        │                                         │
        ├─► [Search Acquisition]                  │
        │         serp_result.json (or bundle)      │
        │                                         │
        ├─► [Keyword Surface] (optional)          │
        │         keyword_surface.json            │
        │                                         │
        ├─► [Competitor Discovery]                │
        │         competitors.json                │
        │         (reads SERP only in Ph2)        │
        │                                         │
        ├─► [Website Acquisition]                 │
        │         site_capture.*.json             │
        │         snapshots/sites/*               │
        │                                         │
        ├─► [Deep Research]                       │
        │         research_memo.json              │
        │                                         │
        └─► build-research-pack ──────────────────┘
                  │
                  ▼
        research_pack.draft.md
        (logical Research Pack + sections)
                  │
                  ▼ HITL
        research_pack.approved.md
                  │
                  ▼ human handoff
              ORCA (R2)
```

### Artifact registry (session folder)

| Artifact | Producer | Pack section(s) |
|----------|----------|-----------------|
| `serp_result.json` | Search Acquisition | SERP Observations |
| `serp_bundle/*` | Search (multi-query) | SERP + Query Set coverage |
| `keyword_surface.json` | Keyword Surface | Query Set (+ optional annex) |
| `competitors.json` | Competitor Discovery | Competitor Observations |
| `site_capture.*.json` | Website Acquisition | Landing / Offer / CTA / Trust |
| `research_memo.json` | Deep Research | Annex + cited narrative |
| `session_manifest.json` | Orchestrator | Metadata, stages, artifact refs |
| `research_pack.*.md` | Pack builder | All sections |

### Research Pack assembly rules

1. **Order:** Search → Competitor (from SERP) → Website (from URLs) → Deep Research (from all).
2. **Missing channel:** section absent + **SAFE UNKNOWN** entry — never fabricated.
3. **Evidence grades:** per-section minimum escalates with phase ([mig-research-pack-contract-v0.md](../contracts/mig-research-pack-contract-v0.md) §5).
4. **LLM narrative** may **summarize** existing JSON — **must not** replace missing SERP fields.

---

## Operator Workflow

### Recommended happy path (groundtruth_run)

```text
1. Submit niche + region + seed queries
      │  (Task file → incoming/mig/requests/  OR  /mig run  Phase 2+)
      ▼
2. Capture search (per query)
      │  provider OR paste manual_serp JSON
      ▼
3. Review SERP coverage
      │  operator confirms maps/ads/organic present; mark gaps
      ▼
4. Competitor discovery pass (automatic from SERP)
      │  operator HITL: add/remove seeds only via new capture, not LLM
      ▼
5. Capture sites (top N URLs)
      │  HTTP fetch; flag SPA for Phase 2 Playwright
      ▼
6. Optional: Wordstat CSV import / keyword surface review
      ▼
7. Deep research (Phase 4 only, optional)
      │  LLM memo with citations; operator reviews claims
      ▼
8. Pack draft → review → approve
      │  research_pack.approved.md + manifest Approved By
      ▼
9. ORCA handoff (human)
```

### MVP operator path (minimal)

```text
submit request (task file) → manual SERP JSON OR first provider call
  → spine draft pack → human edits draft → approve file → ORCA
```

### Workload controls

| Control | Purpose |
|---------|---------|
| **Lock per chat** (Intake) | One active session — reduces cost runaway |
| **Max queries/session** | MVP: 3–5; Phase 2: 10 with charter |
| **Max URLs/session** | MVP: 5–10 fetches |
| **Explicit `request_type`** | Prevents accidental deep/landing pipelines |
| **Sheets registry** | Operator sees history without opening FS |

### Website Factory operator

Factory operators **do not** run acquisition. They receive ORCA outputs. If groundtruth missing, **new Research Request** to MIG — not Factory crawl.

---

## MVP Definition

### Build first (ruthless)

| # | Deliverable | Notes |
|---|-------------|-------|
| 1 | **Manual SERP discipline** | Template JSON + validation; document operator steps |
| 2 | **One SERP provider** | Yandex mobile + geo; map to `serp_result.json`; store raw snapshot |
| 3 | **Wire competitor discovery** | `discover-from-serp` after normalize in spine/Worker |
| 4 | **HTTP site fetch (top 5)** | Static extract → stub landing observations in pack |
| 5 | **Task file + spine path** | Already exists — extend manifest `acquisition_coverage` |
| 6 | **HITL approve** | `research_pack.approved.md` + manifest fields (manual Phase 2) |

### Explicitly out of MVP

- Wordstat API / autocomplete automation  
- Playwright / screenshots  
- Multi-query scheduler (can run **sequential manual** second query)  
- OpenRouter / deep research  
- n8n three-workflow production import (can follow after acquisition modules exist)  
- mars-runtime automation  

### Success criteria (MVP)

Operator can complete **one Yandex mobile SERP session** for a RU local-service niche with **provider OR manual**, **competitors.json** populated, **≥1 site capture**, **draft pack** with honest SAFE UNKNOWN — **without** ORCA or Factory in the loop.

---

## Phase 2

| Item | Description |
|------|-------------|
| Multi-query SERP | `serp_bundle` + multi-query discovery aggregation |
| n8n Worker production | Intake/Worker/Admin webhooks live |
| Keyword surface file | Related searches + manual Wordstat CSV ingest |
| Playwright selective | SPA URLs only |
| OpenRouter | Single-pass cited summarization (optional route) |
| Google Sheets registry | Session index (design already in runtime report) |
| Suggestion capture | Bounded API calls, operator-approved execution |

---

## Phase 3

| Item | Description |
|------|-------------|
| Landing/trust depth | Full Phase 3 pack sections with screenshots |
| Wordstat API module | Standalone ingest service |
| Provider fallback tier | Playwright for degraded SERP |
| Acquisition retry policy | Exponential backoff, partial session resume |
| Coverage dashboards | Admin route: acquisition completeness per session |

---

## Risks

| Risk | Impact | Mitigation |
|------|--------|------------|
| **API dependency** | Provider outage blocks capture | **Hybrid:** manual import always; manifest `source_mode`; degrade don't fake |
| **Cost growth** | Multi-query × SERP × sites | Per-session caps; lock; operator approval for >N queries; cache SERP 24h per query hash (Phase 2) |
| **Captcha / blocking** | Empty SERP / banned IP | Prefer APIs over browser; rotate only with charter; mark `failed` + SAFE UNKNOWN |
| **Vendor lock-in** | SerpApi/DataForSEO pricing | Abstract `SerpProvider` interface in lib; raw payload archived; manual path |
| **OpenRouter dependence** | LLM outage / drift | Deep research optional; deterministic pack valid without memo; credentials in n8n env only |
| **Wordstat limitations** | API access, quotas, semantics | Treat as **artifact import**; ORCA interprets; no auto-bid decisions in MIG |
| **Browser maintenance** | Playwright version drift | Isolate service; pin versions; use only Phase 2+ selective path |
| **n8n limitations** | Timeouts, Code node fs | Heavy work in standalone JS; async Worker; status Telegram chain |
| **Operator overload** | Manual SERP doesn't scale | Invest MVP in **one** reliable API; templates reduce paste errors |
| **Context drift** | Agent invents SERP data | Schema validation; forbid LLM on capture; verifier scripts (pattern: existing `verify-*-v0.mjs`) |
| **R1/R2 bleed** | Keywords clustered in MIG | Enforce boundaries.md; reject `downstream_context` with semantic clusters |

---

## Architecture Decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| **DA-01** | Four acquisition channels + derived competitor pass | Matches pack phases; independent failure domains |
| **DA-02** | Filesystem = artifact SoT; Sheets = index only | Proven v0.1 + MetaBOT hybrid |
| **DA-03** | MVP = manual SERP + one API + HTTP sites | Fastest path to real «eyes» without browser farm |
| **DA-04** | Yandex-first default for RU market | Aligns with scope contracts and ORCA PPC pilots |
| **DA-05** | Keyword **surfaces** in MIG; strategy in ORCA | Strict R1/R2 boundary |
| **DA-06** | No LLM on raw capture | Pack contract + competitor contract forbid invention |
| **DA-07** | n8n orchestrates; lib acquires | Maintainability + unit tests |
| **DA-08** | Multi-query before deep research | Evidence breadth before synthesis |
| **DA-09** | Manual override never removed | Survivability / API outage |
| **DA-10** | No separate acquisition contract file in v1 | This report + existing contracts sufficient; add `mig-data-acquisition-model-v1.md` only when implementing schemas |

---

## SAFE UNKNOWN

| Topic | Status |
|-------|--------|
| Live Yandex Search API feature parity vs SerpApi for **ads/local pack** | **UNKNOWN** — requires operator trial on target queries |
| Exact SerpApi/DataForSEO pricing at expected monthly volume | **UNKNOWN** — depends on query count; model in §Risks |
| VPS RAM headroom for Playwright concurrent with n8n | **UNKNOWN** — measure on host |
| Whether MIG uses dedicated Telegram bot vs shared with MetaBOT | **UNKNOWN** — runtime design prefers `/mig` namespace |
| Wordstat API access for operator account | **UNKNOWN** — may be CSV-only |
| Legal ToS for automated fetch of competitor sites in RU jurisdiction | **UNKNOWN** — human charter; MIG stores public page facts only |
| Auto-cleanup of stale Sheets locks | **UNKNOWN** — MetaBOT export gap noted in runtime report |

---

## Recommended Next Step

1. **Human review** of this report against operator budget (pick **one** SERP vendor for MVP trial).  
2. **Charter MVP implementation** (separate task): provider adapter module + wire `discover-from-serp` + minimal `site-fetcher` — still no n8n export until lib tests pass.  
3. **Update** [OPERATIONAL-INDEX.md](../OPERATIONAL-INDEX.md) with link to this report under «Acquisition architecture».  
4. **Optional:** add `keyword_surface.json` schema stub when Phase 2 starts — not before MVP ships.

**No separate contract file** in v1 — boundaries are already normative in [boundaries.md](../boundaries.md) and domain contracts; acquisition schemas should be introduced alongside implementation PRs.

---

*End of report — MIG Data Acquisition Architecture v1.*
