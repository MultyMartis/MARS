# SITE-002 Production Profile

**Site ID:** SITE-002  
**Project:** ЗПМ / BZPM  
**Document role:** Production environment registration — **not** connection authorization  
**Last updated:** 2026-07-07 (Run 4.212 — post-1C catalog monitor; sitemap **1377** unchanged; +0/−0 delta; 0 onboarding needs; checkpoint unchanged `SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01`)

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
| Current Production checkpoint | [baselines/SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01.md](baselines/SITE-002-STABLE-PROD-CATALOG-BRANCH-FOLLOWUP-01.md) (parent [SITE-002-STABLE-PROD-CATALOG-NEW-BRANCH-01.md](baselines/SITE-002-STABLE-PROD-CATALOG-NEW-BRANCH-01.md); brand [SITE-002-STABLE-PROD-BRAND-ZPM-01.md](baselines/SITE-002-STABLE-PROD-BRAND-ZPM-01.md)) |
| SEO readiness (Production) | **POST-1C MONITOR** (Run 4.212) — read-only sitemap delta after 1C SUCCESS; **1377** URLs unchanged; 0 category onboarding needs; reusable post-1C monitor rule · [monitor report](reports/SITE-002-PROD-POST-1C-CATALOG-ONBOARDING-MONITOR-01.md) · prior [Run 4.211](reports/SITE-002-PROD-CATALOG-BRANCH-ONBOARDING-FOLLOWUP-01.md) |
| Yandex analytics (Production) | **VERIFIED** (Run 4.189) — Metrika counter in `common/footer.twig` (masked `110***756`); Webmaster verification in `common/header.twig` (masked `13a***c77`); confirmed on live HTML (home, category, information); **OPERATOR WIP — DO NOT OVERWRITE** · [report](reports/SITE-002-PROD-YANDEX-CODES-VERIFY-01.md) |
| HTML body structure (Production) | **FIXED** (Run 4.190) — duplicate `<body>` + global preloader + `page_overlay` removed from live `header.twig`; 4-URL HTML validation PASS; Yandex blocks unchanged · [report](reports/SITE-002-PROD-HTML-BODY-DUPLICATE-FIX-01.md) |
| MARS 1C cron wrapper | **OPERATIONAL — FIRST SCHEDULED RUN VERIFIED** (Run 4.194) — Beget cron first automatic run SUCCESS 2026-07-06 08:00 Moscow; run ID `mars-20260706-080002-09436ae7`; report `mars_1c_import_2026-07-06_080007.txt`; steps `1c`+`1c_offers` PASS; lock removed; schedule `0 8 * * *` (Moscow → 12:00 Barnaul); wrapper v1.1.0; HTTP gateway; Sergey legacy **preserved**; duration 0s field **WARN only** |
| MARS 1C cron reports | **CURRENT** (Run 4.194) — `/storage/mars-tools/cron/reports/` includes first scheduled run `mars_1c_import_2026-07-06_080007.txt` plus prior manual run and status files; Run 4.184 cleanup retained policy |
| Catalog load more (Production) | **ACTIVE** (Run 4.185) — «Показать ещё» append via `initLoadMore()`; counter «Показано X из Y»; numeric pagination hidden when JS (`js-load-more`); rollback in Storage `deployments/SITE-002-PROD-LOAD-MORE-01/rollback/` |
| Neutral parent category tiles (Production) | **ACTIVE** (Run 4.195) — 9 branches on homepage/hub `zpm-cat-card`; IDs `322,331,301,326,354,358,207,80,86`; 4 new WebP images (`stellazhi`, `polki-nastennye-i-nastolnye`, `shkafy-i-lari`, `telezhki-shpilki-i-protivni`); `category_visibility.php` only; **COMPOSER_ONLY_NO_API** · [report](reports/SITE-002-PROD-NEUTRAL-PARENT-CATEGORIES-ROLLOUT-01.md) |
| Neutral category image white-bg refresh (Production) | **ACTIVE** (Run 4.196) — 3 images refreshed to white studio style (354/358/86); 331 deferred; master `1800×1200` + cache `300×300` FTP overwrite; 0 admin saves; **COMPOSER_ONLY_NO_API** · [report](reports/SITE-002-PROD-NEUTRAL-CATEGORY-IMAGES-WHITE-BG-REFRESH-01.md) |
| Polki category image fix (Production) | **ACTIVE** (Run 4.197) — ID 331 Полки настенные и настольные refreshed; master+cache FTP overwrite; stale dark cache replaced; 0 admin saves; **COMPOSER_ONLY_NO_API** · [report](reports/SITE-002-PROD-NEUTRAL-CATEGORY-IMAGE-POLKI-FIX-01.md) |
| Mail recipients architecture (Production) | **ACTIVE — ADMIN-MANAGED** (Run 4.186 discovery + Run 4.187 confirmation) — unified form handler `catalog/controller/checkout/anketa.php`; active recipients from OpenCart **`config_mail_alert_email`** (comma-separated); operator updated via admin **Additional Alert Emails**; delivery verified; order alerts share same setting; legacy hardcoded email in anketa **inactive**; no custom admin section; no code deploy · [discovery](reports/SITE-002-PROD-MAIL-RECIPIENTS-DISCOVERY-01.md) · [confirmation](reports/SITE-002-PROD-MAIL-RECIPIENTS-ADMIN-ADD-01.md) |
| Catalog default sort (Production) | `pd.name ASC` when `sort`/`order` omitted |

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
