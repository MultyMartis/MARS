# MIG Provider Connection Authorization v1

**Status:** **authorization** — human decision record (Phase 2g)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2g — Demand Surface Provider Connection Authorization  
**Prior artifacts:** [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) · [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) · [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) · [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md) · [MIG-WORDSTAT-READINESS-CHARTER-v1.md](MIG-WORDSTAT-READINESS-CHARTER-v1.md) · [MIG-MOCK-PROVIDER-REPLAY-v1.md](MIG-MOCK-PROVIDER-REPLAY-v1.md)  
**Validated market (pilot context):** Грузотакси / Краснодар / проект Триумф

**This document delivers:** candidate provider evaluation, authorization matrix, connection rules, human review gate, reality review, final verdict, recommended next step.

**This document does not deliver:** runtime, schemas, API clients, CSV ingest code, Wordstat UI automation, registry writer, ORCA handoff, or Phase 1 redesign.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This document **authorizes one demand provider path** for a **controlled, human-supervised pilot**. It does **not** authorize implementation, automation, or registry writer coding.

---

## Authorization gate status (G-01..G-07)

| Gate | Item | Status at authorization |
|------|------|---------------------------|
| **G-01** | Human authorization record (this document) | **Met** — this document |
| **G-02** | JSON Schema stub (Keyword Object, registry, demand snapshot) | **Not met** — blocks first real ingest |
| **G-03** | Snapshot → Keyword Object mapping spec | **Not met** — blocks first real ingest |
| **G-04** | Registry writer contract (logical upsert) | **Not met** — blocks first real ingest |
| **G-05** | Manifest `keyword_pass` flag path | **Not met** — blocks first real ingest |
| **G-06** | Operator review checklist | **Met** — §Human Review Gate below |
| **G-07** | Tabletop replay | **Met** — [MIG-MOCK-PROVIDER-REPLAY-v1.md](MIG-MOCK-PROVIDER-REPLAY-v1.md) — REPLAY PASSED WITH GAPS |

**Normative:** Authorization of the **provider path** is granted. **First real provider data ingest** remains blocked until G-02..G-05 are satisfied in separate design artifacts.

---

# REPORT — Provider Connection Authorization

## Candidate Review

Evaluation of demand provider classes against MIG Phase 2 foundation, MVP freeze evidence, and mock replay outcomes. Scoring is qualitative — **reality-first**, not feature wishlist.

### 1. Manual Wordstat Export

| Dimension | Assessment |
|-----------|------------|
| **Benefits** | Canonical RU-market demand source; raw file artifact preserves evidence; aligns with Keyword Intelligence v1 §3.5 primary path; lowest engineering surface; operator controls region and phrase list; mock replay absorbed export-shaped rows without model amendment |
| **Risks** | Operator burden per session; export column variance; region label inconsistency («Краснодар» vs «Краснодарский край»); duplicate re-export may produce numeric conflict; no trend time-series if export is single-period only |
| **Operational complexity** | **Low engineering / medium operator** — human runs Wordstat UI, downloads CSV/XLSX, attaches to session; no API credentials in MIG |
| **Reality quality** | **High** for phrase + frequency when export region matches session scope — independent of SERP recurrence |
| **Human review compatibility** | **High** — file is inspectable; operator verifies region, phrase coverage, and conflicts before registry freeze |

### 2. Wordstat API

| Dimension | Assessment |
|-----------|------------|
| **Benefits** | Repeatable capture; timestamped request ids; potential multi-period pulls; lower per-session operator time at scale |
| **Risks** | Access gating and quota unknown in repo; ToS/compliance not assessed; engineering before manual path validated; failure modes (partial quota, rate limit) need runtime handling not yet chartered |
| **Operational complexity** | **High** — credentials, client, error recovery, credential storage boundary |
| **Reality quality** | **High** (same underlying source as export) — when API returns same columns as export |
| **Human review compatibility** | **Medium** — response JSON less familiar to operators than spreadsheet; still reviewable with raw payload preserved |

### 3. Third-party keyword provider

| Dimension | Assessment |
|-----------|------------|
| **Benefits** | May offer bundled metrics (CPC, difficulty, SERP features); faster multi-engine coverage |
| **Risks** | Provenance opaque vs Yandex-native demand; schema variance per vendor; cost; `KS-PROV-FUTURE-PROVIDER` is generic placeholder — no vendor-specific evidence contract in repo; numbers may not match Wordstat semantics |
| **Operational complexity** | **High** — subscription, API keys, column mapping per vendor, ongoing vendor drift |
| **Reality quality** | **Unknown** — not validated on pilot market; cross-provider conflict likely if mixed with Wordstat |
| **Human review compatibility** | **Medium–Low** — operator must understand vendor methodology; harder to verify against session scope |

### 4. Search suggestions only

