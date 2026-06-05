# MIG Mock Provider Replay v1

**Status:** **replay** — tabletop exercise only (Phase 2f)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2f — Mock Provider Replay  
**Prior artifacts:** [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) · [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) · [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md) · [MIG-WORDSTAT-READINESS-CHARTER-v1.md](MIG-WORDSTAT-READINESS-CHARTER-v1.md)  
**Validated market (replay context):** Грузотакси / Краснодар / проект Триумф  
**Replay session (logical):** `mig-20260605-mqgt01-replay` — **synthetic tabletop only**

**This document delivers:** mock provider dataset, capability/data/registry mapping, stress tests, integrity validation, replay findings, gap review, final verdict.

**This document does not deliver:** runtime, schemas, Wordstat integration, API calls, acquisition, provider onboarding, ORCA semantics, or implementation.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This replay is a **paper exercise**. All numeric values are **illustrative**. No provider was contacted. No Wordstat data was used.

---

# REPORT — Mock Provider Replay

## Mock Dataset

> **⚠ MOCK DATA — NOT REAL WORDSTAT**  
> Source label: `mock_provider_export_v1` (hypothetical demand-provider table).  
> Numbers are **examples only** for architecture validation.

**Pilot market:** Грузотакси Краснодар  
**Scope region (session):** Краснодар  
**Export period (mock):** 2026-05 (monthly)  
**Provider name (fictional):** `MOCK-STAT-EXPORT` — generic placeholder, not Yandex Wordstat

| Row | phrase | region | period | frequency (shows) | Notes |
|-----|--------|--------|--------|-------------------|-------|
| M-01 | грузотакси краснодар | Краснодар | 2026-05 | 12400 | Core head phrase |
| M-02 | грузовое такси краснодар | Краснодар | 2026-05 | 3100 | Lexical variant |
| M-03 | газель краснодар | Краснодар | 2026-05 | 8900 | Service variant |
| M-04 | грузоперевозки краснодар | Краснодар | 2026-05 | 5600 | Service variant |
| M-05 | перевозка мебели краснодар | Краснодар | 2026-05 | 2100 | Cargo-type query |
| M-06 | квартирный переезд краснодар | Краснодар | 2026-05 | 1800 | Service variant |
| M-07 | вызов газели краснодар | Краснодар | 2026-05 | 950 | Commercial shape |
| M-08 | заказать газель краснодар | Краснодар | 2026-05 | 720 | Commercial + action |
| M-09 | газель с грузчиками краснодар | Краснодар | 2026-05 | 640 | Crew modifier |
| M-10 | грузотакси краснодар недорого | Краснодар | 2026-05 | 890 | Extension + price |
| M-11 | грузотакси краснодар цены | Краснодар | 2026-05 | 1100 | Extension + comparison |
| M-12 | сколько стоит грузотакси краснодар | Краснодар | 2026-05 | 420 | Question form |
| M-13 | грузотакси краснодар срочно | Краснодар | 2026-05 | 310 | Urgency modifier |
| M-14 | грузотакси краснодар отзывы | Краснодар | 2026-05 | 280 | Attribute / comparison |
| M-15 | грузотакси краснодар | Краснодарский край | 2026-05 | 15200 | **Same phrase, different region** |
| M-16 | грузотакси краснодар | *(blank)* | 2026-05 | 12400 | **Unknown region cell** |
| M-17 | грузотакси краснодар | Краснодар | 2026-05 | *(blank)* | **Missing frequency** |
| M-18 | грузотакси краснодар | Краснодар | 2026-05 | 11800 | **Conflict row** — second mock export same phrase/region/period |

**Row count:** 18 (within 15–20 target).

**Additional replay inputs (non-mock-provider, for cross-channel stress):**

| Ref | phrase | channel | Notes |
|-----|--------|---------|-------|
| S-01 | грузотакси Краснодар | operator_seed | mqgt01 Research Request seed |
| S-02 | грузотакси краснодар | search_suggestion | Mock suggestion list child of S-01 |
| S-03 | грузотакси краснодар | executed_query | mqgt01 manifest executed |

