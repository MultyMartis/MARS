# ATLAS Consumer Mapping Rules v1

**Status:** **documented** — Phase 6 normative mapping between consumer-local states and ATLAS (normative).  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-04  
**Parent:** [ATLAS-CONSUMER-ADOPTION-MODEL-v1.md](ATLAS-CONSUMER-ADOPTION-MODEL-v1.md) · [ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md](ATLAS-CONSUMER-SEMANTIC-CONTRACT-v1.md)  
**Related:** [ATLAS-LIFECYCLE-CROSSWALK-v1.md](ATLAS-LIFECYCLE-CROSSWALK-v1.md) · [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md)  
**Is not:** ETL specification, sync protocol, field-level API mapping, CRM integration design.

**Phase 1–5 constraint:** No changes to approved Phase 1–5 documents unless contradictions are discovered. None identified at Phase 6 authoring.

---

## 1. Purpose

Define **how consumer-local states may map to ATLAS** without overwriting ATLAS lifecycle or forking semantics.

**Core invariant:**

> **ATLAS lifecycle must not be overwritten by consumer lifecycle.**

Example (normative):

> Consumer **“Project completed”** ≠ ATLAS **`deprecated`** without attested structural end.

---

## 2. Mapping philosophy

### 2.1 Two layers, one direction of authority

```text
┌─────────────────────────────┐     read / propose      ┌─────────────────────────────┐
│  Consumer operational layer │ ◄────────────────────── │  ATLAS canonical layer      │
│  (work truth)               │                         │  (structural truth)         │
│  CRM · PM · SEO · CMS · …   │ ──mapping table only──► │  lifecycle · relationships  │
└─────────────────────────────┘   never reverse-write └─────────────────────────────┘
```

| Direction | Allowed | Forbidden |
|-----------|---------|-----------|
| ATLAS → consumer display | Yes (labels) | — |
| Consumer → ATLAS code in canonical store | **Only via attest/propose** | Direct overwrite |
| Consumer ops → ATLAS lifecycle inference | **Documented suggest only** | Auto-sync |

### 2.2 Mapping tables are consumer-owned artifacts

Each consumer **must** maintain a **published mapping document** (charter appendix or `consumer-atlas-mapping.md`) containing:

| Column | Description |
|--------|-------------|
| `consumer_status` | Local code or label |
| `consumer_domain` | CRM · PM · SEO · CMS · etc. |
| `atlas_lifecycle` | Target ATLAS code or **NONE** |
| `mapping_type` | See §4 |
| `attestation_required` | Yes / No |
| `notes` | Risk, UNKNOWN handling |

---

## 3. Operational lifecycle (consumer-owned)

Consumers **may** define arbitrary operational state machines:

| Domain | Example local states | Owned by |
|--------|---------------------|----------|
| CRM | lead · qualified · negotiation · won · lost | CRM / commercial consumer |
| Project management | planning · in_progress · blocked · completed | PM tool / program |
| SEO workflow | intake · research · draft · review · published | MIG / content programs |
| Document workflow | draft · legal_review · signed · filed | Secretary / contract (future) |
| CMS / deploy | build · staging · production · rollback | WPilot / CI |
| Market capture | captured · validated · packaged | MIG evidence |

**Rule MAP-01:** Operational states live **only** in consumer stores.

**Rule MAP-02:** Operational transitions **never** emit ATLAS lifecycle transitions without human attest path.

---

## 4. Mapping types

| Type | Code | Definition | ATLAS impact |
|------|------|------------|--------------|
| **Display-only** | `M-DISP` | UI label for ATLAS code | None |
| **Suggest trigger** | `M-SUGG` | Local event **may** trigger proposal intake | Creates/updates **proposed** only |
| **No mapping** | `M-NONE` | Local state has no ATLAS equivalent | NONE — do not infer |
| **Forbidden** | `M-BAN` | Local state must never map to ATLAS | Governance violation if attempted |

**Rule MAP-03:** Default for ambiguous ops states is **M-NONE**, not guess **deprecated**.

---

## 5. Allowed mappings

### 5.1 ATLAS lifecycle → consumer display (always allowed)

Per [ATLAS-LIFECYCLE-CROSSWALK-v1.md](ATLAS-LIFECYCLE-CROSSWALK-v1.md) §9 — display synonyms only.

### 5.2 Consumer → ATLAS (allowed with constraints)

| Pattern | Allowed when | Result in ATLAS |
|---------|--------------|-----------------|
| Import discovered org | Steward intake | **proposed** entity |
| Operator confirms structural end | Attest after review | **deprecated** (or **merged** / **replaced**) |
| Duplicate detected | Governance merge | **merged** + redirect |
| Relationship correction | Supersession workflow | **replaced** + successor |
| “No canonical org yet” | — | **SAFE UNKNOWN** (no row) |

### 5.3 Illustrative mapping examples (non-exhaustive)

#### CRM status → ATLAS

