# MIG Keyword Registry Model v1

**Status:** **normative** — registry organization only (Phase 2d)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2d — Keyword Registry Model  
**Prior artifacts:** [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) · [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](../reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) · [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md)  
**Related (reference, not superseded):** [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md)  
**Validated market (examples):** Грузотакси / Краснодар / проект Триумф

**This document delivers:** registry responsibilities, registry entities, lifecycle, identity model, integrity rules, non-goals, reality review.

**This document does not deliver:** runtime, JSON Schema, storage engine, acquisition adapters, Wordstat implementation, API integration, ORCA semantics, pack builder changes, or Phase 1 redesign.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This model defines **how Keyword Objects exist together** — organization, relationships, versioning discipline, and reference rules — not how they are collected, written to disk, or validated at runtime.

---

## Scope of this model

| In scope | Out of scope |
|----------|--------------|
| **Keyword Registry** as logical container and authority boundary | File layout, registry writer, merge scripts |
| Registry **entities** and ownership matrix | Collection acquisition, provider APIs |
| **Lifecycle** states and transition rules | Runtime state machines, automation |
| **Identity** — same, related, different | Semantic clustering, ORCA merge |
| **Integrity** rules — duplicates, conflicts, unknowns | Verify scripts, schema validation |
| **Versioning** and reference discipline | Git storage, immutability enforcement code |
| Alignment with Phase 2c Keyword Object fields | Redesign of Phase 2c object shape |

---

## Registry Responsibilities

### What is a Keyword Registry?

The **Keyword Registry** is the **session-scoped authoritative index** of Keyword Objects for one research session. It answers:

> **Which observable phrases were recorded for this session, under what identity, with what provenance and attachments, and what is explicitly unknown?**

The registry is **not** a search engine, **not** a cluster catalog, **not** a campaign structure, and **not** a cross-session phrase library. It is the **organizational layer** that binds Keyword Objects into a coherent, replayable demand-surface record.

**Normative container (logical):** `keyword_registry` — future artifact name `keyword_registry.json` per Keyword Intelligence v1 §5.5. This document defines **logical behavior**; file naming is reference only.

### What the registry owns

| Responsibility | Description |
|----------------|-------------|
| **Keyword identity** | Assignment and immutability of `keyword_id` within a session revision; index of all registered phrase identities |
| **Phrase history** | Ordered `provenance_records[]` per object — which channels observed the phrase, when, with what host context |
| **Provenance history** | Channel-level evidence trail (`KS-PROV-*`); registry preserves **all** provenance entries on merge — no silent overwrite |
| **Evidence references** | Session-level index of `evidence_refs[]` targets; registry **indexes** refs, does **not** duplicate upstream SoT (SERP, snapshots) |
| **Registry integrity** | Duplicate policy, conflict surfacing, session-level `safe_unknown[]`, stats by `source_type` |
| **Object lifecycle state** | Per-object registry state (`KR-LC-*`) — observed → registered → enriched → deprecated → archived |
| **Cross-object links** | **Related** phrase links (identity model) — explicit `related_keyword_refs[]`, not implicit clustering |
| **Revision pointer** | Which registry revision is current for the session; prior revisions retained when re-capture occurs |
| **Rollup authority** | On conflict between registry and derived views (`keyword_surface`, pack projections), **registry wins** |

### What the registry does NOT own

| Excluded concern | Owner / rule |
|------------------|--------------|
| **SERP outcomes** (URLs, positions, domains) | Market Surface — registry may reference `serp_result.json` only |
| **Page HTML facts** (title as page fact) | Website Intelligence — Keyword Surface references with `page_visible` provenance (KS-02) |
| **Raw provider captures** (Wordstat rows, suggestion API dumps) | **Keyword Snapshot** artifacts — registry **derives** objects from snapshots, does not replace them |
| **Extraction algorithms** (modifier tagging, intent derivation) | Separate gate — registry **stores** results, does not define matchers |
| **Storage engine, file paths, immutability enforcement** | Implementation gate |
| **Semantic equivalence** («грузотакси» = «грузовое такси») | **Forbidden** auto-merge — related link only |
| **Clustering, priority, strategy fields** | ORCA — forbidden on Keyword Object |
| **Cross-session phrase catalog** | Future catalog layer — **out of Phase 2d** |
| **Operator strategy notes** | ORCA / HITL outside registry |
| **Query execution decisions** | Human session scope — registry records what was observed, not what should run next |

