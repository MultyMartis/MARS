# ATLAS Wave 5B Domain Relationship Population v1

**Status:** **documented** — first canonical Domain-family relationship population plan.  
**Program:** ATLAS — Business Reality Registry  
**Date:** 2026-06-06  
**Parent:** [ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md](ATLAS-WAVE5-DOMAIN-ATTESTATION-v1.md) · [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) · [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) · [ATLAS-WAVE1-DATASET-v0.4.xlsx](ATLAS-WAVE1-DATASET-v0.4.xlsx)  
**Is not:** runtime, API, database schema, DNS automation, registrar integration, relationship attestation act, Wave 6 execution.

**Prerequisites (operator-confirmed):**

- Wave 1 Organizations: **COMPLETE**
- Wave 2 Persons: **COMPLETE**
- Wave 2B Person → Organization: **COMPLETE**
- Wave 3 Projects: **COMPLETE**
- Wave 3B Project → Organization: **COMPLETE**
- Wave 4 Website Population: **COMPLETE**
- Wave 4B Website Relationships: **COMPLETE**
- Wave 5 Domain Population: **COMPLETE**
- Population verdict: **READY FOR WAVE 5B DOMAIN RELATIONSHIP POPULATION**

---

## 1. Purpose

Зафиксировать **канонический план population** первого набора **Domain-family** relationships для Wave 5B: состав рёбер PRIMARY_DOMAIN, evidence basis, lifecycle intent, ownership neutrality, deferred items, границы foundation.

**Normative scope Wave 5B:**

```text
Domain → Website PRIMARY_DOMAIN (REL-0036..0039)
Triumph client properties only (DOM-0001..0004 → WEB-0006..0009)
No Organization → Domain OWNS
No Organization → Domain CUSTODIAN
No SECONDARY_DOMAIN (unless evidence — none attested)
No REDIRECTS_TO / POINTS_TO
No DNS relationships
No registrar relationships
No Person ↔ Domain
No new entity types
No new relationship families
No Foundation modifications
```

**Binding operator modeling decision:**

- **PRIMARY_DOMAIN** (Domain → Website) — canonical primary hostname anchor for web property identity; **not** ownership, **not** DNS record content.
- **Website OWNS** (Organization → Website, Wave 4B) — structural business ownership of **web property**; **distinct** from domain registrant / registrar account.
- **Domain OWNS** (Organization → Domain) — **not created** in Wave 5B; registrar evidence absent → **SAFE UNKNOWN** / **proposed only** for future wave.
- **SECONDARY_DOMAIN** — **not created**; `www.gktriumph.ru` lacks steward hostname-policy attestation in current package.

---

## 2. Population summary

| Metric | Count |
|--------|-------|
| Relationships in scope | **4** |
| Domain endpoints (source) | **4** (DOM-0001..0004) |
| Website endpoints (target) | **4** (WEB-0006..0009) |
| Relationship types used | **PRIMARY_DOMAIN** only |
| PRIMARY_DOMAIN per Website | **1** each (singleton slot satisfied) |
| Domain reused across relationships | **0** (one Domain → one Website) |

### 2.1 Summary table

| relationship_id | source_id | target_id | relationship_type | attestation readiness |
|-----------------|-----------|-----------|-------------------|-----------------------|
| REL-0036 | DOM-0001 gktriumph.ru | WEB-0006 gktriumph.ru | **PRIMARY_DOMAIN** | **ready** |
| REL-0037 | DOM-0002 blog.gktriumph.ru | WEB-0007 blog.gktriumph.ru | **PRIMARY_DOMAIN** | **ready** |
| REL-0038 | DOM-0003 gruzotaxi-triumph.ru | WEB-0008 gruzotaxi-triumph.ru | **PRIMARY_DOMAIN** | **ready** |
| REL-0039 | DOM-0004 manipulator-triumph.ru | WEB-0009 manipulator-triumph.ru | **PRIMARY_DOMAIN** | **ready** |

### 2.2 ID continuity note

Wave 4B attestation closed at **REL-0035** (Organization → Website OWNS). Wave 5B mints **REL-0036..0039** for Domain → Website PRIMARY_DOMAIN — first Domain-family relationship ids in the canonical graph.

| Prior wave last rel_id | Wave 5B rel_ids | Family |
|------------------------|-----------------|--------|
| REL-0035 ORG-0004 → WEB-0009 OWNS | REL-0036..0039 | Domain → Website PRIMARY_DOMAIN |

