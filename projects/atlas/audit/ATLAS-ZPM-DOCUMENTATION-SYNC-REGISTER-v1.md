# ATLAS ZPM Documentation Sync Register v1

**Status:** **documented** — point-in-time sync action register.  
**Program:** ATLAS — Business Reality Registry  
**Sync date:** 2026-06-07  
**Scope:** ORG-0005 **ЗПМ** — P1 documentation synchronization  
**Parent:** [ATLAS-ZPM-DOCUMENTATION-SYNC-v1.md](ATLAS-ZPM-DOCUMENTATION-SYNC-v1.md) · [ATLAS-ZPM-DOCUMENTATION-SYNC-SUMMARY-v1.md](ATLAS-ZPM-DOCUMENTATION-SYNC-SUMMARY-v1.md)  
**Is not:** population register, attestation export, runtime table.

---

## 1. Register purpose

Единый **sync register** — какие артефакты обновлены, какие findings закрыты, что остаётся open. Lifecycle authority — attestation acts; sync **не меняет** graph structure.

---

## 2. Sync Group A — register updates

| register_id | target artifact | field / section | before | after | finding |
|-------------|-----------------|-----------------|--------|-------|---------|
| SYNC-A-01 | Wave 2 ZPM Person Register | PER-0014 lifecycle | **proposed** | **active** | ZPM-C-02 |
| SYNC-A-02 | Wave 2 ZPM Person Register | PER-0015 lifecycle | **proposed** | **active** | ZPM-C-02 |
| SYNC-A-03 | Wave 3 ZPM Project Register | PRJ-0009 lifecycle | **proposed** | **active** | ZPM-C-03 |
| SYNC-A-04 | Wave 3 ZPM Project Register | PRJ-0010 lifecycle | **proposed** | **deprecated** | ZPM-C-03 |
| SYNC-A-05 | Wave 3 ZPM Project Register | §9 deferred queue | Wave 3B/4/5 pending | completed items moved | ZPM-C-09 |
| SYNC-A-06 | Wave 4 ZPM Website Register | status header | pending attestation | attestation complete | ZPM-C-04 |
| SYNC-A-07 | Wave 4 ZPM Website Register | WEB-ZPM-01 lifecycle | **proposed** | **active** | ZPM-C-04 |
| SYNC-A-08 | Wave 4 ZPM Website Register | WEB-ZPM-02 | retired *(unchanged)* | **rejected / not minted** verified | — |
| SYNC-A-09 | Wave 5 ZPM Domain Register | status header | pending attestation | attestation complete | ZPM-C-05 |
| SYNC-A-10 | Wave 5 ZPM Domain Register | DOM-ZPM-01 lifecycle | target active | **active** attested | ZPM-C-05 |
| SYNC-A-11 | Wave 1B Org Register | `primary_contact_person_id` | absent | **PER-0014** | ZPM-C-01 |
| SYNC-A-12 | Wave 1B Org Register | `primary_domain` | SAFE UNKNOWN | **DOM-ZPM-01** *(active)* | ZPM-C-01 |

**Counts:** updates **12** · graph mutations **0**

---

## 3. Sync Group B — backup snapshot

| sync_id | section | action | entities added |
|---------|---------|--------|----------------|
| SYNC-B-01 | §1 summary | Person 13 → **15** | PER-0014, PER-0015 |
| SYNC-B-02 | §1 summary | Project 6 → **8** | PRJ-0009, PRJ-0010 |
| SYNC-B-03 | §1 summary | Website 4 → **5** | WEB-ZPM-01 |
| SYNC-B-04 | §1 summary | Domain 4 → **5** | DOM-ZPM-01 |
| SYNC-B-05 | §1 summary | Relationship 36 → **45** | REL-ZPM-* (9) |
| SYNC-B-06 | §4 Persons | roster rows | PER-0014, PER-0015 |
| SYNC-B-07 | §5 Relationships | family counts + ZPM ids | REL-ZPM-01, 02, PJ-01..04, WB-01, 03, 04 |
| SYNC-B-08 | §6 Projects | roster rows | PRJ-0009, PRJ-0010 |
| SYNC-B-09 | §7 Websites | roster row | WEB-ZPM-01 |
| SYNC-B-10 | §8 Domains | roster row | DOM-ZPM-01 |
| SYNC-B-11 | §10 *(new)* | ZPM slice roster | full entity + relationship table |
| SYNC-B-12 | §1 deferred note | remove stale ORG-0005 deferral | — |

**Finding closed:** **ZPM-C-06**

---

## 4. Sync Group C — integrity snapshot