### Registry authority rules

| Rule id | Statement |
|---------|-----------|
| **KR-OWN-01** | One **current** Keyword Registry per session revision — not per engine, not per provider |
| **KR-OWN-02** | Keyword Object fields defined in [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) remain canonical; registry adds **index and lifecycle** semantics only |
| **KR-OWN-03** | Snapshots are **upstream SoT** for raw capture; registry is **SoT** for registered Keyword Objects |
| **KR-OWN-04** | Research Pack sections (`keyword_observations`, `search_demand`) are **projections** — registry is authoritative on conflict |
| **KR-OWN-05** | Empty registry (zero Keyword Objects) is **valid** when keyword pass not executed — session-level SAFE UNKNOWN required |

---

## Registry Entities

### Entity overview

Six logical entities participate in registry organization. Only **Keyword Object** and **Keyword Registry** are authoritative for registered demand language; others are supporting or upstream.

```text
                    ┌─────────────────────────┐
                    │    Keyword Registry      │  ← session SoT for registered objects
                    │  (index + lifecycle)     │
                    └───────────┬─────────────┘
                                │ indexes 1..N
                                ▼
                    ┌─────────────────────────┐
                    │     Keyword Object       │  ← canonical per phrase identity
                    └───────────┬─────────────┘
            ┌───────────────────┼───────────────────┐
            │                   │                   │
            ▼                   ▼                   ▼
   Keyword Observation    Keyword Collection    related_keyword_refs[]
   (pre-register event)  (logical batch)       (explicit links only)

   Keyword Snapshot ──ingest──► Keyword Observation ──register──► Keyword Object
   (raw capture SoT)

   Keyword Surface ──derive──► rollup view (non-authoritative)
```

### Keyword Object

| Aspect | Definition |
|--------|------------|
| **Role** | Canonical record of one observable phrase identity within a session |
| **Owner** | Keyword Registry indexes it; object shape owned by Phase 2c data model |
| **Cardinality** | 0..N per session |
| **Registry adds** | `registry_state` (`KR-LC-*`), optional `related_keyword_refs[]`, `supersedes_keyword_id` when deprecated |

**Normative:** Phase 2c fields unchanged. Registry layer **must not** add forbidden ORCA/strategy fields.

### Keyword Registry

| Aspect | Definition |
|--------|------------|
| **Role** | Session-level index of Keyword Objects + session metadata |
| **Owner** | Keyword Surface layer (Demand Surface) |
| **Cardinality** | 1 current revision per session; 0..N historical revisions |

**Logical fields (conceptual — not schema):**

| Field | Required | Meaning |
|-------|----------|---------|
| **registry_id** | Yes | Opaque handle — typically aligns with `session_id` + revision |
| **session_id** | Yes | Owning research session |
| **revision** | Yes | Monotonic integer — `1` on first write; increments on re-capture |
| **keywords[]** | Yes | Array of Keyword Object references or embedded objects |
| **collections[]** | Optional | Keyword Collection descriptors (see below) |
| **stats** | Optional | `{ total, by_source_type, by_registry_state }` — derivable |
| **session_safe_unknown[]** | Yes | Session-level gaps — may be empty |
| **supersedes_revision** | Optional | Prior revision pointer when re-capture |
| **registry_state** | Yes | Session-level: `open` \| `frozen` \| `archived` |
| **capture_time** | Yes | Last material registry update |

### Keyword Collection

| Aspect | Definition |
|--------|------------|
| **Role** | **Logical batch** grouping Keyword Objects for navigation — **not** a semantic cluster |
| **Owner** | Keyword Registry declares collections; does not change object identity |
| **Cardinality** | 0..N per registry |

**Allowed collection kinds (normative):**

| Collection kind | Groups by | Example (pilot) |
|-----------------|-----------|-----------------|
| **seed_batch** | Declared Research Request seeds | mqgt01 seed list |
| **executed_batch** | Manifest `queries_executed` | 8 executed of 11 seeds |
| **suggestion_batch** | One suggestions snapshot invocation | `sg-yandex-{capture_id}` |
| **related_batch** | Related searches extracted from one SERP | per `serp_result` query |
| **wordstat_batch** | One Wordstat export ingest | **future** |
| **operator_batch** | Operator import worksheet | manual tag pass |

