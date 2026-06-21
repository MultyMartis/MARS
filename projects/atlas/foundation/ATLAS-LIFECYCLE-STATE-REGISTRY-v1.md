# ATLAS Lifecycle State Registry v1

**Status:** **documented** — Phase 5 normative state vocabulary.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-LIFECYCLE-MODEL-v1.md](ATLAS-LIFECYCLE-MODEL-v1.md)  
**Companion:** [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](ATLAS-LIFECYCLE-TRANSITIONS-v1.md) · [ATLAS-LIFECYCLE-CROSSWALK-v1.md](ATLAS-LIFECYCLE-CROSSWALK-v1.md)  
**Is not:** database enum migration script, UI copy deck.

---

## 1. Purpose

Provide the **authoritative registry of lifecycle states** — codes, meanings, entry/exit conditions, and transition constraints — after architectural evaluation of candidate lists from Phases 1–4 and the Phase 5 mission brief.

---

## 2. Evaluation of candidate universal states

### 2.1 Candidates from mission brief

| Candidate | Verdict | Rationale |
|-----------|---------|-----------|
| **PROPOSED** | **Universal core** | Required for human-gated intake ([ATLAS-ATTESTATION-MODEL-v1.md](ATLAS-ATTESTATION-MODEL-v1.md)) |
| **ACTIVE** | **Universal core** | Only forward-canonical state |
| **DISPUTED** | **Universal core** | Required for contested claims without silent dual canonical |
| **DEPRECATED** | **Universal core** | Ended reality with audit; Phase 1–4 already use |
| **MERGED** | **Universal facet** (entity) | Absorption is distinct from mere deprecation — redirect semantics |
| **ARCHIVED** | **Universal core** | Long-term read-only; Phase 2 relationships already define |

### 2.2 Additional states required by prior phases (not in brief list)

| State | Verdict | Rationale |
|-------|---------|-----------|
| **replaced** | **Relationship facet** | Phase 2 supersession chain — not reducible to deprecated without successor pointer |
| **split_source** | **Entity facet** | Phase 3 split lineage — distinct from merge |

### 2.3 Candidates rejected as universal states

| Candidate | Rejection |
|-----------|-----------|
| **SAFE UNKNOWN** | Not a record state — explicit **absence** of active canonical at subject/slot |
| **merged_into** | Legacy alias — normative code is **merged** (crosswalk preserves `merged_into` as synonym) |
| **replaced** on entities | Supersession of **links**, not orgs — use **merged** for entities |
| **inactive** | Ambiguous — use **deprecated** or **archived** |
| **deleted** | Forbidden for canonical — tombstone via deprecated/merged/archived |
| **closed** (project) | Operational — map to **deprecated** |
| **former_*** | Relationship **type** prefix, not lifecycle state ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](ATLAS-RELATIONSHIP-TAXONOMY-v1.md)) |

### 2.4 Normative code convention

| Form | Usage |
|------|-------|
| **Registry code** | lowercase snake: `proposed`, `active`, … |
| **Documentation heading** | Title Case for readability |
| **Forbidden** | Consumer-specific synonyms as ATLAS codes |

---

## 3. Universal core state registry

### 3.1 `proposed`

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Candidate reality claim awaiting human attestation; visible for intake review |
| **Canonical?** | **Never** |
| **Applies to** | All entity records; all relationship records |
| **Entry conditions** | Human or consumer creates candidate record; import without promotion; duplicate check pending |
| **Exit conditions** | Attest → **active**; reject → delete proposal (non-attested only) or **archived** stub; escalate → **disputed** |
| **Allowed transitions** | → `active`, `disputed`, `archived` (reject path), (delete if never attested) |
| **Forbidden transitions** | → `deprecated`, `merged`, `replaced` (skip attestation path) |

### 3.2 `active`

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Human-attested canonical claim; authoritative for structural truth now (subject to effective dates on relationships) |
| **Canonical?** | **Yes** (when C-01–C-06 satisfied — [ATLAS-REGISTRY-ARCHITECTURE-v1.md](ATLAS-REGISTRY-ARCHITECTURE-v1.md)) |
| **Entry conditions** | Attestation from **proposed**; or direct attested create; dispute resolution affirming this record |
| **Exit conditions** | End of structural truth; dispute; merge absorption (loser); supersession (relationship); split (source); explicit deprecate |
| **Allowed transitions** | → `disputed`, `deprecated`, `merged`, `split_source`, `replaced` (relationship only, via supersession), `archived` (direct only with policy — normally via deprecated/replaced) |
| **Forbidden transitions** | → `proposed` (demotion forbidden); → `active` (self-loop not a transition event) |

### 3.3 `disputed`

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Competing or insufficiently evidenced claims; blocks canonical use of this record and/or slot |
| **Canonical?** | **Never** |
| **Entry conditions** | Human flag; conflicting imports; duplicate canonical risk; consumer ≠ ATLAS conflict on structure |
| **Exit conditions** | Resolution → one **active** (+ losers **merged**/**replaced**/**deprecated**); or **SAFE UNKNOWN**; reject proposals |
| **Allowed transitions** | → `active`, `deprecated`, `merged`, `replaced`, `archived`, (delete **proposed** competitors) |
| **Forbidden transitions** | → `proposed` (re-open intake uses governance note, not state demotion); parallel **active** on same record |

### 3.4 `deprecated`

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Structural claim ended or downgraded; retained for audit and historical queries; not default forward truth |
| **Canonical?** | **Yes as historical fact**; **No** for forward default joins |
| **Entry conditions** | **active** ended without merge absorption; wrong promotion corrected after successor exists; relationship `effective_to` set |
| **Exit conditions** | → **archived** after cooling period; remain deprecated indefinitely; rare **active** reactivation (governance) |
| **Allowed transitions** | → `archived`; → `active` (reactivation — rare, attested); relationship may also → `replaced` before or instead of deprecated |
| **Forbidden transitions** | → `proposed`; → `merged` without merge governance (use merge workflow) |

