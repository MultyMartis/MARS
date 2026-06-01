# MIG Keyword Intelligence Architecture v1

**Status:** **documented** — domain-level architecture for MIG Keyword Intelligence (search-demand acquisition channel).  
**Not:** implementation, JSON Schema registry, Wordstat OAuth setup, browser farm product, suggestion API credentials, clustering engine, PPC/SEO strategy generator, ORCA semantics, or runtime product.

**Supersedes:** Implicit «Keyword Surface» / «Keyword Acquisition» sections in [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) §Keyword Acquisition Layer (this contract is the **normative** design for that channel).  
**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md); Research Session; Search Acquisition (`serp_result.json`); [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md); [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) (`page_visible` channel).  
**Downstream:** [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) (projected sections — §7); [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md).

**Consumers (future, by reference only):** MIG Worker (keyword passes), session spine, operator HITL UX, ORCA, future MARS runtime observers.

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

Keyword Intelligence **collects observable phrases and frequency evidence**. It **must not** cluster, prioritize, group, or produce campaign or semantic-core structure.

---

## 1. Keyword Intelligence — definition

### 1.1 What Keyword Intelligence is

**Keyword Intelligence** is the MIG acquisition layer that answers:

> **What phrases and query surfaces were observable at capture time, and what frequency or demand signals were attached to them as evidence?**

It is **not** «what should we bid on» or «what is our SEO structure» — those are ORCA questions.

```text
Research Request
    ↓
Research Session
    ↓
Search Acquisition (SERP)
    ↓
Competitor Discovery (optional)
    ↓
Website Acquisition (optional)
    ↓
Keyword Intelligence Pass          ← this architecture
    ↓
keyword_registry.json
keyword_surface.json
wordstat_snapshot.json (optional)
suggestions_snapshot.json (optional)
    ↓
Research Pack (keyword / demand projections)
    ↓
ORCA (R2) — interprets phrases for intent, clusters, PPC, SEO
```

| Concern | Keyword Intelligence owns |
|---------|----------------------------|
| Operator **seed query** strings (exact text) | **Yes** |
| **Executed** query strings (SERP runs) | **Yes** — mirror from Search Acquisition |
| SERP-visible **related searches** / query refinements on captured SERP | **Yes** — when present on surface |
| Autocomplete / **suggestion** strings (Yandex, Google) | **Yes** — as captured lists, not expanded runs |
| **Wordstat** tables (API, export, manual CSV) | **Yes** — raw snapshot artifact |
| **Frequency indicators** (shows, clicks, share — as returned by source) | **Yes** — stored as signals, not interpreted |
| **Page-visible** phrases (title, H1, meta) from Website Acquisition | **Yes** — ingested as `page_visible` surface |
| Per-phrase **source evidence** and capture timestamps | **Yes** |
| **SAFE UNKNOWN** for missing demand data | **Yes** |
| Evidence grade at capture time | **Yes** |

### 1.2 What Keyword Intelligence is not

| Anti-pattern | Owner / reason |
|--------------|----------------|
| Intent clustering, semantic groups, «themes» | **ORCA** |
| Keyword prioritization, head/tail classification for strategy | **ORCA** |
| PPC campaign / ad group / bid structure | **ORCA** |
| SEO semantic core, content cluster map | **ORCA** |
| Query **generation** or expansion automation inside MIG | **Forbidden** — operator or ORCA may propose seeds for **human** re-submission |
| Volume-based **recommendations** («target these first») | **ORCA** |
| LRL, Commander exports, Factory blueprints | **ORCA / Factory** — downstream |
| Replacing SERP or website artifacts as SoT | **Forbidden** — registry **references** upstream artifacts |

### 1.3 Acquisition vs interpretation

| Layer | Question answered |
|-------|-------------------|
| **Acquisition (MIG)** | What **strings** appeared on which **surface**? What **numbers** did Wordstat (or export) return for which phrase+region? |
| **Interpretation (ORCA)** | What **demand**, **intent**, and **structure** do these observations imply for SEO/PPC/Factory? |

**Normative:** A Wordstat row with `shows: 1200` is **evidence**. «High-volume commercial intent» is **interpretation**.

### 1.4 Relationships to other MIG capabilities