**Forbidden collection semantics:** campaign groups, ad groups, intent segments, head/tail buckets, ORCA themes, priority tiers.

| Rule id | Statement |
|---------|-----------|
| **KR-COL-01** | A Keyword Object may belong to **multiple** collections simultaneously |
| **KR-COL-02** | Collection membership **must not** imply merge, equivalence, or priority |
| **KR-COL-03** | Collections are **registry metadata** — omitting `collections[]` does not invalidate objects |

### Keyword Surface

| Aspect | Definition |
|--------|------------|
| **Role** | **Derived rollup** by `surface_type` / channel — human and pack convenience |
| **Owner** | Keyword Surface layer; **non-authoritative** vs registry |
| **Cardinality** | 0..1 per session (optional) |

**Relationship to registry:**

| Concern | Keyword Registry | Keyword Surface |
|---------|------------------|-----------------|
| Authority on conflict | **Wins** | Loses — refresh from registry |
| `keyword_ids[]` | Source | Denormalized cache |
| `strings[]` | Source via objects | Denormalized cache |
| Lifecycle | Full `KR-LC-*` | No independent lifecycle |

**Normative:** Keyword Surface is **derivable** from registry + snapshots. It **must not** introduce objects absent from registry.

### Keyword Observation

| Aspect | Definition |
|--------|------------|
| **Role** | **Pre-registration event** — a phrase seen in a capture channel before upsert into registry |
| **Owner** | Ingest boundary (future); registry **consumes** observations |
| **Cardinality** | 0..N per snapshot; 1..N may map to 0..1 Keyword Object |

**Distinction from Keyword Object:**

| Keyword Observation | Keyword Object |
|---------------------|----------------|
| Ephemeral ingest unit | Persistent registry record |
| May duplicate across observations | Deduped per identity rules |
| No `keyword_id` until registered | Has immutable `keyword_id` |
| Tied to one snapshot row / extract | May aggregate multiple provenance records |

**Lifecycle entry:** Observation → **register** → Keyword Object in state `registered`.

**Normative:** Observations **may** exist only in ingest logs in future implementation — logical entity defined here for boundary clarity. MVP has **no** observation layer — seeds exist only in manifest.

### Keyword Snapshot

| Aspect | Definition |
|--------|------------|
| **Role** | **Raw capture artifact** — immutable provider or extract output before normalization |
| **Owner** | Acquisition channel — **not** the registry |
| **Cardinality** | 0..N per session per channel type |

| Snapshot type | Logical artifact | Feeds |
|---------------|------------------|-------|
| **Wordstat snapshot** | `wordstat_snapshot.{capture_id}.json` | Observations → Keyword Objects + `numeric_slots` |
| **Suggestions snapshot** | `suggestions_snapshot.{engine}.{capture_id}.json` | Observations → `KS-PROV-SEARCH-SUGGESTION` objects |
| **SERP extract** | Rows from `serp_result.json` (related block) | Observations → `KS-PROV-RELATED-SEARCH` objects |
| **Operator worksheet** | Manual import file | Observations → `KS-PROV-OPERATOR-INPUT` objects |

| Rule id | Statement |
|---------|-----------|
| **KR-SNAP-01** | Snapshots are **append-only** within a session revision — re-capture adds new snapshot, does not mutate prior |
| **KR-SNAP-02** | Registry **references** snapshots via `evidence_refs[]` — never embeds full snapshot payload |
| **KR-SNAP-03** | Snapshot without registry upsert is **valid** (observed-but-not-registered) — must surface in session SAFE UNKNOWN |

### Entity ownership matrix

| Entity | Primary owner | Registry relationship |
|--------|---------------|----------------------|
| Keyword Object | Keyword Registry (index) | **Contained** |
| Keyword Registry | Keyword Surface / session | **Root** |
| Keyword Collection | Keyword Registry | **Metadata on registry** |
| Keyword Surface | Derived view | **Projection of registry** |
| Keyword Observation | Ingest boundary | **Input to registry** |
| Keyword Snapshot | Acquisition / upstream artifact | **Referenced by registry** |

### Reference discipline

