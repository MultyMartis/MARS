# MIG Competitor Discovery Contract v0

**Status:** **documented** — domain-level Source of Truth for MIG Phase 2 competitor acquisition.  
**Not:** workflow spec, JSON Schema registry, discovery engine, provider integration, n8n graph, ORCA methodology, or runtime product.

**Supersedes:** Implicit competitor mentions in SERP normalization and the «reserved» Competitor Observations stub in [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) §2.5.  
**Upstream:** [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) (`competitor_discovery`, `groundtruth_run`); Research Session (SERP capture + normalization).  
**Downstream:** [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) (`competitor_observations` section); [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) (Observations subset).

**Consumers (future, by reference only):** MIG Worker (discovery pass), MIG Admin, operator HITL UX, ORCA, future MARS runtime observers.

---

## 1. Purpose — What Competitor Discovery is

### Definition

**Competitor Discovery** is the **first market-intelligence enrichment layer** of MIG (R1 Phase 2). It identifies **observable market entities** that appear on capture surfaces during research, records **why each entity entered the discovery set** (objective surface rules only), and assembles **evidence-grade competitor observations** into the Research Pack.

```text
Research Request (competitor_discovery | groundtruth_run)
    ↓
Research Session (SERP capture + normalization)
    ↓
Competitor Discovery Pass          ← this contract
    ↓
Research Pack (competitor_observations section)
    ↓
ORCA (R2) — interprets competitive landscape
```

| Layer | Role |
|-------|------|
| **MIG (this contract)** | Identifies entities on surfaces; types by **surface role**; records evidence and discovery rules fired |
| **ORCA** | Interprets competitive relevance, indirect relationships, positioning, strategy, threat, priority |

**Canonical boundary (normative):**

> **MIG acquires reality. ORCA interprets reality.**

Competitor Discovery **describes who appeared and under what observable conditions**. It **must not** score marketing quality, build positioning, create strategy, rank offers by business value, or recommend actions.

### What Competitor Discovery is not

| Anti-pattern | Why excluded |
|--------------|--------------|
| Competitive positioning analysis | **ORCA** — interpretation |
| Threat scoring / priority ranking | **ORCA** — business judgment |
| «True competitor» vs «not a competitor» verdict | **ORCA** — requires market semantics |
| Indirect-competitor classification | **ORCA** — adjacency is interpretive |
| Landing page offer analysis | **Phase 3** — separate capture layer |
| Deep research synthesis | **Phase 4** — extends evidence, not discovery rules |
| LLM-invented competitor lists | **Forbidden** — no entity without surface evidence |
| Directory crawl / maps API product | **Out of Phase 2 scope** — future charter |

### Relationship to Research Request

- `request_type: competitor_discovery` — primary Phase 2 intake; requires SERP capture (same session or bound prior session per resume rules).
- `request_type: groundtruth_run` — superset; discovery pass runs when SERP artifacts exist.
- `signals[]` — optional manual seeds (domains, business names); **seed only**, not evidence alone.
- Request **`completed`** does **not** imply competitor set completeness — gaps **must** appear in SAFE UNKNOWN.

### Relationship to Research Pack

- Discovery output populates **`competitor_observations`** section per [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) §2.5.
- Phase 2 packs **must** set `mig_phase: "2"` when competitor section is present.
- Section **absent** in Phase 1 packs — listed in SAFE UNKNOWN, not fabricated.

### Relationship to ORCA

- ORCA receives **approved** pack with competitor observations + evidence + SAFE UNKNOWN.
- ORCA **derives** competitive landscape, indirect relationships, and strategic priority — **must not** assume MIG typed entities as «direct competitors» unless MIG evidence explicitly supports surface role only.

---

## 2. Competitor — normative definition

### 2.1 What «competitor» means in MIG

In MIG, a **competitor** (logical term: **discovered market entity**) is an **observable business or service presence** on a market capture surface that **matches objective discovery rules** (§5) for the session scope.

