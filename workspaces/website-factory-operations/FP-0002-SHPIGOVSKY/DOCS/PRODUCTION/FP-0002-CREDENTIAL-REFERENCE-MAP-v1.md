# FP-0002 — Credential Reference Map v1

**Wave:** PROD-P05-FU01  
**Date:** 2026-08-14  
**Validation date:** 2026-08-14  
**Rule:** Paths, classes, status, consumers — **NO secret values**.

---

## Status vocabulary

| Status | Meaning |
|--------|---------|
| `MISSING` | File/class not created / still placeholder |
| `OPERATOR_FILL_REQUIRED` | Template exists; operator must enter values locally |
| `PRESENT_UNVERIFIED` | Operator reports filled; connectivity not proven |
| `VERIFIED` | Gate proved access without printing secrets |
| `INVALID` | Present but cannot be used as filled (wrong target / auth fail / incomplete) |
| `REMOVED / OBSOLETE` | Prior credential/account/jail retired; do not use |
| `DEFERRED` | Intentionally not created or not used this wave |
| `HISTORICAL` | Prior baseline retained as evidence only |

---

## Map

| Credential class | Local-only secret file | Safe metadata file | Consumer | Rotation owner | Current status | Last validation | Allowed operations now |
|------------------|------------------------|--------------------|----------|----------------|----------------|-----------------|------------------------|
| Beget control panel | `secrets.local.md` → BEGET CONTROL PANEL | `site-profile.json` | Operator (manual) | Operator | **MISSING** (optional) | 2026-08-14 | None by agent |
| Filesystem FTP | `secrets.local.md` → FTP OR SFTP | `site-profile.json` | Operator / Cursor tool-mediated | Operator | **VERIFIED** — real `shpigovsky.ru/public_html` | 2026-08-14 FU01 | READ proven. WRITE closed |
| Filesystem SSH | `secrets.local.md` → SSH | `site-profile.json` | Same + **SSH_LOCAL_MYSQL tunnel** | Operator | **VERIFIED** | 2026-08-14 FU01 | READ proven. SSH tunnel SELECT allowed. WRITE closed |
| Prior FTP/SSH jail (`beget.tech` placeholder) | historical note only | this map | none | Operator | **REMOVED / OBSOLETE** | 2026-08-13 | Do not use |
| Database | `secrets.local.md` → DATABASE | Passport / this map | Operator / Cursor-mediated READ | Operator | **VERIFIED** SSH-local SELECT on **post-reimport** DB | 2026-08-14 FU01 | SELECT only. WRITE closed. **Do not restore prior DB without operator approval** |
| WordPress Admin | `secrets.local.md` → WORDPRESS ADMIN | `site-profile.json` | Operator; bounded Admin inspection | Operator | **VERIFIED** — HTTP login **PASS**; `mars` Administrator | 2026-08-14 FU01 | WRITE task-specific only |
| WPilot token | `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` | `site-profile.json` → `wpilot.token_file_path` | WPilot / MARS read client | Operator | **VERIFIED** — local file present (gitignored); authenticated READ **PROVEN**; WRITE disabled | 2026-08-14 FU01 | Authenticated GET only until a write charter |
| Historical local DEV WPilot token | `X:\AI MARS\local\tokens\wpilot-local-shpigovsky.token` | WPilot OPERATIONAL-INDEX | Local `shpigovsky.test` history | Operator | **NOT PRODUCTION AUTHORITY** | n/a | **Do not reuse** |
| SMTP / analytics / CRM / webhooks | `secrets.local.md` → OPTIONAL FUTURE | N/A | None now | Operator | **MISSING** | 2026-08-14 | Not requested |

Tracked value in git for every row above: **NO**.

---

## File inventory (local-only)

| Path | Role | Git |
|------|------|-----|
| `X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md` | **ONE operator fill file** | ignored `/local/` |
| `X:\AI MARS\local\sites\shpigovsky-production\site-profile.json` | Non-secret metadata + path refs | ignored `/local/` |
| `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` | Production WPilot plaintext token — **present, gitignored** | ignored `/local/` |

---

## Operator notes (no values in chat)

* Filesystem + SSH-local DB: **VERIFIED**.
* WordPress Admin: FU01 HTTP login **PASS**.
* WPilot: production token stored locally; authenticated READ **PROVEN**; write remains **disabled**.
* Current post-reimport Beget files+DB backup: **OPERATOR CONFIRMED**.

---

*Credential Reference Map v1 · PROD-P05-FU01 PASS · no secrets.*