| Rule id | Statement |
|---------|-----------|
| **KR-REF-01** | Cross-object links use **`keyword_id`** only — not phrase string joins |
| **KR-REF-02** | `related_keyword_refs[]` entries **must** include `relationship_kind` — see Identity Model |
| **KR-REF-03** | Evidence refs **must** use artifact role + path logical pointers — registry does not store SERP HTML |
| **KR-REF-04** | Market Surface domain refs on Keyword Object — **forbidden** as primary fields; allowed only inside `host_context` for provenance |

---

## Lifecycle

### Registry-level states

| State | Meaning |
|-------|---------|
| **open** | Registry accepts new objects and updates (within session) |
| **frozen** | No new registrations — enrichments may still apply per policy; typical pre-pack approval |
| **archived** | Session complete — registry read-only; tied to session archival |

### Object-level states (`KR-LC-*`)

| State | Meaning | Typical entry |
|-------|---------|---------------|
| **observed** | Phrase appears in snapshot or manifest; **not yet** in registry index | Raw SERP extract, snapshot row |
| **registered** | Keyword Object exists with `keyword_id`, minimum provenance, `evidence_refs[]` | First upsert from observation or seed copy |
| **enriched** | Modifiers, intent flags, and/or numeric slots materially populated beyond registration minimum | Manual tag pass, extraction run, Wordstat row attach |
| **deprecated** | Superseded or rejected — retained with tombstone semantics | Operator merge, duplicate resolution, bad import |
| **archived** | Session frozen — object read-only | Registry → `archived` |

**Note:** `observed` may exist **outside** the registry index (snapshot-only). Once `registered`, object **remains** in index through `deprecated` — not deleted.

### State transition diagram

```text
[upstream capture]
       │
       ▼
  KR-LC-OBSERVED ──register──► KR-LC-REGISTERED ──enrich──► KR-LC-ENRICHED
       │                              │                           │
       │                              │                           │
       └──────────────register────────┘                           │
                                      │                           │
                              deprecate ◄─────────────────────────┘
                                      │
                                      ▼
                              KR-LC-DEPRECATED
                                      │
                              session archive
                                      ▼
                              KR-LC-ARCHIVED
```

### Transition rules

| Rule id | From | To | Trigger | Guard |
|---------|------|-----|---------|-------|
| **KR-TR-01** | observed | registered | Upsert assigns `keyword_id` | Identity rules satisfied; ≥1 provenance record |
| **KR-TR-02** | registered | enriched | Modifiers, intent flags, or numeric slot moves from default empty / `not_captured` to populated | Enrichment **must not** change `phrase` or primary `source_type` without new object |
| **KR-TR-03** | registered / enriched | deprecated | Operator deprecate or dedup merge winner selected | `supersedes_keyword_id` or merge target documented; deprecated object kept |
| **KR-TR-04** | * | archived | Registry `registry_state` → `archived` | No further transitions except read |
| **KR-TR-05** | deprecated | registered | **Forbidden** — ids not recycled | Create new object with new id if phrase re-enters |
| **KR-TR-06** | enriched | registered | **Forbidden** — enrichment is not reversible to «un enriched» without new revision | Use new revision snapshot if rollback needed |

### What changes registry state

| Event | Changes state? | Detail |
|-------|----------------|--------|
| First upsert of phrase from seed/manifest | **Yes** → `registered` | Creates Keyword Object |
| Additional provenance on existing identity | **Yes** — merges records | Stays `registered` or `enriched` |
| Modifier / intent tag pass | **Yes** → `enriched` | If tags or flags added |
| Wordstat numeric attach | **Yes** → `enriched` | `numeric_slots` populated |
| Operator explicit merge | **Yes** — winner stays; loser → `deprecated` | Related refs updated |
| New suggestions snapshot ingest | **Yes** — new objects or provenance merge | Per identity rules |
| SERP re-fetch with same executed query | **Maybe** — new provenance record or new revision | **SAFE UNKNOWN** for provider drift until ingest policy chartered |
| Reading pack projection | **No** | Read-only |
| ORCA consumption | **No** | Downstream read-only |
| Market Surface competitor update | **No** | Different layer |
| Landing snapshot update | **No** — unless page_visible re-index chartered | New observation → optional new object |

### What does NOT change registry state

