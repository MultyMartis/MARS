# REPORT — METALLKA SITE OPS PHASE 2B PRODUCTION READ-ONLY DISCOVERY

**Task:** METALLKA-SITE-OPS — PHASE 2B PRODUCTION READ-ONLY DISCOVERY  
**Date:** 2026-07-26  
**Gate:** `APPROVE METALLKA GATE A — PRODUCTION READ-ONLY DISCOVERY` — executed  
**Canonical locus:** `X:\AI MARS\projects\metallka-ru-site-ops\`

---

## 1. Status

**COMPLETE — PRODUCTION READ-ONLY DISCOVERY COMPLETE**

Partial only for Beget **panel UI** inspection (local panel credential fields still placeholders). Hosting facts otherwise established via SSH + public HTTP + operator intake.

---

## 2. Environment

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD (closeout) | `e18c537d65c4c8c6ba2767201bccaad7248287c4` |
| Staged by task | **empty** |
| Foreign WIP | **present — preserved / untouched** |
| Secrets file | Git-ignored; read process-locally only; **not** printed |

---

## 3. Production Identity

| Field | Value |
|-------|-------|
| Domain | `https://metallka.ru/` (apex canonical) |
| Hosting | **Beget** |
| Docroot | `/home/[REDACTED]/[REDACTED]/metallka.ru/public_html` |
| Webserver | `nginx-reuseport/1.21.1` |
| PHP (HTTP) | **8.3.20** |
| WordPress | **7.0.2** |
| Multisite | No |
| Language | `ru_RU` |
| Permalinks | `/%postname%/` |

---

## 4. Theme Stack

| Item | Value |
|------|-------|
| Parent | The7 `dt-the7` **11.6.0.1** |
| Child | `dt-the7-child` (`the7dtchild`) **1.0.0** |
| Options | `the7dtchild` option array (~956 keys) |
| Source authority | **PROVISIONAL** production runtime; no `.git`; WSP markers in child |

---

## 5. Plugin Stack

Material active: WPBakery 6.10.0, Ultimate VC Addons, RevSlider 6.6.7, CF7 + Honeypot + CFDB7, Popup Maker, Rank Math, Clearfy, Shortcoder, Media File Renamer, Duplicate Page/Menu, Classic Widgets, Advanced Database Cleaner, css-versioning, UnderConstruction (active but site publicly live).

Inactive material: Fast Velocity Minify, Rank Math Pro.  
ACF / Code Snippets / SMTP plugin / WPilot: **absent**.

---

## 6. WPBakery Findings

- Essentially all inspected pages use WPBakery (`_wpb_vc_js_status=true`).
- Storage: classic shortcodes in `post_content`.
- `vc_raw_html`: present on home, contacts, requisites, and heavily on service pages (≈7 each).
- Simple text pages (About, cookie, privacy) use `vc_column_text` without `vc_raw_html`.
- The7 `dt_*` elements on services / mentions.

---

## 7. The7 Ownership

| Surface | Owner |
|---------|-------|
| Header / nav placement | THE7 THEME OPTION + WP menus (`primary` / `mobile`) |
| Footer | THE7 + child `footer.php` / `sidebar-footer.php` (+ Shortcoder contacts) |
| Theme Options | Option `the7dtchild` |
| Generated CSS | `uploads/the7-css/` |
| Page bodies | WPBAKERY |

---

## 8. Page Inventory

Front page ID 2. Services hub 77 with children 86/87/88. About 52. Contacts 41. Legal set 3/30/31/353. Blog page 27. Draft/pending extras present. Full table in `METALLKA-PAGE-INVENTORY-v1.md`.

---

## 9. Forms

CF7 forms 80, 81, 101, 290–292. Honeypot + CFDB7. No dedicated SMTP plugin. No CRM plugin evidenced. Do not submit.

---

## 10. ACF / Custom Data

**ACF NOT PRESENT.** Schema authority N/A. Custom reusable content via Shortcoder + Popup Maker + CF7.

---

## 11. Custom Code

Child: `functions.php`, `style.css` (WSP Fixes), `footer.php`, `sidebar-footer.php`, masked JS. Plugin `css-versioning`. Standard `.htaccess`. No MU plugins. No production `.git`.

---

## 12. Cache Stack

Clearfy active. No `advanced-cache.php` / `object-cache.php`. Leftover `cache/fvm` + `cache/wmac`. The7 + WPBakery upload asset caches. No Cloudflare evidenced.

---

## 13. Backup / Restore

| Item | Value |
|------|-------|
| BACKUP AVAILABLE | **YES** |
| RESTORE AVAILABLE | **YES** |
| RESTORE PROCEDURE UNDERSTOOD | **PARTIAL** |