MIG uses «competitor» as a **pack section label** aligned with operator vocabulary. Semantically, MIG records **discovered entities** — not validated competitive relationships.

**Normative rule:**

> MIG lists **who appeared** on surfaces. ORCA decides **who competes** in a strategic sense.

### 2.2 Surface-role types — in MIG scope

These types describe **where and how** an entity was observed — not strategic relationship.

| Type id | Label | MIG scope | Definition |
|---------|-------|-----------|------------|
| `serp_organic` | SERP organic result | **In** | Domain/entity appearing in normalized organic results for a scope query |
| `serp_paid` | SERP paid result | **In** | Domain/entity appearing in paid/ad blocks for a scope query |
| `local_pack` | Local pack listing | **In** | Named business listing in maps/local pack surface attached to SERP capture |
| `directory_listing` | Directory listing | **In** | Business or service listing observed on a directory platform (2GIS, Yandex Sprav, etc.) when surfaced in capture — not from standalone directory crawl |
| `marketplace_listing` | Marketplace listing | **In** | Vendor/seller/listing on a marketplace domain (Avito, Ozon, etc.) when observed on SERP or local surfaces |
| `aggregator` | Aggregator / lead-gen | **In** | Comparison, review, or lead-generation platform appearing on capture surfaces |
| `brand_entity` | Brand-identified entity | **In** | Same business identified across multiple surface observations (deduped display name + domain cluster) |
| `informational_surface` | Informational surface | **In** | Non-transactional informational result (wiki, forum, news, how-to) — **included in discovery set** with this type; ORCA filters relevance |
| `manual_seed` | Manual seed | **In** | Operator-supplied domain or business name via `signals` — **requires** subsequent surface evidence or explicit «seed only» flag |

### 2.3 Relationship types — excluded from MIG

These require interpretation beyond observable surfaces — **ORCA only**.

| Type | MIG scope | Reason |
|------|-----------|--------|
| `indirect_competitor` | **Out** | Requires category adjacency and market definition |
| `strategic_competitor` | **Out** | Business strategy judgment |
| `substitute` / `alternative` | **Out** | Economic interpretation |
| `market_leader` | **Out** | Ranking by business significance |
| `non_competitor` | **Out** | Negative classification is ORCA work |

**Rule:** MIG **may** record an informational surface or aggregator. MIG **must not** label an entity «indirect competitor» or «not a real competitor».

### 2.4 Type evaluation summary (charter types)

| Charter term | MIG disposition | MIG type id (if in) |
|--------------|-----------------|---------------------|
| SERP competitor | **In** | `serp_organic`, `serp_paid` |
| Local Pack competitor | **In** | `local_pack` |
| Directory competitor | **In** (surface observation) | `directory_listing` |
| Marketplace competitor | **In** (listing observation) | `marketplace_listing` |
| Aggregator competitor | **In** | `aggregator` |
| Brand competitor | **In** (deduped entity) | `brand_entity` (+ underlying surface types) |
| Informational competitor | **In** (typed separately) | `informational_surface` |
| Indirect competitor | **Out** | — (ORCA derives from MIG entity set + scope) |

---

## 3. Discovery sources — Phase 2 scope

Phase 2 discovery **uses only sources already produced or declared in the research session**. No new provider integrations are required by this contract.

