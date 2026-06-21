# ATLAS Integrity Snapshot Register v1

**Status:** **documented** — point-in-time entity and relationship audit register.  
**Program:** ATLAS — Business Reality Registry  
**Audit date:** 2026-06-07 · **sync:** 2026-06-07 (ZPM documentation sync)  
**Parent:** [ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md](ATLAS-INTEGRITY-SNAPSHOT-AUDIT-v1.md) · [ATLAS-INTEGRITY-SNAPSHOT-SUMMARY-v1.md](ATLAS-INTEGRITY-SNAPSHOT-SUMMARY-v1.md)  
**Is not:** population register, attestation export, runtime table.

---

## 1. Register purpose

Единый **audit register** всех сущностей и relationships, входящих в scope активных Wave outputs на дату снимка. Одна строка — одна запись с lifecycle, attestation posture и orphan / ID flags.

**Authority hierarchy applied:**

1. Formal **attestation acts** (`Status: attested`) — canonical lifecycle.
2. Population registers — secondary; flagged when stale vs attestation act.
3. Relationship registers — endpoint validation for graph checks.

---

## 2. Organizations

| org_id | canonical_name | wave | lifecycle | attestation | orphan_check | audit_flag |
|--------|----------------|------|-----------|-------------|--------------|------------|
| ORG-0001 | Веб-студия «Полигон» | W1 | **active** | Wave 1 | — | — |
| ORG-0002 | Агентство «МетаКод» | W1 | **active** | Wave 1 | — | — |
| ORG-0003 | i-SEO Studio | W1 | **active** | Wave 1 | — | — |
| ORG-0004 | Триумф | W1 | **active** | Wave 1 | — | — |
| ORG-0005 | **ЗПМ** | W1-B | **active** | AT-W1B-01 | — | — |
| ORG-0006 | SIBCAR | W1-C | **active** | AT-W1C-01 | — | — |

**Counts:** total **6** · active **6** · proposed **0** · deprecated **0**

---

## 3. Legal entities

| legal_entity_id | legal_entity_name | org_binding | lifecycle | attestation | audit_flag |
|-----------------|-------------------|-------------|-----------|-------------|------------|
| LE-0001 | ИП Русецкий А. А. | ORG-0001 | **active** | Wave 1 | — |
| LE-0002 | ИП Шваков Н. А. | ORG-0003 | **active** | Wave 1 | — |
| LE-0003 | ООО «Триумф» | ORG-0004 | **active** | Wave 1 | — |
| LE-0004 | ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | ORG-0005 | **active** | AT-W1B-01 | — |
| LE-0005 | ООО «СибКар» | ORG-0006 | **active** | AT-W1C-01 | — |

**Counts:** total **5** · active **5** · proposed **0** · deprecated **0**

---

## 4. Persons

| person_id | canonical_name | primary_org | lifecycle | attestation | org_edge | orphan_check |
|-----------|----------------|-------------|-----------|-------------|----------|--------------|
| PER-0001 | Русецкий Андрей Анатольевич | ORG-0001 | **active** | AT-W2-01 | REL-0001, REL-0002 | **Pass** |
| PER-0002 | Фатюткин Сергей Игоревич | **SAFE UNKNOWN** | **active** | AT-W2-05 | *(none — by design)* | **Pass** isolated |
| PER-0003 | Лиматов Роман Курбанович | **SAFE UNKNOWN** | **active** | AT-W2-05 | *(none — by design)* | **Pass** isolated |
| PER-0004 | Макарова Алеся Леонидовна | ORG-0004 | **active** | AT-W2-04 | REL-0013 | **Pass** |
| PER-0005 | Подзолков Максим | ORG-0004 | **active** | AT-W2-04 | REL-0014 | **Pass** |
| PER-0006 | Вагин Иван Владимирович | ORG-0004 | **active** | AT-W2-04 | REL-0015 | **Pass** |
| PER-0007 | Беслангурова Тамила | ORG-0003 | **active** | AT-W2-03 | REL-0007 | **Pass** |
| PER-0008 | Денис Леонов | ORG-0003 | **active** | AT-W2-03 | REL-0008 | **Pass** |
| PER-0009 | Антон Кораблёв | ORG-0003 | **active** | AT-W2-03 | REL-0012 | **Pass** |
| PER-0010 | Дягилева Ольга | ORG-0003 | **active** | AT-W2-03 | REL-0009 | **Pass** |
| PER-0011 | Шваков Никита Алексеевич | ORG-0003 | **active** | AT-W2-02 | REL-0006 | **Pass** |
| PER-0012 | Илья Гуренков | ORG-0003 | **active** | AT-W2-03 | REL-0010 | **Pass** |
| PER-0013 | Иван Корольков | ORG-0003 | **active** | AT-W2-03 | REL-0011 | **Pass** |
| PER-0014 | Алексей Владимирович Дубинский | ORG-0005 | **active** | AT-W2-ZPM-02 | REL-ZPM-02 | **Pass** |
| PER-0015 | Крюков Александр Сергеевич | ORG-0005 | **active** | AT-W2-ZPM-01 | REL-ZPM-01 | **Pass** |