| Event | Reason |
|-------|--------|
| SERP position change for executed query | Market Surface concern |
| Competitor shortlist reorder | Market Surface |
| Comparison matrix update | Website Intelligence |
| Draft pack regeneration | Projection only |
| Operator **viewing** registry | Read-only |
| Hypothetical clustering in ORCA | Outside MIG |
| Missing Wordstat | Absence — declares SAFE UNKNOWN; does not auto-deprecate seeds |

### SAFE UNKNOWN in lifecycle

| Situation | Declaration |
|-----------|-------------|
| Snapshot exists, registry empty | «Keyword observations captured — registry not populated» |
| Seeds in manifest, no keyword pass | «Keyword registry not executed — demand objects not registered» |
| Partial enrich (modifiers only) | «Intent shape not derived» / per-family unknowns |
| Re-capture revision 2 without diff policy | «Registry revision 2 — diff against revision 1 not computed» — **UNKNOWN** until operator review |
| Observed count ≠ registered count | Session stats **must** expose both when observation layer exists |

**Normative:** Lifecycle transitions **must not** be inferred automatically from absence of data — explicit state only.

---

## Identity Model

### Purpose

Define when two phrase representations are **the same** Keyword Object, **related** but distinct objects, or **different** with no special link — without clustering, ORCA semantics, or synonym automation.

### Identity dimensions

Registry identity is the tuple:

```text
( session_id, phrase_normalized, primary source_type, engine? )
```

Plus **mandatory separation** rules that **override** tuple equality (KO-04, KO-06 from data model).

### Same — one Keyword Object

Two representations are the **same** object when **all** apply:

| Criterion | Rule |
|-----------|------|
| Same `session_id` | Required |
| Same `phrase_normalized` per KO-NORM-* | Required |
| Same **primary** `source_type` (`KS-PROV-*`) | Required |
| Same `engine` when channel is engine-bound | Required for suggestion / SERP channels |
| KO-06 separation **does not** apply | e.g. not seed vs page_visible with forced split |

**Action:** Merge `provenance_records[]`, union `evidence_refs[]`, retain single `keyword_id`.

**Example:**

| Phrase | source_type | Same? |
|--------|-------------|-------|
| «грузотакси Краснодар» (seed) | `operator_seed` | — |
| «грузотакси краснодар» (re-declared seed, same request) | `operator_seed` | **Same** — normalization match |

### Related — distinct objects, explicit link

Two Keyword Objects are **related** when they are **not** the same identity but share demand-language affinity **evidence** — registry records **`related_keyword_refs[]`**, never auto-merge.

| Relationship kind | Meaning | Example pair (pilot market) |
|-------------------|---------|----------------------------|
| **KR-REL-NORM_VARIANT** | Different `phrase_normalized`; obvious spelling/spacing variant | «грузотакси краснодар» ↔ «грузoтакси краснодар» (typo) — **if both captured** |
| **KR-REL-LEXICAL_VARIANT** | Near-synonym or reorder; **not** same normalized form | «грузотакси краснодар» ↔ «грузовое такси краснодар» |
| **KR-REL-EXTENSION** | One phrase adds tokens to another | «грузотакси краснодар» ↔ «грузотакси краснодар цены» |
| **KR-REL-CHANNEL_ECHO** | Same display phrase, different primary `source_type` | seed «грузотакси краснодар» ↔ suggestion «грузотакси краснодар» |
| **KR-REL-SHARED_HOST** | Suggestion related to seed via `host_context` | seed ↔ suggestion child |
| **KR-REL-OPERATOR** | Operator-declared association | Manual link only |

**Normative examples (Грузотакси / Краснодар):**

| Phrase A | Phrase B | Judgment | Link kind |
|----------|----------|----------|-----------|
| грузотакси краснодар | грузовое такси краснодар | **Related**, not same | `KR-REL-LEXICAL_VARIANT` |
| грузотакси краснодар | грузотакси краснодар цены | **Related**, not same | `KR-REL-EXTENSION` |
| грузотакси краснодар (seed) | грузотакси краснодар (executed) | **Related** by default (KO-04) | `KR-REL-CHANNEL_ECHO` — separate objects |
| грузотакси краснодар | грузотакси краснодар (same source, same engine) | **Same** | Merge |

**Rules:**

