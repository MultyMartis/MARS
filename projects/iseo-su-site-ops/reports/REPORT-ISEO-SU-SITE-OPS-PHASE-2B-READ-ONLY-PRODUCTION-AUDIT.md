# REPORT — ISEO-SU SITE OPS PHASE 2B READ-ONLY PRODUCTION AUDIT

**Task ID:** ISEO-SU-SITE-OPS-PHASE-2B-ACCESS-REVIEW-AND-READ-ONLY-PRODUCTION-AUDIT  
**Date:** 2026-07-24  
**Final status:** **PHASE 2B — COMPLETE / READ-ONLY PRODUCTION ARCHITECTURE CAPTURED**  
**Canonical locus:** `X:\AI MARS\projects\iseo-su-site-ops\`

---

## 1. Execution Summary

Operator-authorized read-only production audit of `https://i-seo.su/` completed after Beget backup confirmation and local access validation. SFTP inventory established a **hybrid root WordPress + physical PHP-capable HTML** architecture. Public REST and bounded public page GETs classified live routes. WordPress Admin UI via non-browser HTTP client hit a JS challenge shell (residual Admin-only gap). No production writes, no DB access, no WPilot install, no secrets recorded in Git docs.

---

## 2. Environment Preflight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS` |
| Volume | `X:` / **AI WS** |
| Branch | `mars/canonical-post-recovery` |
| HEAD (at task) | `04cd01d1881bccf6fc0dfeebef5b891e378fef37` |
| Upstream | `origin/mars/canonical-post-recovery` |
| Ahead / behind | ahead 14 / behind 60 (foreign to this task) |
| Staged | empty |
| Foreign WIP | present — **preserved** |

---

## 3. Backup Confirmation

Operator attestation received:

`BEGET BACKUP CONFIRMED — full hosting backup created for ISEO-SU-SITE-OPS PHASE 2B on 2026-07-24`

External access proceeded only after this confirmation.

---

## 4. Local Access Presence Review

| Item | Result |
|------|--------|
| `secrets.local.md` | exists, Git-ignored |
| `site-profile.json` | exists, Git-ignored |
| FTP/SFTP required fields | non-empty |
| Protocol signal | SFTP (port 22) |
| WordPress admin fields | non-empty |
| Dedicated MARS WP account | yes |
| Beget panel fields | optional; panel host class `cp.beget.com` |
| Secrets printed | **No** |

**STOP — REQUIRED LOCAL ACCESS CLASS INCOMPLETE** was **not** triggered.

---

## 5. External Access Performed

| Channel | Action | Mutation? |
|---------|--------|-----------|
| SFTP | Directory listings; bounded file reads | **No** |
| Public HTTPS GET | Sample pages for ownership classification | **No** |
| Public `/wp-json/` | Site/types/taxonomies/pages/posts | **No** |
| WordPress Admin HTTP | Login attempt + GET admin screens | **No saves**; UI returned JS challenge shell |
| phpMyAdmin | **Not opened** | — |
| Database | **Not accessed** | — |
| WPilot | **Not installed / not called** | — |

---

## 6. Hosting and Filesystem Findings

- Hosting: Beget; SFTP to sanitized docroot `/home/[REDACTED]/[REDACTED]/i-seo.su/public_html`
- WordPress **root install** co-located with marketing files
- `.htaccess`: HTTPS, www→apex, Bytespider block, **HTML executed as PHP**, standard WP rewrite
- Shared assets: `css/`, `js/`, `img/`, `fonts/`, `libs/`
- Large static trees: `services/`, `cases/`, `report-hub/`
- No on-server `package.json` / `gulpfile` / `src` / `scss`
- Form handlers: many `*__FORM.php` (root + service copies)

Details: [ISEO-SU-REMOTE-FILESYSTEM-INVENTORY-v1.md](../ISEO-SU-REMOTE-FILESYSTEM-INVENTORY-v1.md)

---

## 7. WordPress Findings

| Item | Value |
|------|-------|
| Version | **7.0.2** |
| Theme | `iseoblog` (sole; not child; non-standard style header) |
| Front | Page `glavnaya` + template `page-home.php` |
| Blog | `/blog/` WordPress-rendered |
| CPT | `offer` |
| Plugins on disk | ACF PRO 6.3.10, Yoast 28.0, Jetpack 14.8, WP-Optimize 4.5.5, Akismet, others |
| WPilot | **Absent** |
| ACF JSON | Not found |
| WP_DEBUG | `true` |
| PHP runtime | **SAFE UNKNOWN** (required ≥ 7.4) |
| Admin UI | JS challenge via HTTP client — gap |

Details: [ISEO-SU-WORDPRESS-INVENTORY-v1.md](../ISEO-SU-WORDPRESS-INVENTORY-v1.md)

---

## 8. Hybrid Boundary

Homepage `/` is **SHARED_BUT_WORDPRESS_RENDERED** (WP template with static-like markup). Marketing `.html` trees are **STATIC_FILE_OWNED** (PHP-capable). Blog is **WORDPRESS_OWNED**. Shared CSS/JS are shared static assets. Dual artifacts (`home.html`, `blog.html`) create drift risk.

Details: [ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md](../ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md)

---

## 9. Custom Tools

| Tool | Finding |
|------|---------|
| SEO calculator | Confirmed — `js/common.js` + `calc__FORM.php` + theme/WP tariff page |
| Tariff cards | Confirmed — static + theme parts + `tariff_*__FORM.php` |
| Forms/mail | Confirmed — multiple `*__FORM.php` (emails not recorded) |
| Web-KP | **SAFE UNKNOWN** — candidates `/offers` + CPT `offer` |
| Report Hub | `report-hub/` static HTML app on production |

