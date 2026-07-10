# SITE-002 TECHNICAL KNOWLEDGE MAP

**Site:** SITE-002 (ЗПМ / BZPM)

## Operational authority (present state)

| Field | Value |
|-------|-------|
| **Current operational website** | https://bzpm.ru/ |
| **Historical TEST** | https://zpm.new-site.space/ |
| **Production profile** | [../production-profile.md](../production-profile.md) |
| **Production storage root** | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\` |
| **Production baseline** | Parent baseline `SITE-002-STABLE-PROD-INITIAL-01` · [../baselines/SITE-002-STABLE-PROD-INITIAL-01.md](../baselines/SITE-002-STABLE-PROD-INITIAL-01.md) |
| **Current Production checkpoint** | **ISSUED** — `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01` · [../baselines/SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01.md](../baselines/SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01.md) (parent Wave E) |
| **Production parity with TEST checkpoints** | **VERIFIED** — file + HTTP evidence (Run 4.171-R1) |
| **First controlled Production change** | **COMPLETE** — Run 4.173; single-file text-only FTP deploy |
| **Catalog default sort (Production)** | **COMPLETE** — Run 4.176; default `pd.name ASC` in `category.php` |
| **Catalog sort menu (Production)** | **COMPLETE** — Run 4.177; menu order in `category.twig`; «Умолчанию» removed |
| **MARS 1C cron wrapper (Production)** | **OPERATIONAL — FIRST SCHEDULED RUN VERIFIED** — Run 4.194; automatic run SUCCESS 2026-07-06 08:00 Moscow; daily import OPERATIONAL |
| **MARS 1C cron reports (Production)** | **CURRENT** — Run 4.194; first scheduled report `mars_1c_import_2026-07-06_080007.txt` verified on Production |

**TEST-derived knowledge classification:** Implementation evidence and reusable technical knowledge. **Not** automatic proof of current Production parity.

### Production capture (Run 4.171 / 4.171-R1 — 2026-07-02/03)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-INITIAL-CAPTURE-01` |
| Report | [../reports/SITE-002-FIRST-PRODUCTION-CAPTURE.md](../reports/SITE-002-FIRST-PRODUCTION-CAPTURE.md) |
| HTTP verification | **PASS** — homepage + corporate routes |
| Visual capture | **PASS** — 18/18 screenshots (Run 4.171) |
| Admin read-only | **PASS** — OpenCart **3.0.3.9** |
| FTP/SFTP | **PASS** (retry) — application root `/bzpm.ru/`; FTP chroot `/` → public `/public_html/` + `/storage/` |
| File baseline | **24 files** + SHA-256 in capture `downloaded-baseline/` |
| Active theme | `default` — **CONFIRMED** |
| First test task | `guarantee.twig` — phrase «понятный порядок действий» **CONFIRMED** |
| PDP category classes | **MATCH CONFIRMED** in `catalog/controller/product/product.php` |
| Baseline | **ISSUED** — `SITE-002-STABLE-PROD-INITIAL-01` |
| Storage | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\captures\SITE-002-PROD-INITIAL-CAPTURE-01\` |

### Production path model (Run 4.172)

| Concept | Hosting path | FTP-visible path |
|---------|--------------|------------------|
| Application root | `/bzpm.ru/` | `/` (chrooted login) |
| Public document root | `/bzpm.ru/public_html/` | `/public_html/` |
| OpenCart storage root | `/bzpm.ru/storage/` | `/storage/` |

Secrets `Remote root` = application root. Deploy paths for theme files are under `public_html/` (FTP) or `/bzpm.ru/public_html/` (hosting).

### First controlled Production change (Run 4.173 — 2026-07-04)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-TEXT-CHANGE-01` |
| Status | **COMPLETE** |
| Page | https://bzpm.ru/guarantee |
| Remote file | `/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| Change | `понятный порядок действий` → `чёткий порядок действий` |
| Verification | PASS — remote SHA, HTTP 200, desktop/mobile screenshots |
| Checkpoint | `SITE-002-STABLE-PROD-TEXT-CHANGE-01` |
| Report | [../reports/SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md](../reports/SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md) |

Proven operational boundary:

```text
single-file text-only FTP deploy with backup and rollback readiness
```

Do not generalize Run 4.173 proof to CSS/JS/controller deploys, database operations, admin saves, cache clearing, or bulk file operations.

### Catalog default sort (Run 4.176 — 2026-07-05)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-SORT-AZ-01` |
| Status | **COMPLETE** |
| Remote file | `/public_html/catalog/controller/product/category.php` |
| Change | default `p.date_added DESC` → `pd.name ASC` |
| Verification | PASS — remote SHA, HTTP 200, desktop/mobile screenshots |
| Checkpoint | `SITE-002-STABLE-PROD-SORT-AZ-01` |
| Report | [../reports/SITE-002-PROD-SORT-AZ-01.md](../reports/SITE-002-PROD-SORT-AZ-01.md) |

Proven operational boundary:

```text
single-controller-file FTP deploy with backup, dry-run, verification, rollback readiness
```

Explicit `sort`/`order` URL parameters still override defaults. Twig/CSS/JS not modified in Run 4.176.

### Catalog sort menu order (Run 4.177 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-SORT-MENU-ORDER-01` |
| Status | **COMPLETE** |
| Remote file | `/public_html/catalog/view/theme/default/template/product/category.twig` |
| Change | remove «Умолчанию»; menu order: `pd.name ASC`, `pd.name DESC`, `p.price ASC`, `p.price DESC` |
| Default sort (controller) | unchanged — `pd.name ASC` (Run 4.176) |
| Verification | PASS — remote SHA, HTTP 200, desktop/mobile screenshots |
| Checkpoint | `SITE-002-STABLE-PROD-SORT-MENU-ORDER-01` |
| Report | [../reports/SITE-002-PROD-SORT-MENU-ORDER-01.md](../reports/SITE-002-PROD-SORT-MENU-ORDER-01.md) |

Proven operational boundary:

```text
single-Twig-file FTP deploy with backup, dry-run, verification, rollback readiness
```

Does not prove multi-file frontend deploy, CSS/JS deploy, cache clearing, or database operations.

### Parallel MARS 1C cron wrapper (Run 4.178 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-WRAPPER-01` |
| Status | **PREPARED — CRON ACTIVATION PENDING** |
| Remote files | `/storage/mars-tools/cron/mars_1c_import_wrapper.php` · `/public_html/mars-tools/cron/mars_1c_http_gateway.php` |
| Legacy Sergey import | **PRESERVED** — `cronjob.php`, `import_1C*.php` untouched |
| Real import executed | **No** |
| Beget cron | **Not activated** |
| Checkpoint | `SITE-002-STABLE-PROD-CRON-WRAPPER-01` |
| Report | [../reports/SITE-002-PROD-CRON-WRAPPER-01.md](../reports/SITE-002-PROD-CRON-WRAPPER-01.md) |

Proven operational boundary:

```text
parallel MARS-only wrapper upload under mars-tools — no legacy import mutation
```

Does not prove Beget cron activation, real 1C import execution, or DB cron table changes.

### MARS 1C wrapper TXT reports (Run 4.179 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-RUN-REPORTS-01` |
| Status | **TXT REPORTING VERIFIED — CRON ACTIVATION PENDING** |
| Wrapper version | 1.1.0 |
| Reports path | `/storage/mars-tools/cron/reports/` |
| Logs path (technical) | `/storage/mars-tools/cron/logs/` |
| Report filename pattern | `mars_1c_import[_dry_run|_status]_YYYY-MM-DD_HHMMSS.txt` |
| Legacy Sergey import | **PRESERVED** |
| Real import executed | **No** |
| Beget cron | **Not activated** |
| Checkpoint | `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-01` |
| Report | [../reports/SITE-002-PROD-CRON-RUN-REPORTS-01.md](../reports/SITE-002-PROD-CRON-RUN-REPORTS-01.md) |

Proven operational boundary:

```text
MARS wrapper TXT reporting under mars-tools/reports — no legacy import mutation
```

### MARS 1C cron activation preflight (Run 4.180 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01` |
| Status | **TOKEN CONFIG READY — MANUAL RUN PENDING** |
| Local config | `/storage/mars-tools/cron/mars_1c_wrapper.local.php` (Storage secrets — not in Git) |
| Wrapper version | 1.1.0 |
| HTTP gates | dry-run/status **200** · run without token **403** |
| Input XML | `import0_1.xml` + `offers0_1.xml` present |
| Live cron DB state | **SAFE UNKNOWN** (SSH PHP CLI too old for OpenCart bootstrap) |
| Manual import executed | **No** — blocked G5/G6 |
| Beget cron | **Not activated** |
| Recommended schedule | `0 8 * * *` (Moscow → 12:00 Barnaul) |
| Legacy Sergey import | **PRESERVED** |
| Checkpoint | unchanged — `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-01` |
| Report | [../reports/SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01.md](../reports/SITE-002-PROD-CRON-ACTIVATION-PREFLIGHT-01.md) |

Proven operational boundary:

```text
MARS local token config upload only — no legacy import mutation; manual run gated on live cron DB verify
```

### MARS 1C cron manual run (Run 4.181 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-MANUAL-RUN-01` |
| Status | **MANUAL RUN VERIFIED — CRON ACTIVATION READY** |
| Wrapper version | 1.1.0 |
| Run channel | HTTP gateway (CLI PHP on SSH incompatible) |
| Run ID | `mars-20260705-205929-df82e686` |
| Catalog step | **PASS** (`import0_1.xml`) |
| Offers step | **PASS** (`offers0_1.xml`) |
| Final status | **SUCCESS** |
| TXT report | `mars_1c_import_2026-07-05_205934.txt` |
| DB pre-run | Operator phpMyAdmin confirm `active=0` |
| DB post-run live SELECT | **SAFE UNKNOWN** |
| Beget cron | **Not activated** |
| Recommended schedule | `0 8 * * *` (Moscow → 12:00 Barnaul) |
| Legacy Sergey import | **PRESERVED** |
| Checkpoint | `SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01` |
| Report | [../reports/SITE-002-PROD-CRON-MANUAL-RUN-01.md](../reports/SITE-002-PROD-CRON-MANUAL-RUN-01.md) |

Proven operational boundary:

```text
MARS wrapper manual 1C import on Production — SUCCESS — Sergey legacy preserved — Beget cron not activated
```

### MARS 1C Beget cron activation (Run 4.182 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-BEGET-ACTIVATE-01` |
| Status | **ACTIVATION READY — OPERATOR PANEL ACTION REQUIRED** |
| Wrapper gates | dry-run/status **200** · run without token **403** · lock **free** |
| Manual run prerequisite | Run 4.181 **SUCCESS** — `mars_1c_import_2026-07-05_205934.txt` |
| Cron schedule (Moscow) | `0 8 * * *` (= 12:00 Barnaul) |
| Cron command channel | HTTP gateway — `mars_1c_http_gateway.php?mode=run&token=…` |
| Token fingerprint | `7f113d` (actual command in Storage only) |
| Beget panel inspection | **SAFE UNKNOWN** — SSH `crontab` unavailable |
| Beget cron row created | **No** (operator HITL) |
| Import in this operation | **No** |
| Legacy Sergey import | **PRESERVED** |
| Checkpoint | unchanged — `SITE-002-STABLE-PROD-CRON-MANUAL-RUN-01` |
| Report | [../reports/SITE-002-PROD-CRON-BEGET-ACTIVATE-01.md](../reports/SITE-002-PROD-CRON-BEGET-ACTIVATE-01.md) |

Proven operational boundary:

```text
MARS Beget cron activation prepared — wrapper ready — panel save pending operator
```

### MARS 1C Beget cron active confirmation (Run 4.183 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01` |
| Status | **ACTIVE — DAILY IMPORT SCHEDULED / NEXT RUN MONITORING PENDING** |
| Wrapper gates | dry-run/status **200** · run without token **403** · lock **free** |
| Beget cron row | **Confirmed active** — operator-created `SITE-002 MARS 1C Import Wrapper` |
| Cron schedule | `0 8 * * *` (08:00 Moscow = 12:00 Barnaul) |
| Cron command channel | HTTP gateway — `mars_1c_http_gateway.php?mode=run&token=<TOKEN_PRESENT>` |
| Token | **Present** — not documented; rotation **not performed** (operator decision) |
| Manual run prerequisite | Run 4.181 **SUCCESS** — `mars_1c_import_2026-07-05_205934.txt` |
| Import in this operation | **No** |
| Legacy Sergey import | **PRESERVED** |
| External assum.ru cron rows | **Observed — not touched** |
| Checkpoint | `SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01` |
| Report | [../reports/SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01.md](../reports/SITE-002-PROD-CRON-BEGET-ACTIVE-CONFIRM-01.md) |

Proven operational boundary:

```text
MARS Beget daily 1C cron active — HTTP gateway — Sergey legacy preserved — next scheduled run monitoring pending
```

### MARS 1C cron reports cleanup (Run 4.184 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-REPORTS-CLEANUP-01` |
| Status | **COMPLETE — REDUNDANT TXT REPORTS REMOVED / CURRENT REPORTS PRESERVED** |
| Reports path | `/storage/mars-tools/cron/reports/` |
| Files before | **22** (index + 1 manual run + 1 latest status + 19 redundant dry-run/status) |
| Files after | **3** — `index.html`, `mars_1c_import_2026-07-05_205934.txt`, `mars_1c_import_status_2026-07-05_212740.txt` |
| Remote deletes | **19** exact TXT files (2026-07-05 dry-run/status only) |
| Backups | MARS Storage — `deployments/SITE-002-PROD-CRON-REPORTS-CLEANUP-01/backup-deleted-reports/` |
| Retention policy | Setup date: keep manual run SUCCESS + latest status + index guard; future: keep daily run reports, not every diagnostic dry-run/status |
| Import in this operation | **No** |
| Beget cron change | **No** |
| Legacy Sergey import | **PRESERVED** |
| Report | [../reports/SITE-002-PROD-CRON-REPORTS-CLEANUP-01.md](../reports/SITE-002-PROD-CRON-REPORTS-CLEANUP-01.md) |

Proven operational boundary:

```text
MARS 1C cron reports directory cleaned — current reports preserved — wrapper/logs/cron untouched
```

### MARS 1C first scheduled cron run (Run 4.194 — 2026-07-06)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-CRON-FIRST-SCHEDULED-RUN-VERIFY-01` |
| Status | **COMPLETE — FIRST SCHEDULED CRON RUN VERIFIED** |
| Scheduled time | **2026-07-06T08:00:07+03:00** (08:00 Moscow / 12:00 Barnaul) |
| Run ID | `mars-20260706-080002-09436ae7` |
| Report file | `mars_1c_import_2026-07-06_080007.txt` |
| Step 1 `1c` | **PASS** — `import0_1.xml` — 3.05 s |
| Step 2 `1c_offers` | **PASS** — `offers0_1.xml` — 2.59 s |
| Lock removed | **Yes** |
| DB active after | **0** / **0** |
| Final status | **SUCCESS** |
| Duration field | `0 seconds` — **WARN only** (step durations non-zero) |
| Daily 1C import | **OPERATIONAL** |
| Import in this operation | **No** |
| Beget cron change | **No** |
| Legacy Sergey import | **PRESERVED** |
| Checkpoint | `SITE-002-STABLE-PROD-CRON-SCHEDULED-RUN-01` (parent SEO: `SITE-002-STABLE-PROD-SITEMAP-01`) |
| Report | [../reports/SITE-002-PROD-CRON-FIRST-SCHEDULED-RUN-VERIFY-01.md](../reports/SITE-002-PROD-CRON-FIRST-SCHEDULED-RUN-VERIFY-01.md) |

Proven operational boundary:

```text
MARS Beget daily 1C cron operational — first scheduled run SUCCESS — HTTP gateway — Sergey legacy preserved
```

---

**Environment (TEST-era evidence):** TEST — https://zpm.new-site.space/
**Authority (TEST-era checkpoints):** `SITE-002-STABLE-LIVE-LOCAL-FONTS-01`
**Created:** 2026-06-19
**Purpose:** Persistent technical reference for operators and agents working on SITE-002.

**Evidence cutoff:** M9.8.9 filter recovery (06D–06M) + filter UX polish (04–08A) + tooltips (01) + Commercial Trust (03B/03C) + catalog state persistence (09A–09C) + hub cleanup (10) + operator manual polish (2026-06-21 live state) + M9.13 About Company redesign/polish/rejection/restoration (2026-06-23) + BZPM recovery closeout (2026-06-28).

---

## 0. BZPM UX Redesign — project lifecycle

| Field | Value |
|-------|--------|
| **Recovery status** | **CLOSED** (2026-06-28) |
| **Production status** | **READY AFTER OPERATOR GATES** |
| **Current phase** | **PRODUCTION PREPARATION** |
| **Next phase** | **Production Development** — production promotion after operator gates (B6/B8/B1/B3) |
| **Closeout** | [SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](../reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) |