| Rule id | Statement |
|---------|-----------|
| **KR-ID-01** | **Related ≠ Same** — related pairs always have **two** `keyword_id` values |
| **KR-ID-02** | Related links are **directional optional** — store as undirected pair with canonical ordering by `keyword_id` |
| **KR-ID-03** | Registry **must not** auto-create `KR-REL-LEXICAL_VARIANT` without extraction rule or operator — default is **different with no link** |
| **KR-ID-04** | `KR-REL-EXTENSION` **must not** imply parent/child campaign structure — lexical only |
| **KR-ID-05** | Cross-session relatedness → **SAFE UNKNOWN** — out of scope |

### Different — no link required

Two objects are **different** when normalization differs **and** no operator or chartered rule establishes a `KR-REL-*` link.

| Phrase A | Phrase B | Judgment |
|----------|----------|----------|
| газель краснодар | перевозка мебели краснодар | **Different** — distinct service tokens |
| грузотакси краснодар | грузотакси москва | **Different** — geo scope |
| грузотакси краснодар цены | грузотакси краснодар отзывы | **Different** — distinct extensions (may also be `KR-REL-EXTENSION` to shared stem if operator links stem — **optional**) |

**Default:** Absence of link is **valid** — registry does not require complete graph.

### Identity decision flow (normative)

```text
Same session?
  No → DIFFERENT (cross-session UNKNOWN)
  Yes → Same phrase_normalized + same primary source_type + same engine (if applicable)?
    Yes → KO-06 forced split (page_visible vs executed)?
      Yes → DIFFERENT (+ optional KR-REL-CHANNEL_ECHO)
      No → SAME (merge)
    No → Operator merge or chartered rel rule?
      Yes → RELATED or SAME per operator
      No → DIFFERENT (link optional)
```

### Phrase normalization boundaries (identity)

Reuses KO-NORM-* from data model — registry **must not** extend normalization without charter amendment:

| Allowed for `phrase_normalized` | Forbidden |
|-----------------------------------|-----------|
| Trim, lowercase, NFC, whitespace collapse | Stemming, lemmatization |
| Preserve punctuation in `phrase` | Transliteration RU↔EN auto-merge |
| | Synonym dictionary merge |
| | «грузотакси» ↔ «грузовое такси» collapse |

**SAFE UNKNOWN:** Equivalence beyond normalization → «Phrase equivalence not attested — separate identities retained».

---

## Integrity Rules

Reality-first discipline — registry surfaces conflicts; it does not silently resolve strategy questions.

### Duplicate handling

| Scenario | Rule |
|----------|------|
| Exact identity tuple duplicate on upsert | **Merge** — union provenance and evidence refs (KO-03) |
| Same `phrase`, different `source_type` | **Separate objects** — optional `KR-REL-CHANNEL_ECHO` (KO-04) |
| Same normalized phrase, different `engine` | **Separate objects** — engine is identity dimension for bound channels |
| Operator forced duplicate ids | **Forbidden** — reject at implementation gate |
| Re-ingest same snapshot | **Idempotent merge** — no duplicate objects |

| Rule id | Statement |
|---------|-----------|
| **KR-INT-01** | Merge **never** deletes provenance history — append-only union |
| **KR-INT-02** | Stats `by_source_type` **must** count objects after merge, not raw observation rows |

### Conflicting provenance

| Scenario | Handling |
|----------|----------|
| Same object, two provenance records, conflicting `host_context` | **Retain both** — declare object-level SAFE UNKNOWN |
| Seed declared, never executed | Provenance on seed object only + SAFE UNKNOWN «not executed» |
| `page_visible` phrase matches executed query | **Separate objects** (KO-06) + optional `KR-REL-CHANNEL_ECHO` |
| Operator disputes automated provenance | Add operator provenance record; **do not** delete extracted record — operator wins for **display grade** only |

### Missing evidence

| Scenario | Handling |
|----------|----------|
| Object without `evidence_refs[]` (non-operator-only) | **Invalid for `registered`** — stays `observed` or blocked |
| Suggestion string without snapshot | Register with `evidence_grade: operator` + SAFE UNKNOWN |
| Wordstat phrase without snapshot ref | `numeric_slots: not_captured` + SAFE UNKNOWN — object may exist with phrase only if chartered |
| Broken artifact pointer | Object-level SAFE UNKNOWN «evidence ref unresolved» |

