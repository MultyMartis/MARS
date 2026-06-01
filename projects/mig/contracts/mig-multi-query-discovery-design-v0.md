# MIG Multi-Query Discovery Design v0

**Status:** **documented** — design-only evolution spec for MIG discovery v0.3.  
**Not:** implementation, JSON Schema registry update, provider integration, query automation, ORCA methodology, or runtime product.

**Supersedes:** Nothing — extends [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) semantics for multi-query sessions without bumping discovery contract major version until implementation lands.

**Upstream:** [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md), [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md), [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md).

**Evidence base (v0.2b):** Session spine runs `discoverFromSerp(serpResult)` once per session; `rule_repeated_domain` is defined in contract but **cannot fire meaningfully** when only one SERP artifact and one `query` exist. Partial hook: `options.queries_executed` in `discover-from-serp.js` expects per-row `row.query` tags that v0.1 `serp_result.json` does not populate.

**Consumers (future):** aggregation module, manifest/schema v0.2+, pack builder, verification fixtures — **not** implemented by this document.

---

## 1. Multi-Query Discovery — definition

### 1.1 What it is

**Multi-Query Discovery** is a **session-level competitor discovery pass** that consumes **N normalized SERP captures** (one per **declared scope query**) and produces **one consolidated** `competitor_observations` section / `competitors.json` with **cross-query entity consolidation** and **query coverage metadata**.

```text
Research Request (queries provided by operator)
    ↓
Research Session
    ↓
N × SERP capture → N × serp_result (or serp bundle)
    ↓
Multi-Query Discovery Pass          ← this design
    ↓
competitors.json (consolidated)
    ↓
Research Pack
```

### 1.2 Problem solved

| Limitation (v0.2b) | Multi-Query Discovery (v0.3) |
|--------------------|--------------------------------|
| One `query` / one organic list | Many queries → broader surface sampling |
| `queries_seen` ≈ one entry per entity | Accurate `queries_seen` across scope |
| `rule_repeated_domain` inert (≥2 distinct queries never occur) | Recurrence signal when same domain ranks on multiple queries |
| Competitor set biased to single intent surface | Entities visible only on variant queries can enter set |
| No machine-readable “which queries ran / failed” | `discovery_coverage` block for audit and SAFE UNKNOWN |

### 1.3 New signal (MIG layer only)

| Signal | Meaning | Not |
|--------|---------|-----|
| **Cross-query domain recurrence** | Same registrable domain matched organic rules on ≥2 **executed** queries | “Market leader” or strategic priority |
| **Per-query evidence rows** | `surface_detail.query` + `artifact_ref` pointing to query-specific SERP slice | Semantic intent clustering |
| **Query coverage** | Which declared queries produced capturable SERP vs skipped/failed | Completeness of “the market” |
| **Surface coverage across queries** | e.g. organic on Q1, paid on Q3 for same entity | Offer quality or threat |
| **Strengthened `discovery_strength: repeated`** | Factual recurrence per §5 of discovery contract | Competitive scoring |

### 1.4 Outside MIG scope (unchanged)

- Query **generation**, expansion, or keyword research automation
- SERP **provider** selection, rate limits, scheduling (transport — future Worker)
- Landing analysis, deep research, directory/maps standalone crawl
- Business interpretation: direct vs indirect competitor, relevance, strategy
- ORCA competitive landscape synthesis (R2)
- Competitor **scoring** or rank-by-importance
- LLM-invented entities without surface evidence

**Normative boundary (unchanged):**

> **MIG acquires reality. ORCA interprets reality.**

---

## 2. Query model (minimum v0.3)

### 2.1 Principles

1. **Queries are provided** — operator or upstream adapter supplies strings; MIG does not invent queries.
2. **Stable identity** — each query has a `query_id` for aggregation keys; display string may duplicate across roles only if operator explicitly duplicates (discouraged; audit via `query_id`).
3. **Scope binding** — all queries in one multi-query discovery pass share the same session `scope` (region, engine, device) unless a future charter splits sessions (out of v0.3).

