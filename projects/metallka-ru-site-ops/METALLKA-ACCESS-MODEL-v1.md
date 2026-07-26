# METALLKA — Access Model v1

**Programme:** METALLKA-RU-SITE-OPS  
**Status:** POPULATED — Phase 2B  
**Date:** 2026-07-26  
**Authorization now:** **READ-ONLY discovery only** (Gate A)  
**Secrets location class:** `X:\AI MARS\local\sites\metallka-ru-production\secrets.local.md` (Git-ignored `/local/`)

```text
No secret values in this document.
```

---

## Access classes

| Class | Available? | Purpose | Technical R/W | MARS authorization now | Secret location class | Preferred usage | Restrictions |
|-------|------------|---------|---------------|------------------------|----------------------|-----------------|--------------|
| Public HTTP | **YES** | Surface / REST inventory | Read | Gate A allowed | N/A | First / always | No vuln scan, no brute force, no mass crawl |
| Beget panel | **OPERATOR YES** / agent **PARTIAL** | PHP selector, SSL, backup UI, domain map | Panel can write | Gate A read-only | Local secrets — **panel fields still placeholder** | After secrets filled | No PHP change, backup create/restore, DNS/SSL edits |
| WP Admin | **YES** (creds filled) | Themes/plugins/pages UI | Admin can write | Gate A read-only (no saves) | Local secrets | When WP-CLI insufficient | No save/activate/update/purge |
| SSH | **YES** (creds filled) | Filesystem + WP-CLI read | Shell can write | Gate A read-only | Local secrets | Preferred filesystem channel | No mutating shell/WP-CLI; set `WP_CLI_CACHE_DIR` outside docroot |
| FTP | **YES** (creds filled) | Filesystem fallback | Can write | Gate A — **only if SSH insufficient** | Local secrets | Avoid if SSH works | Read-only listing/download only |
| Database / phpMyAdmin | **YES** (fields filled) | Schema / options | Can write | Gate A — **not used** this wave | Local secrets | Only if unanswered Qs | No writes; redaction mandatory |
| WPilot REST | **N/A** (not installed) | Bridge | N/A | **NOT AUTHORIZED** | N/A | Do not invoke | No token/bridge/smoke |

---

## Discovery channel actually used (Phase 2B)

1. Public HTTPS / REST  
2. SSH + WP-CLI (read-only commands; cache redirected to `/tmp` on follow-up)  
3. Beget panel UI — **skipped** (local panel credentials incomplete)  
4. WP Admin browser — **not required** (WP-CLI covered inventory)  
5. FTP — **not used** (SSH sufficient)  
6. DB panel — **not opened**

---

## Incidental note

Initial WP-CLI use may create a cache directory under the site tree. Follow-up commands used `WP_CLI_CACHE_DIR=/tmp/...`. No intentional content/config mutation was performed.

---

*Access Model v1 · Gate A read-only.*
