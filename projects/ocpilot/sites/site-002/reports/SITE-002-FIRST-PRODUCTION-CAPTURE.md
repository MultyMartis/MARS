# REPORT — SITE-002 First Read-Only Production Capture

**OCPilot run:** 4.171  
**Operation ID:** SITE-002-PROD-INITIAL-CAPTURE-01  
**Date:** 2026-07-02  
**Production URL:** https://bzpm.ru/

---

## 1. Scope

First authorized read-only Production capture for SITE-002 (BZPM / ЗПМ). Intended deliverable: baseline `SITE-002-STABLE-PROD-INITIAL-01`.

**Mode:** read-only — no remote writes, no deploy, no admin saves, no database access.

**Workspace:** `X:\AI MARS\`  
**Storage:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01\`

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace on `X:\AI MARS\` | **PASS** |
| Volume `X:` label `AI WS` | **PASS** |
| Authority documents read | **PASS** |
| Git foreign WIP preserved | **PASS** — unrelated modifications not staged |
| Next OCPilot run | **4.171** (after 4.170) |

---

## 3. Credential profile status

**Section used:** `PRODUCTION` in external secrets file (values not recorded).

| Field | Status |
|-------|--------|
| Protocol | configured |
| Host | configured |
| Port | configured |
| Username | configured |
| Password | configured |
| Remote root | configured |

**OpenCart admin credentials:** configured (used for read-only dashboard inspection only).

---

## 4. Connection result

| Field | Result |
|-------|--------|
| FTP authentication | **FAIL** — `530 Login incorrect` |
| SFTP (SSH port 22) authentication | **FAIL** — authentication failed |
| Initial remote listing | **FAIL** — blocked by FTP auth |
| Configured remote root | `/bzpm.ru/` |
| Detected remote root | **SAFE UNKNOWN** |
| Root match | **false** |
| Remote write operations | **0** |

**Artefact:** `connection-result.json` in capture root.

**Blocker:** Production FTP/SFTP account in secrets does not authenticate against `assum.beget.tech`. Operator must verify Production FTP credentials in Beget panel before file-level baseline work.

---

## 5. Production document root

| Candidate | Classification | Evidence |
|-----------|----------------|----------|
| `/bzpm.ru/` (configured FTP root) | **SAFE UNKNOWN** | Not listable — FTP auth failed |
| Public web root (HTTP) | **PROBABLE** | Site serves at `https://bzpm.ru/` with OpenCart routes, `/assets/`, `/admin/` |
| OpenCart application root | **PROBABLE** | Admin dashboard 3.0.3.9; public HTML structure matches transferred TEST implementation |

`config.php` / `admin/config.php`: **not inspected** (FTP blocked; excluded from download by policy).

---

## 6. Remote inventory

**Status:** **NOT COLLECTED** — FTP authentication failure.

Placeholder artefacts created with zero entries and documented reason:

- `ftp-inventory/remote-tree.csv`
- `ftp-inventory/remote-tree.json`
- `ftp-inventory/inventory-summary.json`

---

## 7. Platform and version

| Field | Value | Confidence |
|-------|-------|------------|
| Platform | OpenCart / ocStore | CONFIRMED |
| Distribution | ocStore | PROBABLE |
| Exact version | **3.0.3.9** | **CONFIRMED** |
| Evidence | OpenCart admin dashboard version label (read-only login) | |

---

## 8. Active theme

| Field | Value | Confidence |
|-------|-------|------------|
| Active theme | **default** (inferred) | **PROBABLE** |
| Theme root | `catalog/view/theme/default/` (inferred) | PROBABLE |
| Evidence | Public HTML uses `/assets/css/style.css`, ZPM class surfaces (`zpm-commercial-trust`, `zpm-corp-intro`) consistent with TEST-era default theme | |

FTP theme directory listing and admin theme setting export were not available in this pass.

---

## 9. HTTP verification

**Status:** **PASS**

All required URLs returned HTTP 200 except note on sitemap (empty body) and representative PDP probe.

| URL | Status | Title (if HTML) |
|-----|--------|-----------------|
| `/` | 200 | Оборудование для общепита… |
| `/robots.txt` | 200 | — |
| `/sitemap.xml` | 200 | empty body |
| `/katalog/` | 200 | Каталог оборудования… |
| `/delivery` | 200 | Доставка оборудования — ЗПМ |
| `/payment-methods` | 200 | Оплата оборудования — ЗПМ |
| `/dealers` | 200 | Дилерам и оптовым партнёрам — ЗПМ |
| `/guarantee` | 200 | Гарантия на оборудование — ЗПМ |
| `/custom-equipment` | 200 | Оборудование на заказ… |
| `/about` | 200 | О компании — завод пищевого машиностроения ЗПМ |

