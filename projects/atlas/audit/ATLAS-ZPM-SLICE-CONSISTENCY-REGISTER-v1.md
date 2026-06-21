# ATLAS ZPM Slice Consistency Register v1

**Status:** **documented** — point-in-time ZPM slice audit register.  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07  
**Scope:** ORG-0005 **ЗПМ** — Wave 1B through Wave 5  
**Parent:** [ATLAS-ZPM-SLICE-CONSISTENCY-AUDIT-v1.md](ATLAS-ZPM-SLICE-CONSISTENCY-AUDIT-v1.md) · [ATLAS-ZPM-SLICE-CONSISTENCY-SUMMARY-v1.md](ATLAS-ZPM-SLICE-CONSISTENCY-SUMMARY-v1.md)  
**Is not:** population register, attestation export, runtime table.

---

## 1. Register purpose

Единый **audit register** сущностей и relationships ZPM slice на дату аудита. Lifecycle — по attestation acts; колонка `register_sync` фиксирует рассинхронизацию population registers.

---

## 2. Organizations

| org_id | canonical_name | legal_entity_id | lifecycle | attestation | aliases (active) | audit_flag |
|--------|----------------|-----------------|-----------|-------------|------------------|------------|
| ORG-0005 | **ЗПМ** | LE-0004 | **active** | AT-W1B-01; RN-W1B-01 | BZPM *(former)*; Завод Пищевого Машиностроения; ООО ЗПМ; ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | — |

**primary_contact_person_id:** **PER-0014** — attested at Wave 2B ([ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md](../population/ATLAS-WAVE2B-ZPM-RELATIONSHIP-ATTESTATION-v1.md) §4). Org register omits field — **ZPM-C-01**.

**Counts:** total **1** · active **1**

---

## 3. Legal entities

| legal_entity_id | legal_entity_name | org_binding | inn | lifecycle | attestation |
|-----------------|-------------------|-------------|-----|-----------|-------------|
| LE-0004 | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | ORG-0005 | 2221237587 | **active** | AT-W1B-01 |

**Counts:** total **1** · active **1**

---

## 4. Persons

| person_id | canonical_name | primary_org | lifecycle *(attested)* | attestation | org_edge | register_sync | orphan_check |
|-----------|----------------|-------------|------------------------|-------------|----------|---------------|--------------|
| PER-0014 | Алексей Владимирович Дубинский | ORG-0005 | **active** | AT-W2-ZPM-02 | REL-ZPM-02 | **stale** — register **proposed** | **Pass** |
| PER-0015 | Крюков Александр Сергеевич | ORG-0005 | **active** | AT-W2-ZPM-01 | REL-ZPM-01 | **stale** — register **proposed** | **Pass** |

**Counts:** total **2** · active **2** · proposed **0** *(attested)*

---

## 5. Projects

| project_id | canonical_name | lifecycle *(attested)* | commissioning | execution | graph_edges | register_sync | orphan_check |
|------------|----------------|------------------------|---------------|-----------|-------------|---------------|--------------|
| PRJ-0009 | Каталог-платформа bzpm.ru | **active** | ORG-0005 | ORG-0001 | REL-ZPM-PJ-01, 02; REL-ZPM-WB-01 | **stale** — register **proposed** | **Pass** |
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **deprecated** | ORG-0005 | ORG-0001 | REL-ZPM-PJ-03, 04; REL-ZPM-WB-03 | **stale** — register **proposed** | **Pass** |

**Counts:** total **2** · active **1** · deprecated **1**

---

## 6. Websites

| website_id | canonical_name | url | lifecycle *(attested)* | primary_org | project_context | register_sync | orphan_check |
|------------|----------------|-----|------------------------|-------------|-----------------|---------------|--------------|
| WEB-ZPM-01 | bzpm.ru | `https://bzpm.ru` | **active** | ORG-0005 | PRJ-0009, PRJ-0010 | **stale** — header pending attestation | **Pass** |

**Retired (verified):**

