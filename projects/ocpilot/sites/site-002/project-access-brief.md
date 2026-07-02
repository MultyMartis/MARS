# Project Access Brief

**Site ID:** SITE-002  
**Status:** **PRODUCTION PARTIAL CAPTURE — BASELINE PENDING**
**Run:** 4.171 — SITE-002 First Read-Only Production Capture (2026-07-02)

**Do not record:** passwords, tokens, credentials, secret URLs, or live `config.php` values.

External credentials: `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md`

Production profile: [production-profile.md](production-profile.md)

---

## Site Identity

| Field | Value |
|-------|-------|
| Site ID | SITE-002 |
| Project name | ЗПМ / BZPM |
| Production URL | https://bzpm.ru/ |
| Historical TEST URL | https://zpm.new-site.space/ |
| Current operational environment | **PRODUCTION** |
| Platform | ocStore / OpenCart |
| Version | SAFE UNKNOWN |
| Production Profile | [production-profile.md](production-profile.md) |

---

## Environments

### site-002-test (historical TEST)

| Field | Value |
|-------|-------|
| Environment ID | `site-002-test` |
| Environment type | TEST (historical) |
| URL | https://zpm.new-site.space/ |
| Role | Previous implementation and verification environment; preserved as historical evidence |
| Credential source | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md` |
| Credential section | `TEST` |
| Connection status | Used during TEST-era OCPilot runs — not current operational authority |
| Write status | **DISABLED** unless explicitly re-authorized for TEST maintenance |
| Database | **EXCLUDED BY DEFAULT** |

### site-002-prod (Production)

| Field | Value |
|-------|-------|
| Environment ID | `site-002-prod` |
| Environment type | **PRODUCTION** |
| URL | https://bzpm.ru/ |
| Role | Current operational website authority |
| Credential source | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md` |
| Credential section | `PRODUCTION` |
| Connection status | **PARTIAL** — HTTP 200 + admin read-only PASS; FTP auth FAIL |
| Write status | **DISABLED UNTIL FIRST PRODUCTION OPERATION IS AUTHORIZED** |
| Database | **EXCLUDED BY DEFAULT** |

---

## Access Inventory (summary)

| Access type | TEST | Production | Credential location |
|-------------|------|------------|---------------------|
| FTP / SFTP | Populated in secrets | **AUTH FAIL** — operator verify Beget credentials | External secrets file — `TEST` / `PRODUCTION` sections |
| Hosting panel | Partial in secrets | **PENDING** | External secrets file |
| SSH | Populated in secrets (TEST) | **PENDING** | External secrets file |
| OpenCart admin | Populated in secrets (TEST) | **PENDING** | External secrets file |
| Database | Populated in secrets (TEST) | **PENDING** | External secrets file — **NOT AUTHORIZED BY DEFAULT** |
| DNS / Domain | SAFE UNKNOWN | **PENDING** | External secrets file |

Full inventory details remain in the external secrets file only. This brief contains **no secret values**.

---

## Credential Storage Rule

**No credentials in repository.**

Credentials may be stored only outside the repo:

- `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md`
- Operator password manager

This file may only contain references such as:

- `Stored in operator password manager`
- `Stored in external secrets folder`
- `Provided manually during supervised session`

---

## Operation Permissions

**Production writes:** **NOT AUTHORIZED** at registration.

Checklist — operator sets before any supervised Production access run:

- [ ] Read-only file inspection allowed
- [ ] Read-only DB inspection allowed *(requires explicit authorization — excluded by default)*
- [ ] Admin panel read-only inspection allowed
- [ ] File edits allowed
- [ ] DB edits allowed
- [ ] Product import allowed
- [ ] Theme edits allowed
- [ ] Controller/model edits allowed

**Write permissions** require backup confirmed, rollback path confirmed, and operator approval — **not satisfied** for Production at registration.

---

## Backup Status

| Field | TEST | Production |
|-------|------|------------|
| File backup status | Operator attestation (Beget) — TEST-era | **PENDING** — FTP blocked at Run 4.171 |
| Database backup status | SAFE UNKNOWN | **NOT AUTHORIZED BY DEFAULT** |
| Backup location | External storage / hosting — TEST-era | `production\backups\` (future) |
| Restore method | Beget full backup + file-level pass backups (TEST-era) | **PENDING** Production baseline |

---

## Allowed Operations

None authorized for Production at registration. TEST-era operations remain historical evidence only.

---

## Forbidden Operations

Default forbidden (see [templates/project-access-brief-template.md](../../templates/project-access-brief-template.md)):

- Destructive SQL
- Live production edits without explicit Production operation charter
- Credential commits
- `config.php` exposure
- Mass delete/move
- Blind import
- Controller edits without rollback

Site-specific at Production registration:

- Production FTP/SFTP/SSH connection until explicitly authorized
- Production deploy until first Production operation is authorized
- Database operations on Production unless separately authorized

---

## Run 5 Readiness

| Gate | Value |
|------|-------|
| **Run 5 allowed** | **NO** — Production profile registration does not authorize Run 5 on Production |

---

## Notes

- Passport: [site-passport.md](site-passport.md)
- Production profile: [production-profile.md](production-profile.md)
- Registry: [project-site-registry.md](../../project-site-registry.md)
- Run 4.170: Production environment registered — **no remote connection performed**

---

## Business Goal

Primary Goal:
Operational Production website for ЗПМ / BZPM at https://bzpm.ru/, managed under OCPilot with human-supervised change control.

Historical TEST at https://zpm.new-site.space/ served as the implementation and verification environment before Production transfer.

---

## Project Priority

Current Phase:

* [ ] INTAKE
* [ ] AUDIT
* [ ] PLANNING
* [x] EXECUTION (TEST history complete)
* [ ] QA
* [ ] FROZEN

Current State:

**PRODUCTION PARTIAL CAPTURE** — Run 4.171 HTTP/admin read-only complete; FTP credential fix required before file baseline.

---

## Environment Classification

| Environment | Type | OCPilot writes |
|-------------|------|----------------|
| site-002-test | Historical TEST | **NO** (unless explicitly re-authorized) |
| site-002-prod | **PRODUCTION** | **NO** until first Production operation authorized |

Required conditions for future Production writes:

* [ ] Backup confirmed
* [ ] Rollback confirmed
* [ ] Operator approval confirmed
