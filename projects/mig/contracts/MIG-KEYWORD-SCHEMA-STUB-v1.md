# MIG Keyword Schema Stub v1

**Status:** **normative** — architecture-only field stub (Phase 2g / G-02)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2g — Provider Infrastructure Contracts  
**Gate closed:** **G-02** — Keyword Object + registry + snapshot field stub (no JSON Schema syntax)  
**Prior artifacts:** [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-REGISTRY-MODEL-v1.md](MIG-KEYWORD-REGISTRY-MODEL-v1.md) · [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md)  
**Related (reference, not superseded):** [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md)

**This document delivers:** architecture-only field stubs for Keyword Object, Keyword Registry, Keyword Snapshot, Keyword Observation — fields, ownership, required vs optional, authority.

**This document does not deliver:** JSON Schema syntax, validation code, runtime types, storage paths, or implementation.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This stub **names and constrains fields** for future artifacts. It does **not** authorize file creation, parsers, or registry writers.

---

## Stub purpose

| Goal | How this stub serves it |
|------|-------------------------|
| Close **G-02** | Field inventory before first manual Wordstat pilot |
| Prevent ad hoc session files | Single authoritative field vocabulary |
| Align ingest design | Snapshot → Observation → Object → Registry chain explicit |
| Defer implementation | No syntax, no code — architecture only |

**Normative:** Where this stub and Phase 2c/2d models differ, **Phase 2c/2d win** — this document **operationalizes** them for infrastructure contracts without redesign.

---

## Entity overview

| Entity | Role | Authority |
|--------|------|-----------|
| **Keyword Snapshot** | Raw provider capture SoT | Acquisition / operator attach — **upstream** |
| **Keyword Observation** | Pre-register ingest unit | Ingest boundary — **ephemeral** |
| **Keyword Object** | Canonical phrase record | Registry index — **session SoT per phrase identity** |
| **Keyword Registry** | Session index of Keyword Objects | Keyword Surface — **session SoT for registered demand language** |

```text
Provider export (raw file)
        │
        ▼
Keyword Snapshot ──extract──► Keyword Observation ──register──► Keyword Object
                                                                        │
                                                                        ▼
                                                              Keyword Registry
```

---

## Keyword Object — field stub

**Owner:** Keyword Surface layer (Demand Surface).  
**Authority:** Registry is SoT for **which** objects exist; object **shape** is defined here and in Phase 2c.

### Core identity

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **keyword_id** | **Yes** | Registry writer (assign at first register) | Immutable within session revision; opaque id |
| **phrase** | **Yes** | Capture channel | Human-visible truth; trim outer whitespace only |
| **phrase_normalized** | Optional | Registry writer (derive) | Dedup identity only — never display |
| **session_id** | **Yes** | Session spine | Must match owning session |

### Provenance and evidence

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **source_type** | **Yes** | Ingest mapping | Primary channel — see Provenance enum below |
| **provenance_records[]** | **Yes** | Ingest + registry merge | Minimum one entry; append-only on merge |
| **evidence_refs[]** | **Yes** | Ingest | Pointers to manifest, snapshot, request — not embedded SoT |
| **evidence_grade** | **Yes** | Ingest | `operator` \| `provider` \| `extracted` |
| **safe_unknown[]** | **Yes** | Ingest + operator | May be empty; gaps **must** appear here |

### Scope context

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **region_scope** | Optional | Provider row + session cross-check | Aligns with session `scope.region` or declares mismatch |
| **period_scope** | Optional | Provider export metadata | Time window for numeric slots |
| **locale** | Optional | Session / provider context | BCP-47 when known |
| **engine** | Optional | Channel | Required identity dimension when engine-bound (`yandex`, `google`, `unknown`) |

### Attachments

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **modifier_tags[]** | **Yes** | Enrichment pass (manual or future extraction) | May be empty `[]` — see MOD SAFE UNKNOWN rules in Phase 2c |
| **intent_shape_flags[]** | **Yes** | Enrichment pass | Must include `KS-INT-UNKNOWN` when no other shape evidenced — empty array forbidden |
| **numeric_slots** | Optional | Provider ingest | Container for freq / trend / share — status-first |
| **capability_refs[]** | Optional | Planning traceability | `KS-CAP-*` ids — non-authoritative |

### Lifecycle (registry layer)

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **registry_state** | **Yes** (when in registry) | Registry writer | `KR-LC-*` — observed \| registered \| enriched \| deprecated \| archived |
| **related_keyword_refs[]** | Optional | Operator / chartered rules | Explicit links only — no auto-cluster |
| **supersedes_keyword_id** | Optional | Registry writer on deprecate | Tombstone target |
| **capture_time** | **Yes** | Registry writer | ISO-8601 UTC last material update |

### Forbidden fields (normative)