---

## Capability Mapping

Each mock row maps to **KS-CAP-*** capabilities. Provider rows activate phrase + numeric families; modifier/intent capabilities are **derived** (planning assumption — extraction not operational).

### Provider row → capability activation

| Row | KS-CAP-PHR (phrase) | KS-CAP-MOD (modifiers) | KS-CAP-SIG (signals) | KS-CAP-NUM (numeric) |
|-----|---------------------|------------------------|----------------------|----------------------|
| M-01 | *(via KS-PROV-FUTURE-PROVIDER)* | GEO | LOCAL, COMMERCIAL | FREQ: 12400 |
| M-02 | provider row | GEO, SERVICE | LOCAL, COMMERCIAL | FREQ: 3100 |
| M-03 | provider row | GEO, SERVICE | LOCAL, COMMERCIAL | FREQ: 8900 |
| M-04 | provider row | GEO, SERVICE | LOCAL, COMMERCIAL | FREQ: 5600 |
| M-05 | provider row | GEO, SERVICE | LOCAL, COMMERCIAL | FREQ: 2100 |
| M-06 | provider row | GEO, SERVICE | LOCAL, COMMERCIAL | FREQ: 1800 |
| M-07 | provider row | GEO, SERVICE, COMMERCIAL | LOCAL, COMMERCIAL, ACTION | FREQ: 950 |
| M-08 | provider row | GEO, SERVICE, COMMERCIAL, ACTION | LOCAL, COMMERCIAL | FREQ: 720 |
| M-09 | provider row | GEO, SERVICE, ATTRIBUTE | LOCAL, COMMERCIAL | FREQ: 640 |
| M-10 | provider row | GEO, PRICE | LOCAL, COMMERCIAL, COMPARISON | FREQ: 890 |
| M-11 | provider row | GEO, PRICE | LOCAL, COMPARISON | FREQ: 1100 |
| M-12 | provider row | GEO, QUESTION, PRICE | LOCAL, QUESTION, COMPARISON | FREQ: 420 |
| M-13 | provider row | GEO, URGENCY | LOCAL, COMMERCIAL | FREQ: 310 |
| M-14 | provider row | GEO, ATTRIBUTE | LOCAL, COMPARISON | FREQ: 280 |
| M-15 | provider row | GEO | LOCAL, COMMERCIAL | FREQ: 15200 + region mismatch handling |
| M-16 | provider row | GEO | LOCAL, COMMERCIAL | FREQ: 12400 + region SAFE UNKNOWN |
| M-17 | provider row | GEO | LOCAL, COMMERCIAL | FREQ slot `unknown` |
| M-18 | provider row | GEO | LOCAL, COMMERCIAL | FREQ `provider_conflict` vs M-01 |

### Cross-channel capability mapping (stress inputs)

| Ref | Primary capability | Secondary |
|-----|-------------------|-----------|
| S-01 | KS-CAP-PHR-SEED | KS-CAP-MOD-GEO, KS-INT-LOCAL |
| S-02 | KS-CAP-PHR-SUGGEST | host seed S-01; KS-CAP-MOD-GEO |
| S-03 | KS-CAP-PHR-EXEC | KS-CAP-MOD-GEO; Market Surface owns SERP outcome (KS-03) |

### Capability model verdict (replay)

| Question | Result | Evidence |
|----------|--------|----------|
| Can provider rows activate phrase capabilities without new ids? | **Yes** | `KS-PROV-FUTURE-PROVIDER` / `KS-PROV-FUTURE-WORDSTAT` reserved in data model §Provenance |
| Can numeric columns map to KS-CAP-NUM-*? | **Yes** | FREQ on all rows; TREND/SHARE absent → `not_captured` per capability model |
| Can modifiers be tagged from phrase text? | **Yes** | All 18 rows classifiable per capability model pilot table §Modifier taxonomy |
| Does replay require new capability family? | **No** | Generic provider rows fit existing PHR + NUM + MOD + SIG families |