**Lifecycle:** Research → Corporate Pages Program → Recovery (**CLOSED**) → Production Development

**M9.13 About redesign:** **RE-ACTIVATED** on TEST (2026-06-29) — live authority = `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`. Pre-redesign restore checkpoint retained as historical — see **§17**.

**Operator implementation order (remaining pages):** M9.14 Delivery **IMPLEMENTED** · M9.15 Payment **IMPLEMENTED** · M9.17 Warranty **IMPLEMENTED** · M9.16 Dealers **IMPLEMENTED** · M9.18 Custom Manufacturing **IMPLEMENTED** — Corporate Pages Program implementation phase **COMPLETE on TEST** (pending operator B6/B8).

---

## 1. Authority Rules

### Source of truth (priority order)

| # | Source | Rule |
|---|--------|------|
| 1 | **Live Production** (`bzpm.ru`) | Authoritative runtime state once Production connection verified |
| 2 | **Live TEST** (`zpm.new-site.space`) | Authoritative for TEST-era evidence and historical checkpoints |
| 3 | **Beget full backup** | Operator-controlled disaster recovery |
| 4 | **Manual UI / CSS / Twig / JS refinements** | **CANONICAL on TEST** — operator edits on live TEST override older deploy snapshots; Production parity **unverified** |
| 5 | **This Knowledge Map** | Architecture and discovered behaviour — update when new forensic evidence appears |
| 6 | **Latest Stable Checkpoint** | TEST-proven checkpoints under [../baselines/](../baselines/); Production baseline **pending** |

### Current stable state

- **Authority:** `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` (font delivery + TEST checkpoint; visual baseline from Operator Manual Polish 01 preserved)
- **Supersedes:** `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01`
- **Catalog UX cluster:** filter recovery (06D–06M) → filter UX (04–08A) → tooltips (01) → Commercial Trust (03B/03C + operator polish) → catalog state persistence (09A–09C) → hub cleanup (10)
- **About page:** M9.13 redesign + polish v1 **re-activated** on TEST (2026-06-29) — authority `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02`; prior rejection/restoration history in **§17**

### Manual UI refinements are canonical

Operator manual CSS, Twig, JS, and UX edits on live TEST are the **visual and behavioural authority**. Repo work copies (`*-work/`), prior STABLE folders, and `.pre-*.bak` from earlier passes are **historical** unless refreshed by live FTP capture.

See also **§12 Operator Manual JS Refinements** (post M9.8.9-04A/04B operator polish).

### Conflict resolution

If documentation contradicts current **Production** behaviour → verify on https://bzpm.ru/ after Production connection is authorized. If documentation contradicts **TEST-era** behaviour → **live TEST wins** for that era. Update this map and checkpoint docs after verified forensic pass.

---

## 2. 1C Architecture

### Overview

1C exchange uses two XML files and a two-step cron sequence. Live path: `1c_incoming/webdata/` (legacy `1c_exchange/` is commented out in import handlers).

| File | Cron command | Handler | Purpose |
|------|--------------|---------|---------|
| `import0_1.xml` | `1c` | `import_1C.php` | Catalog: products, categories, attributes, images, SEO |
| `offers0_1.xml` | `1c_offers` | `import_1C_offers.php` | Prices and stock: `oc_product.price`, `oc_product.quantity` |

### Cron table (`cron` — no `oc_` prefix)

| id | name | command | Purpose |
|----|------|---------|---------|
| 1 | Импорт 1C | `1c` | `import0_*.xml` |
| 2 | Импорт 1C - цены и остатки | `1c_offers` | `offers0_*.xml` |

**Task selection** (`catalog/model/catalog/cronjob.php`):

```sql
SELECT * FROM `cron`
WHERE DATE_ADD(`lastrun`, INTERVAL `duration` SECOND) < NOW()
  AND active = 1;
```

Only **one** eligible task runs per HTTP hit; on success `lastrun` is updated and loop breaks.

### Entry point

```
https://zpm.new-site.space/index.php?route=common/cronjob
```

**Controller:** `catalog/controller/common/cronjob.php`

```
ControllerCommonCronjob::index()
  → ModelCatalogCronjob::getTasks()
  → switch command:
       '1c'        → parse1C()        → include import_1C.php
       '1c_offers' → parse1COffers() → include import_1C_offers.php
  → if $itsOK → setDone(cron_id)
```

### Operator import sequence (mandatory order)

1. Upload XML to `{site_root}/1c_incoming/webdata/`
2. **Step 1 — Catalog:**
   ```sql
   UPDATE cron SET active = 0;
   UPDATE cron SET active = 1 WHERE command = '1c';
   ```
   Hit cron URL → wait for product messages → `UPDATE cron SET active = 0 WHERE command = '1c';`
3. **Step 2 — Offers:**
   ```sql
   UPDATE cron SET active = 1 WHERE command = '1c_offers';
   ```
   Hit cron URL → wait for price/qty messages → `UPDATE cron SET active = 0 WHERE command = '1c_offers';`

Post-**M9.8.9-06F** live code: offers import calls `refreshPriceIndex()` for each updated `product_id`.

### import0_1.xml — what is imported

**File:** `catalog/controller/common/import_1C.php` → `processProduct1C()` → `import_1C_process.php`

| Imported | Not imported by this stage |
|----------|---------------------------|
| `xml_id`, model, image, manufacturer | `price`, `price2`, `price3`, `discount1c` |
| status, descriptions | `oc_product_price_index` |
| categories, attributes | specials / product_discount |
| dimensions (weight, width, height, length) | |

**Does NOT call** `refreshPriceIndex()`.

### offers0_1.xml — what is imported

**File:** `catalog/controller/common/import_1C_offers.php`

| Imported | Not imported |
|----------|--------------|
| `oc_product.quantity` | `price2`, `price3`, `discount1c` |
| `oc_product.price` (base retail) | categories, attributes, status |
| `refreshPriceIndex()` per updated ID (**since 06F**) | specials |

Match key: `xml_id` → `product_id`. Unknown `xml_id` offers are silently skipped.

### SAFE UNKNOWN

- Exact ocStore/OpenCart version line
- Whether cron was re-run after every XML upload (check `cron.lastrun` vs file mtime)
- Exact `<Предложение>` count in live `offers0_1.xml` at next import

---

## 3. Product Lifecycle

```
1C export
  │
  ├─ import0_1.xml ──► cron command '1c'
  │                      └─ import_1C.php
  │                           └─ processProduct1C()
  │                                └─ oc_product (insert/update)
  │                                └─ oc_product_description
  │                                └─ oc_product_attribute
  │                                └─ oc_product_to_category
  │                                └─ oc_product_image
  │                                └─ oc_seo_url (product_id=*)
  │
  └─ offers0_1.xml ──► cron command '1c_offers'
                         └─ import_1C_offers.php
                              └─ UPDATE oc_product.price, quantity
                              └─ refreshPriceIndex(product_id)  [since 06F]
                                   └─ oc_product_price_index

Storefront read paths:
  PLP filter/sort/range ──► oc_product_price_index (via getProducts/getCategoryPriceRange)
  PDP card price        ──► getProduct() — oc_product + price2/3/discount1c/special chain
  Cart / Checkout       ──► standard OC cart (not price index)
```

### SEO

Product SEO URLs created during catalog import (`oc_seo_url` where `query LIKE 'product_id=%'`). Category SEO preserved across product reset.

#### Production SEO readiness (Run 4.188 — 2026-07-06)

| Field | Value |
|-------|--------|
| Operation | `SITE-002-PROD-SEO-READINESS-ROBOTS-01` |
| Checkpoint | `SITE-002-STABLE-PROD-SEO-ROBOTS-01` |
| robots.txt | https://bzpm.ru/robots.txt — deployed; rollback in Storage `deployments/SITE-002-PROD-SEO-READINESS-ROBOTS-01/rollback/` |
| Meta audit scope | **Non-product only** — 43 URLs; product PDP excluded |
| Meta audit result | PASS 12 · WARN 14 · FAIL 17 |
| Valid XML sitemap | **AUTO-GENERATED FEED CONFIRMED** (Run 4.214) — https://bzpm.ru/sitemap.xml — OpenCart Google Sitemap `extension/feed/google_sitemap`; physical file **absent**; `.htaccess` rewrite; live per-request; count **1377**; MARS monitor-only — no manual XML edit · [authority discovery](../reports/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md) · [enable Run 4.191](../reports/SITE-002-PROD-SITEMAP-ENABLE-01.md) |
| Non-product SEO meta fix | **INFORMATION META COMPLETE** (Run 4.199) — 4.192: technical noindex + contact/stoly · 4.193: home + category 301/322/326 admin · 4.198: authority mapped · **4.199: corp 6 controllers + `product/katalog.php` + `blog/category.php` (hub + news fallback theme_id=1) patched; category admin SEO 331/354/358 verified** |
| Product PDP meta generator | **DEPLOYED** (Run 4.201 + 4.202) — runtime fallback in `product.php`: preserve manual meta (≥80 chars, not import-stub); generate description/keywords when empty/weak; **keywords v1.1** (Run 4.202): numeric-only filter, max 18 phrases / ~300 chars, family `pickAttributePhrase` (no raw attribute dump); import-time unchanged in `import_1C_process.php`; 24 deep PDP sample: 0 empty description, 24/24 CLEAN keywords · [keywords tune](../reports/SITE-002-PROD-SEO-PRODUCT-META-KEYWORDS-TUNE-01.md) · [fix report](../reports/SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-FIX-01.md) · [discovery](../reports/SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-DISCOVERY-01.md) |
| llms.txt (AI agent guide) | **ZPM BRAND + UTF-8 BOM VERIFIED** (Run 4.205) — `/public_html/llms.txt` · https://bzpm.ru/llms.txt — public brand **ЗПМ** (not БЗПМ); UTF-8 BOM preserved; plain Markdown site summary; does not replace robots.txt or sitemap.xml · [brand remediation](../reports/SITE-002-PROD-BRAND-ZPM-REMEDIATION-01.md) · [encoding fix](../reports/SITE-002-PROD-LLMS-TXT-ENCODING-FIX-01.md) |
| Public brand policy (Production) | **ACTIVE + REGRESSION VERIFIED** (Run 4.205 + 4.206 + 4.207) — correct public Russian brand: **ЗПМ** · forbidden in public content: **БЗПМ** · domain remains **bzpm.ru** · Run 4.207: 0 forbidden brand on 66 fixed deep PLP targets |
| Final meta inventory (Production) | **COMPLETE — MINOR EDGE ISSUES** (Run 4.206) — 320 URLs crawled; sitemap 1320; robots/llms/Yandex/body verified · [report](../reports/SITE-002-PROD-SEO-META-FINAL-INVENTORY-01.md) |
| Deep PLP meta edge fix (Production) | **COMPLETE — DEEP PLP META VERIFIED** (Run 4.207) — 66 sub-category admin SEO descriptions; authority `category_description[1][meta_description]`; 0 FTP/DB · [report](../reports/SITE-002-PROD-SEO-META-EDGE-FIX-01.md) |
| PDP keyword gap follow-up (Production) | **COMPLETE — NO MUTATION REQUIRED** (Run 4.208) — 11 Run 4.206 “missing keywords” = hub/category PLP (`page--category`); 0 true PDP gaps; `product.php` v1.1 unchanged · [report](../reports/SITE-002-PROD-SEO-PRODUCT-META-GENERATOR-TUNE-02.md) |
| Sitemap delta audit (Production) | **COMPLETE — MINOR REVIEW ITEMS** (Run 4.209) — baseline 1320 (4.206) → live **1377**; +59/−2; konditerskiy-inventar catalog growth; 0 RED on added; 2 YELLOW category meta · [report](../reports/SITE-002-PROD-SITEMAP-DELTA-AUDIT-01.md) |
| New catalog branch onboarding (Production) | **COMPLETE** (Run 4.210 + 4.211) — 1C growth onboarding; admin category SEO for ids **360/361/88/141/140**; parent-aware resolution for `/lari/proizvodstvennye-lari` · [follow-up report](../reports/SITE-002-PROD-CATALOG-BRANCH-ONBOARDING-FOLLOWUP-01.md) · [Run 4.210](../reports/SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-01.md) |
| Post-1C catalog monitor (Production) | **ALLOWLIST UPDATED — ONBOARDING 0** (Runs 4.251–**4.255**) — manual folders `2026-07-10_13-27-20` → `2026-07-10_18-16-39`; classification **HYGIENE_REVIEW_REQUIRED** (onboarding needs **0**); Run **4.254** meta + Run **4.255** `ONBOARDED_CATEGORY_PATHS` nested Lari + ids **362/363** · [entrypoint onboarding](../reports/SITE-002-PROD-CATEGORY-ENTRYPOINT-ONBOARDING-01.md) · [meta onboarding](../reports/SITE-002-PROD-CATEGORY-META-ONBOARDING-01.md) · [runbook](../runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md) · [monitor](../tools/site-002-prod-post-1c-catalog-onboarding-monitor-02.py) |
| UX task intake (Production) | Task 01 **DONE** Run 4.220 — lari/konditerskiy tiles verified · Task 02 **DONE** Run 4.218 · [intake report](../reports/SITE-002-PROD-UX-TASK-INTAKE-01.md) · [entrypoints 02 report](../reports/SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02.md) |
| PDP extra info layout (Production) | **COMPLETE — EXTRA INFO BLOCK VERIFIED** (Run 4.218) — «Дополнительные сведения» display-only extraction in `product.php`; block in `producttabs.twig` after `product-content__specs-toggle-wrap`; CSS `assets/css/style.css`; meta generator preserved; 0 DB/admin/data · [report](../reports/SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01.md) · [tool](../tools/site-002-prod-pdp-extra-info-attribute-layout-01.py) · checkpoint `SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01` |
| OpenCart Document robots API | **Not available** — no `Document::setRobots()`; use `X-Robots-Tag` response header; `header.twig` hardcodes `<meta robots index,follow>` |
| Yandex Metrika / Webmaster (live Twig) | **VERIFIED** (Run 4.189) — preserved after Run 4.192 |
| Duplicate body / preloader (Production) | **FIXED** (Run 4.190) — unchanged by Run 4.192 |
| Protected Twig (operator WIP) | `catalog/view/theme/default/template/common/header.twig`, `common/footer.twig` — **DO NOT OVERWRITE / DO NOT REFORMAT** |
| Meta fix report | [SITE-002-PROD-SEO-META-FIX-01.md](../reports/SITE-002-PROD-SEO-META-FIX-01.md) |
| Sitemap report | [SITE-002-PROD-SITEMAP-ENABLE-01.md](../reports/SITE-002-PROD-SITEMAP-ENABLE-01.md) |
| Robots / meta audit report | [SITE-002-PROD-SEO-READINESS-ROBOTS-01.md](../reports/SITE-002-PROD-SEO-READINESS-ROBOTS-01.md) |

**robots.txt policy (Production):** block admin/system/storage/account/cart/checkout/search; allow `/catalog/view/` assets and `/image/`; disallow faceted query params (`sort`, `order`, `limit`, `page`, `filter_name`, `tracking`); Yandex `Clean-param: tracking`.

### Images

Physical files: `image/catalog/1c_import/`. Product reset does **not** delete image files; fresh import re-links paths.

---

## 4. Pricing System

### Fields on `oc_product`

| Field | Known role | Updated by 1C offers? |
|-------|------------|----------------------|
| `price` | Base retail price | **Yes** (`offers0_1.xml`) |
| `price2` | Dealer price (customer group mapping in `getProduct`) | **No** — not in offers import |
| `price3` | Wholesale price | **No** |
| `discount1c` | Percent discount from 1C | **No** in offers path |
| `quantity` | Stock | **Yes** |

### OpenCart standard tables

| Table | Role |
|-------|------|
| `oc_product_special` | Time-bound special prices per customer group |
| `oc_product_discount` | Quantity discounts per customer group |

### `getProduct()` price chain (PDP / cards)

Documented in live `catalog/model/catalog/product.php` captures:

1. Select base by customer group: default `price`, dealer → `price2`, wholesale → `price3`
2. Apply `discount1c` percent if > 0
3. Apply `product_discount` / `product_special` if active

**PLP filter does NOT use this chain directly** — it uses `oc_product_price_index` (see §5).

### Customer groups

- Guest / default storefront group used in filter forensic: **customer_group_id = 2**
- Index rows exist per customer group; full rebuild indexes all groups

### SAFE UNKNOWN

- Who populates `price2`, `price3`, `discount1c` in production (manual admin? separate 1C pass? legacy data?)
- Whether dealer/wholesale groups are actively used on TEST storefront
- Exact mapping of OC customer group IDs to B2B roles beyond group 2

---

## 5. Price Index System

