# MIG Keyword Registry Writer Contract v1

**Status:** **normative** — logical write behaviors only (Phase 2g / G-04)  
**Date:** 2026-06-06  
**Lane:** A — MIG Phase 2 Planning  
**Phase:** 2g — Provider Infrastructure Contracts  
**Gate closed:** **G-04** — Registry writer logical upsert contract  
**Prior artifacts:** [MIG-KEYWORD-REGISTRY-MODEL-v1.md](MIG-KEYWORD-REGISTRY-MODEL-v1.md) · [MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md](MIG-KEYWORD-SURFACE-DATA-MODEL-v1.md) · [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md) · [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md)  
**Validated market (examples):** Грузотакси / Краснодар / проект Триумф

**This document delivers:** required logical behaviors for create, merge, conflict, deprecate, and freeze registry operations.

**This document does not deliver:** storage engine, file I/O, code, JSON Schema, or automated registry implementation.

---

## Canonical boundary (normative)

> **MIG acquires reality. ORCA interprets reality.**

This contract defines **what a registry writer must do** when invoked — not **how** it is implemented. No storage engine is authorized by this document.

---

## Writer role

The **registry writer** is the logical component that:

1. Accepts Keyword Observations or fully shaped Keyword Objects as input.
2. Applies identity, merge, and integrity rules from Phase 2c/2d.
3. Mutates the **current** Keyword Registry revision for a session.
4. Surfaces conflicts and SAFE UNKNOWN — never silent resolution.

**Authority:** Keyword Registry is session SoT for registered demand language (KR-OWN-04). Writer **must not** write ORCA or strategy fields.

---

## Preconditions (all operations)

| Precondition | Requirement |
|--------------|-------------|
| Session exists | Valid `session_id` |
| Registry state | `open` — **except** read-only operations on `frozen` / `archived` |
| Input shape | Conforms to [MIG-KEYWORD-SCHEMA-STUB-v1.md](MIG-KEYWORD-SCHEMA-STUB-v1.md) |
| Mapping applied | Provider rows passed through [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md) when from snapshot |
| Snapshot SoT | Raw provider file referenced before registry claims authority (PCR-01) |

**Rejected input (normative):** Empty phrase; forbidden ORCA fields; registration without provenance when `evidence_grade` ≠ pure operator-declared seed copy.

---

## Operation: Create object

**Purpose:** Register a new Keyword Object when identity tuple does not match an existing object.

### Trigger

| Input | Create when |
|-------|-------------|
| Keyword Observation | No existing object matches `(session_id, phrase_normalized, primary source_type, engine?)` |
| Seed copy from manifest | First registration of operator seed |
| Operator manual phrase | New `operator_input` identity |

### Required behaviors

| # | Behavior |
|---|----------|
| **CR-01** | Assign new **keyword_id** — opaque, unique within session revision |
| **CR-02** | Set **registry_state** → `registered` |
| **CR-03** | Copy **phrase**, **provenance_records[]**, **evidence_refs[]**, **evidence_grade**, **safe_unknown[]** from input |
| **CR-04** | Initialize **modifier_tags[]** and **intent_shape_flags[]** — may be empty tags + explicit UNKNOWN flag per Phase 2c |
| **CR-05** | Initialize **numeric_slots** — absent or all slots `not_captured` unless provider input supplies values |
| **CR-06** | Set **capture_time** to operation timestamp (ISO-8601 UTC) |
| **CR-07** | Increment registry **stats** (if maintained) |
| **CR-08** | Append object to registry **keywords[]** |
| **CR-09** | Non-operator-only objects **must** have ≥1 **evidence_refs[]** — else reject (KR-INT-03) |

### Postconditions

| Check | Expected |
|-------|----------|
| Object retrievable by **keyword_id** | Yes |
| **keyword_id** immutable thereafter | Yes (KO-01) |
| Duplicate identity tuple | Should not occur — merge path instead |

---

## Operation: Merge object

**Purpose:** Upsert into existing Keyword Object when identity tuple matches (KO-03).

### Trigger

| Input | Merge when |
|-------|------------|
| Same phrase_normalized + same primary **source_type** + same **engine** (when applicable) | Identity match |
| Re-ingest identical snapshot row | Idempotent merge (MAP-09) |
| Additional provenance for executed query already registered | Provenance append |