**Counts:** total **15** · active **15** · proposed **0** · deprecated **0**

---

## 5. Projects

| project_id | canonical_name | lifecycle | commissioning | execution | graph_edges | orphan_check |
|------------|----------------|-----------|---------------|-----------|-------------|--------------|
| PRJ-0001 | MARS | **active** | **SAFE UNKNOWN** | ORG-0002 *(display)* | *(none attested)* | **Pass** — internal; documented |
| PRJ-0004 | Редизайн gktriumph.ru | **deprecated** | ORG-0004 | ORG-0001 | REL-0017, 0018; WEB via REL-0027 | **Pass** |
| PRJ-0005 | Грузотакси | **active** | ORG-0004 | ORG-0001 | REL-0019, 0020; REL-0030 | **Pass** |
| PRJ-0006 | SEO gktriumph.ru | **active** | ORG-0004 | ORG-0001 | REL-0021, 0022; REL-0028 | **Pass** |
| PRJ-0007 | Блог gktriumph.ru | **active** | ORG-0004 | ORG-0001 | REL-0023, 0024; REL-0029 | **Pass** |
| PRJ-0008 | Манипулятор | **active** | ORG-0004 | ORG-0001 | REL-0025, 0026; REL-0031 | **Pass** |
| PRJ-0009 | Каталог-платформа bzpm.ru | **active** | ORG-0005 | ORG-0001 | REL-ZPM-PJ-01, 02; REL-ZPM-WB-01 | **Pass** |
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **deprecated** | ORG-0005 | ORG-0001 | REL-ZPM-PJ-03, 04; REL-ZPM-WB-03 | **Pass** |

**Counts:** total **8** · active **6** · proposed **0** · deprecated **2**  
**Audit flag:** **FINDING-INT-03** *(reclassified — documentation gap only)* — no dedicated Project entity attestation act file; endpoints used in attested Wave 3B / 4B. See [ATLAS-AUDIT-FINDINGS-REMEDIATION-v1.md](ATLAS-AUDIT-FINDINGS-REMEDIATION-v1.md).

---

## 6. Websites

| website_id | canonical_name | lifecycle | primary_org | project_context | domain_link | orphan_check |
|------------|----------------|-----------|-------------|-----------------|-------------|--------------|
| WEB-0006 | gktriumph.ru | **active** | ORG-0004 | PRJ-0004, PRJ-0006 | DOM-0001 REL-0036 | **Pass** |
| WEB-0007 | blog.gktriumph.ru | **active** | ORG-0004 | PRJ-0007 | DOM-0002 REL-0037 | **Pass** |
| WEB-0008 | gruzotaxi-triumph.ru | **active** | ORG-0004 | PRJ-0005 | DOM-0003 REL-0038 | **Pass** |
| WEB-0009 | manipulator-triumph.ru | **active** | ORG-0004 | PRJ-0008 | DOM-0004 REL-0039 | **Pass** |
| WEB-ZPM-01 | bzpm.ru | **active** | ORG-0005 | PRJ-0009, PRJ-0010 | DOM-ZPM-01 *(5B queue)* | **Pass** |

**Counts:** total **5** · active **5** · proposed **0** · deprecated **0**  
**Audit flag:** **FINDING-INT-03** *(reclassified — documentation gap only)* — no dedicated Website entity attestation act file.

---

## 7. Domains

| domain_id | canonical_name | lifecycle | website_link | org_owns_edge | orphan_check |
|-----------|----------------|-----------|--------------|---------------|--------------|
| DOM-0001 | gktriumph.ru | **active** | WEB-0006 REL-0036 | **none** *(SAFE UNKNOWN registrant)* | **Pass** |
| DOM-0002 | blog.gktriumph.ru | **active** | WEB-0007 REL-0037 | **none** | **Pass** |
| DOM-0003 | gruzotaxi-triumph.ru | **active** | WEB-0008 REL-0038 | **none** | **Pass** |
| DOM-0004 | manipulator-triumph.ru | **active** | WEB-0009 REL-0039 | **none** | **Pass** |
| DOM-ZPM-01 | bzpm.ru | **active** | WEB-ZPM-01 *(PRIMARY_DOMAIN Wave 5B)* | **none** *(registrant SAFE UNKNOWN)* | **Pass** |

