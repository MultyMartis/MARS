# MIG Provider Mapping Spec v1

**Status:** **normative** — mapping rules only (Phase 2g / G-03)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2g — Provider Infrastructure Contracts  
**Gate closed:** **G-03** — Provider column → Keyword Object field mapping  
**Prior artifacts:** [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md) · [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-REGISTRY-MODEL-v1.md](MIG-KEYWORD-REGISTRY-MODEL-v1.md) · [MIG-MOCK-PROVIDER-REPLAY-v1.md](../reports/MIG-MOCK-PROVIDER-REPLAY-v1.md)  
**Validated market (examples):** Грузотакси / Краснодар / проект Триумф

**This document delivers:** provider column → Keyword Object field mapping, mapping rules, SAFE UNKNOWN handling, provider_conflict handling.

**This document does not deliver:** parser, CSV ingest code, API client, registry writer, or validation runtime.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This spec defines **logical mapping** from provider export shape to Keyword Surface objects. It does **not** authorize automated ingest.

---

## Mapping scope

| In scope | Out of scope |
|----------|--------------|
| Manual Wordstat Export (primary authorized path) | Wordstat API response mapping (deferred) |
| Generic demand provider table (phrase + region + period + frequency) | Third-party vendor-specific transforms |
| Snapshot row → Keyword Observation → Keyword Object | Modifier/intent extraction algorithms |
| Column alias recognition (RU + EN headers) | Unit conversion, rounding, tier labels |

**Primary provider:** Manual Wordstat Export per [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md).

---

## Mapping pipeline (logical)

```text
Raw export file (CSV/XLSX) — preserved as SoT
        │
        ▼
Keyword Snapshot (header + rows[] + raw_columns)
        │
        ▼
Keyword Observation (per row)
        │
        ▼
Keyword Object (registry upsert input)
```

**Normative:** Raw file **must** be stored before mapping (PCR-01). Mapping **must not** discard unmapped columns — preserve in **raw_columns**.

---

## Provider column → Keyword Object field map

### Core columns (Wordstat manual export — illustrative)

| Provider column (aliases) | Snapshot field | Keyword Object field | Required | Notes |
|---------------------------|----------------|----------------------|----------|-------|
| **phrase**, «Запрос», «Query», «Keyword» | `rows[].phrase` | **phrase** | **Yes** | Exact cell — trim outer whitespace only |
| *(derived)* | — | **phrase_normalized** | Optional | KO-NORM-* — lowercase, NFC, whitespace collapse |
| **region**, «Регион», «Region», «Geo» | `rows[].region` or header `region_label` | **region_scope** | Optional | See §Region alignment |
| **period**, «Период», «Period», «Month» | `rows[].period` or header `period` | **period_scope** | Optional | See §Period alignment |
| **frequency**, «Частота», «Shows», «Количество запросов», «Impressions» | `rows[].frequency` | **numeric_slots.freq** | Optional | See §Frequency mapping |
| **frequency_share**, «Доля», «Share», «shows_share» | `rows[].frequency_share` | **numeric_slots.share** | Optional | Absent column → share `not_captured` |
| **trend**, «Тренд», «Δ», «Change» | `rows[].trend` | **numeric_slots.trend** | Optional | Absent column → trend `not_captured` |
| **all other columns** | `rows[].raw_columns` | **numeric_slots.*.raw_columns** (object level) | **Yes** when present | Verbatim preservation |

### Provenance and identity (not from export columns)

| Logical source | Keyword Object field | Value |
|----------------|---------------------|-------|
| Mapping spec | **source_type** | `future_wordstat` (Wordstat) or `future_provider` (generic) |
| Mapping spec | **provenance_records[].provenance_id** | `KS-PROV-FUTURE-WORDSTAT` or `KS-PROV-FUTURE-PROVIDER` |
| Session spine | **session_id** | Owning session |
| Snapshot header | **provenance_records[].import_method** | `manual_export` |
| Snapshot header | **provenance_records[].evidence_refs[]** | `{ snapshot_ref, row_id, source_file_ref }` |
| Mapping spec | **evidence_grade** | `provider` when from export; `operator` when manual paste without file |

### Scope fields from session (cross-check, not blind copy)

| Session / manifest field | Keyword Object cross-check |
|--------------------------|----------------------------|
| `scope.region` | **region_scope** must match or declare SAFE UNKNOWN |
| Research Request seed list | Phrase coverage checklist — not a column map |
| `capture_profile.keyword_pass` | Set only after review — see pass manifest contract |

---

## Mapping rules

