# ATLAS Wave 6A Commercial Relationship Population v1

**Status:** **documented** — first canonical Organization ↔ Organization commercial relationship population plan.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx)  
**Is not:** runtime, API, database schema, relationship attestation act, Wave 6B execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Wave 4B Website Relationships: **COMPLETE**
- Wave 5 Domain Population: **COMPLETE**
- Wave 5B Domain Relationships: **COMPLETE**
- Population verdict: **READY FOR WAVE 6A COMMERCIAL RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** первого набора **Organization ↔ Organization** commercial relationships для Wave 6A: состав рёбер, типы, evidence basis, lifecycle intent, deferred items, границы foundation.

**Normative scope Wave 6A:**

```text
Organization ↔ Organization commercial relationships only
Type: CLIENT_OF only (approved operator list)
Endpoints: ORG-0001 Polygon, ORG-0004 Triumph only
No VENDOR_OF, PARTNER_OF, SUPPLIER_OF
No Person, Project, Website, or Domain relationships
No new entity types
No new relationship families
```

**Binding operator business reality (carried from Wave 1–5 deferrals):**

- Triumph (**ORG-0004**) **purchases services from** Polygon (**ORG-0001**).
- Canonical edge: **ORG-0004 ──CLIENT_OF──► ORG-0001** (REL-0016).
- Dataset draft note: «Клиент Полигона» — direction preserved.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **1** |
| Organization endpoints (active) | **2** (ORG-0001, ORG-0004) |
| Relationship family used | Organization → Organization only |
| Relationship types used | **CLIENT_OF** only |

### 2.1 Summary table

| relationship_id | source_organization | target_organization | relationship_type | commercial role | attestation readiness |
|-----------------|---------------------|---------------------|-------------------|-----------------|-----------------------|
| REL-0016 | ORG-0004 ООО «Триумф» | ORG-0001 Веб-студия «Полигон» | **CLIENT_OF** | Triumph = client; Polygon = vendor | **ready** |

---

## 3. Per-relationship analysis — REL-0016

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0016 |
| **source_organization** | ORG-0004 ООО «Триумф» |
| **target_organization** | ORG-0001 Веб-студия «Полигон» |
| **relationship_type** | **CLIENT_OF** |
| **attestation_basis** | E1 dataset Relationships sheet (draft REL-0016); operator-confirmed commercial reality (Triumph purchases services from Polygon); E1 corroboration Wave 3B project graph (PRJ-0004..0008 **COMMISSIONED_BY** ORG-0004, **EXECUTES** ORG-0001); EV-0005 Triumph CC; EV-0003 Polygon CC (LE-0001); ORG-0001 **active** (Wave 1 W1-A); ORG-0004 **active** (Wave 1 W1-B) |
| **evidence_tier** | **E1** (primary); E0 operator-direct corroboration |
| **lifecycle_state** | **active** (target upon attestation) |
| **slot** | CLIENT_OF, ORG-0004 → ORG-0001 |
| **notes** | First attested org↔org commercial edge; structural link — not contract value or deal stage |

---

## 4. Required analysis

### 4.1 Commercial reality validation

| Check | Result | Basis |
|-------|--------|-------|
| Triumph is a **client organization** of operator delivery stack | **Pass** | Wave 1 W1-B active client; [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) §2.1 |
| Polygon is **delivery / vendor org** for Triumph initiatives | **Pass** | Wave 3B EXECUTES on PRJ-0004..0008; Wave 3 project register |
| Active commercial delivery in flight | **Pass** | PRJ-0005..0008 **active**; PRJ-0004 **deprecated** (completed) |
| OPS «Client Триумф» maps to Organization + CLIENT_OF | **Pass** | [OPS-ATLAS-ALIGNMENT-v1.md](../foundation/OPS-ATLAS-ALIGNMENT-v1.md) §4.2 |
| CC alone auto-creates CLIENT_OF | **Rejected path** | [ATLAS-COUNTERPARTY-CARD-MODEL-v1.md](../foundation/ATLAS-COUNTERPARTY-CARD-MODEL-v1.md) CC-EDO-01 — multi-source E1 used |
| Contract / invoice as primary evidence | **Not used** | OAR-BAN-01 — structural E1 sufficient for Wave 6A |

**Verdict:** Commercial reality **validated** for REL-0016 at org↔org structural level.

### 4.2 Evidence review

| Ref | Artifact | Role for REL-0016 |
|-----|----------|-------------------|
| Dataset draft | `ATLAS-WAVE1-DATASET-v0.4.xlsx` Relationships — REL-0016 | Primary E1 draft; type CLIENT_OF; endpoints ORG-0004 → ORG-0001 |
| EV-0005 | `triumph/…2024.xlsx` (external CC) | Client org endpoint corroboration (Wave 1) |
| EV-0003 | `polygon/ИП Русецкий А. А.pdf` (external CC, LE-0001) | Vendor org endpoint corroboration (Wave 1) |
| Wave 3B register | REL-0017..0026 COMMISSIONED_BY / EXECUTES pairs | Independent E1 structural corroboration of client/vendor roles |
| Operator intake | Wave 6A approved business reality | E0 overlay — Triumph purchases services from Polygon |
| **Excluded** | Contracts, acts, invoices | OPS domain — not ATLAS CC primary path |