**Counts:** total **5** · active **5** · proposed **0** · deprecated **0**  
**Audit flag:** **FINDING-INT-03** *(reclassified — documentation gap only)* — no dedicated Domain entity attestation act file.

---

## 8. Relationships — attested roster

| relationship_id | family | source | target | type | lifecycle | endpoint_check |
|-----------------|--------|--------|--------|------|-----------|----------------|
| REL-0001 | P→O | PER-0001 | ORG-0001 | OWNER | **active** | **Pass** |
| REL-0002 | P→O | PER-0001 | ORG-0002 | OWNER | **active** | **Pass** |
| REL-0006 | P→O | PER-0011 | ORG-0003 | OWNER | **active** | **Pass** |
| REL-0007 | P→O | PER-0007 | ORG-0003 | EMPLOYEE | **active** | **Pass** |
| REL-0008 | P→O | PER-0008 | ORG-0003 | EMPLOYEE | **active** | **Pass** |
| REL-0009 | P→O | PER-0010 | ORG-0003 | EMPLOYEE | **active** | **Pass** |
| REL-0010 | P→O | PER-0012 | ORG-0003 | EMPLOYEE | **active** | **Pass** |
| REL-0011 | P→O | PER-0013 | ORG-0003 | EMPLOYEE | **active** | **Pass** |
| REL-0012 | P→O | PER-0009 | ORG-0003 | EMPLOYEE | **active** | **Pass** |
| REL-0013 | P→O | PER-0004 | ORG-0004 | REPRESENTATIVE | **active** | **Pass** |
| REL-0014 | P→O | PER-0005 | ORG-0004 | EMPLOYEE | **active** | **Pass** |
| REL-0015 | P→O | PER-0006 | ORG-0004 | GENERAL_DIRECTOR | **active** | **Pass** |
| REL-ZPM-01 | P→O | PER-0015 | ORG-0005 | GENERAL_DIRECTOR | **active** | **Pass** |
| REL-ZPM-02 | P→O | PER-0014 | ORG-0005 | REPRESENTATIVE | **active** | **Pass** |
| REL-0016 | O→O | ORG-0004 | ORG-0001 | CLIENT_OF | **active** | **Pass** |
| REL-0017 | Pj→O | PRJ-0004 | ORG-0004 | COMMISSIONED_BY | **active** | **Pass** |
| REL-0018 | O→Pj | ORG-0001 | PRJ-0004 | EXECUTES | **active** | **Pass** |
| REL-0019 | Pj→O | PRJ-0005 | ORG-0004 | COMMISSIONED_BY | **active** | **Pass** |
| REL-0020 | O→Pj | ORG-0001 | PRJ-0005 | EXECUTES | **active** | **Pass** |
| REL-0021 | Pj→O | PRJ-0006 | ORG-0004 | COMMISSIONED_BY | **active** | **Pass** |
| REL-0022 | O→Pj | ORG-0001 | PRJ-0006 | EXECUTES | **active** | **Pass** |
| REL-0023 | Pj→O | PRJ-0007 | ORG-0004 | COMMISSIONED_BY | **active** | **Pass** |
| REL-0024 | O→Pj | ORG-0001 | PRJ-0007 | EXECUTES | **active** | **Pass** |
| REL-0025 | Pj→O | PRJ-0008 | ORG-0004 | COMMISSIONED_BY | **active** | **Pass** |
| REL-0026 | O→Pj | ORG-0001 | PRJ-0008 | EXECUTES | **active** | **Pass** |
| REL-0027 | W→Pj | WEB-0006 | PRJ-0004 | BELONGS_TO | **active** | **Pass** |
| REL-0028 | W→Pj | WEB-0006 | PRJ-0006 | BELONGS_TO | **active** | **Pass** |
| REL-0029 | W→Pj | WEB-0007 | PRJ-0007 | BELONGS_TO | **active** | **Pass** |
| REL-0030 | W→Pj | WEB-0008 | PRJ-0005 | BELONGS_TO | **active** | **Pass** |
| REL-0031 | W→Pj | WEB-0009 | PRJ-0008 | BELONGS_TO | **active** | **Pass** |
| REL-0032 | O→W | ORG-0004 | WEB-0006 | OWNS | **active** | **Pass** |
| REL-0033 | O→W | ORG-0004 | WEB-0007 | OWNS | **active** | **Pass** |
| REL-0034 | O→W | ORG-0004 | WEB-0008 | OWNS | **active** | **Pass** |
| REL-0035 | O→W | ORG-0004 | WEB-0009 | OWNS | **active** | **Pass** |
| REL-0036 | D→W | DOM-0001 | WEB-0006 | PRIMARY_DOMAIN | **active** | **Pass** |
| REL-0037 | D→W | DOM-0002 | WEB-0007 | PRIMARY_DOMAIN | **active** | **Pass** |
| REL-0038 | D→W | DOM-0003 | WEB-0008 | PRIMARY_DOMAIN | **active** | **Pass** |
| REL-0039 | D→W | DOM-0004 | WEB-0009 | PRIMARY_DOMAIN | **active** | **Pass** |
| REL-ZPM-PJ-01 | Pj→O | PRJ-0009 | ORG-0005 | COMMISSIONED_BY | **active** | **Pass** |
| REL-ZPM-PJ-02 | O→Pj | ORG-0001 | PRJ-0009 | EXECUTES | **active** | **Pass** |
| REL-ZPM-PJ-03 | Pj→O | PRJ-0010 | ORG-0005 | COMMISSIONED_BY | **active** | **Pass** |
| REL-ZPM-PJ-04 | O→Pj | ORG-0001 | PRJ-0010 | EXECUTES | **active** | **Pass** |
| REL-ZPM-WB-01 | W→Pj | WEB-ZPM-01 | PRJ-0009 | BELONGS_TO | **active** | **Pass** |
| REL-ZPM-WB-03 | W→Pj | WEB-ZPM-01 | PRJ-0010 | BELONGS_TO | **active** | **Pass** |
| REL-ZPM-WB-04 | O→W | ORG-0005 | WEB-ZPM-01 | OWNS | **active** | **Pass** |