### Table: `oc_product_price_index`

Denormalized effective prices per `product_id` × `customer_group_id`.

**Populated by:** `ModelCatalogProduct::refreshPriceIndex($product_id)` — DELETE + INSERT using `getProductForIndex()` logic (price / price2 / price3 / discount1c / specials).

### Used by (PLP / catalog filter layer)

| Feature | Method | Notes |
|---------|--------|-------|
| Price range slider min/max | `getCategoryPriceRange()` | Aggregates index; excludes `effective_price <= 0` since **06H** |
| `price_from` / `price_to` filter | `getProducts()`, `getTotalProducts()` | Uses effective price expression |
| `only_with_price` | `getProducts()` | Forces `price_from >= 1` on effective price |
| `only_discount` | `getProducts()` | Index `special` column |
| Sort `sort=p.price` | `getProducts()` ORDER BY | Effective price since **06M** |

### NOT used by

| Surface | Price source |
|---------|--------------|
| **PDP** | `getProduct()` |
| **Cart** | Cart session / OC cart model |
| **Checkout** | Cart + order totals |

### Effective price expression (current live — post 06M)

```sql
IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)
```

**Critical discovery:** `IFNULL(ppi.special, ppi.price)` treats `special = 0` (common after offers import) as effective price **0**, breaking filters. Fixed in **M9.8.9-06M**.

### M9.8.9 discoveries (preserved)

| Task | Finding | Resolution |
|------|---------|------------|
| **06D** | Category 301 had **1/419** index rows (0.24%); slider collapsed to 51280–51281 | Targeted `refreshPriceIndex` × 418 → 100% coverage; range 5405–72630 |
| **06F** | Offers import never called `refreshPriceIndex` | Hook in `import_1C_offers.php` — batch refresh after each file |
| **06H** | Zero-price SKUs («По запросу») pulled `min_price` to 0 in sidebar | `getCategoryPriceRange()` excludes `effective_price <= 0` |
| **06M** | `IFNULL(special, price)` broke `only_with_price`, price sort, combined attr+price filters | Align filter/sort/count with `IF(special > 0, …)` |

### Manual maintenance

`reindex_prices.php` at site root — loops all products via admin model. **Not** wired to cron. Use for bulk catch-up if hook missed.

---

## 6. Filter System

### Filter profiles

**Location (live):** `system/library/zpm/filter_profiles/`

**Resolver:** `system/library/zpm/filter_profile_resolver.php` — `resolveForCategory($category_id)` → profile PHP array.

| Profile file | Branch root | category_id |
|--------------|-------------|-------------|
| `301_stoly.php` | Столы | 301 |
| `322_podtovarniki.php` | Подтоварники | 322 |
| `326_telezhki.php` | Тележки | 326 |
| `80_moechnye_vanny.php` | Моечные ванны | 80 |
| `207_zonty.php` | Зонты вытяжные | 207 |
| `global_hidden.php` | Global hide list | — |

Profile schema: `primary_attribute_ids`, `secondary_attribute_ids`, `hidden_attribute_ids`, sort weights.

Controller applies profile in `getCategory()` path via `applyProfileToAttributes()`.

### Filter UI

- Form: `[data-filters-form]` inside `[data-filters]`
- Sidebar mobile: `[data-filter-sidebar]` + `[data-filter-open]` / `[data-filter-close]`
- Groups: `<section class="flt__group">`
- JS: `syncFromRanges()` writes `price_from`/`price_to` into form on init — **any attribute click submits price range too**

### Numeric attributes (M9.8.9-06J)

**Bug:** attrs **47**, **51** have **empty** `filter_name` in `oc_attribute_description` → sidebar renders `attr[51][]` (numeric key).

**Old SQL:** `ad.filter_name = '51'` → 0 rows.

**Fix (06J):** if `is_numeric($attr_slug)` → `pa.attribute_id = (int)$attr_slug`; else slug branch unchanged.

### Slug attributes

Attributes with populated `filter_name` (e.g. `construction`, `shell-size`, `table-top-material`) use:

```sql
AND ad.filter_name = '{slug}'
```

### Combined filter behaviour (06K)

Isolated `attr[51][]` URL works. Sidebar form also sends price params → before **06M** caused 0 cards. After **06M**: combined attr + `only_with_price` works on Столы (15 cards).

### SAFE UNKNOWN

- Full list of attributes with empty `filter_name` beyond 47 and 51
- Whether `len_from`/`w_from`/`h_from` dimension filters use separate SQL path (not attribute_id branch)

---

## 7. Filter Architecture

End-to-end PLP filter behaviour on live TEST (post M9.8.9 filter recovery + UX wave).

### Filter sidebar

| Layer | Location | Role |
|-------|----------|------|
| **Template** | `catalog/view/theme/default/template/sections/filterssidebar.twig` | Renders `[data-filters]` / `[data-filters-form]`; attribute groups `.flt__group`; price/LWH ranges; switches; global reset footer |
| **Mobile shell** | Same twig + `style.css` | `[data-filter-sidebar]`, open/close hooks, `.category__sidebar__overlay` |
| **Controller data** | `catalog/controller/product/category.php` | Builds `filter_groups`, `filter_subcategories`, price range, `filter_custom` from query |
| **Profiles** | `system/library/zpm/filter_profiles/*.php` | Per-branch attribute visibility and sort weights |

**Hidden subcategories policy (M9.8.9-07):** Sidebar block `<!-- SUBCATEGORIES -->` gated by `{% if false and filter_subcategories %}` — **UI only**. Controller, `filter_custom['s']`, and SQL `product_to_category` IN clause remain intact for restore.

### AJAX flow

```
User change (checkbox / range / switch / group reset / global reset)
  → syncChoiceClasses(root)          — visual .active on labels; group-reset disabled state (08A)
  → updateBrowserUrl(form)           — serialize form → query param `filters` (+ preserve sort/limit)
  → debounced updateProducts(root)   — fetch full category URL
  → parse HTML → replace .category__grid + .pagination
  → scrollToCategorySection()        — offset 0 (04B canonical)
```

Filter state is **not** a separate API — vanilla JS fetches the full PLP page and swaps grid fragments.

### `syncChoiceClasses(root)`

- Scoped to filter root `[data-filters]`
- Toggles `.active` on `.flt__check` labels from `:checked` on `.flt__check-input`
- Calls `updateGroupResetVisibility(root)` (08/08A) — `disabled` + `.is-active` on `[data-filter-group-reset]` per attribute group
- Invoked on init, checkbox change, group reset, global reset

### `updateBrowserUrl(form)`

- Reads `[data-filters-form]` fields into semicolon-separated `filters` payload (PHP `parse_str` compatible)
- Updates `history.replaceState` / URL without full navigation
- Preserves non-filter query params (`sort`, `order`, `limit`, `page`)
- Triggers debounced `updateProducts` via change handlers on checks and ranges

### `updateProducts(root)`

- `fetch(location.href)` — full category page
- Replaces `.category__grid` and `.pagination` from response
- Calls `scrollToCategorySection()` — targets category section anchor, **not** `grid.scrollIntoView` (04)
- Re-inits pagination AJAX handlers on new DOM

### Group reset (08 / 08A)

| Item | Behaviour |
|------|-----------|
| Scope | Attribute checkbox groups only (not price, LWH, switches, subcategories) |
| Trigger | `[data-filter-group-reset]` inside `.flt__group-body` (08A position) |
| Action | Uncheck panel inputs; remove `.active`; `syncChoiceClasses` → `updateBrowserUrl` |
| Visibility | Button always rendered; `disabled` when no selection; `.is-active` when group has checks |

### Global reset

- Footer control clears all checks, ranges to min/max, switches, search inputs
- Resets URL to pathname; calls `updateProducts(root)`

### Numeric attributes

Attributes with **empty** `filter_name` render as `attr[47][]`, `attr[51][]` (numeric keys). SQL branch (06J): `pa.attribute_id = (int)$slug` instead of `ad.filter_name = '{slug}'`.

### Effective price logic

PLP filter/sort/count uses `oc_product_price_index` with expression:

```sql
IF(ppi.special IS NOT NULL AND ppi.special > 0, ppi.special, ppi.price)
```

**Not** `IFNULL(special, price)` — special=0 after offers import must fall back to base price (06M).

### Price index dependency

| Operation | Index touch |
|-----------|-------------|
| Catalog import (`1c`) | **No** automatic refresh |
| Offers import (`1c_offers`) | `refreshPriceIndex(product_id)` per updated SKU (06F) |
| `getCategoryPriceRange()` | Reads index; excludes `effective_price <= 0` (06H) |
| `getProducts()` price filter/sort | Reads index effective price (06M) |

Bulk catch-up: `reindex_prices.php` at site root (manual, not cron).

**Evidence:** [SITE-002-M9.8.9-08-FILTER-GROUP-RESET-FORENSIC.md](../reports/SITE-002-M9.8.9-08-FILTER-GROUP-RESET-FORENSIC.md) · [SITE-002-M9.8.9-07-REMOVE-SUBCATEGORIES-FILTER-BLOCK.md](../reports/SITE-002-M9.8.9-07-REMOVE-SUBCATEGORIES-FILTER-BLOCK.md)

---

## 8. Live Files With Business Logic

Canonical live paths on TEST — capture before any deploy in these areas.

| File | Why it matters |
|------|----------------|
| `catalog/model/catalog/product.php` | **Filter SQL core** — `getProducts()`, `getTotalProducts()`, `getCategoryPriceRange()`; numeric attribute branch (06J); effective price expression (06M); zero-price exclusion (06H); `refreshPriceIndex()` / `getProductForIndex()` |
| `catalog/controller/common/import_1C_offers.php` | **1C offers pipeline** — updates `oc_product.price` + `quantity`; calls `refreshPriceIndex()` after each product (06F); price index stays in sync with offers XML |
| `catalog/view/theme/default/template/sections/filterssidebar.twig` | **Filter sidebar markup** — form structure, attribute groups, group-reset buttons (08/08A), subcategories hide gate (07), price/LWH ranges, global reset |
| `assets/js/main.js` | **Filter client orchestration** — `syncChoiceClasses`, `updateBrowserUrl`, `updateProducts`, `scrollToCategorySection` (04/04B), `initGroupReset` (08/08A), wishlist/compare tooltips (01), global filter reset |
| `assets/css/style.css` | **Filter + PLP + Commercial Trust presentation** — sidebar layout, `.flt__group-reset` states (08A), mobile filter shell, category grid density (operator polish), `.zpm-commercial-trust*` block (03C + operator polish), overlay coordination |
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | **Commercial Trust block markup** — category PLP CTA: header, cert podium, OEM benefits, lead form, FAQ grid (operator polish canonical) |
| `catalog/controller/product/category.php` | **Commercial Trust dynamic H2** — `$data['commercial_trust_heading']` map + `blockcommercialtrust` view load |

**Rule:** Repo `*-work/` copies and `backups/*.pre-*` are deploy artefacts — **live TEST** is authority unless freshly captured.

---

## 9. Overlay System

### Global page overlay

| Element | Hook | CSS |
|---------|------|-----|
| `.page_overlay` | `[data-overlay]` | `body.has-overlay` toggles visibility |
| Themes | `body.overlay--light` / `body.overlay--dark` | blur + rgba background |
| Scroll lock | `body.is-scroll-locked` | `position: fixed` on body |

Used as shared backdrop for multiple popups (catalog mega menu, etc.).

### Desktop catalog mega menu

| Element | Hook / class |
|---------|--------------|
| Container | `.zpm-catalog`, `.zpm-catalog__megamenu` |
| Open state | `html.is-catalog-open` |
| Data prep | `prepareMegamenuCategories()` — hides zero-count branches |

Animation: fade + `translateY(100px → 0)` per `style.css` overlay section.

### Mobile menu

| Element | Hook |
|---------|------|
| Panel | `#zpmMobileMenu`, `[data-mobile-menu]` |
| Overlay | `.zpm-mmenu__overlay`, `[data-menu-close]` |
| Trigger | `aria-controls="zpmMobileMenu"` |

### Search

| Surface | Hook |
|---------|------|
| Mobile search overlay | `.zpm-qsearch-mobile__overlay`, `[data-qsearch-mobile-close]` |

**SAFE UNKNOWN:** desktop search overlay mechanism — not fully traced in repo evidence.

### Cart dropdown

**SAFE UNKNOWN:** exact DOM hooks and JS init path for header cart dropdown — not captured in M9.8.9 forensic bundle. Likely standard theme header partial.

### Catalog filter (mobile sidebar)

| Element | Hook |
|---------|------|
| Sidebar | `[data-filter-sidebar]` |
| Open | `[data-filter-open]` |
| Close | `[data-filter-close]` |
| Inner overlay | `.category__sidebar__overlay` |

Sidebar is `aria-hidden="true"` until opened; uses popup close button pattern (`.zpm-popup_close`).

### Overlay coordination

**SAFE UNKNOWN:** whether a single `has-overlay` class coordinates all subsystems or each popup manages its own overlay layer. PLP HTML shows **two** `.page_overlay` nodes — stacking behaviour not fully documented.

---

## 10. PDP Architecture

### Gallery (M9.8.1 — PDP Gallery Compact)

- Side-rail vertical thumbs on desktop (≥1025px); horizontal reinit on smaller viewports
- Single-image SKUs: no thumbs rail
- Fancybox hooks preserved (`data-fancybox`)
- Evidence: [m9.8.1-pdp-gallery-compact-qa-result.json](../qa/m9.8.1-pdp-gallery-compact/m9.8.1-pdp-gallery-compact-qa-result.json)

### Lightbox (M9.8.2 — PDP Lightbox Constraints)

- Fancybox with constrained viewport: desktop **80vw / 80vh**; mobile **95vw / 90vh**
- `object-fit: contain` — no crop/stretch
- Class: `is_product_fancybox` on panzoom content
- Evidence: [m9.8.2-pdp-lightbox-constraints-qa-result.json](../qa/m9.8.2-pdp-lightbox-constraints/m9.8.2-pdp-lightbox-constraints-qa-result.json)

### Specifications Collapse (PDP V5.1)

- Collapsible specs block in lower PDP content
- Evidence: [SITE-002-PDP-V5.1-SPECIFICATIONS-COLLAPSE-PASS.md](../reports/SITE-002-PDP-V5.1-SPECIFICATIONS-COLLAPSE-PASS.md)

### Scroll Offset (Wave 1B)

- Anchor scroll offset for PDP section navigation
- Evidence: [SITE-002-WAVE-1B-PDP-SCROLL-SECTIONS-v1.md](../reports/SITE-002-WAVE-1B-PDP-SCROLL-SECTIONS-v1.md)

### PDP price display

Uses `getProduct()` — **not** `oc_product_price_index`. Zero price → «По запросу» display.

### PDP body category classes (2026-06-29)

- Checkpoint: `SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01`
- Controller: `catalog/controller/product/product.php` → `setProductCategoryBodyClasses()`
- Classes: `category-root-{id}` · `category-parent-{id}` from OpenCart `path` param
- **No CSS yet** — foundation for future category-specific PDP styling
- Report: [SITE-002-PDP-BODY-CATEGORY-CLASSES.md](../reports/SITE-002-PDP-BODY-CATEGORY-CLASSES.md) · §30

---

## 11. Catalog Architecture

### Products Per Page (M9.8.5)

- Selector: 10 / 20 / 50 / 100 on PLP
- Query param: `limit`
- Evidence: [m9.8.5-products-per-page-qa-result.json](../qa/m9.8.5-products-per-page/m9.8.5-products-per-page-qa-result.json)

### Filter Profiles

See §6. Per-category PHP profiles control which attributes appear in sidebar and in what order.

### Category Images (M9.7)

- Hub mode category cards with WebP images
- Evidence: M9.7 image deploy reports

### Neutral parent categories (Production Run 4.195)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01` |
| Branch IDs | `322, 331, 301, 326, 354, 358, 207, 80, 86` |
| New branches | 331 Полки настенные и настольные · 354 Тележки-шпильки и противни · 358 Шкафы и лари · 86 Стеллажи |
| Tile authority | `system/library/zpm/category_visibility.php` → `$neutral_hub_branch_ids` |
| Homepage cards | `buildHomepageCategoryCards()` — 9 `zpm-cat-card` |
| Hub cards | `category.php` hub mode — same list |
| Megamenu tiles | `prepareMegamenuCategories()` — already dynamic (9) |
| Images | `image/catalog/Category-image/{slug}.webp` — **COMPOSER_ONLY_NO_API** |
| Checkpoint | `SITE-002-STABLE-PROD-NEUTRAL-PARENT-CATEGORIES-01` |
| Report | [SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01.md](../reports/SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01.md) |

### Pending new section entry points (intake Run 4.217)

