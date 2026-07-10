# SITE-002 — Site Passport

**Status:** **STABLE PRODUCTION CHECKPOINT — POST-1C LARI DURATION MONITOR MANUAL VERIFIED** (checkpoint `SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01`; Run 4.252 consolidation; parent Wave E)
**Run:** 4.252 — SITE-002 Stable Checkpoint Consolidation (2026-07-10)

---

## Identity

| Field | Value |
|-------|-------|
| **Site ID** | SITE-002 |
| **Site Name** | ЗПМ |
| **Slug** | site-002 |
| **Platform** | ocStore / OpenCart |
| **Version** | **3.0.3.9** (Production admin read-only, Run 4.171) |
| **Baseline Match** | `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` (Home) · `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` (About) · `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` (site-wide fonts) |
| **Hosting** | Beget (FTP `polygonws.beget.tech`) — operator-recorded |
| **Repository metadata** | `X:\AI MARS\projects\ocpilot\sites\site-002\` |
| **Access Methods** | Documented in [project-access-brief.md](project-access-brief.md); credential locations outside repo |
| **Storage Location** | `X:\AI MARS STORAGE\ocpilot\project-sites\site-002\` |
| **Local runtime root** | `X:\MARS-Localhost\` |
| **SITE-002 runtime subpath** | SAFE UNKNOWN — verify before execution (MLI pattern: `sites\opencart\projects\{slug}\`; `site-002` tree not verified on `X:` at 2026-06-29) |
| **Current operational environment** | **PRODUCTION** |
| **Production URL** | https://bzpm.ru/ |
| **Historical TEST URL** | https://zpm.new-site.space/ |
| **Environment (legacy field)** | TEST (historical registration) · Production registered 2026-07-02 |
| **Production Profile** | [production-profile.md](production-profile.md) |
| **Production connection** | **VERIFIED** — HTTP/admin (Run 4.171) + FTP/file baseline (Run 4.171-R1); path model reconciled (Run 4.172) |
| **Production baseline** | **PARENT** — [baselines/SITE-002-STABLE-PROD-INITIAL-01.md](baselines/SITE-002-STABLE-PROD-INITIAL-01.md) |
| **Current Production checkpoint** | **ISSUED** — [baselines/SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01.md](baselines/SITE-002-STABLE-PROD-POST-1C-LARI-DURATION-MONITOR-MANUAL-VERIFIED-01.md) (parent [SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md](baselines/SITE-002-STABLE-PROD-AUDIT-WAVE-E-INFO-META-H1-01.md)) |
| **Public brand policy** | **ЗПМ** — correct public Russian brand · **БЗПМ** forbidden in public copy/meta/llms/generated output · domain `bzpm.ru` unchanged · **0 violations after Run 4.207 edge fix** |
| **Deep PLP meta edge fix** | **COMPLETE — DEEP PLP META VERIFIED** (Run 4.207) — [report](reports/SITE-002-PROD-SEO-META-EDGE-FIX-01.md) |
| **New catalog branch onboarding** | **COMPLETE** (Run 4.210 + 4.211) — konditerskiy-inventar/formy-konditerskie (360/361); lari branches (88/141/140); deferred `/lari/proizvodstvennye-lari` resolved · [follow-up](reports/SITE-002-PROD-CATALOG-BRANCH-ONBOARDING-FOLLOWUP-01.md) · [Run 4.210](reports/SITE-002-PROD-CATALOG-NEW-BRANCH-ONBOARDING-01.md) |
| **Accepted UX tasks (intake)** | (1) new section tiles — **DONE** Run 4.220 · [entrypoints 02 report](reports/SITE-002-PROD-NEW-SECTIONS-ENTRYPOINTS-02.md) · (2) PDP «Дополнительные сведения» — **DONE** Run 4.218 · [layout report](reports/SITE-002-PROD-PDP-EXTRA-INFO-ATTRIBUTE-LAYOUT-01.md) · [intake report](reports/SITE-002-PROD-UX-TASK-INTAKE-01.md) |
| **Post-1C catalog monitor** | **RUNNER CONFIRMED — HARDENED ARTIFACTS CONFIRMED MANUALLY** (Run 4.251 + Run 4.252) — operator manual run **2026-07-10 13:27 +07** → folder `2026-07-10_13-27-20` (full Run 4.228 contract); Task LastTaskResult **0**; classification **ONBOARDING_REQUIRED** (5 needs); natural post-hardening scheduled timing on 2026-07-10 **NOT CLAIMED** — workstation off/unavailable; historical scheduled run **2026-07-08** LastTaskResult **0** · [consolidation report](reports/SITE-002-STABLE-CHECKPOINT-CONSOLIDATION-01.md) · [manual run report](reports/SITE-002-LOCAL-MONITOR-MANUAL-RUN-01.md) · [verification Run 4.250](reports/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md) · [hardening](reports/SITE-002-POST-1C-MONITOR-ARTIFACTS-HARDENING-01.md) · [runbook](runbooks/SITE-002-POST-1C-MONITOR-AUTOMATION-RUNBOOK.md) |
| **Sitemap authority** | **COMPLETE — AUTO-GENERATED FEED CONFIRMED** (Run 4.214) — OpenCart `extension/feed/google_sitemap`; physical file absent; live per-request; MARS does not manually edit XML; audit baseline [SITE-002-SITEMAP-AUTHORITY-DISCOVERY-01](baselines/SITE-002-SITEMAP-AUTHORITY-DISCOVERY-01.md) · [report](reports/SITE-002-PROD-SITEMAP-AUTHORITY-DISCOVERY-01.md) |
| **MARS 1C cron wrapper** | **OPERATIONAL — FIRST SCHEDULED RUN VERIFIED** (Run 4.194) — automatic run SUCCESS 2026-07-06 08:00 Moscow; run ID `mars-20260706-080002-09436ae7`; report `mars_1c_import_2026-07-06_080007.txt`; daily import OPERATIONAL; Sergey legacy preserved |
| **Mail recipients** | **ACTIVE — ADMIN-MANAGED** (Run 4.187) — handler `checkout/anketa.php`; list via OpenCart `config_mail_alert_email`; operator updated admin **Additional Alert Emails**; delivery verified; no code deploy · [discovery](reports/SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01.md) · [confirmation](reports/SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01.md) |
| **Mail system (redesign intake)** | **DISCOVERED — CHARTERS READY** (Run 4.222) — full read-only map: anketa forms + standard OC mails; no service info in admin form mail; hybrid renderer recommended; Beget backup confirmed; 0 mutation · [report](reports/SITE-002-PROD-MAIL-SYSTEM-DISCOVERY-01.md) · [audit baseline](baselines/SITE-002-MAIL-SYSTEM-DISCOVERY-01.md) |
| **Mail design system (Production)** | **ACTIVE — CUSTOMER CONFIRMATIONS + LOADING UX** (Run 4.226) — conditional customer confirmations; no service info in customer emails; form loading/abort UX · **delivery retest** Run 4.231 — submit `ok: true` · **inbox confirmation** Run 4.232 — operator verified delivery/design/no service info · [report](reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-01.md) · [delivery confirmation](reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-DELIVERY-CONFIRMATION-01.md) · [inbox confirmation](reports/SITE-002-PROD-MAIL-CUSTOMER-FORMS-INBOX-CONFIRMATION-01.md) · [checkpoint](baselines/SITE-002-STABLE-PROD-MAIL-CUSTOMER-FORMS-01.md) |
| **Info page corp CTA forms** | **ACTIVE — INTEGRATED** (Run 4.230) — 5 forms wired to AJAX mail pipeline; dialogs 7/8/9/10/11; inline success-state · [report](reports/SITE-002-PROD-INFO-PAGE-FORMS-INTEGRATION-01.md) · [checkpoint](baselines/SITE-002-STABLE-PROD-INFO-PAGE-FORMS-01.md) |
| **Category Lari reparent** | **ACTIVE — LARI CONFIRMED** (Run 4.235 + Run 4.248 + Run 4.250) — Лари **88** under **358**; category_path nested; flat `/lari` **301**; Run **4.250** quick recheck **PASS** · [verification 03](reports/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md) · [reparent](reports/SITE-002-PROD-CATEGORY-LARI-REPARENT-IMPLEMENTATION-01.md) · [parent tiles](reports/SITE-002-PROD-PARENT-CATEGORY-TILES-LARI-REMOVAL-01.md) |
| **Contacts URL routing** | **DECIDED — /CONTACT CANONICAL** (Run 4.238) — **`/contact` canonical**; `/kontakty` **404 accepted**; Option E **rejected**; no implementation planned · [decision](reports/SITE-002-PROD-CONTACTS-URL-ROUTING-DECISION-01.md) · [review](reports/SITE-002-PROD-CONTACTS-URL-ROUTING-REVIEW-01.md) |
| **MARS 1C cron reports** | **CONFIRMED** (Run 4.250) — post-patch TXT `mars_1c_import_2026-07-10_080008.txt`; Duration **6.17s**; SUCCESS · [verification 03](reports/SITE-002-PROD-DURATION-MONITOR-VERIFICATION-03.md) · [duration fix](reports/SITE-002-PROD-CRON-RUN-REPORTS-DURATION-FIX-01.md) |
| **Current Status** | **STABLE PRODUCTION CHECKPOINT — POLKI CATEGORY IMAGE 01** |
| **Active baseline** | [baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md) · About: [M9.13-ABOUT-REDESIGN-02](baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02.md) · fonts: [LOCAL-FONTS-01](baselines/SITE-002-STABLE-LIVE-LOCAL-FONTS-01.md) |
| **Technical Knowledge Map** | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — incl. [§7 Filter Architecture](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#7-filter-architecture), [§8 Live Files](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#8-live-files-with-business-logic), [§14 Commercial Trust Block](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#14-commercial-trust-block), [§16 Catalog State Persistence](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#16-catalog-state-persistence), [§17 About Page History](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#17-about-page-history), [§26 Operator Manual Polish 01](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#26-operator-manual-polish-01--superseded-visual-baseline-retained), [§27 Local Fonts 01](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#27-local-fonts-01--active) |
| **Operator manual JS (04B)** | [reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md](reports/SITE-002-M9.8.9-04B-OPERATOR-MANUAL-JS-POLISH-REGISTRATION.md) |
| **Rollback source** | Beget full backup + current live TEST + file-level pass backups |
| **Notes** | Production first controlled change **COMPLETE**: single-file text-only FTP deploy on `/guarantee`, rollback readiness verified, HTTP/visual verification PASS, current Production checkpoint `SITE-002-STABLE-PROD-TEXT-CHANGE-01`. TEST площадка remains historical evidence. **MANUAL UI / CSS / TWIG / JS REFINEMENTS ARE CANONICAL** for TEST-era context. **Delivery summary strip** — Commercial Trust service cards on `/delivery` **PASS** (2026-06-29) · [Knowledge Map §32](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#32-delivery-summary--commercial-trust-reuse-active) · checkpoint `SITE-002-STABLE-LIVE-DELIVERY-SUMMARY-01`. **Custom OEM proof strip** — Commercial Trust service cards on `/custom-equipment` **PASS** (2026-06-29) · [Knowledge Map §31](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#31-custom-oem-proof-strip--commercial-trust-reuse-active) · checkpoint `SITE-002-STABLE-LIVE-CUSTOM-PROOF-STRIP-01`. **PDP body category classes** — `category-root-*` / `category-parent-*` on product pages **PASS** (2026-06-29) · [Knowledge Map §30](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#30-pdp-body-category-classes-01--active) · checkpoint `SITE-002-STABLE-LIVE-PDP-BODY-CATEGORY-CLASSES-01`. **Corporate intro blocks** — `.zpm-corp-intro` on 6 corp pages **PASS** (2026-06-29 closeout) · [Knowledge Map §29](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md#29-corporate-intro-image-blocks-01--active) · checkpoint `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01`. **Home CTA** — `zpm-commercial-trust` active (2026-06-29). **M9.13 About redesign RE-ACTIVATED** (2026-06-29). Local Fonts 01 **retained**. |

---

## Authority policy

| Rule | Value |
|------|-------|
| **Authority checkpoint** | `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` (Home) · `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` (About) · `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` (fonts) · `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` (visual baseline) · `SITE-002-STABLE-LIVE-CORPORATE-INTRO-BLOCKS-01` (corp intro) |
| **MANUAL UI REFINEMENTS ARE CANONICAL** | Operator manual CSS, Twig, JS, and UX edits on live TEST override older M9.x deploy snapshots |
| **MANUAL CSS REFINEMENTS ARE CANONICAL** | Operator CSS edits on live TEST override repo work copies |
| **MANUAL TWIG REFINEMENTS ARE CANONICAL** | Operator Twig edits on live TEST override repo work copies |
| **Conflict resolution (Production)** | Current operational website authority = https://bzpm.ru/; cron checkpoint `SITE-002-STABLE-PROD-CRON-SCHEDULED-RUN-01`; SEO checkpoint `SITE-002-STABLE-PROD-LLMS-TXT-UTF8-01` (parent llms `SITE-002-STABLE-PROD-LLMS-TXT-01`; keywords `SITE-002-STABLE-PROD-SEO-PRODUCT-META-KEYWORDS-01`; product meta `SITE-002-STABLE-PROD-SEO-PRODUCT-META-01`; information meta `SITE-002-STABLE-PROD-SEO-INFORMATION-META-01`; sitemap `SITE-002-STABLE-PROD-SITEMAP-01`); llms.txt at `/llms.txt` **UTF-8 BOM VERIFIED** (Run 4.204); daily 1C import **OPERATIONAL** (Run 4.194); product PDP keywords v1.1 **DEPLOYED** (Run 4.202); product PDP meta generator **DEPLOYED** (Run 4.201); valid XML sitemap at `/sitemap.xml` (Run 4.191); duplicate body fixed (Run 4.190); Yandex **VERIFIED** (Run 4.189) — header/footer **DO NOT OVERWRITE** |
| **Conflict resolution (TEST evidence)** | If documentation contradicts historical TEST state, live TEST on https://zpm.new-site.space/ remains evidence for TEST-era checkpoints |
| **Do NOT use as visual baseline** | Pass 1.2 CSS/HTML/JS · `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` · pre-checkpoint work copies · `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` · M9.13 About redesign work copies |

---

## Production checkpoint (current)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-PROD-SITEMAP-01` |
| Registered | 2026-07-06 |
| Type | Stable Production checkpoint — valid XML sitemap + robots Sitemap directive |
| Parent | `SITE-002-STABLE-PROD-HTML-BODY-FIX-01` |
| Operation | `SITE-002-PROD-SITEMAP-ENABLE-01` |
| Scope | OpenCart Google Sitemap feed enable (admin) + `/public_html/robots.txt` Sitemap line |
| Report | [SITE-002-PROD-SITEMAP-ENABLE-01.md](reports/SITE-002-PROD-SITEMAP-ENABLE-01.md) |