| sync_id | target | action | finding |
|---------|--------|--------|---------|
| SYNC-C-01 | Integrity Audit §0.1 | Add Wave 3–5 ZPM scope rows | ZPM-C-07 |
| SYNC-C-02 | Integrity Audit §1 | Project 6→8, Website 4→5, Domain 4→5, Rel 38→45 | ZPM-C-07 |
| SYNC-C-03 | Integrity Audit §7.5 | Replace «No Project/Website/Domain» with attested slice | ZPM-C-07 |
| SYNC-C-04 | Integrity Register §5 | Add PRJ-0009, PRJ-0010 | ZPM-C-07 |
| SYNC-C-05 | Integrity Register §6 | Add WEB-ZPM-01 | ZPM-C-07 |
| SYNC-C-06 | Integrity Register §7 | Add DOM-ZPM-01 | ZPM-C-07 |
| SYNC-C-07 | Integrity Register §8 | Add REL-ZPM-PJ-01..04, REL-ZPM-WB-01, 03, 04 | ZPM-C-07 |
| SYNC-C-08 | Integrity Register §10.5 | SU-DOM-05 — DOM-ZPM-01 minted annotation | ZPM-C-08 |
| SYNC-C-09 | Integrity Audit | FINDING-INT-02 → **Resolved** | ZPM-C-02 |
| SYNC-C-10 | Integrity Audit | FINDING-INT-04 → **Resolved** | ZPM-C-06 |
| SYNC-C-11 | Integrity Summary | Statistics + Wave 5B readiness | ZPM-C-07 |

**Finding closed:** **ZPM-C-07**, **ZPM-C-08** *(registrant SAFE UNKNOWN preserved)*

---

## 5. Findings closure register

| ID | Severity | Topic | sync_status |
|----|----------|-------|-------------|
| **ZPM-C-01** | Low | Org register `primary_contact_person_id` | **Closed** — SYNC-A-11 |
| **ZPM-C-02** | Low | Person register lifecycle stale | **Closed** — SYNC-A-01, 02 |
| **ZPM-C-03** | Low | Project register lifecycle stale | **Closed** — SYNC-A-03, 04 |
| **ZPM-C-04** | Low | Website register header stale | **Closed** — SYNC-A-06, 07 |
| **ZPM-C-05** | Low | Domain register header stale | **Closed** — SYNC-A-09, 10 |
| **ZPM-C-06** | Medium | Backup snapshot incomplete | **Closed** — SYNC-B-* |
| **ZPM-C-07** | Medium | Integrity snapshot missing Waves 3–5 | **Closed** — SYNC-C-* |
| **ZPM-C-08** | Low | SU-DOM-05 not updated | **Closed** — SYNC-C-08 |
| **ZPM-C-09** | Info | Deferred-queue text outdated | **Closed** — SYNC-A-05 |

**P1 findings open:** **0**

---

## 6. SAFE UNKNOWN — post-sync posture

### 6.1 Resolved (unchanged — not re-opened)

| ID | Topic |
|----|-------|
| ME-W1B-04 | BZPM → **ЗПМ** canonical |
| SU-ZPM-PRJ-03 | Single Website model |
| ZPM-WEB-D-01 | WEB-ZPM-02 retired |

### 6.2 Open (unchanged — not closed by sync)

| ID | Topic | blocks Wave 5B? |
|----|-------|-----------------|
| ME-W2-ZPM-05 | Diadoc / EDO signer | **No** |
| SU-ZPM-PRJ-01, 02 | Historical contract / acceptance | **No** |
| SU-ZPM-PRJ-06 | Person ↔ Project edges | **No** |
| SU-ZPM-PRJ-07 | CLIENT_OF commercial | **No** — Wave 6 |
| SU-ZPM-PRJ-08 | Domain registrant | **Yes** — ORG→Domain OWNS |
| ME-W5-ZPM-01 | Registrar WHOIS | **Yes** — Wave 5B OWNS |
| ME-W5-ZPM-02 | `www.bzpm.ru` policy | **No** |
| SU-W4B-ZPM-01 | ORG-0001 OPERATES | **No** |
| SU-W4B-ZPM-02 | `www.bzpm.ru` secondary | **No** — Wave 5B |

---

## 7. ZPM slice roster (post-sync canonical documentation)

| Class | ID | lifecycle | attestation |
|-------|-----|-----------|-------------|
| Organization | ORG-0005 | **active** | AT-W1B-01 |
| Person | PER-0014 | **active** | AT-W2-ZPM-02 |
| Person | PER-0015 | **active** | AT-W2-ZPM-01 |
| Project | PRJ-0009 | **active** | AT-W3-ZPM-01 |
| Project | PRJ-0010 | **deprecated** | AT-W3-ZPM-02 |
| Website | WEB-ZPM-01 | **active** | AT-W4-ZPM-01 |
| Website | WEB-ZPM-02 | **not minted** | COR-ZPM-WEB-01 |
| Domain | DOM-ZPM-01 | **active** | AT-W5-ZPM-01 |

| relationship_id | lifecycle |
|-----------------|-----------|
| REL-ZPM-01, REL-ZPM-02 | **active** |
| REL-ZPM-PJ-01..04 | **active** |
| REL-ZPM-WB-01, REL-ZPM-WB-03, REL-ZPM-WB-04 | **active** |
| REL-ZPM-WB-02 | **cancelled** |

---

*ATLAS ZPM Documentation Sync Register v1 — sync only.*