| Capability | Relationship |
|------------|--------------|
| **Search Acquisition** | **Upstream** — supplies executed queries, organic titles/snippets, SERP features (related searches when visible). Keyword Intelligence **may** ingest from `serp_result.json` without re-fetching SERP. |
| **Competitor Discovery** | **Parallel / weak upstream** — does not supply keywords directly; supplies entity context for pack narrative only. |
| **Website Acquisition** | **Parallel upstream** — supplies `page_visible` phrase channel via snapshot extract fields. |
| **Research Pack** | **Downstream projection** — pack sections are **views**; keyword artifacts remain SoT. |
| **ORCA** | **Consumer** — after human approval; may request new seeds via Research Request, not by mutating MIG artifacts in place. |

### 1.5 Relationship to Research Request

- `queries.seed_queries[]` is the **primary MVP intake** for keyword work — declared before session bind.
- Optional future fields (not required v1 architecture lock-in):
  - `signals.keyword_seeds[]` — extra seeds without new SERP run
  - `signals.wordstat_import_path` — operator CSV drop reference
  - `capture_profile.keyword_pass` — enum: `off` \| `surface_only` \| `surface_and_wordstat`
- Request **must not** carry pre-built clusters or `downstream_context` with semantic groups (per request contract §4).

---

## 2. Acquisition sources — evaluation

Scoring legend: **Value** (evidence richness for ORCA) · **Cost** (operator time, API money, infra) · **Complexity** (engineering + compliance) · **MVP** / **Ph2** / **Long** suitability.

### 2.1 Source matrix

| Source | Value | Cost | Complexity | MVP | Phase 2 | Long-term | MIG role |
|--------|-------|------|------------|-----|---------|-----------|----------|
| **Manual seed queries** | Medium — anchors session | Low | Low | **Core** | ✓ | ✓ | Copy exact strings to registry + Query Set |
| **Executed queries (SERP)** | Medium — proves what was searched | Low (already paid) | Low | **Core** | ✓ | ✓ | Mirror from manifest / `serp_result.json` |
| **SERP organic titles/snippets** | Medium — market language on SERP | Low | Low | **Implicit** (via SERP) | Optional `keyword_surface` row | ✓ | Extract strings; **no** separate fetch |
| **SERP related searches** (on-page feature) | High — demand hints | Low | Low | **Out** (unless manual SERP includes) | **In** | ✓ | `surface_type: serp_related` |
| **Yandex suggestions** (autocomplete API/UI) | High — expansion surface | Medium | Medium | **Out** | **In** (controlled) | ✓ | `suggestions_snapshot.json` |
| **Google suggestions** | Medium–High (locale-dependent) | Medium | Medium | **Out** | Optional secondary | ✓ | Same model; engine tag on artifact |
| **Yandex Wordstat API** | Very high — numeric demand | High (access, quotas) | High | **Out** | **Hybrid** (see §3) | **In** | `wordstat_snapshot.json` |
| **Wordstat manual export (CSV/XLSX)** | Very high | Low operator | Low | **Out** | **In** (import adapter) | ✓ | Same snapshot schema as API |
| **Wordstat browser automation** | High | High operator + fragility | Very high | **Forbidden MVP** | **Discouraged** | Last resort | Only if API/export blocked — charter + compliance review |
| **Competitor `page_visible`** | Medium — competitor lexicon | Low (after website pass) | Low | **Out** | **In** | ✓ | From website snapshots |
| **Third-party SEO APIs** (Ahrefs, etc.) | High | Very high $$ | Medium | **Out** | **Out** | Charter-only | Separate acquisition module if ever |
| **SERP ads headlines** | Medium | Low | Low | Optional stub | ✓ | ✓ | From normalized ads block in SERP |
| **Future: Search Console / Direct** | High for owned sites | Medium | High | **Out** | **Out** | Charter | Not MIG bootstrap |

### 2.2 Normative source rules

1. **No source may trigger automatic query execution** without operator-approved request scope (multi-query design §1.4 applies).
2. **Every phrase** stored as a **Keyword Object** (§5) or surface row — never only in pack markdown.
3. **Third-party APIs** are not MVP; vendor lock-in requires human charter.
4. **Browser automation** for Wordstat is **not** the default path — see §3.

---

## 3. Wordstat architecture

### 3.1 Design principle

Wordstat data is **evidence**, not strategy. MIG stores **what Wordstat returned** for **which phrase, region, and period** at **capture time**. ORCA applies business rules, seasonality judgment, and campaign structure.

### 3.2 Access modes evaluated