| Field | Value |
|-------|-------|
| Sections | **Лари** (category_id **88**) · **Кондитерский инвентарь** (category_id **360**) |
| Live PLP | HTTP 200; meta onboarded (Runs 4.210–4.211) |
| Megamenu | Present |
| Homepage/hub `zpm-cat-card` | **10 tiles** (Run 4.236) — IDs `322,331,301,326,354,358,207,80,86,360`; **88** Лари removed from parent tiles; **358** kept |
| Display sort | **А → Я** by Russian name (Run 4.221) — `sortCategoriesByRussianName()` |
| Future implementation | **COMPLETE** Run 4.220 + **4.221** — whitelist + images + A→Z display · [4.220 report](../reports/SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02.md) · [4.221 report](../reports/SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01.md) · [tool](../tools/site-002-prod-category-entrypoints-sort-az-01.py) |
| Intake report | [SITE-002-PROD-UX-TASK-INTAKE-01.md](../reports/SITE-002-PROD-UX-TASK-INTAKE-01.md) |

### PDP attribute «Дополнительные сведения» (Run 4.218 — LIVE)

| Field | Value |
|-------|-------|
| Rule | Attribute **«Дополнительные сведения»** is **not** rendered in `spec-table`; shown as `product-content__extra-info` immediately after `product-content__specs-toggle-wrap` |
| Controller | `/public_html/catalog/controller/product/product.php` — `$data['extra_info_attribute']` extracted from display `attribute_groups` **after** meta generator + `super_atts` |
| Twig authority | `/public_html/catalog/view/theme/default/template/product/producttabs.twig` (not `product.twig`) |
| CSS | `/public_html/assets/css/style.css` — `.product-content__extra-info`, `.product-extra-info__title`, `.product-extra-info__text` |
| Data / DB / admin | **No changes** — display-only |
| Meta generator | Uses unfiltered `$attribute_groups` at load time — **preserved** |
| Modification overlays | **Absent** for PDP controller/template |
| Rollback | `source-before/` in deployment folder — re-upload 3 files |
| Checkpoint | `SITE-002-STABLE-PROD-PDP-EXTRA-INFO-LAYOUT-01` |
| Report | [SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01.md](../reports/SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01.md) |
| Intake (historical) | [SITE-002-PROD-UX-TASK-INTAKE-01.md](../reports/SITE-002-PROD-UX-TASK-INTAKE-01.md) — 66/100 sample prevalence |

### Neutral category image white-bg refresh (Production Run 4.196)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01` |
| Refreshed IDs | 354 Тележки-шпильки и противни · 358 Шкафы и лари · 86 Стеллажи |
| Kept unchanged | 331 Полки настенные и настольные |
| Deploy | FTP overwrite masters `image/catalog/Category-image/*.webp` + cache `image/cache/...-300x300.webp` |
| Admin saves | **0** |
| Generation | **COMPOSER_ONLY_NO_API** + Pillow normalize |
| Checkpoint | `SITE-002-STABLE-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-01` |
| Report | [SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01.md](../reports/SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01.md) |

### Polki category image fix (Production Run 4.197)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01` |
| Refreshed ID | 331 Полки настенные и настольные |
| Deploy | FTP overwrite master `polki-nastennye-i-nastolnye.webp` + cache `polki-nastennye-i-nastolnye-300x300.webp` |
| Root cause | Stale dark OpenCart cache served on tiles while master passed corner heuristic in 4.196 |
| Admin saves | **0** |
| Generation | **COMPOSER_ONLY_NO_API** + Pillow normalize |
| Checkpoint | `SITE-002-STABLE-PROD-POLKI-CATEGORY-IMAGE-01` |
| Report | [SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01.md](../reports/SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01.md) |

### Megamenu (M9.7)

- `prepareMegamenuCategories()` filters empty branches
- Template: `catalog/view/theme/default/template/common/megamenu.twig`
- Evidence: [REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md](../reports/REPORT-BZPM-M9.7C-IMAGE-DEPLOY-MEGAMENU-CLEANUP.md)

### PLP Layout (Category V2.x)

- Grid / list view switcher (desktop ≥1025)
- List card compactness passes V2.1–V2.3
- Scoped CSS: `.page--category`, `.category--view-list`
- Operator manual PLP polish (canonical)

### Hub Mode (M9.5)

- Parent categories show subcategory hub instead of flat product grid where configured

---

## 12. Operator Manual JS Refinements

**Registered:** M9.8.9-04B (2026-06-19) — operator manual edits on live TEST **after** M9.8.9-04A deploy pass.

**Policy:** Manual JS refinements on live TEST are **canonical**. Repo work copies, pass reports (including 04A), and deploy snapshots describe **historical** deploy state unless refreshed by live capture.

### Filter scroll offset

| Item | M9.8.9-04A report | Live canonical (post operator edit) |
|------|-------------------|-------------------------------------|
| `scrollToCategorySection()` offset | `15px` (fixed) | **`0`** |
| Location | `assets/js/main.js` | same |

Operator set offset to **0** on live. Treat **0** as authoritative for filter/AJAX scroll-to-category behaviour.

**Prior pass evidence (historical):** [SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md](../reports/SITE-002-M9.8.9-04A-FILTER-SCROLL-OFFSET-TUNING.md)

### Sticky header trigger

Operator manually adjusted the sticky header appearance threshold in `assets/js/main.js` on live TEST.

| Item | Status |
|------|--------|
| File | `assets/js/main.js` |
| Change type | Manual threshold tweak (sticky header show/hide) |
| Exact value | **SAFE UNKNOWN** — not captured in repo at registration time |
| Canonical | Live TEST behaviour |

### Pre-task rule (header / filter JS)

Before **any** JS task touching header sticky behaviour or catalog filter scroll:

1. **Verify live** `assets/js/main.js` on TEST (FTP capture or operator confirmation) — do not assume 04A report values.
2. Confirm current `scrollToCategorySection()` offset (canonical: **0**).
3. Confirm sticky header trigger matches live UX; document exact threshold if captured.
4. Treat operator manual JS as override over pass reports and work copies.

**Registration report:** [SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md](../reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md)

---

## 13. Operational Rules

### PRE-TASK RULE (mandatory — all SITE-002 tasks)

Before **any** SITE-002 task:

1. **Read** this Technical Knowledge Map
2. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Verify Authority State** matches checkpoint name
4. **Check Active Roadmap Stage** — [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)
5. **Only then** perform audit or changes

### PRE-TASK RULE UPDATE (domain-specific — filters / sort / pagination / limit / only_with_price)

Before **any** task touching **filters**, **sort**, **pagination**, **limit**, or **only_with_price**:

1. **Read** this Technical Knowledge Map — **§16 Catalog State Persistence** (mandatory)
2. **Read** pass reports **M9.8.9-09A**, **M9.8.9-09B**, **M9.8.9-09C** as mandatory context
3. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
4. Test **interaction paths** — filter AJAX → limit click; limit → filter; full combo with sort + page — not only full-page URL loads

### PRE-TASK RULE UPDATE (domain-specific — About page)

Before **any** task touching the **About page** (`/about`, `information/about`) or planning a **new About redesign**:

1. **Read** this Technical Knowledge Map — **§17 About Page History** (mandatory)
2. **Read** [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md)
3. **Read** [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md)
4. **Read** [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md)
5. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
6. Treat **restored version** on live TEST as **source of truth** — M9.13 work copies are historical reference only

### PRE-TASK RULE UPDATE (domain-specific — filters / catalog / 1C / price / PLP)

Before **any** task touching **filters**, **catalog**, **1C import**, **price**, or **PLP**:

1. **Read** this Technical Knowledge Map — especially **§5 Price Index**, **§6 Filter System**, **§7 Filter Architecture**, **§8 Live Files With Business Logic**, **§16 Catalog State Persistence**
2. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Live-capture** the specific business-logic files in scope (`product.php`, `import_1C_offers.php`, `filterssidebar.twig`, `main.js`, `style.css`, `category.php`) before deploy
4. Test isolated URL params **and** sidebar form submit; test `only_with_price` + attribute combos; verify price range min ≠ 0 when zero-price SKUs exist

### PRE-TASK RULE UPDATE (domain-specific — Commercial Trust / CTA)

Before **any** task touching **trust block**, **certificates**, **dealers form**, or **category CTA**:

1. **Read** this Technical Knowledge Map — **§14 Commercial Trust Block**
2. **Read** the latest Stable Checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Live-capture** `blockcommercialtrust.twig`, `style.css`, `category.php` before deploy — do not trust 03C work copies or pass reports alone
4. Verify dynamic H2 on at least one mapped category + fallback category
5. Treat operator manual CSS/Twig on live as **canonical** over repo work copies

### Deploy rules (summary)

- Live FTP capture + SHA256 before any write
- Backup to `backups/*.pre-<pass>.bak`
- Clear Twig cache after deploy
- Document rollback in report
- See [SITE-002-WORKING-RULES.md](../SITE-002-WORKING-RULES.md)

### 1C import rules

- Always: catalog (`1c`) **before** offers (`1c_offers`)
- Deactivate cron tasks after each step
- Post-import verify: product count, index coverage, sample PLP price range
- Never assume index is current without checking `oc_product_price_index` row count

### 1C catalog growth onboarding (Run 4.210 + 4.211)

- Daily 1C import may add categories/products — **normal growth**, not default garbage
- New sitemap URLs → classify: PRODUCT_PDP vs CATEGORY_PLP vs CATEGORY_HUB vs TECHNICAL
- **Onboard** new category PLP/hub (admin `meta_description` only) — do **not** delete/hide/noindex by default
- PDP meta → product generator track; category PLP meta → admin category SEO track
- Post-import monitoring: diff sitemap for new CATEGORY_PLP with missing meta — tool `site-002-prod-post-1c-catalog-onboarding-monitor-02.py`; **local scheduler verified** (Run 4.216) via `site-002-post-1c-monitor-runner.ps1` + Windows Task `MARS_SITE_002_Post_1C_Catalog_Monitor` — **enabled**; hardened artifacts **CONFIRMED_MANUALLY** Run 4.251/4.252/4.255; Run **4.255** allowlist nested Lari paths + ids **362/363**; manual run `2026-07-10_18-16-39` — classification **HYGIENE_REVIEW_REQUIRED**, onboarding needs **0** · [entrypoint report](../reports/SITE-002-PROD-CATEGORY-ENTRYPOINT-ONBOARDING-01.md) · [meta report](../reports/SITE-002-PROD-CATEGORY-META-ONBOARDING-01.md) · [runbook](../runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md) · **runner sync to `X:\AI MARS` recommended**
- Onboarded 2026-07-07: category ids **360** (konditerskiy-inventar), **361** (formy-konditerskie), **88** (lari), **141** (skladskie-lari), **140** (proizvodstvennye-lari under Лари)
- **Parent-aware resolution** required when admin names duplicate (e.g. «Производственные» id 140 under Лари vs id 130 under Шкафы)
- Deferred Run 4.210 `/lari/proizvodstvennye-lari` — **RESOLVED** Run 4.211 → category_id **140**, HIGH confidence

### Category Lari reparent discovery (Run 4.234)

- **Лари** category_id **88** — current `parent_id=79` (direct under neutral hub); **wrong** vs 1C business grouping
- **Шкафы и лари** category_id **358** — sibling under 79; current child **359** (Шкафы кухонные)
- **Target:** `88.parent_id = 358` → public path `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari`
- **Children of 88:** **140** Производственные, **141** Складские — `category_path` cascade required
- **SEO keyword** `lari` unchanged (`oc_seo_url` single-segment); full path from `category_path`
- Tool: `site-002-prod-category-lari-reparent-discovery-01.py` · [report](../reports/SITE-002-PROD-CATEGORY-LARI-REPARENT-DISCOVERY-01.md)

### Category Lari reparent implementation (Run 4.235)

- **Status:** **ACTIVE — LARI CONFIRMED** (Run 4.248 + Run 4.250 quick recheck PASS; post-import revert not observed)
- **DB:** `88.parent_id=358`; `category_path` rebuilt for **88/140/141**
- **Canonical URL:** `/katalog/nejtralnoe-oborudovanie/shkafy-i-lari/lari`
- **Redirects:** `.htaccess` 301 old flat `/lari` tree → nested
- **Root cause (nested→flat):** `seo_pro.php` `validate()` used stale `cache.category.seopath` (old `79_88` path) — fixed by cache purge + `getPathByCategory()` now reads `oc_category_path`
- **Patched files:** `seo_pro.php`, `seo_url.php`, `category_visibility.php`, `category.php`, `.htaccess`
- **Entrypoints:** nested **Лари** page/redirect/sitemap from Run 4.235 **unchanged**; parent tile **88** removed Run 4.236
- Tool: `site-002-prod-category-lari-reparent-implementation-01.py` · [report](../reports/SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01.md) · [checkpoint](../baselines/SITE-002-STABLE-PROD-CATEGORY-LARI-REPARENT-01.md)

### Parent Category Tiles Lari removal (Run 4.236)

- **Terminology:** Parent Category Tiles / Витрина родительских категорий
- **Status:** **COMPLETE**
- **Patch:** removed **88** from `$neutral_hub_branch_ids` in `category_visibility.php`
- **After:** homepage + neutral hub **10** `zpm-cat-card` tiles; **358** Шкафы и лари present; standalone **Лари** parent tile absent
- **Unchanged:** **Лари** child on `/shkafy-i-lari`; nested URL **200**; old flat **301**; no DB/SEO/redirect edits
- Tool: `site-002-prod-parent-category-tiles-lari-removal-01.py` · [report](../reports/SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md) · [checkpoint](../baselines/SITE-002-STABLE-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md)

### Sitemap authority (Run 4.214)

- **Authority:** OpenCart built-in Google Sitemap feed — `catalog/controller/extension/feed/google_sitemap.php`
- **Route:** `extension/feed/google_sitemap` · public URL `https://bzpm.ru/sitemap.xml` via `.htaccess` `RewriteRule ^sitemap.xml$ index.php?route=extension/feed/google_sitemap [L]`
- **Physical file:** `/public_html/sitemap.xml` — **absent** (not manually maintained)
- **Generation:** live per HTTP request from catalog models — **no** feed-level cache, **no** disk write
- **Data sources:** `getProducts()` (status=1), recursive `getCategories()` (status=1), `getInformations()` (status=1), `getManufacturers()` — URLs via `url->link()` + SEO rewrite
- **Noindex/canonical:** **not** checked in feed — external SEO audit required for mismatches
- **1C relationship:** daily import updates DB → sitemap reflects on next fetch; **no** manual regeneration by MARS
- **MARS policy:** monitor/audit delta only; **never** hand-edit `sitemap.xml` in normal ops; onboard new categories via admin SEO, do not remove new URLs by default
- Tool: `site-002-prod-sitemap-authority-discovery-01.py` · [report](../reports/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md)

### Full Tech SEO Audit (Run 4.241)

- **Status:** **COMPLETE — READ-ONLY** (2026-07-10)
- **Scope:** 1417 URL HTTP crawl; meta/canonical/H1; internal links; assets/images; sitemap/robots/llms; catalog 237 categories + 1156 products; information/forms static; brand scan; security surface; DB + FTP cross-check
- **Result:** 1408/1408 sitemap URLs HTTP **200**; **0** broken internal links; **0** public **БЗПМ**; **0** broken core CSS/JS
- **Accepted:** `/contact` canonical; `/kontakty` 404; post-1C verification pending (Run 4.240)
- **Top hygiene items:** ~~flat Lari URLs without 301~~ **resolved** Run 4.242; ~~7 legacy `index.php?route=information` sitemap entries~~ **fixed** Run 4.243; ~~optional `/contact` sitemap inclusion~~ **fixed** Run 4.243; missing alt bulk (deferred)
- **Issue register:** Storage `audits/SITE-002-PROD-FULL-TECH-SEO-AUDIT-01/issue-register/` (11 items: P2×3, P3×5, P4×3)
- **AUDIT-006:** **resolved** Run 4.242 — flat Lari **301** confirmed; Run 4.241 false positive (urllib auto-follow)
- **AUDIT-007:** **fixed** Run 4.243 — sitemap emits route-based `information/*` pretty URLs
- **AUDIT-004:** **fixed** Run 4.243 — redundant `compare-products`/`wishlist` seo_url rows removed
- **AUDIT-002:** **fixed** Run 4.243 — `/contact` in sitemap
- **AUDIT-008:** **fixed** Run 4.244 — meta description on `/about_us`, `/brands/assum`, `/terms`
- **AUDIT-009:** **fixed** Run 4.244 — H1 on `/brands/assum`
- **Roadmap:** Storage `audits/SITE-002-PROD-FULL-TECH-SEO-AUDIT-01/roadmap/`
- **Checkpoint:** unchanged `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`
- Tool: `site-002-prod-full-tech-seo-audit-01.py` · [report](../reports/SITE-002-PROD-FULL-TECH-SEO-AUDIT-01.md)

