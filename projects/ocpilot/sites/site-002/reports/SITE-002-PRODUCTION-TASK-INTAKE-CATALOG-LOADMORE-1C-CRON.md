# REPORT — SITE-002 Production Task Intake: Catalog Sorting / Load More / 1C Cron

**OCPilot run:** 4.174  
**Date:** 2026-07-05  
**Environment:** PRODUCTION — https://bzpm.ru/  
**Mode:** READ-ONLY AUDIT + IMPLEMENTATION PLAN — **no Production changes performed**

---

## 1. Scope

Planning intake for three operator-requested Production tasks (ЗПМ / BZPM):

| # | Task | Intake goal |
|---|------|-------------|
| 1 | Catalog default sort A → Я | Identify exact implementation surfaces and controlled deploy scope |
| 2 | Pagination / Load More | Choose Option A vs B with evidence; plan UX and files |
| 3 | 1C parser cron at 12:00 Barnaul | Map import flow; plan Beget cron without executing it |

**Forbidden in this run:** deploy, FTP write, DB mutation, parser URL execution, Beget cron creation, admin save, cache clear.

**Allowed evidence:** local repo/docs, Production HTTP GET, Production baseline capture (2026-07-02/03), TEST-era forensic captures, read-only audit artefacts.

---

## 2. Pre-flight

