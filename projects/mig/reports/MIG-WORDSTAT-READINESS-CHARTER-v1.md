# MIG Wordstat Readiness Charter v1

**Status:** **charter** — readiness assessment only (Phase 2e)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2e — Demand Surface Provider Readiness  
**Prior artifacts:** [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) · [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) · [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md) · [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md)  
**Related (reference, not superseded):** [mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md)

**This document delivers:** foundation audit, generic demand-provider compatibility review, gap register, readiness matrix, authorization gate, reality review, final verdict.

**This document does not deliver:** runtime, acquisition, APIs, Wordstat integration, provider onboarding, ORCA semantics, Phase 1 redesign, or implementation planning.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This charter answers one question only:

> **Can the current Demand Surface architecture accept a future demand provider without redesign?**

**Normative:** This document **does not authorize** Wordstat integration, any provider connection, or implementation work.

---

## Foundation Audit

Audit of Phase 2 foundation layers completed through Phase 2d (Registry Model). Each layer rated against **architectural readiness for a generic demand provider** — not implementation readiness.

### Summary table

| Layer | Document | Status | Confidence |
|-------|----------|--------|------------|
| Charter | [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) | **Partially Ready** | B+ |
| Capability Model | [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) | **Partially Ready** | B+ |
| Data Model | [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) | **Partially Ready** | B+ |
| Registry Model | [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md) | **Partially Ready** | B+ |

**Aggregate:** No layer is **Not Ready** for architectural acceptance. No layer is **Ready** for provider connection without remaining gaps. All four are **Partially Ready** — sufficient to **plan** provider attachment; insufficient to **connect** a provider tomorrow.

---

### Charter (Phase 2a)

**Status: Partially Ready**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Demand Surface mission defined | **Ready** | Mission frame: «what query language, modifiers, and demand signals were observable at capture time» — charter §Mission |
| Market vs Demand boundary | **Ready** | KS-01..KS-06; three-layer stack — charter §Boundaries |
| Wordstat named as capability placeholder | **Ready** | §Keyword Surface capability model — Wordstat placeholder; P2-KS-04 |
| Evidence taxonomy includes frequency/trend | **Ready** | `frequency_evidence`, `trend_evidence` in §Evidence model |
| SAFE UNKNOWN discipline | **Ready** | §SAFE UNKNOWN discipline — missing Wordstat ≠ zero volume |
| Provider integration authorized | **Not Ready** | Explicitly out of scope: «Wordstat runtime, API clients, CSV ingest» — §Out of scope |
| Schema / pack section lock-in | **Not Ready** | «No final schema decisions in this charter» — §Outputs |

**Reasoning:** The charter correctly frames Demand Surface and reserves Wordstat as a **named, unimplemented** channel. It authorizes **planning** only. It does not define provider lifecycle, snapshot contracts, or operator review gates — those defer to later artifacts (now partially addressed in 2b–2d).

---

### Capability Model (Phase 2b)

**Status: Partially Ready**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Phrase capabilities cover provider rows | **Ready** | KS-CAP-PHR-* family — exact strings from any channel |
| Numeric demand capabilities defined | **Ready** | KS-CAP-NUM-FREQ, TREND, SHARE — «what may be stored when provider returns numbers» |
| Provenance source candidates | **Ready** | Wordstat listed under KS-CAP-NUM-FREQ evidence sources; future gate explicit |
| Modifier / intent without ORCA bleed | **Ready** | Forbidden fields list; KS-INT-* shape flags only |
| Extraction operationalized | **Not Ready** | «Extraction algorithm for modifiers — undefined operationally» — §Reality review gaps |
| Validation by replay | **Not Ready** | «No keyword artifacts in MVP evidence — cannot empirically test» — §Reality review |
| Generic provider (non-Wordstat) | **Partially Ready** | Numeric capabilities are provider-agnostic; no separate `KS-CAP-*` for arbitrary third-party APIs |

**Reasoning:** Capability taxonomy is **complete for planning** what a demand provider would supply (phrases + numbers + provenance). Capabilities describe **understanding**, not **fetch**. Operational extraction and replay validation remain open — these block implementation, not architectural slot reservation.

---

### Data Model (Phase 2c)