### Audit Wave C Redirect Hygiene (Run 4.242)

- **Status:** **COMPLETE — NO-OP** (2026-07-10)
- **Scope:** verify AUDIT-006 flat Lari **301** + optional AUDIT-010 bare `/index.php` alias; read-only HTTP (curl), FTP source mirrors, DB SELECT
- **Result:** all 3 flat Lari URLs **301** to nested; nested **200**; bare `/index.php` **301** to `/`; `index.php?route=...` functional; **0** mutation
- **Authority:** Run 4.235 `.htaccess` rules active since Lari reparent
- **Checkpoint:** unchanged `SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`
- Tool: `site-002-prod-audit-wave-c-redirect-hygiene-01.py` · [report](../reports/SITE-002-PROD-AUDIT-WAVE-C-REDIRECT-HYGIENE-01.md)

### Audit Wave B SEO Foundation (Run 4.243)

- **Status:** **COMPLETE** (2026-07-10)
- **Scope:** sitemap controller patch for route-based `information/*` URLs; scoped DELETE of redundant `compare-products`/`wishlist` seo_url rows; `/contact` sitemap inclusion
- **Result:** sitemap 1408→**1409**; **0** legacy `index.php?route=information` URLs; `/contact` present; 1 FTP upload; 2 seo_url rows deleted (928/927) with backup
- **`google_sitemap.php`:** emits distinct `information/*` routes from `oc_seo_url`; skips migrated legacy `information_id` 6/9/10/11/12/13/14
- **Checkpoint:** `SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01`
- Tool: `site-002-prod-audit-wave-b-seo-foundation-01.py` · mirror `google_sitemap-site-002-prod-audit-wave-b-seo-foundation-01.php` · [report](../reports/SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md)

### Audit Wave E Info Meta H1 (Run 4.244)

- **Status:** **COMPLETE** (2026-07-10)
- **Scope:** AUDIT-008 missing meta on `/about_us`, `/brands/assum`, `/terms`; AUDIT-009 missing H1 on `/brands/assum`
- **Owners:** `oc_information_description` id **4** + **5** (about_us, terms); Assum = `manufacturer_id=11` via `product/manufacturer.php` + `manufacturer_info.twig`
- **Result:** 2 DB `meta_description` updates; 2 FTP uploads (Assum scoped `setDescription` + brand PLP `h2`→`h1`); regression **PASS**; public **БЗПМ** **0**
- **Checkpoint:** `SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01`
- Tool: `site-002-prod-audit-wave-e-info-meta-h1-01.py` · mirrors `manufacturer-site-002-prod-audit-wave-e-info-meta-h1-01.php`, `manufacturer_info-site-002-prod-audit-wave-e-info-meta-h1-01.twig` · [report](../reports/SITE-002-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md)

### Post-1C monitor scheduler (Run 4.215 / 4.216)

- **1C import:** automatic Beget cron **08:00 Moscow** / **12:00 Barnaul**
- **Sitemap:** automatic OpenCart feed (see § above) — no manual XML edit
- **MARS monitor:** read-only Python monitor; **automatic locally** after operator install+enable (Run 4.216 verified)
- **Runner:** `site-002-post-1c-monitor-runner.ps1` — uses call-operator for paths with spaces (`X:\AI MARS`); logs under `X:\AI MARS STORAGE\...\scheduled-monitors\post-1c\`
- **Task name:** `MARS_SITE_002_Post_1C_Catalog_Monitor` — **enabled**; LastTaskResult **0** expected on success; **2** = execution failure (historically path quoting)
- **Recommended schedule:** **12:30 Barnaul** (30 min after import)
- **Server cron alternative:** deferred — separate operation required
- **Forbidden from monitor flow:** delete/hide/noindex, sitemap edit, production mutation
- [runner fix report](../reports/SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01.md) · [readiness report](../reports/SITE-002-POST-1C-MONITOR-SCHEDULER-READINESS-01.md) · [runbook](../runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md)

### Filter change rules

- Test both isolated URL params and sidebar form submit
- Test `only_with_price` + attribute combo
- Test numeric (`attr[51][]`) and slug (`attr[construction][]`) keys
- Verify `getCategoryPriceRange` min ≠ 0 when zero-price SKUs exist

---

## 14. Commercial Trust Block

Category PLP decision-stage block — after product grid, before footer. **Live TEST is canonical**; M9.8.9-03C deploy + operator manual polish registered in `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` (catalog UX carried forward from Commercial Trust 01 / Catalog UX Complete 01).

### Purpose

Convert post-catalog evaluation into trust + lead capture: manufacturer proof (OEM, certs, «Сделано в России»), procurement reassurance, and price-list request form (`dialog=7`).

**Scope:** category PLP (`blockcommercialtrust.twig` + FAQ grid). Homepage uses **`blockcommercialtrust_home.twig`** (same trust card, home copy, **no** FAQ grid) since checkpoint `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01`. `/katalog` retains legacy `blockdealersform.twig` (`zpm-dealers`). PDP, filters — **out of scope**.

### Structure (live canonical — 2026-06-21 capture)

```
section.zpm-commercial-trust[data-commercial-trust]
└── .container → .zpm-commercial-trust__card
    └── .zpm-commercial-trust__wrap (flex row)
        ├── .zpm-commercial-trust__info
        │   ├── .zpm-commercial-trust__header — label + H2 + lead
        │   └── .zpm-commercial-trust__main
        │       ├── .zpm-commercial-trust__cert-col — cert on podium (sert-base.jpg)
        │       └── .zpm-commercial-trust__benefits — 3 OEM benefit rows
        └── .zpm-commercial-trust__form-wrap
            ├── .zpm-decoration-with-logo — decor-logo.svg background contours
            └── .zpm-commercial-trust__form-col → form card (dialog=7)

section.zpm-catalog-faq
└── .zpm-commercial-trust__services--like-FAQ
    ├── «Частые вопросы» heading
    └── .zpm-commercial-trust__services — 8 FAQ cards (4-col grid desktop)
```

**Mobile stack:** header → cert → benefits → form → FAQ grid (2 columns ≤1024px).

### Files

| File | Role |
|------|------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust.twig` | Markup — trust card + FAQ section |
| `catalog/controller/product/category.php` | Loads view; sets `commercial_trust_heading` |
| `assets/css/style.css` | Block `M9.8.9-03C` CSS + operator polish (podium, cert size, form, FAQ grid, logo decor) |
| `assets/img/certificates/thumb_00.png` | Visible certificate thumb |
| `assets/img/certificates/certificat_00.jpg` | Fancybox full-size target |
| `assets/img/sert-base.jpg` | Certificate podium base |
| `assets/img/decor-logo.svg` | Background logo contours in form wrap |

**Not used on live block:** `main.js` changes for Commercial Trust — form uses existing `zpm-form` / mask / validation patterns.

### Dynamic headings

`category.php` maps category name → H2:

| Category name | H2 |
|---------------|-----|
| Столы | Нужна помощь с выбором столов? |
| Моечные ванны | Нужна помощь с выбором моечных ванн? |
| Подтоварники и подставки | Нужна помощь с выбором подтоварников и подставок? |
| Тележки сервировочные | Нужна помощь с выбором тележек? |
| Зонты вытяжные | Нужна помощь с выбором зонтов? |
| **Fallback** | Подберём оборудование под вашу задачу |

Twig: `{{ commercial_trust_heading|default('Подберём оборудование под вашу задачу') }}`

### Certificate

| Item | Live behaviour |
|------|----------------|
| Visible count | **1** slide in `.swiper.js-commercial-trust-certs` |
| Display | Enlarged on podium (`__cert-card--base` + `sert-base.jpg`); `max-width: 250px` on cert card |
| Interaction | Fancybox `data-fancybox="certificates-plp"` on cert link |
| «Все сертификаты» | **Not present** on live twig (removed in operator polish) |

**SAFE UNKNOWN:** whether hidden `certificat_01` should return for multi-doc tenders.

### Form

| Item | Value |
|------|-------|
| Endpoint | `POST` `dialog=7` (existing dealers/lead handler) |
| Title | «Получить прайс-лист» |
| Fields | name, phone (`data-mask="phone"`), email, message (Комментарий), agree checkbox |
| Submit | «Отправить заявку» |
| Visual | Backdrop-blur card; decor logo behind form wrap |

**Preserved:** field IDs/names, privacy links, `zpm-form` classes — backend-safe.

### FAQ grid

8 service cards with `fad` icons — catalog gaps, full price list, custom sizes, lead times, dealers, documentation, project fit, nationwide delivery.

CSS: `.zpm-commercial-trust__services` — `grid-template-columns: repeat(4, 1fr)` desktop; `repeat(2, 1fr)` ≤1024px.

### Change rules

Before **any** edit to trust block, certificates strip, dealers form, or category CTA:

1. Read **§14** (this section)
2. Read latest stable checkpoint — [SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md)
3. **Live-capture** `blockcommercialtrust.twig`, `style.css`, `category.php` — do not trust 03C work copies or pass reports alone
4. Operator manual CSS/Twig on live **override** repo work copies
5. Clear Twig cache after twig deploy
6. Test at least one mapped category + fallback category PLP

**Evidence:** [SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md](../reports/SITE-002-M9.8.9-03B-COMMERCIAL-TRUST-BLOCK-REDESIGN.md) · [SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md](../reports/SITE-002-M9.8.9-03C-COMMERCIAL-TRUST-BLOCK-IMPLEMENTATION.md) · [live-capture 2026-06-21](../reports/m9.8.9-commercial-trust-checkpoint-work/live-capture/)

---

## 15. Page Intro Block (`page-intro`)

Shared H1 strip rendered **above `<main>`** via header partial — not inside `category.twig`.

### Render chain

| Step | File | Role |
|------|------|------|
| 1 | Controller sets `Pageintro` | `$pageintro->title`, `$pageintro->description` |
| 2 | `Pageintro::render()` | Emits `<section class="page-intro">` HTML (incl. optional `.page-intro__description`) |
| 3 | `$this->document->setPageintro(...)` | Stores rendered HTML on document |
| 4 | `catalog/controller/common/header.php` | `$data['pageintro'] = $this->document->getPageintro()` |
| 5 | `catalog/view/theme/default/template/common/header.twig` | `{% if pageintro %}{{ pageintro }}{% endif %}` after breadcrumbs |

**Important:** `$data['description']` in `category.php` (from `oc_category_description`) is the **SEO/category body block below the grid** — **not** the same as `$pageintro->description`.

### Data sources by route

| Route / page | Controller | `$pageintro->description` source | Live (post M9.8.9-10) |
|--------------|------------|--------------------------------|------------------------|
| `/katalog` | `catalog/controller/product/katalog.php` | Hardcoded string | **Present** — «Для предприятий общественного питания…» |
| Category PLP (branch) | `catalog/controller/product/category.php` | Always `''` | **Absent** |
| Neutral hub `/katalog/nejtralnoe-oborudovanie` | `category.php` + `$is_hub` | Was hardcoded M9.5 hub copy; **removed M9.8.9-10** | **Absent** |
| PDP | `product.php` | **SAFE UNKNOWN** — no forensic in this pass | **Absent** on sampled PLPs |
| Wishlist / compare / account | respective controllers | Usually `''` | **Absent** when empty |

Hub intro text was **controller logic**, not CMS category description, not language file, not twig override per category.

### M9.8.9-10 change

Removed hub-only hardcoded string from `category.php`; all category routes now set `$pageintro->description = ''`. **`katalog.php` unchanged** — catalog root keeps its intro line.

**Evidence:** [SITE-002-M9.8.9-10-PAGE-INTRO-DESCRIPTION-REMOVAL.md](../reports/SITE-002-M9.8.9-10-PAGE-INTRO-DESCRIPTION-REMOVAL.md)

---

## 16. Catalog State Persistence

PLP query-state model on live TEST (post M9.8.9-09A / 09B / 09C). **Joint behaviour:** `filter` + `limit` + `sort` + `pagination` + `only_with_price` work together when combined via sidebar AJAX, limit menu, sort buttons, and pagination.

### State model

| Param | Role | Set by |
|-------|------|--------|
| `filters` | Semicolon-separated filter payload (`only_with_price=1`, `attr[51][]=…`, `price_from`/`price_to`, etc.) | Sidebar form → JS `updateBrowserUrl()` |
| `limit` | Products per page (15 / 25 / 50 / 100 on live) | Limit menu `<a href>` or preserved in URL |
| `sort` | Sort field (e.g. `p.price`) | Sort button `data-sort` → JS URL merge |
| `order` | Sort direction (`ASC` / `DESC`) | Sort button `data-sort` → JS URL merge |
| `page` | Pagination page index | Pagination links or `initPaginationAJAX` merge |

**Fetch model:** filter changes do **not** call a separate filter API — `updateProducts()` fetches the **full category page** at current `location.href` and swaps DOM fragments.

### `updateBrowserUrl(form)`

**File:** `assets/js/main.js`

- Reads `[data-filters-form]` fields into semicolon-separated `filters` string
- Merges into existing `URLSearchParams(window.location.search)` — **preserves** `limit`, `sort`, `order`, `page`, and other query keys
- Updates `filters` only (set or delete)
- Applies `history.replaceState` without full navigation
- Triggers debounced `updateProducts(root)`

**Since 09A:** replaced naive `pathname + "?filters=" + stateText` rebuild that dropped non-filter params.

### `updateProducts(root)`

**File:** `assets/js/main.js`

```
fetch(location.href) — full category page
  → parse HTML response
  → replace .category__grid innerHTML
  → replace .pagination outerHTML (or insert/remove)
  → replace .category__limit outerHTML + initCategoryLimitMenu()  [since 09C]
  → scrollToCategorySection()
  → initPaginationAJAX(root)
  → initLoadMore(root)  [Production Run 4.185]
```

**Since 09C:** limit toolbar refresh closes the 09B gap — after filter AJAX, limit hrefs match server-rendered filtered URLs.

**Since Run 4.185 (Production):** `initLoadMore()` appends next-page `.p-card` elements on «Показать ещё» click; counter `[data-load-more-counter]` shows «Показано X из Y»; numeric `.pagination__pages` hidden when `<html>` has class `js-load-more`.

### `category__limit` refresh

| Layer | Role |
|-------|------|
| **PHP** | `category.php` builds `$data['limits'][]['href']` — appends `&filters=` when request carries `filters` (09A) |
| **Twig** | `category.twig` — `.category__limit` menu with `<a href="{{ l.href }}">` |
| **JS (09C)** | After AJAX, swap `.category__limit` from fetched HTML; call `initCategoryLimitMenu()` to re-bind dropdown toggle |

**09B discovery:** pagination was already refreshed after filter AJAX; limit menu was **not** — operator path filter→limit click used stale plain-page hrefs.

### Pagination refresh

| Layer | Role |
|-------|------|
| **PHP** | `category.php` pagination `$url` includes `filters` when present (09A) |
| **JS** | `updateProducts()` replaces `.pagination` from response; `initPaginationAJAX` merges `page` into current browser URL on click; **`initLoadMore`** fetches `data-next` and **appends** `.p-card` to grid (Run 4.185) |
| **Counter** | `category.twig` — `[data-load-more-counter]` with `product_total` / `product_shown` from `category.php` |
| **CSS** | `.js-load-more .pagination__pages { display: none }` — numeric pagination not primary UI when JS active |

Post-filter AJAX, pagination links in fetched HTML include `filters` — consistent with full-page filtered load.

### Sort behaviour

Sort toolbar uses `<button data-sort="sort=…&order=…">` — **not** server-rendered hrefs.

JS click handler merges sort params into `window.location.href` (which already contains `filters` after sidebar toggle). Sort path was unaffected by 09A/09C limit bug.

### PHP URL generation (09A)

**File:** `catalog/controller/product/category.php`

In sort, limit, and pagination `$url` assembly blocks:

```php
if (isset($this->request->get['filters'])) {
    $url .= '&filters=' . $this->request->get['filters'];
}
```

Ensures full-page navigation links (limit menu, pagination) carry active filter state when request URL includes `filters`.

### Interaction matrix (registered behaviour)

| Scenario | Expected | Mechanism |
|----------|----------|-----------|
| Toggle filter at `?limit=50` | Both params in URL | `updateBrowserUrl()` merge (09A) |
| Filter AJAX → click limit 50 | Filter persists | Limit href refreshed from response (09C) |
| Set limit → toggle filter | Limit persists | `updateBrowserUrl()` merge (09A) |
| Filter + sort + page combo | All params coexist | Sort JS merge + PHP pagination URLs + 09C limit refresh |
| `only_with_price` + attribute + limit | Combined `filters` + `limit` | Full stack |

### Change rules

Before **any** edit to catalog URL state, limit menu, pagination AJAX, or filter sidebar submit chain:

