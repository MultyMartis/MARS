# ATLAS Identifier Model v1

**Status:** **documented** — Phase 3 canonical identifier strategy (principles only).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md)  
**Is not:** database schema, auto-increment sequence design, UUID policy implementation, API path design, file naming convention for repo folders, checksum algorithm.

---

## 1. Purpose

Define **how** ATLAS assigns and governs **opaque stable identifiers** for each MVP entity type — so Phase 1 entities and Phase 2 relationships can be referenced uniformly across MARS **before** any registry storage or API exists.

**Scope boundary:** Principles and exemplar **shapes** only. No sequences, no tables, no generators.

---

## 2. Identifier philosophy

### 2.1 Opaque and dumb

Identifiers carry **no business meaning** in the string. They do not encode:

- legal form (`OOO`, `LLC`)
- country
- tax id
- domain name
- person surname
- relationship type

**Rationale:** Meaning in ids causes **reuse temptation**, **merge errors**, and **breaking changes** when attributes change.

### 2.2 Human-legible prefixes

Prefixes aid **manual review** in spreadsheets and logs. They are **not** a type system for parsers in Phase 3 — consumers must treat the full string as atomic.

| Prefix | Entity type |
|--------|-------------|
| `ORG-` | Organization |
| `PER-` | Person |
| `PRJ-` | Project |
| `WEB-` | Website |
| `DOM-` | Domain |
| `REL-` | Relationship |

**Exemplar shapes (illustrative, not allocated):**

```text
ORG-0001   PER-0001   PRJ-0001   WEB-0001   DOM-0001   REL-0001
```

Numeric suffix width and padding are **implementation choices** deferred. Phase 3 requires only: **fixed prefix per type** + **opaque suffix**.

### 2.3 One id per entity record

| Rule | Detail |
|------|--------|
| **IDN-01** | Each canonical entity record has exactly one primary id |
| **IDN-02** | Ids are not composite of names or endpoints |
| **IDN-03** | Relationship id is independent of subject/object ids |
| **IDN-04** | Alias strings never substitute for id in normative contracts |

---

## 3. Canonical identifier strategy by type

### 3.1 Organization (`ORG-`)

| Aspect | Principle |
|--------|-----------|
| **Assign** | On first **active** attestation of business unit |
| **Stability** | Survives rename, alias add, jurisdiction field add |
| **Survivor** | Merge: non-survivor `ORG-*` → `merged_into` redirect |
| **Not used for** | CRM account id, ERP company code (optional external ref) |

### 3.2 Person (`PER-`)

| Aspect | Principle |
|--------|-----------|
| **Assign** | On first **active** attestation of natural person |
| **Stability** | Survives org changes, role changes (via relationships) |
| **Survivor** | Merge only when attested same human (rare; high evidence) |
| **Not used for** | Email login, WP user id, Telegram handle as primary key |

### 3.3 Project (`PRJ-`)

| Aspect | Principle |
|--------|-----------|
| **Assign** | On first **active** attestation of initiative identity |
| **Stability** | Survives display rename; initiative end → deprecate, not reuse id |
| **Distinction** | MARS program `project_id` (`atlas`, `orca`) is separate namespace |
| **Not used for** | CRM opportunity id, Jira project key as ATLAS id |

### 3.4 Website (`WEB-`)

| Aspect | Principle |
|--------|-----------|
| **Assign** | On first **active** attestation of web property identity |
| **Stability** | Survives rebrand; domain changes via relationships |
| **Not used for** | Deploy id, build number, staging hostname as primary id |

### 3.5 Domain (`DOM-`)

| Aspect | Principle |
|--------|-----------|
| **Assign** | On first **active** attestation of hostname identity |
| **Policy** | Apex vs `www` as separate `DOM-*` or alias — **human attested** per intake charter |
| **Stability** | Id does not change when DNS registrar changes |
| **Not used for** | DNS record content hash, SSL cert serial |

### 3.6 Relationship (`REL-`)

| Aspect | Principle |
|--------|-----------|
| **Assign** | On creation of relationship record (proposed or active) |
| **Stability** | Id preserved through type correction via **supersession** (Phase 2), not id reuse |
| **Slot** | Duplicate detection uses type + endpoints + dates — not id string semantics |
| **Alignment** | Phase 2 RI-01–RI-04 unchanged |

---

## 4. Stability

| Principle | Normative rule |
|-----------|----------------|
| **Permanent reference** | Once published to consumers as canonical, id remains valid pointer for audit |
| **Attribute drift** | Name, alias, optional metadata may change; id does not |
| **Consumer contract** | Durable references use `ORG-*` etc.; versioned APIs may wrap, not replace |
| **Breaking change** | Changing an id is **forbidden**; merge uses redirect |
| **Fork prevention** | Re-import must map to existing id via stewardship — not mint second id |

---

## 5. Permanence

**Permanence** means the identifier **always refers to the same registry row lineage**, even when:

- entity is **deprecated**
- entity is **merged_into** survivor
- entity is **archived**

| Event | Id behavior |
|-------|-------------|
| Rename | Same id |
| Add alias | Same id |
| Deprecate | Same id; state flag |
| Merge (absorbed) | Absorbed id permanent; points to survivor |
| Split (source) | Source id permanent; deprecated; children get new ids |
| Archive | Same id; read-only |

