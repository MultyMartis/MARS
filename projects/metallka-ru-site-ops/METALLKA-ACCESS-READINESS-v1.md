# METALLKA — Access Readiness v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** COMPLETE (Phase 2B0 — local access bootstrap)  
**Date:** 2026-07-26  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`  
**Site:** `https://metallka.ru/`  

**Purpose:** Record **non-secret** operator intake and local access-contour readiness for later Gate A / Phase 2B production read-only discovery.

```text
This document does NOT authorize write operations.
Gate A authorizes read-only discovery only.
Credentials must NOT appear in this file, in reports, or in chat.
```

Related:

- [METALLKA-ACCESS-INTAKE-REQUIREMENTS-v1.md](METALLKA-ACCESS-INTAKE-REQUIREMENTS-v1.md)
- [METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md](METALLKA-PRODUCTION-READ-ONLY-DISCOVERY-CHARTER-v1.md)
- [METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md](METALLKA-EVIDENCE-AND-REDACTION-RULES-v1.md)
- [METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md](METALLKA-READ-ONLY-STOP-CONDITIONS-v1.md)
- Local policy: `projects/wpilot/local-storage-policy.md`

---

## 1. Gate A approval

| Field | Value |
|-------|-------|
| **Gate A** | **APPROVED** |
| **Exact approval** | `APPROVE METALLKA GATE A — PRODUCTION READ-ONLY DISCOVERY` |
| **Authorizes** | Production **read-only** discovery only |
| **Does NOT authorize** | Writes; WPilot install; WPilot token; bridge; REST smoke; backup creation; cache purge; production mutation |

Phase 2B0 prepared the **local-only** access contour. Phase 2B production read-only discovery was **executed 2026-07-26** after operator confirmed local secrets were filled.

---

## 2. Operator intake (non-secret, confirmed)

| Item | Status |
|------|--------|
| **Hosting provider** | Beget — **OPERATOR CONFIRMED** |
| **Hosting panel** | AVAILABLE — **OPERATOR CONFIRMED** |
| **WP Admin** | AVAILABLE — **OPERATOR CONFIRMED** |
| **SSH** | AVAILABLE — **OPERATOR CONFIRMED** |
| **FTP** | AVAILABLE — **OPERATOR CONFIRMED** |
| **Staging/dev** | NONE — **OPERATOR CONFIRMED** |
| **Staging requirement** | **NOT REQUIRED** BY OPERATOR FOR CURRENT SITE OPS MODEL |
| **Hosting backup** | AVAILABLE |
| **Hosting restore** | AVAILABLE |
| **External Git/source/archive** | NOT AVAILABLE / NOT KNOWN |
| **Current source authority** | PRODUCTION RUNTIME — **PROVISIONAL** |

---

## 3. Local access contour

| Item | Path / note |
|------|-------------|
| **Local root** | `X:\AI MARS\local\sites\metallka-ru-production\` |
| **Non-secret profile** | `site-profile.json` |
| **Secret template** | `secrets.local.md` (operator manual fill; placeholders only at bootstrap) |
| **WPilot token file** | **NOT CREATED** — not authorized at this stage |
| **Git boundary** | Covered by root `.gitignore` rule `/local/` |

Filenames follow the accepted ISEO / WPilot local site pattern: `site-profile.json` + `secrets.local.md`.

Credential population (Phase 2B): **WP Admin / SSH / FTP / DB fields filled** in local secrets. **Beget panel fields still incomplete** (placeholders). Values never copied into tracked docs.

Phase 2B discovery executed 2026-07-26 — see passport / REPORT.

---

## 4. Preferred future discovery order (Gate A)

1. Public browser / HTTP inspection  
2. Beget panel **read-only** metadata  
3. WordPress Admin **read-only** inspection  
4. SSH **read-only** filesystem inspection  
5. FTP **only if** SSH is insufficient  
6. Database access **only if** specific unanswered discovery questions require it  

**Reason:** SSH provides a stronger read-only filesystem inspection surface than FTP when available. FTP must not be used merely because credentials exist. **No write operations** through SSH or FTP.

---

## 5. SSH safety model (future Gate A — do not connect in 2B0)

### Allowed (read-only examples)

- `pwd`, `ls`, bounded `find`, `stat`, `file`, `du`
- read-only grep/search
- `php --version`
- `wp --info` if WP-CLI exists; `wp core version`
- `wp option get` for **explicitly approved non-secret** options
- `wp theme list`, `wp plugin list`
- `wp post list` with bounded fields
- checksums / hash commands
- `cat` / `head` / `sed` **only** on non-secret files

### Forbidden

- `rm`, `mv`, `cp` into production, `touch`, `mkdir`, `chmod`, `chown`
- `sed -i`, redirects `>`
- package managers
- `wp plugin` activate / deactivate / install / update / delete
- `wp theme` activate / install / update / delete
- `wp option` update / delete / add
- `wp post` update / delete / create
- mutating `wp db query`, `wp search-replace`
- cache flush, cron execution
- shell scripts with unknown side effects

### Special protection

**DO NOT** output contents of `wp-config.php`.  
Limited sanitized metadata from it may be allowed later **only if strictly needed**; secrets must never enter logs, reports, or chat.

---

## 6. WordPress Admin safety model (future Gate A)

### Allowed

- Dashboard inspection; WordPress version; Site Health read-only information
- Themes / plugins inventory; page/post lists
- Edit screens **without saving**
- WPBakery structure inspection; menu inspection without save
- The7 settings inspection without save
- Form / ACF configuration inspection without save
- User role **class** confirmation without exposing unnecessary PII

### Forbidden

- Save / Update / Publish
- Activate / Deactivate / Install / Update
- Regenerate assets; purge cache
- Create users; edit profile; change settings
- Run migration / setup wizards

If opening an admin page may **automatically mutate** configuration: **STOP** and document it.

---

## 7. Beget panel safety model (future Gate A)

### Allowed (read-only)

- Identify PHP version; domains / site binding; directory / docroot mapping
- Backup availability; restore UI existence
- SSH / FTP service metadata
- DB names / instances **without** credential exposure
- Cron inventory; logs availability; SSL / site mapping
- Resource / runtime metadata

### Forbidden

- Change PHP; restore backup; create backup unless separately approved
- Modify domains; create / delete FTP / SSH users; reset passwords
- Edit DNS; edit cron; edit DB; change SSL; modify files

---

## 8. Authorization boundaries (explicit)

| Class | Authorized now? |
|-------|-----------------|
| Local contour create / document | **YES** (Phase 2B0) |
| Operator fill of local secrets | **PENDING** (operator) |
| Gate A read-only discovery (Phase 2B) | **EXECUTED** (2026-07-26) — read-only only |
| WPilot install / token / bridge | **NO** |
| Writes / smoke / backup creation | **NO** |
| Local mirror | **DEFER** |

---

*METALLKA Access Readiness v1 · Phase 2B discovery EXECUTED · Gate A read-only · Beget panel secrets still incomplete · writes NOT AUTHORIZED.*
