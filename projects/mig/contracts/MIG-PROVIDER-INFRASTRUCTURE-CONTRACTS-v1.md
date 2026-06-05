# MIG Provider Infrastructure Contracts v1

**Status:** **normative** — infrastructure contract umbrella (Phase 2g)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2g — Provider Infrastructure Contracts  
**Gates closed:** **G-02**, **G-03**, **G-04**, **G-05**  
**Prior artifacts:** [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) · [MIG-WORDSTAT-READINESS-CHARTER-v1.md](../reports/MIG-WORDSTAT-READINESS-CHARTER-v1.md) · [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) · [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-REGISTRY-MODEL-v1.md](MIG-KEYWORD-REGISTRY-MODEL-v1.md) · [MIG-MOCK-PROVIDER-REPLAY-v1.md](../reports/MIG-MOCK-PROVIDER-REPLAY-v1.md)

**This document delivers:** umbrella index of infrastructure contracts, gate closure record, consistency audit, infrastructure readiness assessment, final verdict, recommended next step.

**This document does not deliver:** runtime, provider integration, Wordstat ingest, acquisition code, JSON Schema files, ORCA handoff, or Phase 1 redesign.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

Provider **path** is authorized ([MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md)). Provider **infrastructure contracts** are defined here. **Implementation** remains a separate gate.

---

# REPORT — Provider Infrastructure Contracts

## Infrastructure Contract Set

Phase 2g closes the design gates that blocked first real provider ingest (G-02..G-05). The contract set:

| Contract | Gate | Path | Purpose |
|----------|------|------|---------|
| **Keyword Schema Stub** | G-02 | [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md) | Architecture-only fields: Keyword Object, Registry, Snapshot, Observation |
| **Provider Mapping Spec** | G-03 | [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md) | Provider column → Keyword Object; SAFE UNKNOWN; provider_conflict |
| **Registry Writer Contract** | G-04 | [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) | Create, merge, conflict, deprecate, freeze — logical behaviors |
| **Keyword Pass Manifest Contract** | G-05 | [MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md](MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md) | `keyword_pass` states, transitions, artifacts, review gate |

### Authorization gate status (updated)

| Gate | Item | Status after Phase 2g |
|------|------|------------------------|
| **G-01** | Human authorization record | **Met** — [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) |
| **G-02** | Schema stub (architecture-only — no JSON Schema syntax) | **Met** — [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md) |
| **G-03** | Snapshot → Keyword Object mapping spec | **Met** — [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md) |
| **G-04** | Registry writer contract | **Met** — [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) |
| **G-05** | Manifest `keyword_pass` path | **Met** — [MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md](MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md) |
| **G-06** | Operator review checklist | **Met** — authorization doc HR-01..HR-05 |
| **G-07** | Tabletop replay | **Met** — [MIG-MOCK-PROVIDER-REPLAY-v1.md](../reports/MIG-MOCK-PROVIDER-REPLAY-v1.md) |

**Normative:** G-02..G-05 are **design-complete**. They do **not** imply runtime exists.

### Dependency graph

```text
G-01 Authorization ──► G-02 Schema Stub ──► G-03 Mapping Spec ──► G-04 Registry Writer
                                                      │
G-07 Replay (validated) ─────────────────────────────┤
                                                      ▼
                                              G-05 Manifest Contract
                                                      │
                                              [Implementation gate — NOT STARTED]
```

---

## Schema Stub

**Document:** [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md)

| Entity | Field count (stub) | Authority |
|--------|-------------------|-----------|
| Keyword Object | 20+ logical fields + numeric_slots sub-stub | Session phrase SoT |
| Keyword Registry | 10 logical fields | Session index SoT |
| Keyword Snapshot | Header + row stub | Raw capture SoT |
| Keyword Observation | 11 logical fields | Pre-register ingest unit |

**Key decisions:** Snapshot rows ≠ Keyword Objects; forbidden ORCA fields restated; no JSON Schema syntax per Phase 2g rules.

---

## Mapping Specification

**Document:** [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md)

| Provider column | Keyword Object target |
|-----------------|----------------------|
| phrase | **phrase**, **phrase_normalized** |
| region | **region_scope** (+ SAFE UNKNOWN on mismatch) |
| period | **period_scope** |
| frequency / shows | **numeric_slots.freq** |
| share | **numeric_slots.share** |
| trend | **numeric_slots.trend** |
| other columns | **raw_columns** |

**Stress cases covered:** region mismatch (M-15), blank frequency (M-17), provider conflict (M-18), seed vs Wordstat separation (KO-04).

---

## Registry Writer Contract

**Document:** [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md)

| Operation | Summary |
|-----------|---------|
| **Create** | New keyword_id; state → registered |
| **Merge** | Append provenance; union evidence; idempotent re-ingest |
| **Conflict** | provider_conflict — no averaging |
| **Deprecate** | Tombstone; no id recycle |
| **Freeze** | Integrity checklist; revision discipline |

