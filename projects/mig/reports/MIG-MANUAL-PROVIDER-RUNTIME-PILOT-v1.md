# MIG Manual Provider Runtime Pilot v1

**Status:** **pilot charter** — Phase 3a runtime pilot definition (human-supervised)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 3a  
**Phase:** 3a — Manual Provider Runtime Pilot  
**Prior artifacts:** [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) · [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) · [MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md](../contracts/MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md) · [MIG-KEYWORD-SCHEMA-STUB-v1.md](../contracts/MIG-KEYWORD-SCHEMA-STUB-v1.md) · [MIG-PROVIDER-MAPPING-SPEC-v1.md](../contracts/MIG-PROVIDER-MAPPING-SPEC-v1.md) · [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](../contracts/MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) · [MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md](../contracts/MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md)

**This document delivers:** first Demand Surface runtime pilot definition — scope, artifact chain, inventory, success/failure criteria, reality review, readiness verdict.

**This document does not deliver:** runtime, parser, registry writer code, API clients, n8n graphs, ORCA handoff, automation, or Phase 1 redesign.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This pilot proves that **real provider data** can traverse the Demand Surface architecture under **human supervision**. It does **not** prove automation, scale, or unattended ingest.

**Authorization in force:** **LIMITED PROVIDER AUTHORIZATION** — Manual Wordstat Export only ([MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md)).

**Infrastructure verdict in force:** **INFRASTRUCTURE READY FOR MANUAL PROVIDER PILOT** — G-01..G-07 design gates closed ([MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md](../contracts/MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md)).

---

# REPORT — Manual Provider Runtime Pilot

## Pilot Scope

### Purpose

Execute the **first real Demand Surface runtime pilot** — a single human-supervised cycle proving that Manual Wordstat Export data can traverse:

```text
Wordstat Export → Keyword Snapshot → Keyword Observation → Keyword Registry → Human Review → keyword_pass
```

**Explicit non-goals:** APIs, automation, n8n, ORCA, scaling, SERP re-capture, website re-acquisition, registry writer implementation, pack approval workflow.

### Market binding

| Parameter | Value | Evidence |
|-----------|-------|----------|
| **Market** | Грузотакси Краснодар | Four validated MVP sessions — [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) |
| **Project** | Триумф | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` |
| **Pilot package** | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/` | Existing groundtruth evidence chain |
| **Logical parent session** | `mig-20260604-mqgt01` | Same query set used in multi-query SERP — phrase list pre-approved |

### Approved query set (verified)

Source: [multi-query-market-query-set-v1.md](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/multi-query-market-query-set-v1.md) · [multi-query-market-query-set-v1.json](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/multi-query-market-query-set-v1.json)

| ID | Query | Role |
|----|-------|------|
| **q01** | грузотакси Краснодар | primary |
| **q02** | грузовое такси Краснодар | wording_variant |
| **q03** | газель Краснодар | supporting |
| **q04** | грузоперевозки Краснодар | category_broad |
| **q05** | перевозка мебели Краснодар | supporting |
| **q06** | квартирный переезд Краснодар | supporting |
| **q07** | вызов газели Краснодар | commercial_variant |
| **q08** | газель с грузчиками Краснодар | supporting |
| **q09** | грузовое такси с грузчиками Краснодар | supporting |
| **q10** | грузоперевозки по Краснодару | geo_variant |
| **q11** | заказать газель Краснодар | commercial_variant |

**Verification:** 11 queries declared in both `.md` and `.json`; machine-readable set matches markdown table. Phrase list ⊆ approved set — **no MIG-generated queries** (PCR authorization rule).

**Cross-layer honesty:** Phase 1 SERP groundtruth captured **8/11** queries (q05–q07 `execution_status: failed` in mqgt01). Wordstat pilot **may** still attempt all 11 phrases — demand and SERP layers are **independent** (KS-06). Divergence must be declared in `keyword_pass_safe_unknown[]`, not merged.

### Region assumptions

| Assumption | Value | Authority |
|------------|-------|-----------|
| **Session scope.region** | `Краснодар` | mqgt01 `session_manifest.json` `scope.region` |
| **Yandex geo alignment** | `lr=35` (Краснодар) | multi-query-market-query-set-v1 §Scope binding |
| **Wordstat region** | Operator selects **Краснодар** (city) in Wordstat UI | Operator action — must match session scope or declare SAFE UNKNOWN per PCR-08 |
| **Region label variance** | «Краснодар» vs «Краснодарский край» possible in export | HR-02: mismatch → object-level `safe_unknown[]`; no silent rewrite |