**Status: Partially Ready**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Keyword Object canonical shape | **Ready** | Full field model — §Canonical Keyword Object |
| Provider phrase representation | **Ready** | `phrase`, `phrase_normalized`, dedup rules KO-01..KO-06 |
| Provider provenance | **Ready** | `KS-PROV-FUTURE-WORDSTAT`, `KS-PROV-FUTURE-PROVIDER` — §Provenance Model |
| Numeric slots for provider numbers | **Ready** | `numeric_slots.freq/trend/share` with status-first semantics — §Numeric Placeholder Model |
| Provider conflict representation | **Ready** | `status: provider_conflict`, `conflict_values[]` — NUM-06, §Provider conflict handling |
| Provider gap / absence | **Ready** | `not_captured`, `unknown`, `safe_unknown[]` — NUM-01..NUM-03 |
| Wordstat without redesign | **Ready** | Reality review: «Yes — for data representation» — §Reality Review |
| Rich time-series history | **Partially Ready** | «Time-series array >2 points in one slot — Not defined; possible Phase 2d extension» |
| JSON Schema / runtime types | **Not Ready** | Explicitly out of scope — document header |

**Reasoning:** The data model is the strongest architectural evidence that a generic demand provider **fits without object redesign**. `future_*` provenance channels exist precisely so provider rows do not require amending Keyword Object shape. Remaining gap: multi-point trend history inside one slot is underspecified — affects historical Wordstat exports, not single-snapshot ingest.

---

### Registry Model (Phase 2d)

**Status: Partially Ready**

| Criterion | Assessment | Evidence |
|-----------|------------|----------|
| Session-scoped registry container | **Ready** | Keyword Registry logical fields — §Keyword Registry |
| Provider batch grouping | **Ready** | `wordstat_batch` collection kind — §Keyword Collection |
| Snapshot → observation → register path | **Ready** | Keyword Snapshot, Keyword Observation entities — §Registry Entities |
| Lifecycle for numeric enrich | **Ready** | `registered` → `enriched` on Wordstat attach — §Transition rules KR-TR-02 |
| Provider conflict integrity | **Ready** | Aligns with Phase 2c `provider_conflict` — §Provider disagreement |
| Multi-export / revision policy | **Ready** | `revision` increment; append-only snapshots — KR-SNAP-01 |
| Observation layer in MVP | **Not Ready** | «MVP has no observation layer — seeds exist only in manifest» — §Keyword Observation |
| Registry writer / schema | **Not Ready** | «JSON Schema / registry writer — Phase 2e+ implementation gate» — §Non-Goals |
| Cross-session phrase catalog | **Not Ready** | Explicitly out of scope — future catalog layer |

**Reasoning:** Registry organization accommodates Wordstat and generic provider ingest **without container redesign**. The ingest boundary (Observation entity) is **logical only** — no runtime path exists. Revision and conflict rules are defined; re-capture **diff policy** remains SAFE UNKNOWN per registry §SAFE UNKNOWN in lifecycle.

---

## Provider Compatibility Review

Assessment assumes a **generic demand provider** — any source that returns **phrase strings** and optional **numeric columns** with **region/period context**. Not Wordstat-specific semantics.

### Compatibility questions

| Question | Answer | Evidence |
|----------|--------|----------|
| **Can provider phrases be represented?** | **Yes** | Keyword Object `phrase` (required); `phrase_normalized` for dedup — Data Model KO-NORM-*; KS-CAP-PHR-* capabilities |
| **Can provider numbers be represented?** | **Yes** | `numeric_slots.freq/trend/share`; `value` stored raw; `raw_columns` for unmapped export — Data Model §Numeric Placeholder Model; KS-CAP-NUM-* |
| **Can provider provenance be represented?** | **Yes** | `KS-PROV-FUTURE-PROVIDER` (generic); `KS-PROV-FUTURE-WORDSTAT` (named anchor); `provenance_records[]` with `import_method`, `provider_ref`, `evidence_refs[]` — Data Model §Provenance Model PR-06 |
| **Can provider conflicts be represented?** | **Yes** | `numeric_slots.*.status: provider_conflict`; `conflict_values[]` — no silent averaging — Data Model NUM-06; Registry §Provider disagreement |
| **Can provider gaps be represented?** | **Yes** | `not_captured`, `unknown`; object and session `safe_unknown[]`; empty registry valid when pass not run — KR-OWN-05; Charter SAFE UNKNOWN table |
| **Can provider updates be represented?** | **Partially** | New snapshot → new observations → registry `revision` increment; append-only provenance KR-INT-01; **re-capture diff against prior revision — SAFE UNKNOWN** until operator review flow chartered — Registry §SAFE UNKNOWN in lifecycle |

### Provider update semantics (detail)

