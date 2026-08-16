# REPORT — FP-0002 PROD-P01 Beget Read-Only Onboarding

**Date:** 2026-08-13  
**Factory project:** FP-0002 — Шпиговский  
**Scope:** Post-migration Beget identity, authority model, public smoke, A01 survival, WPilot package reconciliation, install readiness — **no production mutation**

---

## 1. Status

| Item | Result |
|------|--------|
| Wave status | **PARTIAL** |
| Production mutations | **0** |
| DB writes | **0** |
| WP Admin writes | **0** |
| WPilot installed by this wave | **No** (already present from migration — see §13–14) |
| Commit / push | **None** |

### Why PARTIAL (not PASS / not BLOCKED)

- Beget host reachable; core routes healthy; A01 Program + Comfort publicly verified; theme CSS/JS public hashes match source.  
- Residual migration defects: hardcoded `http://shpigovsky.test/...` CTA links; site title still «локальная разработка»; HTTPS on beget.tech not usable from probe; WPilot already live with **non-safe** public posture (`bridge_enabled=true`, `dev_confirmed=true`, `token-generated`); production WPilot **version** not publicly knowable.  
- Not BLOCKED: inspection possible; site is clearly the migrated Shpigovsky V9 stack; WPilot package authority reconciled from repo.

---

## 2. Production Identity

| Item | Value |
|------|-------|
| Working host | `http://shpigovsky.beget.tech/` |
| Final domain | `shpigovsky.ru` |
| DNS | **`DNS_CUTOVER = DEFERRED`** (still old hosting) |
| Provider | Beget |
| Backup | **`BACKUP CONFIRMED BY OPERATOR`** (files + DB post-migration) |

Passport: `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`

---

## 3. Public Production Health

| Check | Result |
|-------|--------|
| `/` and major IA routes | **200** |
| Invalid route | **404** (theme 404) |
| HTTP→HTTPS | Not forced on working host |
| HTTPS `https://shpigovsky.beget.tech/` | Probe **timeout / unavailable** this wave |
| Server | nginx-reuseport/1.21.1 |
| PHP | 8.3.20 |
| Assets (theme CSS/JS/vendor/images) | Load; key hashes match source |
| Visible PHP notices | Not observed in sampled HTML |
| `/wp-login.php` | Reachable **200** (no auth) |
| `/wp-json/` | **200** |
| `/robots.txt` | Default allow-site / disallow wp-admin |
| Sitemaps | `wp-sitemap.xml` / `sitemap.xml` → **404** |

Route matrix: `REPORTS/evidence/prod-p01-beget-read-only-onboarding/route-matrix.json`

---

## 4. Migration Integrity