---

## Data Model Mapping

Replay constructs **logical Keyword Objects** per [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md). Three fully worked examples + summary table for remainder.

### Worked example — M-01 (standard provider row)

```text
Keyword Object {
  keyword_id:           "kw-replay-00001"
  phrase:               "грузотакси краснодар"
  phrase_normalized:    "грузотакси краснодар"
  session_id:           "mig-20260605-mqgt01-replay"
  source_type:          future_provider
  provenance_records: [
    {
      provenance_id:    KS-PROV-FUTURE-PROVIDER
      capture_time:     "2026-06-06T12:00:00Z"
      host_context:     { export_id: "mock_provider_export_v1", row: "M-01" }
      import_method:    manual_paste
      evidence_refs:    [ "mock_provider_export_v1#M-01" ]
      evidence_grade:   provider
      safe_unknown:     [ "MOCK DATA — not real Wordstat" ]
    }
  ]
  region_scope:         { value: "Краснодар", code: null, status: "declared" }
  period_scope:         { value: "2026-05", status: "declared" }
  locale:               "ru-RU"
  engine:               null
  modifier_tags: [
    { modifier_type: KS-MOD-GEO, matched_text: "краснодар", evidence_basis: lexical_match }
  ]
  intent_shape_flags: [
    { signal_id: KS-INT-LOCAL, confidence: derived, evidence_basis: [ "modifier:KS-MOD-GEO" ] },
    { signal_id: KS-INT-COMMERCIAL, confidence: derived, evidence_basis: [ "lexical_pattern" ] }
  ]
  numeric_slots: {
    freq:  { status: known, value: 12400, period: "2026-05", provider_ref: "mock#M-01" }
    trend: { status: not_captured }
    share: { status: not_captured }
  }
  evidence_refs:        [ "mock_provider_export_v1#M-01" ]
  evidence_grade:       provider
  safe_unknown:         [ "MOCK DATA — not real Wordstat", "Trend evidence not present in source export" ]
  capture_time:         "2026-06-06T12:00:00Z"
  capability_refs:      [ KS-CAP-PHR-*, KS-CAP-NUM-FREQ, KS-CAP-MOD-GEO, KS-CAP-SIG-INTENT ]
  registry_state:       enriched
}
```

### Worked example — M-10 (extension phrase)

```text
Keyword Object {
  keyword_id:           "kw-replay-00010"
  phrase:               "грузотакси краснодар недорого"
  phrase_normalized:    "грузотакси краснодар недорого"
  source_type:          future_provider
  modifier_tags:        [ GEO: краснодар, PRICE: недорого ]
  intent_shape_flags:   [ KS-INT-LOCAL, KS-INT-COMMERCIAL, KS-INT-COMPARISON ]
  numeric_slots.freq:   { status: known, value: 890 }
  related_keyword_refs: [ { keyword_id: kw-replay-00001, relationship_kind: KR-REL-EXTENSION } ]
  registry_state:       enriched
}
```

### Worked example — M-17 (missing frequency)

```text
Keyword Object {
  keyword_id:           "kw-replay-00017"
  phrase:               "грузотакси краснодар"
  phrase_normalized:    "грузотакси краснодар"
  source_type:          future_provider
  numeric_slots: {
    freq:  { status: unknown, safe_unknown: [ "Provider cell empty — frequency unknown; not inferred as zero" ] }
    trend: { status: not_captured }
    share: { status: not_captured }
  }
  safe_unknown:         [ "Frequency cell blank in mock export row M-17" ]
  registry_state:       registered
}
```

**Note:** M-01 and M-17 share `phrase_normalized` but differ by **numeric context + provenance host_context row** — separate objects per KO-03 unless same identity tuple; here M-17 is same phrase but **different export row with missing freq** → remains **separate object** (distinct evidence row) or merge with conflict handling if same row re-imported. Replay treats as **separate** `kw-replay-00017` to exercise missing-freq path without collapsing M-01.

