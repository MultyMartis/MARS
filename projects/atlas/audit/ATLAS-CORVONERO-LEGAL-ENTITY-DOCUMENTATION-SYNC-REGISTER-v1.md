# ATLAS Corvonero Legal Entity Documentation Sync Register v1

**Status:** **documented** — point-in-time sync action register.  
**Program:** ATLAS — Business Reality Registry  
**Sync date:** 2026-06-29  
**Scope:** ORG-0009 / **LE-0006** — post–AT-CORV-LE-01 documentation synchronization  
**Parent:** [ATLAS-CORVONERO-LEGAL-ENTITY-DOCUMENTATION-SYNC-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-DOCUMENTATION-SYNC-v1.md) · [ATLAS-CORVONERO-LEGAL-ENTITY-DOCUMENTATION-SYNC-SUMMARY-v1.md](ATLAS-CORVONERO-LEGAL-ENTITY-DOCUMENTATION-SYNC-SUMMARY-v1.md)  
**Is not:** population register, attestation export, runtime table.

---

## 1. Register purpose

Единый **sync register** — какие артефакты обновлены после enrichment **LE-0006**, какие stale references закрыты, что остаётся **SAFE UNKNOWN**. Lifecycle authority — **AT-CORV-LE-01**; sync **не меняет** graph structure.

---

## 2. Sync Group A — register updates

| register_id | target artifact | field / section | before | after | finding |
|-------------|-----------------|-----------------|--------|-------|---------|
| SYNC-A-01 | Corvonero Organization Register | §3 legal entity index | identity only; «operator intake only» | requisites + addresses + banking; **AT-CORV-LE-01** | CORV-SYNC-01 |
| SYNC-A-02 | Corvonero Organization Register | §1 summary attestation | AT-CORV-ORG-01 only | + **AT-CORV-LE-01** | CORV-SYNC-02 |
| SYNC-A-03 | Corvonero Organization Register | footer completeness note | «E0 partial» | «E0 requisites-enriched partial» | CORV-SYNC-02 |
| SYNC-A-04 | Corvonero LE Register | §2.2 roster columns | `ИП`; `bank_account` / `corr_account` | `individual_entrepreneur`; `jurisdiction` **RU**; settlement / correspondent accounts | CORV-SYNC-03 |
| SYNC-A-05 | Corvonero LE Register | §2.2a *(new)* | absent | canonical field verification matrix | CORV-SYNC-03 |
| SYNC-A-06 | Corvonero LE Register | §6 SAFE UNKNOWN | 10 items | 13 items — tax_system, registration_authority, operational_contacts explicit | CORV-SYNC-03 |
| SYNC-A-07 | Corvonero Registration Report | §4.2 LE-0006 | intake-only partial | full requisites subset + sync cross-ref | CORV-SYNC-04 |

**Counts:** documentation updates **7** · graph mutations **0** · entities minted **0**

---

## 3. Sync Group B — backup snapshot

| sync_id | target | check | action | finding |
|---------|--------|-------|--------|---------|
| SYNC-B-01 | ATLAS-BACKUP-SNAPSHOT-v1 | LE-0006 incomplete ref | **None found** — predates Corvonero | — |
| SYNC-B-02 | ATLAS-BACKUP-SNAPSHOT-v1 | entity totals | **Unchanged** — not required | — |

**Finding:** no backup snapshot sync required.

---

## 4. Sync Group C — integrity snapshot

| sync_id | target | check | action | finding |
|---------|--------|-------|--------|---------|
| SYNC-C-01 | Integrity snapshot trilogy | Corvo Nero LE incomplete ref | **None found** | — |
| SYNC-C-02 | Integrity snapshot trilogy | entity totals | **Unchanged** — not required | — |

**Finding:** no integrity snapshot sync required.

---

## 5. Stale reference closure register

| ID | topic | location | sync_status |
|----|-------|----------|-------------|
| **CORV-SYNC-01** | Org register LE index stale completeness | Organization register §3 | **Closed** — SYNC-A-01 |
| **CORV-SYNC-02** | Org register missing AT-CORV-LE-01 | Organization register §1, footer | **Closed** — SYNC-A-02, 03 |
| **CORV-SYNC-03** | LE register missing canonical field map | LE register §2.2, §2.2a, §6 | **Closed** — SYNC-A-04..06 |
| **CORV-SYNC-04** | Registration report §4.2 stale | Registration report | **Closed** — SYNC-A-07 |

**Open stale refs in synced scope:** **0**

---

## 6. Canonical field presence register — LE-0006

| field | present | evidence |
|-------|---------|----------|
| legal_entity_type = **individual_entrepreneur** | **Yes** | EV-CORV-OP-REQ-01 |
| jurisdiction = **RU** | **Yes** | inferred from ИП + RU addresses — documented, not E2 |
| legal_address | **Yes** | EV-CORV-OP-REQ-01 |
| actual_address | **Yes** | EV-CORV-OP-REQ-01 |
| inn | **Yes** | EV-CORV-OP-REQ-01 |
| ogrnip | **Yes** | EV-CORV-OP-REQ-01 |
| bik | **Yes** | EV-CORV-OP-REQ-01 |
| settlement_account | **Yes** | EV-CORV-OP-REQ-01 |
| correspondent_account | **Yes** | EV-CORV-OP-REQ-01 |
| bank_name | **SAFE UNKNOWN** | — |
| tax_system | **SAFE UNKNOWN** | — |
| registration_authority | **SAFE UNKNOWN** | — |
| legal_signatory_contact | **SAFE UNKNOWN** | — |
| operational_contacts | **SAFE UNKNOWN** | — |
| registrar | **SAFE UNKNOWN** | Domain layer |
| domain ownership confirmation | **SAFE UNKNOWN** | Website / Domain layers |

---

## 7. Validation matrix

| Gate | Result |
|------|--------|
| ORG-0009 unchanged | **Pass** |
| LE-0006 unchanged *(entity)* | **Pass** |
| only documentation synchronized | **Pass** |
| no new entities | **Pass** |
| no new relationships | **Pass** |
| no lifecycle changes | **Pass** |
| no Foundation changes | **Pass** |
| no graph mutations | **Pass** |

---

## 8. Readiness verdict

```text
CORVO NERO LEGAL ENTITY DOCUMENTATION FULLY SYNCHRONIZED
```

---

*ATLAS Corvonero Legal Entity Documentation Sync Register v1 — sync only; no commit.*