**Counts:** total **45** · active **45** · proposed **0** · deprecated **0**  
**Orphan relationship failures:** **0**

**Intentional non-created IDs:** REL-0003 (deferred), REL-0004 (rejected), REL-0005 (rejected).

---

## 9. ID validation matrix

| Prefix | Assigned range | Gaps | Duplicates | Collisions | Reuse |
|--------|----------------|------|------------|------------|-------|
| ORG-* | 0001..0006 | none | none | none | none |
| LE-* | 0001..0005 | none | none | none | none |
| PER-* | 0001..0015 | none | none | none | none |
| PRJ-* | 0001, 0004..0010 | 0002, 0003 — no evidence | none | none | none |
| WEB-* | 0006..0009, WEB-ZPM-01 | 0001..0005 deferred | none | none | none |
| DOM-* | 0001..0004, DOM-ZPM-01 | none | none | none | none |
| REL-* | 0001..0039 | 0003..0005 intentional | none | none | none |
| REL-ZPM-* | 01..02, PJ-01..04, WB-01, 03, 04 | WB-02 cancelled | none | none vs REL-* | none |

**Verdict:** **Pass** — gaps are documented governance decisions, not repair-required defects.

---

## 10. SAFE UNKNOWN inventory

### 10.1 Organization

| ID | Topic | Entity | Severity |
|----|-------|--------|----------|
| SU-ORG-01 | ORG-0005 production domain registrant | ORG-0005 | Low |
| SU-ORG-02 | ORG-0005 EDO / Diadoc participant id | ORG-0005 | Low |
| SU-ORG-03 | ORG-0006 production public URL | ORG-0006 | Low |
| SU-ORG-04 | ORG-0006 production domain | ORG-0006 | Low |
| SU-ORG-05 | ORG-0006 EDO / Diadoc participant id | ORG-0006 | Low |
| SU-ORG-06 | ORG-0006 phone / fax not on CC | ORG-0006 | Low |
| SU-ORG-07 | ORG-0005 Diadoc / EDO specific signer | ORG-0005 | Medium |
| SU-ORG-08 | Site title «Автосалон СИБКАР» vs CC name | ORG-0006 | Low |

### 10.2 Person

| ID | Topic | Entity | Severity |
|----|-------|--------|----------|
| SU-PER-01 | PER-0002 primary organization (Moscow SERM) | PER-0002 | Medium *(2B only)* |
| SU-PER-02 | PER-0003 primary organization (Metallka) | PER-0003 | Medium *(2B only)* |
| SU-PER-03 | PER-0015 email, Telegram | PER-0015 | Low |
| SU-PER-04 | Patronymics UNKNOWN (i-SEO team subset) | PER-0008, 0010, 0012, 0013, 0005 | Low |

