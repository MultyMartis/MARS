# Project Access Brief

**Purpose:** Sanitized access inventory and operation permissions for Cursor/OCPilot.  
**Do not record:** passwords, tokens, credentials, secret URLs, or live `config.php` values.

Copy to `projects/ocpilot/sites/<site-id>/project-access-brief.md` per site.  
External credentials (if any): `C:\AI MARS STORAGE\ocpilot\project-sites\<site-id>\secrets\` — see [Credential Storage Rule](#credential-storage-rule).

---

## Site Identity

| Field | Value |
|-------|-------|
| Site ID | |
| Project name | |
| Public URL | |
| Test URL | |
| Admin URL | |
| Environment | test / staging / production / SAFE UNKNOWN |
| Platform | OpenCart / ocStore / SAFE UNKNOWN |
| Version | |
| Baseline candidate | e.g. `ocstore-3038-rs2` / `ocstore-3039-rs1` / SAFE UNKNOWN |

---

## Access Inventory

| Access type | Available YES/NO | Location of credentials | Allowed use | Restrictions | SAFE UNKNOWN |
|-------------|------------------|-------------------------|-------------|--------------|--------------|
| Hosting panel | | | | | |
| FTP / SFTP | | | | | |
| SSH | | | | | |
| phpMyAdmin | | | | | |
| OpenCart admin | | | | | |
| Database credentials | | | | | |
| Domain / DNS | | | | | |
| Email / SMTP | | | | | |
| Backup panel | | | | | |

**Location of credentials** — references only, for example:

- `Stored in operator password manager`
- `Stored in external secrets folder`
- `Provided manually during supervised session`
- `Not available` / `SAFE UNKNOWN`

---

## Credential Storage Rule

**No credentials in repository.**

Credentials may be stored only outside the repo, for example:

- `C:\AI MARS STORAGE\ocpilot\project-sites\<site-id>\secrets\`
- Operator password manager (org policy)

The repo file may only contain references such as:

- `Stored in operator password manager`
- `Stored in external secrets folder`
- `Provided manually during supervised session`

Never commit passwords, API keys, DB passwords, session cookies, SSH keys, or URLs that embed secrets.

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

**Write permissions** (file edits, DB edits, product import, theme edits, controller/model edits) require **all** of:

1. **Backup confirmed** — file and/or DB per scope
2. **Rollback path confirmed** — see site rollback plan / external backups
3. **Operator approval** — explicit for this task and environment

Read-only permissions still require operator approval and target/environment confirmation per [access-and-safety.md](../access-and-safety.md).

---

## Backup Status

| Field | Value |
|-------|-------|
| File backup status | yes / no / SAFE UNKNOWN |
| Database backup status | yes / no / SAFE UNKNOWN |
| Backup location | external label only — no secret paths with credentials |
| Backup date | |
| Restore method | summary only |
| SAFE UNKNOWN | list open backup unknowns |

---

## Allowed Operations

List operations explicitly approved for the current charter (read-only audit, specific file paths, etc.):

- 

---

## Forbidden Operations

Default forbidden unless explicit human charter overrides:

- Destructive SQL (DROP, TRUNCATE, mass DELETE without approval)
- Live production edits without approval
- Credential commits to git
- `config.php` exposure (copy with live secrets into repo)
- Mass delete/move without inventory and backup
- Blind import (unreviewed catalog/theme packages)
- Controller/model edits without rollback path confirmed

Add site-specific forbidden items:

- 

---

## Run 5 Readiness

Checklist — **First Read-Only Site Audit** gate:

- [ ] Site identity known
- [ ] Version known
- [ ] Baseline selected
- [ ] Access inventory complete
- [ ] Backup status known
- [ ] Read-only scope approved
- [ ] SAFE UNKNOWN recorded

| Gate | Value |
|------|-------|
| **Run 5 allowed** | YES / NO |

Set **YES** only when all checklist items above are satisfied **and** [intake-readiness-review.md](../intake-readiness-review.md) checklist is all **YES**.

---

## Notes

- 
- Related: [site-passport.md](../sites/_template-site/site-passport.md) (per-site copy), [access-and-safety.md](../access-and-safety.md), [shared/external-access-patterns/](../../../shared/external-access-patterns/README.md)