| website_id | disposition | audit_flag |
|------------|-------------|------------|
| WEB-ZPM-02 | **not minted** — COR-ZPM-WEB-01 | **Pass** — fully retired |

**Counts:** active **1** · retired **1** *(id unused)*

---

## 7. Domains

| domain_id | canonical_name | hostname_class | lifecycle *(attested)* | website_pair | registrar | register_sync | orphan_check |
|-----------|----------------|----------------|------------------------|--------------|-----------|---------------|--------------|
| DOM-ZPM-01 | bzpm.ru | apex | **active** | WEB-ZPM-01 | **SAFE UNKNOWN** | **stale** — header pending attestation | **Pass** |

**Duplicate hostname check:** No other `DOM-*` with `bzpm.ru` — **Pass**

**Counts:** total **1** · active **1**

---

## 8. Relationships — attested roster

| relationship_id | family | source | target | type | lifecycle | endpoint_check |
|-----------------|--------|--------|--------|------|-----------|----------------|
| REL-ZPM-01 | P→O | PER-0015 | ORG-0005 | GENERAL_DIRECTOR | **active** | **Pass** |
| REL-ZPM-02 | P→O | PER-0014 | ORG-0005 | REPRESENTATIVE | **active** | **Pass** |
| REL-ZPM-PJ-01 | Pj→O | PRJ-0009 | ORG-0005 | COMMISSIONED_BY | **active** | **Pass** |
| REL-ZPM-PJ-02 | O→Pj | ORG-0001 | PRJ-0009 | EXECUTES | **active** | **Pass** |
| REL-ZPM-PJ-03 | Pj→O | PRJ-0010 | ORG-0005 | COMMISSIONED_BY | **active** | **Pass** |
| REL-ZPM-PJ-04 | O→Pj | ORG-0001 | PRJ-0010 | EXECUTES | **active** | **Pass** |
| REL-ZPM-WB-01 | W→Pj | WEB-ZPM-01 | PRJ-0009 | BELONGS_TO | **active** | **Pass** |
| REL-ZPM-WB-03 | W→Pj | WEB-ZPM-01 | PRJ-0010 | BELONGS_TO | **active** | **Pass** |
| REL-ZPM-WB-04 | O→W | ORG-0005 | WEB-ZPM-01 | OWNS | **active** | **Pass** |

**Cancelled (verified absent):**

| relationship_id | prior draft | reason |
|-----------------|-------------|--------|
| REL-ZPM-WB-02 | WEB-ZPM-02 → PRJ-0010 BELONGS_TO | COR-ZPM-WEB-06 |

**Counts:** attested **9** · cancelled **1** · orphan failures **0**

---

## 9. ZPM graph cross-reference

```
ORG-0005 ЗПМ ──OWNS──► WEB-ZPM-01 bzpm.ru
       │                      │
       │                      ├──BELONGS_TO──► PRJ-0009 (active)
       │                      └──BELONGS_TO──► PRJ-0010 (deprecated)
       │
       ├──◄──REL-ZPM-01── PER-0015 (GENERAL_DIRECTOR)
       └──◄──REL-ZPM-02── PER-0014 (REPRESENTATIVE; primary_contact)

PRJ-0009 ──COMMISSIONED_BY──► ORG-0005    ORG-0001 ──EXECUTES──► PRJ-0009
PRJ-0010 ──COMMISSIONED_BY──► ORG-0005    ORG-0001 ──EXECUTES──► PRJ-0010

DOM-ZPM-01 bzpm.ru ──(Wave 5B queue)──► WEB-ZPM-01 PRIMARY_DOMAIN
```

---

## 10. Findings register

