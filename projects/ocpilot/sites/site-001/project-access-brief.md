# Project Access Brief

**Site ID:** SITE-001  
**Status:** **INTAKE IN PROGRESS** — identity/version recorded, access and backup gates pending before Run 5  
**Run:** 4.5 — repository-only intake completion update

**Do not record:** passwords, tokens, credentials, secret URLs, or live `config.php` values.

External credentials (if operator places them): `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\secrets\`

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

- `C:\AI MARS STORAGE\ocpilot\project-sites\site-001\secrets\`
- Operator password manager

This file may only contain references such as:

- `Stored in operator password manager`
- `Stored in external secrets folder`
- `Provided manually during supervised session`

---

## Operation Permissions

- [x] Read-only file inspection allowed
- [x] Read-only DB inspection allowed
- [x] Admin panel read-only inspection allowed
- [ ] File edits allowed
- [ ] DB edits allowed
- [ ] Product import allowed
- [ ] Theme edits allowed
- [ ] Controller/model edits allowed

Write permissions require: backup confirmed, rollback path confirmed, operator approval.

---

## Backup Status

| Field | Value |
|-------|-------|
| File backup status | YES |
| Database backup status | YES |
| Backup location | Beget backup system |
| Backup date | 31.05.2026 |
| Restore method | Beget restore |
| SAFE UNKNOWN | No backup facts supplied in Run 4 |

---

## Allowed Operations

None chartered. Run 5 not approved.

---

## Forbidden Operations

Default forbidden (see [templates/project-access-brief-template.md](../../templates/project-access-brief-template.md)):

- Destructive SQL
- Live production edits without approval
- Credential commits
- `config.php` exposure
- Mass delete/move
- Blind import
- Controller edits without rollback

Until intake completes: **all** FTP, PMA, admin, and site modification operations forbidden.

---

## Run 5 Readiness

- [x] Site identity known
- [x] Version known
- [x] Baseline selected
- [ ] Access inventory complete
- [ ] Backup status known
- [ ] Read-only scope approved
- [x] SAFE UNKNOWN recorded

| Gate | Value |
|------|-------|
| **Run 5 allowed** | **NO** |

Operator must complete this brief and satisfy [intake-readiness-review.md](../../intake-readiness-review.md) before setting **YES**.

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

* [ ] INTAKE
* [ ] AUDIT
* [ ] PLANNING
* [ ] EXECUTION
* [ ] QA
* [ ] FROZEN

Current State:

INTAKE

---

## Environment Classification

Environment Type:

* [ ] TEST
* [ ] DEV
* [ ] STAGING
* [ ] PROD

May OCPilot perform write operations here?

* [ ] YES
* [ ] NO

If YES:

Required conditions:

* Backup confirmed
* Rollback confirmed
* Operator approval confirmed

Notes:

SAFE UNKNOWN