**Normative:** Export region ≠ `scope.region` → **SAFE UNKNOWN**, not session failure.

### Period assumptions

| Assumption | Value | Notes |
|------------|-------|-------|
| **Default period** | Operator-declared at export time | Wordstat UI period (e.g. month, week) — **not pre-fixed in repo** |
| **Snapshot header `period`** | Record exact Wordstat period label selected | e.g. `month`, `2026-05`, or `unknown` if UI unclear |
| **Cross-session comparability** | **Not required** for first pilot | Single review cycle; re-export diff policy = SAFE UNKNOWN (KR revision rules) |
| **Trend columns** | Optional — map to `numeric_slots.trend` if present | Multi-point history underspecified — declare gap if export contains series |

**SAFE UNKNOWN:** Exact Wordstat period semantics for this export are **unknown until operator records** `exported_at` + `period` in snapshot header.

### Session type

| Parameter | Value |
|-----------|-------|
| **Session kind** | New keyword-demand session (recommended id pattern: `mig-YYYYMMDD-kwrd01`) |
| **Location** | `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-<session_id>/` |
| **Phase 1 touch** | **None** — no SERP re-fetch, no website re-acquisition |
| **Provider** | Manual Wordstat Export only |
| **Review cycles** | **One** — single export → single review → single `keyword_pass` decision |

### Expected artifacts (pilot deliverables)

| Stage | Artifact | Required at pilot end? |
|-------|----------|------------------------|
| Export | Raw `wordstat-export.*` (CSV/XLSX) | **Yes** — PCR-01 |
| Snapshot | `wordstat_snapshot.{capture_id}.json` | **Yes** — KP-PENDING+ |
| Observation | Logical ingest units (may be inline in review notes if no writer) | **Yes** — at least documented per row |
| Registry | `keyword_registry.json` (revision 1) | **Yes** for KP-COMPLETE — manual authorship per G-04 |
| Review | `keyword_review.md` | **Yes** — HR-01..HR-05 record |
| Manifest | `session_manifest.json` with keyword pass fields | **Yes** — `keyword_pass: true` only after review |

---

## Artifact Chain

Explicit chain referencing Phase 2g contracts. **No implementation** — operator or manual JSON authorship following contracts.

```text
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 0 — Operator action (outside MIG runtime)                            │
│  Yandex Wordstat UI → export CSV/XLSX for q01–q11 / region Краснодар        │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 1 — Raw export preservation                                          │
│  Artifact: wordstat-export.{date}.{ext}                                     │
│  Contract: PCR-01, HR-01                                                    │
│  Authority: Upstream SoT — never discarded after mapping                    │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 2 — Keyword Snapshot                                                 │
│  Artifact: wordstat_snapshot.{capture_id}.json                            │
│  Contract: MIG-KEYWORD-SCHEMA-STUB-v1 §Keyword Snapshot                     │
│  Mapping: header + rows[] from export columns                               │
│  Authority: Snapshot = raw capture SoT (KR-OWN-03)                          │
│  Manifest: KP-OFF → KP-PENDING; keyword_artifacts.snapshot_ref set          │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 3 — Keyword Observation (ingest boundary)                            │
│  Entity: Keyword Observation per snapshot row                               │
│  Contract: MIG-KEYWORD-SCHEMA-STUB-v1 §Keyword Observation                    │
│  Mapping: MIG-PROVIDER-MAPPING-SPEC-v1 (phrase → phrase_normalized,         │
│           region → region_scope, frequency → numeric_preview)               │
│  Authority: Ephemeral — consumed at register; not session SoT               │
│  Lifecycle: Observation → register → Keyword Object (KR-TR-01)              │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 4 — Keyword Registry                                                 │
│  Artifact: keyword_registry.json (revision 1)                               │
│  Contract: MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1 (Create, Merge, Conflict)  │
│  Model: MIG-KEYWORD-REGISTRY-MODEL-v1                                       │
│  Authority: Session SoT for registered demand language (KR-OWN-04)          │
│  Rules: PCR-03 conflict no averaging; PCR-09 seed/provider separation       │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 5 — Human Review                                                     │
│  Artifact: keyword_review.md                                                │
│  Contract: HR-01..HR-05 (MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1)          │
│  Gate: Registry freeze or operator sign-off before authoritative claim        │
└───────────────────────────────────┬─────────────────────────────────────────┘
                                    │
                                    ▼
┌─────────────────────────────────────────────────────────────────────────────┐
│  STAGE 6 — keyword_pass                                                     │
│  Field: capture_profile.keyword_pass = true                                 │
│  Contract: MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1 (KP-COMPLETE)              │
│  Guard: PCR-12 — true only after ingest + Human Review Gate passed          │
│  Note: Runtime forces false until operator manifest edit (KP-MC-05)         │
└─────────────────────────────────────────────────────────────────────────────┘
```