| ID | Severity | Topic | register_sync |
|----|----------|-------|---------------|
| ZPM-C-01 | Low | `primary_contact_person_id` not on org register | Org register |
| ZPM-C-02 | Low | Person register lifecycle stale | Person register |
| ZPM-C-03 | Low | Project register lifecycle stale | Project register |
| ZPM-C-04 | Low | Website register attestation header stale | Website register |
| ZPM-C-05 | Low | Domain register attestation header stale | Domain register |
| ZPM-C-06 | Medium | Backup snapshot incomplete for ZPM slice | Backup snapshot |
| ZPM-C-07 | Medium | Integrity snapshot missing Waves 3–5 ZPM | Integrity trilogy |
| ZPM-C-08 | Low | SU-DOM-05 not annotated for DOM-ZPM-01 | Integrity register |
| ZPM-C-09 | Info | Deferred-queue text references completed waves | Project register §9 |

---

## 11. SAFE UNKNOWN inventory (ZPM slice)

### 11.1 Resolved (closed)

| ID | Topic | Resolution |
|----|-------|------------|
| ME-W1B-04 | BZPM acronym expansion | Canonical **ЗПМ** — RN-W1B-01 |
| SU-ZPM-PRJ-03 | Deployment replace vs coexistence | Single Website model — COR-ZPM-WEB-* |
| ZPM-WEB-D-01 | Dual Website same hostname | WEB-ZPM-02 retired |

### 11.2 Open (correctly unresolved)

| ID | Topic | Entity | Severity | Blocks Wave 5B? |
|----|-------|--------|----------|-----------------|
| ME-W2-ZPM-05 | Diadoc / EDO signer | ORG-0005 | Medium | **No** |
| ME-W2-ZPM-04 | PER-0015 email, Telegram | PER-0015 | Low | **No** |
| SU-ZPM-PRJ-01 | Historical contract dates | PRJ-0010 | Low | **No** |
| SU-ZPM-PRJ-02 | Formal acceptance docs | PRJ-0010 | Low | **No** |
| SU-ZPM-PRJ-06 | Person ↔ Project edges | — | Low | **No** |
| SU-ZPM-PRJ-07 | CLIENT_OF ORG-0005 → ORG-0001 | ORG-0005 | Medium | **No** — Wave 6 |
| SU-ZPM-PRJ-08 | Domain registrant | DOM-ZPM-01 | Low | **Yes** — ORG→Domain OWNS |
| ME-W5-ZPM-01 | Registrar WHOIS export | DOM-ZPM-01 | Medium | **Yes** — Wave 5B OWNS |
| ME-W5-ZPM-02 | `www.bzpm.ru` policy | — | Low | **No** — policy choice |
| SU-W4B-ZPM-01 | ORG-0001 OPERATES WEB-ZPM-01 | WEB-ZPM-01 | Low | **No** |
| SU-W4B-ZPM-02 | `www.bzpm.ru` secondary hostname | — | Low | **No** — Wave 5B |

---

## 12. Source register index

| Register | Path | Audit role |
|----------|------|------------|
| Wave 1B Org | [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](../population/ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) | ORG-0005, LE-0004 |
| Wave 1B Rename | [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](../population/ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md) | Canonical **ЗПМ** |
| Wave 2 ZPM Person | [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](../population/ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | PER-0014, 0015 |
| Wave 2B ZPM Rel | [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](../population/ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) | REL-ZPM-01, 02 |
| Wave 3 ZPM Project | [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](../population/ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | PRJ-0009, 0010 |
| Wave 3B ZPM Rel | [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](../population/ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) | REL-ZPM-PJ-* |
| Wave 4 ZPM Website | [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](../population/ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | WEB-ZPM-01 |
| Wave 4B ZPM Rel | [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](../population/ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) | REL-ZPM-WB-* |
| Wave 5 ZPM Domain | [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](../population/ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) | DOM-ZPM-01 |
| Website correction | [ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md](../population/ATLAS-ZPM-WEBSITE-MODEL-CORRECTION-EXECUTION-v1.md) | WEB-ZPM-02 retirement |
| Backup | [ATLAS-BACKUP-SNAPSHOT-v1.md](../population/ATLAS-BACKUP-SNAPSHOT-v1.md) | Baseline |
| Integrity | Integrity Snapshot trilogy | Ecosystem cross-check |

---

*ATLAS ZPM Slice Consistency Register v1 — audit only.*