| Source | Phase 2 | Role | Notes |
|--------|---------|------|-------|
| **SERP organic results** | **In** | Primary | From `serp_result.json` → `organic_results[]` |
| **SERP paid / ads blocks** | **In** | Primary | From `ads_blocks` + paid rows when normalized |
| **Repeated domains across queries** | **In** | Reinforcement | When `queries_executed` > 1; increases `discovery_strength` (§5.3) — not a new source |
| **Local pack / maps surface** | **In** | Primary when captured | From `maps_local_pack` normalized body — not standalone Maps API |
| **Aggregators (SERP-derived)** | **In** | Primary | From `serp_result.aggregators[]` + organic domain match |
| **Marketplaces (SERP-derived)** | **In** | Primary | From `serp_result.marketplaces[]` + organic domain match |
| **Directories (SERP-derived)** | **In** | Conditional | Only when directory domain/listing appears in SERP capture — **no** directory crawl |
| **Manual seeds** | **In** | Seed input | From `Research Request.signals[]` — evidence rules §5.4 apply |
| **Provider enrichment** | **In** | Capture transport | Provider payload normalized into SERP — discovery reads normalized artifact only |
| **Landing observations** | **Out** | Phase 3 | May **reference** URL seen on SERP; no landing fetch in Phase 2 |
| **Deep research / memory** | **Out** | Phase 4 | Extends evidence on known entities — not Phase 2 discovery |
| **Standalone directory crawl** | **Out** | Future charter | Avoid scope creep |
| **Standalone maps API** | **Out** | Future charter | Local pack via SERP capture only in Phase 2 |
| **LLM synthesis** | **Out** | Forbidden as source | May format narrative; **must not** add entities |

**Phase 2 scope boundary (normative):**

> Competitor Discovery Phase 2 is **SERP-session-derived**. All entities **must** trace to SERP capture artifacts or manual seeds with explicit evidence discipline (§6).

---

## 4. Competitor Object — canonical structure

Logical object embedded in Research Pack `competitor_observations` section. Future serialization: `competitors.json` or embedded array in `research_pack.json`.

### 4.1 Competitor Object (entity)