Verified proof boundary: admin single-setting enable, robots.txt backup/deploy, sitemap HTTP/XML verification (1320 URLs), Yandex + single-body spot check, rollback readiness.

---

## Prior Production checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-PROD-HTML-BODY-FIX-01` |
| Registered | 2026-07-06 |
| Type | Stable Production checkpoint — duplicate body/preloader HTML fix |
| Parent | `SITE-002-STABLE-PROD-SEO-ROBOTS-01` |
| Operation | `SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01` |
| Scope | `/public_html/catalog/view/theme/default/template/common/header.twig` only |
| Report | [SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01.md](reports/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01.md) |

Verified proof boundary: single-file header.twig FTP deploy with backup, Yandex preservation gate, 4-URL HTML structure verification, rollback readiness.

---

## Prior Production checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-PROD-SEO-ROBOTS-01` |
| Registered | 2026-07-06 |
| Type | Stable Production checkpoint — SEO readiness + robots.txt deploy |
| Parent | `SITE-002-STABLE-PROD-LOAD-MORE-01` |
| Operation | `SITE-002-PROD-SEO-READINESS-ROBOTS-01` |
| Scope | `/public_html/robots.txt` only; non-product meta audit artefacts |
| Report | [SITE-002-PROD-SEO-READINESS-ROBOTS-01.md](reports/SITE-002-PROD-SEO-READINESS-ROBOTS-01.md) |