---

## Keyword Pass Contract

**Document:** [MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md](MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md)

| State | `keyword_pass` | When |
|-------|----------------|------|
| KP-OFF | `false` | Default (MVP) |
| KP-PENDING | `false` | Snapshot attached, review incomplete |
| KP-COMPLETE | **`true`** | Ingest + HR-01..HR-05 passed |
| KP-PARTIAL / KP-SKIPPED | `false` | Honest partial or skip |

Integrates with mqgt01-style `capture_profile` and `artifacts` pointers without Phase 1 redesign.

---

## Consistency Audit

Cross-check of Phase 2 foundation vs four new contracts.

### Compatibility table

| Foundation layer | Schema Stub (G-02) | Mapping Spec (G-03) | Writer Contract (G-04) | Pass Manifest (G-05) | Compatible? |
|------------------|--------------------|--------------------|------------------------|----------------------|-------------|
| **Capability Model** | capability_refs optional; KS-CAP-NUM slots | Maps to KS-CAP-NUM-FREQ/SHARE/TREND | No strategy fields | No ORCA bleed at manifest | **Yes** |
| **Data Model** | Field stub mirrors Phase 2c tables | Implements KO-03..KO-06, NUM status | Implements KO-01, KR-TR-* | SAFE UNKNOWN aligns PR/NUM | **Yes** |
| **Registry Model** | Registry + Observation entities | Snapshot → Observation → Object | KR-INT-*, lifecycle ops | Registry freeze before KP-COMPLETE | **Yes** |
| **Authorization (PCR/HR)** | source_file_ref required | PCR-01..PCR-11 reflected | Conflict = PCR-03 | PCR-12 keyword_pass truth | **Yes** |
| **Mock Replay** | M-01..M-18 row shape | All stress rows mapped | Merge/conflict paths | KP-PENDING → COMPLETE flow | **Yes** |
| **Keyword Intelligence v1** | Logical snapshot compatible | Column map extends §3.7 | Upsert aligns §5 dedup | Boolean vs enum note | **Partial** — see contradictions |

### Contradictions and resolutions

| ID | Apparent contradiction | Resolution | Severity |
|----|-------------------------|------------|----------|
| **C-01** | Readiness Charter G-02 said «JSON Schema stub»; Phase 2g task forbids JSON Schema syntax | **G-02 closed as architecture-only stub** per Phase 2g charter; machine validation deferred to implementation gate | **Low** — scope clarification, not model conflict |
| **C-02** | Keyword Intelligence v1 uses `source_type: wordstat` enum; Data Model uses `future_wordstat` | Mapping spec and schema stub use **Phase 2c** `future_wordstat` / `KS-PROV-FUTURE-WORDSTAT` as normative; KI v1 remains reference — implementers map `wordstat_export` → `future_wordstat` | **Low** — naming crosswalk at implementation |
| **C-03** | KI v1 `keyword_pass` enum: `off \| surface_only \| surface_and_wordstat`; manifests use boolean | Pass manifest contract **locks boolean for v1 pilot**; enum deferred — documented in KP-MC-01 | **Low** — pilot discipline |
| **C-04** | KI v1 embeds `frequency_signal` on snapshot row; schema stub uses flat `frequency` + `numeric_slots` on object | **No conflict** — snapshot row is raw; object uses Phase 2c numeric_slots — mapping spec bridges | **None** |
| **C-05** | Runtime forces `keyword_pass: false` ([resolve-capture-profile.js](../../lib/runtime/resolve-capture-profile.js)) | Pass manifest documents **operator manifest edit** for manual pilot until runtime gate — not a contract contradiction | **Medium** — operational blocker, not doc conflict |
| **C-06** | Authorization doc still lists G-02..G-05 as «Not met» | **Superseded by this umbrella** — authorization doc not auto-amended; human may update status in follow-up | **Low** — doc hygiene |

**No architectural contradictions** requiring Phase 2c/2d model amendment were found.

### Traceability matrix (gates → rules)

| Gate | Primary rules satisfied |
|------|-------------------------|
| G-02 | KO-* fields, KR registry fields, KR-SNAP-* |
| G-03 | MAP-*, PCR-08, NUM-03, provider_conflict |
| G-04 | KO-03, KR-INT-01, KR-TR-*, freeze checklist |
| G-05 | PCR-12, HR-01..HR-05, KR-OWN-05 |

---

## Readiness Assessment

**Question:** After these contracts, what still blocks a **first manual Wordstat pilot**?

### Real blockers only