| Dimension | Assessment |
|-----------|------------|
| **Benefits** | Surfaces query language variants; complements seed list; low cost if captured from existing SERP/session context |
| **Risks** | **No frequency evidence** — incomplete Demand Surface per Phase 2 charter; suggestion order ≠ demand volume; recursive expansion forbidden (KI-03); cannot satisfy `frequency_evidence` |
| **Operational complexity** | **Low–Medium** — paste or API; but does not deliver primary numeric demand signal |
| **Reality quality** | **Partial** — phrase discovery only; KS-06 forbids inferring volume from suggestions |
| **Human review compatibility** | **High** for strings; **N/A** for numeric demand gate |

### 5. Operator-entered demand data

| Dimension | Assessment |
|-----------|------------|
| **Benefits** | Zero external dependency; seeds already proven in Phase 1 manifests |
| **Risks** | **Not independent demand evidence** — re-enters declared scope; no numeric signal unless operator types numbers (fabrication risk); violates acquisition mission if presented as provider demand |
| **Operational complexity** | **Lowest** |
| **Reality quality** | **Low as demand provider** — appropriate for `operator_seed` channel, not `future_wordstat` / provider numeric |
| **Human review compatibility** | **N/A** — seeds already human-declared; not a substitute for provider connection |

### Recommended first provider (single)

**Manual Wordstat Export** — operator-downloaded CSV/XLSX from Yandex Wordstat UI, scoped to session region and approved phrase list, preserved as raw snapshot evidence, mapped to Keyword Registry through the chartered ingest path (when G-02..G-05 exist).

**Why this provider first**

1. **Architecture fit proven** — mock replay (18 rows, 7 stress tests) absorbed export-shaped data without redesign ([MIG-MOCK-PROVIDER-REPLAY-v1.md](MIG-MOCK-PROVIDER-REPLAY-v1.md)).
2. **Prior art in repo** — Keyword Intelligence v1 §3.5 names manual export as **Phase 2 MVP for Wordstat**; Readiness Charter recommended this path over API/automation.
3. **Evidence discipline** — raw file satisfies «preserve raw evidence»; operator inspects region and conflicts before registry authority.
4. **Lowest connection risk** — no API credentials, no browser bot fragility, no third-party semantic mismatch.
5. **Pilot market alignment** — Грузотакси Краснодар query set already declared ([multi-query-market-query-set-v1.md](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/multi-query-market-query-set-v1.md)); Wordstat is the native demand instrument for Yandex RU local commercial queries.

**Why others are not first**

| Provider class | Not first because |
|----------------|-------------------|
| **Wordstat API** | Same source, higher connection cost; manual path must validate operator workflow and mapping before automation |
| **Third-party provider** | Provenance and numeric semantics unvalidated; introduces vendor dependency before Yandex-native baseline |
| **Suggestions only** | Does not deliver `frequency_evidence` — Demand Surface remains incomplete for pack `search_demand` / `frequency_signals` sections |
| **Operator input** | Already captured as seeds; not an external demand signal; typing volumes would corrupt evidence grade |

---

## Authorization Matrix

| Provider | Authorized | Condition |
|----------|------------|-----------|
| **Manual Wordstat Export** | **YES — limited pilot** | (1) Human-supervised session on validated market only (Грузотакси Краснодар first). (2) G-02..G-05 complete before any real rows enter `keyword_registry`. (3) Raw export file preserved as SoT with `import_method: manual_export`. (4) Phrase list ⊆ approved query set + operator-declared expansion only — no MIG-generated queries. (5) Region = `scope.region` (Краснодар) or explicit SAFE UNKNOWN on mismatch. (6) Human Review Gate (below) passed before registry authoritative. (7) `keyword_pass` set only after review — not at file drop. |
| **Wordstat API** | **NO** | Deferred until manual export pilot completes one reviewed cycle and API access/ToS assessed in separate charter |
| **Third-party Provider** | **NO** | No vendor selected; no provenance contract; generic `KS-PROV-FUTURE-PROVIDER` insufficient for production vendor without named evidence spec |
| **Search suggestions only** | **NO** (as primary demand provider) | May supplement registry as `search_suggestion` channel **after** numeric baseline exists — not authorized as first Demand Surface provider |
| **Operator-entered demand data** | **NO** (as demand provider) | Remains `operator_seed` only; does not satisfy provider connection authorization |

---

## Connection Rules

Minimum normative rules for any authorized provider connection. Derived from Phase 2c/2d models and mock replay stress tests.