Verified proof boundary: single-file robots.txt FTP deploy with backup, deploy gates, HTTP verification, rollback readiness; meta audit non-product only.

---

## Prior Production checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-PROD-LOAD-MORE-01` |
| Registered | 2026-07-06 |
| Type | Stable Production checkpoint — multi-file catalog load-more deploy |
| Parent | `SITE-002-STABLE-PROD-CRON-BEGET-ACTIVE-01` |
| Operation | `SITE-002-PROD-LOAD-MORE-01` |
| Scope | category.twig/php, main.js, style.css — append load-more + counter |
| Report | [SITE-002-PROD-LOAD-MORE-01.md](reports/SITE-002-PROD-LOAD-MORE-01.md) |

Verified proof boundary: multi-file catalog frontend FTP deploy with backup, dry-run, HTTP/visual verification, rollback readiness.

---

## Prior Production checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-PROD-SORT-MENU-ORDER-01` |
| Registered | 2026-07-06 |
| Type | Stable Production checkpoint — single-Twig catalog sort menu deploy |
| Parent | `SITE-002-STABLE-PROD-SORT-AZ-01` |
| Operation | `SITE-002-PROD-SORT-MENU-ORDER-01` |
| Scope | sort menu order in `category.twig`; «Умолчанию» removed |
| Report | [SITE-002-PROD-SORT-MENU-ORDER-01.md](reports/SITE-002-PROD-SORT-MENU-ORDER-01.md) |