| Rule id | Statement |
|---------|-----------|
| **KR-INT-03** | Missing evidence **≠** negative evidence — never infer zero frequency |
| **KR-INT-04** | Session-level SAFE UNKNOWN **must** aggregate pass-level gaps (keyword pass not run, Wordstat not captured) |

### Provider disagreement

| Scenario | Handling |
|----------|----------|
| Two Wordstat exports, different `shows` for same phrase | `numeric_slots.freq.status: provider_conflict` — preserve `conflict_values[]` (NUM model) |
| Suggestion list changed between captures | **Separate snapshots** — new provenance or revision; **no** silent overwrite |
| Related search block differs on SERP re-fetch | New provenance with new `capture_time`; prior retained in revision history |

**Normative:** Registry **must not** pick winner in provider conflict without operator `evidence_grade: operator` override.

### Phrase normalization boundaries (integrity)

| Check | On failure |
|-------|------------|
| Empty phrase after trim | Reject registration |
| Phrase > max length (implementation cap) | Reject with operator alert — **UNKNOWN** limit in Phase 2d |
| Mixed scripts without capture context | Register with SAFE UNKNOWN «script/locale ambiguity» |
| Normalization collision (distinct phrases → same normalized) | **Separate display phrases**, one normalized key — merge only if source_type+engine match; else **related or different** per operator |

### Registry-wide caps (reference — implementation deferred)

Per Keyword Intelligence v1: ~2000 objects per session hard cap with operator alert. Phase 2d **does not** set runtime enforcement — documents expectation only.

### Integrity checklist (session close)

Before registry `frozen`:

| Check | Required |
|-------|----------|
| Every `registered` object has ≥1 provenance record | Yes |
| Session SAFE UNKNOWN reflects absent passes | Yes |
| Deprecated objects have documented reason | When deprecated > 0 |
| `stats.total` matches `keywords[]` length | Yes |
| No forbidden ORCA fields present | Yes |

---

## Non-Goals

Explicit exclusions for this registry model and immediate follow-on until separately chartered:

| Non-goal | Rationale |
|----------|-----------|
| **SEO clusters / semantic core** | ORCA — registry stores objects, not themes |
| **Campaign structures** | ORCA execution layer |
| **ORCA semantics** | Downstream interpretation |
| **Ad groups** | PPC structure — ORCA |
| **Content plans** | MetaBOT / Factory / ORCA |
| **Keyword difficulty** | Third-party SEO metric |
| **Priority scoring** | ORCA — forbidden field |
| **Ranking strategy** | ORCA |
| **Wordstat runtime** | Acquisition gate |
| **Search volume tiers** | Interpretation — forbidden |
| **Autonomous dedup / merge** | Human or chartered rules only |
| **Cross-session registry** | Future catalog — not Phase 2d |
| **JSON Schema / registry writer** | Phase 2e+ implementation gate |
| **Storage engine design** | Implementation gate |
| **Phase 1 redesign** | MVP freeze honored |

---

## Reality Review

### Question

Can this registry model support future **Wordstat**, **Search Suggestions**, **Related Searches**, and **Operator Input** without redesign?

### Answer

**Yes — for registry organization.** Phase 2c object shape and Phase 2d lifecycle, identity, and integrity rules accommodate all four input channels via Keyword Snapshot → Keyword Observation → registry upsert. **Implementation** (adapters, files, writers) remains unbuilt.

### Source-by-source assessment

| Source | Supported without redesign? | Registry mechanism | Honest gaps |
|--------|----------------------------|-------------------|-------------|
| **Operator Input** | **Yes** | `KS-PROV-OPERATOR-INPUT`; `operator_batch` collection; `evidence_grade: operator` | Operator merge policy at scale — procedural, not model gap |
| **Search Suggestions** | **Yes** | `suggestions_snapshot` → observations → objects; `suggestion_batch`; `host_context` seed link; `KR-REL-SHARED_HOST` | Recursive expansion still forbidden (KI-03) |
| **Related Searches** | **Yes** | SERP extract snapshot → `related_batch`; `KS-PROV-RELATED-SEARCH` | MVP did not extract — registry empty valid with SAFE UNKNOWN |
| **Wordstat** | **Yes** | `wordstat_batch`; `KS-PROV-FUTURE-WORDSTAT`; numeric enrich → `enriched`; `provider_conflict` integrity | Multi-row **history** per phrase across periods — may need `observation` array extension in trend slot; not registry redesign |