---

## 6. Non-reuse

| Rule | Detail |
|------|--------|
| **IDN-NR01** | Retired ids are **never** assigned to a new business subject |
| **IDN-NR02** | Gap in numeric sequence is **acceptable** — do not backfill |
| **IDN-NR03** | Test / sandbox ids (if ever used) must not collide with production namespace policy (implementation) |
| **IDN-NR04** | Merge survivor retains id; absorbed ids frozen |

**Rationale:** Reuse destroys audit trails and causes silent wrong joins in consumer caches.

---

## 7. Retirement rules

### 7.1 Deprecation (entity still distinct)

| Trigger | Id state |
|---------|----------|
| Business unit dissolved but history needed | `deprecated` → `archived` |
| Website decommissioned | `deprecated`; relationships ended per Phase 2 |
| Project closed | `deprecated`; not deleted |

Consumers must stop **forward** canonical use; historical reads allowed.

### 7.2 Merge retirement (absorbed id)

| Field (conceptual) | Value |
|--------------------|-------|
| `identity_state` | `merged_into` |
| `redirect_to` | Survivor `ORG-*` (etc.) |
| `merged_at` | Attestation timestamp |
| `evidence_ref` | Governance tier |

Absorbed id **never** returns to `active`.

### 7.3 Relationship retirement

Follow [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](ATLAS-RELATIONSHIP-LIFECYCLE-v1.md): `deprecated`, `replaced`, `archived` — **REL-*** id not reused.

### 7.4 When retirement is forbidden as substitute for merge

| Wrong pattern | Correct pattern |
|---------------|-----------------|
| Deprecate duplicate org without merge redirect | Merge with survivor + alias union |
| Delete id from registry | Archive + redirect |
| Mint new id because name changed | Update canonical name / alias |

---

## 8. External and consumer identifiers

| Kind | Role in ATLAS |
|------|----------------|
| **ATLAS canonical id** | Primary business reality reference |
| **Consumer foreign key** | Optional `external_ref` metadata (future); maps **to** ATLAS id |
| **MARS program id** | `registry/project-registry.md` — not ATLAS entity id |
| **Tax id / VAT** | Optional attested attribute; **not** primary id (ERP remains SoR for tax) |
| **Domain name string** | Label on `DOM-*` record, not substitute id |

**Rule IDN-EXT01:** Import pipelines propose **mapping**; stewards attest. No auto-canonical from foreign key alone.

---

## 9. Uniqueness within namespace

| Scope | Rule |
|-------|------|
| **Within type** | Each `ORG-*` unique among organizations |
| **Across types** | `ORG-0001` and `PER-0001` may share numeric suffix — prefixes disambiguate |
| **Global** | Full string `ORG-0001` unique across registry |

Collision on mint is **implementation error** — governance does not define technical dedup algorithms.

---

## 10. Relationship to aliases

| Identifier | Alias |
|------------|-------|
| `ORG-0042` | Polygon, Полигон, WSP |
| Stable | Mutable set |
| Required in contracts | Convenience in UI only |

See [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md).

---

## 11. Prohibitions

| # | Prohibition |
|---|-------------|
| **IDN-X01** | Semantic ids (`org-polygon`, `web-triumf-krasnodar`) as normative standard |
| **IDN-X02** | Reusing `ORG-0007` after merge for new org |
| **IDN-X03** | Encoding tax id in id string |
| **IDN-X04** | Relationship id derived only from hash of endpoints (opaque id required) |
| **IDN-X05** | Business Scope string as entity id prefix |

---

## 12. Deferred to Registry Architecture Foundation

The following are **explicitly out of scope** for this document:

- Sequence generators, UUID v7, database sequences
- Id minting API, bulk import id assignment
- Physical storage of redirect table
- Cross-region replication of id namespace
- Check digit / validation regex in SDK

---

## 13. Exemplar reference table (illustrative only)

| Business subject (narrative) | Exemplar id | Notes |
|------------------------------|-------------|-------|
| Polygon company | `ORG-0001` | Aliases: Полигон, WSP |
| Andrey (person) | `PER-0001` | Multi-org via `REL-*` |
| грузотакси pilot | `PRJ-0001` | Links to client org via relationships |
| Brand site | `WEB-0001` | |
| `polygon.ru` | `DOM-0001` | |
| Andrey OWNER Polygon | `REL-0001` | Slot: OWNER, PER-0001 → ORG-0001 |

Numbers are **not allocated** by Phase 3 documentation.

---

## 14. Related documents

| Document | Role |
|----------|------|
| [ATLAS-IDENTITY-MODEL-v1.md](ATLAS-IDENTITY-MODEL-v1.md) | Sameness, lifecycle, philosophy |
| [ATLAS-ALIAS-MODEL-v1.md](ATLAS-ALIAS-MODEL-v1.md) | Names vs ids |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](ATLAS-IDENTITY-GOVERNANCE-v1.md) | Merge redirect policy |
| [ATLAS-RELATIONSHIP-MODEL-v1.md](ATLAS-RELATIONSHIP-MODEL-v1.md) | `REL-*` slot rules |