| Field | Required | Type | Meaning |
|-------|----------|------|---------|
| `competitor_id` | **Yes** | string | Stable id within pack — pattern `{session_id}-c{seq}` e.g. `mig-20260601-a1b2c3-c001` |
| `display_name` | **Yes** | string | Name as observed on surface (title, business name, ad headline) — **not** normalized brand strategy |
| `primary_domain` | **O** | string \| null | Registrable domain when applicable; null for some local listings |
| `domains_observed` | **O** | string[] | All domains seen for this entity across evidence |
| `surface_types` | **Yes** | enum[] | Subset of §2.2 type ids — all types that apply |
| `discovery_sources` | **Yes** | object[] | See §4.2 — at least one entry |
| `first_seen_query` | **Yes** | string | First scope query where entity matched a rule |
| `queries_seen` | **Yes** | string[] | All scope queries where entity matched |
| `discovery_rules_fired` | **Yes** | string[] | Rule ids from §5 — objective audit trail |
| `discovery_strength` | **Yes** | enum | `single` \| `repeated` \| `multi_surface` — see §5.3 |
| `region` | **Yes** | string | Copied from session scope.region |
| `city` | **O** | string \| null | From scope or local pack observation |
| `evidence` | **Yes** | object[] | See §4.3 — minimum one item for inclusion |
| `evidence_grade` | **Yes** | enum | Worst grade among `evidence[]` — per [Research Pack §4](mig-research-pack-contract-v0.md#4-evidence-model) |
| `capture_time` | **Yes** | ISO-8601 | Earliest evidence `observed_at` |
| `updated_at` | **O** | ISO-8601 | Last evidence append |
| `listing_refs` | **O** | object[] | Local pack / directory row refs (url, position, snippet) |
| `manual_seed` | **O** | boolean | true if entered via `signals` before surface confirmation |
| `seed_only` | **O** | boolean | true when manual seed has **no** surface evidence yet — **must** pair with SAFE UNKNOWN |
| `notes` | **O** | string | Operator capture notes — **no** strategic interpretation |
| `safe_unknown` | **O** | string[] | Entity-level gaps (e.g. domain ambiguous) |

**Inclusion rule:** An entity **must not** appear in `competitor_observations` without at least one `evidence[]` item at grade **A**, **B**, or **C**, **unless** `seed_only: true` with explicit SAFE UNKNOWN (§7).

### 4.2 Discovery Source (attribution sub-object)

| Field | Required | Meaning |
|-------|----------|---------|
| `source_kind` | **Yes** | `serp_organic` \| `serp_paid` \| `local_pack` \| `aggregator_list` \| `marketplace_list` \| `manual_seed` |
| `artifact_ref` | **Yes** | Registry key — typically `serp_result` |
| `source_label` | **O** | Human-readable (e.g. «Yandex mobile SERP») |
| `observed_at` | **Yes** | ISO-8601 |

### 4.3 Evidence item (per entity)

| Field | Required | Meaning |
|-------|----------|---------|
| `evidence_id` | **O** | `{competitor_id}-e{seq}` |
| `source_type` | **Yes** | Per Research Pack §4.3: `human` \| `serp_provider` \| `snapshot` \| `filesystem_artifact` \| `unknown` |
| `artifact_ref` | **Yes** | e.g. `serp_result`, future `snapshots/competitor-{id}.png` |
| `observed_at` | **Yes** | ISO-8601 |
| `grade` | **Yes** | A \| B \| C \| D \| X |
| `surface_detail` | **O** | Structured capture row — position, url, title, snippet (from normalization) |
| `snapshot_ref` | **O** | Phase 2+ optional path under `snapshots/` |

### 4.4 Competitor Observations section (pack-level wrapper)

| Field | Required | Meaning |
|-------|----------|---------|
| `section_id` | **Yes** | `competitor_observations` |
| `schema_version` | **Yes** | `"0"` — this contract |
| `discovery_pass_at` | **Yes** | ISO-8601 when discovery pass completed |
| `discovery_phase` | **Yes** | `2` for this contract |
| `query_set_ref` | **Yes** | Links to pack `query_set` |
| `competitors` | **Yes** | Array of Competitor Object — **may be empty** only with SAFE UNKNOWN explaining why |
| `excluded_surfaces` | **O** | Surfaces scanned but yielding no normalize-able rows (audit) |
| `section_evidence_grade` | **Yes** | Worst grade among competitors + empty-state policy |
| `section_coverage` | **Yes** | Per Research Pack §4.5: `complete` \| `partial` \| `minimal` \| `unknown` |
| `discovery_notes` | **O** | Operator notes on capture conditions |
| `safe_unknown` | **O** | Section-level gaps — **must** merge into pack SAFE UNKNOWN at approval |

### 4.5 Example (illustrative, non-normative)

```json
{
  "competitor_id": "mig-20260601-a1b2c3-c001",
  "display_name": "Манипулятор-Сервис Краснодар",
  "primary_domain": "manipulator-krd.ru",
  "domains_observed": ["manipulator-krd.ru"],
  "surface_types": ["serp_organic", "local_pack"],
  "discovery_sources": [{
    "source_kind": "serp_organic",
    "artifact_ref": "serp_result",
    "observed_at": "2026-06-01T10:00:00Z"
  }],
  "first_seen_query": "аренда манипулятора Краснодар",
  "queries_seen": ["аренда манипулятора Краснодар"],
  "discovery_rules_fired": ["rule_serp_organic_top_n"],
  "discovery_strength": "multi_surface",
  "region": "Krasnodar Krai",
  "city": "Krasnodar",
  "evidence": [{
    "source_type": "filesystem_artifact",
    "artifact_ref": "serp_result",
    "observed_at": "2026-06-01T10:00:00Z",
    "grade": "C",
    "surface_detail": { "position": 3, "url": "https://manipulator-krd.ru/", "title": "Манипулятор-Сервис Краснодар" }
  }],
  "evidence_grade": "C",
  "capture_time": "2026-06-01T10:00:00Z"
}
```

---

## 5. Discovery rules — objective only

Discovery rules are **deterministic predicates** on normalized capture artifacts. They **must not** encode marketing judgment.

### 5.1 Rule catalog (Phase 2)

| Rule id | Predicate | Emits type |
|---------|-----------|------------|
| `rule_serp_organic_top_n` | Organic result at position ≤ **N** (default **10**) for any executed query | `serp_organic` |
| `rule_serp_paid_visible` | Entity in paid/ad block with visible url or domain | `serp_paid` |
| `rule_local_pack_present` | Named listing in normalized local pack body | `local_pack` |
| `rule_aggregator_domain` | Domain matches aggregator list in `serp_result.aggregators[]` or known aggregator domain table (config) | `aggregator` |
| `rule_marketplace_domain` | Domain matches `serp_result.marketplaces[]` or known marketplace domain table | `marketplace_listing` |
| `rule_directory_domain` | Domain matches known directory platform table **and** row represents a business listing | `directory_listing` |
| `rule_repeated_domain` | Same registrable domain in organic results for ≥ **2** distinct executed queries | adds `discovery_strength: repeated` |
| `rule_multi_surface` | Same entity (domain or normalized name match) on ≥ **2** surface kinds | adds `discovery_strength: multi_surface` |
| `rule_manual_seed` | Domain or name in `signals[]` | `manual_seed` |
| `rule_informational_domain` | Domain matches informational allowlist (wiki, forum patterns) or SERP row typed informational by normalization | `informational_surface` |

**Configurable constants (Phase 2 defaults):** `N=10` for top organic; domain tables are **operator-maintained config**, not LLM inference.

### 5.2 Exclusion rules (Phase 2)

| Rule id | Effect |
|---------|--------|
| `exclude_own_domain` | Skip domains in request `signals.exclude_domains[]` if present |
| `exclude_search_engine` | Skip search engine own domains (google.com, yandex.ru, etc.) |
| `exclude_no_url_no_name` | Skip rows with neither display name nor domain |
| `exclude_duplicate_entity` | Merge into existing `competitor_id` by domain match or normalized name key |

### 5.3 Discovery strength (enum)

| Value | Condition | Meaning |
|-------|-----------|---------|
| `single` | One query, one surface | Minimal recurrence signal |
| `repeated` | `rule_repeated_domain` fired | Same domain across queries |
| `multi_surface` | `rule_multi_surface` fired | Same entity on e.g. organic + local pack |

**Normative:** `discovery_strength` is a **recurrence/surface fact** — not competitive importance. ORCA **must not** treat `multi_surface` as «stronger competitor».

### 5.4 Manual seed rules

1. Seed creates **candidate** with `manual_seed: true`.
2. If no surface rule fires in same session: `seed_only: true`, grade **X** or **D**, **must** appear in SAFE UNKNOWN.
3. Seed **never** upgrades evidence grade without surface evidence.
4. Operator may remove seed-only candidates at review — not at discovery automation.

### 5.5 What discovery rules must never do

- Rank entities by «business value» or estimated revenue
- Filter out aggregators/informational as «not competitors» — type them instead
- Collapse local + organic into strategic «same competitor» without domain/name match keys
- Infer entities not present in normalized artifacts
- Apply niche-specific «relevance» (e.g. «this is not crane rental») — **ORCA**

---

## 6. Evidence model

Aligns with [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) §4.

### 6.1 Minimum required evidence

| Scenario | Minimum evidence | Minimum grade | Pack effect |
|----------|------------------|---------------|-------------|
| SERP-derived entity | One `evidence[]` with `artifact_ref: serp_result` + `surface_detail` | **C** (normalized derivative) | Included in competitors[] |
| Provider SERP with raw stored | Same + optional raw ref in registry | **B** possible | Included |
| Manual SERP observation | Human-entered row in manual capture | **A** or **B** | Included |
| Manual seed only | `seed_only: true`, no surface row | **X** | Listed with SAFE UNKNOWN — **or** excluded from competitors[] and noted in SAFE UNKNOWN |
| Local pack unavailable | No local entities | — | Section notes gap; `rule_local_pack_present` not fired |
| Fallback SERP (empty organic) | No entities pass rules | — | `competitors: []` + SAFE UNKNOWN — **no speculative entries** |

### 6.2 Evidence grade per competitor

- `evidence_grade` = **lowest** grade among entity evidence items (pessimistic).
- LLM narrative **cannot** raise grade above underlying capture.

### 6.3 Section evidence grade

- `section_evidence_grade` = lowest among all competitors **and** SERP dependency grade.
- If SERP is **D** or **X**, competitor section **cannot** exceed SERP grade.

### 6.4 Evidence coverage (competitor section)

| Coverage | Condition |
|----------|-----------|
| `complete` | ≥1 competitor with grade ≥ C; local pack captured or explicitly N/A in scope; no seed-only without operator ack |
| `partial` | Some rules blocked (e.g. local pack X); mix of C and seed-only |
| `minimal` | Empty organic; only seed-only or D-grade placeholders |
| `unknown` | Operator has not assessed — discouraged; use `partial` + SAFE UNKNOWN |

### 6.5 Avoiding speculative competitors

**Normative:**

> No entity in `competitors[]` without traceable `discovery_rules_fired` and `evidence[]` (except explicit `seed_only` policy).

Provider failure → empty set + SAFE UNKNOWN, **not** LLM-generated competitors.

---

## 7. Research Pack integration

### 7.1 Section placement

`competitor_observations` follows `serp_observations` and precedes `landing_observations` per Research Pack §3.

### 7.2 Required fields (Phase 2 pack)

| Pack area | Requirement |
|-----------|-------------|
| `mig_phase` | `"2"` when section populated |
| `competitor_observations` | Full §4.4 wrapper + `competitors[]` |
| `evidence_grades.competitor_observations` | Section grade |
| `artifact_registry.competitors` | **O** — future `competitors.json` path |
| `safe_unknown` | Union includes competitor gaps |

### 7.3 Optional fields (Phase 2)

| Field | Notes |
|-------|-------|
| `snapshots/` entries per competitor | When operator captures screenshots |
| `excluded_surfaces` | Audit trail |
| `discovery_notes` | Operator commentary |

### 7.4 Future fields (Phase 3+)

| Field | Phase | Purpose |
|-------|-------|---------|
| `landing_evidence_refs[]` | 3 | Link to landing_observations by url |
| `offer_evidence_refs[]` | 3 | Observed offer patterns per entity |
| `trust_evidence_refs[]` | 3 | Reviews/trust per entity |
| `deep_research_refs[]` | 4 | Memory / extended query evidence |
| `entity_revision` | 3+ | Re-capture increment |

**Stability rule:** Phase 3+ **appends** evidence and refs — **must not** rename `competitor_id` or remove §4.1 required fields without contract revision.

### 7.5 Relationships to other sections

| Related section | Relationship |
|-----------------|--------------|
| **SERP observations** | **Upstream dependency** — discovery reads normalized SERP; SERP section remains authoritative for raw surface |
| **Landing observations** | **Downstream (Phase 3)** — may reference same domains; discovery does not duplicate landing body in Phase 2 |
| **Deep research** | **Phase 4** — may add queries_seen and evidence; same entity ids |

### 7.6 Markdown representation (v0.1 projection)

Human-readable pack **must** include:

```markdown
## Competitor Observations

| ID | Name | Domain | Types | Strength | Grade | First query |
|----|------|--------|-------|----------|-------|-------------|
...

### Discovery notes
...

### Entity evidence (summary)
...
```

Generated from logical object — template is representation, not SoT.

---

## 8. SAFE UNKNOWN — competitor policy

### 8.1 Mandatory competitor SAFE UNKNOWN cases

| Case | Example entry |
|------|-----------------|
| Provider failure | «SERP provider unavailable — competitor discovery skipped; organic list empty» |
| Partial capture | «Local pack not captured — local_pack entities missing» |
| Ambiguous domain | «Entity c003: display name only, domain unresolved» |
| Seed without confirmation | «Manual seed example.ru — no SERP confirmation (seed_only)» |
| Insufficient evidence | «Fallback mode — competitor section empty pending human SERP capture» |
| Phase 1 session | «Competitor discovery not in scope for mig_phase 1» |
| Rule config gap | «Directory domain table not configured — directory_listing rule skipped» |
| Dedup uncertainty | «Two local listings may be same entity — merged by domain; name variant unresolved» |

### 8.2 Entity-level vs pack-level

- Entity `safe_unknown[]` — specific to one competitor object.
- Section / pack SAFE UNKNOWN — session-wide gaps.
- **At approval:** union **must** be consistent between manifest and pack markdown.

### 8.3 When competitors[] may be empty

Allowed when:

1. SERP capture yielded no rule matches **and** no seeds, with SAFE UNKNOWN explaining; or
2. SERP itself is X/D with explicit «discovery not executed» note.

**Forbidden:** empty competitors[] with no SAFE UNKNOWN entry when Phase 2 pack claims `mig_phase: 2`.

---

## 9. ORCA consumption rules

### 9.1 What ORCA receives

| Deliverable | Content |
|-------------|---------|
| **Competitor list** | `competitors[]` with ids, names, domains, surface types |
| **Evidence** | Per-entity evidence items + grades + artifact refs |
| **Queries seen** | `queries_seen`, `first_seen_query` per entity |
| **Discovery audit** | `discovery_rules_fired`, `discovery_strength` |
| **Capture notes** | `discovery_notes`, operator `notes` |
| **SAFE UNKNOWN** | Pack + entity-level gaps |
| **SERP linkage** | `artifact_ref: serp_result` — ORCA can read full SERP section |

### 9.2 What ORCA must never assume

| Assumption | Why forbidden |
|------------|---------------|
| Every entity is a «direct competitor» | MIG types surface roles only |
| `informational_surface` is irrelevant | ORCA decides informational vs competitive intent |
| `aggregator` is or is not a threat | Strategic judgment |
| `discovery_strength: multi_surface` means market leader | Recurrence ≠ importance |
| Empty local pack means no local competitors exist | Capture gap — check SAFE UNKNOWN |
| `seed_only` entities are validated competitors | Explicit gap marker |
| Competitor set is complete | MIG captures observed surfaces only |
| MIG excluded indirect competitors correctly | MIG does not classify indirect |

### 9.3 What ORCA must derive itself

- Competitive set for strategy (who matters for the niche)
- Direct vs indirect relationships
- Positioning and offer comparison
- Priority / threat / opportunity ranking
- Campaign architecture implications
- Whether aggregators should be targets or channels
- Filtering informational surfaces from competitive analysis

### 9.4 Handoff alignment

Maps to [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md):

| Handoff field | Competitor source |
|---------------|-------------------|
| Observations | `competitor_observations` section |
| Evidence Grade | Section + per-entity grades |
| SAFE UNKNOWN | §8 |
| Snapshots | Optional per-entity `snapshot_ref` |
| Queries | `queries_seen` aggregated in Query Set |

---

## 10. Phase evolution — contract stability

### 10.1 Phase 2 — SERP-based discovery (this contract)

- Sources: §3 Phase 2 table only
- Output: `competitor_observations` with SERP/local evidence
- `discovery_phase: 2`
- Snapshots optional, not required

### 10.2 Phase 3 — Landing enrichment

- **Adds** `landing_evidence_refs[]`, offer/CTA/trust refs on existing entities
- **May** discover new entities **only** from landing urls already linked to SERP entities or explicit new capture charter — **not** from speculative crawl
- `discovery_phase` remains `2` for rule core; `enrichment_phase: 3` optional flag
- Competitor Object **unchanged** required fields — optional refs only

### 10.3 Phase 4 — Deep research enrichment

- **Adds** queries, evidence items, `deep_research_refs[]`
- Multi-query sessions default for `groundtruth_run`
- **May** increase `queries_seen` and evidence count — **must not** retroactively change `discovery_rules_fired` history (append revision log instead)
- Same `competitor_id` stability across phases

### 10.4 Versioning

| Change type | Action |
|-------------|--------|
| New optional fields | Minor — same `schema_version: "0"` with doc addendum |
| New required fields | Bump contract to v1 |
| Rule semantics change | Document in discovery rules registry; do not silently alter past packs |

---

## 11. Implementation readiness — remaining gaps

After this design, the following artifacts are **still missing** before coding:

| Artifact | Path (proposed) | Purpose |
|----------|-----------------|---------|
| **Competitor JSON Schema** | `schemas/competitors-v0.1.schema.json` | Validate `competitors.json` / section serialization |
| **Discovery rules config** | `config/competitor-discovery-rules-v0.json` | N, domain tables (aggregator, marketplace, directory, informational, search-engine exclude) |
| **Discovery pass module** | `lib/competitor-discovery/discover-from-serp.js` | Deterministic rule engine over `serp_result.json` |
| **Pack builder extension** | `lib/session-spine/build-research-pack.js` | Emit `competitor_observations` markdown + optional JSON |
| **Session manifest extension** | `schemas/session-manifest-v0.2.schema.json` | `artifacts.competitors`, `mig_phase`, discovery pass metadata |
| **Research Pack contract patch** | `mig-research-pack-contract-v0.md` §2.5 | Link here; optional field checklist (reference update) |
| **Worker route** | n8n / spine entry for `competitor_discovery` | Wire request type → SERP + discovery pass |
| **Test fixtures** | `test/test-payload-competitor-discovery-v0.1.json` | Golden session with known SERP → expected competitors |
| **Verification script** | `tools/verify-competitor-discovery-v0.mjs` | Rule coverage checks without provider |
| **Operator domain tables** | Human-maintained seed lists per niche/region | **Process**, not code — document in config README |

**Explicitly not required for Phase 2 coding start:** provider integration, landing fetch, ORCA changes, LLM enrichment, snapshot automation.

**Minimum coding slice (recommended order):**

1. Schema + rules config  
2. `discover-from-serp.js` + unit tests  
3. Pack builder + manifest artifacts  
4. Worker route + test fixture  
5. HITL markdown review template  

---

## 12. Explicit non-goals

This contract is **not**:

- Competitor discovery **implementation** or n8n workflow
- SERP provider integration or OpenRouter usage
- Landing analysis methodology (Phase 3)
- ORCA competitive analysis redesign
- Scoring, ranking, strategy, or positioning
- Directory/maps standalone crawl products
- Proof that discovery pass exists in repo

---

## Related

| Document | Path |
|----------|------|
| Research Request | [mig-research-request-contract-v0.md](mig-research-request-contract-v0.md) |
| Research Pack | [mig-research-pack-contract-v0.md](mig-research-pack-contract-v0.md) |
| ORCA handoff | [mig-orca-handoff-contract-v0.md](mig-orca-handoff-contract-v0.md) |
| SERP result schema (v0.1) | [../schemas/serp-result-v0.1.schema.json](../schemas/serp-result-v0.1.schema.json) |
| Session spine | [../lib/session-spine/](../lib/session-spine/) |
| Multi-Query Discovery (v0.3 design) | [mig-multi-query-discovery-design-v0.md](mig-multi-query-discovery-design-v0.md) |
| Boundaries | [../boundaries.md](../boundaries.md) |

---

*Contract v0 — documentation only. No implementation. No git commit by default.*