### Entity fit

| Future need | Phase 2d entity | Amendment required? |
|-------------|-----------------|---------------------|
| Multiple Wordstat exports per session | Keyword Snapshot (multiple) + revision | **No** — `revision` increment |
| Same phrase seed + Wordstat + suggestion | Three objects or merged provenance | **No** — identity rules explicit |
| Time-series &gt;2 points | Trend slot | **Possible** Phase 2e trend slot array — not registry container change |
| Cross-session phrase catalog | — | **Yes — future layer** — explicitly out of scope |
| ORCA cluster export | — | **No MIG amendment** — ORCA consumes registry read-only |

### What would require model amendment

| Need | Assessment |
|------|------------|
| Global phrase id across sessions | New catalog entity — **outside** Keyword Registry |
| Automatic lexical variant linking | Would violate KR-ID-03 — **forbidden** without charter change |
| Cluster membership on registry | **Forbidden** — non-goal |
| Real-time sync with live SERP | Operational — revision policy, not entity redesign |

### Confidence

| Area | Level | Basis |
|------|-------|-------|
| Registry responsibility clarity | **A-** | Strict owns / does-not-own matrix |
| Entity model completeness | **B+** | Six entities; observation layer logical only |
| Lifecycle sufficiency | **B+** | Covers enrich and deprecate; re-capture via revision |
| Identity model for pilot phrases | **B** | Examples grounded; lexical variant auto-link intentionally withheld |
| Integrity / conflict handling | **B+** | Aligns with Phase 2c numeric conflict model |
| Ready for implementation | **N/A** | **Not authorized** — architecture only |

---

## Architecture decisions (registry model)

| ID | Decision | Rationale |
|----|----------|-----------|
| **KR-AD-01** | Keyword Registry is **session-scoped SoT** for Keyword Objects | Aligns Keyword Intelligence KI-01 |
| **KR-AD-02** | Keyword Collection is **batch metadata**, not cluster | Prevents ORCA bleed |
| **KR-AD-03** | Keyword Observation is **pre-register** logical entity | Separates snapshot ingest from index |
| **KR-AD-04** | Identity **same / related / different** is normative without auto-synonym merge | Reality-first; ORCA owns semantics |
| **KR-AD-05** | Lifecycle `observed` may exist outside index | Honest pre-pass state |
| **KR-AD-06** | Registry wins over Keyword Surface on conflict | KI-08 / charter rollup rule |
| **KR-AD-07** | Provider conflict preserved, not averaged | NUM-06 / reality-first |

---

## Recommended Next Step

1. **Human review** of identity examples against mqgt01 seed list — tabletop: classify pairs as same / related / different.
2. **Phase 2e gate (optional):** JSON Schema stub for registry container fields only — still no registry writer.
3. **Research Pack contract stub** — projection rules from registry (`stats`, sample `keyword_id`s, SAFE UNKNOWN aggregation).
4. **Operator manual tag pass** on pilot — validate `enriched` transition with real phrases.
5. **Wordstat readiness decision** — separate charter; registry model does not authorize ingest.
6. **Stop condition:** If work shifts to clustering, volume tiers, schema implementation, or ORCA enums — stop and split per [boundaries.md](../boundaries.md).

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) | Phase 2c — Keyword Object shape |
| [MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md](MIG-KEYWORD-SURFACE-CAPABILITY-MODEL-v1.md) | Phase 2b — capabilities |
| [MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md](../reports/MIG-PHASE2-KEYWORD-SURFACE-CHARTER-v1.md) | Phase 2a mission |
| [mig-keyword-intelligence-architecture-v1.md](mig-keyword-intelligence-architecture-v1.md) | Acquisition channel (future) — §5–6 registry reference |
| [boundaries.md](../boundaries.md) | MIG vs ORCA |
| [MIG-MVP-VALIDATION-FREEZE-v1.md](../reports/MIG-MVP-VALIDATION-FREEZE-v1.md) | Phase 1 evidence |

---

*MIG Keyword Registry Model v1 · 2026-06-06 · registry organization only · no runtime*