### Required behaviors

| # | Behavior |
|---|----------|
| **MG-01** | Retain existing **keyword_id** — never reassign |
| **MG-02** | **Append** new **provenance_records[]** entries — never delete prior (KR-INT-01, PCR-10) |
| **MG-03** | Union **evidence_refs[]** — dedupe by logical pointer equality |
| **MG-04** | Union **safe_unknown[]** — dedupe identical strings |
| **MG-05** | Update **capture_time** |
| **MG-06** | **Must not** change **phrase** or primary **source_type** without creating new object (KR-TR-02) |
| **MG-07** | Numeric merge: if new freq equals existing → no conflict; if different same period/region → **conflict** path (see below) |
| **MG-08** | If enrichment fields supplied (modifiers, intent), merge arrays per MOD-04 / IS rules — may transition to `enriched` |

### Forbidden merge behaviors

| Forbidden | Rule |
|-----------|------|
| Delete provenance history | KR-INT-01 |
| Merge seed object with Wordstat object | KO-04, PCR-09 |
| Merge `page_visible` with `executed_query` | KO-06 |
| Auto-merge lexical variants | KR-ID-03 |

---

## Operation: Conflict object

**Purpose:** Surface provider numeric disagreement without picking a winner.

### Trigger

| Condition | Action |
|-----------|--------|
| Merge or second ingest: same identity tuple, same region_scope + period_scope, different frequency value | Set **numeric_slots.freq.status** → `provider_conflict` |
| Operator attaches conflicting export to same object | Same |

### Required behaviors

| # | Behavior |
|---|----------|
| **CF-01** | Set **numeric_slots.freq.status** = `provider_conflict` |
| **CF-02** | Populate **conflict_values[]** with all observed values + **provider_ref** + **capture_time** |
| **CF-03** | Clear single **value** field — no winner (MAP spec, NUM model) |
| **CF-04** | Append object **safe_unknown[]**: «Numeric provider conflict — operator verification required» |
| **CF-05** | Append provenance for **both** captures |
| **CF-06** | **Must not** average, max, min, or prefer-latest (PCR-03, KR-AD-07) |
| **CF-07** | Session **session_safe_unknown[]** should note conflict count when >0 |

### Operator resolution (procedural — not writer automation)

Operator may later: deprecate incorrect object; add operator provenance documenting verified value; or leave conflict exposed for ORCA/HITL. Writer **must not** auto-resolve.

---

## Operation: Deprecate object

**Purpose:** Tombstone a Keyword Object without deleting history.

### Trigger

| Scenario | Deprecate |
|----------|-----------|
| Operator dedup — merge winner selected | Loser deprecated |
| Bad import row | Operator reject |
| Duplicate forced by operator policy | Loser deprecated |
| Phrase rejected from registry | Operator action |

### Required behaviors

| # | Behavior |
|---|----------|
| **DP-01** | Set **registry_state** → `deprecated` |
| **DP-02** | Set **supersedes_keyword_id** or document merge target in provenance |
| **DP-03** | Object **remains** in **keywords[]** index — not deleted (KR-TR-03) |
| **DP-04** | Record deprecation reason in **safe_unknown[]** or operator annotation ref |
| **DP-05** | Update **related_keyword_refs[]** on surviving object when applicable |
| **DP-06** | **Must not** recycle **keyword_id** (KR-TR-05) |
| **DP-07** | Deprecated object **excluded** from stats `by_registry_state` active counts unless stats explicitly include deprecated |

### Forbidden

| Forbidden | Reason |
|-----------|--------|
| Hard delete from registry | Audit trail loss |
| Deprecated → registered transition | KR-TR-05 |
| Silent remove from index | Integrity violation |

---

## Operation: Freeze registry

**Purpose:** Mark registry revision read-only for pack projection and session close.

### Trigger

| Event | Freeze |
|-------|--------|
| Operator completes Human Review Gate (HR-01..HR-05) | Manual freeze |
| Session archival workflow | Auto freeze with archive |
| Pre-pack approval checkpoint | Policy-dependent |

### Required behaviors