### 2.2 Query record (minimum)

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `query_id` | **Yes** | string | Stable within session — pattern `q{nn}` e.g. `q01` |
| `query_text` | **Yes** | string | Exact capture string sent to SERP |
| `role` | **Yes** | enum | See §2.3 |
| `locale_hint` | **O** | string | e.g. `ru-RU` — copy-only for pack; no NLP |
| `geo_variant` | **O** | object | `{ city, region_override }` when geographic variant differs from session default |
| `execution_status` | **O** | enum | Set at capture time: `pending` \| `captured` \| `failed` \| `skipped` |
| `skip_reason` | **O** | string | Human/operator reason when `skipped` |

### 2.3 Query roles (v0.3 enum)

| `role` | Use | Example |
|--------|-----|---------|
| `primary` | Main commercial intent | «аренда манипулятора Краснодар» |
| `supporting` | Adjacent intent same niche | «услуги автокрана Краснодар» |
| `wording_variant` | Same intent, different phrasing | «манипулятор в аренду краснодар» |
| `commercial_variant` | Transactional modifier | «цена аренды манипулятора краснодар» |
| `geo_variant` | Geo-qualified variant | «аренда манипулятора краснодарский край» |

**Minimum v0.3:** at least one `primary`; total **executed** queries **≥ 1**. Multi-query discovery **recommended** when **≥ 2** queries with `execution_status: captured`.

**v0.3 does not require** all role types — only `primary` + `role` enum discipline.

### 2.4 Request / manifest mapping

| Source | v0.3 target |
|--------|-------------|
| `queries.seed_queries[]` | Seeds **all** `query_text` values; adapter assigns `query_id` + default `role: primary` for first, `supporting` for rest unless operator overrides |
| `queries.query_used` | **Deprecated for multi-query** — keep for v0.1 compat as `queries_executed[0]` mirror |
| New `queries.query_set[]` | Array of query records (§2.2) — **canonical** for v0.3 sessions |
| New `queries.queries_executed[]` | Ordered list of `query_id` that produced SERP artifacts |
| New `queries.queries_declared[]` | All `query_id` in scope for discovery |

**Single-query compat:** `query_set` length = 1 → degenerate multi-query (aggregation rules still apply; `rule_repeated_domain` needs ≥2 captures to fire).

### 2.5 Explicit non-goals

- Automatic query suggestions from SERP
- Query clustering or intent labels
- Per-query different `search_engine` / `device` in one session (future charter → split session)

---

## 3. SERP aggregation model

### 3.1 Canonical strategy: **per-query artifacts + session index**

**Normative (v0.3):** Do **not** merge raw provider payloads into one blob at capture time. Normalize **each** query to its own artifact, then aggregate **at discovery time** into one competitor section.

```text
queries_declared [q01, q02, q03]
    ↓
capture (per query)
    ↓
serp_results/q01.json
serp_results/q02.json
serp_results/q03.json
    ↓
serp_index.json (manifest pointer)
    ↓
discoverFromSerpBundle(serp_index, rules)
    ↓
competitors.json
```

**Rationale:** preserves per-query evidence grade, replay, and SAFE UNKNOWN; matches Research Pack artifact registry pattern.

### 3.2 `serp_index.json` (new session artifact)

| Field | Required | Meaning |
|-------|----------|---------|
| `schema_version` | **Yes** | `"0.1"` |
| `session_id` | **Yes** | Session id |
| `aggregation_model` | **Yes** | `"per_query_files"` |
| `default_scope` | **Yes** | Copy of manifest `scope` |
| `entries` | **Yes** | Array of `{ query_id, query_text, role, artifact_path, captured_at, source_mode, status }` |
| `safe_unknown` | **O** | Index-level gaps (failed captures) |

**Backward compatibility:** Legacy sessions with only `serp_result.json` are treated as **implicit** single-entry index:

```json
{
  "aggregation_model": "legacy_single",
  "entries": [{ "query_id": "q01", "artifact_path": "serp_result.json", "status": "captured" }]
}
```

Discovery entrypoint **must** accept both shapes.

### 3.3 Aggregation pass ordering

1. Load `serp_index` (or synthesize legacy).
2. For each `entry` with `status: captured`, load normalized SERP, run **per-query slice** of rules (organic top-N, paid, local pack when present).
3. Emit **candidate hits**: `{ query_id, query_text, domain_key, surface_kind, row, artifact_ref, grade }`.
4. **Consolidate** candidates → competitor objects (§4).
5. Apply **post-consolidation** rules: `rule_repeated_domain`, `rule_multi_surface`.
6. Compute **coverage** (§6).

### 3.4 Alternative considered — rejected for v0.3