| Update type | Supported without redesign? | Mechanism |
|-------------|----------------------------|-----------|
| First provider ingest for session | **Yes** | Snapshot → register objects → `enriched` |
| Second export same phrase, different shows | **Yes** | `provider_conflict` or new provenance record with new `capture_time` |
| Re-ingest identical snapshot | **Yes** | Idempotent merge — KR-INT idempotency rule |
| Multi-period history in one export | **Partially** | Single `trend` slot; array of observations **not defined** — may need Phase 2f slot extension, not registry redesign |
| Provider row for phrase not in seed list | **Yes** | Register as new Keyword Object with `KS-PROV-FUTURE-PROVIDER`; `unmapped_phrases` handling referenced in Keyword Intelligence v1 |

### Alignment with Keyword Intelligence v1 (reference)

[mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md) defines logical `wordstat_snapshot.json` shape (§3.7) and ingest path. Phase 2c Keyword Object and Phase 2d registry **subsume** that shape via `evidence_refs[]` and `numeric_slots` — **no structural conflict**. Column mapping and `keyword_id` assignment remain **implementation gates**, not model gaps.

---

## Gap Register

**Real gaps only** — items that would block or corrupt provider connection if ignored. No speculative wishlist.

| Gap ID | Gap | Layer | Blocker for connection? | Evidence |
|--------|-----|-------|-------------------------|----------|
| **GAP-01** | **No JSON Schema** for Keyword Object, registry container, or `wordstat_snapshot` | Implementation | **Yes** | All Phase 2b–2d docs: «no JSON Schema»; Registry §Non-Goals |
| **GAP-02** | **No registry writer** — `keyword_registry.json` does not exist in runtime | Runtime | **Yes** | Freeze: `keyword_pass: false`; no keyword artifacts in MVP evidence |
| **GAP-03** | **No snapshot ingest contract** locked to Phase 2c object mapping (column → `numeric_slots`) | Design | **Yes** | Keyword Intelligence §3.7 logical shape exists; mapping to `KS-PROV-FUTURE-WORDSTAT` not normatively bound in Phase 2c |
| **GAP-04** | **No Keyword Observation ingest boundary** in runtime | Runtime | **Yes** | Registry: «MVP has no observation layer» |
| **GAP-05** | **No operator review flow** for keyword registry before pack projection | Process | **Yes** | Freeze: no approved research pack; charter defers HITL keyword summary to Keyword Intelligence §6 |
| **GAP-06** | **Trend history model** — multi-point time series inside `trend` slot undefined | Data Model | **Partial** | Data Model §What would not fit: «Time-series array >2 points»; Registry notes same |
| **GAP-07** | **Research Pack section stubs** — `keyword_observations`, `search_demand`, `frequency_signals` not activated in contract | Pack | **Partial** | Charter §Research Pack sections «future»; pack builder unchanged |
| **GAP-08** | **Manifest `keyword_pass` / `capture_profile`** — no spine path to set or verify keyword pass | Runtime | **Yes** | All MVP manifests `keyword_pass: false` — freeze §Known Limitations |
| **GAP-09** | **Provider lifecycle charter** — onboarding, credential boundary, quota, skip policy | Governance | **Partial** | Keyword Intelligence §3.6 operator requirements exist; not cross-walked to Phase 2d registry lifecycle |
| **GAP-10** | **Replay / verify model** for keyword pass — no groundtruth session with keyword artifacts | Validation | **Yes** | Capability Model + Registry: «cannot empirically test until capture chartered» |
| **GAP-11** | **Re-capture diff policy** — revision 2 vs revision 1 comparison | Registry | **Partial** | Registry SAFE UNKNOWN: «diff against revision 1 not computed» |
| **GAP-12** | **Modifier/intent extraction** undefined — provider phrases would register without enrich unless manual pass | Capability | **No** (for numeric provider) | Provider connection does not require modifier extraction; enrich is optional KR-TR-02 |

**Not gaps (explicitly excluded):**

- Semantic clustering, volume tiers, ORCA intent — forbidden, not missing.
- Cross-session phrase catalog — future layer, out of scope.
- Wordstat API client — acquisition choice, not architectural gap.
- Phase 1 SERP / landing redesign — frozen, unrelated.

---

## Readiness Matrix

