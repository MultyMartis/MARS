# REPORT — FP-0002 PROD-P04-FU01 Filesystem Baseline

**Date:** 2026-08-13  
**Host:** `http://shpigovsky.beget.tech/`  
**Canonical domain:** `shpigovsky.ru` (`DNS_CUTOVER = DEFERRED`)  
**Evidence:** `REPORTS/evidence/prod-p04-fu01-filesystem-baseline/`

```text
FP-0002 REAL BEGET WORDPRESS FILESYSTEM READ PROVEN
FULL PRODUCT FILESYSTEM SHA BASELINE KNOWN
DB SELECT ALREADY PROVEN
READY FOR CONTROLLED WPILOT UPGRADE/AUTH GATE
NO PRODUCTION PRODUCT MUTATIONS
NO COMMIT / NO PUSH
```

---

## 1. Status

* **PASS**
* production mutations: **0**
* filesystem writes: **0**
* DB writes: **0**
* WP Admin writes: **0**
* WPilot writes: **0** (no upgrade; no token reissue; `write_enabled=false`)
* commit/push: **none**

Desired end-state for this wave is **reached**.

---

## 2. Filesystem Access

| Item | Result |
|------|--------|
| Protocol | **SSH preferred** (paramiko SFTP + remote `sha256sum`); FTP :21 also **PASS** |
| Auth | **VERIFIED** (`shpigovsky_mars`) |
| Actual WordPress root | `/home/s/shpigovsky/shpigovsky.ru/public_html` — account `pwd` / FTP `/` |
| Prior jail | `…/shpigovsky.beget.tech/public_html` — **REMOVED / OBSOLETE** |
| Result | **REAL WORDPRESS FILESYSTEM READ PROVEN** |

Required paths readable: `wp-config.php`, `wp-admin/`, `wp-includes/`, `wp-content/`, theme `shpigovsky/`, `shpigovsky-core/`, `metacode-wpilot/`, `wp-content/acf-json/`, `uploads/`.

---

## 3. WordPress Runtime

| Field | Value |
|-------|-------|
| Docroot | `/home/s/shpigovsky/shpigovsky.ru/public_html` |
| Core version | **7.0.4** (`wp-includes/version.php`) |
| Core structure | **OK** (version.php, wp-settings.php, wp-admin/includes, wp-includes/js) |
| PHP web (prior) | **8.3.20** (unchanged observation class from P01/P03) |
| PHP CLI default on SSH | 5.6.40 (host default; not site PHP) |
| `wp-content` | present / readable |
| Theme | `wp-content/themes/shpigovsky` — SHA baseline complete |
| Custom plugin | `wp-content/plugins/shpigovsky-core` — SHA baseline complete |
| ACF JSON | `wp-content/acf-json` (24 files) — primary; stale secondary copy also at docroot `/acf-json` (7 older files; not used as parity authority) |
| Uploads | present / readable (corpus not inventoried) |

---

## 4. wp-config Safe Metadata

No secrets reported.

| Field | Production | vs P04 DB |
|-------|------------|-----------|
| `DB_NAME` | `shpigovsky_main` | **consistent** |
| `DB_HOST` | `localhost` | **SSH_LOCAL_MYSQL model confirmed** |
| `$table_prefix` | `fp02_` | **consistent** |
| `DB_CHARSET` | `utf8` (define) | live tables were `utf8mb4` in P04 SELECT — note only |
| `DB_COLLATE` | empty | — |
| `WP_DEBUG` | `true` | migration leftover |
| `WP_DEBUG_LOG` | `true` | leftover |
| `WP_DEBUG_DISPLAY` | `false` | — |
| `SCRIPT_DEBUG` | `true` | leftover |
| `DISALLOW_FILE_EDIT` | `true` | — |
| `WP_ENVIRONMENT_TYPE` | `local` | migration leftover |
| `WP_DEBUG_LOG_FILE` | historical `D:/MARS-Localhost/…` path | migration leftover (path only; not mutated) |
| Password / salts / keys | **PRESENT flags only** — values never captured | — |

---

## 5. Theme Parity

Local: `WORDPRESS/theme/shpigovsky/` → prod `wp-content/themes/shpigovsky/`

