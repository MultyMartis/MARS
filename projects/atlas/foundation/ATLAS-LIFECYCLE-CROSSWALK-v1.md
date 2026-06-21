# ATLAS Lifecycle Crosswalk v1

**Status:** **documented** — Phase 5 reconciliation across Phases 1–4 lifecycle semantics.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-LIFECYCLE-MODEL-v1.md](ATLAS-LIFECYCLE-MODEL-v1.md) · [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md)  
**Is not:** retroactive edit of approved Phase 1–4 documents.

---

## 1. Purpose

**Eliminate semantic drift** by mapping lifecycle language found in Reality, Relationship, Identity, and Registry Architecture foundations to the **Phase 5 authoritative vocabulary**.

**Rule:** Where Phase 5 defines a unified code, **implementations and new docs** use Phase 5. Prior phase documents remain approved; this crosswalk is the **interpretation layer** for consumers and future charters.

---

## 2. Authoritative vocabulary (Phase 5)

### 2.1 Universal core

`proposed` · `active` · `disputed` · `deprecated` · `archived`

### 2.2 Facet extensions

| Code | Facet |
|------|-------|
| `merged` | Entity / identity record (absorbed id) |
| `split_source` | Entity record (split origin) |
| `replaced` | Relationship record (superseded edge) |

### 2.3 Non-state

**SAFE UNKNOWN** — slot/subject posture, not `lifecycle_state` on a row.

---

## 3. Phase 1 — Reality Foundation

| Source | Prior language | Phase 5 mapping | Notes |
|--------|----------------|-----------------|-------|
| [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) | Human attestation; SAFE UNKNOWN | **proposed** / **active** / UNKNOWN posture | No explicit state enum in Phase 1 |
| [ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-08 | Tombstone; id not reused | **deprecated** · **merged** · **archived** | Aligns with invariants LC-INV-07 |
| [ATLAS-ENTITY-TAXONOMY-v1.md](ATLAS-ENTITY-TAXONOMY-v1.md) | Project lifecycle (proposed → active → closed) | **proposed** → **active** → **deprecated** | **closed** → **deprecated**, not ops “closed” |
| [ATLAS-EXPANSION-RULES-v1.md](ATLAS-EXPANSION-RULES-v1.md) | Status lifecycle on Project must not become workflow | Phase 5 **LC-BAN-01** reaffirms | No contradiction |
| [ATLAS-BOUNDARIES-v1.md](ATLAS-BOUNDARIES-v1.md) | Contract lifecycle tools | **Out of scope** — not ATLAS lifecycle | Boundary preserved |

**Phase 1 gap filled:** Phase 1 implied lifecycle discipline; Phase 5 makes state registry normative.

---

## 4. Phase 2 — Relationship Foundation

| Source | Prior language | Phase 5 mapping | Notes |
|--------|----------------|-----------------|-------|
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) §2 | proposed, active, deprecated, replaced, disputed, archived | **1:1** on relationships | Phase 2 is specialized detail; states unchanged |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) §8 | Lifecycle overview pointer | Use Phase 5 + Phase 2 mechanics | |
| [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) | Dispute resolution | **disputed** → resolution transitions | Governance unchanged |
| FORMER_* types | Taxonomy type prefix | **Not** lifecycle states | May coexist with **deprecated** |

**Relationship archive:** Phase 2 **archived** affirmed — relationships **can** be archived (Phase 5 analysis Q3).

**No contradiction** identified between Phase 2 and Phase 5.

---

## 5. Phase 3 — Identity Foundation

| Source | Prior language | Phase 5 mapping | Notes |
|--------|----------------|-----------------|-------|
| [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) §7.1 | proposed, active, deprecated, merged_into, split_from, disputed, archived | See §6 conflicts | Unified codes **merged**, **split_source** |
| [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) §7.2 diagram | intake → proposed → active | **1:1** | |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) | Merge → `merged_into` + redirect | **merged** + `redirect_to` | Synonym documented |
| [ATLAS-IDENTIFIER-MODEL-v1.md](ATLAS-IDENTIFIER-MODEL-v1.md) | deprecated, replaced, archived for REL-* | Relationship facet **replaced** | Identifier doc references rel lifecycle |

**Identity = entity record lifecycle:** Phase 3 identity lifecycle states apply to **entity registry rows**, not a parallel shadow state machine.

---

## 6. Documented conflicts and resolutions

### 6.1 Naming: `merged_into` vs `merged`

| Aspect | Phase 3 | Phase 5 resolution |
|--------|---------|-------------------|
| Code string | `merged_into` | Normative: **`merged`** |
| Semantics | Absorbed id + redirect | Unchanged |
| Action | **No Phase 3 edit** | Crosswalk synonym; implementations accept both during migration |

**Severity:** Low — cosmetic code alignment.

### 6.2 Naming: `split_from` vs `split_source`