### 10.3 Project

| ID | Topic | Entity | Severity |
|----|-------|--------|----------|
| SU-PRJ-01 | PRJ-0001 COMMISSIONED_BY | PRJ-0001 | Low |
| SU-PRJ-02 | PRJ-0001 EXECUTES attested edge | PRJ-0001 | Low — ORG-0002 display only |

### 10.4 Website

| ID | Topic | Entity | Severity |
|----|-------|--------|----------|
| SU-WEB-01 | ORG-0001 OPERATES WEB-0006..0009 | WEB-0006..0009 | Low |

### 10.5 Domain

| ID | Topic | Entity | Severity |
|----|-------|--------|----------|
| SU-DOM-01 | Registrar / registrant DOM-0001..0004 | DOM-0001..0004 | Medium |
| SU-DOM-02 | ORG-0004 → DOM-* OWNS edge | DOM-0001..0004 | Medium |
| SU-DOM-03 | `www.gktriumph.ru` policy | — | Low |
| SU-DOM-04 | ORG-0001 DNS custodian | DOM-0001..0004 | Low |
| SU-DOM-05 | ORG-0005 production domain | ORG-0005 / DOM-ZPM-01 | Low — **entity minted**; registrant **SAFE UNKNOWN** |

### 10.6 Relationship

| ID | Topic | Severity |
|----|-------|----------|
| SU-REL-01 | REL-0016 effective_from / effective_to | Low |
| SU-REL-02 | REL-0016 service line granularity | Low |
| SU-REL-03 | Diadoc signer edge ORG-0005 | Medium |
| SU-REL-04 | ORG-0005 CLIENT_OF ORG-0001 | Medium |
| SU-REL-05 | ORG-0005 ↔ ORG-0006 commercial | Medium |
| SU-REL-06 | ORG-0006 CLIENT_OF ORG-0001 | Medium |
| SU-REL-07 | W1-C latent clients → ORG-0001 | Medium |
| SU-REL-08 | Moscow SERM / Metallka org edges | Medium |
| SU-REL-09 | REL-0003 PER-0001 MANAGER ORG-0003 | Low |
| SU-REL-10 | Person ↔ Project edges | Low |
| SU-REL-11 | ORG-0002 MetaCode EXECUTES PRJ-0001 | Low |
| SU-REL-12 | i-SEO vs Polygon on SEO delivery | Low |

---

## 11. Source register index

| Register | Path | Audit role |
|----------|------|------------|
| Wave 1B BZPM Org | [ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md](../population/ATLAS-WAVE1B-BZPM-ORGANIZATION-REGISTER-v1.md) | ORG-0005, LE-0004 |
| Wave 1C SIBCAR Org | [ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md](../population/ATLAS-WAVE1C-SIBCAR-ORGANIZATION-REGISTER-v1.md) | ORG-0006, LE-0005 |
| Wave 2 Person | [ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md](../population/ATLAS-WAVE2-ATTESTATION-REGISTER-v1.md) | PER-0001..0013 |
| Wave 2 ZPM Person | [ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md](../population/ATLAS-WAVE2-ZPM-PERSON-REGISTER-v1.md) | PER-0014, 0015 |
| Wave 3 Project | [ATLAS-WAVE3-PROJECT-REGISTER-v1.md](../population/ATLAS-WAVE3-PROJECT-REGISTER-v1.md) | PRJ-* |
| Wave 4 Website | [ATLAS-WAVE4-WEBSITE-REGISTER-v1.md](../population/ATLAS-WAVE4-WEBSITE-REGISTER-v1.md) | WEB-* |
| Wave 5 Domain | [ATLAS-WAVE5-DOMAIN-REGISTER-v1.md](../population/ATLAS-WAVE5-DOMAIN-REGISTER-v1.md) | DOM-* |
| Wave 3 ZPM Project | [ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md](../population/ATLAS-WAVE3-ZPM-PROJECT-REGISTER-v1.md) | PRJ-0009, 0010 |
| Wave 4 ZPM Website | [ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md](../population/ATLAS-WAVE4-ZPM-WEBSITE-REGISTER-v1.md) | WEB-ZPM-01 |
| Wave 5 ZPM Domain | [ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md](../population/ATLAS-WAVE5-ZPM-DOMAIN-REGISTER-v1.md) | DOM-ZPM-01 |
| Wave 2B / 2B ZPM / 3B / 3B ZPM / 4B / 4B ZPM / 5B / 6A | Relationship registers | REL-* |

---

*ATLAS Integrity Snapshot Register v1 — audit only.*