### Summary — all mock rows → Keyword Object fields

| Row | keyword_id | modifier_tags (summary) | intent_shape_flags | freq.status | registry_state |
|-----|------------|-------------------------|-------------------|-------------|----------------|
| M-01 | kw-replay-00001 | GEO | LOCAL, COMMERCIAL | known (12400) | enriched |
| M-02 | kw-replay-00002 | GEO, SERVICE | LOCAL, COMMERCIAL | known (3100) | enriched |
| M-03 | kw-replay-00003 | GEO, SERVICE | LOCAL, COMMERCIAL | known (8900) | enriched |
| M-04 | kw-replay-00004 | GEO, SERVICE | LOCAL, COMMERCIAL | known (5600) | enriched |
| M-05 | kw-replay-00005 | GEO, SERVICE | LOCAL, COMMERCIAL | known (2100) | enriched |
| M-06 | kw-replay-00006 | GEO, SERVICE | LOCAL, COMMERCIAL | known (1800) | enriched |
| M-07 | kw-replay-00007 | GEO, SERVICE, COMMERCIAL | LOCAL, COMMERCIAL | known (950) | enriched |
| M-08 | kw-replay-00008 | GEO, SERVICE, COMMERCIAL, ACTION | LOCAL, COMMERCIAL | known (720) | enriched |
| M-09 | kw-replay-00009 | GEO, SERVICE, ATTRIBUTE | LOCAL, COMMERCIAL | known (640) | enriched |
| M-10 | kw-replay-00010 | GEO, PRICE | LOCAL, COMMERCIAL, COMPARISON | known (890) | enriched |
| M-11 | kw-replay-00011 | GEO, PRICE | LOCAL, COMPARISON | known (1100) | enriched |
| M-12 | kw-replay-00012 | GEO, QUESTION, PRICE | LOCAL, QUESTION, COMPARISON | known (420) | enriched |
| M-13 | kw-replay-00013 | GEO, URGENCY | LOCAL, COMMERCIAL | known (310) | enriched |
| M-14 | kw-replay-00014 | GEO, ATTRIBUTE | LOCAL, COMPARISON | known (280) | enriched |
| M-15 | kw-replay-00015 | GEO | LOCAL, COMMERCIAL | known (15200) | enriched |
| M-16 | kw-replay-00016 | GEO | LOCAL, COMMERCIAL | known (12400) | enriched |
| M-17 | kw-replay-00017 | GEO | LOCAL, COMMERCIAL | unknown | registered |
| M-18 | kw-replay-00018 | GEO | LOCAL, COMMERCIAL | provider_conflict | enriched |

### Data model verdict (replay)

| Mechanism | Survives replay? | Evidence |
|-----------|------------------|----------|
| Keyword Object creation | **Yes** | 18 objects constructed without field invention |
| Provenance assignment | **Yes** | `KS-PROV-FUTURE-PROVIDER` + evidence_refs per row |
| Modifier tagging | **Yes** | KS-MOD-* applied per capability taxonomy |
| Intent flags | **Yes** | Multi-flag sets; no ORCA enums |
| Numeric slots | **Yes** | known / unknown / provider_conflict exercised |
| Forbidden fields absent | **Yes** | No cluster_id, priority, intent enum |

---

## Registry Mapping

Logical **Keyword Registry** per [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md).

### Registry container (replay)

