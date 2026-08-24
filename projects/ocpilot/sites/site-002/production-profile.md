# SITE-002 Production Profile

**Site ID:** SITE-002  
**Project:** ЗПМ / BZPM  
**Document role:** Production environment registration — **not** connection authorization  
**Last updated:** 2026-08-25 (Run 4.343 — SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01 — 8-root model applied; sitemap live **1861** vs baseline **1887**)

---

## Profile status

| Field | Value |
|-------|-------|
| Profile status | **REGISTERED — CONNECTED** |
| Remote access status | **HTTP/ADMIN/FTP VERIFIED; FTP WRITE VERIFIED FOR ONE FILE** |
| Production operations | **FIRST CONTROLLED PRODUCTION CHANGE COMPLETE** |

---

## Identity

| Field | Value |
|-------|-------|
| Site ID | SITE-002 |
| Project | ЗПМ / BZPM |
| Environment ID | `site-002-prod` |
| Environment type | **PRODUCTION** |
| Production URL | https://bzpm.ru/ |
| Historical TEST URL | https://zpm.new-site.space/ |
| Platform | ocStore / OpenCart |
| Exact platform version | **3.0.3.9** (admin read-only, Run 4.171) |
| OCPilot owner | `projects/ocpilot/sites/site-002/` |
| Operator model | human-supervised / HITL |

---

## Environment roles

### Production

**URL:** https://bzpm.ru/

Current operational website authority. Production was created by transferring the approved TEST website. OCPilot treats this URL as the present-day operational target for SITE-002 Production work once connection is authorized.

### Historical TEST

**URL:** https://zpm.new-site.space/

Previous implementation and verification environment. Preserve as historical evidence and optional future test environment. **Do not treat as current Production authority.**

| Field | Value |
|-------|-------|
| Production parity with latest TEST checkpoints | **FILE + HTTP VERIFIED** (Run 4.171-R1) — corp pages FUNCTIONALLY PRESENT |

Do not claim that Production exactly matches TEST unless evidence proves it.

---

## Authority bindings