| Aspect | Phase 3 | Phase 5 resolution |
|--------|---------|-------------------|
| Code string | `split_from` | Normative: **`split_source`** |
| Semantics | Split origin id | Unchanged |

**Severity:** Low.

### 6.3 Entity registry list vs identity list

| Aspect | [ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md) §4.1 | Phase 3 §7.1 |
|--------|-----------------------------------------------------------------------------|--------------|
| Listed states | proposed · active · disputed · deprecated | + merged · split_source · archived |
| Resolution | Phase 5 registry is **complete** for entities | ER model “variants per Phase 2” = **replaced** on relationships only |

**Severity:** Low — ER model deferred packaging explicitly to Phase 5.

### 6.4 MERGED as universal vs facet

| Mission brief candidate | Phase 5 |
|-------------------------|---------|
| MERGED universal | **merged** is **entity facet**; relationships use **replaced**, not merged |

**Severity:** None — architectural decision documented in State Registry §2.

### 6.5 Reactivation mention

| Source | Text | Phase 5 |
|--------|------|---------|
| [ATLAS-CHANGE-GOVERNANCE-v1.md](ATLAS-CHANGE-GOVERNANCE-v1.md) §3.1 | Reactivate deprecated entity | **deprecated** → **active** allowed (rare) |
| Phase 5 | **merged** → **active** forbidden | Consistent — reactivation applies to **deprecated**, not absorbed ids |

**No contradiction.**

### 6.6 Contradictions requiring Phase 1–4 edits

**None identified** at Phase 5 authoring. Prior docs remain authoritative; Phase 5 supersedes **vocabulary interpretation** only.

---

## 7. Phase 4 — Registry Architecture Foundation

| Source | Prior language | Phase 5 mapping | Notes |
|--------|----------------|-----------------|-------|
| [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) RA-05 | proposed, active, disputed, deprecated | Subset of core — **archived** added in unified registry | RA-05 non-exhaustive list |
| [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) C-02 | active for canonical | **active** + attest + no **disputed** block | |
| [ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md) §5 | Intake diagram proposed → active → disputed → deprecated | Add **merged** · **archived** · **split_source** | Diagram superseded by Phase 5 §9 |
| [ATLAS-ENTITY-REGISTRY-MODEL-v1.md](ATLAS-ENTITY-REGISTRY-MODEL-v1.md) §5 | “Deferred to Registry Lifecycle Foundation” | **Delivered** — this package | |
| [ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md) §10 diagram | ACTIVE, DISPUTED, SAFE UNKNOWN | **active**, **disputed**, UNKNOWN posture | Case convention only |
| [ATLAS-CONSUMER-CONTRACTS-v1.md](ATLAS-CONSUMER-CONTRACTS-v1.md) | Respect disputed/deprecated | Must add **merged** · **replaced** · **archived** | Consumer contract extension in adoption package |

**Phase 4 explicit deferral** ([ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md) closeout): unified registry lifecycle → **resolved by Phase 5**.

---

## 8. Cross-facet lifecycle matrix (reconciliation)

| Business question | Entity record | Relationship record |
|-------------------|---------------|---------------------|
| Is this org canonical now? | **active** on ORG-* | N/A |
| Does client link exist now? | N/A | **active** CLIENT_OF (dates) |
| Did org cease to exist as separate unit? | Loser **merged** | N/A |
| Did client link end? | N/A | **deprecated** / FORMER_* |
| Was edge corrected? | N/A | **replaced** + successor |
| Is ownership contested? | Entities may stay **active** | Slot **disputed** / SAFE UNKNOWN |

---

## 9. Consumer mapping guidance (normative intent)

Consumers **must** implement a mapping table:

| ATLAS `lifecycle_state` | May display (example) | Must not store as ATLAS code |
|-------------------------|----------------------|------------------------------|
| proposed | Candidate | pending_review |
| active | Canonical | live, verified |
| disputed | Contested | conflict |
| deprecated | Ended | closed, inactive |
| merged | Absorbed | deleted |
| split_source | Split origin | split |
| replaced | Superseded | outdated |
| archived | Archived | removed |

---

## 10. Implementation pointers (non-normative)

When implementation exists:

1. Single enum module citing Phase 5 State Registry.  
2. Relationship service accepts **replaced**; entity service accepts **merged** / **split_source**.  
3. Migration aliases: `merged_into` → `merged`, `split_from` → `split_source`.  
4. Validation engine enforces [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](ATLAS-LIFECYCLE-TRANSITIONS-v1.md) forbidden list.

---

## 11. Open crosswalk items (for adoption package)

| Item | Owner doc (future) |
|------|-------------------|
| Exact consumer API field names | Consumer Adoption Framework |
| Cache TTL vs lifecycle refresh | Consumer Adoption Framework |
| Redirect table format for **merged** | Implementation charter |

---

*ATLAS Lifecycle Crosswalk v1 — Phase 1–4 reconciliation. Documentation only.*
