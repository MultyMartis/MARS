# Project Access Brief

**Site ID:** SITE-002  
**Status:** **REGISTRATION ONLY** — no supervised access authorized  
**Run:** 4.113 — SITE-002 Registration (2026-06-09)

**Do not record:** passwords, tokens, credentials, secret URLs, or live `config.php` values.

External credentials (when operator places them): `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\`

---

## Site Identity

| Field | Value |
|-------|-------|
| Site ID | SITE-002 |
| Project name | ЗПМ |
| Public URL | SAFE UNKNOWN |
| Test or Dev URL | https://zpm.new-site.space/ |
| Admin URL | SAFE UNKNOWN |
| Environment | TEST |
| Platform | ocStore / OpenCart |
| Version | SAFE UNKNOWN |
| Baseline candidate | SAFE UNKNOWN |

---

## Access Inventory

| Access type | Available YES/NO | Location of credentials | Allowed use | Restrictions | SAFE UNKNOWN |
|-------------|------------------|-------------------------|-------------|--------------|--------------|
| Hosting panel | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | Not in registration scope |
| FTP / SFTP | **PENDING** | Stored in external secrets folder *(when supplied)* | SAFE UNKNOWN | SAFE UNKNOWN | Credentials not yet provided |
| SSH | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | Not in registration scope |
| phpMyAdmin | **PENDING** | Stored in external secrets folder *(when supplied)* | SAFE UNKNOWN | SAFE UNKNOWN | Credentials not yet provided |
| OpenCart admin | **PENDING** | Stored in external secrets folder *(when supplied)* | SAFE UNKNOWN | SAFE UNKNOWN | Credentials not yet provided |
| Database credentials | **PENDING** | Stored in external secrets folder *(when supplied)* | SAFE UNKNOWN | SAFE UNKNOWN | Via phpMyAdmin channel |
| Domain / DNS | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |
| Email / SMTP | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | Not in registration scope |
| Backup panel | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | SAFE UNKNOWN | |

---

## Credential Storage Rule

**No credentials in repository.**

Credentials may be stored only outside the repo, for example:

- `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\`
- Operator password manager

This file may only contain references such as:

- `Stored in operator password manager`
- `Stored in external secrets folder`
- `Provided manually during supervised session`

---

## Operation Permissions

Checklist — operator sets before any supervised access run:

- [ ] Read-only file inspection allowed
- [ ] Read-only DB inspection allowed
- [ ] Admin panel read-only inspection allowed
- [ ] File edits allowed
- [ ] DB edits allowed
- [ ] Product import allowed
- [ ] Theme edits allowed
- [ ] Controller/model edits allowed

**Write permissions** require backup confirmed, rollback path confirmed, and operator approval — **not satisfied** at registration.

---

## Backup Status

| Field | Value |
|-------|-------|
| File backup status | SAFE UNKNOWN |
| Database backup status | SAFE UNKNOWN |
| Backup location | SAFE UNKNOWN |
| Backup date | SAFE UNKNOWN |
| Backup verification status | SAFE UNKNOWN |
| Restore method | SAFE UNKNOWN |
| SAFE UNKNOWN | All backup facts pending first operator session |

---

## Allowed Operations

None authorized at registration. Container and access placeholders only.

---

## Forbidden Operations

Default forbidden (see [templates/project-access-brief-template.md](../../templates/project-access-brief-template.md)):

- Destructive SQL
- Live production edits
- Credential commits
- `config.php` exposure
- Mass delete/move
- Blind import
- Controller edits without rollback

Site-specific at registration:

- FTP scan, discovery, audit, or site modifications until intake and charter complete

---

## Run 5 Readiness

- [x] Site identity known
- [ ] Version known
- [ ] Baseline selected
- [ ] Access inventory complete (credential locations)
- [ ] Backup status known
- [ ] Read-only scope approved
- [x] SAFE UNKNOWN recorded

| Gate | Value |
|------|-------|
| **Run 5 allowed** | **NO** |

---

## Notes

- Passport: [site-passport.md](site-passport.md)
- Registry: [project-site-registry.md](../../project-site-registry.md)
- Run 4.113: container only — no invented hosting or access details

---

## Business Goal

Primary Goal:
Рабочая тестовая площадка для аудита и внедрения изменений PDP / Catalog UX на OpenCart / ocStore.

Planned Work:

* [ ] Technical audit
* [ ] PDP UX changes
* [ ] Catalog UX changes
* [ ] Theme changes
* [ ] OpenCart development
* [ ] SEO optimization
* [ ] Other

Description:

TEST environment at `https://zpm.new-site.space/` — operator-supplied registration fact.

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
* [ ] EXECUTION
* [ ] QA
* [ ] FROZEN

Current State:

**AWAITING INTAKE** — registration complete; credentials and intake materials pending.

---

## Environment Classification

Environment Type:

* [x] TEST
* [ ] DEV
* [ ] STAGING
* [ ] PROD

May OCPilot perform write operations here?

* [ ] YES
* [x] NO

If YES:

Required conditions:

* [ ] Backup confirmed
* [ ] Rollback confirmed
* [ ] Operator approval confirmed

Notes:

No write operations until operator charter and access brief updated.