| Document | Path |
|----------|------|
| Site passport | [site-passport.md](site-passport.md) |
| Project access brief | [project-access-brief.md](project-access-brief.md) |
| OCPilot state | [../../OCPILOT-STATE.md](../../OCPILOT-STATE.md) |
| Operational index | [../../OPERATIONAL-INDEX.md](../../OPERATIONAL-INDEX.md) |
| Project site registry | [../../project-site-registry.md](../../project-site-registry.md) |
| Technical knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) |
| Current M9.x baselines | [baselines/](baselines/) — TEST-proven checkpoints |
| Post-corporate-page checkpoints | Home Commercial Trust · Corporate Intro · Custom Proof Strip · Delivery Summary · PDP Body Category Classes |
| Production baseline parent | [baselines/SITE-002-STABLE-PROD-INITIAL-01.md](baselines/SITE-002-STABLE-PROD-INITIAL-01.md) |
| Current Production checkpoint | [baselines/SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01.md](baselines/SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01.md) (parent [SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md](baselines/SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md)) |
| Mail design system (Production) | **ACTIVE — CUSTOMER CONFIRMATIONS + LOADING UX** (Run 4.226) — `ZpmMailRenderer` in `checkout/anketa.php`; admin emails ЗПМ-styled + service info (Run 4.224/4.225); **customer confirmations conditional** on posted email or logged-in customer email — **no service info in customer copy**; form loading state `zpm-form--loading` + abort on modal close · **delivery retest** Run 4.231 — controlled submit `ok: true` with operator mailbox · **inbox confirmation** Run 4.232 — operator verified delivery/design/no service info issue · [report](reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-01.md) · [delivery confirmation](reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01.md) · [inbox confirmation](reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-INBOX-CONFIRMATION-01.md) · [checkpoint](baselines/SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md) |
| Info page corp CTA forms (Production) | **ACTIVE — INTEGRATED** (Run 4.230) — 5 corp footer forms on `/custom-equipment`, `/payment-methods`, `/delivery`, `/dealers`, `/guarantee` submit via `checkout/anketa`; dialogs 7/8/9/10/11; inline success-state; live markup in `information/*.twig` · [report](reports/SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01.md) · [checkpoint](baselines/SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01.md) |
| Info page corporate intro images (Production) | **ACTIVE — DELIVERY RESTORED** (Run **4.263**) — `/delivery` `.zpm-corp-intro` restored; asset `/assets/img/corporate/delivery-intro.jpg` pre-existing (no image FTP); CSS unchanged; exact file `/public_html/catalog/view/theme/default/template/information/delivery.twig`; other info pages unchanged; 1 FTP twig · discovery [PARTIAL](reports/SITE-002-PROD-INFO-PAGE-HERO-IMAGES-DISCOVERY-01.md) · [restore](reports/SITE-002-PROD-INFO-PAGE-HERO-IMAGES-RESTORE-01.md) · Storage `deployments/SITE-002-PROD-INFO-PAGE-HERO-IMAGES-RESTORE-01/` |
| Category entrypoints display sort (Production) | **ACTIVE** (Run 4.221) — megamenu + homepage + neutral hub **А → Я** by Russian name; `sortCategoriesByRussianName()` in `category_visibility.php`; hub sort in `category.php`; membership/images unchanged · [report](reports/SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01.md) |
| SEO readiness (Production) | **NEW SECTION ENTRYPOINTS VERIFIED** (Run 4.220) — lari/konditerskiy tiles on homepage/hub; Composer-only images; IDs 88/360 in whitelist · [report](reports/SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02.md) · **PDP EXTRA INFO LAYOUT VERIFIED** (Run 4.218) — display-only extraction; meta generator preserved · [report](reports/SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01.md) · **SITEMAP AUTHORITY CONFIRMED** (Run 4.214) — AUTO-GENERATED OpenCart Google Sitemap feed; route `extension/feed/google_sitemap`; `.htaccess` rewrite; live per-request; **1408** URLs (post 2026-07-08 1C import); MARS monitor/audit only — no manual XML edit · [authority report](reports/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md) · **Post-1C hygiene review** (Run 4.227) — +31 PRODUCT_PDP PASS; 0 **БЗПМ** · [hygiene report](reports/SITE-002-POST-1C-CATALOG-HYGIENE-REVIEW-01.md) · **Post-1C monitor artifacts** (Run 4.228) — hardened scheduled artifact contract; strict garbage markers; classification/next_action · [hardening report](reports/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md) · **Post-1C monitor scheduler** (Run 4.216) — Windows Task verified LastTaskResult **0**; task enabled · [runner fix report](reports/SITE-002-POST-1C-MONITOR-SCHEDULER-RUNNER-FIX-01.md) · [runbook](runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md) |
| Yandex analytics (Production) | **VERIFIED** (Run 4.189) — Metrika counter in `common/footer.twig` (masked `110***756`); Webmaster verification in `common/header.twig` (masked `13a***c77`); confirmed on live HTML (home, category, information); **OPERATOR WIP — DO NOT OVERWRITE** · [report](reports/SITE-002-PROD-YANDEX-CODES-VERIFY-01.md) |
| HTML body structure (Production) | **FIXED** (Run 4.190) — duplicate `<body>` + global preloader + `page_overlay` removed from live `header.twig`; 4-URL HTML validation PASS; Yandex blocks unchanged · [report](reports/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01.md) |
| MARS 1C cron wrapper | **OPERATIONAL — DURATION REPORTING FIX CONFIRMED** (Run 4.239 + Run 4.250) — wrapper v**1.1.1**; post-patch import `mars_1c_import_2026-07-10_080008.txt` Duration **6.17s** SUCCESS; schedule `0 8 * * *` Moscow; Sergey legacy **preserved** · [verification Run 4.250](reports/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md) · [duration fix report](reports/SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md) |
| MARS 1C cron reports | **DAILY HEALTHY — OFFERS STEP RECOVERED** — latest completed natural import `mars_1c_import_2026-08-24_080010.txt` / `mars-20260824-080002-509cb9e8` **SUCCESS**; catalog `import0_1.xml` **PASS** `4.17s`; offers `offers0_1.xml` **PASS** `4.04s`; total `8.22s`; mapping `95`/`364` persistence confirmed after post-B1 imports · [healthcheck 4.338](reports/SITE-002-POST-IMPORT-AND-MONITOR-HEALTHCHECK-01.md) · prior [healthcheck 4.325](reports/SITE-002-PROD-POST-1C-OFFERS-RECOVERY-AND-NEW-SECTIONS-HEALTHCHECK-01.md) · prior [forensic 4.319](reports/SITE-002-PROD-1C-FIRST-LEVEL-CATEGORY-PLACEMENT-FORENSIC-01.md) · [duration fix](reports/SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md) |
| Catalog normalization apply (Production) | **COMPLETE (Run 4.343)** — 8 public roots live; `381` Upakovochnoe created+mapped; promote `364`/`375`/`373`; tmp+disable legacy roots; htaccess 301; `[96]` hold; Upakovochnoe product pending import; baseline refresh separate · [apply 4.343](reports/SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01.md) · [freeze 4.342](reports/SITE-002-CATALOG-NORMALIZATION-DECISION-FREEZE-01.md) |
| Post-1C catalog monitor (Production) | **BASELINE 1887 ACTIVE — LIVE SITEMAP 1861 POST-NORMALIZATION (Run 4.343)** — refresh pending Apply 07 · [apply 4.343](reports/SITE-002-CATALOG-NORMALIZATION-APPLY-COMBINED-01.md) · [healthcheck 4.338](reports/SITE-002-POST-IMPORT-AND-MONITOR-HEALTHCHECK-01.md) · checkpoint [1887-09](baselines/SITE-002-STABLE-PROD-POST-C2-PRETTY-URL-MONITOR-BASELINE-1887-09.md) |
| Current catalog tree export (Production) | **COMPLETE / READ-ONLY (Run 4.339)** — DB-parent hierarchy **226** categories (**225 active / 1 inactive**), 10 roots, depth 3; all active categories match sitemap; baseline/live **1887**, URL delta 0/0; `upakovochnoe` absent DB+sitemap/404; tree ready for operator review; mutation 0 · [report](reports/SITE-002-CATALOG-TREE-CURRENT-EXPORT-01.md) · [tree](reports/SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-TREE.md) · [flat CSV](reports/SITE-002-CATALOG-TREE-CURRENT-EXPORT-01-FLAT.csv) |
| New sections onboarding / placement charter (Production) | **WAVE CLOSED / PERSISTENCE CONFIRMED** (Run **4.338**) — Wave B1 `95`/`364` mapped and persisted through natural imports 2026-08-20..24; `barnoe`/`upakovochnoe`/`hlebopekarnoe` root mapping still separate; pretty-URL baseline **1887** accepted · [healthcheck 4.338](reports/SITE-002-POST-IMPORT-AND-MONITOR-HEALTHCHECK-01.md) · [closeout 4.336](reports/SITE-002-POST-BASELINE-WORKSPACE-CLOSEOUT-01.md) · [apply 4.329](reports/SITE-002-PROD-NEW-SECTIONS-WAVE-B1-MAPPING-BACKFILL-APPLY-01.md) |
| Catalog structure / 1C placement (Production) | **POST-IMPORT PERSISTENCE CONFIRMED** (Run **4.299**) after importer GUID/path patch **4.297** / mapping **4.296** / leaves **4.295** — natural imports 2026-07-24..27 SUCCESS; critical **4707/4708→378**, **4710→379**, **4712→380**, **4709→376**; **demo Group A 154–170 physically deleted (Run 4.303)**; **legacy parent 153 physically deleted (Run 4.306)**; no redirects; sitemap live **1879** (post-import 2026-07-28); monitor baseline refreshed to **1879** (Run **4.312**); critical canonical after import (Run **4.311**); ambiguous empties inventoried in Run **4.308** (**119** charter-style / **99** leaves; DELETE_READY **0**; operator review **97**); HITL triage Run **4.309** — decision sheet ready (WAIT **96** / KEEP **1** / DELETE_CAND **0**; apply not executed); **Run 4.310** — empty neutral leaves under **79** intentionally UI-hidden until products (not a data bug) · [visibility diagnostic 4.310](reports/SITE-002-PROD-NEUTRAL-NEW-CATEGORIES-VISIBILITY-DIAGNOSTIC-01.md) · [HITL triage 4.309](reports/SITE-002-PROD-EMPTY-CATEGORIES-HITL-TRIAGE-01.md) · [review charter 4.308](reports/SITE-002-PROD-AMBIGUOUS-EMPTY-CATEGORIES-REVIEW-CHARTER-01.md) · [baseline refresh 4.307](reports/SITE-002-MONITOR-BASELINE-REFRESH-07.md) · [parent 153 delete apply 4.306](reports/SITE-002-PROD-PARENT-153-DELETE-APPLY-01.md) · [parent 153 review 4.305](reports/SITE-002-PROD-PARENT-153-REVIEW-CHARTER-01.md) · [delete apply 4.303](reports/SITE-002-PROD-DEMO-CATEGORY-DELETE-APPLY-01.md) · [demo cleanup 4.302](reports/SITE-002-PROD-DEMO-CATALOG-CLEANUP-CHARTER-01.md) · [legacy charter 4.301](reports/SITE-002-PROD-LEGACY-CATEGORY-CLEANUP-CHARTER-01.md) · [persistence check 4.299](reports/SITE-002-PROD-1C-POST-IMPORT-PERSISTENCE-CHECK-01.md) · [baseline refresh 4.300](reports/SITE-002-MONITOR-BASELINE-REFRESH-05.md) · [importer patch 4.297](reports/SITE-002-PROD-1C-IMPORTER-GUID-PATH-PATCH-01.md) |
| Catalog Section Tiles (Production) | **ACTIVE + POLISHED + MEGA PARITY + ALL-15 FIRST-LEVEL** (Runs **4.285**–**4.287** + **4.298** + **4.314** + **4.316** + **4.317**) — EN/RU Catalog Section Tiles; roots **79** + **362**; tech name `Технологическое оборудование`; tile images for **368/373/369/371/372/370** (+ regen **373/364/369/368**) + **375** `elektromehanicheskoe.webp` (Run **4.298**) + empty Neutral **82/83/85/87/89** images (Run **4.317**); `.btn.zpm-catalog__all-link` → `/katalog/`; mega menu children via `buildHubChildCards` (**neutral product gate still live for mega**); Run **4.316** ALL-15 Neutral tiles; Run **4.317** empty copy on PLP only (not cards) · [empty-copy+images 4.317](reports/SITE-002-PROD-EMPTY-CATEGORY-COPY-RELOCATE-AND-NEW-FIRSTLEVEL-IMAGES-01.md) · [all15 correction 4.316](reports/SITE-002-PROD-FIRST-LEVEL-BLOCK-ALL15-CORRECTION-APPLY-01.md) · [closeout 4.315](reports/SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-CLOSEOUT-01.md) · [hybrid apply 4.314](reports/SITE-002-PROD-FIRST-LEVEL-BLOCK-HYBRID-APPLY-01.md) · [scope decision 4.313](reports/SITE-002-PROD-FIRST-LEVEL-BLOCK-SCOPE-DECISION-01.md) · [first-level block charter 4.311](reports/SITE-002-PROD-POST-1C-NEUTRAL-FIRST-LEVEL-BLOCK-CHARTER-01.md) · [visibility diagnostic 4.310](reports/SITE-002-PROD-NEUTRAL-NEW-CATEGORIES-VISIBILITY-DIAGNOSTIC-01.md) · [elektro image 4.298](reports/SITE-002-PROD-ELEKTROMEHANICHESKOE-CATEGORY-IMAGE-APPLY-01.md) · [megamenu children 4.287](reports/SITE-002-PROD-MEGAMENU-CHILDREN-AUTOMATION-01.md) · [polish 4.286](reports/SITE-002-PROD-CATALOG-TILE-POLISH-01.md) · [tiles 4.285](reports/SITE-002-PROD-CATALOG-TILE-BLOCKS-AUTOMATION-01.md) |
| Catalog load more (Production) | **ACTIVE** (Run 4.185) — «Показать ещё» append via `initLoadMore()`; counter «Показано X из Y»; numeric pagination hidden when JS (`js-load-more`); rollback in Storage `deployments/SITE-002-PROD-LOAD-MORE-01/rollback/` |
| Neutral parent category tiles (Production) | **ACTIVE** (Run 4.195 + **4.220** + **4.221** + **4.236**) — **10** parent branches on homepage/hub `zpm-cat-card` (was 11); IDs `322,331,301,326,354,358,207,80,86,360`; **88** Лари removed from parent tiles (Run 4.236); display order **А → Я** (Run 4.221); `category_visibility.php` · [4.236 report](reports/SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md) · [4.221 report](reports/SITE-002-PROD-CATEGORY-ENTRYPOINTS-SORT-AZ-01.md) |
| Category Lari reparent (Production) | **ACTIVE — LARI CONFIRMED** (Run 4.235 + Run 4.248 + Run 4.250) — Лари id **88** `parent_id=358`; category_path nested; canonical `/shkafy-i-lari/lari`; flat `/lari` **301** (HEAD no-follow verified); sitemap nested only; Run **4.250** quick recheck **PASS** · [verification Run 4.250](reports/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md) · [verification Run 4.248](reports/SITE-002-PROD-POST-1C-LARI-REPARENT-AND-DURATION-VERIFICATION-02.md) · [implementation](reports/SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01.md) · [parent tiles](reports/SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md) |
| Contacts URL routing (Production) | **DECIDED — /CONTACT CANONICAL** (Run 4.238) — **`/contact` canonical** (`information/contact`, `oc_seo_url` **846**); `/kontakty` **404 accepted / not a bug**; no migration planned; Run 4.237 Option E **rejected**; optional future sitemap inclusion for `/contact` only · [decision](reports/SITE-002-PROD-CONTACTS-URL-ROUTING-DECISION-01.md) · [review](reports/SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01.md) |
| Full Tech SEO Audit (Production) | **COMPLETE — READ-ONLY** (Run 4.241) — 1408 sitemap URLs all HTTP 200; 0 broken internal links; 0 public **БЗПМ**; 11-item issue register + remediation roadmap; accepted `/kontakty` 404; `/contact` sitemap omission P3 optional · Storage `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\audits\SITE-002-PROD-FULL-TECH-SEO-AUDIT-01\` · [report](reports/SITE-002-PROD-FULL-TECH-SEO-AUDIT-01.md) · 0 mutation; checkpoint unchanged |
| Audit Wave C redirect hygiene (Production) | **COMPLETE — NO-OP** (Run 4.242) — flat Lari **301**→nested + bare `/index.php` **301**→`/` confirmed live; AUDIT-006 **resolved** (Run 4.241 false positive = urllib auto-follow); 0 FTP upload · [report](reports/SITE-002-PROD-AUDIT-WAVE-C-REDIRECT-HYGIENE-01.md) · Storage `deployments/SITE-002-PROD-AUDIT-WAVE-C-REDIRECT-HYGIENE-01/` |
| Audit Wave B SEO foundation (Production) | **COMPLETE** (Run 4.243) — sitemap 1408→1409; 0 legacy `index.php?route=information` URLs; `/contact` in sitemap; redundant `compare-products`/`wishlist` seo_url rows removed (928/927); 1 FTP upload + scoped DB DELETE; AUDIT-007/004/002 **fixed**; AUDIT-010 partially resolved · [report](reports/SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md) · [checkpoint](baselines/SITE-002-STABLE-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01.md) · Storage `deployments/SITE-002-PROD-AUDIT-WAVE-B-SEO-FOUNDATION-01/` |
| Neutral category image white-bg refresh (Production) | **ACTIVE** (Run 4.196) — 3 images refreshed to white studio style (354/358/86); 331 deferred; master `1800×1200` + cache `300×300` FTP overwrite; 0 admin saves; **COMPOSER_ONLY_NO_API** · [report](reports/SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01.md) |
| Polki category image fix (Production) | **ACTIVE** (Run 4.197) — ID 331 Полки настенные и настольные refreshed; master+cache FTP overwrite; stale dark cache replaced; 0 admin saves; **COMPOSER_ONLY_NO_API** · [report](reports/SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01.md) |
| Elektromehanicheskoe category image (Production) | **ACTIVE** (Run **4.298**) — category **375** under **362**; `catalog/Category-image/elektromehanicheskoe.webp` + `300×300` cache; DB image bind; legacy **153** untouched; **COMPOSER_ONLY_NO_API**; reconfirmed in Run **4.300** · [report](reports/SITE-002-PROD-ELEKTROMEHANICHESKOE-CATEGORY-IMAGE-APPLY-01.md) |
| Mail recipients architecture (Production) | **ACTIVE — TEMP TEST RECIPIENT** (Run 4.264 confirm · Run 4.265 re-verify · Run 4.266 full form mail rerun) — `config_mail_alert_email` currently **only** `client.leads@polygon-ws.ru`; `info@bzpm.ru` **not** restored yet; handler `catalog/controller/checkout/anketa.php`; admin-managed comma list · empty-lead backend guard OK (8 valid 200 / 3 negatives 400) · [full rerun](reports/SITE-002-PROD-FORM-MAIL-FULL-TEST-RERUN-01.md) · [follow-up](reports/SITE-002-PROD-FORM-EMPTY-LEAD-GUARD-FOLLOWUP-01.md) · [audit](reports/SITE-002-PROD-1C-LOGS-AND-FORM-MAIL-AUDIT-01.md) · [discovery](reports/SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01.md) · [confirmation](reports/SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01.md) |
| Mail system architecture (Production) | **DISCOVERED — REDESIGN CHARTERS READY** (Run 4.222) — read-only full mail map: 29 public forms → anketa; standard OC twig mails (order/account/affiliate); no service info in admin form mail today; hybrid shared-renderer recommended; 5 future charters; Beget backup confirmed; 0 Production mutation · [report](reports/SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01.md) · [audit baseline](baselines/SITE-002-MAIL-SYSTEM-DISCOVERY-01.md) |
| Catalog default sort (Production) | `pd.name ASC` when `sort`/`order` omitted |
| Custom blog / scheduled news (Production) | **ACTIVE** (Run **4.279** smoke GREEN + **4.282** hotfix) — post **13** live; SEO `/blog/news/{slug}` + `/blog/news` via `seo_url.php` full-path bridge **preserved**; Run **4.282** also rebuilds incomplete product `path` for parent-PLP PDPs; brand/sliders OK · [hotfix 4.282](reports/SITE-002-PROD-REGRESSION-HOTFIX-01.md) · [final smoke 4.279](reports/SITE-002-PROD-BLOG-WAVE-FINAL-SMOKE-01.md) · [SEO routing 4.278](reports/SITE-002-PROD-BLOG-SEO-URL-ROUTING-FIX-01.md) |

---

## Current implementation inheritance

Production is **believed** to inherit the transferred TEST state including:

| Area | Evidence class |
|------|----------------|
| M9.13 About | TEST-proven implementation |
| M9.14 Delivery | TEST-proven implementation |
| M9.15 Payment | TEST-proven implementation |
| M9.16 Dealers | TEST-proven implementation |
| M9.17 Warranty | TEST-proven implementation |
| M9.18 Custom Manufacturing | TEST-proven implementation |
| Post-corporate polish checkpoints | TEST-proven implementation |
| Local Fonts checkpoint | TEST-proven implementation |
| Home Commercial Trust checkpoint | TEST-proven implementation |

| Classification | Value |
|----------------|-------|
| Implementation evidence | **TEST-PROVEN IMPLEMENTATION** |
| Production parity | **VERIFIED** (HTTP + file baseline, Run 4.171-R1) |

---

## Storage bindings

**Production storage root:**

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\
```

