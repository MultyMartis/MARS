# FP-0002 — Source / Production Authority v1

**Wave:** PROD-P04-FU02  
**Date:** 2026-08-14  
**Canonical narrative:** `WORDPRESS/SOURCE-AUTHORITY.md`  
**This file:** operational access-contour binding. Does not replace SOURCE-AUTHORITY.md. Does not rewrite Stable v1 history.

---

## Dual authority (post-reimport)

| Surface | Role |
|---------|------|
| `WORDPRESS/` (theme, `shpigovsky-core`, ACF JSON/PHP) | **CODE / SOURCE AUTHORITY** |
| Beget live host `http://shpigovsky.beget.tech/` (docroot `…/shpigovsky.ru/public_html`) | **LIVE RUNTIME TRUTH** |
| **Current** Beget WordPress DB (operator re-import) | **LIVE CONTENT / ADMIN AUTHORITY** |
| PROD-P04 / PROD-P04-FU01 DB + FS manifests | **HISTORICAL PRE-REIMPORT BASELINE** |
| `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` | **DEV / ACCEPTED REFERENCE** — must not automatically overwrite production |
| `shpigovsky.ru` DNS | **NOT Beget authority** until DNS cutover |

### Critical preservation rule

```text
NO OLD DB RESTORE OR LOCAL DB OVERWRITE WITHOUT EXPLICIT OPERATOR APPROVAL
CURRENT BEGET DB = LIVE CONTENT / ADMIN AUTHORITY
```

The imported DB intentionally contains desired demo/content edits. Do **not** restore prior production DB values merely because they differ.

### Filesystem parity status (PROD-P04-FU02)

```text
POST-REIMPORT FULL PRODUCT FILESYSTEM SHA BASELINE = ESTABLISHED
REIMPORT PRODUCT CODE PARITY CLEAN
```

Theme + `shpigovsky-core` + `wp-content/acf-json` SHA baseline recomputed.  
Authority hierarchy is **unchanged** — proven read does **not** authorize write or blind sync.

---

## Reconciliation rule (filesystem)

For PHP/CSS/JS/theme/plugin source:

```text
FETCH CURRENT PROD → HASH → DIFF → BACKUP EXACT PROD FILE
→ RECONCILE (preserve legitimate production drift into source)
→ EDIT SOURCE → EXACT UPLOAD → VERIFY REMOTE → QA → ROLLBACK READY
```

Never:

- upload entire theme blindly;
- mirror local WordPress root;
- overwrite `uploads`;
- broad sync / `robocopy /MIR`;
- use stale source without fetch;
- deploy from dirty `X:\AI MARS`;
- restore old production DB over the imported live DB without explicit operator approval.

Use exact allowlists only.

---

## Content / Admin rule

Prefer WP Admin (or proven WPilot capability) for:

- page/post content;
- ACF **values** where DB-owned;
- menus;
- media;
- forms;
- SEO metadata;
- plugin settings;
- redirects where plugin-owned.

Do not use filesystem or raw DB merely because credentials exist.

If a value has a source-controlled representation, **canonize back into `WORDPRESS/`**.

---

## Database rule

**Current** production DB is live admin/content authority.

- SELECT/read allowed after access validation.  
- Writes forbidden until explicit task.  
- No SQL edits as substitute for WP Admin where a native authoring surface exists.  
- Schema writes require full DB backup.  
- Prior PROD-P04 counts/content inventory are **historical evidence only**.

---

## Evidence

* Current: `REPORTS/evidence/prod-p04-fu02-post-reimport-rebaseline/`
* Historical FU01: `REPORTS/evidence/prod-p04-fu01-filesystem-baseline/`

---

*Source/Production Authority v1 · PROD-P04-FU02 · no secrets.*