1. Read **§16** (this section) and **§7 Filter Architecture**
2. Read **09A / 09B / 09C** pass reports
3. Live-capture `assets/js/main.js` and `catalog/controller/product/category.php`
4. QA **interaction paths** — not only direct URL loads

**Evidence:** [SITE-002-M9.8.9-09A-FILTER-LIMIT-PERSISTENCE-HOTFIX.md](../reports/SITE-002-M9.8.9-09A-FILTER-LIMIT-PERSISTENCE-HOTFIX.md) · [SITE-002-M9.8.9-09B-LIMIT-LINK-FORENSIC-AFTER-HOTFIX.md](../reports/SITE-002-M9.8.9-09B-LIMIT-LINK-FORENSIC-AFTER-HOTFIX.md) · [SITE-002-M9.8.9-09C-LIMIT-TOOLBAR-AJAX-REFRESH-HOTFIX.md](../reports/SITE-002-M9.8.9-09C-LIMIT-TOOLBAR-AJAX-REFRESH-HOTFIX.md)

**SAFE UNKNOWN:** M9.8.9-09C browser QA Q1–Q6 — automated probe PASS; operator interaction HITL **PENDING**. Mobile filter shell separate limit control — not probed in 09C.

---

## 17. About Page History

Corporate page `/about` — route `information/about`. **Current canonical state = M9.13 redesign + polish v1 re-activated** on live TEST (2026-06-29).

### 1. Original page (pre-M9.13)

| Item | Value |
|------|--------|
| **Route** | `information/about` |
| **Controller** | `catalog/controller/information/about.php` |
| **Twig** | `catalog/view/theme/default/template/information/about.twig` |
| **Structure** | Legacy layout — `about-page--main-wrap`, video hero (`about-page-video`), metrics, certificate Swiper, dealer form, geo block (`geo-web.png`) |
| **Hero image** | `assets/img/about-page-img.jpg` |
| **CSS** | Scoped rules in `assets/css/style.css` (no `zpm-about-*` namespace) |

This structure was live before M9.13 redesign (2026-06-23).

### 2. M9.13 redesign

| Item | Value |
|------|--------|
| **Status** | **IMPLEMENTED** · **QA PASSED** · **REJECTED BY OPERATOR** |
| **Scope** | 6-section compact concept — `zpm-about-hero`, company, advantages, certs, geo, CTA |
| **Files changed** | `about.twig`, `about.php`, `style.css` (`zpm-about-page*` block) |
| **Evidence** | [SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-REDESIGN-IMPLEMENTATION.md) |
| **Work copies** | `reports/m9.13-work/` |
| **Backups** | `backups/*.pre-m9.13-about-redesign.bak` |

Removed legacy blocks: video hero, metrics cards, cert slider, dealer section, advantage partials.

### 3. M9.13 polish

| Item | Value |
|------|--------|
| **Status** | **IMPLEMENTED** · **QA PASSED** · **REJECTED WITH REDESIGN** |
| **Scope** | Hero trust row, spacing, cert column sizing, hero + logistics image upgrades |
| **Files changed** | `about.twig`, `style.css`, `about-page-img.jpg`; **new** `about-logistics.jpg` |
| **Evidence** | [SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-POLISH-PASS-V1.md) |
| **Work copies** | `reports/m9.13-polish-work/` |
| **Backups** | `backups/*.pre-m9.13-about-polish-v1.bak` |

Structure unchanged from redesign — polish only.

### 4. Operator review

| Item | Value |
|------|--------|
| **Decision** | **REJECTED** — M9.13 redesign/polish not accepted for production |
| **Classification** | Operator visual evaluation — not a technical deploy failure |
| **Implication** | Redesign work copies remain **historical reference**; live must return to pre-redesign |

### 5. Restoration

| Item | Value |
|------|--------|
| **Status** | **RESTORED** · **QA PASSED** |
| **Type** | **Operator-approved restoration** — **not** rollback failure |
| **Date** | 2026-06-23 |
| **Script** | `reports/m9.13-restore-work/m913-about-restore-to-pre-redesign.py` |
| **Evidence** | [SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md](../reports/SITE-002-M9.13-ABOUT-COMPANY-RESTORE-TO-PRE-REDESIGN.md) |

**Restored from:** `backups/*.pre-m9.13-about-redesign.bak` (+ `about-page-img.jpg` from polish backup — same pre-redesign bytes).

**Removed:** `assets/img/about-logistics.jpg` (polish-only asset).

**SHA verified** against redesign pre-deploy manifest — restored files match pre-M9.13 state.

### 6. Re-activation (2026-06-29)

| Item | Value |
|------|--------|
| **Status** | **RE-ACTIVATED** · **QA PASSED** · **HITL PENDING** |
| **Type** | Saved M9.13 implementation restored — **not** new redesign |
| **Script** | `reports/m9.13-restore-v2-work/m913-about-restore-redesign-v2.py` |
| **Merge policy** | Live operator CSS (Local Fonts 01 + Operator Manual Polish 01) preserved; M9.13 `zpm-about-page*` block merged |
| **Evidence** | [SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md](../reports/SITE-002-ABOUT-COMPANY-REDESIGN-RESTORE-V2.md) |

**Deployed from:** `reports/m9.13-work/` (twig, php, css block) + `reports/m9.13-polish-work/assets/img/` (hero, logistics).

**Backups:** `backups/*.pre-site-002-about-restore-v2.bak`

### 7. Current canonical state

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/about |
| **Structure** | **M9.13 compact 6-section** — `zpm-about-hero` … `zpm-about-cta` |
| **M9.13 namespaces** | **Present** on live |
| **Source of truth** | Live TEST M9.13 redesign + polish v1 |
| **Authority** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` |

### Change rules

Before **any** edit to About page:

1. Read **§17** (this section)
2. Read redesign, polish, and restore-v2 reports (listed above)
3. **Live-capture** `about.twig`, `about.php`, `style.css` before deploy
4. Operator manual CSS/Twig/JS on non-About pages remains **CANONICAL** — merge carefully for About-only changes
5. Rollback: `m913-about-rollback-restore-v2.py` or `.pre-site-002-about-restore-v2.bak` files

**Evidence:** [SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-REDESIGN-02.md](../reports/SITE-002-STABLE-CHECKPOINT-M9.13-ABOUT-REDESIGN-02.md) · [SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md](../baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md)

**SAFE UNKNOWN:** Form POST end-to-end on TEST — operator smoke test pending. Operator visual HITL @ 1440 / 1024 / 390 pending.

---

## 18. Delivery Page (M9.14)

Corporate page `/delivery` — route `information/delivery`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/delivery |
| **Route** | `information/delivery` |
| **SEO** | `oc_seo_url` keyword `delivery` → `information/delivery` |
| **Controller** | `catalog/controller/information/delivery.php` |
| **Twig** | `catalog/view/theme/default/template/information/delivery.twig` |
| **CSS namespace** | `zpm-delivery-page`, `zpm-delivery-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — scoped `[data-delivery-faq]` |
| **Copy** | [BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md](../copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01` (page domain only) |

### Structure

Pageintro (H1 + Lead) → shipment points → organization (summary row) → methods → 7-step timeline → packaging → Russia coverage → outcomes → TK table → FAQ (8) → Commercial Trust CTA + form (region required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Forbidden on page:** map · calculator · TK logos · Басовская · mid-page primary submit

### Change rules

1. Read [SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION-CHARTER-v1.md) and **§18**
2. Live-capture remote files before deploy
3. Do not bleed scope into About, Contacts, catalog, or other corp pages

**Evidence:** [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](../reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.14-DELIVERY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.14-DELIVERY-01.md) · `reports/m9.14-work/`

---

## 19. Payment Page (M9.15)

Corporate page `/payment-methods` — route `information/payment`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/payment-methods |
| **Route** | `information/payment` |
| **SEO** | `oc_seo_url` keyword `payment-methods` → `information/payment` |
| **Controller** | `catalog/controller/information/payment.php` |
| **Twig** | `catalog/view/theme/default/template/information/payment.twig` |
| **CSS namespace** | `zpm-payment-page`, `zpm-payment-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-delivery-faq], [data-payment-faq]` |
| **Copy** | [BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md](../copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01` (page domain only) |

### Structure

Pageintro (H1 + Lead) → 6-step payment timeline (step 6 = Подготовка к отгрузке + Delivery handoff) → payment methods + summary table → document proof cards (5) → legal entity strip → FAQ (8) → Commercial Trust CTA + form (company required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` + company field — **not** contact card grid or map
- **Delivery:** one-line / step-6 handoff only — **not** TK tables, shipment points, or logistics timeline
- **Forbidden on page:** bank widgets · payment logos · QR · Moscow warehouse detail · freight/logistics bodies

### Change rules

1. Read [BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/BZPM-M9.15-PAYMENT-DESIGN-CHARTER-v1.md) and **§19**
2. Live-capture remote files before deploy
3. Do not bleed scope into About, Delivery, Contacts, catalog, or other corp pages

**Evidence:** [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](../reports/SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md](../baselines/SITE-002-STABLE-LIVE-M9.15-PAYMENT-01.md) · `reports/m9.15-work/`

---

## 20. Warranty Page (M9.17)

Corporate page `/guarantee` — route `information/guarantee`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/guarantee |
| **Route** | `information/guarantee` |
| **SEO** | `oc_seo_url` keyword `guarantee` → `information/guarantee` (id 1048; prior `information_id=11`) |
| **Controller** | `catalog/controller/information/guarantee.php` |
| **Twig** | `catalog/view/theme/default/template/information/guarantee.twig` |
| **CSS namespace** | `zpm-warranty-page`, `zpm-warranty-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-delivery-faq], [data-payment-faq], [data-warranty-faq]` |
| **Copy** | [BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md](../copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01` (page domain only) |

### Structure

Pageintro (H1 + Lead) → warranty principles + coverage (BLOCK 01) → document checklist (BLOCK 02) → 5-step claim timeline (BLOCK 03) → verification cases (BLOCK 04) → service outcomes (BLOCK 05) → FAQ (8) → Commercial Trust CTA + service form (equipment_model required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Delivery:** outbound/RMA pointers only — **not** TK tables or shipment points
- **Payment:** deal-docs pointer only — **not** methods matrix or bank detail
- **Forbidden on page:** term badge without OQ-W01 · ASC map · fear exclusion walls · warranty certificate hero · photo upload MVP

### Change rules

1. Read [SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION-CHARTER-v1.md) and **§20**
2. Live-capture remote files before deploy
3. Do not bleed scope into About, Delivery, Payment, Contacts, catalog, or other corp pages

**Evidence:** [SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](../reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md](../baselines/SITE-002-STABLE-LIVE-M9.17-WARRANTY-01.md) · `reports/m9.17-work/`

---

## 21. Dealers Page (M9.16)

Corporate page `/dealers` — route `information/dealers`. **Implemented on live TEST** (2026-06-28).

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/dealers |
| **Route** | `information/dealers` |
| **SEO** | `oc_seo_url` keyword `dealers` → `information/dealers` (id 1049; prior `information_id=10`) |
| **Controller** | `catalog/controller/information/dealers.php` |
| **Twig** | `catalog/view/theme/default/template/information/dealers.twig` |
| **CSS namespace** | `zpm-dealers-page`, `zpm-dealers-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-delivery-faq], [data-payment-faq], [data-warranty-faq], [data-dealers-faq]` |
| **Copy** | [BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md](../copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) |
| **Authority** | `SITE-002-STABLE-LIVE-M9.16-DEALERS-01` (page domain only) |

### Structure (target)

Pageintro (H1 + Lead) → optional trust strip → partner matrix (SC-13) → OEM proof (BLOCK 02) → partner outcomes → 5-step timeline → supply chain + cross-links → FAQ (8) → Commercial Trust CTA + qualification form (company + city required).

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap on corp page — **not** full PLP trust block; **do not** edit PLP `blockdealersform.twig` in M9.16 scope
- **Delivery / Payment / Warranty:** one-line summaries + links only — **not** embedded sibling bodies
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Forbidden on page:** form-as-hero · discount map · franchise aesthetics · territory map · partner logo wall · СНГ geography

### Governance (B3)

Standalone `/dealers` corp page = **primary qualification surface** per charter. PLP dealer form reconciliation = **separate future task** — operator blocker **B3** is governance-only for M9.16 implementation start.

### Change rules

1. Read [SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION-CHARTER-v1.md) and **§21**
2. Live-capture remote files before deploy
3. Do not bleed scope into PLP dealer form unless operator opens dedicated B3 task

**Evidence:** [SITE-002-M9.16-DEALERS-IMPLEMENTATION.md](../reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION.md) · [SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md](../baselines/SITE-002-STABLE-LIVE-M9.16-DEALERS-01.md) · `reports/m9.16-work/`

---

## 22. Custom Manufacturing Page (M9.18)

Corporate page `/custom-equipment` — route `information/custom_equipment`. **IMPLEMENTED** on live TEST (2026-06-28). Checkpoint **`SITE-002-STABLE-LIVE-M9.18-CUSTOM-01`**.

| Item | Value |
|------|--------|
| **Live URL** | https://zpm.new-site.space/custom-equipment |
| **Route** | `information/custom_equipment` |
| **SEO** | `oc_seo_url` keyword `custom-equipment` → `information/custom_equipment` (id 1042; prior `information_id=14`) |
| **Legacy CMS** | Information id **14** — orphaned, not deleted |
| **Controller** | `catalog/controller/information/custom_equipment.php` |
| **Twig** | `catalog/view/theme/default/template/information/custom_equipment.twig` |
| **CSS namespace** | `zpm-custom-page`, `zpm-custom-*`, shared `zpm-corp-timeline`, `zpm-corp-faq` |
| **JS** | Corp FAQ accordion in `assets/js/main.js` — `[data-custom-faq]` in selector list |
| **Copy** | [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md](../copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md) |
| **Charter** | [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md) |
| **Implementation** | [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md) |
| **Checkpoint** | [SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md](../baselines/SITE-002-STABLE-LIVE-M9.18-CUSTOM-01.md) |

### Structure (target)

Pageintro (H1 + Lead) → when custom needed (BLOCK 01 + BLOCK 02) → scope + OEM proof (BLOCK 03 + BLOCK 04) → **8-step process timeline** (BLOCK 05 — dominant) → requirements + materials (BLOCK 06 + BLOCK 07) → project outcomes (BLOCK 08 — second emphasis) → FAQ (8) → Commercial Trust CTA + custom form (company, contact, phone, email, project_description required; **no upload MVP**).

**Proof strip (BLOCK 04):** `.zpm-custom-oem__proof-strip` uses **Commercial Trust service cards** (checkpoint `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`) — see **§31**.

### Reuse boundaries

- **Commercial Trust:** CTA card + form wrap — **not** full PLP trust block
- **Contacts:** `zpm-form` discipline — **not** contact card grid or map
- **Delivery / Payment / Warranty / Dealers:** one-line summaries + links only — **not** embedded sibling bodies
- **Catalog:** text links and scope bridge — **not** PLP grid or prices
- **Forbidden on page:** calculator/configurator · file upload MVP · price/lead badges · tender portal UX · fake case gallery · universal AISI table hero

### Program note

M9.18 is the **terminal** Corporate Pages Program implementation milestone. After stable checkpoint, corp implementation phase for M9.14–M9.18 (About restoration separate) is **complete on TEST** — pending operator gates B6/B8 for formal sign-off.

### Change rules

1. Read [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md](../reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION-CHARTER-v1.md) and **§22**
2. Live-capture remote files before deploy
3. Do not bleed scope into sibling corp pages or catalog templates

**Evidence:** [BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md](../reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [reports/m9.18-work/deploy-manifest.json](../reports/m9.18-work/deploy-manifest.json) · [qa/m9.18-custom-screenshots/](../qa/m9.18-custom-screenshots/)

---

## Document maintenance

| When | Action |
|------|--------|
| New stable checkpoint | Update §1 authority reference |
| New forensic pass | Add row to relevant § + evidence link |
| Live code change | Update affected §; note SHA in pass report |
| SAFE UNKNOWN resolved | Replace with evidence; remove UNKNOWN label |

---

## 23. Corporate Pages Visual Polish (Pass 1)

**Scope:** M9.14–M9.18 corporate routes on TEST — CSS-only spacing alignment to Home tokens.

| Item | Value |
|------|--------|
| **Status** | **REJECTED BY OPERATOR** (2026-06-28) — rolled back on TEST |
| **Checkpoint** | `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01` — **historical / not active visual authority** |
| **Current visual authority** | **Pre-Pass-1** — `style.css` SHA256 `8ad9397e52b44fb784c6e911031c1a68f2dbc6f83fe7597b53b3ec922dd1886c` |
| **Audit** | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md) — **TRACKED** (Scope A closeout 2026-06-30) |
| **Implementation report** | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01.md) |
| **Rollback report** | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01-ROLLBACK.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-01-ROLLBACK.md) |
| **Rejected patch** | [site-002-corp-visual-polish-pass1.css](../reports/site-002-visual-polish-pass1-work/site-002-corp-visual-polish-pass1.css) |
| **Pre-Pass-1 backup** | [backups/style.css.pre-site-002-corp-visual-polish-pass1.bak](../backups/style.css.pre-site-002-corp-visual-polish-pass1.bak) |
| **Rejected-state backup** | [backups/style.css.rejected-site-002-corp-visual-polish-pass1.bak](../backups/style.css.rejected-site-002-corp-visual-polish-pass1.bak) |
| **Rejected post_sha256** | `d4303c40d972135c092f5b8803b148b37e80881ac6f6db9e76a220995115ca42` |

