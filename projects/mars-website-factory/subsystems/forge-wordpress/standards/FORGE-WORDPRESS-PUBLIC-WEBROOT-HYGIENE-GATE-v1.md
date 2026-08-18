# Forge WordPress — Public Webroot Hygiene Gate v1

**ID:** FW-S-20  
**Status:** ACTIVE — CANONICAL SECURITY GATE  
**Date:** 2026-08-18  
**Class:** C / G  
**Evidence:** FP-0002 P17-FU02 `mars-runtime/` incident

---

## 1. Incident (anonymized)

A leftover local-runtime folder remained in the **public** WordPress docroot. A **GET** request to an obsolete populate/migration PHP script **mutated live WordPress objects** (stub pages and menu items). Objects had to be rolled back.

```text
NEVER probe unknown public PHP migration scripts with GET merely to discover behavior.
Inspect source first.
```

---

## 2. Canonical rules

- Migration, diagnostic, bootstrap, populate, seed runners **must not** remain executable in public webroot after use.
- Prefer: delete; or move outside docroot; or deny by server config **and** still delete when possible.
- Do not commit runners that are designed to run via HTTP.
- Pre-launch **public webroot audit** is mandatory.

**Remove or relocate before launch:**

| Class | Examples |
|-------|----------|
| Logs | `debug.log`, public `*.log` |
| Dumps | `*.sql`, `*.sql.gz`, DB exports |
| Archives | random `*.zip` / `*.tar` of backups |
| Runners | `populate-*.php`, `migrate-*.php`, `mars-runtime/` |
| Temp imports | `_tmp-*`, unpack folders |
| Backups | copies of `wp-config`, uploads dumps |
| phpinfo | `info.php`, `phpinfo.php` |
| Obsolete scripts | old `app/` scaffolds, `.bak` media |

---

## 3. Gate

**PUBLIC WEBROOT PRE-CUTOVER HYGIENE = PASS** is required before NS/domain cutover.

Procedure: list docroot; classify; snapshot; remove allowlisted junk; confirm mutating URLs 404; do not recursive-delete unknown trees without charter.

---

*FW-S-20 v1.*