**Minimum tier:** E1 for CLIENT_OF per [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.6 — **met**.

### 4.3 Lifecycle validation

| Rule | Check | Result |
|------|-------|--------|
| LC-P02 | Both endpoints **active** before **active** edge | **Pass** — ORG-0001, ORG-0004 attested Wave 1 |
| Target state | **active** post steward attestation | **ready** |
| FORMER_CLIENT_OF | Not applicable — relationship ongoing | — |
| disputed | No conflicting canonical slot | **Pass** |
| effective_from / effective_to | Not attested at Wave 6A | **SAFE UNKNOWN** — see §6 |

### 4.4 Ownership neutrality

| Concern | Treatment |
|---------|-----------|
| PER-0001 **OWNER** ORG-0001 | Person ownership **does not** substitute for org↔org CLIENT_OF; edge is org-level only |
| PER-0004..0006 Triumph staff edges | Person → Organization participation **independent** of commercial org link |
| ORG-0004 **OWNS** WEB-0006..0009 (Wave 4B) | Client **property ownership** — does not reverse vendor direction |
| ORG-0001 **EXECUTES** Triumph projects (Wave 3B) | Delivery participation **corroborates** vendor role — does not replace CLIENT_OF |
| Infer CLIENT_OF from CRM «account owner» | **Forbidden** — [ATLAS-ROLE-MODEL-v1.md](../foundation/ATLAS-ROLE-MODEL-v1.md) |
| Mint **VENDOR_OF** mirror edge | **Not created** — operator scope; CLIENT_OF canonical slot sufficient |

**Verdict:** Ownership and operational roles **neutralized** — REL-0016 stands alone as attested commercial structure.

### 4.5 Relationship direction validation

```text
Business fact:  Triumph purchases services from Polygon
Taxonomy rule:  Subject (client) ──CLIENT_OF──► Object (vendor)
Canonical edge: ORG-0004 Триумф ──CLIENT_OF──► ORG-0001 Полигон   ✓
```

| Direction candidate | Verdict | Reason |
|---------------------|---------|--------|
| ORG-0004 → CLIENT_OF → ORG-0001 | **Approved** | Subject = client (Triumph); object = vendor (Polygon) — [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §2 |
| ORG-0001 → CLIENT_OF → ORG-0004 | **Rejected** | Would assert Polygon is client of Triumph — contradicts business reality |
| ORG-0001 → VENDOR_OF → ORG-0004 | **Not created** | Out of Wave 6A scope; inverse not required when CLIENT_OF attested |
| Dual CLIENT_OF (both directions) | **Rejected** | Taxonomy symmetry note §2 — rare dual role not attested |

**SC-R02 alignment:** CLIENT_OF = subject org is **client** of object org in attested commercial service relationship — **Pass**.

### 4.6 Foundation consistency

| Foundation doc | Wave 6A alignment |
|----------------|-------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) | One directed Org→Org edge; RP-04 single canonical CLIENT_OF slot — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §2 | CLIENT_OF in Organization ↔ Organization family — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target **active** after attestation — **yes** |
| [ATLAS-RELATIONSHIP-GOVERNANCE-v1.md](../foundation/ATLAS-RELATIONSHIP-GOVERNANCE-v1.md) §6.1 | Direction verified before affirm — **yes** |
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) | Organization endpoints only — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship lifecycle `active` — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required — **yes** |
| [ATLAS-POPULATION-PRIORITIES-v1.md](../foundation/ATLAS-POPULATION-PRIORITIES-v1.md) §Wave 6 | Sub-wave **6A** = ORG↔ORG — **yes** |
| [ATLAS-WAVE-1-EXECUTION-v1.md](../foundation/ATLAS-WAVE-1-EXECUTION-v1.md) W1-EXEC-05 | CLIENT_OF deferred from Wave 2B to Wave 6A — **honored** |

**No new entity types.** **No new relationship families.**

---

## 5. Commercial graph discipline — Triumph / Polygon

```text
ORG-0004 Триумф ──CLIENT_OF──► ORG-0001 Полигон     [Wave 6A — REL-0016]

PRJ-0004..0008 ──COMMISSIONED_BY──► ORG-0004         [Wave 3B — attested]
ORG-0001 Полигон ──EXECUTES──► PRJ-0004..0008        [Wave 3B — attested]

ORG-0004 Триумф ──OWNS──► WEB-0006..0009             [Wave 4B — attested]
```

**Layering rule:** CLIENT_OF is **org-level commercial structure**. Project COMMISSIONED_BY / EXECUTES and Website OWNS remain **independent** attested families — not substitutes for REL-0016.

---

## 6. Explicit exclusions and deferred commercial relationships

| Item | Treatment | Target |
|------|-----------|--------|
| ORG-0001 → **VENDOR_OF** → ORG-0004 | **Do not create** | Out of Wave 6A scope; CLIENT_OF canonical |
| ORG-0001 / ORG-0004 **PARTNER_OF** | **Do not create** | No attested peer partnership |
| **SUPPLIER_OF** (any pair) | **Do not create** | Out of scope |
| ORG-0002 MetaCode ↔ any org commercial edge | **Deferred** | No operator-approved 6A candidate |
| ORG-0003 i-SEO ↔ any org commercial edge | **Deferred** | Operational SEO via persons — no org↔org edge |
| W1-C latent historical clients | **Deferred** | Future Organization + 6A extension |
| Moscow SERM / Metallka commercial edges | **Deferred** | Organization endpoints not populated |
| Person / Project / Website / Domain edges | **Out of scope** | Waves 2B–5B / 6B–6D |
| Contract value, SOW, invoice metadata on edge | **Forbidden** | RP-03 / RR-09 |

---

## 7. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) | Canonical commercial relationship roster |
| [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) | Project-level corroboration |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