**Rejection reason:** global `padding-top: 0` on corporate sections (VP-01) removed vertical rhythm.

**Next:** Pass 1.1 — see §24.

---

## 24. Corporate Pages Visual Polish Pass 1.1

**Scope:** M9.14–M9.18 — CSS + Twig lead migration; Home token rhythm.

| Item | Value |
|------|--------|
| **Status** | **SUPERSEDED** by Pass 1.2 (2026-06-28) — retained as prior checkpoint |
| **Checkpoint** | `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1` |
| **Live CSS post SHA256** | `e83dae3e08c30969cce68e366fa7f0b7dbf4ca80e3df204644ac87c40de80b5d` |
| **Report** | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.1.md) |

### Operator rules (still binding)

- **RULE 01** — `.page-intro__description` forbidden on M9.14–M9.18; lead in `main` via `.zpm-corp-page-lead`.
- **RULE 02** — Reuse `.zpm-commercial-trust` and `.zpm-catalog-faq` families.
- **RULE 03** — Home is visual authority (not Catalog/PDP).
- **RULE 04** — No global `padding-top: 0` on corporate sections.
- **RULE 05** — Beget + file backups + git checkpoint before each pass.

---

## 25. Corporate Pages Visual Polish Pass 1.2 — superseded

**Scope:** M9.14–M9.18 — CSS-only fine rhythm pass on TEST.

| Item | Value |
|------|--------|
| **Status** | **SUPERSEDED** by Operator Manual Polish 01 (2026-06-29) — **do not use as visual reference** |
| **Checkpoint** | `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` — historical |
| **Pass 1.2 CSS post SHA256** | `243d6d5e2a1ad00c06c450f4b90dc72adb1671b64a681f266675abdbd9330252` |
| **Report** | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](../baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md) |
| **Pre-deploy backup** | [backups/style.css.pre-site-002-corp-visual-polish-pass1.2.bak](../backups/style.css.pre-site-002-corp-visual-polish-pass1.2.bak) |
| **Audit (input)** | [SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md](../reports/SITE-002-CORPORATE-PAGES-VISUAL-POLISH-AUDIT-v1.md) |

Pass 1 (`SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-01`) remains **REJECTED** — see §23.

**Active authority:** §27 Local Fonts 01.

---

## 26. Operator Manual Polish 01 — superseded (visual baseline retained)

**Scope:** Full TEST storefront after operator manual polish following Visual Polish Pass 1.2.

| Item | Value |
|------|--------|
| **Status** | **SUPERSEDED for checkpoint authority** (2026-06-29) by Local Fonts 01 — **visual/behavioural baseline preserved** |
| **Checkpoint** | `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` |
| **Live CSS SHA256** | `1d190d97953cfaab17bb1f9948e0eecafb777710d7c1ba613a35181b28e88a86` |
| **Live JS SHA256** | `17cb1fffe8831d4ac633d5bd41e047c31b4fd478a0e1cfa67c8667c42ab539e8` |
| **Report** | [SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md](../reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md](../baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md) |
| **Capture manifest** | [capture-manifest.json](../reports/site-002-operator-manual-polish-01-work/capture-manifest.json) |
| **Backups** | `backups/*.pre-site-002-operator-manual-polish-01.bak` |

### Operator manual delta vs Pass 1.2

| File | Changed vs Pass 1.2 |
|------|---------------------|
| `assets/css/style.css` | **YES** |
| `catalog/view/theme/default/template/information/dealers.twig` | **YES** (vs Pass 1.1 deploy snapshot) |
| Other captured corp twig/php | **NO** at capture time |

### Forbidden for future tasks

- Pass 1.2 CSS/HTML/JS as reference baseline
- Pre-checkpoint repo work copies unless refreshed from this capture

---

## 27. Local Fonts 01 — active

**Scope:** Eliminate FOUT/FOIT — 100% local Inter webfonts on TEST; no Google Fonts / CDN font CSS.

| Item | Value |
|------|--------|
| **Status** | **ACTIVE on TEST** (2026-06-29) — **SITE-002 checkpoint authority** |
| **Checkpoint** | `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` |
| **Visual baseline** | Preserved from Operator Manual Polish 01 — typography tokens unchanged |
| **Live CSS SHA256** | `78c6e13b17632e8f8638515af5141c8a79c432ff45e215e75d56c5b3430635d7` |
| **Report** | [SITE-002-LOCAL-FONTS-MIGRATION.md](../reports/SITE-002-LOCAL-FONTS-MIGRATION.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md](../baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md) |
| **Deploy manifest** | [deploy-manifest.json](../reports/local-fonts-work/deploy-manifest.json) |
| **Pre-deploy backups** | `backups/*.pre-site-002-local-fonts-01.bak` |

### Font inventory (local)

| Weight | File | Preload |
|--------|------|---------|
| 400 | `Inter-Regular.woff2` (+ `.woff`) | **yes** |
| 500 | `Inter-Medium.woff2` (+ `.woff`) | **yes** |
| 600 | `Inter-SemiBold.woff2` (+ `.woff`) | no |
| 700 | `Inter-Bold.woff2` | no |
| 800 | `Inter-ExtraBold.woff2` | no |

### `@font-face` location

- Primary: top of `assets/css/style.css`
- Mirror: `assets/css/style.min.css` (file commented out in `header.twig`)

### Preload (header.twig)

```html
<link rel="preload" href="/assets/fonts/Inter-Regular.woff2" as="font" type="font/woff2" crossorigin />
<link rel="preload" href="/assets/fonts/Inter-Medium.woff2" as="font" type="font/woff2" crossorigin />
```

---

## 28. Home Commercial Trust 01 — active

**Scope:** Home CTA band only — replaces legacy `zpm-dealers` dealers teaser with catalog `zpm-commercial-trust` card (first section only).

| Item | Value |
|------|--------|
| **Status** | **ACTIVE on TEST** (2026-06-29) |
| **Checkpoint** | `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` |
| **Report** | [SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md](../reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](../baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md) |
| **Deploy manifest** | [fix-manifest-20260628-193747.json](../reports/home-commercial-trust-work/fix-manifest-20260628-193747.json) |
| **Pre-deploy backups** | `backups/*.pre-home-commercial-trust-01.bak` |

### Files

| File | Role |
|------|------|
| `catalog/view/theme/default/template/sections/blockcommercialtrust_home.twig` | Home trust card markup |
| `catalog/controller/common/home.php` | `$data['blockdealersform'] = load('sections/blockcommercialtrust_home')` |
| `catalog/view/theme/default/template/sections/blockdealersform.twig` | **Legacy** — still used on `/katalog` only |
| `assets/css/style.css` | Existing `.zpm-commercial-trust*` — **no Home-specific CSS patch** |

### JS hook

Dual class on Home section: `zpm-commercial-trust zpm-dealers` + `data-dealers` — preserves `.zpm-dealers[data-dealers] .zpm-form` handler without `main.js` edits.

### Rollback

`reports/home-commercial-trust-work/site-002-home-commercial-trust-rollback.py`

---

## 29. Corporate Intro Image Blocks 01 — active

**Scope:** Visual intro blocks (image 1/3 + text 2/3) on About + M9.14–M9.18 corporate pages.

| Item | Value |
|------|--------|
| **Status** | **ACTIVE / PASS on TEST** (2026-06-29 closeout) — all 6 intro assets HTTP 200 |
| **Checkpoint** | `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01` |
| **Report** | [SITE-002-CORPORATE-INTRO-BLOCKS-01.md](../reports/SITE-002-CORPORATE-INTRO-BLOCKS-01.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01.md](../baselines/SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01.md) |
| **Deploy** | [corporate-intro-blocks-work/deploy-manifest.json](../reports/corporate-intro-blocks-work/deploy-manifest.json) |
| **Pre-deploy backups** | `backups/*.pre-site-002-corp-intro-blocks-01.bak` |

### Markup

- Class shell: `.zpm-corp-page-lead.zpm-corp-intro` + `aria-label="Вводная информация"`
- Grid: `.zpm-corp-intro__grid` — desktop `1fr 2fr`; mobile stacked
- Assets path: `/assets/img/corporate/{page}-intro.jpg`
- About hero image remains `/assets/img/about-page-img.jpg` (not intro asset)
- Custom OEM proof strip remains `/assets/img/about-page-img.jpg`

### CSS

Append marker: `SITE-002 — Corporate intro image blocks (zpm-corp-intro)` in `assets/css/style.css`

### Rollback

`reports/corporate-intro-blocks-work/site-002-corp-intro-blocks-rollback.py`

---

## 30. PDP Body Category Classes 01 — active

**Scope:** Additive `<body>` classes on product pages for future category-specific CSS. **No visual change.**

| Item | Value |
|------|--------|
| **Status** | **ACTIVE / PASS on TEST** (2026-06-29) |
| **Checkpoint** | `SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01` |
| **Report** | [SITE-002-PDP-BODY-CATEGORY-CLASSES.md](../reports/SITE-002-PDP-BODY-CATEGORY-CLASSES.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01.md](../baselines/SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01.md) |
| **Deploy** | [pdp-body-category-classes-work/deploy-manifest.json](../reports/pdp-body-category-classes-work/deploy-manifest.json) |
| **Pre-deploy backup** | `backups/catalog__controller__product__product.php.pre-pdp-body-category-classes.bak` |

### Body class format

```
page page--product category-root-{root_id} category-parent-{parent_id}
```

- **Source:** OpenCart `path` query parameter (same chain as PDP breadcrumbs)
- **Root:** first segment of `path`
- **Parent:** second segment of `path` (second-level category)
- **Missing path:** only `page page--product` — no category classes (SAFE UNKNOWN for DB-only resolution)

### Controller

| File | Method |
|------|--------|
| `catalog/controller/product/product.php` | `setProductCategoryBodyClasses()` (private) |

### Rollback

`reports/pdp-body-category-classes-work/site-002-pdp-body-category-classes-rollback.py`

---

## 31. Custom OEM Proof Strip — Commercial Trust Reuse (ACTIVE)

**Checkpoint:** `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`
**Scope:** `/custom-equipment` — `.zpm-custom-oem__proof-strip` only
**Status:** **ACTIVE / PASS** (2026-06-29)

| Item | Value |
|------|--------|
| **Pattern authority** | `.zpm-commercial-trust__services` card grid (Home / catalog FAQ) |
| **Wrapper** | `.zpm-custom-oem__proof-strip` — margin + 3-col grid override only |
| **Twig** | `catalog/view/theme/default/template/information/custom_equipment.twig` |
| **CSS** | Append block in `assets/css/style.css` — `SITE-002 — Custom OEM proof strip → commercial trust services reuse` |
| **Icons** | `fad fa-industry` · `fad fa-file-certificate` · `fad fa-th-large` |
| **Report** | [SITE-002-CUSTOM-PROOF-STRIP-RESTYLE.md](../reports/SITE-002-CUSTOM-PROOF-STRIP-RESTYLE.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01.md](../baselines/SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01.md) |
| **Rollback** | `reports/custom-proof-strip-work/site-002-custom-proof-strip-rollback.py` |

**Change rules:** Reuse Commercial Trust service classes; do not invent new card markup. Sibling corp pages **out of scope**.

---

## 32. Delivery Summary — Commercial Trust Reuse (ACTIVE)

**Checkpoint:** `SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01`
**Scope:** `/delivery` — `.zpm-delivery-summary` only
**Status:** **ACTIVE / PASS** (2026-06-29)

| Item | Value |
|------|--------|
| **Pattern authority** | `.zpm-commercial-trust__services` card grid (Home / catalog FAQ) |
| **Wrapper** | `.zpm-delivery-summary` — margin reset + 4-col grid override only |
| **Twig** | `catalog/view/theme/default/template/information/delivery.twig` |
| **CSS** | Append block in `assets/css/style.css` — `SITE-002 — Delivery summary → commercial trust services reuse` |
| **Icons** | `fad fa-map-marked-alt` · `fad fa-warehouse` · `fad fa-shipping-fast` · `fad fa-user-headset` |
| **Report** | [SITE-002-DELIVERY-SUMMARY-RESTYLE.md](../reports/SITE-002-DELIVERY-SUMMARY-RESTYLE.md) |
| **Baseline** | [SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01.md](../baselines/SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01.md) |
| **Rollback** | `reports/delivery-summary-work/site-002-delivery-summary-rollback.py` |

**Change rules:** Reuse Commercial Trust service classes; content meaning unchanged; sibling corp pages **out of scope**.

---

## 33. Mail Recipients Architecture (Production — ACTIVE)

**Discovery:** Run 4.186 — `SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01` (2026-07-06)
**Confirmation:** Run 4.187 — `SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01` (2026-07-06)
**Status:** **ACTIVE — admin-managed via OpenCart Mail Alert Emails; no code deploy**