No dataset draft rel_ids exist for Domain-family edges (Domains sheet absent in v0.4).

---

## 3. Per-relationship analysis

### 3.1 DOM-0001 → WEB-0006 — REL-0036

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0036 |
| **source_id** | DOM-0001 gktriumph.ru |
| **target_id** | WEB-0006 gktriumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | E1 operator roster; co-terminous hostname `gktriumph.ru` on attested DOM-0001 **active** (Wave 5) and WEB-0006 **active** (Wave 4); live URL `https://gktriumph.ru`; REL-0032 ORG-0004 **OWNS** WEB-0006 (website-level — not domain registrant); EV-0005 Triumph CC (client context) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Apex corporate hostname; singleton PRIMARY_DOMAIN for WEB-0006; `www.gktriumph.ru` **not** modeled |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Endpoint validation** | DOM-0001 **active**; WEB-0006 **active** — **Pass** |
| **Lifecycle validation** | Live production hostname + active website → **active** edge — **Pass** |
| **Evidence review** | E1 co-terminous identity + live URL + operator roster — **Pass** |
| **Ownership neutrality** | Edge links hostname anchor to property; does **not** assert registrant or ORG→Domain OWNS — **Pass** |
| **Foundation consistency** | Domain→Website PRIMARY_DOMAIN family; ≤1 active per Website — **Pass** |

### 3.2 DOM-0002 → WEB-0007 — REL-0037

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0037 |
| **source_id** | DOM-0002 blog.gktriumph.ru |
| **target_id** | WEB-0007 blog.gktriumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | E1 operator roster; co-terminous FQDN `blog.gktriumph.ru`; DOM-0002 **active**; WEB-0007 **active**; distinct from DOM-0001 / WEB-0006 (EIR-D01, EIR-W01); REL-0033 ORG-0004 **OWNS** WEB-0007; REL-0029 BELONGS_TO PRJ-0007 |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Subdomain FQDN is **separate Domain entity** — primary for blog property only; not collapsed into apex DOM-0001 |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Endpoint validation** | DOM-0002 **active**; WEB-0007 **active** — **Pass** |
| **Lifecycle validation** | Live blog hostname — **Pass** |
| **Evidence review** | E1 FQDN match + live URL — **Pass** |
| **Ownership neutrality** | No DNS zone operator modeled; no domain OWNS — **Pass** |
| **Foundation consistency** | Subdomain = independent PRIMARY_DOMAIN target — **Pass** |

### 3.3 DOM-0003 → WEB-0008 — REL-0038

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0038 |
| **source_id** | DOM-0003 gruzotaxi-triumph.ru |
| **target_id** | WEB-0008 gruzotaxi-triumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | E1 operator roster; co-terminous hostname; DOM-0003 **active**; WEB-0008 **active**; live URL `https://gruzotaxi-triumph.ru`; REL-0034 ORG-0004 **OWNS** WEB-0008; REL-0030 BELONGS_TO PRJ-0005; EV-0005 Triumph CC; MIG pilot prep (identity support — AT-E-03) |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Standalone apex landing domain — not subdomain of `gktriumph.ru` zone |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Endpoint validation** | DOM-0003 **active**; WEB-0008 **active** — **Pass** |
| **Lifecycle validation** | Live landing hostname — **Pass** |
| **Evidence review** | E1 + MIG context (non-registrar) — **Pass** |
| **Ownership neutrality** | Website OWNS attested; Domain OWNS not inferred — **Pass** |
| **Foundation consistency** | One PRIMARY_DOMAIN for WEB-0008 — **Pass** |

### 3.4 DOM-0004 → WEB-0009 — REL-0039

| Field | Value |
|-------|-------|
| **relationship_id** | REL-0039 |
| **source_id** | DOM-0004 manipulator-triumph.ru |
| **target_id** | WEB-0009 manipulator-triumph.ru |
| **relationship_type** | **PRIMARY_DOMAIN** |
| **attestation_basis** | E1 operator roster; co-terminous hostname; DOM-0004 **active**; WEB-0009 **active**; live URL `https://manipulator-triumph.ru`; REL-0035 ORG-0004 **OWNS** WEB-0009; REL-0031 BELONGS_TO PRJ-0008; EV-0005 Triumph CC |
| **evidence_tier** | **E1** |
| **lifecycle_state** | **active** |
| **notes** | Website Factory / ORCA delivery context — MARS program pack ≠ duplicate relationship |