| # | Behavior |
|---|----------|
| **FR-01** | Set registry **registry_state** → `frozen` |
| **FR-02** | Set all non-deprecated objects **registry_state** → `archived` when session archives; or leave `registered`/`enriched` when frozen-only |
| **FR-03** | Reject create, merge, deprecate (except operator emergency with new revision — see FR-05) |
| **FR-04** | Run integrity checklist (below) — failures **block** freeze unless operator documents waiver |
| **FR-05** | Re-capture requires **new revision** (`revision` increment, **supersedes_revision** pointer) — do not mutate frozen revision in place |
| **FR-06** | Update registry **capture_time** |

### Integrity checklist (before freeze)

| Check | Required |
|-------|----------|
| Every `registered` / `enriched` object has ≥1 provenance record | Yes |
| Session **session_safe_unknown[]** reflects absent passes / partial coverage | Yes |
| No forbidden ORCA fields | Yes |
| **stats.total** matches **keywords[]** length (non-deprecated policy documented) | Yes |
| Deprecated objects have documented reason when count > 0 | Yes |
| Provider conflicts surfaced, not averaged | When conflicts exist |

---

## Session-level SAFE UNKNOWN aggregation

Writer **must** maintain **session_safe_unknown[]** on registry:

| Event | Session SAFE UNKNOWN action |
|-------|----------------------------|
| Keyword pass not run | «Keyword registry not executed — demand objects not registered» |
| Snapshot without registry upsert | «Keyword observations captured — registry not populated» |
| Partial phrase coverage | «Provider rows missing for: …» |
| Wordstat not captured | «Frequency evidence not captured for this session» |
| Revision 2 without diff | «Registry revision N — diff against prior revision not computed» |

**Normative:** Absence of data **must not** auto-populate objects — declare at session level.

---

## Lifecycle transitions (writer responsibility)

| From | To | Writer operation |
|------|-----|------------------|
| *(none)* | `registered` | **Create object** |
| `registered` | `enriched` | **Merge object** with modifiers / intent / numeric populate |
| `registered` / `enriched` | `deprecated` | **Deprecate object** |
| `*` | `archived` | **Freeze registry** (session archive) |
| `observed` | `registered` | **Create object** from observation |

Writer **must not** transition `enriched` → `registered` (KR-TR-06).

---

## Collection updates (optional)

When **collections[]** maintained:

| Operation | Behavior |
|-----------|----------|
| Create | Add object id to `wordstat_batch`, `seed_batch`, etc. |
| Merge | Retain collection membership |
| Deprecate | Remove from active batch views; optional tombstone in collection metadata |
| Freeze | Collections immutable |

Collections **must not** imply merge or priority (KR-COL-02).

---

## Error handling (logical — no implementation)

| Error | Writer response |
|-------|-----------------|
| Registry frozen | Reject mutation; suggest new revision |
| Identity ambiguous | Reject; require operator input |
| Missing evidence_refs | Reject create |
| Forbidden field in input | Reject entire operation |
| Phrase empty after trim | Reject |
| Provider conflict on merge | **Conflict object** — not error |

---

## Architecture decisions (registry writer contract)

| ID | Decision | Rationale |
|----|----------|-----------|
| **KR-WC-01** | Five operations: create, merge, conflict, deprecate, freeze | Covers G-04 minimal set |
| **KR-WC-02** | Conflict is explicit operation outcome | Not silent merge branch |
| **KR-WC-03** | No hard deletes | KR-TR-03, audit trail |
| **KR-WC-04** | Freeze requires integrity checklist | Registry Model §Integrity checklist |
| **KR-WC-05** | Re-capture = new revision | KR-SNAP-01, revision policy |

---

## Related documents

| Document | Role |
|----------|------|
| [MIG-KEYWORD-REGISTRY-MODEL-v1.md](MIG-KEYWORD-REGISTRY-MODEL-v1.md) | Phase 2d lifecycle + identity |
| [MIG-PROVIDER-MAPPING-SPEC-v1.md](MIG-PROVIDER-MAPPING-SPEC-v1.md) | Input mapping (G-03) |
| [MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md](MIG-KEYWORD-PASS-MANIFEST-CONTRACT-v1.md) | Manifest truth (G-05) |
| [MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md](../reports/MIG-PROVIDER-CONNECTION-AUTHORIZATION-v1.md) | Human Review Gate |

---

*MIG Keyword Registry Writer Contract v1 · 2026-06-06 · logical behaviors only · G-04 closed · no storage engine · no code*