Verified proof boundary: single-Twig-file FTP deploy with backup, dry-run, verification, rollback readiness.

---

## Prior Production checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-PROD-SORT-AZ-01` |
| Registered | 2026-07-05 |
| Type | Stable Production checkpoint — single-controller catalog sort deploy |
| Parent | `SITE-002-STABLE-PROD-TEXT-CHANGE-01` |
| Operation | `SITE-002-PROD-SORT-AZ-01` |
| Scope | default catalog sort `pd.name ASC` in `category.php` |
| Report | [SITE-002-PROD-SORT-AZ-01.md](reports/SITE-002-PROD-SORT-AZ-01.md) |

Verified proof boundary: single-controller-file FTP deploy with backup, dry-run, verification, rollback readiness.

---

## Prior Production checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-PROD-TEXT-CHANGE-01` |
| Registered | 2026-07-04 |
| Type | Stable Production checkpoint — first controlled single-file text deploy |
| Parent | `SITE-002-STABLE-PROD-INITIAL-01` |
| Operation | `SITE-002-PROD-TEXT-CHANGE-01` |
| Scope | `/guarantee` text replacement in `guarantee.twig` |
| Report | [SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md](reports/SITE-002-FIRST-CONTROLLED-PRODUCTION-CHANGE.md) |