| Check | Result |
|-------|--------|
| Workspace | `X:\AI MARS\` — **PASS** |
| Volume | `X:` label `AI WS` — **PASS** |
| Branch | `mars/canonical-post-recovery` — **PASS** |
| HEAD | `1ee0efd9b6d536bd22af476e1bca2f13868f2f9e` |
| Authority docs read | AGENTS.md, .cursorrules, OPERATIONAL-INDEX, OCPILOT-STATE, production-profile, site-passport, project-access-brief, SITE-002-TECHNICAL-KNOWLEDGE-MAP, baselines/reports per charter — **PASS** |
| Production path model | Application `/bzpm.ru/` · FTP chroot `/` → `public_html/` + `storage/` — **CONFIRMED** (Run 4.172) |
| Remote mutations | **0** |

---

## 3. Operator WIP protection

### Git inventory (local repo)

`git status --short` shows **no modified tracked files** under `projects/ocpilot/sites/site-002/` catalog Twig/CSS controllers. SITE-002 entries are predominantly **untracked backups** and work-folder artefacts — treated as **historical evidence**, not deploy targets.

Foreign WIP exists elsewhere in the monorepo (FP-0002, forge-wordpress, `.recovery-temp/`, etc.) — **not staged, not touched**.

### Production operator WIP (remote)

Operator stated manual Twig/CSS edits on **live Production** that must not be overwritten. These changes are **not represented in git** and may post-date capture baseline `SITE-002-STABLE-PROD-INITIAL-01` (2026-07-03).

| Surface | Status |
|---------|--------|
| Operator manual Twig/CSS on Production | **PROTECTED OPERATOR WIP** — live FTP capture mandatory before any catalog/CSS deploy |
| `guarantee.twig` (Run 4.173 text change) | **OCPilot-controlled checkpoint** — do not revert |
| Production baseline `downloaded-baseline/` (24 files) | **Historical snapshot** — must not replace live files blindly |

**Rule for all three tasks:** pre-deploy FTP capture + SHA256 of every file in scope; merge operator deltas; never normalize/format operator WIP.

---

## 4. Current Production baseline

| Field | Value |
|-------|-------|
| Current checkpoint | `SITE-002-STABLE-PROD-TEXT-CHANGE-01` |
| Parent baseline | `SITE-002-STABLE-PROD-INITIAL-01` |
| Proven deploy class | **Single-file text-only FTP** with backup + rollback (Run 4.173) |
| OpenCart version | **3.0.3.9** (admin read-only, Run 4.171) |
| Active theme | `default` |
| Catalog PLP live probe (2026-07-05) | https://bzpm.ru/katalog/nejtralnoe-oborudovanie/stoly — sort label **«Умолчанию»**, limit **15**, hybrid pagination (numeric + «Показать еще») |

CSS/JS/controller/catalog deploy classes are **not proven** on Production.

---

## 5. Task 1 — Alphabetical catalog sorting

### Current behaviour (evidence)

**Production controller baseline** (`catalog/controller/product/category.php`, capture SHA matches Production initial baseline):

```php
// Default when sort/order absent from URL:
$sort = 'p.date_added';
$order = 'DESC';
$data['sorttext'] = 'Умолчанию';
// Maps pd.name ASC → 'Название - от А до Я'
```

**Live HTTP (2026-07-05):** `/katalog/nejtralnoe-oborudovanie/stoly` renders sort button text **«Умолчанию»** — consistent with `p.date_added DESC`.

**Sort UI** (`category.twig`): buttons with `data-sort` — first option «Умолчанию» = `sort=p.date_added&order=DESC`; «Название - от А до Я» = `sort=pd.name&order=ASC`.

**Query pipeline:** `category.php` passes `'sort' => $sort, 'order' => $order` into `ModelCatalogProduct::getProducts()` / `getTotalProducts()`. Filter AJAX (`updateProducts`) fetches full page at current URL — sort params preserved (M9.8.9-09A/09C).

**SEO URLs:** canonical/prev/next links generated from `$page` and category path — independent of default sort when params omitted.

### Target behaviour

| Param | Target default |
|-------|----------------|
| `sort` | `pd.name` |
| `order` | `ASC` |

Preserve: limit selector (15/25/50/100), filters, hub mode, search/filter AJAX, SEO URL scheme, operator WIP.

### Recommended implementation

| Layer | File (FTP path under `public_html/`) | Change |
|-------|--------------------------------------|--------|
| **Primary** | `catalog/controller/product/category.php` | Default `$sort = 'pd.name'`, `$order = 'ASC'`; default `$data['sorttext'] = 'Название - от А до Я'` |
| **UI label (optional)** | `catalog/view/theme/default/template/product/category.twig` | Re-label first sort option from «Умолчанию» → «По умолчанию (А→Я)» **or** swap default mapping so «Умолчанию» triggers name ASC — operator decision |
| **Model** | `catalog/model/catalog/product.php` | **No change expected** — already honours passed sort/order |
| **JS** | `assets/js/main.js` | **No change required** — sort buttons merge params into URL |
| **CSS** | `assets/css/style.css` | **No change expected** |

**Dropdown selected state:** After controller change, clean category URLs without `sort`/`order` should render **«Название - от А до Я»** in `.category__sort-btn-text`.

**Old URL compatibility:** Explicit `?sort=p.date_added&order=DESC` and other sort links continue to work. No link migration required.

**OCMOD / events:** None identified in repo evidence for sort defaults.

### Risk / backup / verification

| Item | Value |
|------|-------|
| Risk level | **MEDIUM** — single PHP controller file, but affects all category PLPs |
| Deploy class | **First Production controller deploy** — stricter charter than Run 4.173 |
| Backup scope | Live capture `category.php` + Twig cache note; Beget backup already done per operator |
| Verification URLs | `/katalog/nejtralnoe-oborudovanie/stoly` (large), leaf category, filtered PLP `?filters=only_with_price=1`, hub parent (no grid), `?limit=50`, explicit old default URL |
| QA matrix | Full-page load + filter AJAX + sort change + limit change + pagination click |

### Task 1 status

**READY FOR IMPLEMENTATION** — scope is narrow and surfaces are identified. **Pre-requisite:** live FTP capture of Production `category.php` and `category.twig` before diff (operator WIP may differ from July baseline).

---

## 6. Task 2 — Pagination / Load More decision

### Current behaviour (evidence)

**Markup (Production HTTP 2026-07-05):**

```html
<nav class="pagination" aria-label="Пагинация">
  <div class="pagination__pages">…numeric links 1…35…</div>
  <button class="btn pagination__more" type="button" data-next="…?page=2">Показать еще</button>