| Approach | Verdict |
|----------|---------|
| Single `serp_result.json` with `organic_results[].query` tags | Allowed as **compat shim** only; not canonical — easy to break evidence refs |
| Concatenate all organic into one list at normalize time | **Reject** — loses per-query grade and positions |

### 3.5 SERP capture failure

- Failed query → no file; `execution_status: failed` on query record; index entry `status: failed`.
- Discovery **continues** with captured subset; coverage `partial`; SAFE UNKNOWN lists failed `query_id`s.
- **Zero** captured queries → empty competitors + SAFE UNKNOWN (same discipline as v0.2b empty organic).

---

## 4. Entity consolidation

### 4.1 Identity keys (priority order)

| Priority | Key | When |
|----------|-----|------|
| 1 | `primary_domain` (registrable, www-stripped) | URL present |
| 2 | `domain_cluster_id` | Future — **not** v0.3 |
| 3 | `name_key` | `normalize(display_name)` lowercased, punctuation-stripped | No domain; local pack name-only |
| 4 | `manual_seed_id` | Seed from `signals[]` before match |

**Normative:** Same domain across queries → **one** `competitor_id`. Different domains → **never** merge solely because display names look similar (dedup uncertainty → entity `safe_unknown`).

### 4.2 Merge rules

When a candidate hit matches an existing entity:

| Field | Merge behavior |
|-------|----------------|
| `competitor_id` | **Immutable** — first creation wins |
| `display_name` | Keep first non-empty unless new hit has longer observed title on **primary** query — configurable **off** in v0.3 (keep first for simplicity) |
| `primary_domain` | Set if null; else unchanged |
| `domains_observed` | Union |
| `surface_types` | Union of type ids |
| `discovery_sources` | Append unique `(source_kind, artifact_ref, query_id)` |
| `queries_seen` | Union of `query_text` (or `query_id` in evidence — see §7) |
| `first_seen_query` | Earliest capture order in `queries_executed` |
| `discovery_rules_fired` | Union |
| `evidence[]` | Append per hit (cap optional **future**; v0.3: no cap, operator review) |
| `evidence_grade` | Pessimistic (worst) across items |
| `discovery_strength` | Recompute after pass (§5) |
| `capture_time` | `min(observed_at)` |
| `updated_at` | `max(observed_at)` |

### 4.3 Deduplication within one query

Same domain twice in one organic list (rare): **one** evidence row per (domain, position) — keep best (lowest) position; do not duplicate rules except note in `discovery_notes` if needed.

### 4.4 `exclude_duplicate_entity`

Unchanged from discovery contract — merge into existing id by domain or `name_key`.

### 4.5 Conflicts (SAFE UNKNOWN, not ORCA)

| Conflict | Handling |
|----------|----------|
| Same domain, materially different `display_name` | Single entity; entity `safe_unknown`: «name variant unresolved» |
| Same name, different domains | **Two** entities |
| Seed domain matches discovered domain | Merge; `manual_seed: true`; clear `seed_only` when surface evidence exists |

---

## 5. `rule_repeated_domain` — design (v0.3)

### 5.1 Purpose

Objective signal: registrable domain appeared in **normalized organic top-N** on **≥ 2 distinct executed queries** within the same discovery pass.

### 5.2 Trigger conditions (normative)

| Condition | Required |
|-----------|----------|
| `queries_executed` with `status: captured` | **≥ 2** |
| Domain `d` | Matched `rule_serp_organic_top_n` on query `q_i` and `q_j`, `i ≠ j` |
| Same session scope | Same `session_id` |
| Exclusions | `exclude_own_domain`, `exclude_search_engine` applied before count |

**Does not fire when:**

- Only one SERP captured (legacy v0.2b path) — strength stays `single` unless `rule_multi_surface` applies.
- Domain appears twice on **same** query only — not recurrence across queries.
- Domain only in paid/local on one query and organic on another — **does not** count for `rule_repeated_domain` (organic-only rule per contract §5.1); may still contribute to `rule_multi_surface`.

### 5.3 Thresholds

| Constant | Default | Notes |
|----------|---------|-------|
| `MIN_DISTINCT_QUERIES` | **2** | Matches contract |
| `top_n` | **10** | From rules config |
| Paid/local recurrence | **Out of scope** for this rule id | Future separate rule ids if chartered |