### Chain rules (normative)

| Rule ID | Requirement | Contract source |
|---------|-------------|-----------------|
| **PILOT-C-01** | Snapshot rows ≠ Keyword Objects | KS-SS-03 |
| **PILOT-C-02** | Numbers remain raw — no rescaling | PCR-02, MAP frequency → numeric_slots.freq |
| **PILOT-C-03** | Missing frequency → `status: unknown`, not `0` | PCR-06, M-17 |
| **PILOT-C-04** | Provider conflict → `provider_conflict`, no winner | PCR-03, M-18 |
| **PILOT-C-05** | SERP data must not populate freq | PCR-05, KS-06 |
| **PILOT-C-06** | `keyword_pass: true` only after HR gate | PCR-12, KP-MC-03 |
| **PILOT-C-07** | Seed objects (operator_seed) remain separate from provider rows | PCR-09, KO-04 |

### Mapping reference (snapshot row → Keyword Object)

Per [MIG-PROVIDER-MAPPING-SPEC-v1.md](../contracts/MIG-PROVIDER-MAPPING-SPEC-v1.md):

| Export column | Target |
|---------------|--------|
| phrase | `phrase`, `phrase_normalized` |
| region | `region_scope` (+ SAFE UNKNOWN on mismatch) |
| period | `period_scope` |
| frequency / shows | `numeric_slots.freq` |
| share | `numeric_slots.share` |
| trend | `numeric_slots.trend` |
| other | `raw_columns` |

**Provenance:** `KS-PROV-FUTURE-WORDSTAT`, `source_type: future_wordstat`, `import_method: manual_export`.

---

## Artifact Inventory

Runtime artifact inventory using contract terminology. Paths are **logical** under `session-<session_id>/`.

| Artifact | Authority | Owner | Lifecycle | Contract ref |
|----------|-----------|-------|-----------|--------------|
| **wordstat-export.{date}.csv** (or `.xlsx`) | **Upstream SoT** — raw provider evidence | Operator (attach) | **Immutable** after attach; retained for session lifetime; referenced by snapshot `source_file_ref` | PCR-01, HR-01 |
| **wordstat_snapshot.{capture_id}.json** | **Raw capture SoT** — structured export faithful to provider | Operator / ingest (manual) | Created at KP-PENDING; revision via new `capture_id` on re-export; append-only snapshots (KR-SNAP-01) | G-02 stub §Keyword Snapshot |
| **Keyword Observation** (logical; may be `keyword_observations.json` or inline in review) | **Ephemeral ingest boundary** | Operator / ingest (manual) | Created per snapshot row at map time; consumed at register; not authoritative post-register | G-02 stub §Keyword Observation |
| **keyword_registry.json** | **Session SoT** for registered demand language | Operator / registry writer (manual) | `revision: 1` on first write; `registry_state: open` → `frozen` after HR gate; objects carry `KR-LC-*` states | G-04, KR-OWN-04 |
| **keyword_review.md** | **Human review record** — gate evidence | Operator | Created at review; immutable after KP-COMPLETE sign-off; referenced by `keyword_artifacts.review_record_ref` | HR-01..HR-05 |
| **session_manifest.json** | **Session audit SoT** — pass truth | Operator (post-pass edit) | KP-OFF → KP-PENDING → KP-COMPLETE; `keyword_pass` boolean per KP-MC-01 | G-05, KP-MC-* |

### Supplementary manifest fields (keyword pass surface)

| Field | Authority | Owner | When set |
|-------|-----------|-------|----------|
| `capture_profile.keyword_pass` | Manifest truth | Operator | `true` at KP-COMPLETE only |
| `keyword_pass_status` | Manifest truth | Operator | `review_pending` → `completed` |
| `keyword_pass_operator_id` | Audit | Operator | At pass attempt |
| `keyword_provider_path` | Audit | Operator | `manual_wordstat_export` |
| `keyword_artifacts.*` | Pointers to SoT artifacts | Operator | KP-PENDING+ |
| `keyword_pass_safe_unknown[]` | Declared gaps | Operator | Always when pass section present |