</nav>
```

**CSS:** `.pagination__more` styled in theme `style.css` (TEST captures + Production theme).

**Custom Pagination class:** `category.php` uses `new Pagination(); $pagination->render()`. Custom HTML with `pagination__more` + `data-next` is generated server-side. **File not in Production 24-file baseline** — inferred path: `system/library/pagination.php` (**SAFE UNKNOWN** until FTP capture).

**JS (Production `assets/js/main.js` via HTTP):**

- `initPaginationAJAX()` — intercepts **numeric** `.pagination a` clicks; sets `page` in URL; calls `updateProducts()` which **replaces** `.category__grid` innerHTML (not append).
- **No handler** for `.pagination__more[data-next]` in Production `main.js` (grep: only `initPaginationAJAX` references).

**Counter «Показано X из Y»:** `$data['results']` built in `category.php` via `text_pagination` language string, but **not rendered** in `category.twig` (no `{{ results }}` in template captures). Production HTML confirms **no visible counter**.

### Option comparison

| Criterion | Option A — cumulative numeric pages | Option B — «Показать ещё» + counter |
|-----------|--------------------------------------|-------------------------------------|
| Current UX | Partially overlaps — numeric AJAX replaces grid; «Показать еще» button present but **behaviour unverified/ likely inert** | Aligns with existing button + operator ask |
| Implementation | Modify `initPaginationAJAX` + server to return cumulative slices or client-side append after fetch — fights current replace semantics | New append path on `data-next`; hide `.pagination__pages`; add counter in Twig |
| Filter/sort reset | Must reset accumulated cards | Same — reset on filter/sort/limit/category change |
| SEO | Page URLs remain; cumulative view is JS-only | Page 1 canonical; deep pages still exist server-side for no-JS |
| Performance | Page 10 = load all prior pages — heavy | Same fetch cost per step, clearer UX cap |
| Production deploy risk | HIGH — JS + mental model change | HIGH — JS + Twig + possibly `pagination.php` |

### Recommendation

**Choose Option B — «Показать ещё» + counter «Показано X из Y товаров».**

Evidence:

1. Production markup **already ships** `pagination__more[data-next]` (hybrid pattern from Category V2 era).
2. Option A would keep confusing dual controls (numbers + cumulative load).
3. Category Audit V1 noted dual pattern «may confuse — pick one primary».
4. `initPaginationAJAX` replace semantics are entrenched in filter stack (M9.8.9-09A–09C); append via dedicated load-more path is cleaner than retuning page-link semantics.
5. Counter string already computed in PHP — only needs Twig exposure.

### Option B — planned behaviour

| Rule | Behaviour |
|------|-----------|
| Initial load | Show `limit` products (default 15) |
| Button | «Показать ещё» — fetch next page, **append** cards to `.category__grid` |
| Counter | «Показано X из Y товаров» — X = visible count, Y = `product_total` |
| Steps | limit=15 → 15, 30, 45…; limit=30 → 30, 60, 90… |
| End state | Hide button when X ≥ Y |
| Reset triggers | Filter change, sort change, limit change, category navigation — reset to page 1 / clear appended |
| URL | **Recommend:** keep `page` at 1 in address bar during append (or use `history.replaceState` without deep page index) — document for SEO |
| No-JS fallback | Standard numeric pagination links remain in HTML inside `.pagination__pages` (can stay visible without JS or via `<noscript>`) |
| SEO | Canonical stays page 1 for filtered views; paginated URLs remain valid for crawlers; appended content is enhancement only |

### Files likely to change (Option B)

| File | Role |
|------|------|
| `system/library/pagination.php` | Hide numeric block when JS enabled **or** always hide pages + keep load-more only — **capture first** |
| `catalog/view/theme/default/template/product/category.twig` | Add `{{ results }}` or custom counter markup near pagination |
| `assets/js/main.js` | `initLoadMore()` — `data-next` fetch, append grid, update counter, disable at end; reset hooks in filter/sort/limit paths |
| `assets/css/style.css` | Counter typography; hide `.pagination__pages` when load-more mode active |
| `catalog/controller/product/category.php` | Possibly pass `product_total`, visible range helpers — may already sufficient |

**Do not modify** filter sidebar Twig operator WIP without capture.

### Fallback plan

- Progressive enhancement: without JS, numbered pagination links work as full page loads (standard OpenCart).
- If JS fails mid-session, user still has page links in DOM (unless hidden — **recommend** hide pages only with JS class on `<html>`, not server-only removal).

### Task 2 status

**READY FOR IMPLEMENTATION** (design) — **BLOCKED for Production deploy** until:

1. Live capture of `pagination.php`, `category.twig`, `main.js`, `style.css`.
2. Separate deploy charter (CSS/JS/controller — **not covered** by Run 4.173 proof).
3. Interaction QA on filter + load-more + sort matrix.

### Operation class note

Catalog CSS/JS/controller changes require a **new, more cautious Production operation** than text-only FTP. Treat as **multi-file charter** with Twig cache clear plan and rollback per file.

---

## 7. Task 3 — 1C parser cron preparation

### Discovered flow (TEST forensic + code audit — Production assumed parity)

| Step | Detail |
|------|--------|
| XML location | `{site_root}/1c_incoming/webdata/` |
| Catalog file | `import0_*.xml` → command `1c` → `catalog/controller/common/import_1C.php` |
| Offers file | `offers0_*.xml` → command `1c_offers` → `catalog/controller/common/import_1C_offers.php` |
| HTTP entry | `index.php?route=common/cronjob` → `ControllerCommonCronjob::index()` |
| DB table | **`cron`** (no `oc_` prefix) |
| Known rows | id 1 «Импорт 1C» command `1c`; id 2 «Импорт 1C - цены и остатки» command `1c_offers` |
| Task gate | `SELECT * FROM cron WHERE DATE_ADD(lastrun, INTERVAL duration SECOND) < NOW() AND active=1` — **one task per HTTP hit** |
| Operator manual sequence | (1) `UPDATE cron SET active=0`; (2) `UPDATE cron SET active=1 WHERE command='1c'`; hit URL; wait; deactivate; (3) activate `1c_offers`; hit URL; deactivate |
| Offers side effect | `refreshPriceIndex(product_id)` per updated SKU (since M9.8.9-06F) |
| Order dependency | **Catalog (`1c`) MUST complete before offers (`1c_offers`)** |
| Auth on URL | **SAFE UNKNOWN** on Production — treat as **mutation trigger**; do not HTTP-test in intake |
| Lock / anti-parallel | **None found** in reviewed import/cronjob code |
| Idempotency | Re-import updates products; offers update price/qty — generally safe but heavy |
| Logs | Echo/HTML output + `$this->log->write("Import: …")` in cronjob — no dedicated cron log file |
| Manual bulk reindex | `reindex_prices.php` at site root (not cron) |
| Runtime | `max_execution_time=300`, `memory_limit=512M` in cronjob controller |

**Production URL (planned):** `https://bzpm.ru/index.php?route=common/cronjob` — **not invoked in this task**.