### 3.5 `archived`

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Long-term read-only storage; operator noise reduced; audit preserved |
| **Canonical?** | **No** forward; **Yes** read-only historical |
| **Entry conditions** | **deprecated** or **replaced** aged out; rejected **proposed** stub; policy-driven archive |
| **Exit conditions** | **Terminal** — only owner error-correction → **deprecated** then possible **active** |
| **Allowed transitions** | → `deprecated` (error correction only, owner) |
| **Forbidden transitions** | → `active` (direct); → `proposed`; structural edits while archived |

---

## 4. Facet state registry

### 4.1 `merged` (entity / identity records)

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Record id absorbed into survivor; permanent redirect; not deleted |
| **Canonical?** | **No** — consumers must resolve `redirect_to` survivor |
| **Applies to** | Organization, Person, Project, Website, Domain — **not** Relationship |
| **Entry conditions** | Approved merge ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md)); loser id frozen |
| **Exit conditions** | **Terminal** for absorbed id |
| **Allowed transitions** | None (except governance error correction → **deprecated** with audit — extremely rare) |
| **Forbidden transitions** | → `active` (absorbed id); → `proposed` |

**Synonym (read-only legacy):** `merged_into` in Phase 3 text maps to **`merged`** + `redirect_to`.

### 4.2 `split_source` (entity records)

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Former canonical id that was source of an approved split; children documented |
| **Canonical?** | **No** |
| **Applies to** | Entity records only; owner-approved split |
| **Entry conditions** | Split approved ([ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) IGV-S01) |
| **Exit conditions** | **Terminal** |
| **Allowed transitions** | Error correction only (owner) |
| **Forbidden transitions** | → `active` |

**Synonym (crosswalk):** Phase 3 `split_from` → **`split_source`**.

### 4.3 `replaced` (relationship records)

| Attribute | Specification |
|-----------|---------------|
| **Meaning** | Relationship superseded by successor `relationship_id`; chain preserved |
| **Canonical?** | **No** forward; **Yes** historical |
| **Applies to** | Relationship records only |
| **Entry conditions** | Supersession per [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) §6 |
| **Exit conditions** | → **archived**; remain **replaced** indefinitely |
| **Allowed transitions** | → `archived` |
| **Forbidden transitions** | → `active`; → `merged` |

**Required field:** `replaced_by` → successor id.

---

## 5. State applicability matrix

| State | Org | Person | Project | Website | Domain | Relationship |
|-------|-----|--------|---------|---------|--------|--------------|
| proposed | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| active | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| disputed | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| deprecated | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| archived | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| merged | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| split_source | ✓ | ✓ | ✓ | ✓ | ✓ | — |
| replaced | — | — | — | — | — | ✓ |

---

## 6. Canonical posture summary

| State | Forward canonical? | Historical? | Requires redirect/successor |
|-------|-------------------|-------------|----------------------------|
| proposed | No | No | — |
| active | Yes | Current | — |
| disputed | No | No | — |
| deprecated | No | Yes | Optional successor link |
| merged | No | Yes | **redirect_to** required |
| split_source | No | Yes | **split_children** refs required |
| replaced | No | Yes | **replaced_by** required |
| archived | No | Yes (read-only) | Prior redirect/successor retained |

---

## 7. SAFE UNKNOWN (non-state)

| Attribute | Specification |
|-----------|---------------|
| **Type** | Explicit registry **posture** at subject or relationship **slot** |
| **Meaning** | No **active** canonical record is attested for this business fact |
| **Not equivalent to** | `proposed` (may have zero rows), `archived`, or placeholder entity |
| **Consumer rule** | Do not invent ids; do not treat consumer cache as canonical |

---

## 8. Forbidden states registry

| Forbidden code | Reason |
|----------------|--------|
| `todo`, `in_progress`, `waiting`, `done` | Work workflow |
| `lead`, `opportunity`, `won`, `lost` | CRM pipeline |
| `closed`, `completed` | Ambiguous ops — use **deprecated** |
| `deleted`, `purged` | Canonical erase forbidden |
| `unknown` as record state | Use SAFE UNKNOWN posture, not a row pretending to exist |
| `inactive` | Use **deprecated** or **archived** |

---

## 9. Transition index (detail)

Full transition rules, attestation requirements, and forbidden edges: [ATLAS-LIFECYCLE-TRANSITIONS-v1.md](ATLAS-LIFECYCLE-TRANSITIONS-v1.md).

### 9.1 Quick reference — allowed edges (core)

```text
proposed ──attest──► active
proposed ──reject──► archived | (delete)
proposed ──flag────► disputed

active ──dispute──► disputed
active ──end──────► deprecated
active ──merge────► merged          [entities]
active ──split────► split_source    [entities]
active ──supersede► replaced        [relationships → successor active]

disputed ──resolve► active | deprecated | merged | replaced | SAFE UNKNOWN

deprecated ──age──► archived
deprecated ──rare──► active         [reactivation, attested]

replaced ──age────► archived
merged ──(terminal)► (error path only)
archived ──error──► deprecated      [owner only]
```

---

## 10. Compliance checklist

- [ ] Code is from §3–§4 registry only?
- [ ] Facet state used only on correct object kind?
- [ ] merged / replaced have redirect/successor fields?
- [ ] No operational vocabulary smuggled as state?

---

*ATLAS Lifecycle State Registry v1 — normative vocabulary. Documentation only.*