```text
Keyword Registry {
  registry_id:          "kr-mqgt01-replay-v1"
  session_id:           "mig-20260605-mqgt01-replay"
  revision:             1
  registry_state:       open
  collections: [
    { kind: wordstat_batch, label: "mock_provider_export_v1", keyword_ids: [ kw-replay-00001 .. kw-replay-00018 ] },
    { kind: seed_batch, label: "mqgt01-seeds-replay", keyword_ids: [ kw-replay-seed-001 ] },
    { kind: suggestion_batch, label: "mock-suggest-yandex-r1", keyword_ids: [ kw-replay-suggest-001 ] },
    { kind: executed_batch, label: "mqgt01-executed-replay", keyword_ids: [ kw-replay-exec-001 ] }
  ]
  stats: {
    total: 21
    by_source_type: { future_provider: 18, operator_seed: 1, search_suggestion: 1, executed_query: 1 }
    by_registry_state: { enriched: 17, registered: 4 }
  }
  session_safe_unknown: [
    "MOCK DATA — tabletop replay only; no real provider contacted",
    "Keyword pass not executed in MVP — replay is synthetic",
    "Trend evidence not present in mock export",
    "Brand/competitor modifier glossary not supplied"
  ]
  capture_time:         "2026-06-06T12:00:00Z"
}
```

### Registration flow (per row)

```text
mock_provider_export_v1 row
    → Keyword Snapshot (logical: mock_provider_export_v1)
    → Keyword Observation (ephemeral)
    → register → Keyword Object (KR-LC-REGISTERED)
    → enrich (modifiers + intent + numeric) → KR-LC-ENRICHED
    → index in Keyword Registry.keywords[]
    → assign to wordstat_batch collection
```

### Identity decisions (replay)

| Pair | Judgment | Registry action |
|------|----------|-----------------|
| M-01 ↔ M-02 | **Related** (`KR-REL-LEXICAL_VARIANT`) | Two keyword_ids; optional related_keyword_refs |
| M-01 ↔ M-10 | **Related** (`KR-REL-EXTENSION`) | Two keyword_ids |
| M-01 ↔ M-15 | **Different** (region dimension differs) | Two keyword_ids; region_scope differs |
| M-01 ↔ M-18 | **Same identity tuple conflict on freq** | Single object **or** merge with `provider_conflict` on freq slot — replay keeps M-18 separate object with conflict flag linking M-01 |
| S-01 ↔ M-01 | **Related** (`KR-REL-CHANNEL_ECHO`) | Separate objects per KO-04 |
| S-01 ↔ S-03 | **Related** (`KR-REL-CHANNEL_ECHO`) | Separate objects per KO-04 |
| S-02 ↔ M-01 | **Related** (`KR-REL-CHANNEL_ECHO` + `KR-REL-SHARED_HOST`) | Three distinct keyword_ids |

### Registry mapping verdict

| Mechanism | Survives replay? | Evidence |
|-----------|------------------|----------|
| Registry registration | **Yes** | 21 objects indexed; stats derivable |
| wordstat_batch collection | **Yes** | KR-COL-* allows provider batch without cluster semantics |
| Lifecycle transitions | **Yes** | observed → registered → enriched exercised |
| related_keyword_refs | **Yes** | Extension and channel-echo links applied |
| Session SAFE UNKNOWN | **Yes** | Aggregated pass-level gaps declared |

---

## Stress Tests

### ST-01 — Same phrase (duplicate provider row, same region/period)

**Input:** M-01 and hypothetical duplicate re-import of M-01 (same shows=12400).

**Expected behavior:**

- Identity tuple `(session, phrase_normalized, future_provider, engine=null)` matches → **merge** per KO-03 / KR-INT-01.
- Union `provenance_records[]`; retain single `keyword_id`.
- Stats count one object, not two.

**Replay result:** **PASS** — model explicitly defines idempotent merge.

---

### ST-02 — Same phrase, different source

**Input:** S-01 (operator_seed) vs M-01 (future_provider) — both «грузотакси краснодар».

**Expected behavior:**

- **Separate Keyword Objects** per KO-04 / KR-INT-02.
- Optional `KR-REL-CHANNEL_ECHO` link.
- Seed object: `numeric_slots.freq.status = not_captured`.
- Provider object: `numeric_slots.freq.status = known`.

**Replay result:** **PASS** — dual objects constructed; no forced merge.

---

### ST-03 — Lexical variant

**Input:** M-01 «грузотакси краснодар» vs M-02 «грузовое такси краснодар».

**Expected behavior:**