| ID | Rule |
|----|------|
| **PCR-01** | **Raw evidence preserved** — provider source file or API response body stored as snapshot SoT; registry objects reference snapshot via `evidence_refs[]`; snapshot is not discarded after mapping |
| **PCR-02** | **Numbers remain raw** — `numeric_slots.*.value` stores provider-returned numbers without rescaling, rounding policy, or unit conversion unless export documents conversion and operator approves |
| **PCR-03** | **No conflict averaging** — duplicate phrase/region/period with different values → `provider_conflict` + `conflict_values[]`; never mean, max, or prefer-latest (KR-AD-07, NUM-06) |
| **PCR-04** | **Registry entry required** — provider rows enter only through Keyword Registry upsert path; ad hoc spreadsheets in session folder without registry linkage are **non-authoritative** |
| **PCR-05** | **No SERP inference** — SERP recurrence, competitor frequency, or landing prominence **must not** populate `numeric_slots.freq` (KS-06, NUM-02) |
| **PCR-06** | **Missing ≠ zero** — blank frequency cell → `status: unknown`; absent column → `not_captured`; never `0` unless provider explicitly returned zero |
| **PCR-07** | **Provenance mandatory** — every Keyword Object from provider carries ≥1 `provenance_records[]` with `KS-PROV-FUTURE-WORDSTAT` (or successor id) and `import_method` |
| **PCR-08** | **Region honesty** — export region ≠ session `scope.region` → object-level `safe_unknown[]`; no silent rewrite to session scope |
| **PCR-09** | **Channel separation** — same normalized phrase from seed vs provider remains separate objects or explicit merge per KO-04; provider numbers do not attach to seed objects without provider provenance |
| **PCR-10** | **Append-only provenance** — re-import merges provenance records; does not delete prior provider evidence |
| **PCR-11** | **No ORCA fields** — forbidden: cluster_id, priority tiers, intent enums, campaign grouping, volume-based recommendations |
| **PCR-12** | **Manifest truth** — `keyword_pass: true` only when provider ingest completed **and** Human Review Gate passed |

---

## Human Review Gate

Minimum viable checklist before provider-sourced data becomes **registry-authoritative** (eligible for pack projection of `frequency_signals`). No bureaucracy — five checks.

| # | Operator must confirm | Fail action |
|---|----------------------|-------------|
| **HR-01** | **Raw snapshot present** — export file attached; filename, export date, and operator id recorded in provenance | Do not register rows |
| **HR-02** | **Region match** — Wordstat region matches session `scope.region` (Краснодар) **or** every mismatch row has SAFE UNKNOWN | Do not freeze registry |
| **HR-03** | **Phrase coverage declared** — which approved queries have provider rows; which are missing; partial coverage stated in session `safe_unknown[]` | Do not imply complete demand surface |
| **HR-04** | **Conflicts surfaced** — duplicate phrase/period with different shows flagged `provider_conflict`; operator acknowledges, does not pick silent winner | Do not average or hide |
| **HR-05** | **No strategy bleed** — review confirms no priority labels, clusters, or recommendations added during ingest | Reject contaminated registry revision |

**Optional (not blocking first pilot):** modifier tags on provider phrases — enrich may remain manual per GAP-R01.

**Registry state after gate:** operator may mark registry revision reviewed; pack `frequency_signals` projection remains **draft** until separate research pack approval workflow exists (MVP freeze: no `research_pack.approved.md`).

---

## Reality Review

### If authorization is granted, what is the safest first pilot?

**Recommended pilot:** **Keyword demand capture pass** on existing market **Грузотакси / Краснодар / проект Триумф**, bound to approved query set `multi-query-market-query-set-v1` (11 queries), **without** re-running Phase 1 SERP or website acquisition.

| Pilot parameter | Value | Evidence |
|-----------------|-------|----------|
| **Market** | Грузотакси Краснодар | Four validated MVP sessions — [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) |
| **Phrase list** | q01–q11 from [multi-query-market-query-set-v1.md](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/multi-query-market-query-set-v1.md) | Same set used in mqgt01 multi-query SERP |
| **Region** | Краснодар (Yandex Wordstat region aligned to `lr=35` scope) | mqgt01 manifest scope |
| **Session type** | New session or additive **keyword pass** on logical descendant of mqgt01 — **not** full stack re-capture | Phase 1 freeze: keyword pass is additive |
| **Provider action** | Operator runs Wordstat UI → exports CSV/XLSX for declared phrases + region → attaches raw file | Manual Wordstat Export (authorized path) |
| **Explicit non-goals** | No SERP re-fetch; no landing re-acquisition; no ORCA handoff; no API; no third-party tool | Authorization scope |
| **Coverage honesty** | Declare that SERP groundtruth had 8/11 queries (q05–q07 failed) — Wordstat may still capture all 11 phrases; document divergence | Freeze §Known Limitations |

**Why this is safest**

1. **Single proven market** — only market with four session evidence chain.
2. **Phrase list pre-approved** — no query generation inside MIG.
3. **Isolated from Phase 1 spine** — demand pass does not touch proven SERP/landing regression path.
4. **Comparable cross-layer check** — operator can compare Wordstat rows to mqgt01 executed queries and market-surface recurrence **without merging** layers (KS-06).
5. **Partial failure tolerance** — missing export rows follow ST-05 (unknown freq), not session failure.