| Rule id | Statement |
|---------|-----------|
| **MAP-01** | One export row → one Keyword Observation → zero or one Keyword Object upsert (identity rules may merge into existing object) |
| **MAP-02** | **phrase** copied exactly from provider cell — no stemming, no synonym substitution |
| **MAP-03** | Blank **phrase** cell → row skipped; row-level SAFE UNKNOWN in snapshot stats — **no** Keyword Object |
| **MAP-04** | All mapped numbers stored **raw** — no rescaling, no «K» suffix expansion unless export documents unit and operator approves (PCR-02) |
| **MAP-05** | Unrecognized columns → **raw_columns** only — do not drop |
| **MAP-06** | Header-level region/period apply to all rows **unless** row overrides — row wins on conflict |
| **MAP-07** | Export row for phrase already present as **operator_seed** → **separate** Keyword Object per KO-04 unless operator merge — provider numbers **must not** attach to seed object without provider provenance (PCR-09) |
| **MAP-08** | Same normalized phrase + same `future_wordstat` + same engine (null for Wordstat) → **merge** provenance into one object (KO-03) |
| **MAP-09** | Re-import of identical snapshot → **idempotent merge** — no duplicate objects (KR-INT idempotency) |
| **MAP-10** | Missing frequency cell ≠ zero — see §Frequency mapping |
| **MAP-11** | Forbidden ORCA/strategy fields **must not** be populated during mapping (PCR-11) |

---

## Region alignment

| Condition | **region_scope** result | SAFE UNKNOWN |
|-----------|-------------------------|--------------|
| Row region = session `scope.region` (label match after trim) | `{ value: "Краснодар", status: "declared" }` | None required |
| Row region = provider code mapped to session region | `{ value: "Краснодар", code: "35", status: "declared" }` | None if mapping documented in snapshot `column_mapping` |
| Row region differs (e.g. «Краснодарский край» vs «Краснодар») | `{ value: "<export label>", status: "declared" }` | **Required:** «Export region ≠ session scope.region — demand geography unverified for session scope» |
| Blank region cell | `{ status: "unknown" }` | **Required:** «Provider row region missing — geographic scope unknown» |
| Header region only, no row column | Use header **region_label** | Mismatch vs session → object-level SAFE UNKNOWN (PCR-08) |

**Normative:** No silent rewrite of export region to session region.

---

## Period alignment

| Condition | **period_scope** result | SAFE UNKNOWN |
|-----------|-------------------------|--------------|
| Export provides month (e.g. `2026-05`) | `{ value: "2026-05", status: "declared" }` | None |
| Export provides «month» / «week» without date | `{ value: "month", status: "partial" }` | Optional: «Exact period window not in export» |
| No period in export | `{ status: "not_applicable" }` or `{ status: "unknown" }` | **Required** when numeric_slots populated: «Period for frequency values unknown» |
| Row period ≠ header period | Row period wins | Object-level SAFE UNKNOWN «Row period differs from export header» |

---

## Frequency mapping

| Provider cell state | **numeric_slots.freq.status** | **value** | SAFE UNKNOWN |
|---------------------|-------------------------------|-----------|--------------|
| Numeric value present | `known` | Raw number as returned | Optional column semantics note |
| Blank / empty cell | `unknown` | absent | «Frequency cell empty for phrase» |
| Column absent in export | `not_captured` | absent | Snapshot-level: «Frequency column not present in export» |
| Non-numeric text | `unknown` | absent | «Frequency cell non-numeric — value unreadable» |
| Provider explicitly returns `0` | `known` | `0` | None — zero is valid provider evidence |
| No Wordstat pass for session | `not_captured` | absent | «Frequency evidence not captured for this session» |

**Share and trend slots:** Same status-first rules. Absent columns → entire slot `not_captured` (NUM-01).

---

## SAFE UNKNOWN handling

### When to declare SAFE UNKNOWN (mandatory)

| Situation | Level | Example declaration |
|-----------|-------|---------------------|
| Region mismatch vs session | Object | «Export region ≠ session scope.region» |
| Missing region cell | Object + snapshot row | «Provider row region missing» |
| Missing frequency cell | Object | «Frequency cell empty for phrase» |
| Unmapped export columns | Snapshot | «Columns X, Y not mapped — preserved in raw_columns» |
| Phrase not in approved query set | Session | «Provider phrase outside approved query set — operator expansion» |
| Partial phrase coverage | Session | «Provider rows missing for q05, q06, q07» |
| Mock / tabletop data | Object | «MOCK DATA — not real Wordstat» (replay only) |

### When empty SAFE UNKNOWN is valid

| Situation | Allowed empty? |
|-----------|----------------|
| Fully mapped row, region match, frequency known | **Yes** — `safe_unknown: []` |
| Modifier extraction not run | **No** — use Phase 2c modifier unknown OR empty tags with explicit unknown |
| Complete export coverage, all checks pass | Session may be empty if no gaps |

### SAFE UNKNOWN must not

| Forbidden | Reason |
|-----------|--------|
| Replace `provider_conflict` | Conflict is explicit status, not unknown |
| Infer frequency from SERP | KS-06, NUM-02 |
| Default missing freq to `0` | NUM-03 |
| Hide duplicate conflicting values | PCR-03 |

---

## provider_conflict handling

### Trigger conditions

| Condition | Result |
|-----------|--------|
| Second ingest: same `phrase_normalized` + same `source_type` (`future_wordstat`) + same **region_scope** + same **period_scope** + **different** frequency value | `numeric_slots.freq.status: provider_conflict` |
| Same row ingested from two export files with different shows | `provider_conflict` |
| Manual operator correction row vs prior export row (same identity tuple) | `provider_conflict` unless operator deprecates prior object |