| Class | Count |
|-------|------:|
| Total compared | **660** |
| MATCH | **655** |
| PRODUCTION_ONLY_OPERATOR_DRIFT | **5** (`.gitkeep` placeholders only) |
| LOCAL_ONLY_NEWER | **0** |
| DIVERGENT | **0** |

Production-only paths: `assets/img/.gitkeep`, `assets/js/.gitkeep`, `assets/svg/.gitkeep`, `languages/.gitkeep`, `template-parts/.gitkeep`.

---

## 6. shpigovsky-core Parity

Local: `WORDPRESS/plugins/shpigovsky-core/` → prod `wp-content/plugins/shpigovsky-core/`

| Class | Count |
|-------|------:|
| Total compared | **25** |
| MATCH | **24** |
| PRODUCTION_ONLY_OPERATOR_DRIFT | **1** (`languages/.gitkeep`) |
| LOCAL_ONLY_NEWER | **0** |
| DIVERGENT | **0** |

Plugin header version on production: `0.3.3-v9-06e25a-source` (matches source authority).

---

## 7. ACF JSON Parity

Local: `WORDPRESS/acf-json/` → prod `wp-content/acf-json/`  
Reconciled against `REPORTS/ACF-SOURCE-RUNTIME-DISPOSITION-FP-0002-V9-STABLE-V1.md`.

| Class | Count |
|-------|------:|
| Total compared | **31** |
| MATCH | **24** |
| KNOWN_INTENTIONAL_SOURCE_ONLY | **7** |
| Unexplained drift / DIVERGENT | **0** |

Intentional source-only (retain; **not** defects):

* `group_fp02_block_final_form.json`
* `group_fp02_block_specialists.json`
* `group_fp02_page_institutional_child.json`
* `group_fp02_page_legal.json`
* `group_fp02_service_faq.json`
* `group_fp02_service_relationships.json`
* `group_fp02_service_structured_sections.json`

Disposition note: `group_fp02_page_ocentre_hub.json` was source-only in Stable v1 docs; on production FS it is now **MATCH** (present both sides, identical SHA). Still not classified as a defect.

Secondary docroot `/acf-json` holds 7 older JSON copies with some hash mismatch vs `wp-content/acf-json` — migration residue / non-authority path; not mutated.

---

## 8. Material Production Drift

Product surfaces (theme + core + ACF), excluding intentional source-only:

| Path | Classification |
|------|----------------|
| `themes/shpigovsky/assets/img/.gitkeep` | PRODUCTION_ONLY_OPERATOR_DRIFT |
| `themes/shpigovsky/assets/js/.gitkeep` | PRODUCTION_ONLY_OPERATOR_DRIFT |
| `themes/shpigovsky/assets/svg/.gitkeep` | PRODUCTION_ONLY_OPERATOR_DRIFT |
| `themes/shpigovsky/languages/.gitkeep` | PRODUCTION_ONLY_OPERATOR_DRIFT |
| `themes/shpigovsky/template-parts/.gitkeep` | PRODUCTION_ONLY_OPERATOR_DRIFT |
| `plugins/shpigovsky-core/languages/.gitkeep` | PRODUCTION_ONLY_OPERATOR_DRIFT |

No material PHP/CSS/JS/JSON content divergence on source-owned product surfaces.  
`.gitkeep` items may be canonized later if desired; **not** blocking.

---

## 9. WPilot Production Filesystem

| Field | Value |
|-------|-------|
| Installed version | **0.3.0** (plugin header + `WPilot_Constants::VERSION`) |
| Schema | **0.2.0** |
| Release label | absent on 0.3.0 tree |
| Current baseline | **0.3.2 / 0.3.2-RC1** |
| Package | `X:\AI MARS STORAGE\wpilot\deploy-packages\metacode-wpilot-v0.3.2-rc1.zip` |
| Package SHA | `d55c19d6ea1a55cd145e9b67c42ca201c30e4356f08d8cf3932ef6a5ebc80934` — **MATCH** |
| Production file count | **27** |
| Production-only vs 0.3.2 source | **0** |
| MATCH vs 0.3.2 | **12** |
| DIVERGENT (expected version delta) | **15** |
| LOCAL_ONLY_NEWER in 0.3.2 | **5** (`content-persistence`, `vc-raw-html-*`, `write-context`) |
| Production modifications that would be lost | **NO** |
| Exact upgrade delta known | **YES** |
| Clean native WP Admin package replacement | **VALID / SAFE** |