### Collection metadata (registry)

| Collection kind | Contents | Pilot use |
|-----------------|----------|-----------|
| `wordstat_batch` | Provider rows from single export | One batch per capture_id |
| `seed_batch` | Optional cross-ref to mqgt01 seeds | Reference only — no merge without KO-04 |

### Forbidden artifacts (pilot contamination)

Must **not** appear: strategy spreadsheets, cluster maps, priority tiers, ORCA intent enums, SERP-derived frequency tables presented as Wordstat evidence.

---

## Success Criteria

Measurable criteria for **pilot success**. All must be satisfied for KP-COMPLETE.

| ID | Criterion | Measurable check | Evidence location |
|----|-----------|------------------|-------------------|
| **SC-01** | **Raw export preserved** | `wordstat-export.*` exists on disk; `source_file_ref` in snapshot header matches path; file not modified after attach | `wordstat_snapshot.*.json` + session folder |
| **SC-02** | **Snapshot created** | `wordstat_snapshot.{capture_id}.json` exists with `schema_stub_version`, `import_method: manual_export`, `rows[]` ≥ 1 | Snapshot artifact |
| **SC-03** | **Phrase coverage attempted** | All 11 query ids (q01–q11) either have matching snapshot row **or** explicit missing declaration in `keyword_pass_safe_unknown[]` | Review + manifest |
| **SC-04** | **Registry populated** | `keyword_registry.json` revision 1 exists; `keywords[]` contains ≥ 1 Keyword Object with `KS-PROV-FUTURE-WORDSTAT` provenance | Registry artifact |
| **SC-05** | **Provenance complete** | Every registry object has ≥ 1 `provenance_records[]` with `import_method: manual_export` and `evidence_refs[]` pointing to snapshot | Registry objects |
| **SC-06** | **Numbers raw** | `numeric_slots.freq.value` matches export cell verbatim (no ×1000, no rounding policy applied) | Spot-check q01 row vs export |
| **SC-07** | **Conflicts surfaced** | If duplicate phrase/period with different values exists → `provider_conflict` on affected slot **or** explicit «none observed» in `keyword_review.md` | Registry + review |
| **SC-08** | **Region honesty** | Export region recorded; mismatches appear in object or session `safe_unknown[]` — zero silent rewrites to Краснодар | HR-02 checklist in review |
| **SC-09** | **SAFE UNKNOWN preserved** | Missing freq → `status: unknown` or `not_captured`; session gaps in `keyword_pass_safe_unknown[]` | Registry + manifest |
| **SC-10** | **Human Review Gate passed** | `keyword_review.md` documents HR-01..HR-05 with pass/fail per check | Review artifact |
| **SC-11** | **keyword_pass completed** | `capture_profile.keyword_pass: true`, `keyword_pass_status: completed`, timestamps set | `session_manifest.json` |
| **SC-12** | **Phase 1 unchanged** | mqgt01 / mlint01 / gtrgt01 artifacts unmodified; no SERP re-capture claimed | Git diff / folder integrity |
| **SC-13** | **No strategy bleed** | Registry objects contain zero forbidden ORCA fields (cluster_id, priority, etc.) | Registry scan |
| **SC-14** | **Cross-layer divergence declared** | If Wordstat covers q05–q07 but SERP did not → documented as independent layers, not merged | `keyword_pass_safe_unknown[]` |

**Pilot success verdict:** **PASSED** when SC-01..SC-14 satisfied and operator signs `keyword_review.md`.

---

## Failure Criteria

Explicit fail conditions. **Any one** triggers pilot failure or KP-PARTIAL (not KP-COMPLETE).