### Required object shape on conflict

| Field | Requirement |
|-------|-------------|
| **numeric_slots.freq.status** | `provider_conflict` |
| **numeric_slots.freq.conflict_values[]** | Each entry: `{ value, provider_ref, capture_time, source_file_ref }` |
| **numeric_slots.freq.value** | **Absent** or null — **no single winner** |
| **safe_unknown[]** | Must include «Numeric provider conflict — operator verification required» |
| **provenance_records[]** | Append both captures — KR-INT-01 |

### Forbidden conflict resolution (normative)

| Forbidden action | Rule |
|------------------|------|
| Average conflicting values | PCR-03, KR-AD-07 |
| Prefer latest export silently | PCR-03 |
| Prefer maximum shows | ORCA-style interpretation |
| Overwrite prior provenance | KR-INT-01 |

### Operator override (future implementation gate)

Operator may attach **new object** or **operator provenance record** with `evidence_grade: operator` documenting verified winner — **must not** delete prior `conflict_values[]`. Deprecation of incorrect object uses registry writer **deprecate** behavior (G-04).

---

## Worked examples (Грузотакси / Краснодар — tabletop)

### Example A — standard row (mock M-01)

| Provider | → Keyword Object |
|--------|------------------|
| phrase: `грузотакси краснодар` | **phrase** / **phrase_normalized** |
| region: `Краснодар` | **region_scope** declared — matches session |
| period: `2026-05` | **period_scope** declared |
| frequency: `12400` | **numeric_slots.freq**: status=`known`, value=`12400` |
| provenance | **KS-PROV-FUTURE-WORDSTAT**, import_method=`manual_export` |

### Example B — region mismatch (mock M-15)

| Provider | → Keyword Object |
|--------|------------------|
| phrase: `грузотакси краснодар` | same phrase |
| region: `Краснодарский край` | **region_scope** with export label + SAFE UNKNOWN vs session «Краснодар» |
| frequency: `15200` | freq status=`known` — number stored raw; geography flagged |

### Example C — missing frequency (mock M-17)

| Provider | → Keyword Object |
|--------|------------------|
| frequency: *(blank)* | **numeric_slots.freq**: status=`unknown` |
| safe_unknown | «Frequency cell empty for phrase» |

### Example D — provider conflict (mock M-01 vs M-18)

| Provider | → Keyword Object |
|--------|------------------|
| First export shows: `12400` | freq status=`known` |
| Second export shows: `11800` (same phrase/region/period) | freq status=`provider_conflict`; conflict_values holds both |
| safe_unknown | «Numeric provider conflict — operator verification required» |

### Example E — seed vs Wordstat (cross-channel)

| Channel | → Keyword Object |
|---------|------------------|
| Seed «грузотакси Краснодар» | **source_type**: `operator_seed` — no numeric_slots |
| Wordstat row «грузотакси краснодар» | **source_type**: `future_wordstat` — separate object (KO-04) |
| Optional link | **related_keyword_refs[]**: `KR-REL-CHANNEL_ECHO` |

---

## Column alias reference (non-exhaustive)

Operators **must** declare actual headers in snapshot **column_mapping**. Recognized aliases:

| Logical slot | Accepted header aliases (case-insensitive, trim) |
|--------------|--------------------------------------------------|
| phrase | phrase, query, keyword, запрос, ключевое слово, поисковый запрос |
| region | region, geo, регион, geo name |
| period | period, month, week, период, месяц |
| frequency | frequency, shows, impressions, count, частота, количество запросов, показы |
| frequency_share | share, shows_share, доля, доля показов |
| trend | trend, change, delta, тренд, изменение |

**Unrecognized header:** Map entire row to **raw_columns**; declare snapshot SAFE UNKNOWN «Column `<name>` not mapped».

---

## Architecture decisions (mapping spec)

| ID | Decision | Rationale |
|----|----------|-----------|
| **MAP-AD-01** | Wordstat manual export is **reference mapping** | Sole authorized provider path |
| **MAP-AD-02** | Status-first numeric mapping | Aligns Phase 2c NUM model |
| **MAP-AD-03** | Region mismatch → SAFE UNKNOWN, not rewrite | PCR-08, mock replay ST-03 |
| **MAP-AD-04** | Conflict preserves all values | Mock replay ST-04; HR-04 |
| **MAP-AD-05** | Seed / Wordstat separation default | KO-04, PCR-09 |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md) | Field stub (G-02) |
| [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) | Upsert after mapping (G-04) |
| [MIG-MOCK-PROVIDER-REPLAY-v1.md](../reports/MIG-MOCK-PROVIDER-REPLAY-v1.md) | Tabletop validation |
| [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) | §3.7 logical snapshot reference |

---

*MIG Provider Mapping Spec v1 · 2026-06-06 · mapping rules only · G-03 closed · no parser · no runtime*