| Mode | Description | Operator burden | Engineering | Compliance / ToS | Recommendation |
|------|-------------|-----------------|-------------|------------------|----------------|
| **Official API** | Yandex Direct / Wordstat API (when licensed) | Low after credential setup | Medium — batch client in JS | Contractual; auditable | **Long-term primary** |
| **Manual export** | Operator downloads CSV/XLSX from Wordstat UI | High per session | Low — file ingest adapter | Human-operated; explicit | **Phase 2 MVP for Wordstat** |
| **Hybrid** | Seeds + regions in MIG; operator uploads export; optional API later for same schema | Medium | Medium | Best pragmatic path | **Phase 2 default** |
| **Browser automation** | Playwright/Puppeteer on wordstat.yandex.ru | High; CAPTCHA risk | High; brittle selectors | **ToS / account risk — SAFE UNKNOWN** | **Not recommended**; charter-only escape hatch |

### 3.3 MVP (Keyword Intelligence)

| Item | Decision |
|------|----------|
| Wordstat | **Not executed** by MIG |
| Pack | Query Set lists seeds + executed queries; SAFE UNKNOWN: «Search demand frequency not captured» |
| Artifacts | No `wordstat_snapshot.json` required |

### 3.4 Phase 2

| Item | Decision |
|------|----------|
| **Primary path** | **Manual export ingest** → normalized `wordstat_snapshot.json` |
| **Secondary path** | Pilot **official API** for batch of seeds (standalone JS module, not n8n) |
| **Operator workflow** | Operator runs Wordstat UI for declared seeds + region → drops file in session folder or `incoming/mig/` with manifest link |
| **Validation** | Ingest adapter checks columns, maps to snapshot schema, records `import_method: manual_export` |
| **No** | Auto-login automation, scheduled scraping |

### 3.5 Long-term

| Item | Decision |
|------|----------|
| **API batch job** | Scheduled acquisition module (`lib/keyword-intelligence/wordstat-api-client.js`) with quota tracking |
| **Credential storage** | Outside repo — env / secret store; **not** in session artifacts |
| **Idempotency** | Re-import creates new snapshot revision with `capture_id`, does not overwrite silently |
| **Region matrix** | Multiple `wordstat_snapshot` rows per session when operator requests multi-region charter |

### 3.6 Operator requirements (all Wordstat paths)

| Requirement | Detail |
|-------------|--------|
| **Account** | Operator-owned Yandex account with Wordstat access — MIG does not provision |
| **Region alignment** | Export region **must** match `scope.region` or explicit override documented in manifest |
| **Phrase list** | Export phrases **must** ⊆ session seed list + explicitly declared expansion list (operator-added, not MIG-generated) |
| **Provenance** | Snapshot records `exported_at`, `operator_id`, `file_name` or `api_request_id` |
| **Failure** | Missing file → session continues; SAFE UNKNOWN + optional `keyword_pass_status: wordstat_skipped` |

### 3.7 `wordstat_snapshot.json` shape (logical)

```json
{
  "schema_version": "0.1",
  "session_id": "mig-YYYYMMDD-xxxxxx",
  "capture_id": "ws-YYYYMMDD-HHMMSS",
  "import_method": "manual_export|api|operator_json",
  "region": "213",
  "region_label": "Москва",
  "period": "month|week|unknown",
  "source_account_ref": "opaque-operator-handle",
  "captured_at": "ISO-8601",
  "rows": [
    {
      "phrase": "натяжные потолки цена",
      "frequency_signal": {
        "shows": 12400,
        "shows_share": null,
        "clicks": null,
        "cpc": null,
        "competition": null,
        "signal_type": "shows",
        "raw_columns": {}
      },
      "keyword_id": "kw-mig-20260601-00001",
      "safe_unknown": []
    }
  ],
  "column_mapping": {
    "shows": "Количество запросов"
  },
  "safe_unknown": ["cpc column not present in export"],
  "evidence_grade": "operator|provider"
}
```

**Rules:**

- Store **all** columns from export in `raw_columns` when mapping uncertain.
- **Do not** compute derived metrics (CTR estimates, «opportunity score») in MIG.
- Null frequency → phrase still registered with `safe_unknown: ["frequency_not_in_export"]`.

---

## 4. Suggestion acquisition

### 4.1 Model

**Suggestions** are **ordered or unordered lists of strings** returned by an autocomplete endpoint or UI capture — **one list per (engine, seed, locale, device)** invocation.