### DB fields toggled (operator description)

| Field | Table | Manual pattern |
|-------|-------|----------------|
| `active` | `cron` | 0 → 1 on target command row; 0 after run |
| `lastrun` | `cron` | Updated by `ModelCatalogCronjob::setDone()` on success |
| `duration` | `cron` | Minimum interval between runs (seconds) |

Toggling **can** be scripted via PHP CLI or SQL in a wrapper — preferable to manual phpMyAdmin.

### Beget cron timezone

**SAFE UNKNOWN** — do not schedule until operator confirms Beget panel timezone (often Moscow for RU hosting).

| If cron uses | Schedule for 12:00 Barnaul (UTC+7) |
|--------------|--------------------------------------|
| Moscow (UTC+3) | **08:00** |
| UTC | **05:00** |
| Server local | **UNKNOWN** — verify in Beget |

### Cron readiness verdict

**NOT READY — PREPARE CRON WRAPPER FIRST**

Gaps:

1. Manual DB flag toggling — error-prone for daily automation.
2. Two-step sequence requires **orchestration** (products then offers with wait/confirm).
3. No lock file — parallel cron + manual import risk.
4. Public HTTP endpoint without confirmed auth token/IP restriction.
5. No structured log destination for operator review.
6. No failure notification path.
7. Production cron table state **not read** in this intake (DB forbidden).

### Recommended cron wrapper plan (future task)