- **Different** `phrase_normalized` → **different** keyword_ids.
- **No auto-merge** per KR-ID-03.
- Optional operator link `KR-REL-LEXICAL_VARIANT` — replay adds link, not merge.

**Replay result:** **PASS** — synonyms remain distinct identities.

---

### ST-04 — Extension phrase

**Input:** M-01 vs M-10 «грузотакси краснодар недорого».

**Expected behavior:**

- Separate objects (different normalized form).
- `KR-REL-EXTENSION` link allowed; **must not** imply campaign parent/child (KR-ID-04).
- M-10 carries PRICE modifier + COMPARISON intent flag.

**Replay result:** **PASS**.

---

### ST-05 — Missing frequency

**Input:** M-17 — blank frequency cell.

**Expected behavior:**

- Object registers with phrase + provenance.
- `numeric_slots.freq.status = unknown` — **not** `0`, not `not_captured` (cell existed but empty) per NUM-03.
- Object-level SAFE UNKNOWN documents blank cell.
- Registry state may remain `registered` (not fully enriched on numeric).

**Replay result:** **PASS** — unknown vs zero distinction holds.

---

### ST-06 — Unknown region

**Input:** M-16 — blank region; M-15 — «Краснодарский край» vs session scope «Краснодар».

**Expected behavior:**

- M-16: `region_scope.status = unknown`; SAFE UNKNOWN «Demand region not supplied in export row».
- M-15: register with `region_scope.value = Краснодарский край`; SAFE UNKNOWN «Demand region (Краснодарский край) ≠ scope.region (Краснодар) — operator verification required» per charter §SAFE UNKNOWN.
- **No silent rewrite** to session scope.

**Replay result:** **PASS** — mismatch surfaced, not corrected.

---

### ST-07 — Provider conflict

**Input:** M-01 shows=12400 vs M-18 shows=11800 — same phrase, region, period, second mock export.

**Expected behavior:**

- `numeric_slots.freq.status = provider_conflict`.
- `conflict_values[]` preserves both `{ value: 12400, provider_ref: mock#M-01 }` and `{ value: 11800, provider_ref: mock#M-18 }`.
- SAFE UNKNOWN: «Numeric provider conflict — operator verification required».
- **No averaging, no prefer-latest** per NUM model / KR-AD-07.

**Replay result:** **PASS** — conflict preserved without resolution.

---

### Stress test summary

| Test | Scenario | Result |
|------|----------|--------|
| ST-01 | Same phrase duplicate | PASS |
| ST-02 | Same phrase different source | PASS |
| ST-03 | Lexical variant | PASS |
| ST-04 | Extension phrase | PASS |
| ST-05 | Missing frequency | PASS |
| ST-06 | Unknown / mismatched region | PASS |
| ST-07 | Provider conflict | PASS |

---

## Replay Findings

Evidence-backed observations only.

### What worked

| Finding | Evidence |
|---------|----------|
| **End-to-end absorb path exists** | Mock export → Snapshot → Observation → Keyword Object → Registry index — no redesign required |
| **Provider-agnostic numeric slots** | `KS-PROV-FUTURE-PROVIDER` accepts mock export without Wordstat-specific fields |
| **Multi-channel coexistence** | Seed + executed + suggestion + provider rows coexist with KO-04 separation |
| **Modifier + intent layering** | All 18 phrases tagged without collapsing to single intent class |
| **Integrity rules actionable** | Merge, conflict, SAFE UNKNOWN rules produced deterministic tabletop outcomes |
| **Collection model fits batch ingest** | `wordstat_batch` holds provider rows without cluster semantics |

### What felt awkward

| Finding | Evidence |
|---------|----------|
| **Manual modifier derivation assumed** | Replay applied tags by hand — capability model admits extraction algorithm undefined |
| **M-01 vs M-17 same phrase, different rows** | Identity tuple ambiguity when same normalized phrase appears twice with different numeric states — required replay assumption to keep separate ids |
| **Conflict on duplicate identity** | ST-07: model allows merge **or** separate object with conflict — implementation must pick policy (merge into one object with conflict_values vs two objects) |
| **Enriched vs registered boundary** | Missing freq leaves object at `registered` — operator must know enriched means «tags **or** numbers», not both required |
| **related_keyword_refs volume** | 18 provider rows + cross-links → graph grows quickly; no auto-link for lexical variants means sparse graph unless operator adds links |