Must **not** appear on Keyword Object: `cluster_id`, `priority`, `intent` (ORCA enum), `campaign`, `ad_group`, `recommended_bid`, `semantic_group`, `keyword_difficulty`, `search_volume_tier`, `head_tail_class`, `theme`, `segment_label`.

### numeric_slots sub-stub (per slot: freq, trend, share)

| Field | Required | When | Authority |
|-------|----------|------|-----------|
| **status** | **Yes** | Always | `known` \| `unknown` \| `not_captured` \| `provider_conflict` |
| **value** | When status=`known` | Provider | Raw as returned — no rescaling |
| **raw_columns** | Optional | Uncertain mapping | Verbatim export columns |
| **period** | Optional | Provider | Window label |
| **as_of** | Optional | Provider | Provider timestamp |
| **provider_ref** | Optional | Ingest | Export file / row handle |
| **evidence_refs[]** | When status=`known` | Ingest | Snapshot row pointer |
| **conflict_values[]** | When status=`provider_conflict` | Ingest | No winner — preserve all |
| **safe_unknown[]** | **Yes** | Always | May be empty |

---

## Keyword Registry — field stub

**Owner:** Keyword Surface / session.  
**Authority:** **Session SoT** for registered Keyword Objects. Wins over Keyword Surface rollup and pack projections on conflict (KR-OWN-04).

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **registry_id** | **Yes** | Registry writer | Typically `session_id` + revision |
| **session_id** | **Yes** | Session spine | Owning session |
| **revision** | **Yes** | Registry writer | Monotonic integer; `1` on first write |
| **registry_state** | **Yes** | Operator + registry writer | `open` \| `frozen` \| `archived` |
| **keywords[]** | **Yes** | Registry writer | Embedded or referenced Keyword Objects |
| **collections[]** | Optional | Registry writer | Batch metadata (`seed_batch`, `wordstat_batch`, etc.) |
| **stats** | Optional | Registry writer (derivable) | `{ total, by_source_type, by_registry_state }` |
| **session_safe_unknown[]** | **Yes** | Ingest + operator | Session-level gaps — may be empty |
| **supersedes_revision** | Optional | Registry writer | Prior revision on re-capture |
| **capture_time** | **Yes** | Registry writer | Last material registry update |

**Cardinality:** One **current** registry revision per session. Historical revisions retained on re-capture.

**Empty registry:** Valid when keyword pass not executed — **must** carry session SAFE UNKNOWN (KR-OWN-05).

---

## Keyword Snapshot — field stub

**Owner:** Acquisition channel / operator attach.  
**Authority:** **Upstream SoT** for raw provider capture. Registry **references** snapshots; does **not** replace them (KR-OWN-03, KR-SNAP-02).

**Logical artifact names (reference only):** `wordstat_snapshot.{capture_id}.json` or generic `demand_snapshot.{capture_id}.json`.

### Snapshot header

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **schema_stub_version** | **Yes** | Contract | `"keyword-snapshot-stub-v1"` — not runtime schema version |
| **session_id** | **Yes** | Session spine | Owning session |
| **capture_id** | **Yes** | Operator / ingest | Opaque per capture invocation |
| **snapshot_type** | **Yes** | Ingest | `wordstat` \| `demand_provider` \| `operator_worksheet` |
| **import_method** | **Yes** | Operator | `manual_export` \| `manual_paste` \| `api` \| `operator_json` |
| **provider_label** | **Yes** | Operator | e.g. `yandex_wordstat`, `MOCK-STAT-EXPORT` |
| **region** | Optional | Export metadata | Provider region code if present |
| **region_label** | Optional | Export metadata | Human label — e.g. «Краснодар» |
| **period** | Optional | Export metadata | e.g. `2026-05`, `month`, `unknown` |
| **source_account_ref** | Optional | Operator | Opaque handle — no secrets in repo |
| **exported_at** | Optional | Export / operator | When provider file was generated |
| **captured_at** | **Yes** | Operator / ingest | When snapshot attached to session |
| **operator_id** | **Yes** | Operator | Human supervision record |
| **source_file_ref** | **Yes** (manual export) | Operator | Pointer to raw CSV/XLSX on disk |
| **column_mapping** | Optional | Ingest / operator | Declared export column → logical slot map |
| **session_safe_unknown[]** | **Yes** | Ingest | Snapshot-level gaps |
| **evidence_grade** | **Yes** | Ingest | `operator` \| `provider` |

### Snapshot row (embedded in **rows[]**)

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **row_id** | **Yes** | Ingest | Stable within snapshot — e.g. `M-01`, line number |
| **phrase** | **Yes** | Provider | Exact cell value |
| **region** | Optional | Provider | Row-level region when export provides it |
| **period** | Optional | Provider | Row-level period when export provides it |
| **frequency** | Optional | Provider | Raw shows / query count — uninterpreted |
| **frequency_share** | Optional | Provider | Share column if present |
| **trend** | Optional | Provider | Trend column if present |
| **raw_columns** | **Yes** | Ingest | All export columns verbatim when mapping applied |
| **safe_unknown[]** | **Yes** | Ingest | Row-level gaps — may be empty |