| Component | Recommendation |
|-----------|------------------|
| Wrapper script | PHP CLI under `public_html/` or outside webroot: e.g. `cron/1c_daily_import.php` |
| Sequence | Activate `1c` only → invoke import (CLI include or single curl to cronjob) → wait until complete marker → deactivate `1c` → activate `1c_offers` → run → deactivate |
| Delay | Wait for catalog completion (poll log / lock file / max timeout) before offers |
| Lock | File lock `storage/logs/1c_import.lock` or DB flag |
| Logging | Append to `storage/logs/1c_cron_YYYYMMDD.log` |
| Failure | Non-zero exit; leave tasks `active=0`; log tail for operator |
| Disable | Set all `cron.active=0`; remove Beget cron entry |
| Beget command | Prefer **PHP CLI** over wget/curl if path available: `/usr/bin/php /home/.../bzpm.ru/public_html/cron/1c_daily_import.php` — **exact path SAFE UNKNOWN** until hosting inspect |
| Alternative | curl only inside wrapper with localhost + secret query token — requires **new** auth hardening |

### Operator actions before enabling cron

1. Confirm Beget cron timezone.
2. Confirm XML drop schedule from 1C (files present before 12:00 Barnaul).
3. Authorize DB read of `cron` table on Production (verify `duration`, `lastrun`, row ids).
4. Approve wrapper script deploy + log directory.
5. Decide auth model for HTTP trigger (IP allowlist / secret / CLI-only).
6. Dry-run manual import once in maintenance window with backup.
7. Only then add Beget cron entry — **separate chartered operation**.

### Task 3 status

**PARTIAL — BLOCKERS / SAFE UNKNOWN REMAIN** (flow mapped from code; Production cron state and Beget timezone unverified).

---

## 8. Files and surfaces discovered

| Surface | Path | In Prod baseline? | Notes |
|---------|------|-------------------|-------|
| Category controller | `catalog/controller/product/category.php` | **Yes** | Sort defaults, pagination, limits, filters URL |
| Category template | `catalog/view/theme/default/template/product/category.twig` | **No** | Sort menu, grid, `{{ pagination }}` |
| Product model | `catalog/model/catalog/product.php` | **No** | Filter SQL, sort order |
| Filter sidebar | `catalog/view/theme/default/template/sections/filterssidebar.twig` | **No** | Operator WIP risk |
| Main JS | `assets/js/main.js` | **No** | `updateProducts`, `initPaginationAJAX` |
| Theme CSS | `assets/css/style.css` | **No** | `.pagination__more` |
| Pagination library | `system/library/pagination.php` | **No** | **SAFE UNKNOWN** — generates load-more markup |
| Cronjob controller | `catalog/controller/common/cronjob.php` | **No** | Forensic copy in `m9.8.9-06c-audit-data/` |
| Cronjob model | `catalog/model/catalog/cronjob.php` | **No** | `cron` table queries |
| Import catalog | `catalog/controller/common/import_1C.php` | **No** | `1c_incoming/webdata/import0_*.xml` |
| Import offers | `catalog/controller/common/import_1C_offers.php` | **No** | `offers0_*.xml` + price index hook |
| DB table | `cron` | n/a | `active`, `command`, `duration`, `lastrun` |
| Reindex utility | `reindex_prices.php` (site root) | **No** | Manual catch-up |

---

## 9. Production risk classification

| Task | Risk | Deploy class | Rollback |
|------|------|--------------|----------|
| 1 — Sort A→Я | **MEDIUM** | First controller deploy | Restore `category.php` from capture |
| 2 — Load More B | **HIGH** | Multi-file PHP + Twig + JS + CSS | Per-file backup; disable JS class fallback |
| 3 — 1C cron | **CRITICAL** (data mutation) | Ops + DB + script; not theme | Deactivate cron rows; remove Beget job; restore from backup |

**Global:** Operator WIP on Twig/CSS increases regression risk for Tasks 1–2. Only proven Production deploy: **single text Twig** (Run 4.173).

---

## 10. Recommended implementation order

**Order A (recommended):**

1. **Catalog default sorting A→Я** — smallest functional change; one primary PHP file; immediate operator value.
2. **1C cron wrapper preparation** — operational; no daily automation until wrapper + timezone + auth resolved; can proceed in parallel with sorting QA but **must not go live** before wrapper sign-off.
3. **Load More (Option B)** — largest UX/JS surface; depends on stable sort defaults; requires multi-file Production charter.