**Required analysis:**

| Review | Finding |
|--------|---------|
| **Endpoint validation** | DOM-0004 **active**; WEB-0009 **active** — **Pass** |
| **Lifecycle validation** | Live landing hostname — **Pass** |
| **Evidence review** | E1 co-terminous identity — **Pass** |
| **Ownership neutrality** | No registrant inference — **Pass** |
| **Foundation consistency** | Singleton slot for WEB-0009 — **Pass** |

---

## 4. Cardinality and graph integrity

```text
DOM-0001 gktriumph.ru           ──PRIMARY_DOMAIN──► WEB-0006 gktriumph.ru
DOM-0002 blog.gktriumph.ru      ──PRIMARY_DOMAIN──► WEB-0007 blog.gktriumph.ru
DOM-0003 gruzotaxi-triumph.ru   ──PRIMARY_DOMAIN──► WEB-0008 gruzotaxi-triumph.ru
DOM-0004 manipulator-triumph.ru ──PRIMARY_DOMAIN──► WEB-0009 manipulator-triumph.ru

(Prior waves — unchanged)
ORG-0004 ──OWNS──► WEB-0006..0009          [Wave 4B — website property]
WEB-0006..0009 ──BELONGS_TO──► PRJ-*       [Wave 4B]
PRJ-* ──COMMISSIONED_BY──► ORG-0004        [Wave 3B]
```

| Check | Result |
|-------|--------|
| One PRIMARY_DOMAIN per Website | **Pass** — 4 websites, 4 edges, 1:1 |
| One Domain source per relationship | **Pass** — each DOM-* used once |
| No duplicate PRIMARY_DOMAIN on same Website | **Pass** |
| No Website → Domain reverse edges | **Pass** — direction Domain → Website per taxonomy §7 |
| Co-terminous hostname strings | **Intentional** — parallel DOM/WEB identities linked by edge only |

---

## 5. Ownership neutrality review

| Topic | Wave 5B posture |
|-------|-----------------|
| Registrar / registrant | **SAFE UNKNOWN** for all four domains — no WHOIS/registrar export in repo |
| ORG-0004 → DOM-* **OWNS** | **Not created** — insufficient domain-level E1; Website OWNS (REL-0032..0035) **does not substitute** |
| PRIMARY_DOMAIN semantics | Hostname-to-property structural link — **not** asset ownership |
| Indirect org candidate (display) | ORG-0004 remains **candidate** on Domain register display fields only — **not promoted** to Domain OWNS |
| ORG-0001 CUSTODIAN / OPERATES | **Not created** — SU-W4B-01, SU-W5-03 carry |
| Infer registrant from client CC | **Rejected** — EV-0005 supports client context for Website graph, not domain registrant |

**Distinction (enforced):**

```text
REL-0032..0035  ORG-0004 ──OWNS──► WEB-*        [attested Wave 4B — web property ownership]
REL-0036..0039  DOM-*    ──PRIMARY_DOMAIN──► WEB-*  [Wave 5B — hostname anchor]
(proposed)      ORG-0004 ──OWNS──► DOM-*        [requires E1 registrar — NOT in 5B]
```

---

## 6. SECONDARY_DOMAIN optional review

| Hostname | Evidence in package | Wave 5B treatment |
|----------|---------------------|-------------------|
| `www.gktriumph.ru` | **Absent** — not in approved roster; no redirect/DNS intent attestation | **Not created** — steward hostname policy deferred (SU-W5-02) |
| IDN / punycode variants | None identified | **N/A** |
| Cross-property aliases | None attested | **Not created** |

