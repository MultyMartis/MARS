# ATLAS Backup Snapshot v1

**Status:** **documented** — point-in-time Atlas registry state capture (documentation only).  
**Program:** ATLAS — Business Reality Registry  
**Snapshot date:** 2026-06-07  
**Trigger:** Pre-population checkpoint — Organization rename ORG-0005 (BZPM → ЗПМ) + ZPM slice documentation sync (Waves 2–5).  
**Parent:** [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md) · [ATLAS-BACKUP-AND-RESTORE-PROCEDURE-v1.md](ATLAS-BACKUP-AND-RESTORE-PROCEDURE-v1.md)  
**Is not:** runtime export, database dump, automated backup artifact, git commit.

---

## 1. Snapshot summary

| Entity class | Total attested / in scope | **active** | **deprecated** | **proposed** |
|--------------|---------------------------|------------|------------------|--------------|
| **Organization** | 6 | **6** | 0 | 0 |
| **Legal entity** | 5 | **5** | 0 | 0 |
| **Person** | 15 | **15** | 0 | 0 |
| **Relationship** | 45 | **45** | 0 | 0 |
| **Project** | 8 | **6** | **2** | 0 |
| **Website** | 5 *(Wave 4 scope)* | **5** | 0 | 0 |
| **Domain** | 5 *(Wave 5 scope)* | **5** | 0 | 0 |

**Deferred (not in attested counts):** WEB-0001..0005 operator sites; Person edges for PER-0002, PER-0003; ORG-0006 Project / Website / Domain / commercial edges; Wave 5B ZPM PRIMARY_DOMAIN / Domain OWNS; Wave 6 ZPM CLIENT_OF.

**ZPM slice (ORG-0005):** ORG-0005, PER-0014, PER-0015, PRJ-0009, PRJ-0010, WEB-ZPM-01, DOM-ZPM-01; REL-ZPM-01, 02, REL-ZPM-PJ-01..04, REL-ZPM-WB-01, 03, 04 — **included** in counts above. WEB-ZPM-02 **not minted**; REL-ZPM-WB-02 **cancelled**.

**Source registers:** Wave 1 dataset + Wave 1B/1C active attestation + Wave 2..6A population registers (documentation-level aggregation).

---

## 2. Organizations — active

| org_id | canonical_name | wave_tier | business_role | legal_entity_id | lifecycle |
|--------|----------------|-----------|---------------|-----------------|-----------|
| ORG-0001 | Веб-студия «Полигон» | W1-A | operator | LE-0001 | **active** |
| ORG-0002 | Агентство «МетаКод» | W1-A | operator | LE-0001 *(shared IP context)* | **active** |
| ORG-0003 | i-SEO Studio | W1-A | operator | LE-0002 | **active** |
| ORG-0004 | Триумф | W1-B | CLIENT | LE-0003 | **active** |
| ORG-0005 | **ЗПМ** | W1-B | CLIENT | LE-0004 | **active** |
| ORG-0006 | SIBCAR | W1-C | CLIENT | LE-0005 | **active** |

**Note ORG-0005:** Canonical renamed from **BZPM** on 2026-06-07 per [ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md](ATLAS-WAVE1B-BZPM-ORGANIZATION-RENAME-v1.md). **BZPM** retained as **former** alias.

---

## 3. Legal entities — active

| legal_entity_id | legal_entity_name | entity_type | inn | kpp | ogrn_ogrnip | org_binding | lifecycle |
|-----------------|-------------------|-------------|-----|-----|-------------|-------------|-----------|
| LE-0001 | ИП Русецкий А. А. | ИП | *(Wave 1 dataset)* | — | *(Wave 1 dataset)* | ORG-0001 | **active** |
| LE-0002 | ИП Шваков Н. А. | ИП | *(Wave 1 dataset)* | — | *(Wave 1 dataset)* | ORG-0003 | **active** |
| LE-0003 | Общество с ограниченной ответственностью «Триумф» | ООО | *(Wave 1 dataset / EV-0005)* | *(EV-0005)* | *(EV-0005)* | ORG-0004 | **active** |
| LE-0004 | Общество с ограниченной ответственностью «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | ООО | 2221237587 | 222101001 | 1172225049787 | ORG-0005 | **active** |
| LE-0005 | Общество с ограниченной ответственностью «СибКар» | ООО | 5405512542 | 540501001 | 1265400004220 | ORG-0006 | **active** |

---

## 4. Persons — active