Upgrade **not** performed this wave.

---

## 10. Production SHA Manifest

* Path: `REPORTS/evidence/prod-p04-fu01-filesystem-baseline/production-source-parity-manifest.json`
* Product files compared (theme + shpigovsky-core + ACF JSON): **716**
* WPilot: summary + full file inventory in `wpilot-parity.json` / `wpilot-upgrade-delta.json`

---

## 11. Access Matrix

| Surface | State |
|---------|-------|
| FS auth | **VERIFIED** |
| Actual WordPress root | **VERIFIED** |
| FS READ | **PROVEN** |
| FS WRITE | **CLOSED BY POLICY** |
| DB | **SSH_LOCAL_MYSQL**; SELECT **PROVEN**; WRITE **CLOSED** |
| WP Admin | inspection **PROVEN**; writes task-specific only |
| WPilot | version **known**; upgrade **pending**; token reconcile **pending**; write **disabled** |
| DNS | **DEFERRED** |

---

## 12. Migration Tails

Carry forward from P04 DB (no mutation):

* **158** `.test` occurrences including revisions
* **46** real non-revision occurrences / **43** objects
* site title still local-development label (`Шпиговский — локальная разработка`)
* wp-config leftovers: `WP_ENVIRONMENT_TYPE=local`, `WP_DEBUG=true`, historical `WP_DEBUG_LOG_FILE` path

Future P06/P07 correction scope after WPilot connection is healthy.

---

## 13. Secret Safety

* exposed values in chat/tracked artifacts: **0**
* tracked secrets: **0**
* obsolete credential secret retained as active authority: **NO** (prior jail marked **REMOVED / OBSOLETE**; no obsolete password preserved as authority)
* wp-config dump: **0**
* DB dump: **0**

---

## 14. Exact Docs/Evidence Changed

**Tracked**

* `DOCS/PRODUCTION/FP-0002-PRODUCTION-ACCESS-MATRIX-v1.md`
* `DOCS/PRODUCTION/FP-0002-CREDENTIAL-REFERENCE-MAP-v1.md`
* `DOCS/PRODUCTION/FP-0002-SOURCE-PRODUCTION-AUTHORITY-v1.md`
* `DOCS/PRODUCTION/FP-0002-MARS-PRODUCTION-CONNECTION-PROFILE-v1.md`
* `DOCS/PRODUCTION/FP-0002-PRODUCTION-SITE-PASSPORT-BEGET-v1.md`
* `PROJECT-STATUS.md`
* `REPORTS/REPORT-FP-0002-PROD-P04-FU01-FILESYSTEM-BASELINE.md`
* `REPORTS/evidence/prod-p04-fu01-filesystem-baseline/*`

**Local-only (gitignored `/local/`)**

* `X:\AI MARS\local\sites\shpigovsky-production\secrets.local.md` (non-secret notes / `ssh_available=yes` only)
* `X:\AI MARS\local\sites\shpigovsky-production\site-profile.json`

---

## 15. Git

* commit: **none**
* push: **none**
* foreign WIP: **untouched**
* `git add` / stash / reset / clean / restore: **not used**

Preflight: cwd `X:\AI MARS`, volume `AI WS`, branch `mars/canonical-post-recovery`.

---

## 16. Next Wave

WPilot production filesystem has **no** undocumented production-only modifications. Native package replacement remains valid.

```text
PROD-P05 — WPilot 0.3.2-RC1 Exact Upgrade + Token Reissue + Authenticated READ Gate
```

Final desired state for this wave:

`FP-0002 REAL BEGET WORDPRESS FILESYSTEM READ PROVEN — FULL PRODUCT FILESYSTEM SHA BASELINE KNOWN — DB SELECT ALREADY PROVEN — READY FOR CONTROLLED WPILOT UPGRADE/AUTH GATE`

---

## Execution safety

- cwd: `X:\AI MARS`
- scope lock honored: yes (`X:\AI MARS` docs/evidence + gitignored `X:\AI MARS\local\…`; package SHA read from `X:\AI MARS STORAGE\…`)
- destructive ops: none
- protected zone touch: production inspected read-only; no `wp-config` edit; no DNS; no WPilot write flag; no remote MySQL exposure; no uploads corpus sync

---

*PROD-P04-FU01 · PASS · no secrets · no commit · no push.*