**SECONDARY_DOMAIN** requires explicit evidence of alias role ([ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7). No qualifying evidence in current package → **zero** SECONDARY_DOMAIN edges.

---

## 7. Explicit exclusions and deferred relationships

| Item | Treatment | Target |
|------|-----------|--------|
| ORG-0004 → DOM-* **OWNS** | **Proposed only** — evidence gate unmet | Wave 6+ (registrar E1) |
| ORG-0001 **CUSTODIAN** / **OPERATES** Domain | **Do not create** | SAFE UNKNOWN |
| `www.gktriumph.ru` SECONDARY_DOMAIN or new DOM | **Deferred** | Steward policy |
| **REDIRECTS_TO** / **POINTS_TO** | **Do not create** | Out of 5B scope |
| DNS A/CNAME/MX/TXT relationships | **Do not create** | Out of ATLAS scope |
| Registrar billing / expiry edges | **Do not create** | Out of scope |
| REL-0016 ORG-0004 **CLIENT_OF** ORG-0001 | **Deferred** | **Wave 6** |
| Person → Domain / Person → Website | **Do not create** | Future expansion |
| Operator org domains | **Out of scope** | Future tranche |
| WEB-0001..0005 hostname edges | **Out of scope** | Future wave |

---

## 8. Candidate relationships for Wave 6

| Candidate | Type | Endpoints | Prerequisite |
|-----------|------|-----------|--------------|
| REL-0016 | **CLIENT_OF** | ORG-0004 → ORG-0001 | Commercial graph attestation |
| ORG-0004 → DOM-0001..0004 | **OWNS** (domain) | Registrar/registrant E1 | ME-W5-01 / SU-W5-01 |
| `www.gktriumph.ru` | **SECONDARY_DOMAIN** or new DOM-* | → WEB-0006 | Hostname policy attestation |
| ORG-0001 | **OPERATES** Website or Domain | WEB-0006..0009 / DOM-* | Separate governance — SU-W4B-01 |
| Person → Project / Person → Website | Various | — | Future expansion |
| PRJ-0001 MARS internal edges | — | — | Internal governance |

---

## 9. Foundation consistency

| Foundation doc | Wave 5B alignment |
|----------------|-------------------|
| [ATLAS-RELATIONSHIP-MODEL-v1.md](../foundation/ATLAS-RELATIONSHIP-MODEL-v1.md) §4 | PRIMARY_DOMAIN singleton per Website — **yes** |
| [ATLAS-RELATIONSHIP-TAXONOMY-v1.md](../foundation/ATLAS-RELATIONSHIP-TAXONOMY-v1.md) §7 | Domain → Website PRIMARY_DOMAIN — **yes** |
| [ATLAS-RELATIONSHIP-LIFECYCLE-v1.md](../foundation/ATLAS-RELATIONSHIP-LIFECYCLE-v1.md) | Target state **active** after steward attestation — **yes** |
| [ATLAS-IDENTITY-MODEL-v1.md](../foundation/ATLAS-IDENTITY-MODEL-v1.md) EIR-D01..D04 | Parallel DOM/WEB ids; co-terminous strings linked by edge — **yes** |
| [ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md](../foundation/ATLAS-LIFECYCLE-STATE-REGISTRY-v1.md) | Relationship **active** — **yes** |
| [ATLAS-EVIDENCE-REQUIREMENTS-v1.md](../foundation/ATLAS-EVIDENCE-REQUIREMENTS-v1.md) §4.6 | E1 for PRIMARY_DOMAIN structural — **yes** |
| [ATLAS-IDENTITY-GOVERNANCE-v1.md](../foundation/ATLAS-IDENTITY-GOVERNANCE-v1.md) §9.3 | Domain OWNS not inferred from Website OWNS — **yes** |
| [ATLAS-ENTITY-TAXONOMY-v1.md](../foundation/ATLAS-ENTITY-TAXONOMY-v1.md) §4–5 | Website vs Domain parallel classes — **yes** |
| [ATLAS-ATTESTATION-MODEL-v1.md](../foundation/ATLAS-ATTESTATION-MODEL-v1.md) | Human attestation required for canonical promotion — **yes** |

**Cross-wave validation:**

| Prior wave doc | Endpoint check |
|----------------|----------------|
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | DOM-0001..0004 **active** — **Pass** |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | WEB-0006..0009 **active** — **Pass** |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | OWNS/BELONGS_TO context consistent — **Pass** |
| [ATLAS-WAVE5-DOMAIN-POPULATION-v1.md](ATLAS-WAVE5-DOMAIN-POPULATION-v1.md) §6.1 | Four PRIMARY_DOMAIN candidates match — **Pass** |

**No new entity types.** **No new relationship families.** **No Foundation modifications.**

---

## 10. Related documents

| Doc | Role |
|-----|------|
| [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-REGISTER-v1.md) | Canonical relationship roster table |
| [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-ATTESTATION-v1.md) | Attestation act and verdict |
| [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | Domain endpoints |
| [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | Website endpoints |
| [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | Website-family context |
| [COUNTERPARTY-CARD-STORAGE-README-v1.md](COUNTERPARTY-CARD-STORAGE-README-v1.md) | External evidence paths |