| Finding | Severity | Notes |
|---------|----------|-------|
| Hardcoded `http://shpigovsky.test/...` in some “all” / CTA links | **HIGH (content/link residue)** | Home + service leaves; e.g. comfort/specialists/genotyping “all” links |
| Site name/title «локальная разработка» | Medium | Public WP identity leftover |
| Broken media / missing CSS/JS for main theme stack | Not found for hashed theme assets | `v9-style.css` etc. **PUBLIC HASH MATCH** |
| Mixed content | N/A on HTTP working host | HTTPS unavailable |
| Old domain `shpigovsky.ru` as live authority | Out of scope | DNS deferred |
| Absolute localhost / `X:\` / `127.0.0.1` | Not found in residue pass | |

Evidence: `migration-residue.json`, `migration-residue-contexts.txt`

**No repairs in this wave.**

---

## 5. FP-0002 Authority Model (post-migration)

| Surface | Role |
|---------|------|
| `WORDPRESS/` Git source | **CODE / SOURCE AUTHORITY** |
| `http://shpigovsky.beget.tech/` | **LIVE RUNTIME TRUTH / PRODUCTION OPERATIONAL AUTHORITY** |
| Beget WP DB | **LIVE CONTENT / ADMIN STATE AUTHORITY** |
| `X:\MARS-Localhost\sites\wordpress\projects\shpigovsky\` | **LOCAL ACCEPTED REFERENCE / DEVELOPMENT MIRROR** (must not auto-overwrite production) |
| Stable v1 freeze + A01 backups | Engineering reference — not automatic production DB rollback |

Golden rule documented: no broad local→production sync; fetch→diff→canonize→exact deploy.

---

## 6. Source ↔ Production Public Parity

| Asset / component | Local authority | Production evidence | Result |
|-------------------|-----------------|---------------------|--------|
| `assets/css/v9-style.css` | SOURCE `1CCC5A8F…` | Public body hash | **PUBLIC HASH MATCH** |
| `fp02-floating-header.css` / `fp02-lifebuoy-parallax.css` / `fp02-search.css` | SOURCE | Public hash | **PUBLIC HASH MATCH** |
| `v9-shell.js` + floating/lifebuoy JS | SOURCE | Public hash | **PUBLIC HASH MATCH** |
| Fancybox CSS/JS + Swiper CSS/JS | SOURCE vendor | Public hash | **PUBLIC HASH MATCH** |
| Branding/social/comfort/program images (sampled) | SOURCE theme assets | Public hash | **PUBLIC HASH MATCH** |
| Theme PHP / `shpigovsky-core` PHP | SOURCE | — | **NOT PUBLICLY VERIFIABLE** |
| ACF JSON/DB | SOURCE + DB | — | **NOT PUBLICLY VERIFIABLE** |
| Uploads / icons under `uploads/2026/07/` | Runtime media | Public bytes | **NOT PUBLICLY VERIFIABLE** vs Git source |
| Hardcoded `.test` CTA hrefs | Should be relative/prod URLs | HTML residue | **DRIFT DETECTED** (content/link) |

Evidence: `theme-css-js-parity.json`, `theme-public-asset-hashes.json`

---

## 7. Program Auto-Source

| Check | Result |
|-------|--------|
| Page | **Пространство восстановления** |
| Slug | `prostranstvo-vosstanovleniya` |
| Route | `/o-centre/programma-lecheniya/prostranstvo-vosstanovleniya/` → **200** |
| Repeated on Home / O-centre / `/uslugi/` / `/uslugi/zavisimosti/` | Current title + slug present |
| Old title `Нейропсихологическая коррекция` | **Absent** on checked routes |
| Old slug `neyropsihologicheskaya-korrektsiya` | **Absent** |

Evidence: `program-auto-source.json`, `program-card-snippets.txt`

---

## 8. Comfort Gallery

| Check | Result |
|-------|--------|
| `/uslugi/`, `/uslugi/zavisimosti/`, leaf e.g. `/uslugi/zavisimosti/lechenie-alkogolnoy-zavisimosti/` | Gallery markup present |
| Fancybox CSS + JS | Enqueued; **PUBLIC HASH MATCH** |
| `data-fancybox` on gallery items | Present (6 on leaves; more on home/o-centre stacks) |
| `comfort__gallery-decor` | Present (decor outside gallery pattern retained) |
| Frontend JS | `v9-shell.js` present (hash match) |
| Browser automation screenshots / console | **Not captured** this wave (HTTP/HTML evidence only) |

---

## 9. Production Site Passport

Created: `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`  
VERIFIED vs SAFE UNKNOWN split recorded therein.

---

## 10. Protected Zones

Created: `DOCS/PRODUCTION/FP-0002-PROTECTED-ZONES-BEGET-v1.md`  
Default-deny inventory including WPilot token/settings, DNS, SSL, ACF, theme/plugin, uploads, DB.

---

## 11. Backup / Rollback Model

Created: `DOCS/PRODUCTION/FP-0002-BEGET-BACKUP-ROLLBACK-MODEL-v1.md`  
Layers A (Beget full) / B (exact file) / C (WPilot op) / D (local references).

---

## 12. Production Change Model

Created: `DOCS/PRODUCTION/FP-0002-BEGET-PRODUCTION-CHANGE-MODEL-v1.md`  
Filesystem fetch→diff→canonize→exact upload; Admin/ACF/DB/FTP/WPilot rules.

---

## 13. Current WPilot Version Truth

### CURRENT GLOBAL NEW-PRODUCTION BASELINE

| Field | Value |
|-------|-------|
| Source plugin version | **0.3.2** |
| Release label | **0.3.2-RC1** |
| Schema | **0.2.0** |
| REST | **wpilot/v1** |
| ZIP | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip` |
| SHA-256 | **`d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934`** (recomputed match) |

RC6 is **historical** proven baseline for i-seo/metallka — **not** current source authority.

### POLYGON HISTORICAL FINAL VERSION

**0.3.2 / 0.3.2-RC1** (P07–P13).

### FP-0002 Beget live