| Blocker | Type | Evidence | Blocks pilot? |
|---------|------|----------|---------------|
| **No registry writer implementation** | Runtime | GAP-02 from Readiness Charter — no code writes `keyword_registry.json` | **Yes** — manual pilot without writer = orphan files (Readiness §What would break) |
| **No snapshot ingest tooling** | Runtime | No CSV/XLSX → Keyword Snapshot mapper in repo | **Yes** — operator can attach raw file but no normative automated path; **manual JSON/tabletop still possible** |
| **Runtime forces keyword_pass off** | Runtime | resolve-capture-profile.js | **Partial** — operator can edit manifest post-pass; spine does not execute keyword pass |
| **No keyword_registry.json in session folders** | Artifact | MVP freeze — zero keyword artifacts | **Yes** for authoritative registry; **No** for dry-run with manual registry file |
| **Human operator Wordstat export** | Operational | Not repo-gated — operator action | **Yes** until export performed |
| **JSON Schema validation files** | Implementation | Deferred per Phase 2g — architecture stub only | **No** for **manual** supervised pilot if operator follows contracts |
| **Research pack projection** | Pack | GAP-07 — sections not activated | **No** for first ingest — registry authority sufficient |
| **Modifier/intent extraction** | Enrichment | GAP-12 — optional for numeric provider | **No** |
| **Wordstat API** | Provider | Explicitly not authorized | **N/A** — manual export path |

### Not blockers (explicitly excluded)

- Phase 2 architecture redesign — **not needed**
- ORCA handoff — **out of scope**
- Cross-session catalog — **future**
- n8n / automation — **deferred**
- Third-party provider — **not authorized**

### Honest manual pilot path (minimum)

A **human-supervised manual pilot** can proceed **without runtime** if operator:

1. Performs Wordstat export (q01–q11 / Краснодар).
2. Preserves raw CSV/XLSX as SoT.
3. Authors Keyword Snapshot + Registry JSON **by hand or script outside MIG runtime** following G-02..G-05 contracts.
4. Updates session manifest per pass contract (KP-PENDING → KP-COMPLETE after HR gate).
5. Does **not** claim pack `frequency_signals` approval until pack workflow exists.

**Normative:** Contracts enable this path; they do **not** authorize claiming runtime integration exists.

---

## Final Verdict

### **INFRASTRUCTURE READY FOR MANUAL PROVIDER PILOT**

| Verdict option | Selected? | Evidence |
|----------------|-----------|----------|
| INFRASTRUCTURE NOT READY | No | G-01..G-07 design gates met; mock replay passed; no model contradictions |
| INFRASTRUCTURE PARTIALLY READY | **Superseded** | Was true before Phase 2g; contracts now close G-02..G-05 |
| **INFRASTRUCTURE READY FOR MANUAL PROVIDER PILOT** | **Yes** | All authorization design gates closed; Manual Wordstat Export path fully specified at contract level |
| INFRASTRUCTURE READY FOR AUTOMATED INGEST | No | No registry writer code, no parser, runtime keyword_pass forced off |

**Confidence:** **B+** — strong contract completeness; runtime implementation explicitly absent.

**Distinction:**

| Layer | Status |
|-------|--------|
| **Design / contracts** | **Ready** for manual provider pilot |
| **Runtime / automation** | **Not ready** — separate implementation gate |
| **Full unattended ingest** | **Not authorized** |

---

## Recommended Next Step

1. **Human review** of this contract set — confirm G-02..G-05 closure and verdict **INFRASTRUCTURE READY FOR MANUAL PROVIDER PILOT**.
2. **Operator dry run (no registry writer):** Wordstat export for Грузотакси Краснодар q01–q11; store raw file only — validates operator workflow (authorization step 4).
3. **Optional:** Update [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) gate table to reflect G-02..G-05 **Met**.
4. **Implementation gate (separate charter):** Minimal registry writer + snapshot mapper — **not** started by Phase 2g.
5. **First authoritative ingest:** Manual or scripted registry following contracts + Human Review Gate — after human approves implementation scope.
6. **Stop condition:** API clients, browser automation, pack builder changes, ORCA handoff — split per [boundaries.md](../boundaries.md).

---

## Architecture decisions (infrastructure umbrella)

| ID | Decision | Rationale |
|----|----------|-----------|
| **PIC-01** | Four child contracts under one umbrella | Traceability for Phase 2g |
| **PIC-02** | G-02 = architecture stub, not JSON Schema | User charter + Phase 2g rules |
| **PIC-03** | Verdict = ready for **manual** pilot only | Runtime absent — reality-first |
| **PIC-04** | No Phase 2c/2d redesign required | Consistency audit clean |
| **PIC-05** | Implementation explicitly out of scope | Contracts only |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md) | G-02 |
| [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md) | G-03 |
| [MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md](MIG-KEYWORD-REGISTRY-WRITER-CONTRACT-v1.md) | G-04 |
| [MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md](MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md) | G-05 |
| [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) | G-01, provider path |
| [MIG-WORDSTAT-READINESS-CHARTER-v1.md](../reports/MIG-WORDSTAT-READINESS-CHARTER-v1.md) | Original gap register |

---

*MIG Provider Infrastructure Contracts v1 · 2026-06-06 · contracts only · G-02..G-05 closed · no runtime*