| person_id | canonical_name | primary_organization | lifecycle |
|-----------|----------------|---------------------|-----------|
| PER-0001 | Русецкий Андрей Анатольевич | ORG-0001 Полигон | **active** |
| PER-0002 | Фатюткин Сергей Игоревич | **SAFE UNKNOWN** | **active** |
| PER-0003 | Лиматов Роман Курбанович | **SAFE UNKNOWN** | **active** |
| PER-0004 | Макарова Алеся Леонидовна | ORG-0004 Триумф | **active** |
| PER-0005 | Подзолков Максим | ORG-0004 Триумф | **active** |
| PER-0006 | Вагин Иван Владимирович | ORG-0004 Триумф | **active** |
| PER-0007 | Беслангурова Тамила | ORG-0003 i-SEO Studio | **active** |
| PER-0008 | Денис Леонов | ORG-0003 i-SEO Studio | **active** |
| PER-0009 | Антон Кораблёв | ORG-0003 i-SEO Studio | **active** |
| PER-0010 | Дягилева Ольга | ORG-0003 i-SEO Studio | **active** |
| PER-0011 | Шваков Никита Алексеевич | ORG-0003 i-SEO Studio | **active** |
| PER-0012 | Илья Гуренков | ORG-0003 i-SEO Studio | **active** |
| PER-0013 | Иван Корольков | ORG-0003 i-SEO Studio | **active** |
| PER-0014 | Алексей Владимирович Дубинский | ORG-0005 ЗПМ | **active** |
| PER-0015 | Крюков Александр Сергеевич | ORG-0005 ЗПМ | **active** |

---

## 5. Relationships — active (by family)

| Family | Count | relationship_ids | register source |
|--------|-------|------------------|-----------------|
| Person → Organization | **14** | REL-0001, 0002, 0006..0015; REL-ZPM-01, 02 | [ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-RELATIONSHIP-REGISTER-v1.md) · [ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE2B-ZPM-RELATIONSHIP-REGISTER-v1.md) |
| Project ↔ Organization | **14** | REL-0017..0026; REL-ZPM-PJ-01..04 | [ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-PROJECT-RELATIONSHIP-REGISTER-v1.md) · [ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE3B-ZPM-PROJECT-RELATIONSHIP-REGISTER-v1.md) |
| Website ↔ Project / Org | **12** | REL-0027..0035; REL-ZPM-WB-01, 03, 04 | [ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-WEBSITE-RELATIONSHIP-REGISTER-v1.md) · [ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE4B-ZPM-WEBSITE-RELATIONSHIP-REGISTER-v1.md) |
| Domain → Website | **4** | REL-0036..0039 *(Wave 5B roster)* | [ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE5B-DOMAIN-RELATIONSHIP-REGISTER-v1.md) |
| Organization ↔ Organization (commercial) | **1** | REL-0016 | [ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md](ATLAS-WAVE6A-COMMERCIAL-RELATIONSHIP-REGISTER-v1.md) |
| **Total** | **45** | REL-0001..0039 + REL-ZPM-* *(gaps intentional)* | — |

---

## 6. Projects — active and deprecated

| project_id | canonical_name | lifecycle | commissioning_org | execution_org |
|------------|----------------|-----------|-------------------|---------------|
| PRJ-0001 | MARS | **active** | **SAFE UNKNOWN** | ORG-0002 MetaCode |
| PRJ-0004 | Редизайн gktriumph.ru | **deprecated** | ORG-0004 Триумф | ORG-0001 Полигон |
| PRJ-0005 | Грузотакси | **active** | ORG-0004 Триумф | ORG-0001 Полигон |
| PRJ-0006 | SEO gktriumph.ru | **active** | ORG-0004 Триумф | ORG-0001 Полигон |
| PRJ-0007 | Блог gktriumph.ru | **active** | ORG-0004 Триумф | ORG-0001 Полигон |
| PRJ-0008 | Манипулятор | **active** | ORG-0004 Триумф | ORG-0001 Полигон |
| PRJ-0009 | Каталог-платформа bzpm.ru | **active** | ORG-0005 ЗПМ | ORG-0001 Полигон |
| PRJ-0010 | Сайт bzpm.ru (исходная версия) | **deprecated** | ORG-0005 ЗПМ | ORG-0001 Полигон |

---

## 7. Websites — active

| website_id | canonical_name | url | primary_org | lifecycle |
|------------|----------------|-----|-------------|-----------|
| WEB-0006 | gktriumph.ru | `https://gktriumph.ru` | ORG-0004 Триумф | **active** |
| WEB-0007 | blog.gktriumph.ru | `https://blog.gktriumph.ru` | ORG-0004 Триумф | **active** |
| WEB-0008 | gruzotaxi-triumph.ru | `https://gruzotaxi-triumph.ru` | ORG-0004 Триумф | **active** |
| WEB-0009 | manipulator-triumph.ru | `https://manipulator-triumph.ru` | ORG-0004 Триумф | **active** |
| WEB-ZPM-01 | bzpm.ru | `https://bzpm.ru` | ORG-0005 ЗПМ | **active** |