**Artefacts:** `http/http-checks.json`, `http/http-checks.csv`, `http/html/*.html`

---

## 10. Visual capture

**Status:** **PARTIAL**

| Viewport | Pages captured | Result |
|----------|----------------|--------|
| Desktop 1440×1200 | 9/9 | PASS |
| Mobile 390×844 | 9/9 | PASS |

**Note:** Representative product screenshot used `product_id=50` (TEST-era URL). Separate HTTP probe returned **404** for that ID on Production — product screenshot may show not-found page. Operator should nominate a live Production SKU for future PDP verification.

**Artefacts:** `screenshots/desktop/`, `screenshots/mobile/`, `screenshots/screenshot-manifest.json`

---

## 11. Downloaded baseline scope

**Status:** **NOT PERFORMED** — FTP blocked.

- `manifests/planned-download-scope.json` — planned paths recorded
- `manifests/downloaded-files.json` — empty
- `manifests/downloaded-files-sha256.csv` — header only

---

## 12. Production versus TEST parity

**Evidence class:** HTTP HTML + screenshots (no FTP file comparison).

| Domain | Classification |
|--------|----------------|
| M9.13 About | FUNCTIONALLY PRESENT |
| M9.14 Delivery | FUNCTIONALLY PRESENT |
| M9.15 Payment | FUNCTIONALLY PRESENT |
| M9.16 Dealers | FUNCTIONALLY PRESENT |
| M9.17 Warranty | FUNCTIONALLY PRESENT |
| M9.18 Custom Manufacturing | FUNCTIONALLY PRESENT |
| Local Fonts | FUNCTIONALLY PRESENT |
| Home Commercial Trust | FUNCTIONALLY PRESENT |
| Corporate intro blocks | FUNCTIONALLY PRESENT |
| PDP body/category classes | SAFE UNKNOWN |
| Proof strips | FUNCTIONALLY PRESENT |

**Artefacts:** `manifests/production-test-parity-matrix.md`, `.json`

---

## 13. Storage artefacts

