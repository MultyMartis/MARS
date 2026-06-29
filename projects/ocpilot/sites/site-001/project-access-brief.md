# Project Access Brief

**Site ID:** SITE-001  
**Status:** **W1 WRITE CHARTER ACTIVE** — TEST-only supervised writes authorized; **PRODUCTION WRITES FORBIDDEN**  
**Run:** 4.101 — W1A pre-execution authorization package (2026-06-08)

**Do not record:** passwords, tokens, credentials, secret URLs, or live `config.php` values.

External credentials (if operator places them): `X:\AI MARS STORAGE\ocpilot\project-sites\site-001\secrets\`

---

## Site Identity

| Field | Value |
|-------|-------|
| Site ID | SITE-001 |
| Project name | Автосалон СИБКАР |
| Public URL | SAFE UNKNOWN |
| Test or Dev URL | https://sibcar.new-site.space/ |
| Admin URL | SAFE UNKNOWN |
| Environment | TEST |
| Platform | ocStore |
| Version | 3.0.3.8 (rs.2) |
| Baseline candidate | ocstore-3038-rs2 |

---

## Access Inventory

| Access type | Available YES/NO | Location of credentials | Allowed use | Restrictions | SAFE UNKNOWN |
|-------------|------------------|-------------------------|-------------|--------------|--------------|
| Hosting panel | YES | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | All channels unconfirmed |
| FTP / SFTP | YES | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| SSH | YES | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| phpMyAdmin | YES | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| OpenCart admin | YES | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| Database credentials | YES | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| Domain / DNS | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| Email / SMTP | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| Backup panel | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |

---

## Credential Storage Rule

**No credentials in repository.**

Credentials may be stored only outside the repo, for example:

- `X:\AI MARS STORAGE\ocpilot\project-sites\site-001\secrets\`
- Operator password manager

This file may only contain references such as:

- `Stored in operator password manager`
- `Stored in external secrets folder`
- `Provided manually during supervised session`

---

## Operation Permissions

**Scope:** **SITE-001 TEST ONLY** — `https://sibcar.new-site.space/`

**Write approver (HITL):** **Андрей**

- [x] Read-only file inspection allowed
- [x] Read-only DB inspection allowed
- [x] Admin panel read-only inspection allowed
- [x] File edits allowed *(TEST only)*
- [x] DB edits allowed *(TEST only)*
- [ ] Product import allowed
- [x] Theme edits allowed *(TEST only)*
- [ ] Controller/model edits allowed

| Permission | TEST | Notes |
|------------|------|-------|
| **Admin writes** | **YES** | W1A Store Settings and subsequent admin waves |
| **Theme writes** | **YES** | W1B+; FTP/SFTP on TEST only |
| **File writes** | **YES** | TEST filesystem only |

**PRODUCTION WRITES FORBIDDEN** — no edits on production host, DNS, or live domain without separate authorization.

Write permissions require: backup confirmed, rollback path confirmed, operator approval — **satisfied for W1A** (2026-06-08).

---

## Backup Status

| Field | Value |
|-------|-------|
| File backup status | **YES** — operator confirmed 2026-06-08 |
| Database backup status | **YES** — operator confirmed 2026-06-08 |
| Backup location | Beget backup system |
| Backup date | **2026-06-08** (pre-W1A; supersedes 2026-05-31 planning reference) |
| Backup verification status | **Operator-confirmed** — files + database backup created; archive filenames not recorded |
| Restore method | Beget restore |
| SAFE UNKNOWN | Credential storage locations for access channels; independent restore drill |

---

## Allowed Operations

Supervised W1 brand replacement on **TEST** per [reports/SITE-001-W1-WRITE-CHARTER-v1.md](reports/SITE-001-W1-WRITE-CHARTER-v1.md). Current wave authorization: **W1A** — [reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md](reports/SITE-001-W1A-AUTHORIZATION-REVIEW-v1.md).

---

## Forbidden Operations

Default forbidden (see [templates/project-access-brief-template.md](../../templates/project-access-brief-template.md)):

- Destructive SQL
- **Live production edits** — **PRODUCTION WRITES FORBIDDEN**
- Credential commits
- `config.php` exposure
- Mass delete/move
- Blind import
- Controller edits without rollback

---

## Run 5 Readiness

- [x] Site identity known
- [x] Version known
- [x] Baseline selected
- [ ] Access inventory complete (credential locations)
- [x] Backup status known
- [ ] Read-only scope approved
- [x] SAFE UNKNOWN recorded

| Gate | Value |
|------|-------|
| **Run 5 allowed** | **YES** *(read-only audit — execution paused)* |
| **W1 writes allowed (TEST)** | **YES** — approver **Андрей**; charter active |

---

## Notes

- Passport: [site-passport.md](site-passport.md)
- Registry: [project-site-registry.md](../../project-site-registry.md)
- Run 4: container only — no URLs or access details invented

---

## Business Goal

Primary Goal:
Перебрендирование готового автосалона под нового клиента. Загрузка автомобилей в каталог. Подготовка сайта к SEO-продвижению и запуску рекламных кампаний Яндекс Директ. Использование проекта как первого боевого пилота OCPilot для отработки процессов аудита, сравнения с baseline и последующих изменений OpenCart.

Planned Work:

* [x] Rebranding
* [x] New dealership launch
* [x] Vehicle catalog import
* [x] SEO optimization
* [x] Yandex Direct launch
* [x] Design changes
* [x] Theme changes
* [x] OpenCart development
* [ ] Custom module development
* [x] Technical audit
* [ ] Other

Description:

SAFE UNKNOWN

---

## Project Priority

Priority:

* [ ] LOW
* [ ] MEDIUM
* [ ] HIGH
* [ ] CRITICAL

Current Phase:

* [x] INTAKE
* [ ] AUDIT
* [ ] PLANNING
* [x] EXECUTION
* [ ] QA
* [ ] FROZEN

Current State:

W1 WRITE CHARTER ACTIVE — W1A authorized on TEST; **PRODUCTION WRITES FORBIDDEN**

---

## Environment Classification

Environment Type:

* [x] TEST
* [ ] DEV
* [ ] STAGING
* [ ] PROD

May OCPilot perform write operations here?

* [x] YES *(TEST only — SITE-001 TEST ONLY)*
* [ ] NO

If YES:

Required conditions:

* [x] Backup confirmed *(2026-06-08 — operator)*
* [x] Rollback confirmed
* [x] Operator approval confirmed *(approver: Андрей)*

Notes:

**PRODUCTION WRITES FORBIDDEN.** Writes limited to TEST URL and W1 charter scope.