Sorting first avoids retesting load-more against changing default order. Cron wrapper is independent code path but **mutation-critical** — prepare before Beget activation, not necessarily before sorting deploy.

---

## 11. Required backups

| Task | Pre-change backup |
|------|-------------------|
| Sort | FTP capture + `category.php` (+ `category.twig` if label change); Beget snapshot already done |
| Load More | Capture `pagination.php`, `category.twig`, `main.js`, `style.css`, `category.php` |
| Cron wrapper | Full DB dump or `cron` table export; copy import scripts; Beget panel export; XML directory snapshot policy |

Store under `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\backups\` per production-profile.

---

## 12. Required operator confirmations

1. Sort UI: keep label «Умолчанию» remapped to A→Я **or** rename first menu item?
2. Load More: confirm Option B; approve hiding numeric pages on desktop when JS active?
3. Counter exact copy: «Показано X из Y товаров» — approved?
4. Production FTP capture authorization for catalog files (operator WIP merge).
5. Beget cron panel timezone.
6. 1C XML delivery time vs 12:00 Barnaul run.
7. Cron auth: CLI-only vs HTTP + secret.
8. Maintenance window for first manual cron dry-run.
9. DB read authorization for `cron` table verification on Production.

---

## 13. Blockers / SAFE UNKNOWN

| Item | Status |
|------|--------|
| Production `system/library/pagination.php` source | **SAFE UNKNOWN** — not in baseline |
| Production `main.js` operator deltas vs TEST captures | **SAFE UNKNOWN** — HTTP shows no `data-next` handler |
| `pagination__more` click behaviour on Production | **SAFE UNKNOWN** — button present; handler absent in fetched JS |
| Beget cron timezone | **SAFE UNKNOWN** |
| Production `cron` table current rows/state | **SAFE UNKNOWN** — DB not read |
| Parser URL auth / IP restriction on Production | **SAFE UNKNOWN** |
| PHP CLI path on Beget for `bzpm.ru` | **SAFE UNKNOWN** |
| Operator manual Production Twig/CSS diff vs July capture | **SAFE UNKNOWN** — treat as WIP |
| Search route default sort (`product/search`) | **SAFE UNKNOWN** — not probed; may need same change |

---

## 14. Next Cursor prompts to prepare

1. **SITE-002-PROD-SORT-AZ-01** — Live capture + implement `pd.name ASC` default in `category.php`; charter + single-controller deploy + QA matrix.
2. **SITE-002-PROD-CRON-WRAPPER-01** — Design/deploy CLI wrapper, lock, logging; DB read-only verification; **no Beget activation**.
3. **SITE-002-PROD-LOAD-MORE-01** — Capture `pagination.php`; implement Option B append + counter; multi-file deploy charter.
4. **SITE-002-PROD-CRON-BEGET-ACTIVATE-01** — After wrapper QA: timezone conversion, Beget cron line, operator HITL — gated separately.

---

## 15. Git status

At task close (scoped work only):

```
?? projects/ocpilot/sites/site-002/reports/SITE-002-PRODUCTION-TASK-INTAKE-CATALOG-LOADMORE-1C-CRON.md
 M projects/ocpilot/OPERATIONAL-INDEX.md
```

Foreign WIP elsewhere in repo — **preserved, not staged**.

---

## 16. Final verdict

| Task | Verdict |
|------|---------|
| **1 — Catalog sort A→Я** | **READY FOR IMPLEMENTATION** (after live capture) |
| **2 — Load More** | **READY FOR IMPLEMENTATION** planning — **Option B recommended**; Production deploy blocked on multi-file charter + capture |
| **3 — 1C cron** | **NOT READY — PREPARE CRON WRAPPER FIRST**; timezone and Production DB state **SAFE UNKNOWN** |

**Run 4.174 overall:** **COMPLETE — IMPLEMENTATION SCOPES PREPARED** with documented SAFE UNKNOWN items and operator WIP protection.

**Intake compliance:** No Production files changed · no parser executed · no DB changed · no cron created · operator remote WIP acknowledged · report and index updated.