```text
seed_query
    ↓
[operator-approved suggestion capture job]
    ↓
HTTP/API call OR manual copy-paste import
    ↓
suggestions_snapshot.json
    ↓
keyword_registry.json (one Keyword Object per distinct string)
```

### 4.2 Acquisition rules

| Rule | Detail |
|------|--------|
| **No recursive expansion** | Capturing suggestions for seed A **must not** auto-run suggestions for each returned string |
| **No clustering** | Store flat `suggestions[]` with `rank` if API provides order |
| **Dedup** | Registry dedupes by normalized phrase + `source_type`; preserve first-seen provenance |
| **Engine tag** | `yandex` \| `google` on artifact |
| **Evidence grade** | `provider` if API; `operator` if paste import |

### 4.3 `suggestions_snapshot.json` (logical)

```json
{
  "schema_version": "0.1",
  "session_id": "mig-YYYYMMDD-xxxxxx",
  "capture_id": "sg-YYYYMMDD-HHMMSS",
  "engine": "yandex",
  "seed_query": "натяжные потолки",
  "locale": "ru-RU",
  "device": "desktop",
  "captured_at": "ISO-8601",
  "import_method": "api|manual_paste",
  "suggestions": [
    { "rank": 1, "phrase": "натяжные потолки москва", "keyword_id": "kw-..." }
  ],
  "safe_unknown": [],
  "evidence_grade": "provider"
}
```

### 4.4 How suggestions become artifacts

1. **Capture** → `suggestions_snapshot.json` (SoT for that API response).
2. **Normalize** → upsert each `phrase` into `keyword_registry.json` with `source_type: suggestion`, `artifact_refs: [{ "role": "suggestions_snapshot", "path": "...", "capture_id": "..." }]`.
3. **Surface rollup** (optional) → append to `keyword_surface.json` under `surface_type: suggestion_api` for pack-friendly listing.
4. **Pack** → Search Demand section lists counts + sample strings + pointer to artifacts — **not** full dump if >50 phrases (registry is authoritative).

### 4.5 Phase suitability

| Phase | Suggestions |
|-------|-------------|
| **MVP** | **Out** — seeds only |
| **Phase 2** | Single-engine, single seed per pass; max **1** API call per seed without charter |
| **Phase 3** | Multi-seed batch file in request; still no recursive expansion |

---

## 5. Canonical Keyword Object

### 5.1 Identity

| Field | Required | Meaning |
|-------|----------|---------|
| `keyword_id` | **Yes** | Stable within session: `kw-{session_suffix}-{seq}` or content-hash id (document choice at implementation) |
| `phrase` | **Yes** | Exact captured string — trim only, no stemming |
| `phrase_normalized` | **O** | Lowercase + NFC for dedup only — **not** for display |
| `session_id` | **Yes** | Owning session |

### 5.2 Provenance

| Field | Required | Meaning |
|-------|----------|---------|
| `source` | **Yes** | Human label: `seed`, `serp_executed`, `serp_organic_title`, `serp_related`, `yandex_suggest`, `google_suggest`, `wordstat_export`, `wordstat_api`, `page_visible`, `manual_operator` |
| `source_type` | **Yes** | Enum: `seed` \| `serp` \| `suggestion` \| `wordstat` \| `website` \| `operator` |
| `capture_time` | **Yes** | ISO-8601 UTC |
| `region` | **O** | Aligns with `scope.region` or Wordstat region code |
| `locale` | **O** | BCP-47 when known |
| `engine` | **O** | `yandex` \| `google` \| null |

### 5.3 Frequency and evidence

| Field | Required | Meaning |
|-------|----------|---------|
| `frequency_signal` | **O** | Object — absent if not captured |
| `frequency_signal.signal_type` | When present | `shows` \| `clicks` \| `shows_share` \| `unknown` |
| `frequency_signal.value` | When present | Number or string as returned — no unit conversion |
| `frequency_signal.period` | **O** | `month` \| `week` \| `quarter` \| `unknown` |
| `frequency_signal.as_of` | **O** | Export/API timestamp |
| `evidence` | **O** | `{ "snippet": "...", "url": "...", "serp_position": 3 }` for SERP/website |
| `artifact_refs` | **Yes** | Array of `{ role, path, capture_id?, row_index? }` |
| `evidence_grade` | **Yes** | `operator` \| `provider` \| `extracted` |
| `safe_unknown` | **Yes** | Array — may be empty `[]` |