Beget hosting-native; panel UI not opened this wave.

---

## 14. Source Authority

Production filesystem = **PROVISIONAL SOURCE AUTHORITY**.  
DB/admin content authoritative for pages/menus/forms/options.  
External Git/archive = none known.

---

## 15. WPilot Presence

**ABSENT** — no directory, options, tables, or REST namespace. No ghosts.

---

## 16. WPilot Compatibility

**CONDITIONALLY COMPATIBLE**

RC6 zip SHA-256 re-verified **MATCH**. No hard install blocker. Conditions: separate install charter, backup proof, keep bridge/write off; CORS caveat for browser `X-WPilot-Token` (server clients likely fine).

---

## 17. SAFE UNKNOWN Resolution

| Metric | Count |
|--------|-------|
| Before | 44 UNKNOWN |
| RESOLVED | 33 |
| PARTIAL | 10 |
| STILL UNKNOWN | 1 (SU-40 licenses) |

---

## 18. Protected Zones

Globals remain protected (header/footer/Theme Options/forms/`vc_raw_html`/child PHP). Several zones now **MAPPED** but **not** write-authorized. Lowest-risk candidate: About page 52 text block.

---

## 19. Local Mirror Decision

**DEFER**

---

## 20. First Safe Development Task

**Exactly one recommendation (do not execute):**

Edit a small text string inside the single `vc_column_text` on page **ID 52** (`/about/`) — no `vc_raw_html`, no forms, no URL/template/header/footer/global block changes.

---

## 21. Operational Readiness

| Track | Decision |
|-------|----------|
| Site Ops normal admin/file work | **READY FOR BOUNDED TASKS** |
| WPilot installation | **CONDITIONALLY READY** |
| WPilot bridge / read-smoke | **NOT AUTHORIZED** |
| WPilot write | **BLOCKED** |

---

## 22. Production Mutations

**NONE** (intentional).

Incidental: WP-CLI may create cache under the site on first use; follow-up used `WP_CLI_CACHE_DIR=/tmp/...`. No content/config saves, uploads, plugin/theme changes, cache purges, backups, DB writes, or WPilot REST.

Validation checklist: uploads 0 · WP saves 0 · plugin/theme changes 0 · cache purge 0 · backups triggered 0 · DB writes 0 · WPilot REST 0 · tokens 0 · bridge changes 0 · files uploaded 0 · git staged by task 0 · secrets in REPORT 0.

---

## 23. Files Created / Modified

**Created**

- `projects/metallka-ru-site-ops/METALLKA-SITE-PASSPORT-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-ACCESS-MODEL-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-WP-ENTITY-MAP-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-THE7-WPBAKERY-MAP-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-PAGE-INVENTORY-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-PLUGIN-INVENTORY-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-FORM-MAP-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-CUSTOM-CODE-MAP-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-CACHE-MAP-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-BACKUP-ROLLBACK-MODEL-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-WPILOT-COMPATIBILITY-ASSESSMENT-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-LOCAL-MIRROR-DECISION-v1.md`
- `projects/metallka-ru-site-ops/reports/REPORT-METALLKA-SITE-OPS-PHASE-2B-PRODUCTION-READ-ONLY-DISCOVERY.md`

**Modified**

- `projects/metallka-ru-site-ops/METALLKA-SAFE-UNKNOWN-REGISTER-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-PROTECTED-ZONES-v1.md`
- `projects/metallka-ru-site-ops/METALLKA-ARTIFACT-REGISTER-v1.md`
- `projects/metallka-ru-site-ops/OPERATIONAL-INDEX.md`
- `projects/metallka-ru-site-ops/METALLKA-ACCESS-READINESS-v1.md`

**Storage evidence (untracked bulk):** `X:\AI MARS STORAGE\wpilot\evidence\metallka-ru-site-ops\phase-2b-discovery\`

---

## 24. Git Operations

**NONE** (no stage / commit / push)

---

## 25. Risks

- Service pages dense with `vc_raw_html` — high edit risk.
- Child footer legal links are hard-coded — global blast radius.
- Clearfy + leftover minify caches — unexpected front performance behavior if touched.
- UnderConstruction plugin active — verify before maintenance experiments.
- Beget panel secrets incomplete — weakens backup UI proof until filled.
- WPBakery major update available (6.10 → 8.x) — **do not** update casually.

---

## 26. Next Recommended Phase

**PHASE 3A — BOUNDED SITE OPS TASK PREPARATION**

(Alternate if operator prioritizes tooling: PHASE 3B — WPILOT INSTALLATION CHARTER.)

Do **not** auto-start.

---

## 27. Stop Condition

**STOP after REPORT.**

No Phase 3 execution in this wave.