| Subfolder | Purpose |
|-----------|---------|
| `backups\` | Scoped pre-change Production backups |
| `baselines\` | Promoted Production baseline artefacts (future) |
| `captures\` | Read-only remote inventory and page captures |
| `deployments\` | Deployment manifests and scoped deploy evidence |
| `verification\` | HTTP smoke, visual verification, operator sign-off evidence |
| `rollback\` | Rollback packages and restore evidence |
| `reports\` | Production operation reports |

**Shared image directories:** reuse existing SITE-002 shared image storage when appropriate. Do not duplicate the image library unless a Production-specific image area is explicitly required.

**Storage README:** `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\production\README.md`

---

## Production path model (Run 4.172)

| Concept | Hosting / application path | FTP-visible path | Status |
|---------|---------------------------|------------------|--------|
| Application root | `/bzpm.ru/` | `/` (chrooted login root) | **CONFIRMED** |
| Public document root | `/bzpm.ru/public_html/` | `/public_html/` | **CONFIRMED** |
| OpenCart storage root | `/bzpm.ru/storage/` | `/storage/` | **CONFIRMED** |

**Secrets field `Remote root`:** denotes **application root** (`/bzpm.ru/`), not the public web directory. Public deploy paths are relative to `public_html/` inside the application root.

**FTP chroot:** the Production FTP account lands at `/` with first-level directories `public_html/` and `storage/`. This is equivalent to hosting application root `/bzpm.ru/`, not a separate site root.

**Example deploy path (guarantee.twig):**

```text
Hosting: /bzpm.ru/public_html/catalog/view/theme/default/template/information/guarantee.twig
FTP:     /public_html/catalog/view/theme/default/template/information/guarantee.twig
```

Do **not** describe `/public_html/` as the application root for the whole OpenCart installation.

---

## Credential binding

**Canonical secrets file:**

```text
X:\AI MARS STORAGE\ocpilot\project-sites\site-002\secrets\secrets.md
```

| Section | Use |
|---------|-----|
| `TEST` | Historical TEST environment credentials |
| `PRODUCTION` | Production environment credentials — operator to populate |

**Supported categories:** FTP / SFTP · Hosting panel · OpenCart Admin · SSH · Database · DNS / Domain · Additional Notes

| Rule | Value |
|------|-------|
| Database access | **NOT AUTHORIZED BY DEFAULT** |
| Secrets in Git | **FORBIDDEN** |
| Credential testing (this registration) | **NOT PERFORMED** |

---

## Operation model

Future Production write sequence (human-supervised):

1. Read Production Profile
2. Read local secrets (`PRODUCTION` section)
3. Confirm exact target (URL, environment ID, remote path)
4. Create scoped backup
5. Prepare local diff and manifest
6. Obtain operator approval
7. Deploy exact scope
8. Verify HTTP and visual result
9. Keep rollback ready
10. Produce report

**Recommended operation identifier:** `SITE-002-PROD-YYYYMMDD-NN`

---

## First controlled Production change (Run 4.173)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-TEXT-CHANGE-01` |
| Status | **COMPLETE** |
| Deploy method | single-file FTP |
| Remote target | `/public_html/catalog/view/theme/default/template/information/guarantee.twig` |
| Change | `понятный порядок действий` → `чёткий порядок действий` |
| Rollback readiness | **VERIFIED** |
| Post-deploy verification | **PASS** — remote hash, HTTP 200, desktop/mobile screenshots |
| Current Production checkpoint | `SITE-002-STABLE-PROD-TEXT-CHANGE-01` |
| Report | [reports/SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md](reports/SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md) |