### 5.4 Full example

```json
{
  "keyword_id": "kw-mig-20260601-ce1557-00042",
  "session_id": "mig-20260601-ce1557",
  "phrase": "натяжные потолки цена москва",
  "phrase_normalized": "натяжные потолки цена москва",
  "source": "yandex_suggest",
  "source_type": "suggestion",
  "capture_time": "2026-06-01T14:22:00Z",
  "region": "213",
  "locale": "ru-RU",
  "engine": "yandex",
  "frequency_signal": null,
  "evidence": {
    "seed_query": "натяжные потолки",
    "suggestion_rank": 3
  },
  "artifact_refs": [
    {
      "role": "suggestions_snapshot",
      "path": "suggestions_snapshot.yandex-ce1557.json",
      "capture_id": "sg-20260601-142200"
    }
  ],
  "evidence_grade": "provider",
  "safe_unknown": ["frequency_not_captured"]
}
```

### 5.5 Registry container

**`keyword_registry.json`** is the session-level **index of Keyword Objects**.

| Field | Required |
|-------|----------|
| `schema_version` | **Yes** — `"0.1"` |
| `session_id` | **Yes** |
| `keywords` | **Yes** — array of Keyword Objects |
| `stats` | **O** — `{ "total": N, "by_source_type": {} }` |
| `safe_unknown` | **Yes** — session-level gaps |

**Dedup rule:** Same `phrase` + same `source_type` + same `engine` → merge `artifact_refs`; do not fork ids.

**Forbidden fields on Keyword Object:** `cluster_id`, `priority`, `intent`, `campaign`, `ad_group`, `recommended_bid`, `semantic_group`.

---

## 6. Artifact architecture

### 6.1 Layering

```text
keyword_registry.json          ← canonical Keyword Object index (required when pass runs)
keyword_surface.json           ← rollup by surface_type (optional convenience)
wordstat_snapshot.json         ← optional; 0..N per session
suggestions_snapshot.json      ← optional; 0..N per session
serp_result.json               ← upstream SoT (read-only for keyword pass)
website_snapshots.json         ← upstream for page_visible
```

### 6.2 Artifact registry

| Artifact | Required | Phase | Role |
|----------|----------|-------|------|
| `keyword_registry.json` | **When keyword pass executed** | Ph2+ | **SoT** for Keyword Objects |
| `keyword_surface.json` | **Optional** | Ph2+ | Human/pack-friendly rollup; derivable from registry |
| `wordstat_snapshot.json` | **Optional** | Ph2+ | Raw frequency table snapshot |
| `suggestions_snapshot.json` | **Optional** | Ph2+ | Per-invocation suggestion list |
| `keyword_pass_manifest.json` | **Optional** | Ph2+ | Pass metadata: seeds processed, skips, operator notes |

**MVP:** None of the above required — Query Set in pack + manifest mirrors seeds.

### 6.3 `keyword_surface.json` (logical)

Rollup **without** grouping into strategy buckets:

```json
{
  "schema_version": "0.1",
  "session_id": "mig-20260601-ce1557",
  "seed_queries": ["натяжные потолки"],
  "queries_executed": ["натяжные потолки москва"],
  "surfaces": [
    {
      "surface_id": "surf-001",
      "surface_type": "seed|serp_executed|serp_related|serp_organic|suggestion_api|wordstat|page_visible|operator",
      "engine": "yandex",
      "source_artifact": "serp_result.json",
      "strings": [],
      "keyword_ids": [],
      "captured_at": "ISO-8601",
      "evidence_grade": "extracted"
    }
  ],
  "safe_unknown": []
}
```

**Rule:** `strings[]` is denormalized cache; **`keyword_registry.json` wins** on conflict.

### 6.4 Relationships

```text
serp_result.json ──extract──► keyword_surface (serp_*)
                          └──► keyword_registry

suggestions_snapshot.json ──► keyword_registry

wordstat_snapshot.json ──► keyword_registry (frequency_signal populated)

website_snapshots.json ──► keyword_surface (page_visible)

keyword_registry.json ──project──► Research Pack sections
```

### 6.5 Session folder layout (Phase 2+)

```text
{session_id}/
  session_manifest.json
  serp_result.json
  competitors.json
  keyword_registry.json
  keyword_surface.json              ← optional
  wordstat/
    wordstat_snapshot.{capture_id}.json
  suggestions/
    suggestions_snapshot.{engine}.{capture_id}.json
  research_pack.draft.md
```