Installed (public ping). Version label **SAFE UNKNOWN**. Public posture: bridge on, DEV confirmed, token generated, write off.

---

## 14. WPilot Install Readiness

Doc: `DOCS/PRODUCTION/FP-0002-WPILOT-INSTALL-READINESS.md`

| Item | Value |
|------|-------|
| Package ready | **Yes** (0.3.2-RC1 ZIP + SHA verified) |
| Install method | WP Admin Upload Plugin (if upgrade/clean install chartered) |
| Expected safe defaults (clean activate) | bridge/write/dev_confirmed false |
| Beget actual | **Not** safe-default posture |
| Operator action | **Reconcile version in WP Admin first** — do not blind reinstall |
| STOP point | After version report (and after any authorized upgrade activation) — before token/bridge/write |

---

## 15. Authentication Preparation

| Item | Value |
|------|-------|
| Auth model | Header `X-WPilot-Token`; hash-only on site |
| Future token path | `X:\AI MARS\local\tokens\wpilot-prod-shpigovsky.token` |
| Secret generated this wave | **No** |

---

## 16. Runtime Checkout

| Item | Value |
|------|-------|
| Proposed path | `X:\AI MARS STORAGE\runtime-checkouts\fp-0002-shpigovsky-production\repo` |
| Status | **Documented future path only** — **not** provisioned in PROD-P01 |
| Rule | Scheduled/runtime jobs must not run from dirty `X:\AI MARS` |

---

## 17. DNS Cutover

| Item | Value |
|------|-------|
| Status | **`DNS_CUTOVER = DEFERRED`** |
| Current temporary host | `shpigovsky.beget.tech` |
| Risks | Indexing of temporary host; dual public sites until cutover; title still “локальная разработка”; some `.test` links |

No DNS/SSL/robots mutations.

---

## 18. SAFE UNKNOWN (before next WPilot gate)

See `REPORTS/evidence/prod-p01-beget-read-only-onboarding/SAFE-UNKNOWN-REGISTER.md` — notably: production WPilot Version, DB identity/prefix on Beget, docroot, HTTPS/cert, SMTP, backup ID, OPcache/WAF, logs.

---

## 19. Exact Documentation Files Changed

**Created**

- `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`
- `DOCS/PRODUCTION/FP-0002-PROTECTED-ZONES-BEGET-v1.md`
- `DOCS/PRODUCTION/FP-0002-BEGET-BACKUP-ROLLBACK-MODEL-v1.md`
- `DOCS/PRODUCTION/FP-0002-BEGET-PRODUCTION-CHANGE-MODEL-v1.md`
- `DOCS/PRODUCTION/FP-0002-WPILOT-INSTALL-READINESS.md`
- `REPORTS/REPORT-FP-0002-PROD-P01-BEGET-READ-ONLY-ONBOARDING.md`
- `REPORTS/evidence/prod-p01-beget-read-only-onboarding/**` (compact JSON/TXT evidence)

**Updated**

- `PROJECT-STATUS.md`
- `WORDPRESS/SOURCE-AUTHORITY.md`

Stable v1 historical docs: **not** rewritten.

---

## 20. Git Status

- **No commit**
- **No push**
- Foreign WIP / staged unrelated paths: **untouched**
- Working tree remains dirty shared monorepo; HEAD may differ from `origin/mars/canonical-post-recovery` due to foreign work — not modified by this wave

---

## 21. Next Operator Action

1. Confirm Beget full backup is still recent enough for a WPilot reconcile/upgrade wave.  
2. WP Admin → Plugins → open **MetaCODE WPilot** → report **Version** (and any release label) to MARS.  
3. **STOP** — do not create token, do not change bridge/write.  
4. If MARS then authorizes upgrade: upload exact ZIP  
   `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip`  
   SHA-256 `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934`  
   then activate if needed and **STOP** again.  

Separate future charters (not now): safe-defaults reset; token rotation to `wpilot-prod-shpigovsky.token`; `.test` link cleanup; site title cleanup; DNS cutover.

---

## Desired end-state statement

**FP-0002 BEGET PRODUCTION IDENTITY AND CHANGE MODEL KNOWN — CURRENT WPILOT INSTALL PACKAGE RECONCILED — READY FOR SEPARATE OPERATOR-ASSISTED WPILOT RECONCILE / INSTALL GATE**

(Install package ready; live site already has a migrated WPilot instance requiring reconcile-first handling.)