Verified proof boundary:

```text
single-file text-only FTP deploy with backup and rollback readiness
```

This does not prove generic deploy tooling for other file classes, cache clearing, OpenCart admin changes, database changes, or bulk operations.

---

## Catalog default sort (Run 4.176)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-SORT-AZ-01` |
| Status | **COMPLETE** |
| Deploy method | single-controller FTP |
| Remote target | `/public_html/catalog/controller/product/category.php` |
| Change | default `p.date_added DESC` → `pd.name ASC` |
| Rollback readiness | **VERIFIED** |
| Post-deploy verification | **PASS** — remote hash, HTTP 200, desktop/mobile screenshots |
| Current Production checkpoint | `SITE-002-STABLE-PROD-SORT-AZ-01` |
| Report | [reports/SITE-002-PROD-SORT-AZ-01.md](reports/SITE-002-PROD-SORT-AZ-01.md) |

Verified proof boundary:

```text
single-controller-file FTP deploy with backup, dry-run, verification, rollback readiness
```

Does not prove multi-file frontend deploy (Twig/CSS/JS), cache clearing, or database operations.

---

## Catalog sort menu order (Run 4.177)

| Field | Value |
|-------|-------|
| Operation | `SITE-002-PROD-SORT-MENU-ORDER-01` |
| Status | **COMPLETE** |
| Deploy method | single-Twig FTP |
| Remote target | `/public_html/catalog/view/theme/default/template/product/category.twig` |
| Change | remove «Умолчанию»; reorder menu: A→Я, Я→А, price ASC, price DESC |
| Default catalog sort (controller) | unchanged — `pd.name ASC` (Run 4.176) |
| Rollback readiness | **VERIFIED** |
| Post-deploy verification | **PASS** — remote hash, HTTP 200, desktop/mobile screenshots |
| Current Production checkpoint | `SITE-002-STABLE-PROD-SORT-MENU-ORDER-01` |
| Report | [reports/SITE-002-PROD-SORT-MENU-ORDER-01.md](reports/SITE-002-PROD-SORT-MENU-ORDER-01.md) |