### 6.6 Future artifacts (charter only)

| Artifact | Purpose |
|----------|---------|
| `search_demand_notes.md` | Operator freeform — not SoT |
| `keyword_registry.revision.json` | Re-capture without deleting prior revision |
| Third-party API raw dumps | Vendor-specific; normalize to registry |

---

## 7. Research Pack integration

Pack remains **projection**; artifacts remain **SoT** per [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md).

### 7.1 New logical sections (stable ids)

Add to pack contract evolution — populated when keyword pass runs:

| Section id | Phase | Required when |
|------------|-------|---------------|
| `keyword_observations` | Ph2+ | Keyword pass executed |
| `search_demand` | Ph2+ | Any frequency or Wordstat snapshot present |
| `frequency_signals` | Ph2+ | `wordstat_snapshot` or SERP volume feature present |

**MVP:** Sections **absent**; gaps in **SAFE UNKNOWN** — not fabricated.

### 7.2 `keyword_observations` (projection)

| Content | Source |
|---------|--------|
| Seed and executed query lists | manifest / registry |
| Count by `source_type` | registry stats |
| Representative phrase samples (max 20 per type) | registry |
| Pointers | `artifact_registry.keyword_registry`, `keyword_surface` |
| **No** clusters, **no** «top keywords» ranking | — |

### 7.3 `search_demand` (projection)

| Content | Source |
|---------|--------|
| Statement of whether demand **frequency** was captured | manifest `keyword_pass_status` |
| Region / period used for Wordstat | `wordstat_snapshot` |
| Table sample: phrase + raw shows (max 30 rows) | snapshot |
| Explicit «not captured» bullets | SAFE UNKNOWN |

**Forbidden:** «Commercial demand is high», intent labels, recommended spend.

### 7.4 `frequency_signals` (projection)

Dedicated subsection when numeric signals exist:

| Field | Meaning |
|-------|---------|
| `signal_provenance` | `wordstat_export` \| `wordstat_api` |
| `signals[]` | `{ keyword_id, phrase, signal_type, value, period, as_of }` |
| `unmapped_phrases` | Export rows that did not match any seed |

### 7.5 SAFE UNKNOWN rules (keyword-specific)

| Situation | Pack / manifest entry |
|-----------|------------------------|
| Keyword pass not run | «Keyword Intelligence pass not executed — search demand unknown» |
| Suggestions skipped | «Autocomplete suggestions not captured» |
| Wordstat skipped | «Wordstat frequency evidence not captured for this session» |
| Partial Wordstat (some seeds missing) | List missing seeds |
| Region mismatch | «Wordstat region (X) does not match scope.region (Y) — operator verified: yes/no» |
| API quota exceeded | «Wordstat API capture incomplete — see wordstat_snapshot safe_unknown» |

**Approved pack rule:** SAFE UNKNOWN section **must not** be empty; keyword gaps **must** appear if pass was skipped or partial.

### 7.6 Artifact registry extensions

| Artifact key | Path |
|--------------|------|
| `keyword_registry` | `keyword_registry.json` |
| `keyword_surface` | `keyword_surface.json` |
| `wordstat_snapshots` | `wordstat/*.json` or single file |
| `suggestions_snapshots` | `suggestions/*.json` |

### 7.7 Query Set interaction

Existing **Query Set** section remains **required** — seeds + executed queries.  
Keyword sections **complement** Query Set; they **do not** replace it.  
Query Set `query_notes` may reference keyword pass status — **no** semantic clustering in notes.

---

## 8. n8n architecture

Aligned with [REPORT-mig-runtime-design-metabot-patterns-v1.md](../reports/REPORT-mig-runtime-design-metabot-patterns-v1.md) and Website Acquisition §8.

### 8.1 Inside n8n

| Concern | Role |
|---------|------|
| **Worker route trigger** | After SERP (+ optional website) — `acquiring_keywords` stage |
| **Operator gates** | Telegram confirm before suggestion API spend |
| **Stage / Sheets updates** | `keyword_pass_status`, counts |
| **Thin Code node** | `require()` → `run-keyword-pass.js` |
| **Manual import webhook** | Optional: notify operator Wordstat file received |

### 8.2 Inside JS modules (`projects/mig/lib/keyword-intelligence/`)