---

## 10. Source-of-Truth Findings

Production is the only confirmed runtime source location. No Git/build tree on server. Dual homepage/blog files and duplicated form handlers are primary drift risks. Matrix: [ISEO-SU-HYBRID-SOURCE-OF-TRUTH-MATRIX-v1.md](../ISEO-SU-HYBRID-SOURCE-OF-TRUTH-MATRIX-v1.md)

---

## 11. WPilot Pre-install Inputs

Captured in [ISEO-SU-WPILOT-PREINSTALL-INPUTS-v1.md](../ISEO-SU-WPILOT-PREINSTALL-INPUTS-v1.md).  
**Not an install approval.** WPilot absent; WP 7.0.2; custom theme; Jetpack/Yoast/WP-Optimize present; Admin automation challenge noted; staging absent; backup confirmed for this session.

---

## 12. Database Access Decision

- phpMyAdmin URL was recorded as metadata only (`https://mayday.beget.com/phpMyAdmin/`);
- phpMyAdmin was **not** opened;
- DB credentials were **not** copied from `wp-config.php`;
- direct DB access was **not** required;
- any future DB access requires a **separate explicit charter**.

Database credential source (reference only): production `wp-config.php`  
Database access: **NOT AUTHORIZED / NOT REQUIRED FOR CURRENT AUDIT**

---

## 13. Files Created or Updated

**Created:**

- `ISEO-SU-READ-ONLY-PRODUCTION-AUDIT-v1.md`
- `ISEO-SU-REMOTE-FILESYSTEM-INVENTORY-v1.md`
- `ISEO-SU-WORDPRESS-INVENTORY-v1.md`
- `ISEO-SU-STATIC-WP-BOUNDARY-MAP-v1.md`
- `ISEO-SU-HYBRID-SOURCE-OF-TRUTH-MATRIX-v1.md`
- `ISEO-SU-PROTECTED-ZONES-v1.md`
- `ISEO-SU-WPILOT-PREINSTALL-INPUTS-v1.md`
- `reports/REPORT-ISEO-SU-SITE-OPS-PHASE-2B-READ-ONLY-PRODUCTION-AUDIT.md`

**Updated:**

- `ISEO-SU-SITE-EVIDENCE-INTAKE-v1.md`
- `ISEO-SU-PUBLIC-ROUTE-REGISTER-v1.md`
- `ISEO-SU-SITE-OPS-SAFE-UNKNOWN-REGISTER-v1.md`
- `ISEO-SU-SITE-OPS-ARTIFACT-REGISTER-v1.md`
- `ISEO-SU-ACCESS-CLASSIFICATION-v1.md`
- `OPERATIONAL-INDEX.md`

Local scratch under `_phase2b-scratch/` (gitignored) held transient audit helpers — not programme authority.

---

## 14. Validation

| Check | Result |
|-------|--------|
| No remote mutations | **Pass** |
| No WordPress forms saved | **Pass** |
| No plugins/themes/core changed | **Pass** |
| No database access | **Pass** |
| No secret values in reports | **Pass** (intended) |
| No local secrets printed | **Pass** |
| Tracked writes under `projects/iseo-su-site-ops/` | **Pass** |
| No Storage / Localhost writes | **Pass** |
| Registry / ATLAS / WPilot source / Report Hub / infrastructure unchanged | **Pass** |
| Staged diff empty | **Pass** (expected) |
| Foreign WIP preserved | **Pass** |

---

## 15. Risks

1. Dual homepage (`page-home.php` vs `home.html`) and dual blog file.
2. Duplicated `*__FORM.php` trees.
3. `WP_DEBUG` true + `debug.log` present.
4. HTML-as-PHP expands include/injection surface.
5. Admin automation blocked — incomplete Admin-only inventory.
6. WPilot cannot cover static HTML/form handlers.
7. Branch ahead/behind remote (unrelated foreign state).

---

## 16. SAFE UNKNOWN

PHP runtime version; exact plugin actives; ACF field UI; menus/widgets; web-KP naming; SMTP path details; restore drill proof; maintained external SoT (U-022). See SAFE UNKNOWN register.

---

## 17. Git and Foreign WIP

- No stage / commit / push performed.
- Scoped status expected: modified/new files only under `projects/iseo-su-site-ops/`.
- Large foreign WIP elsewhere in the repo left untouched.

---

## 18. Recommended Next Gate

**B. ISEO-SU-SITE-OPS — PHASE 4B WPILOT PREINSTALL PACKAGE AND COMPATIBILITY GATE**

Architecture and compatibility inputs are sufficient to draft the preinstall package. Do **not** install WPilot in that gate until operator approval.

Optional: Phase 2C only if operator wants Admin-UI gap closure first (PHP version, plugin actives, ACF UI, confirm web-KP URL).

---

## 19. Required Operator Review

1. Accept Phase 2B architecture capture.
2. Confirm whether `/offers` + CPT `offer` is the “web-KP” tool (or name the real URL).
3. Decide 4B now vs optional 2C Admin HITL first.
4. Re-confirm Beget backup before any future production session.

---

## 20. Stop Condition

Satisfied:

- no production write;
- no file upload;
- no WordPress save;
- no database login;
- no plugin installation/activation;
- no token creation;
- no WPilot REST smoke;
- no cache purge;
- no Localhost / ATLAS / registry mutation;
- no Git stage/commit/push;
- waiting for operator review.

---

*REPORT — Phase 2B · 2026-07-24 · secrets excluded.*