---

## 8. Domains — active

| domain_id | canonical_name | primary_org_candidate | primary_website | lifecycle |
|-----------|----------------|----------------------|-----------------|-----------|
| DOM-0001 | gktriumph.ru | ORG-0004 Триумф | WEB-0006 | **active** |
| DOM-0002 | blog.gktriumph.ru | ORG-0004 Триумф | WEB-0007 | **active** |
| DOM-0003 | gruzotaxi-triumph.ru | ORG-0004 Триумф | WEB-0008 | **active** |
| DOM-0004 | manipulator-triumph.ru | ORG-0004 Триумф | WEB-0009 | **active** |
| DOM-ZPM-01 | bzpm.ru | ORG-0005 ЗПМ | WEB-ZPM-01 | **active** |

---

## 9. ORG-0005 alias state at snapshot

| alias | role | state |
|-------|------|-------|
| BZPM | former / abbreviation | **active** |
| Завод Пищевого Машиностроения | trade | **active** |
| ООО ЗПМ | legal / abbreviation | **active** |
| ООО «ЗАВОД ПИЩЕВОГО МАШИНОСТРОЕНИЯ» | legal | **active** |

**Primary contact:** PER-0014 — attested Wave 2B ZPM (REL-ZPM-02).

---

## 10. ZPM slice — entity and relationship roster

| Class | ID | canonical_name | lifecycle | attestation |
|-------|-----|----------------|-----------|-------------|
| Organization | ORG-0005 | **ЗПМ** | **active** | AT-W1B-01; RN-W1B-01 |
| Person | PER-0014 | Алексей Владимирович Дубинский | **active** | AT-W2-ZPM-02 |
| Person | PER-0015 | Крюков Александр Сергеевич | **active** | AT-W2-ZPM-01 |
| Project | PRJ-0009 | Каталог-платформа bzpm.ru | **active** | AT-W3-ZPM-01 |
| Project | PRJ-0010 | Сайт bzpm.ru (исходная версия) | **deprecated** | AT-W3-ZPM-02 |
| Website | WEB-ZPM-01 | bzpm.ru | **active** | AT-W4-ZPM-01 |
| Domain | DOM-ZPM-01 | bzpm.ru | **active** | AT-W5-ZPM-01 |

| relationship_id | source | target | type | lifecycle |
|-----------------|--------|--------|------|-----------|
| REL-ZPM-01 | PER-0015 | ORG-0005 | GENERAL_DIRECTOR | **active** |
| REL-ZPM-02 | PER-0014 | ORG-0005 | REPRESENTATIVE | **active** |
| REL-ZPM-PJ-01 | PRJ-0009 | ORG-0005 | COMMISSIONED_BY | **active** |
| REL-ZPM-PJ-02 | ORG-0001 | PRJ-0009 | EXECUTES | **active** |
| REL-ZPM-PJ-03 | PRJ-0010 | ORG-0005 | COMMISSIONED_BY | **active** |
| REL-ZPM-PJ-04 | ORG-0001 | PRJ-0010 | EXECUTES | **active** |
| REL-ZPM-WB-01 | WEB-ZPM-01 | PRJ-0009 | BELONGS_TO | **active** |
| REL-ZPM-WB-03 | WEB-ZPM-01 | PRJ-0010 | BELONGS_TO | **active** |
| REL-ZPM-WB-04 | ORG-0005 | WEB-ZPM-01 | OWNS | **active** |

**Retired / cancelled:** WEB-ZPM-02 *(not minted)*; REL-ZPM-WB-02 *(cancelled — COR-ZPM-WEB-06)*.

---

## 11. Repository and storage pointers

| Location | Role at snapshot |
|----------|------------------|
| `C:\AI MARS\projects\atlas\` | Git-tracked foundation + population + audit documentation |
| `C:\AI MARS STORAGE\atlas\evidence\counterparty-cards\` | External CC evidence (8 org folders + README) |

See [ATLAS-BACKUP-AND-RESTORE-PROCEDURE-v1.md](ATLAS-BACKUP-AND-RESTORE-PROCEDURE-v1.md) for backup scope and restore sequence.

---

*ATLAS Backup Snapshot v1 — documentation only; ZPM slice synced 2026-06-07.*