| Item | Production value |
|------|------------------|
| **Unified form handler** | `catalog/controller/checkout/anketa.php` — `ControllerCheckoutAnketa::index()` |
| **Frontend route** | `POST /index.php?route=checkout/anketa` via `assets/js/main.js` (`sendForm`, `processSubmission`) |
| **Form markup** | `zpm-form` + hidden `dialog` (1/2/3/5/7) in Fancybox, PLP Commercial Trust, corporate `corpcta-form-*` partials |
| **Security** | CSRF session token + Google reCAPTCHA v3 |
| **DB persist** | `catalog/model/checkout/anketa.php` → `addanketa()` |
| **Active recipients** | OpenCart setting **`config_mail_alert_email`** — comma-separated; loop in anketa + order alert |
| **Admin path** | **System → Settings → Mail → Additional Alert Emails** (*Дополнительные адреса оповещения*) |
| **Operator update** | Run 4.187 — recipient list updated in admin; delivery verified by operator |
| **From / SMTP** | OpenCart mail settings (`config_email`, `config_mail_*`) — **unchanged** (Run 4.187) |
| **Order admin alerts** | `catalog/controller/mail/order.php` → `config_email` + same `config_mail_alert_email` when `config_mail_alert` includes `order` |
| **Native contact** | `information/contact.php` → `config_email` only (no alert list) |
| **Legacy dead code** | hardcoded `$to` recipient — **removed** in Run 4.224 |
| **Multi-recipient** | **Supported** via comma-separated admin setting |
| **Custom admin section** | **Not implemented** — not required; optional future phase only for differentiated per-flow recipients |
| **Discovery report** | [SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01.md](../reports/SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01.md) |
| **Confirmation report** | [SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01.md](../reports/SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01.md) |
| **Storage artefacts** | Discovery: `.../SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01\` · Confirmation: `.../SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01\` |

**Change rules:** Recipients are managed through OpenCart native Mail Alert Emails — do not hardcode in `anketa.php` unless admin path is unavailable. Do not edit anketa/mail paths during unrelated catalog/cron work. Verify CSRF + reCAPTCHA after any anketa change. Mask recipient emails in reports.

---

## 34. Mail System Architecture (Production — CUSTOMER FORMS ACTIVE)

**Discovery:** Run 4.222 — `SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01` (2026-07-08)
**Admin forms integration:** Run 4.224 — `SITE-002-PROD-MAIL-ADMIN-FORMS-01` (2026-07-08)
**Inbox confirmation:** Run 4.225 — `SITE-002-PROD-MAIL-ADMIN-FORMS-INBOX-CONFIRMATION-01` (2026-07-08)
**Customer forms integration:** Run 4.226 — `SITE-002-PROD-MAIL-CUSTOMER-FORMS-01` (2026-07-08)
**Customer delivery confirmation:** Run 4.231 — `SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01` (2026-07-09) — controlled submit dialog 11 `ok: true` with operator mailbox `i***@mail.ru`
**Customer inbox confirmation:** Run 4.232 — `SITE-002-PROD-MAIL-CUSTOMER-FORMS-INBOX-CONFIRMATION-01` (2026-07-09) — operator verified delivery/design/no service info issue
**Status:** **ACTIVE — admin + conditional customer form mail operator-verified; form loading UX; standard OC mails unchanged**

| Item | Production value |
|------|------------------|
| **Form mail handler** | `catalog/controller/checkout/anketa.php` — `renderAdminForm()` + conditional `renderCustomerFormConfirmation()` |
| **Subject (admin)** | `ЗПМ: новая заявка — {dialog_label}` |
| **Subject (customer)** | `ЗПМ: заявка получена — {dialog_label}` |
| **Dialogs** | 1 product question · 2 callback · 3 price · 5 review · 7 dealers/wholesale |
| **Frontend** | `zpm-form` → `POST checkout/anketa` via `main.js`; CSRF + reCAPTCHA v3; **`zpm-form--loading`** + abort on modal close |
| **Admin recipients** | `config_mail_alert_email` (Run 4.186/4.187) — unchanged |
| **Customer recipient rule** | posted valid **email** OR logged-in customer account email; else skip (not error) |
| **Service info in admin mail** | **active** — IP, UA, browser, device, OS, referrer, page URL, dialog, UTM, city=unknown |
| **Service info in customer mail** | **forbidden** |
| **JSON response** | `ok: true` after admin send success; customer send failure does not break response |
| **Standard OC mails** | `catalog/controller/mail/*` + `template/mail/*.twig` — **unchanged** |
| **Staged roadmap** | ~~(1) admin forms~~ → ~~(2) customer form copy~~ → (3) account → (4) order → (5) polish |
| **Next charter** | `SITE-002-PROD-MAIL-ACCOUNT-TRANSACTIONAL-01` |
| **Report** | [SITE-002-PROD-MAIL-CUSTOMER-FORMS-01.md](../reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-01.md) |
| **Checkpoint** | [SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md](../baselines/SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md) |
| **Storage** | `.../deployments/SITE-002-PROD-MAIL-CUSTOMER-FORMS-01\` |

**Change rules:** Mail redesign requires explicit charter per stage. Do not expose SMTP secrets. Admin service-info block is admin-only — never include IP/UA in customer-facing mail.

---

## 35. Mail Design System (Production — ACTIVE)

**Operation:** Run 4.223 — `SITE-002-PROD-MAIL-DESIGN-SYSTEM-01` (2026-07-08)
**Integration:** Run 4.224 — anketa admin forms · Run 4.225 — operator inbox confirmation · Run 4.226 — customer confirmations + loading UX · Run 4.231 — customer delivery retest · Run 4.232 — customer inbox confirmation (operator-verified)
**Status:** **ACTIVE** — renderer integrated for admin + customer form mail

| Item | Production value |
|------|------------------|
| **Renderer class** | `ZpmMailRenderer` |
| **Remote path** | `/public_html/system/library/zpm/mail_renderer.php` |
| **Live references** | `checkout/anketa.php` → `renderAdminForm()` + `renderCustomerFormConfirmation()` |
| **Brand in templates** | **ЗПМ** (not БЗПМ) |
| **Layout** | 600px table-based, inline CSS, plain text fallback |
| **Admin mail** | service info block in `renderAdminForm()` |
| **Customer mail** | `renderCustomerFormConfirmation()` — contact fields + message; **no service info** |
| **Form loading UX** | `assets/js/main.js` — global `zpmFormSetLoading` / `AbortController`; `assets/css/style.css` — `.zpm-form--loading` |
| **Repo source** | [mail_renderer.php](../tools/mail_renderer.php) · [anketa patch](../tools/checkout_anketa_mail_customer_forms.php) · [orchestrator](../tools/site-002-prod-mail-customer-forms-01.py) |
| **Checkpoint** | [SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md](../baselines/SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md) |

**Change rules:** Renderer must remain send-free (render only). Account/order mail integration requires separate charters.

---

## 36. Post-1C Catalog Hygiene (2026-07-08)

**Operation:** Run 4.227 — `SITE-002-POST-1C-CATALOG-HYGIENE-REVIEW-01` (2026-07-08)
**Related import:** `mars-20260708-080001-bb67ff2b` — SUCCESS
**Scheduled monitor:** `2026-07-08_12-30-02` — exit **0**

| Item | Value |
|------|-------|
| **Sitemap before** | **1377** (Run 4.212 baseline) |
| **Sitemap after** | **1408** |
| **Added URLs** | **31** — all PRODUCT_PDP |
| **Groups** | 8 подтоварники + 23 зонты вытяжные ЗВЦ |
| **Onboarding needs** | **0** |
| **Public БЗПМ** | **0** |
| **Hygiene verdict** | **31 ADDED URLS PASS** |
| **Monitor garbage hits** | 31 — **false positives** (`/assets/img/demo/`, «Пример эксплуатации» docs) |
| **Production checkpoint** | unchanged `SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01` |
| **Audit baseline** | [SITE-002-POST-1C-CATALOG-HYGIENE-REVIEW-2026-07-08.md](../baselines/SITE-002-POST-1C-CATALOG-HYGIENE-REVIEW-2026-07-08.md) |
| **Report** | [SITE-002-POST-1C-CATALOG-HYGIENE-REVIEW-01.md](../reports/SITE-002-POST-1C-CATALOG-HYGIENE-REVIEW-01.md) |
| **Tool** | [site-002-post-1c-catalog-hygiene-review-01.py](../tools/site-002-post-1c-catalog-hygiene-review-01.py) |
| **Optional follow-up** | ~~`SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01`~~ **DONE** Run 4.228 |

---

## 37. Post-1C Monitor Artifacts Hardening (2026-07-08)

**Operation:** Run 4.228 — `SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01`

| Item | Value |
|------|-------|
| **Artifact contract** | Per scheduled folder: added/removed URLs, sitemap snapshots, hygiene flags, classification |
| **Strict garbage hits (31 URL retest)** | **0** (was 31 false positives in Run 4.227) |
| **Duration in run-summary** | **yes** (`duration_seconds` + `duration_human`) |
| **UTF-8 logs** | Runner uses UTF-8 process capture |
| **Classification** | `HYGIENE_REVIEW_REQUIRED` when delta exists without onboarding |
| **Scheduler impact** | Category **A** — no task re-registration |
| **Production checkpoint** | unchanged `SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01` |
| **Report** | [SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md](../reports/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md) |
| **Baseline** | [SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md](../baselines/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md) |

---

## 38. Info Page Corp CTA Forms Discovery (2026-07-09)

**Operation:** Run 4.229 — `SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01`

| Item | Value |
|------|-------|
| **Pages** | `/custom-equipment`, `/payment-methods`, `/delivery`, `/dealers`, `/guarantee` |
| **Form location** | Bottom `.zpm-corp-cta` block — **live markup in `information/*.twig`** (inline); `sections/corpcta-*.twig` partials also updated |
| **Live status (post 4.230)** | **Integrated** — corp CTA handler in `main.js`; `checkout/anketa` dialogs 7–11 |
| **Root cause** | `action=#` + handlers only bind `[data-fb-form]` (popup) and `.zpm-dealers[data-dealers] .zpm-form` |
| **Popup success reuse** | `fancyboxforms.twig` — icon `#zpm_ico__successful` + «Спасибо» / «Ваша заявка отправлена!» |
| **Recommended dialogs** | 8 delivery · 9 payment · 10 warranty · 11 custom-equipment · 7 dealers (existing) |
| **Next task** | ~~customer inbox confirmation~~ **DONE** Run 4.232; account/order transactional mail |
| **Production checkpoint** | `SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01` (Run 4.230) |
| **Integration report** | [SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01.md](../reports/SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01.md) |
| **Integration baseline** | [SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01.md](../baselines/SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01.md) |
| **Report** | [SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01.md](../reports/SITE-002-PROD-INFO-PAGE-FORMS-DISCOVERY-01.md) |
| **Baseline** | [SITE-002-INFO-PAGE-FORMS-DISCOVERY-01.md](../baselines/SITE-002-INFO-PAGE-FORMS-DISCOVERY-01.md) |

---

## 39. Post-1C Import Logs and Monitor Artifacts Audit (2026-07-09)

**Operation:** Run 4.233 — `SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01`

| Item | Value |
|------|-------|
| **Server 1C reports path** | `/storage/mars-tools/cron/reports/mars_1c_import_YYYY-MM-DD_HHMMSS.txt` |
| **Server 1C logs path** | `/storage/mars-tools/cron/logs/mars_1c_import_YYYYMMDD.log` |
| **2026-07-08 import run ID** | `mars-20260708-080001-bb67ff2b` — **SUCCESS** (FTP-confirmed) |
| **TXT Duration anomaly** | **FIX CONFIRMED** (Run 4.250) — post-patch `mars_1c_import_2026-07-10_080008.txt` Duration **6.17s** |
| **Scheduled monitor folder** | `scheduled-monitors/post-1c/2026-07-08_12-30-02` — pre-hardening (summary+log); latest hardened **manual** folder `2026-07-10_13-27-20` (Run 4.251) |
| **Post-4.228 scheduled hardened run** | **CONFIRMED_MANUAL** (Run 4.251) — natural 12:30 timing **still NOT OBSERVED**; next Task Scheduler **2026-07-11 12:30 +07** |
| **Task Scheduler** | Re-verified OK — enabled; LastTaskResult **0** |
| **Audit storage** | `deployments/SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01/` |
| **Report** | [SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01.md](../reports/SITE-002-POST-1C-IMPORT-LOGS-AND-MONITOR-ARTIFACTS-AUDIT-01.md) |

---

## 40. Cron Run Reports Duration Fix (Production — 2026-07-09)

**Operation:** Run 4.239 — `SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01`

| Item | Value |
|------|-------|
| **Wrapper path** | `/storage/mars-tools/cron/mars_1c_import_wrapper.php` |
| **Version** | **1.1.1** |
| **Root cause** | `mars_report_begin()` called after import in `mars_mode_run()` — `$startedAt` ≈ report write time |
| **Fix** | Optional `$wallStartedAt` param; pass run `$started` from `mars_mode_run()` |
| **Pre-patch anomaly** | All run-mode TXT through 2026-07-09 showed `Duration: 0 seconds` |
| **Confirmation** | **CONFIRMED** — Run **4.250** (2026-07-10); post-patch TXT `mars_1c_import_2026-07-10_080008.txt`; Duration **6.17 seconds**; Run ID `mars-20260710-080001-df983482` |
| **Report** | [SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md](../reports/SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md) |
| **Checkpoint** | [SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md](../baselines/SITE-002-STABLE-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md) |

---

## 41. Contacts URL Routing (Production — DECIDED 2026-07-09)

**Operations:** Run 4.237 — `SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01` (read-only discovery) · Run 4.238 — `SITE-002-PROD-CONTACTS-URL-ROUTING-DECISION-01` (operator decision)

| Item | Production value |
|------|------------------|
| **Canonical contacts URL** | **`/contact`** — **200** (operator decision Run 4.238) |
| **`/kontakty`** | **404** — **accepted / not a bug** (not required project URL) |
| **Route owner** | Native OpenCart `information/contact` — **not** `oc_information` page |
| **Controller** | `catalog/controller/information/contact.php` |
| **Template** | `catalog/view/theme/default/template/information/contact.twig` — cards, map, requisites, native POST form |
| **SEO URL** | `oc_seo_url` id **846** — keyword `contact` → query `information/contact` |
| **`kontakty` SEO row** | **Absent** — explains `/kontakty` 404; **no fix planned** |
| **Information page «Контакты»** | **Does not exist** — ids 4/7 are О нас / Пользовательское соглашение |
| **Internal links** | header/footer + 5 corp pages → `/contact` (**working**; no `/kontakty` links) |
| **Sitemap** | **Neither** `/contact` nor `/kontakty` — `google_sitemap.php` lists `oc_information` only |
| **`llms.txt`** | References `https://bzpm.ru/contact` |
| **Run 4.237 Option E** | **Rejected** — do not migrate to `/kontakty` |
| **Implementation planned** | **None** for contacts routing |
| **Optional future hygiene** | `SITE-002-PROD-CONTACT-SITEMAP-INCLUSION-01` — sitemap emission for `/contact` only |
| **Decision report** | [SITE-002-PROD-CONTACTS-URL-ROUTING-DECISION-01.md](../reports/SITE-002-PROD-CONTACTS-URL-ROUTING-DECISION-01.md) |
| **Discovery report** | [SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01.md](../reports/SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01.md) |

**Change rules:** Do not create duplicate contacts information page. Preserve native contact form mail (`config_email`). Do not edit Yandex blocks in header/footer. **Do not** implement Run 4.237 Option E (`contact` → `kontakty` migration).

---

## 42. Post-1C Lari Reparent and Duration Verification (Production — 2026-07-10)

**Operation:** Run 4.240 — `SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-01` (timing gate only — **superseded by Run 4.248** for current-state checks)

| Item | Value |
|------|-------|
| **Mode** | Read-only verification — **no mutation** |
| **Timing gate** | Latest import TXT must postdate Run 4.239 deploy |
| **Deploy 4.239** | `2026-07-09T17:07:52+00:00` |
| **Gate result (4.240)** | **BLOCKED** — import gate only; phases 2–6 skipped |

---

## 43. Post-1C Lari Reparent and Duration Verification 02 (Production — 2026-07-10)

**Operation:** Run 4.248 — `SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-02`

| Item | Value |
|------|-------|
| **Mode** | Read-only verification — **no mutation** |
| **Worktree** | `X:\AI MARS STORAGE\git-sync-e01\repo` (clean; origin `0d1174a3`) |
| **Latest import TXT** | `mars_1c_import_2026-07-09_080009.txt` — still **pre-patch** |
| **Lari DB/HTTP/sitemap** | **PASS** — reparent intact at verification time |
| **Duration fix (4.239)** | **NOT CONFIRMED** — no post-patch import |
| **Monitor hardened (4.228)** | **NOT OBSERVED** — latest folder `2026-07-08_12-30-02` pre-hardening |
| **Verdict** | **PARTIAL** — Lari confirmed; Duration pending |
| **Tool** | `site-002-prod-post-1c-lari-reparent-and-duration-verification-02.py` |
| **Report** | [SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-02.md](../reports/SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-02.md) |
| **Storage** | `verification/SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-02/` |

---

## 44. Duration and Monitor Verification 03 (Production — 2026-07-10)

**Operation:** Run 4.250 — `SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03`

| Item | Value |
|------|-------|
| **Mode** | Read-only verification — **no mutation** |
| **Worktree** | `X:\AI MARS STORAGE\git-sync-e01\repo` (origin `bf4ba612`) |
| **Post-patch import TXT** | `mars_1c_import_2026-07-10_080008.txt` — Duration **6.17s** SUCCESS |
| **Duration fix (4.239)** | **CONFIRMED** |
| **Lari** | **CONFIRMED** — DB + HTTP quick recheck |
| **SEO regression** | **PASS** — sitemap **1424** URLs; 0 flat Lari; `/contact` present |
| **Monitor hardened (4.228)** | **NOT OBSERVED** — no folder after 2026-07-10 12:30 +07 (superseded by Run 4.251 manual confirmation) |
| **Task Scheduler** | Last run 2026-07-08; next **2026-07-11 12:30 +07** |
| **Verdict** | **PARTIAL** — Duration confirmed; monitor not observed on natural schedule |
| **Tool** | `site-002-prod-duration-monitor-verification-03.py` |
| **Report** | [SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md](../reports/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md) |
| **Storage** | `verification/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03/` |

---

## 45. Local Monitor Manual Run (Production — 2026-07-10)

**Operation:** Run 4.251 — `SITE-002-LOCAL-MONITOR-MANUAL-RUN-01`

| Item | Value |
|------|-------|
| **Mode** | Operator-approved manual Task Scheduler trigger — read-only monitor |
| **Trigger** | `Start-ScheduledTask` on `\MARS_SITE_002_Post_1C_Catalog_Monitor` |
| **Task LastTaskResult** | **0** |
| **Run folder** | `scheduled-monitors/post-1c/2026-07-10_13-27-20` |
| **Hardened contract (4.228)** | **CONFIRMED_MANUAL** — all artifact families present |
| **Duration** | **91.378s** |
| **Classification** | **ONBOARDING_REQUIRED** (`monitor-classification.json`) |
| **Sitemap delta** | baseline **1377** → current **1424**; +61 / −14 |
| **Natural scheduled timing** | **still NOT OBSERVED** — manual ≠ 12:30 daily slot |
| **Next Task Scheduler** | **2026-07-11 12:30 +07** (unchanged) |
| **Production mutation** | **0** |
| **Checkpoint** | unchanged `SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01` |
| **Report** | [SITE-002-LOCAL-MONITOR-MANUAL-RUN-01.md](../reports/SITE-002-LOCAL-MONITOR-MANUAL-RUN-01.md) |
| **Storage** | `verification/SITE-002-LOCAL-MONITOR-MANUAL-RUN-01/` |

---

*Documentation only — Production evidence in Run 4.173+ operation manifests. Last updated: 2026-07-10 (Run 4.251 — hardened artifacts confirmed manually; natural scheduled timing still pending).*