Verified proof boundary:

```text
single-Twig-file FTP deploy with backup, dry-run, verification, rollback readiness
```

Does not prove multi-file frontend deploy, CSS/JS deploy, cache clearing, or database operations.

---

## Approval gates

Every Production **write** requires:

| Gate | Required |
|------|----------|
| Exact task scope | yes |
| Exact remote path | yes |
| Backup | yes |
| Rollback method | yes |
| Operator approval | yes |
| Post-change verification | yes |

Read-only inspection does **not** require a separate approval gate once Production connection has been explicitly authorized for read-only work.

---

## Protected zones

Protected by default — separate explicit task and operator authorization required:

| Zone | Notes |
|------|-------|
| `config.php` | Core configuration |
| `admin/config.php` | Admin configuration |
| `system/` | Core system |
| `storage/` | OpenCart storage |
| `image/catalog/` bulk operations | Mass image changes |
| Payment modules | Checkout-related |
| Checkout | Order flow |
| Cron | Scheduled jobs |
| Database | **NOT AUTHORIZED BY DEFAULT** |
| Server configuration | Hosting-level |
| DNS | Domain routing |
| Mail configuration | SMTP / mail |

Protected does **not** mean permanently forbidden.

---

## Deploy, rollback, and verification bindings (registered, not verified)