| ID | Fail condition | Severity | Detection |
|----|----------------|----------|-----------|
| **FC-01** | **Lost provenance** — registry rows exist without `source_file_ref` or snapshot pointer | **Critical** | HR-01 fail |
| **FC-02** | **Frequency converted** — shows rescaled, averaged, or inferred from SERP recurrence | **Critical** | SC-06 violation; PCR-02/PCR-05 |
| **FC-03** | **Region ambiguity hidden** — export region ≠ scope.region without `safe_unknown[]` | **Critical** | HR-02 fail; PCR-08 |
| **FC-04** | **Conflict silently resolved** — duplicate values merged to single number without `provider_conflict` | **Critical** | PCR-03; NUM-06 |
| **FC-05** | **Registry bypassed** — frequency data only in ad hoc spreadsheet or review prose, no `keyword_registry.json` | **Critical** | PCR-04 |
| **FC-06** | **Missing treated as zero** — blank export cell → `value: 0` with `status: known` | **High** | PCR-06 |
| **FC-07** | **Manifest lie** — `keyword_pass: true` without review record or with KP-PENDING artifacts only | **High** | KP-MC-03; contradiction guards |
| **FC-08** | **Snapshot discarded** — raw export deleted after mapping | **High** | PCR-01 |
| **FC-09** | **Seed/provider merge error** — Wordstat numbers attached to `operator_seed` object without provider provenance | **High** | PCR-09; KO-04 |
| **FC-10** | **Strategy contamination** — priority, cluster, or intent enum added during ingest | **High** | HR-05 fail |
| **FC-11** | **Phrase invention** — registry contains phrases not in q01–q11 and not operator-declared expansion | **Medium** | Authorization rule (5) |
| **FC-12** | **Phase 1 regression** — pilot overwrites or invalidates mqgt01 SERP/landing artifacts | **Medium** | SC-12 violation |
| **FC-13** | **False completeness** — `keyword_pass: true` while `keyword_pass_safe_unknown[]` contains «registry not populated» | **High** | Pass manifest SAFE UNKNOWN rules |
| **FC-14** | **Unauthorized provider** — API pull, third-party tool, or suggestion-only data presented as Wordstat demand | **Critical** | Authorization matrix |

**Pilot failure verdict:** **FAILED** on any FC-01..FC-06 or FC-14. **PARTIAL** on FC-07..FC-13 with recoverable remediation path (KP-PARTIAL → fix → KP-PENDING).

---

## Reality Review

### What remains unproven even if pilot succeeds?

Honest list — pilot success validates **one manual cycle on one market**, not production Demand Surface.

| Area | Still unproven | Why |
|------|----------------|-----|
| **Automation** | Unattended export, ingest, registry write | Pilot is human-supervised; no runtime writer in repo |
| **Replay at scale** | Batch ingest across many sessions/markets | Single session, 11 phrases only |
| **Multiple providers** | Wordstat API, third-party vendors | Only Manual Wordstat Export authorized |
| **Provider updates** | Re-export diff policy, revision 2 vs 1 comparison | Declared SAFE UNKNOWN until chartered |
| **Cross-session registry** | Phrase catalog spanning sessions | Session-scoped registry only |
| **Runtime manifest integration** | `resolve-capture-profile.js` forces `keyword_pass: false` | Operator manual manifest edit required (KP-MC-05) |
| **JSON Schema validation** | Machine validation of registry/snapshot shape | Architecture stub only — no `.schema.json` files |
| **Research pack projection** | `frequency_signals` section in approved pack | GAP-07 — pack builder unchanged |
| **Modifier/intent enrichment** | Automated modifier extraction from provider phrases | Optional; may remain empty `[]` |
| **Trend time-series** | Multi-point history in single `trend` slot | Data model partial gap |
| **Wordstat period comparability** | Month-over-month demand drift | Single period per pilot |
| **Operator workflow repeatability** | Second operator, second market | One operator, one review cycle |
| **SERP ↔ demand correlation** | Whether Wordstat volume aligns with SERP recurrence | Layers intentionally separate — no merge authorized |
| **ORCA consumption** | Strategy quality from registry projection | No ORCA handoff in pilot |
| **n8n / MARS orchestration** | Graph-triggered keyword pass | Explicitly excluded |
| **Acquisition failure recovery** | Timeout/retry for provider attach | Not in scope |
| **HITL approval workflow** | `research_pack.approved.md` with frequency section | MVP freeze: draft only |

**Bottom line:** Pilot success proves **architecture traversal with real provider data** under human discipline. It does **not** prove **operational production readiness** or **automated Demand Surface**.

---

## Final Readiness Assessment

### Question

Can the operator now perform the **first real Wordstat export**?

### Verdict

## **READY FOR OPERATOR EXPORT**

### Evidence