### What required assumptions

| Assumption | Why needed |
|------------|------------|
| Modifier tags derived by tabletop lexical rules | No extraction runtime |
| `KS-PROV-FUTURE-PROVIDER` used instead of `future_wordstat` | Mock is generic provider, not Wordstat-branded |
| M-18 kept as separate object with conflict flag | Alternative valid path: merge M-01/M-18 provenance into one object |
| Suggestion/seed/executed objects constructed from replay refs S-01..S-03 | MVP has no keyword artifacts — cross-channel stress required synthetic refs |
| Intent flags marked `derived` not `declared` | No automated rule engine — manual stand-in for future extraction |

### What appears missing (from replay — not necessarily blockers)

| Gap | Replay signal | Classification |
|-----|---------------|----------------|
| **Implementation policy for conflict merge** | ST-07 ambiguity | Implementation Gap |
| **Modifier extraction rules document** | Manual tagging only | Model Gap (operational) |
| **Region code normalization** | «Краснодар» vs «Краснодарский край» — no code enum | Model Gap |
| **Observation layer spec** | Logical entity only — no ingest log shape | Implementation Gap |
| **JSON Schema / registry writer** | Tabletop only | Implementation Gap |
| **Multi-period trend array** | Single trend slot; no time series | Model Gap (Phase 2e extension per Wordstat charter G-07) |
| **Brand/competitor glossary** | Not exercised in mock rows | Model Gap — operator dependency |

---

## Gap Review

| ID | Description | Class | Blocker? |
|----|-------------|-------|----------|
| GAP-R01 | Modifier extraction algorithm undefined | **Model Gap** | **No** — manual pass sufficient for next gate |
| GAP-R02 | Provider conflict merge policy (one object vs two) | **Implementation Gap** | **No** — either path fits model |
| GAP-R03 | Region code / hierarchy normalization | **Model Gap** | **No** — SAFE UNKNOWN covers mismatch |
| GAP-R04 | Trend time-series array >2 points | **Model Gap** | **No** — defer to Phase 2e; freq-only replay sufficient |
| GAP-R05 | Observation ingest log shape | **Implementation Gap** | **No** — registry accepts objects directly in replay |
| GAP-R06 | JSON Schema + registry writer | **Implementation Gap** | **No** — expected; not authorized |
| GAP-R07 | Cross-session phrase catalog | **Architecture Gap** | **No** — explicitly out of scope |
| GAP-R08 | Generic third-party provider id beyond `future_*` | **Registry Gap** | **No** — `KS-PROV-FUTURE-PROVIDER` sufficient |
| GAP-R09 | Auto lexical-variant linking | **Registry Gap** | **No** — intentional omission per KR-ID-03 |
| GAP-R10 | Validation against real mqgt01 keyword artifacts | **Implementation Gap** | **No** — MVP has none; replay substitutes mock |

### Blocker determination

**No architecture blocker revealed.** All 18 mock rows and 7 stress scenarios absorbed without model amendment. Remaining gaps are **implementation**, **operational extraction**, or **deferred extensions** — consistent with [MIG-WORDSTAT-READINESS-CHARTER-v1.md](MIG-WORDSTAT-READINESS-CHARTER-v1.md) G-07 closure.

---

## Registry Integrity Validation

### Can identity rules survive?

**Yes.**

| Evidence |
|----------|
| KO-03 merge exercised (ST-01) |
| KO-04 / KO-05 channel separation exercised (ST-02) |
| KR-REL-LEXICAL_VARIANT without auto-merge (ST-03) |
| Region as identity/context dimension (M-15 vs M-01) |
| 21 distinct keyword_ids assigned without collision |