| CRM `consumer_status` | `mapping_type` | `atlas_lifecycle` | Notes |
|-----------------------|----------------|-------------------|-------|
| lead | M-NONE | NONE | Pipeline ≠ existence |
| active_account | M-DISP | (read **active** org) | Display only if org canonical |
| churned | M-SUGG | (suggest **deprecated** CLIENT_OF) | Requires attest |
| duplicate_record | M-SUGG | (suggest merge proposal) | Not auto-merge |

#### Project status → ATLAS

| PM `consumer_status` | `mapping_type` | `atlas_lifecycle` | Notes |
|----------------------|----------------|-------------------|-------|
| planning | M-NONE | NONE | Ops planning |
| in_progress | M-NONE | NONE | **≠** ATLAS **active** |
| completed | M-NONE | NONE | **≠** ATLAS **deprecated** |
| cancelled | M-SUGG | suggest end Project/relationships | Attest required |

**Normative exemplar (mission brief):**

| Consumer phrase | ATLAS |
|-----------------|-------|
| Project completed | **No automatic mapping** |
| Client left | Suggest **deprecated** on **CLIENT_OF** |
| Site decommissioned | Suggest **deprecated** on **WEB-*** + relationships |

#### SEO workflow → ATLAS (MIG / ORCA)

| SEO `consumer_status` | `mapping_type` | ATLAS |
|-----------------------|----------------|-------|
| serp_captured | M-NONE | NONE — evidence stays MIG |
| competitor_found | M-SUGG | **proposed** org/website |
| pilot_closed | M-NONE | NONE for ATLAS lifecycle |
| report_delivered | M-NONE | NONE |

#### Document workflow → ATLAS (future Secretary)

| Doc `consumer_status` | `mapping_type` | ATLAS |
|-----------------------|----------------|-------|
| draft | M-NONE | NONE |
| signed | M-NONE | NONE — signature ≠ structural attest |
| wrong_party_detected | M-SUGG | proposal / dispute flag | |

---

## 6. Forbidden mappings

| Forbidden pattern | Rule ID | Why |
|-------------------|---------|-----|
| `done` / `completed` → **deprecated** auto | MAP-B01 | Work completion ≠ structural end |
| `live` / `published` → **active** auto | MAP-B02 | Ops go-live ≠ canonical existence |
| `deleted` → purge ATLAS row | MAP-B03 | Tombstone via lifecycle only |
| CRM `won` → create **CLIENT_OF** without attest | MAP-B04 | Commercial fact needs relationship attest |
| `inactive` → **archived** auto | MAP-B05 | Use explicit ATLAS transition |
| Consumer cache stale → overwrite ATLAS | MAP-B06 | ATLAS wins on conflict |
| Business Scope tag → partition entities | MAP-B07 | Scope is classification only |
| SEO competitor → **active** org | MAP-B08 | Market ≠ business attest |

**Rule MAP-B09:** No consumer status from [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) §8 forbidden list may be stored as ATLAS code.

---

## 7. Relationship and identity mapping

### 7.1 CRM role → relationship type

| CRM field | Mapping | ATLAS type |
|-----------|---------|------------|
| Account Owner (user) | M-BAN if auto **OWNER** | Requires attest **OWNER** |
| Primary Contact | M-SUGG **REPRESENTATIVE** or local only | Case-by-case |
| Customer of Vendor | M-SUGG **CLIENT_OF** | Direction Org → Org |

**Rule MAP-R01:** CRM cardinality does not create duplicate canonical **CLIENT_OF** without slot rules ([ATLAS-REALITY-MODEL-v1.md](ATLAS-REALITY-MODEL-v1.md) CR-04).

### 7.2 Local foreign keys

| Pattern | Allowed |
|---------|---------|
| `atlas_org_id` nullable + `local_org_label` | Yes when UNKNOWN |
| `atlas_org_id` required for publish | Yes when consumer policy requires canonical |
| `atlas_org_id` invented UUID | **Forbidden** — use proposals |

---

## 8. Multi-consumer consistency

When two consumers map the same local concept differently:

1. **ATLAS code is authoritative** — align mapping tables to ATLAS, not to each other’s ops vocabulary.
2. Discrepancy in **interpretation** → Semantic Contract violation → governance.
3. Discrepancy in **ops labels** → acceptable if both map tables are correct.

---

## 9. Mapping governance

| Event | Action |
|-------|--------|
| New consumer ops state | Add row to mapping table; default M-NONE |
| ATLAS lifecycle amendment | Review all M-SUGG rows |
| Certification C2+ | Mapping table published and reviewed |

Escalation: [ATLAS-CONSUMER-GOVERNANCE-v1.md](ATLAS-CONSUMER-GOVERNANCE-v1.md).

---

## 10. Compliance checklist

- [ ] Mapping table exists and is versioned?
- [ ] No MAP-B01–B09 violations in automation rules?
- [ ] **completed** / **done** rows are M-NONE or M-SUGG only?
- [ ] ATLAS-shaped fields contain only Phase 5 codes?
- [ ] Business Scope not used as mapping key for lifecycle?

---

*ATLAS Consumer Mapping Rules v1 — Phase 6 Foundation. Documentation only.*