### 5.4 Evidence impact

- Append **one evidence item per (query, position)** — do not collapse cross-query rows.
- Each `surface_detail` **must** include: `query_id`, `query_text`, `position`, `url`, `title`, `snippet`.
- `artifact_ref`: `serp_results/{query_id}.json` or legacy `serp_result` for q01.
- Grade: per underlying SERP `source_mode` (pessimistic at entity level).

### 5.5 `discovery_strength` evolution

| State | Set when |
|-------|----------|
| `single` | Default; one query or no cross-query recurrence |
| `repeated` | `rule_repeated_domain` fired; **does not downgrade** if `multi_surface` also fires |
| `multi_surface` | ≥2 surface kinds on consolidated entity (any queries) — **takes precedence** over `repeated` for enum value when both fire (per existing implementation pattern) |

**Order of evaluation:** per-query hits → merge → `rule_multi_surface` → `rule_repeated_domain`.

### 5.6 Pack / artifact representation

| Location | Addition |
|----------|----------|
| `discovery_rules_fired` | Include `rule_repeated_domain` when fired |
| `queries_seen` | All queries where domain matched top-N organic |
| Optional `recurrence` | `{ "distinct_query_count": 3, "query_ids": ["q01","q03"] }` — **optional** v0.3 field on competitor object |
| Markdown table | Optional column «Queries» = count or joined ids — representation only |

**No** narrative like «strong competitor» in MIG output.

---

## 6. Query coverage model

### 6.1 Section-level: `discovery_coverage` (new, inside `competitor_observations`)

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `queries_declared` | **Yes** | string[] | `query_id` list in scope |
| `queries_executed` | **Yes** | string[] | Captured SERP available |
| `queries_missing` | **Yes** | string[] | Declared but not captured (`failed` + `skipped` + `pending`) |
| `query_coverage` | **Yes** | enum | `full` \| `partial` \| `none` |
| `surface_coverage` | **O** | object | Per-surface tallies (below) |

**`query_coverage` enum:**

| Value | Condition |
|-------|-----------|
| `full` | `queries_missing` empty and ≥1 executed |
| `partial` | Some executed, some missing |
| `none` | Zero executed |

### 6.2 `surface_coverage` (optional object)

| Key | Meaning |
|-----|---------|
| `organic_queries_with_results` | Count of executed queries with ≥1 organic row after normalize |
| `local_pack_captured_queries` | Queries with non-empty local pack body |
| `paid_visible_queries` | Queries with paid/ad blocks |
| `rules_blocked` | e.g. `{ "rule_local_pack_present": ["q02"] }` when pack absent |

### 6.3 Entity-level

| Field | Meaning |
|-------|---------|
| `queries_seen` | **Yes** (existing) — query **text** or parallel `query_ids_seen[]` **optional** v0.3 |
| `queries_missing` | **No** at entity level — section only |

### 6.4 Link to `section_coverage`

Existing enum (`complete` \| `partial` \| `minimal` \| `unknown`) **remains**. Mapping:

| `query_coverage` | Typical `section_coverage` |
|------------------|----------------------------|
| `full` + competitors | `complete` or `partial` (grade-dependent) |
| `partial` | `partial` |
| `none` | `minimal` |

**Both** must be present in v0.3 packs when multi-query enabled.

---

## 7. Research Pack integration (extensions only)

### 7.1 Query Set section

| Field | Change |
|-------|--------|
| `seed_queries` | Keep |
| `queries_executed` | **Required** array of strings (text or ids — document as text in v0.3 pack markdown, ids in JSON) |
| `query_set` | **O** — full query records for audit |
| `query_notes` | Unchanged |

### 7.2 Competitor Observations section

| Field | Change |
|-------|--------|
| `discovery_coverage` | **New** §6 |
| `query_set_ref` | From single string → **session query set id** or joined primary query text; legacy: single string still valid |
| `competitors[].recurrence` | **O** §5.6 |
| `competitors[].query_ids_seen` | **O** parallel to `queries_seen` |

### 7.3 New observation types (factual)

- «Domain X appeared in organic top-N on queries q01, q03» — table or bullet from `recurrence`
- «Query q02 SERP capture failed — entities from q02 not represented»

### 7.4 New evidence fields

`surface_detail.query_id`, `surface_detail.query_text` on all multi-query evidence items.