| Area | Status | Risk |
|------|--------|------|
| **Phrase Model** | **Partially Ready** | Low — `phrase` + dedup rules sufficient; normalization edge cases (synonyms, typos) require operator links, not redesign |
| **Provenance** | **Partially Ready** | Low — `KS-PROV-FUTURE-*` channels reserved; risk if implementers bypass `provenance_records[]` and infer from SERP |
| **Numeric Slots** | **Partially Ready** | Medium — single-value slots ready; multi-period history underspecified; column mapping unbound |
| **Registry** | **Partially Ready** | Medium — logical model complete; no runtime container, observation layer, or writer |
| **Evidence Model** | **Partially Ready** | Low — `evidence_grade`, `evidence_refs[]`, SAFE UNKNOWN aligned across layers; snapshot SoT vs registry SoT must be respected (KR-OWN-03) |
| **SAFE UNKNOWN** | **Ready** | Low — normative across charter, capability, data, registry models; primary discipline for honest provider absence |
| **Lifecycle / Revision** | **Partially Ready** | Medium — states defined; re-capture diff and operator freeze gate procedural |
| **Provider Conflict** | **Ready** | Low — `provider_conflict` + no averaging — explicit in data and registry models |
| **Operator / HITL Gate** | **Not Ready** | High — no keyword pass review workflow proven |
| **Runtime / Replay** | **Not Ready** | High — zero keyword artifacts in freeze evidence |

---

## Authorization Gate

**Minimal set** that MUST exist before the **first demand provider may be connected** (including manual Wordstat export). Avoids overengineering.

| # | Gate item | Rationale |
|---|-----------|-----------|
| **G-01** | **Human authorization record** — explicit decision document authorizing *one* provider path (e.g. manual Wordstat export only) | This charter explicitly does **not** authorize connection |
| **G-02** | **JSON Schema stub** for Keyword Object + `keyword_registry` container + provider snapshot (`wordstat_snapshot` or generic `demand_snapshot`) | GAP-01; without schema, ingest cannot validate |
| **G-03** | **Snapshot → Keyword Object mapping spec** — one page: column names → `numeric_slots`, row → `KS-PROV-FUTURE-*`, `region_scope` / `period_scope` alignment rules | GAP-03; prevents ad hoc mapping per session |
| **G-04** | **Registry writer contract** — logical upsert behavior only: identity merge (KO-03), conflict surfacing, session `safe_unknown[]` | GAP-02, GAP-04 |
| **G-05** | **Manifest flag path** — `capture_profile.keyword_pass` or equivalent set and recorded when provider ingest runs | GAP-08 |
| **G-06** | **Operator review checklist** — before registry `frozen`: snapshot present, region match, partial phrase coverage declared | GAP-05 |
| **G-07** | **One tabletop replay** — map mqgt01 seeds to logical Keyword Objects + one mock provider row; no production runtime required | GAP-10; validates model fit on pilot phrases |

**Explicitly NOT required before first connection (deferred):**

- Wordstat API client or browser automation
- Modifier/intent extraction pipeline
- Research pack builder changes
- Cross-session catalog
- n8n graph deployment
- Production verify scripts ( desirable after first mock ingest)

---

## Reality Review

### Question

If Wordstat (or any demand provider) were connected **tomorrow**, what would break and what would not?

### What would **not** break

| Area | Why |
|------|-----|
| **Phase 1 session spine** | Keyword pass is additive — freeze: «Phase 2 is additive»; SERP, discovery, website, landing paths unchanged |
| **Market Surface artifacts** | KS-01: domains/competitors remain Market Surface; registry references SERP, does not embed |
| **Website Intelligence** | Landing observations, comparison matrix — KS-05 unchanged |
| **Keyword Object shape** | `future_wordstat` provenance and `numeric_slots` already defined — no emergency schema redesign |
| **ORCA boundary** | Forbidden fields remain forbidden; raw numbers do not become strategy |
| **SAFE UNKNOWN discipline** | Missing provider data already declared in all manifests via `keyword_pass: false` |
| **MVP freeze claims** | Connecting provider **after** authorization gate does not retroactively falsify Phase 1 validation |

### What would **break** (or fail silently — worse)

| Failure mode | Cause | Severity |
|--------------|-------|----------|
| **No artifact home** | `keyword_registry.json`, `wordstat_snapshot.json` not written by any module | **Critical** — data loss or ad hoc files outside SoT |
| **Unvalidated JSON** | No schema — malformed rows enter session folder | **High** — corrupt registry state |
| **Silent SERP inference** | Operator maps SERP recurrence to frequency without provider | **High** — violates NUM-02, KS-06; false demand evidence |
| **Region mismatch undetected** | Export region ≠ `scope.region` without `safe_unknown` | **High** — wrong demand geography in pack |
| **Duplicate phrase chaos** | Identity rules not implemented — seed vs Wordstat row merge errors | **Medium** — KO-04/KO-05 violations |
| **Provider conflict averaged** | Implementation picks «latest» shows without `provider_conflict` | **Medium** — violates KR-AD-07, NUM-06 |
| **Pack false completeness** | Projections show frequency without `keyword_pass` or section stubs | **Medium** — operator believes demand captured when partial |
| **Manifest lie** | `keyword_pass: false` while snapshot exists on disk | **Medium** — audit trail broken |
| **Phase 1 regression noise** | Keyword work touches `run-mig-session.js` without isolation | **Low–Medium** — **UNKNOWN** until implementation scope defined |