**Pilot success criteria (authorization level — not implementation)**

- Raw export preserved with provenance.
- All 11 phrases attempted; missing rows declared SAFE UNKNOWN.
- At least one `provider_conflict` or region-mismatch exercise documented if encountered — or explicit «none observed» in review notes.
- Registry revision reviewed per Human Review Gate.
- Phase 1 artifacts unchanged and still valid.

---

## Final Verdict

### **LIMITED PROVIDER AUTHORIZATION**

| Verdict option | Selected? | Evidence |
|----------------|-----------|----------|
| **NO PROVIDER AUTHORIZED** | No | G-07 replay passed; architecture accepts provider; manual export path low-risk and pre-recommended in Keyword Intelligence v1 |
| **LIMITED PROVIDER AUTHORIZATION** | **Yes** | One provider class authorized (Manual Wordstat Export) under strict pilot constraints; G-02..G-05 still block real ingest; no API/automation/third-party |
| **FULL PROVIDER AUTHORIZATION** | No | Registry writer, schema stub, manifest path, and one real ingest cycle not proven; HITL keyword approval not in MVP evidence |

### Evidence summary

| Criterion | Met? |
|-----------|------|
| Phase 2 architecture accepts provider rows without redesign | **Yes** — Readiness Charter PARTIALLY READY; replay PASSED WITH GAPS |
| Mock replay — no architecture blocker | **Yes** — [MIG-MOCK-PROVIDER-REPLAY-v1.md](MIG-MOCK-PROVIDER-REPLAY-v1.md) |
| First provider path selected with justification | **Yes** — Manual Wordstat Export |
| Other provider classes deferred with rationale | **Yes** — Authorization Matrix |
| Connection rules and review gate defined | **Yes** — PCR-01..PCR-12, HR-01..HR-05 |
| Safe pilot named on real market | **Yes** — Грузотакси Краснодар, mqgt01 query set |
| Implementation authorized | **No** — G-02..G-05 open; explicit stop condition |

**Confidence:** **B** — strong architectural and tabletop evidence; operational gates incomplete.

---

## Recommended Next Step

1. **Human review** of this authorization — confirm **LIMITED PROVIDER AUTHORIZATION** and Manual Wordstat Export as sole first path.
2. **Complete G-02 + G-03** — JSON Schema stub + snapshot-to-Keyword-Object mapping one-pager in `contracts/` (design only).
3. **Complete G-04 + G-05** — registry writer contract (logical) + manifest `keyword_pass` flag specification.
4. **Operator dry run (no registry writer):** Operator performs Wordstat export for q01–q11 / Краснодар and stores raw file in pilot folder **without** claiming registry authority — validates operator workflow before ingest.
5. **First real ingest** — only after G-02..G-05 reviewed and Human Review Gate checklist attached to session.
6. **Defer** Wordstat API, third-party providers, and suggestion-only demand capture until manual pilot cycle completes.

**Stop condition:** CSV ingest scripts, API clients, browser automation, or pack builder changes — split to implementation gate; not covered by this authorization.

---

## Architecture decisions (authorization)

| ID | Decision | Rationale |
|----|----------|-----------|
| **PCA-01** | First authorized provider = **Manual Wordstat Export** | Lowest risk; architecture-aligned; Keyword Intelligence v1 primary path |
| **PCA-02** | Verdict = **LIMITED PROVIDER AUTHORIZATION** | Path authorized; ingest blocked on G-02..G-05 |
| **PCA-03** | Wordstat API / third-party / suggestions / operator numeric **not authorized** | Defer until baseline proven or wrong evidence type |
| **PCA-04** | Pilot market locked to **Грузотакси Краснодар** | Only MVP-validated market in freeze |
| **PCA-05** | Mock replay does **not** substitute for real export | Replay validates model; real export validates operator workflow |
| **PCA-06** | Conflict merge policy remains implementation choice | Both paths model-valid per MPR-05 |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-WORDSTAT-READINESS-CHARTER-v1.md](MIG-WORDSTAT-READINESS-CHARTER-v1.md) | G-01..G-07 gate definition |
| [MIG-MOCK-PROVIDER-REPLAY-v1.md](MIG-MOCK-PROVIDER-REPLAY-v1.md) | G-07 tabletop evidence |
| [mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md) | Manual export reference §3.5 |
| [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) | Numeric and provenance rules |
| [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md) | Registry authority model |
| [multi-query-market-query-set-v1.md](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/multi-query-market-query-set-v1.md) | Pilot phrase list |

---

*MIG Provider Connection Authorization v1 · 2026-06-06 · authorization only · no runtime · no Wordstat integration*