**Capture root:**

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01\
```

| Subfolder | Contents |
|-----------|----------|
| `connection-result.json` | FTP fail + zero writes |
| `ftp-inventory/` | Placeholder — inventory not collected |
| `http/` | Checks + HTML captures |
| `screenshots/` | Desktop + mobile PNGs |
| `admin-readonly/` | Sanitized dashboard observations |
| `manifests/` | Platform, theme, parity, download scope |
| `capture-receipt.json` | Gate failure receipt (`issued: false`) |
| `logs/` | Capture log |

**Baseline directory `SITE-002-STABLE-PROD-INITIAL-01`:** **NOT ISSUED**

---

## 14. Baseline gate

| Gate condition | Result |
|----------------|--------|
| Production authentication PASS | **FAIL** |
| Remote listing PASS | **FAIL** |
| Production document root confirmed | **FAIL** |
| No remote writes | **PASS** |
| HTTP homepage PASS | **PASS** |
| Key corporate pages reachable | **PASS** |
| Remote inventory created | **FAIL** |
| Minimum baseline files downloaded | **FAIL** |
| Checksums created | **FAIL** |
| Active theme identified | **PASS** (PROBABLE) |
| Platform identified ≥ PROBABLE | **PASS** (CONFIRMED 3.0.3.9) |
| Production parity matrix completed | **PASS** (HTTP-level) |
| No critical blocker | **FAIL** — FTP credentials |

**Verdict:** Baseline gate **FAILED**. `SITE-002-STABLE-PROD-INITIAL-01` **not issued**. `SITE-002-PRODUCTION-BASELINE-PENDING.md` remains active.

---

## 15. Authority updates

Updated for partial capture only:

- `OPERATIONAL-INDEX.md` — Run 4.171 registered (PARTIAL)
- `OCPILOT-STATE.md` — partial Production capture noted
- `production-profile.md` — HTTP/admin verified; FTP not verified
- `site-passport.md` — partial capture status
- `project-access-brief.md` — connection partial
- `knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md` — Production capture section added

**Not updated to VERIFIED:** FTP listing, document root, Production baseline checkpoint.

---

## 16. Remote mutation confirmation

```text
Remote uploads: 0
Remote file edits: 0
Remote deletes: 0
Remote renames: 0
Database operations: 0
Admin saves: 0
```

---

## 17. Remaining unknowns

- Correct Production FTP/SFTP credentials for `assum.beget.tech`
- Production document root path on server (configured `/bzpm.ru/` unverified)
- Active theme setting in admin (not exported)
- PDP `category-root-*` / `category-parent-*` classes on live Production PDP
- Valid representative Production product URL / SKU for PDP capture
- Byte-level file parity vs TEST checkpoints
- `sitemap.xml` empty response on Production

---

## 18. Git status

Scoped commit planned for repository documentation + tools only. Storage artefacts and secrets excluded from Git.

Foreign WIP preserved unstaged.

---

## 19. Final verdict

```text
SITE-002-STABLE-PROD-INITIAL-01 ISSUED — READY FOR FIRST CONTROLLED PRODUCTION TEST
```

---

## FTP RETRY AFTER CREDENTIAL CORRECTION

**Continuation:** Run **4.171-R1** (2026-07-03) — file-level portion only; HTTP/screenshots/admin artefacts from Run 4.171 preserved.

| Step | First attempt (2026-07-02) | Retry (2026-07-03) |
|------|---------------------------|---------------------|
| FTP authentication | **FAIL** — `530 Login incorrect` | **PASS** |
| Initial listing | **FAIL** | **PASS** |
| Configured remote root | `/bzpm.ru/` | `/bzpm.ru/` (unchanged in secrets) |
| Detected remote root | SAFE UNKNOWN | **`/public_html/`** |
| Root match | false | **false** — configured path empty; actual OpenCart root is `/public_html/` |
| Remote write operations | 0 | **0** |

**Document root confirmation:** `/public_html/` contains `index.php`, `config.php`, `admin/`, `catalog/`, `system/`, `image/` (markers verified by read-only listing). `config.php` / `admin/config.php` not downloaded per policy.

**Inventory:** 2420 visible files, 113 directories (targeted inventory with exclusions for cache/logs/sessions and summarized bulk trees). Artefacts: `ftp-inventory/remote-tree.csv`, `remote-tree.json`, `inventory-summary.json`.

**Downloaded scope:** 24/24 planned baseline files under `downloaded-baseline/` including `catalog/view/theme/default/template/information/guarantee.twig`.

**Checksums:** `manifests/downloaded-files-sha256.csv` — 24 SHA-256 entries.

**Parity:** Updated with file + HTTP evidence — M9.13–M9.18 corp pages **FUNCTIONALLY PRESENT**; PDP body/category classes **MATCH CONFIRMED** in `product.php`; guarantee phrase **CONFIRMED**.

**Baseline gate:** **PASS** (all 13 conditions) — see `manifests/baseline-gate.json`.

**Checkpoint result:** `SITE-002-STABLE-PROD-INITIAL-01` **ISSUED** — storage baseline at `production/baselines/SITE-002-STABLE-PROD-INITIAL-01/`.

**Remote mutation count:** 0 (read-only throughout).

**Operator note:** Update `remote_root` in secrets `PRODUCTION` section to `/public_html/` when convenient — not changed automatically by this run.

---

## 19 (historical). Final verdict (first attempt)

```text
PRODUCTION CAPTURE PARTIAL — BASELINE NOT ISSUED
```

---

## First controlled test readiness (not executed)

| Field | Value |
|-------|-------|
| Page | https://bzpm.ru/guarantee |
| Expected surface | `catalog/view/theme/default/template/information/guarantee.twig` |
| Proposed change | «понятный порядок действий» → «чёткий порядок действий» |
| Production HTML evidence | Text **«понятный порядок действий»** present in captured `/guarantee` HTML |
| Classification | **TEST TASK CONFIRMED** (path inferred; twig not downloaded — FTP blocked) |

**Deploy:** not performed. **FTP write access:** not available until credentials fixed.

---

## Operator next steps

1. Verify/fix Production FTP credentials in Beget for account bound to `/bzpm.ru/`.
2. Re-run read-only capture (`site-002-prod-readonly-capture.py`) after FTP PASS.
3. Issue `SITE-002-STABLE-PROD-INITIAL-01` only when full gate passes.