### Honest bottom line

**Architecture would hold.** **Runtime would not.** Connecting a provider tomorrow without G-01..G-07 would produce **orphan files** or **informal data** outside the Keyword Registry authority model — equivalent to breaking SoT discipline without breaking Phase 1 SERP intelligence.

---

## Final Verdict

### Verdict: **PARTIALLY READY**

| Verdict option | Applicable? | Reason |
|----------------|-------------|--------|
| NOT READY | **No** | Four foundation layers explicitly reserve provider slots; data and registry models state «yes without redesign» |
| **PARTIALLY READY** | **Yes** | Architecture accepts a generic demand provider; authorization gates and runtime artifacts absent |
| READY FOR PILOT | **No** | Pilot implies controlled connection — G-01..G-07 not met; no mock ingest replay executed |
| READY FOR IMPLEMENTATION | **No** | Explicit non-goal of this phase; registry writer, schema, observation layer unbuilt |

### Evidence summary

1. **Data Model** (KS-DM-02): `future_*` provenance exists so Wordstat rows do not require object redesign.
2. **Registry Model** reality review: «Yes — for registry organization» via Snapshot → Observation → upsert.
3. **Capability Model** (KS-CAP-NUM-*): numeric demand named and bounded.
4. **MVP Freeze**: `keyword_pass: false` — honest absence; no keyword SoT in evidence today.
5. **Gap Register**: seven **Yes** blockers (GAP-01, 02, 03, 04, 05, 08, 10) before connection.

**Confidence:** **B** — strong architectural alignment; weak operational readiness.

---

## Recommended Next Step

1. **Human review** of this charter — confirm verdict **PARTIALLY READY** and authorization gate G-01..G-07.
2. **If gate approved:** Author **Provider Connection Authorization v1** (separate document) selecting **one** path — recommend manual export per Keyword Intelligence §3.5, not API/automation.
3. **Execute G-02 + G-03:** JSON Schema stub + snapshot-to-Object mapping one-pager in `contracts/`.
4. **Execute G-07:** Tabletop replay on mqgt01 seed list with one mock Wordstat row per seed — validates phrase, numeric, provenance, conflict paths without runtime.
5. **Defer** registry writer implementation until schema stub reviewed.
6. **Stop condition:** If work becomes ingest coding, API design, or ORCA handoff — stop; split per [../boundaries.md](../boundaries.md).

---

## Architecture decisions (readiness charter)

| ID | Decision | Rationale |
|----|----------|-----------|
| **P2E-01** | Generic provider assessed, not Wordstat-only | Demand Surface must accept any phrase+numeric provider |
| **P2E-02** | Verdict **PARTIALLY READY** | Architecture sufficient; connection gates unmet |
| **P2E-03** | This charter **does not authorize** provider connection | Readiness ≠ implementation |
| **P2E-04** | Authorization gate G-01..G-07 is **minimal** set | Avoids overengineering per user charter |
| **P2E-05** | Trend multi-point history is **partial gap**, not redesign | Data Model deferred extension |
| **P2E-06** | Phase 1 MVP freeze **remains valid** | Provider work is additive |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) | Phase 2a mission |
| [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) | Phase 2b capabilities |
| [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](../contracts/MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) | Phase 2c objects |
| [MIG-KEYWORD-REGISTRY-MODEL-v1.md](../contracts/MIG-KEYWORD-REGISTRY-MODEL-v1.md) | Phase 2d registry |
| [MIG-MVP-VALIDATION-FREEZE-v1.md](MIG-MVP-VALIDATION-FREEZE-v1.md) | Phase 1 evidence |
| [mig-keyword-intelligence-architecture-v1.md](../contracts/mig-keyword-intelligence-architecture-v1.md) | Acquisition reference (future) |
| [../boundaries.md](../boundaries.md) | MIG vs ORCA |

---

*MIG Wordstat Readiness Charter v1 · 2026-06-06 · readiness assessment only · no runtime · no provider integration*