| Module (proposed) | Responsibility |
|-------------------|----------------|
| `build-seed-plan.js` | Seeds from request + manifest |
| `ingest-serp-surfaces.js` | SERP-related + organic strings → registry |
| `ingest-website-visible.js` | Page titles/H1/meta from snapshots |
| `capture-suggestions.js` | API call wrapper — rate limit, single depth |
| `ingest-wordstat-export.js` | CSV/XLSX → snapshot |
| `wordstat-api-client.js` | Phase 2+ pilot — **not** n8n |
| `merge-registry.js` | Dedup + artifact_refs |
| `write-keyword-artifacts.js` | Persist §6 layout |
| `run-keyword-pass.js` | Orchestrate plan → captures → registry |
| `session-spine/build-research-pack.js` | **Extend** — project keyword sections |

**Pattern:** Same as `competitor-discovery/` and `website-acquisition/` — CLI-testable, n8n invokes one entrypoint.

### 8.3 Outside MIG

| Concern | Where |
|---------|--------|
| **Wordstat UI** | Operator browser |
| **OAuth / API keys** | Secret store — not in repo |
| **ORCA** | Consumes approved pack + registry read-only |
| **MetaBOT SEO graphs** | Unrelated content generation |

### 8.4 n8n anti-patterns

| Do not | Why |
|--------|-----|
| Wordstat login automation in graph | Brittle, ToS risk |
| Recursive suggestion loops in n8n | Unbounded cost |
| Clustering Code node | R1/R2 violation |
| Store full registry in Telegram message | Use path + counts |

---

## 9. Operator workflow — canonical flow

```text
1. Submit Research Request
      scope.region, queries.seed_queries[], capture_profile.keyword_pass (Ph2+)
        ↓
2. Search Acquisition
      serp_result.json, queries_executed recorded
        ↓
3. HITL — SERP acceptable?
        ↓
4. (Optional) Competitor Discovery → Website Acquisition
        ↓
5. Keyword Intelligence Pass
      5a. Register seeds + executed queries → keyword_registry.json
      5b. Extract SERP surfaces (if enabled)
      5c. (Ph2) Operator uploads Wordstat export OR API job runs
      5d. (Ph2) Approved suggestion capture per seed
      5e. (Ph2) Ingest page_visible from website snapshots
        ↓
6. HITL — Review keyword summary (counts, missing Wordstat, blocked suggestions)
        ↓
7. Research Pack draft
      keyword_observations + search_demand + frequency_signals (as applicable)
        ↓
8. review → approved → ORCA handoff (human)
```

### 9.1 MVP shortcut

```text
task file → spine (SERP) → draft pack
  Query Set = seeds only
  SAFE UNKNOWN: «Search demand frequency not captured; Keyword Intelligence pass not executed»
```

### 9.2 Phase 2 happy path

```text
seed query(s) in request
  → acquire keyword surfaces (SERP extract + optional suggestions)
  → operator Wordstat export for same seeds + region
  → ingest → wordstat_snapshot.json
  → build keyword_registry.json
  → draft pack with demand tables
```

### 9.3 Workload controls

| Control | Default |
|---------|---------|
| Suggestion API calls / session | 5 seeds max without charter |
| Wordstat imports / session | 3 snapshot files max |
| Phrases in registry / session | 2000 hard cap (operator alert) |
| Auto-suggest without HITL | **Forbidden** |

---

## 10. Roadmap

### 10.1 Keyword Intelligence MVP

**Goal:** Honest demand boundary without new infra.

| # | Deliverable | Acceptance |
|---|-------------|------------|
| 1 | Documented contract (this file) | Operator-readable |
| 2 | Query Set discipline in spine | Seeds + executed in pack |
| 3 | SAFE UNKNOWN template for missing demand | Every draft pack |
| 4 | Manifest optional `keyword_pass_status: not_run` | Explicit |

**Explicitly not in MVP:** registry file, Wordstat, suggestions API, keyword pack sections.

### 10.2 Phase 2

| # | Item |
|---|------|
| 1 | `keyword_registry.json` + ingest from SERP surfaces |
| 2 | `ingest-wordstat-export.js` + `wordstat_snapshot` schema |
| 3 | `keyword_surface.json` rollup |
| 4 | Pack sections: `keyword_observations`, `search_demand`, `frequency_signals` |
| 5 | Single-engine suggestion capture (pilot) |
| 6 | `verify-keyword-intelligence-v0.mjs` fixtures |
| 7 | n8n Worker hook for `groundtruth_run` |