### 7.5 New SAFE UNKNOWN scenarios

| Case | Example entry |
|------|----------------|
| Partial query capture | «Queries q02, q04 not captured — discovery coverage partial» |
| Repeated-domain ineligible | «Only one SERP captured — cross-query recurrence not evaluated» |
| Role mismatch | «Declared 5 queries; 2 skipped by operator — see query_set» |
| Index/artifact drift | «serp_index lists q03 but file missing» |
| Legacy session | «Multi-query coverage not computed — single serp_result.json session» |

### 7.6 SERP Observations section

- **Upstream** remains authoritative per query file.
- Pack may add **summary** table: query_id | captured_at | organic_count | grade — **optional** markdown; not SoT.

**No redesign** of pack lifecycle, grades philosophy, or approval gates.

---

## 8. Artifact evolution

### 8.1 `competitors.json`

| Change | Compat |
|--------|--------|
| `competitor_observations.discovery_coverage` | Optional — old validators pass |
| `competitor_observations.competitors[].recurrence` | Optional |
| `competitor_observations.competitors[].query_ids_seen` | Optional |
| `discovery_mode` on envelope | **O** `"single"` \| `"multi_query"` — default infer from index |

Envelope `schema_version` stays **`0.1`** until required fields added → then bump **`0.2`**.

### 8.2 `session_manifest.json`

| Change | Compat |
|--------|--------|
| `queries.query_set[]` | Optional |
| `queries.queries_executed[]` | Optional; mirror from index |
| `artifacts.serp_index` | `"serp_index.json"` |
| `artifacts.serp_results_dir` | `"serp_results/"` |
| `artifacts.serp_result` | **Retain** for legacy single-query |
| `competitor_discovery.discovery_mode` | Optional |
| `competitor_discovery.query_coverage` | Optional enum |

Proposed schema file: `session-manifest-v0.2.schema.json` — **additive** to v0.1.

### 8.3 `serp_result.json`

- **Unchanged** for legacy path.
- New per-query files: same schema as `serp-result-v0.1` with **required** `query_id` field (additive property — optional in schema until v0.2 schema wave).

### 8.4 Future artifacts

| Artifact | Role |
|----------|------|
| `serp_index.json` | Discovery input manifest |
| `serp_results/{query_id}.json` | Normalized SERP per query |
| `discovery_pass_log.json` | **Future** — rule hit audit; not v0.3 minimum |

### 8.5 Backward compatibility rules

1. Single `serp_result.json` sessions **must** run through discovery without migration.
2. `discoverFromSerp(serpResult)` **remains** public API — wrapper calls bundle path with synthetic index.
3. Packs without `discovery_coverage` → ORCA treats as «single-query session» (no cross-query recurrence claims).
4. Do **not** rename `competitor_id` when adding queries to same session (resume adds captures, same ids).

---

## 9. ORCA implications

### 9.1 What ORCA gains (read-only facts)

| Input | Use in R2 |
|-------|-----------|
| `discovery_coverage` | Know whether competitor set is query-complete |
| `queries_seen` / `recurrence` | Weight **observed** recurrence — still not «importance» |
| Per-query evidence | Trace which wording surfaced which domain |
| `rule_repeated_domain` in audit trail | Objective cross-query signal |
| Partial capture SAFE UNKNOWN | Avoid overfitting to one query |

### 9.2 What ORCA still must infer

- Strategic competitor set and priority
- Direct vs indirect relationships
- Whether recurrence implies demand vs SEO strength
- Whether to ignore aggregators/informational surfaces
- Market completeness beyond MIG capture
- Campaign or positioning recommendations

### 9.3 R1/R2 boundary (strict)

| MIG (R1) | ORCA (R2) |
|----------|-----------|
| «Domain D on queries Q1,Q3 in top-10 organic» | «D is a primary local competitor» |
| `query_coverage: partial` | «We have enough SERP breadth for strategy» |
| `discovery_strength: repeated` | «Pursue conquest campaign against D» |

ORCA **must not** treat `repeated` or `multi_surface` as business scoring — per [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) §5.3, §9.2.

---

## 10. Implementation readiness — backlog

Precise artifacts after this design (no code in this task):