Verified proof boundary: single-file text-only FTP deploy with backup and rollback readiness.

---

## Stable TEST checkpoint (historical evidence)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01` |
| Registered | 2026-06-29 |
| Type | Stable live checkpoint — Home CTA band FTP deploy |
| Scope | Home only — `/katalog` legacy `blockdealersform` preserved |
| Report | [SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md](reports/SITE-002-HOME-COMMERCIAL-TRUST-REPLACEMENT.md) |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §28 |

**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-HOME-COMMERCIAL-TRUST-01.md)

---

## Prior stable checkpoint

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01` |
| Registered | 2026-06-29 |
| Type | Stable live checkpoint — FTP read-only capture + metadata registration |
| Supersedes (live truth) | `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` |
| Operator manual delta | `style.css` · `dealers.twig` changed vs Pass 1.2 / Pass 1.1 deploy snapshots |
| Capture | [capture-manifest.json](reports/site-002-operator-manual-polish-01-work/capture-manifest.json) |
| Knowledge map | [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md) — §26 |
| Registration | [reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md](reports/SITE-002-STABLE-CHECKPOINT-OPERATOR-MANUAL-POLISH-01.md) |

**Baseline doc:** [baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-OPERATOR-MANUAL-POLISH-01.md)

---

## Prior checkpoints (historical)

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2` |
| Doc | [baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md](baselines/SITE-002-STABLE-LIVE-CORPORATE-PAGES-VISUAL-POLISH-PASS-1.2.md) |
| Scope | Corp visual polish Pass 1.2 — **superseded**; do not use as reference |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md](baselines/SITE-002-STABLE-LIVE-M9.13-ABOUT-COMPANY-RESTORED-01.md) |
| Scope | About restoration — superseded for live visual truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-CATALOG-UX-COMPLETE-01.md) |
| Scope | Catalog UX cluster — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-COMMERCIAL-TRUST-01.md) |
| Scope | Commercial Trust — superseded for live truth |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md](baselines/SITE-002-STABLE-LIVE-M9.8.9-FILTER-UX-COMPLETE-01.md) |
| Scope | Filter recovery + filter UX — historical |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01` |
| Doc | [baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md](baselines/SITE-002-STABLE-LIVE-M9.8-UX-POLISH-01.md) |
| Scope | M9.8.1/2/5 + operator PLP polish — historical |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14` |
| Doc | [baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md](baselines/SITE-002-STABLE-LIVE-PDP-V5.1-2026-06-14.md) |
| Scope | PDP V5.1 · Category V2.3.1 — historical |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI` |
| Doc | [reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md](reports/SITE-002-STABLE-M9.7D-AFTER-MANUAL-UI.md) |
| Scope | File + scoped DB JSON backup — historical file rollback only |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE` |
| Doc | [reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md](reports/SITE-002-STABLE-M9.7E-HOMEPAGE-COMPLETE.md) |
| Scope | Historical capture — homepage 5-branch deploy |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M9-COMPLETE-20260615` |
| Doc | [reports/SITE-002-STABLE-M9-COMPLETE.md](reports/SITE-002-STABLE-M9-COMPLETE.md) |
| Scope | Pre-M9.7D / pre-manual UI |

| Field | Value |
|-------|--------|
| Name | `SITE-002-STABLE-M8.3-BEFORE-M9-20260615-0159` |
| Doc | [reports/SITE-002-STABLE-M8.3-BEFORE-M9.md](reports/SITE-002-STABLE-M8.3-BEFORE-M9.md) |
| Scope | Pre-M9 rollback — M7.1 + M8.3 only |

---

## Project status (BZPM)

### BZPM UX REDESIGN — project banner

| Field | Value |
|-------|--------|
| **Project** | BZPM UX REDESIGN (SITE-002) |
| **Recovery status** | **CLOSED** (2026-06-28) — [SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) |
| **Production status** | **READY AFTER OPERATOR GATES** |
| **Current phase** | **PRODUCTION PREPARATION** |
| **Next phase** | **Production Development** — production promotion after operator gates (B6/B8/B1/B3) |
| **Implementation (corp pages)** | M9.14–M9.18 **IMPLEMENTED** on TEST — program implementation phase **COMPLETE** (pending operator B6/B8) |
| **Live About authority** | `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` |
| **M9.13 redesign** | **RE-ACTIVATED** on TEST (2026-06-29) — see Knowledge Map **§17** |

**Lifecycle:** Research → Corporate Pages Program → Recovery (**CLOSED**) → Production Development

**Post-recovery reconciliation:** [SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md](reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md)

### Active blockers (production path)

Recovery is **not** a blocker. Operator gates before Corporate Pages implementation:

| Blocker | Status | Affected |
|---------|--------|----------|
| **B6** | OPEN | Design Charter operator approval — all M9.13–M9.18 |
| **B8** | OPEN | PAGE-COPY formal sign-off — all M9.13–M9.18 |
| **B1** | OPEN | МО warehouse address — M9.14 · M9.16 |
| **B3** | OPEN | PLP dealer form vs `/dealers` — M9.16 |

**Operator implementation order:** M9.14 Delivery → M9.15 Payment → M9.17 Warranty → M9.16 Dealers → M9.18 Custom Manufacturing — **all IMPLEMENTED** (2026-06-28). **M9.18 checkpoint** `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01` — [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md). **Design order** (historical, unchanged): M9.13 → M9.15 → M9.14 → M9.17 → M9.16 → M9.18 — see [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md).

### Завершено

- M7.1 Launch Mode
- M8 Cleanup
- M9 Filter Profiles
- M9.5 Hub Mode
- M9.7 Images
- M9.7 Megamenu Cleanup
- Homepage Neutral Branches
- Manual UI Refinement
- M9.8.1 PDP Gallery Compact
- M9.8.2 PDP Lightbox Constraints
- M9.8.5 Products Per Page Selector
- Operator manual PLP / filter / breakpoint / CSS / Twig polish
- **Product reset + fresh 1C import**
- **Price index recovery (06D, 06F)**
- **Filter UX polish (04, 04A, 04B, 07, 08, 08A)**
- **Wishlist / Compare smart tooltips (01)**
- **Commercial Trust block (03B/03C + operator manual polish)**
- **Catalog state persistence (09A, 09B, 09C)**
- **Hub cleanup — page-intro removal (10)**
- **M9.13 About Company** — redesigned, polished, **rejected by operator**, **restored** to pre-redesign state

### Активный этап

**M9.8.9 Minor Fixes Pack #1** — remaining tasks per [BZPM-PRODUCT-ROADMAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-PRODUCT-ROADMAP-v1.md)

### Corporate Pages Program

**Status:** Implementation phase **COMPLETE on historical TEST** (2026-06-28) — Research **COMPLETE** · IA **READY** · Copy **SUBSTANTIVELY COMPLETE** (sign-off pending B8) · Design Charter **DRAFT COMPLETE / APPROVAL OPEN** (B6) · visual design **NOT OPEN**

**Corporate pages M9.14–M9.18:** Implemented and verified on historical TEST. Production parity remains **unverified**.
**Program doc:** [BZPM-CORPORATE-PAGES-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-PROGRAM-v1.md)  
**IA map:** [BZPM-CORPORATE-PAGES-IA-MAP-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-IA-MAP-v1.md)  
**Design program:** [BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-CORPORATE-PAGES-DESIGN-PROGRAM-v1.md)  
**Charters:** [charters/README.md](../../../website-factory/execution-cases/bzpm-roadmap/charters/README.md)  
**Copy standard:** [BZPM-COPY-STANDARDS-v1.md](../../../website-factory/execution-cases/bzpm-roadmap/BZPM-COPY-STANDARDS-v1.md)

| ID | Page | URL (TEST) | Research | IA | Copy | Design Charter | Design Brief |
|----|------|------------|----------|-----|------|----------------|--------------|
| M9.13 | About Company | `/about` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED · REJECTED · RESTORED** |
| M9.14 | Delivery | `/delivery` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.15 | Payment | `/payment-methods` | Complete | Mapped | Substantively complete (v1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.16 | Dealers | `/dealers` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.17 | Warranty | `/guarantee` | Complete | Mapped | Substantively complete (v1) | Draft complete | **IMPLEMENTED · QA PASSED** |
| M9.18 | Custom Manufacturing | `/custom-equipment` | Complete | Mapped | Substantively complete (v1.1) | Draft complete | **IMPLEMENTED · QA PASSED** |

**Research artifacts:** [M9.13](reports/BZPM-M9.13-ABOUT-COMPANY-FORENSIC-RESEARCH.md) · [M9.14](reports/BZPM-M9.14-DELIVERY-FORENSIC-RESEARCH.md) · [M9.15](reports/BZPM-M9.15-PAYMENT-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.16](reports/BZPM-M9.16-DEALERS-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.17](reports/BZPM-M9.17-WARRANTY-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md) · [M9.18](reports/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-FORENSIC-AND-COMMERCIAL-RESEARCH.md)

**PAGE-COPY artifacts (canonical):** [M9.13 v1.1](copy/BZPM-M9.13-ABOUT-COMPANY-PAGE-COPY-v1.1.md) · [M9.14 v1.1](copy/BZPM-M9.14-DELIVERY-PAGE-COPY-v1.1.md) · [M9.15 v1](copy/BZPM-M9.15-PAYMENT-PAGE-COPY-v1.md) · [M9.16 v1.1](copy/BZPM-M9.16-DEALERS-PAGE-COPY-v1.1.md) · [M9.17 v1](copy/BZPM-M9.17-WARRANTY-PAGE-COPY-v1.md) · [M9.18 v1.1](copy/BZPM-M9.18-CUSTOM-MANUFACTURING-PAGE-COPY-v1.1.md)

**Contacts (separate workstream):** Status **Delivered** — IA mapped for cross-links only. Evidence: [SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md](reports/SITE-002-CONTACTS-PAGE-MAIN-REDESIGN-IMPLEMENTATION.md)

**M9.14 Delivery implementation:** **IMPLEMENTED** on TEST (2026-06-28) — checkpoint `SITE-002-STABLE-LIVE-M9.14-DELIVERY-01` · [SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md](reports/SITE-002-M9.14-DELIVERY-IMPLEMENTATION.md)

**M9.15 Payment implementation:** **IMPLEMENTED** on TEST (2026-06-28) — checkpoint `SITE-002-STABLE-LIVE-M9.15-PAYMENT-01` · [SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md](reports/SITE-002-M9.15-PAYMENT-IMPLEMENTATION.md)

**M9.17 Warranty implementation:** **IMPLEMENTED** on TEST (2026-06-28) — checkpoint `SITE-002-STABLE-LIVE-M9.17-WARRANTY-01` · [SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md](reports/SITE-002-M9.17-WARRANTY-IMPLEMENTATION.md)

**M9.16 Dealers implementation:** **IMPLEMENTED** (2026-06-28) · checkpoint `SITE-002-STABLE-LIVE-M9.16-DEALERS-01` · B3 PLP reconciliation **OPEN / out of scope** · [SITE-002-M9.16-DEALERS-IMPLEMENTATION.md](reports/SITE-002-M9.16-DEALERS-IMPLEMENTATION.md)

**M9.18 Custom Manufacturing:** **IMPLEMENTED** (2026-06-28) · checkpoint `SITE-002-STABLE-LIVE-M9.18-CUSTOM-01` · [SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md](reports/SITE-002-M9.18-CUSTOM-MANUFACTURING-IMPLEMENTATION.md) · **terminal corp page** — program implementation phase **COMPLETE on TEST**

**Post-recovery completeness:** [SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md](reports/SITE-002-BZPM-POST-RECOVERY-COMPLETENESS-RECONCILIATION.md) — audit semantics reconciled 2026-06-28.

**Recovery closeout:** [SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md](reports/SITE-002-BZPM-RECOVERY-CLOSEOUT-REGISTRATION.md) — recovery **CLOSED**; production preparation active.

### Отложено (M9.8 UX Polish Pack — остаток)

M9.8.3 Homepage Hero · M9.8.4 PLP Density · M9.8.6 UltraWide · M9.8.7 EC-01 · M9.8.8 Thumbnail Rail — per roadmap

---

## Next work rule

Before next SITE-002 change:

1. Read [knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md](knowledge/SITE-002-TECHNICAL-KNOWLEDGE-MAP.md)
2. Use `SITE-002-STABLE-LIVE-LOCAL-FONTS-01` as site-wide checkpoint authority; `SITE-002-STABLE-LIVE-M9.13-ABOUT-REDESIGN-02` for About
3. For About page — read Knowledge Map **§17** + M9.13 restore/redesign/polish reports
4. For filters / sort / pagination / limit / only_with_price — read Knowledge Map **§16** + passes 09A/09B/09C
5. For filter / catalog / 1C / price / PLP — follow Knowledge Map §13 domain-specific PRE-TASK rule
6. For trust block / certificates / dealers form / category CTA — follow Knowledge Map §14 + §13 Commercial Trust PRE-TASK rule
7. Live-capture any files touched before deploy
8. **Do not** start M10 without operator charter

Rollback = Beget full backup → current live TEST → file-level pass backups.

---

## SAFE UNKNOWN

- ocStore / OpenCart exact version and release line
- Beget backup artifact location and timestamp (operator attestation only)
- M9.8.9-09C browser QA Q1–Q6 — operator interaction HITL pending
- M10 scope and authorization status
- Who populates `price2`, `price3`, `discount1c` in production workflow

---

## Security notes

| Check | Value |
|-------|-------|
| No secrets in checkpoint docs | **yes** |
| DB JSON in repo (prior baselines) | Row data only — treat as sensitive; no credentials in dumps |