### 10.3 Phase 3

| # | Item |
|---|------|
| 1 | Wordstat API batch module |
| 2 | Multi-seed suggestion batch (still no recursion) |
| 3 | `page_visible` bulk ingest from website pass |
| 4 | Registry revisioning |
| 5 | ORCA handoff bundle includes `keyword_registry.json` as required artifact |

### 10.4 Explicitly out of scope (all phases unless charter)

- Clustering, intent taxonomy, semantic core  
- PPC structure, bid recommendations  
- Query generation inside MIG  
- Wordstat browser bots as default  
- Third-party SEO APIs without charter  

---

## 11. ORCA handoff — keyword evidence

Minimum additional ORCA-readable facts (human-delivered bundle):

| Deliverable | When |
|-------------|------|
| `keyword_registry.json` | Phase 2+ when pass executed |
| `wordstat_snapshot.json` | When frequency captured |
| Pack sections §7 | Projections with artifact pointers |

ORCA **may:**

- Cluster phrases by intent  
- Prioritize by volume and business rules  
- Build PPC and SEO structures  
- Propose **new** seed queries back to operator for a **new** MIG session  

ORCA **must not:**

- Rewrite MIG artifacts to embed strategy  
- Treat missing Wordstat as zero volume without SAFE UNKNOWN  

---

## 12. Architecture decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| **KI-01** | `keyword_registry.json` is Keyword Object SoT | Pack is projection; avoids markdown drift |
| **KI-02** | Wordstat Phase 2 = manual export first | Lowest compliance risk; API pilot parallel |
| **KI-03** | No suggestion recursion | Prevents runaway acquisition |
| **KI-04** | SERP strings ingested, not re-fetched | Reuse Search Acquisition investment |
| **KI-05** | Frequency stored raw | ORCA owns interpretation |
| **KI-06** | MVP = Query Set + SAFE UNKNOWN only | Ruthless scope |
| **KI-07** | Keyword pass in JS, not n8n logic | Testability; MetaBOT pattern |
| **KI-08** | `keyword_surface.json` optional | Convenience rollup; registry wins |
| **KI-09** | Stable pack section ids early | Avoid contract churn |
| **KI-10** | Browser Wordstat discouraged | ToS/account risk; document escape hatch only |

---

## 13. Risks

| Risk | Mitigation |
|------|------------|
| R1/R2 bleed (clustering in MIG) | boundaries.md; reject forbidden fields; code review |
| Wordstat ToS / API access denied | Manual export path; SAFE UNKNOWN |
| Suggestion API rate limits | Per-session caps; operator gate |
| Phrase explosion from surfaces | Registry cap 2000; pack shows samples only |
| Operator region mismatch | Validation warning + manifest flag |
| Duplicate phrases across sources | Dedup with merged `artifact_refs` |
| ORCA treats missing frequency as zero | Handoff doc + pack SAFE UNKNOWN |
| Export column drift | `raw_columns` + `column_mapping` + safe_unknown |

---

## 14. SAFE UNKNOWN — authoritative gaps

| Unknown | Declaration |
|---------|-------------|
| Wordstat API availability for operator | **UNKNOWN** — may be export-only for extended period |
| Yandex Suggest unofficial API stability | **UNKNOWN** — prefer manual paste fallback |
| Google suggest locale parity | **UNKNOWN** — secondary engine |
| Legal review of browser Wordstat automation | **UNKNOWN** — not default |

---

## 15. Related documents

| Document | Role |
|----------|------|
| [boundaries.md](../boundaries.md) | MIG vs ORCA matrix |
| [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) | Pack sections — extend in future pack revision |
| [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) | `queries.seed_queries[]` |
| [REPORT-mig-data-acquisition-architecture-v1.md](../reports/REPORT-mig-data-acquisition-architecture-v1.md) | Superseded keyword section |
| [mig-website-acquisition-architecture-v1.md](mig-website-acquisition-architecture-v1.md) | `page_visible` channel |

---

## 16. Recommended next step (architecture only)

1. Add `keyword_pass_status` to session manifest schema (design stub — no implementation in this charter).  
2. When Phase 2 starts: implement `ingest-serp-surfaces.js` + `keyword_registry.json` schema v0.1.  
3. Draft pack builder extension spec referencing §7 section ids.  
4. Operator one-pager: Wordstat export column expectations for ingest adapter.

**No implementation, credentials, or API setup in this document.**