**Normative:** Snapshot rows are **not** Keyword Objects. Mapping to objects is defined in [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md).

---

## Keyword Observation — field stub

**Owner:** Ingest boundary (logical).  
**Authority:** **Ephemeral** — consumed by registry writer; may exist only in ingest logs in future implementation.

| Field | Required | Owner | Authority |
|-------|----------|-------|-----------|
| **observation_id** | **Yes** | Ingest | Ephemeral — not `keyword_id` |
| **session_id** | **Yes** | Session spine | Owning session |
| **snapshot_ref** | **Yes** | Ingest | Pointer to Keyword Snapshot + row_id |
| **phrase** | **Yes** | Snapshot row | Copied for ingest convenience |
| **phrase_normalized** | Optional | Ingest (derive) | For identity check before register |
| **provenance_id** | **Yes** | Mapping spec | `KS-PROV-FUTURE-WORDSTAT` or `KS-PROV-FUTURE-PROVIDER` |
| **region_scope** | Optional | Mapping spec | From row or snapshot header |
| **period_scope** | Optional | Mapping spec | From row or snapshot header |
| **numeric_preview** | Optional | Mapping spec | Logical freq/trend/share values before object attach |
| **safe_unknown[]** | **Yes** | Ingest | Pre-register unknowns |
| **observed_at** | **Yes** | Ingest | ISO-8601 UTC |

**Lifecycle:** Observation → **register** → Keyword Object with assigned `keyword_id` (KR-TR-01).

**MVP note:** Observation layer does not exist in Phase 1 evidence — stub defines boundary for first provider pilot.

---

## Provenance enum stub (Keyword Object **source_type**)

| provenance_id | source_type value | Use |
|---------------|-------------------|-----|
| **KS-PROV-OPERATOR-SEED** | `operator_seed` | Research Request seeds |
| **KS-PROV-EXECUTED-QUERY** | `executed_query` | Manifest executed queries |
| **KS-PROV-SEARCH-SUGGESTION** | `search_suggestion` | Suggestion snapshot |
| **KS-PROV-RELATED-SEARCH** | `related_search` | SERP related block |
| **KS-PROV-PAGE-VISIBLE** | `page_visible` | Page title/H1/meta |
| **KS-PROV-OPERATOR-INPUT** | `operator_input` | Manual operator import |
| **KS-PROV-FUTURE-WORDSTAT** | `future_wordstat` | Yandex Wordstat export row |
| **KS-PROV-FUTURE-PROVIDER** | `future_provider` | Generic demand provider row |

**Provider pilot default:** Manual Wordstat Export → `KS-PROV-FUTURE-WORDSTAT` with `import_method: manual_export`.

---

## Authority matrix (summary)

| Concern | Keyword Snapshot | Keyword Observation | Keyword Object | Keyword Registry |
|---------|------------------|---------------------|----------------|------------------|
| Raw provider numbers | **Owns** (row) | Carries preview | Stores in `numeric_slots` | Indexes object |
| Phrase string | **Owns** (row) | Carries copy | **Owns** (canonical) | Indexes object |
| Provenance history | Header + row refs | Single channel | **Owns** (aggregated) | Indexes object |
| Session demand SoT | No | No | Per-identity SoT | **Owns** (index) |
| SAFE UNKNOWN | Snapshot + row | Observation | Object | Session aggregate |
| ORCA / strategy fields | **Forbidden** | **Forbidden** | **Forbidden** | **Forbidden** |

---

## Architecture decisions (schema stub)

| ID | Decision | Rationale |
|----|----------|-----------|
| **KS-SS-01** | Stub uses **field tables**, not JSON Schema | G-02 closed per Phase 2g charter — syntax deferred to implementation gate |
| **KS-SS-02** | Four entities explicit | Matches Registry Model §Registry Entities |
| **KS-SS-03** | Snapshot rows ≠ Keyword Objects | Preserves KR-OWN-03 upstream SoT |
| **KS-SS-04** | Observation layer stubbed | Closes ingest boundary without runtime |
| **KS-SS-05** | Phase 2c forbidden fields restated | Prevents pilot contamination |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) | Phase 2c canonical object |
| [MIG-KEYWORD-REGISTRY-MODEL-v1.md](MIG-KEYWORD-REGISTRY-MODEL-v1.md) | Phase 2d registry organization |
| [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md) | Snapshot row → Object (G-03) |
| [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) | Upsert behaviors (G-04) |
| [MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md](MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md) | Umbrella + audit |

---

*MIG Keyword Schema Stub v1 · 2026-06-06 · architecture-only · G-02 closed · no runtime*