| Profile | Storage binding | Status |
|---------|-----------------|--------|
| Deploy profile | `production\deployments\` | REGISTERED, NOT VERIFIED |
| Rollback profile | `production\rollback\` | REGISTERED, NOT VERIFIED |
| Verification profile | `production\verification\` | REGISTERED, NOT VERIFIED |

Future Production tooling must:

- use the `PRODUCTION` section of the local secrets file;
- use `X:\` paths;
- avoid hardcoded credentials;
- avoid historical `C:\MARS Phenix` paths;
- support exact file scope;
- support backup and rollback;
- produce a manifest.

Deploy-tool preparation is a **separate task**.

---

## Registration state

| Item | State |
|------|-------|
| Production identity | **REGISTERED** |
| Production URL | **REGISTERED** |
| Storage bindings | **REGISTERED** |
| Credential slots | **REGISTERED** |
| Credentials populated | **YES** |
| HTTP connection | **VERIFIED** (Run 4.171) |
| Admin read-only connection | **VERIFIED** (Run 4.171) |
| FTP/SFTP connection | **VERIFIED** (Run 4.171-R1) |
| Remote listing | **VERIFIED** — application root `/bzpm.ru/`; FTP chroot `/` → `public_html/` + `storage/` |
| Production baseline | **SUPERSEDED BY TEXT CHANGE CHECKPOINT** — parent `SITE-002-STABLE-PROD-INITIAL-01` |
| Current Production checkpoint | **ISSUED** — `SITE-002-STABLE-PROD-SORT-AZ-01` (2026-07-05) |
| Deploy profile | **VERIFIED FOR SINGLE-FILE TEXT-ONLY FTP DEPLOY** |
| Rollback profile | **READINESS VERIFIED FOR SINGLE-FILE RESTORE** |
| Verification profile | **VERIFIED** — file hash + HTTP + desktop/mobile screenshots |
| First Production change | **COMPLETE** — `SITE-002-PROD-TEXT-CHANGE-01` |

---

## Related documents

- Registration report: [reports/SITE-002-PRODUCTION-PROFILE-REGISTRATION.md](reports/SITE-002-PRODUCTION-PROFILE-REGISTRATION.md)
- External storage registry: [../../external-storage-registry.md](../../external-storage-registry.md)
- Recovery closeout: [reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md)


| Offers + price form diagnostic (Production) | **COMPLETE — FORM FIXED / IMPORT ATTENTION** (Run **4.320**, 2026-08-06) — `offers0_*.xml` absent; latest import SUCCESS with offers inputs none; price-list dialog7 UI fixed (FormData before `zpmFormSetLoading`); sitemap 1879 · [report](reports/SITE-002-PROD-1C-OFFERS-MISSING-AND-PRICE-FORM-DIAGNOSTIC-01.md) |
| Price form spam guard (Production) | **ACTIVE — LAYERED ANTI-SPAM** (Run **4.321**, 2026-08-10) — dialog7 gibberish blocked via honeypot `zpm_hp` / timestamp `zpm_ft` / risk scoring / soft-hard rate-limit in `checkout/anketa.php` + `assets/js/main.js`; empty-lead guard + Run 4.320 FormData fix intact; recipients unchanged · [report](reports/SITE-002-PROD-PRICE-FORM-SPAM-GUARD-01.md) |
| Stable prod checkpoint after spam guard | **ISSUED** (Run **4.322**, 2026-08-12) — Git tag `site-002/stable-prod-after-spam-guard-20260812`; operator `SPAM_GUARD_OBSERVATION_PRELIMINARY_OK` + dealer form OK; later healthcheck Run **4.325** confirms 1C offers recovery closed and shifts attention to onboarding / monitor semantics · [report](reports/SITE-002-PROD-STABLE-CHECKPOINT-AFTER-SPAM-GUARD-AND-CLEANUP-INVENTORY-01.md) · [offers recovery healthcheck](reports/SITE-002-PROD-POST-1C-OFFERS-RECOVERY-AND-NEW-SECTIONS-HEALTHCHECK-01.md) |