| Gate / requirement | Status | Evidence |
|---------------------|--------|----------|
| Provider path authorized | **Met** | LIMITED PROVIDER AUTHORIZATION — Manual Wordstat Export ([MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md)) |
| Infrastructure contracts complete | **Met** | G-01..G-07 closed ([MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md](../contracts/MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md)) |
| Query set verified | **Met** | q01–q11 in `multi-query-market-query-set-v1.{md,json}` |
| Region scope defined | **Met** | `scope.region: Краснодар`, `lr=35` binding |
| Artifact chain specified | **Met** | This document §Artifact Chain + Phase 2g contracts |
| Human Review Gate defined | **Met** | HR-01..HR-05 in authorization doc |
| Mock replay passed | **Met** | [MIG-MOCK-PROVIDER-REPLAY-v1.md](MIG-MOCK-PROVIDER-REPLAY-v1.md) — architecture absorbed export-shaped rows |
| Pilot market validated | **Met** | Four MVP sessions on same market — freeze |
| Runtime required for export step | **No** | Export is operator action in Wordstat UI |
| Runtime required for full chain | **No** — manual JSON authorship permitted | Infrastructure contracts §Honest manual pilot path |

### Distinctions (normative)

| Action | Ready? | Notes |
|--------|--------|-------|
| **Operator performs Wordstat export** (q01–q11, Краснодар) | **Yes** | Attach raw file to new session folder |
| **Operator authors snapshot + registry manually** | **Yes** | Following G-02..G-05 contracts |
| **Operator sets `keyword_pass: true`** | **Yes** | After HR gate — manual manifest edit |
| **Automated ingest via MIG runtime** | **No** | Implementation gate not started |
| **Pack `frequency_signals` approval** | **No** | Pack workflow not proven |

### Blockers that do **not** prevent export

- No registry writer code — manual registry authorship allowed
- No CSV parser in repo — operator may author snapshot JSON from export
- Runtime forces `keyword_pass: false` — post-pass operator edit documented

### Confidence

**B+** — strong contract and authorization evidence; first real export not yet in repo (expected after operator action).

---

## Recommended Next Step

1. **Operator:** Create session folder `incoming/mig/pilots/triumph-gruzotaxi-krasnodar/session-mig-YYYYMMDD-kwrd01/`.
2. **Operator:** Run Yandex Wordstat UI — export q01–q11 for region **Краснодар**; save as `wordstat-export.{date}.csv` (or `.xlsx`).
3. **Operator:** Record export metadata (period, export date, operator id) — attach raw file only (dry run step 2 from authorization doc) **or** proceed full chain per §Artifact Chain.
4. **Operator:** Author `wordstat_snapshot.{capture_id}.json` following schema stub; map rows per mapping spec.
5. **Operator:** Author `keyword_registry.json` revision 1 following registry writer contract.
6. **Operator:** Complete `keyword_review.md` (HR-01..HR-05); update `session_manifest.json` to KP-COMPLETE.
7. **Human review** of pilot outcome against SC-01..SC-14 and FC-01..FC-14.
8. **Defer** implementation gate (registry writer, parser, runtime `keyword_pass` automation) until pilot cycle reviewed.

**Stop condition:** API clients, browser automation, n8n deployment, ORCA handoff — not authorized by this pilot.

---

## Architecture decisions (pilot charter)

| ID | Decision | Rationale |
|----|----------|-----------|
| **MPRP-01** | First runtime pilot = Manual Wordstat Export only | Authorization + infrastructure verdict |
| **MPRP-02** | Market locked to Грузотакси Краснодар | Only MVP-validated market |
| **MPRP-03** | Phrase list = q01–q11 from multi-query set | Pre-approved; no query generation |
| **MPRP-04** | Single review cycle | Minimal scope per Phase 3a charter |
| **MPRP-05** | Verdict = **READY FOR OPERATOR EXPORT** | Contracts enable export; runtime not required for export step |
| **MPRP-06** | Pilot success ≠ automation readiness | Reality-first distinction |

---

## Related documents

| Document | Role |
|----------|------|
| [multi-query-market-query-set-v1.md](../../../incoming/mig/pilots/triumph-gruzotaxi-krasnodar/multi-query-market-query-set-v1.md) | Approved phrase list |
| [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) | Provider authorization + HR gate |
| [MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md](../contracts/MIG-PROVIDER-INFRASTRUCTURE-CONTRACTS-v1.md) | G-02..G-05 closure |
| [MIG-KEYWORD-SCHEMA-STUB-v1.md](../contracts/MIG-KEYWORD-SCHEMA-STUB-v1.md) | Entity field stubs |
| [MIG-PROVIDER-MAPPING-SPEC-v1.md](../contracts/MIG-PROVIDER-MAPPING-SPEC-v1.md) | Column mapping |
| [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](../contracts/MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) | Registry operations |
| [MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md](../contracts/MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md) | keyword_pass states |

---

*MIG Manual Provider Runtime Pilot v1 · 2026-06-06 · pilot definition only · no runtime · no implementation*