| # | Artifact | Path (proposed) | Purpose |
|---|----------|-----------------|---------|
| 1 | Multi-query design (this doc) | `contracts/mig-multi-query-discovery-design-v0.md` | SoT for v0.3 |
| 2 | SERP index schema | `schemas/serp-index-v0.1.schema.json` | Validate `serp_index.json` |
| 3 | SERP result schema bump | `schemas/serp-result-v0.2.schema.json` | Optional required `query_id` |
| 4 | Session manifest v0.2 | `schemas/session-manifest-v0.2.schema.json` | `query_set`, artifacts |
| 5 | Competitors schema bump | `schemas/competitors-v0.2.schema.json` | `discovery_coverage`, optional recurrence |
| 6 | Query set normalizer | `lib/session-spine/normalize-query-set.js` | Build `query_set` from intake |
| 7 | Per-query SERP writer | `lib/session-spine/write-serp-bundle.js` | Index + directory layout |
| 8 | Aggregation module | `lib/competitor-discovery/discover-from-serp-bundle.js` | Multi-query pass |
| 9 | Refactor | `discover-from-serp.js` | Per-query slice + delegate to bundle |
| 10 | Spine orchestration | `run-session-spine.js` | Loop captures or accept pre-built bundle |
| 11 | Pack builder | `build-research-pack.js` | Coverage block, query table |
| 12 | Manifest finalize | `create-manifest.js` | `queries_executed`, discovery_mode |
| 13 | Rules config note | `config/competitor-discovery-rules-v0.json` | Document `MIN_DISTINCT_QUERIES` |
| 14 | Unit tests | `test/test-payload-multi-query-discovery-v0.1.json` | Golden 3-query merge + repeated domain |
| 15 | Verification | `tools/verify-multi-query-discovery-v0.mjs` | Index + coverage + rule firing |
| 16 | Intake (future) | `validate-intake.js` / request contract addendum | Accept `query_set` overrides |
| 17 | Contract cross-link | `mig-competitor-discovery-contract-v0.md` §10 addendum | Reference v0.3 when implemented |
| 18 | Operator doc | `incoming/mig/README.md` snippet | How to supply multi-query task files |

**Recommended implementation order:** 2 → 6 → 7 → 8 → 9 → 12 → 11 → 14 → 15 → 1 (schema publication) → 16.

**Explicitly not in v0.3 backlog:** OpenRouter, provider scheduler, landing, deep research, ORCA pack changes, query generation.

---

## 11. Architecture decisions

| ID | Decision | Rationale |
|----|----------|-----------|
| AD-1 | Per-query SERP files + index | Evidence traceability |
| AD-2 | Discovery-time aggregation | Avoid destructive merge at normalize |
| AD-3 | Domain-first identity | Matches existing `discover-from-serp.js` |
| AD-4 | `rule_repeated_domain` organic-only across queries | Aligns with contract §5.1 |
| AD-5 | `discovery_coverage` on section, not pack root | Keeps competitor pass cohesive |
| AD-6 | Legacy `serp_result.json` supported indefinitely | v0.2b sessions remain valid |
| AD-7 | No query automation in v0.3 | Charter boundary |
| AD-8 | `discovery_strength` enum unchanged | ORCA stability |

---

## 12. SAFE UNKNOWN (design-level)

| Topic | Status |
|-------|--------|
| Provider multi-capture scheduling | **UNKNOWN** — out of design |
| Max queries per session | **UNKNOWN** — recommend soft limit 10 in operator doc; not enforced here |
| Evidence row cap per entity | **UNKNOWN** — v0.3 uncapped |
| `name_key` normalization locale rules | **UNKNOWN** — use simple lowercase trim v0.3 |
| Whether paid cross-query recurrence needs new rule id | **Deferred** — not v0.3 |
| REPORT v0.2b on disk | Referenced in charter; **not found** under `projects/mig/reports/` — behavior inferred from `verify-competitor-discovery-v0.mjs` + spine |

---

## Related

| Document | Path |
|----------|------|
| Competitor Discovery | [mig-competitor-discovery-contract-v0.md](mig-competitor-discovery-contract-v0.md) |
| Research Pack | [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) |
| Research Request | [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) |
| ORCA handoff | [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) |
| discover-from-serp (v0.2b) | [../lib/competitor-discovery/discover-from-serp.js](../lib/competitor-discovery/discover-from-serp.js) |
| Session spine | [../lib/session-spine/](../lib/session-spine/) |

---

*Design v0 — documentation only. No implementation. No git commit by default.*