### Can provenance survive?

**Yes.**

| Evidence |
|----------|
| Each object carries ≥1 `provenance_records[]` entry |
| Cross-channel objects retain distinct `KS-PROV-*` ids |
| Merge rule KR-INT-01: provenance append-only on duplicate upsert |
| MOCK DATA flagged in provenance `safe_unknown` |

### Can SAFE UNKNOWN survive?

**Yes.**

| Evidence |
|----------|
| M-17 missing freq → `unknown`, not zero |
| M-16 blank region → explicit unknown |
| M-15 region mismatch → charter-aligned declaration |
| Session-level aggregation in registry `session_safe_unknown[]` |
| Empty modifier array distinguished from «modifiers unknown» per KS-DM-06 |

### Can provider_conflict survive?

**Yes.**

| Evidence |
|----------|
| M-18 vs M-01 → `provider_conflict` status |
| `conflict_values[]` preserves both numbers |
| No averaging / prefer-latest — KR-AD-07 honored |
| Operator override path documented (not exercised) |

### Can registry lifecycle survive?

**Yes.**

| Evidence |
|----------|
| Provider rows: observed → registered → enriched |
| M-17 stops at registered (numeric incomplete) |
| Collections assign batch without changing lifecycle |
| Deprecated path not required in replay — rule KR-TR-05 verified as design-only |
| Registry `open` state accepts all mock upserts |

---

## Final Verdict

### **REPLAY PASSED WITH GAPS**

### Evidence summary

| Criterion | Met? |
|-----------|------|
| Capability Model absorbs provider-style rows | **Yes** |
| Data Model creates Keyword Objects without redesign | **Yes** |
| Registry Model indexes, links, and integrity-rules hold | **Yes** |
| All 7 stress scenarios produce defined behavior | **Yes** |
| No ORCA bleed (forbidden fields, clustering, tiers) | **Yes** |
| Zero architecture blockers | **Yes** |
| Implementation / extraction gaps remain | **Yes** — expected |

**Not REPLAY FAILED:** No scenario required model amendment or contradicted normative rules.

**Not REPLAY PASSED (unqualified):** Modifier extraction, conflict merge policy, and trend time-series remain undefined — documented gaps, not failures.

---

## Recommended Next Step

1. **Human review** of this replay — confirm stress-test outcomes and conflict-merge policy preference.
2. **Close G-07** in Wordstat Readiness Charter — tabletop replay complete.
3. **Operator manual tag pass** on real mqgt01 seed list — validate modifier tagging against live phrases (no runtime).
4. **Phase 2g gate (optional):** Document provider conflict merge policy as implementation note — still no registry writer.
5. **Defer** real provider authorization until separate readiness decision — replay does **not** authorize Wordstat or any API.

**Stop condition:** If next work shifts to Wordstat UI, CSV ingest, or schema implementation — stop; split per Phase 2 boundaries.

---

## Architecture decisions (replay)

| ID | Decision | Rationale |
|----|----------|-----------|
| **MPR-01** | Mock provider labeled `MOCK-STAT-EXPORT`, not Wordstat | Avoid false provider claim |
| **MPR-02** | 18 rows + 3 cross-channel refs | Covers pilot vocabulary + stress dimensions |
| **MPR-03** | Verdict = PASSED WITH GAPS | Honest — no blockers, open implementation gaps |
| **MPR-04** | No model amendments proposed | Replay did not prove redesign necessity |
| **MPR-05** | Conflict merge left as implementation choice | Both paths model-valid |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) | Phase 2b — capabilities replayed |
| [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) | Phase 2c — Keyword Object shape |
| [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md) | Phase 2d — registry rules |
| [MIG-WORDSTAT-READINESS-CHARTER-v1.md](MIG-WORDSTAT-READINESS-CHARTER-v1.md) | G-07 replay gate |
| [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) | Phase 1 evidence |

---

*MIG Mock Provider Replay v1 · 2026-06-06 · tabletop only · MOCK DATA · no runtime · no Wordstat*
